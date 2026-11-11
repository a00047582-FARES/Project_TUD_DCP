import pandas as pd

data = {
    "Date": ["2026-11-07", "2026-11-08", "2026-11-09", "2026-11-10", "2026-11-11"],
    "Water (ml)": [2100, 1800, 2400, 2000, 2600],
    "Overall Feeling (1-10)": [7, 5, 8, 6, 9],
    "Physical Activity (hours)": [1.0, 0.0, 1.5, 0.5, 1.5],
    "Sleep (hours)": [7.5, 6.0, 8.0, 6.5, 8.0],  # the 5th column
}

df = pd.DataFrame(data)

print(df.to_string(index=False))

# Work out how wide each column needs to be
widths = [max(len(str(v)) for v in [col] + df[col].astype(str).tolist()) for col in df.columns]

# Build aligned rows (header + data)
rows = [list(df.columns)] + df.astype(str).values.tolist()
lines = ["| ".join(v.ljust(w) for v, w in zip(row, widths)) for row in rows]

# Save as a neatly aligned CSV
with open("wellness_dataset.csv", "w") as f:
    f.write("\n".join(lines))

print("\nSaved as wellness_dataset.csv")