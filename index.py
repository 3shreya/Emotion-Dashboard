import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set page settings
st.set_page_config(page_title="Emotion Dashboard", layout="wide")
st.title("🎵 Emotion Dashboard")
st.markdown("Analyze your favorite songs to understand your mood trends.")

# Define possible moods
mood_labels = ['Happy', 'Sad', 'Calm', 'Energetic', 'Angry', 'Romantic']

# File uploader
uploaded_file = st.file_uploader("📁 Upload a CSV file with 'Song' and 'Artist' columns", type=['csv'])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        if 'Song' not in df.columns or 'Artist' not in df.columns:
            st.error("⚠️ CSV must contain 'Song' and 'Artist' columns.")
        else:
            # Simulate mood detection (replace this with real model later)
            df['Detected Mood'] = np.random.choice(mood_labels, size=len(df))

            # Show uploaded data
            st.subheader("🎧 Uploaded Songs")
            st.dataframe(df)

            # Mood count summary
            mood_counts = df['Detected Mood'].value_counts()

            # --- Mood Distribution (Bar Chart) ---
            st.subheader("📊 Mood Distribution")
            bar_fig = px.bar(
                mood_counts,
                x=mood_counts.index,
                y=mood_counts.values,
                labels={'x': 'Mood', 'y': 'Count'},
                color=mood_counts.index,
                title="Distribution of Detected Moods"
            )
            st.plotly_chart(bar_fig, use_container_width=True)

            # --- Mood Pie Chart ---
            pie_fig = px.pie(
                names=mood_counts.index,
                values=mood_counts.values,
                title="Mood Composition"
            )
            st.plotly_chart(pie_fig, use_container_width=True)

            # --- Heatmap of Mood vs Songs ---
            st.subheader("🧠 Emotion Heatmap")
            heatmap_data = pd.crosstab(df['Song'], df['Detected Mood'])

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt='d', linewidths=0.5, ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

            st.success("✅ Emotion analysis complete (simulated). Replace logic with a model or API to go deeper.")
    
    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

else:
    st.info("Upload a CSV to get started!")

