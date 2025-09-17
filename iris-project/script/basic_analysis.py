# scripts/basic_analysis.py
"""
Task 2: Basic Data Analysis on the Iris dataset
"""

import pandas as pd
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
CLEAN_FILE = DATA_DIR / "iris_cleaned.csv"

def main():
    # Load cleaned dataset
    df = pd.read_csv(CLEAN_FILE)
    print("=== Dataset Loaded ===")
    print(df.head(), "\n")

    # 1. Basic statistics of numerical columns
    print("=== Basic Statistics (Numerical Columns) ===")
    print(df.describe().T, "\n")

    # 2. Group by species (categorical column) and compute mean of numerical columns
    if "species" in df.columns:
        print("=== Mean of Numerical Columns by Species ===")
        print(df.groupby("species").mean(numeric_only=True), "\n")
    else:
        print("No 'species' column found in dataset. Try grouping by another categorical column.\n")

    # 3. Interesting patterns (example findings)
    print("=== Observations ===")
    print("- Use the means above to compare petal/sepal size across species.")
    print("- Look for which species has the largest/smallest average petal length.")
    print("- Check the spread (std) in describe() for which measurement varies most.")

if __name__ == "__main__":
    main()
