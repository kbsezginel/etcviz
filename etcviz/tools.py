"""
ETC tools.
"""
import os
import csv
import shutil
import imageio


def images_to_gif(img_dir, gif_file):
    """
    Convert images in a given directory to a gif file using imageio.

    Parameters
    ----------
    img_dir: str
        Path to the directory containing image files.
    gif_file: str
        Path to the gif file.

    Returns
    -------
    None

    """
    filenames = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if os.path.splitext(f)[1] == '.jpg']
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(gif_file, images)


def read_csv(filename):
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        rows = []
        for row in csvreader:
            rows.append(row)
    return rows


def write_csv(filename, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            csvwriter.writerow(row)
