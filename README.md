# Tools

A collection of useful tools and utilities for everyday use.

## Projects

### [Audio](audio/)
Audio manipulation tools for processing sound files.

#### Union Audio
Combine multiple audio files into a single file using `pydub`.

**Features:**
- Merges multiple audio files sequentially
- Exports to MP3 format
- Supports any audio format that pydub can read

**Usage:**
```python
from union_audio import unir_audios

audio_files = ["1.mp3", "2.mp3", "3.mp3"]
unir_audios(audio_files, "output.mp3")
```

**Dependencies:** `pydub`

---

### [Excel](excel/)
Excel spreadsheet manipulation utilities.

#### Random Excel
Shuffle rows in an Excel file and save to a new file.

**Features:**
- Reads Excel files using pandas
- Randomly shuffles rows with reproducible results
- Exports shuffled data to a new Excel file

**Usage:**
```python
import pandas as pd
import random

df = pd.read_excel('input.xlsx')
shuffled = df.sample(frac=1, random_state=42)
shuffled.to_excel('output.xlsx', index=False)
```

**Dependencies:** `pandas`, `openpyxl`

---

### [Dados](dados/)
An interactive web application to explore probability and statistics with dice rolling.

**Features:**
- Roll 1 to 100 dice simultaneously
- Real-time probability calculations
- Visual representation of dice results
- Statistics tracking (wins, loss rate)
- Responsive dark theme UI
- Animated dice rolling effect

**How it works:**
- Select the number of dice to roll
- Click the "Tirar dados" button to roll
- The app calculates the probability of all dice matching
- Track statistics across multiple rolls
- See visual feedback for matching vs non-matching results

**Probability Formula:**
For `n` dice, the probability that all show the same number is: `P = (1/6)^(n-1)`

**Open in browser:** Open `dados/index.html` in your web browser.

---

## Installation

Most tools require Python 3.6+

```bash
# For audio tools
pip install pydub

# For Excel tools
pip install pandas openpyxl
```

## License

Feel free to use and modify these tools as needed.

