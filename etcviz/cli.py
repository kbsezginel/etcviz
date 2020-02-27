"""
ETC command line interface.
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="""
    ============================== o   o ==
    ███████╗████████╗ ██████╗       \ /
    ██╔════╝╚══██╔══╝██╔════╝  ╔═════╩════╗
    █████╗     ██║   ██║       ║ ╦  ╦╦╔═╗ ║
    ██╔══╝     ██║   ██║       ║ ╚╗╔╝║╔═╝ ║
    ███████╗   ██║   ╚██████╗  ║  ╚╝ ╩╚═╝ ║
    ╚══════╝   ╚═╝    ╚═════╝  ╚══════════╝
    Critter & Guitari ETC Video Synthesizer
    Mode Development Tools
    =======================================
        """,
        epilog="""
    Example:
    > etcviz ETC_Mode
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Positional arguments
    parser.add_argument('mode', type=str,
                        help="Filename or directory of the ETC mode")

    # Optional arguments
    parser.add_argument('-r', '--record', type=int,
                        help="Record out to image sequence for ffmpeg")
    parser.add_argument('-k', '--knobs', default=[0.5, 0.5, 0.5, 0.2, 0.5],
                        type=float, metavar='', nargs=5,
                        help="ETC knob settings (ex: 0.5 0.5 0.5 0.2 0.5)")
    parser.add_argument('-g', '--gif', type=str,
                        help="Save image sequence as gif file")
    args = parser.parse_args()
