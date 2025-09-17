# scripts/load_explore_clean.py
"""
Load, explore and clean the Iris dataset.
Saves cleaned CSV to data/iris_cleaned.csv
Usage:
    python3 scripts/load_explore_clean.py
"""
from pathlib import Path
import sys
import pandas as pd
import numpy as np
import csv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

def find_iris_file(data_dir: Path) -> Path:
    candidates = [p for p in data_dir.iterdir() if p.is_file() and "iris" in p.name.lower()]
    if not candidates:
        print("No file matching '*iris*' found in:", data_dir)
        print("Files present:", [p.name for p in sorted(data_dir.iterdir())])
        sys.exit(1)
    # prefer common extensions
    for ext in (".csv", ".data", ".txt"):
        for p in candidates:
            if p.suffix.lower() == ext:
                return p
    # otherwise return first candidate
    return candidates[0]

def load_csv(path: Path) -> pd.DataFrame:
    # try standard read
    try:
        df = pd.read_csv(path)
        # if it loaded as a single column (bad delim), try sniffing delimiter
        if df.shape[1] == 1:
            # sniff delimiter
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                sample = f.read(2048)
            try:
                dialect = csv.Sniffer().sniff(sample)
                sep = dialect.delimiter
            except Exception:
                sep = None

            # try sensible fallbacks
            for s in (sep, ",", ";", "\t", r"\s+"):
                if s is None:
                    continue
                try:
                    df2 = pd.read_csv(path, sep=s, engine="python")
                    if df2.shape[1] > 1:
                        df = df2
                        break
                except Exception:
                    continue
        return df
    except Exception as e:
        print("pd.read_csv failed:", e)
        print("Trying without header (header=None)...")
        try:
            df = pd.read_csv(path, header=None)
            return df
        except Exception as e2:
            print("Also failed:", e2)
            sys.exit(1)

def explore(df: pd.DataFrame):
    print("\n=== FIRST 10 ROWS (head) ===")
    print(df.head(10).to_string(index=False))
    print("\n=== SHAPE ===")
    print(df.shape)
    print("\n=== DTYPES ===")
    print(df.dtypes)
    print("\n=== INFO() ===")
    df.info()
    print("\n=== NUMERIC DESCRIPTIVE STATS ===")
    print(df.select_dtypes(include=[np.number]).describe().round(4))
    print("\n=== ALL DESCRIPTIVE STATS ===")
    print(df.describe(include='all').T)
    print("\n=== MISSING VALUES PER COLUMN ===")
    missing = df.isnull().sum()
    pct = (100 * missing / len(df)).round(2)
    print(pd.DataFrame({"missing_count": missing, "missing_pct": pct}).sort_values("missing_pct", ascending=False))
    # show a few rows that contain missing values (if any)
    if df.isnull().any(axis=1).any():
        print("\n=== SAMPLE ROWS WITH MISSING VALUES ===")
        print(df[df.isnull().any(axis=1)].head().to_string(index=False))
    else:
        print("\nNo missing values found (according to pandas).")

def clean(df: pd.DataFrame) -> pd.DataFrame:
    print("\n=== CLEANING ===")
    total_missing = int(df.isnull().sum().sum())
    print("Total missing values in dataset:", total_missing)

    if total_missing > 0:
        # numeric columns -> fill with median
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        for c in num_cols:
            if df[c].isnull().any():
                med = df[c].median()
                df[c].fillna(med, inplace=True)
                print(f"Filled numeric column '{c}' with median = {med}")

        # categorical/object columns -> fill with mode (or 'Unknown' if no mode)
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        for c in cat_cols:
            if df[c].isnull().any():
                mode_series = df[c].mode()
                fill_val = mode_series.iloc[0] if not mode_series.empty else "Unknown"
                df[c].fillna(fill_val, inplace=True)
                print(f"Filled categorical column '{c}' with mode = '{fill_val}'")

        # drop any rows still containing missing values
        remaining = int(df.isnull().sum().sum())
        if remaining > 0:
            before = len(df)
            df.dropna(inplace=True)
            print(f"Dropped {before - len(df)} rows due to remaining missing values ({remaining}).")
    else:
        print("No missing values to fill.")

    # remove duplicate rows
    dup_count = int(df.duplicated().sum())
    if dup_count > 0:
        df.drop_duplicates(inplace=True)
        print(f"Dropped {dup_count} duplicate rows.")
    else:
        print("No duplicate rows found.")

    # reset index (clean)
    df.reset_index(drop=True, inplace=True)
    return df

def save_cleaned(df: pd.DataFrame, data_dir: Path):
    out = data_dir / "iris_cleaned.csv"
    df.to_csv(out, index=False)
    print(f"Saved cleaned dataset to: {out}")

def main():
    if not DATA_DIR.exists():
        print("Data directory not found:", DATA_DIR)
        sys.exit(1)

    path = find_iris_file(DATA_DIR)
    print("Using file:", path)
    df = load_csv(path)
    explore(df)
    df_clean = clean(df.copy())
    save_cleaned(df_clean, DATA_DIR)
    print("\nDone.")

if __name__ == "__main__":
    main()
PY
