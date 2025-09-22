import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ==========================
# Load the data
# ==========================
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    # Extract publication year
    df["year"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.year
    return df

df = load_data()

# ==========================
# Streamlit Layout
# ==========================
st.title("📊 CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers dataset")

# Sidebar filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["year"].min() if df["year"].notnull().any() else 2019),
    int(df["year"].max() if df["year"].notnull().any() else 2023),
    (2020, 2021)
)

# Filter dataset by year
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# ==========================
# Visualizations
# ==========================
st.subheader("📈 Publications Over Time")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

st.subheader("🏛️ Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
st.bar_chart(top_journals)

st.subheader("☁️ Word Cloud of Paper Titles")
titles = " ".join(filtered_df["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.subheader("🔍 Sample Data")
st.write(filtered_df.head(20))
