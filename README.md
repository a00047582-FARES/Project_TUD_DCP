 Wellness Dataset

A small Python script that builds a daily wellness dataset and saves it as a neatly aligned CSV file. The dataset is meant to be edited and extended over time.

## Dataset

Each row is one day. The script currently tracks these columns:

| Column | Description | Example unit / scale |
|---|---|---|
| Date | Day of the entry (typed in manually) | YYYY-MM-DD |
| Water (ml) | Water drunk during the day | Milliliters |
| Overall Feeling | Self-rated mood for the day | Numeric scale (e.g. 1-10) |
| Physical Activity (hours) | Time spent exercising | Hours |
| Sleep (hours) | Hours slept the night before | Hours |

The number of rows, the date range, the value ranges, the scales, and even the columns themselves are not fixed. Add, remove, or rename anything as the project changes.

## Requirements

- Python 3.8 or newer
- pandas

Install pandas with:

```
pip install pandas
```

## How to run

1. Open a terminal in the folder that contains `wellness_dataset.py`.
2. Run:

```
python wellness_dataset.py
```

## Output

- The table is printed in the terminal.
- A file called `wellness_dataset.csv` is created in the same folder.

The CSV is padded with spaces so the columns line up when opened in a text editor such as VS Code or Notepad.

## Editing the data

All the data lives in the `data` dictionary at the top of the script.

- **Add or change rows:** add or edit values in each column's list. Every list must have the same number of items.
- **Add a column:** add a new key with its list of values.
- **Remove or rename a column:** delete or rename its key.
- **Dates:** they are typed in by hand, so write each one in whatever format you prefer.

## Notes

- The data is sample data, written to look realistic.
- If you open the CSV in Excel and the numbers behave like text, remove the padding by replacing the save section of the script with `df.to_csv("wellness_dataset.csv", index=False)`.
