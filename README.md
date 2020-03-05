# etcviz
Critter &amp; Guitari ETC video synthesizer development tools

```
============================== o   o ==
███████╗████████╗ ██████╗       \ /
██╔════╝╚══██╔══╝██╔════╝  ╔═════╩════╗
█████╗     ██║   ██║       ║ ╦  ╦╦╔═╗ ║
██╔══╝     ██║   ██║       ║ ╚╗╔╝║╔═╝ ║
███████╗   ██║   ╚██████╗  ║  ╚╝ ╩╚═╝ ║
╚══════╝   ╚═╝    ╚═════╝  ╚══════════╝
Critter & Guitari ETC Video Synthesizer
Development and Visualization Tools
=======================================
```

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

## [ETC Manual](https://critterandguitari.github.io/ETC_Manual/)

## Usage
To see usage in command line:
```bash
etcviz -h
```

### Visualizing mode(s)
In ETC, modes are stored as separate directories each containing a `main.py` file.
`etcviz` uses the same structure for reading mode files.
You can either give a single mode directory:
```bash
etcviz Modes/my_mode
```
which will read this mode and display it.

Alternatively you can provide the whole `Modes` directory which loads all modes and lets you switch between different modes with left and right arrow keys:
```bash
etcviz Modes
```
### Changing knobs
ETC has 5 knobs which can control different settings for each mode.
You can emulate knob value changes by pressing a number between 1 - 5 and pressing up/down arrow key. For example if you press key `1` and hold up arrow key this will increase `knob1` value maxing at `1.0`.

### Saving mode(s)
As you develop your mode and play around with different knob settings you might want to save the mode with current settings. If you press `a` key while display is on, this will save the current settings internally (almost like the *Scene Save* button on ETC). You can keep adding more modes this way. Once you want to save these to a file press `w` key. This will write all saved mode settings to `Scenes.csv` file in the current directory.

> #### `Scenes.csv`
> This file can be found in `ETC/Scenes/Scenes.csv` and it is used as to store settings for saved scenes/modes. You can navigate between different saved scenes using the  You can create your own `Scenes.csv` file using `etcviz` as described above.

### Visualizing scenes
You can read `Scenes.csv` file and visualize them by proving the `Modes` directory and scenes file:
```bash
etcviz Modes --scenes Scenes/Scenes.csv
```
You can switch between scenes with left and right arrow keys.
If you would like to update your `Scenes.csv` file you can edit the scenes (e.g. knob settings), press the `a` key to add the scene(s) you want and press `w` to write them to file.

### Recording images / gif
Record 30 images:
```bash
etcviz test_mode -r 30
```
Record gif with 50 images:
```bash
etcviz test_mode -r 50 -g my_mode.gif
```
