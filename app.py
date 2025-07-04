import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page setup
st.set_page_config(page_title="Wingo Prediction App", layout="wide")

# 2. Title and intro
st.title("🔮 Wingo Prediction App")
st.write("Welcome! This app helps you analyze and predict the next Wingo result.")
st.success("Streamlit is working!")

# 3. Input history section
st.header("📥 Enter Previous Wingo Results")
history_input = st.text_area(
    'Paste recent results (format: color,number on each line)',
    height=200,
    placeholder="Green,4\nRed,8\nGreen,2\nRed,9\nGreen,7"
)

# 4. Parse user input
try:
    lines = history_input.strip().split("\n")
    results = []
    for line in lines:
        color, number = line.strip().split(",")
        results.append((color.lower(), int(number)))
except Exception as e:
     # Count color and number frequencies
    color_counts = {"green": 0, "red": 0}
    number_counts = [0] * 10

    for color, num in results:
        if color in color_counts:
            color_counts[color] += 1
        if 0 <= num <= 9:
            number_counts[num] += 1

    # Predict most frequent values
    predicted_color = max(color_counts, key=color_counts.get)
    predicted_number = number_counts.index(max(number_counts))

    # Show prediction
    st.subheader("🎯 Prediction:")
    st.markdown(f"**Color:** {predicted_color.capitalize()}")
    st.markdown(f"**Number:** {predicted_number}")

    # Show color frequency chart
    color_df = pd.DataFrame.from_dict(color_counts, orient='index', columns=["Count"])
    st.subheader("🎨 Color Frequency")
    st.bar_chart(color_df)

    # Show number frequency chart
    number_df = pd.DataFrame({
        "Number": list(range(10)),
        "Count": number_counts
    })
    st.subheader("🔢 Number Frequency")
    st.bar_chart(number_df.set_index("Number"))
else:
    st.info("Enter valid Wingo results to get predictions.") 
    st.error(f"❌ Error parsing input: {e}")
    results = []

# 5. Prediction logic
if results:
    # Count frequencies
    color_counts = {"green": 0, "red": 0}
    number_counts = [0] * 10  # index = number 0–9

    for color, num in results:
        if color in color_counts:
            color_counts[color] += 1
        if 0 <= num <= 9:
            number_counts[num] += 1

    # Choose most frequent
    predicted_color = max(color_counts, key=color_counts.get)
    predicted_number = number_counts.index(max(number_counts))

    # 6. Display prediction
    st.subheader("🎯 Prediction:")
    st.markdown(f"**Color:** {predicted_color.capitalize()}")
    st.markdown(f"**Number:** {predicted_number}")

    # 7. Show frequency charts
    # Color bar chart
    color_df = pd.DataFrame.from_dict(
        color_counts,
        orient="index",
        columns=["Count"]
    )
    st.subheader("🎨 Color Frequency")
    st.bar_chart(color_df)

    # Number bar chart
    number_df = pd.DataFrame({
        "Number": list(range(10)),
        "Count": number_counts
    })
    st.subheader("🔢 Number Frequency")
    st.bar_chart(number_df.set_index("Number"))
else:
    st.info("Enter valid Wingo results to see predictions.")
