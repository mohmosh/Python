# scripts/visualizations.py
"""
Task 3: Data Visualization on the Iris dataset
Creates line chart, bar chart, histogram, and scatter plot.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
CLEAN_FILE = DATA_DIR / "iris_cleaned.csv"

def main():
    # Load cleaned dataset
    df = pd.read_csv(CLEAN_FILE)
    print("Dataset loaded:", df.shape)

    # 1. Line chart (example: cumulative petal length, acts like a time series)
    df["row_index"] = range(1, len(df) + 1)
    plt.figure(figsize=(8, 5))
    plt.plot(df["row_index"], df["petal_length"], label="Petal Length", color="blue")
    plt.title("Line Chart: Petal Length across samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Petal Length (cm)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: Average petal length per species
    plt.figure(figsize=(8, 5))
    sns.barplot(x="species", y="petal_length", data=df, ci=None, palette="Set2")
    plt.title("Bar Chart: Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.tight_layout()
    plt.show()

    # 3. Histogram: Distribution of sepal length
    plt.figure(figsize=(8, 5))
    plt.hist(df["sepal_length"], bins=20, color="purple", edgecolor="black")
    plt.title("Histogram: Sepal Length Distribution")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot: Sepal length vs Petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="Set1")
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
