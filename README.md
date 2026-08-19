# contributionGraphArts 🎨

Turn your GitHub contribution graph into pixel art. This repo is Python-based and contains a separate script for each year (`hack2017.py` → `hack2026.py`) that generates a year's worth of backdated commits shaped into text/patterns on your GitHub profile's contribution heatmap.

## How it works

Each `hackYYYY.py` script:

1. Encodes a design as a **7×51 matrix** (7 days a week × 51 weeks), where `1` marks a cell that should be "lit up" on the contribution graph and `0` leaves it blank.
2. Walks through the matrix day by day, and for every `1` cell, makes several small changes to placeholder files (`pythonFileText.py`, `htmlFileText.html`, `cssFileText.css`, `jsFileText.js`, `qtCppFileText.cpp`).
3. Stages and commits those changes with a **backdated commit date** (`git commit --date="..."`) so the commit lands on the correct day of that year.
4. Repeats this for every lit-up cell in the grid, effectively "drawing" on the calendar.
5. Pushes everything to `origin main` once the whole pattern has been committed.

The result is a year of green squares on your GitHub contribution graph arranged into a custom design instead of random activity.

## Usage

1. Clone this repo (or create a fresh empty repo and copy a `hackYYYY.py` script + placeholder files into it).
2. Open the script for the year you want and edit the `dateArray` matrix to spell out the text/pattern you want (each row = a day of the week, each column = a week of the year; `1` = filled, `0` = empty).
3. Update the starting date at the top of the script (e.g. `date_2026 = datetime(2026, 1, 4)`) to match the first Sunday/Monday of the target year, matching how GitHub lays out its contribution graph.
4. Set your `git` identity if needed:
   ```bash
   git config user.name "Your Name"
   git config user.email "you@example.com"
   ```
5. Run the script:
   ```bash
   python hack2026.py
   ```
   The script will generate the commits locally and then run `git push -u origin main` to push them to your remote.

> ⚠️ **Note:** This generates a large number of backdated, low-content commits purely to shape your contribution graph. It's a fun visual hack for your GitHub profile, not a reflection of real project activity — use it on a dedicated/side repo rather than a repo with genuine collaborators or contribution history you care about keeping meaningful.

## Requirements

- Python 3
- `numpy`
- `git` installed and configured, with push access to the target remote

```bash
pip install numpy
```

## Customizing your own design

To design your own pattern:
- Sketch it out on a 7-row × 51-column grid (one row per weekday, one column per week of the year).
- Mark the squares you want lit up as `1` and everything else as `0`.
- Paste the grid into the `dateArray` variable in the script for the year you're targeting.
---
## Author

**Mubashir Iqbal**
AI Researcher | System Engineer | Qt C++ Software & Web Engineer
[github.com/Mubshr07](https://github.com/Mubshr07)
