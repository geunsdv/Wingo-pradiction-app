import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page setup
st.set_page_config(page_title="Wingo Prediction App")

# 2. Title and intro
st.title("🔮 Wingo Prediction App")
st.write("Welcome! This app helps you analyze and predict Wingo results.")
st.success("✅ Streamlit is working!")

# 3. Input history section
st.header("📥 Enter Previous Wingo Results")
history_input = st.text_area(
    'Paste recent results (format: color,number on each line)',
    height=200,
    placeholder="Green,4\nRed,8\nGreen,2\nRed,9\n..."
)

# 4. Data processing and prediction
if history_input:
    try:
        # Split lines and convert into DataFrame
        lines = history_input.strip().split("\n")
        data = [line.strip().split(",") for line in lines if "," in line]
        df = pd.DataFrame(data, columns=["Color", "Number"])
        df["Number"] = pd.to_numeric(df["Number"], errors='coerce')
        df.dropna(inplace=True)

        st.subheader("📊 Last 10 Results")
        st.dataframe(df.tail(10))

        # Frequency count
        color_counts = df["Color"].value_counts()
        number_counts = df["Number"].value_counts().sort_index()

        # Prediction logic (simple pattern-based)
        most_common_color = color_counts.idxmax()
        most_common_number = number_counts.idxmax()

        st.subheader("🔎 Prediction")
        st.write(f"🟢 Most frequent color: **{most_common_color}**")
        st.write(f"#️⃣ Most frequent number: **{most_common_number}**")
        st.success(f"📌 Next prediction: **{most_common_color}, {most_common_number}**")

        # Visualization
        st.subheader("📈 Color Frequency Chart")
        fig, ax = plt.subplots()
        color_counts.plot(kind='bar', color=['green', 'red', 'blue'], ax=ax)
        plt.title("Color Frequency")
        st.pyplot(fig)

    except Exception as e:
        st.error("❌ Error processing input. Please follow format correctly.")
        st.exception(e)
