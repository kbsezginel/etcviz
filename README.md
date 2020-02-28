# etcviz
Critter &amp; Guitari ETC video synthesizer development tools

## Installation
```bash
pip install git+https://github.com/kbsezginel/etcvis.git
```

### For development
```bash
git clone https://github.com/kbsezginel/etcvis.git
cd etcviz
pip install -e .
```

## Usage
To see usage in command line:
```bash
etcviz -h
```

### Reading mode Python file
```bash
etcviz mode_file.py
```

#### Recording images / gif
Record 30 images:
```bash
etcviz mode_file.py -r 30
```
Record gif with 50 images:
```bash
etcviz mode_file.py -r 50 -g mode.gif
```

#### Reading ETC `Scenes.csv` file (*In Progress*)
You can read ETC `Scenes.csv` file, visualize modes, add / remove or edit modes and save your changes.
```bash
etcviz mode_file.py -rs Scenes.csv
```
