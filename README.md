# Messy Python Code Improvement

I took a deliberately messy Python script and improved it with AI assistance, keeping the output exactly the same.
Part of my portfolio: https://github.com/Naman-Chandak

## Files

| File | Purpose |
|---|---|
| `messy.py` | The original script: one-letter variable names, no functions, repeated loops, magic numbers. |
| `clean.py` | The improved version, same behaviour. |

## What the script does

It takes four students' marks and prints each student's total, average and grade, then the class average, the topper, how many passed and the lowest scorer.

## What was wrong with the messy version

| Problem | Example in `messy.py` |
|---|---|
| Unclear names | `a`, `x`, `y`, `z`, `m`, `mn`, `c`, `l` |
| Everything in one block | No functions at all |
| Repeated loops | Three separate loops over the same list to find the topper, pass count and lowest |
| Magic numbers | `90`, `75`, `60`, `50` and `1000` with no explanation |
| Fragile logic | The lowest score started at `1000`, which only works if every score is below that |
| No explanation | No comments or docstrings |
| Data mixed with logic | Student data is a list of lists indexed by position (`i[1]`, `i[2]`) |

## What I changed in `clean.py`

| Improvement | How |
|---|---|
| Clear names | `students`, `average`, `topper`, `PASS_MARK` |
| One job per function | `calculate_average`, `assign_grade`, `build_results`, `count_passed`, `print_report` |
| Named constants | `PASS_MARK` and `GRADE_BOUNDARIES` can be changed in one place |
| Data as dictionaries | `student["name"]` instead of `i[0]` |
| Less repetition | `max()` and `min()` replace hand-written loops |
| Docstrings | Each function says what it does |
| Entry point | `if __name__ == "__main__"` so the file can also be imported |

## How to run

```bash
python messy.py
python clean.py
```

Both print the same report:

```
Aarav - 255 - 85.0 - B
Diya - 195 - 65.0 - C
Kabir - 273 - 91.0 - A
Meera - 157 - 52.33 - D
class avg 73.33
topper Kabir 91.0
passed 4 out of 4
lowest Meera 52.33
```

To check they match yourself:

```bash
python messy.py > a.txt
python clean.py > b.txt
diff a.txt b.txt        # on Windows: fc a.txt b.txt
```

## What I learned

Code that works is not always code that is easy to read. Good names and small functions make the same logic much easier to change later.
