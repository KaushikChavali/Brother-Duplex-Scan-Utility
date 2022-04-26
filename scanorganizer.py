#!/usr/bin/env/python3

"""
The tool helps rearrange documents scanned from a Brother multi-function printer
where the ADF does not support Duplex (two-sided) scan. In such cases, a duplex
scan requires the user to manually scan the front side of a page in one batch
and the backside in another. The Brother utility assigns sequential naming to
files. For example, a 10-page duplex document has a file numbering of 1-10 for
the front side and 11-20 for the backside. The tool corrects the ordering so
that the files are ordered [1:20, 2:19, 3:18, 4:17 ..., 10-11].
"""

import argparse
from posixpath import dirname
import img2pdf
import os, os.path
import sys

# Define base file name and extension
BASE_FILENAME = 'Scan'
NEW_FILENAME = 'Page'
FILE_EXTENSION = '.png'

# Create the parser
parser = argparse.ArgumentParser(description="Sort scanned documents.")

# Add the arguments
parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='the path to scanned pages')

parser.add_argument("--pdf", default=False, action="store_true",
                    help="Combines the PNG files into a PDF file.")

# Execute the parse_args() method
args = parser.parse_args()

# Assign the path
dir = args.Path

# Check if the directory exists
if not os.path.isdir(dir):
    print('The path specified does not exist')
    sys.exit()

# Get the number of files in the folder
no_of_files = len([f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and f[0] != '.'])
print(no_of_files, "files processed.")

# Correct file ordering and naminga
for i in range(int(no_of_files/2)):
    # Get the front and back page number pairs
    front_page_number = i;
    back_page_number = no_of_files - i - 1;

    # Build the input filenames
    filename_front = BASE_FILENAME + ' ' + str(front_page_number) + FILE_EXTENSION
    filename_back = BASE_FILENAME + ' ' + str(back_page_number) + FILE_EXTENSION

    # The initial file has no numbering as per Apple Scan utility
    if i == 0:
        filename_front = BASE_FILENAME + FILE_EXTENSION

    # Build absoulute path name
    filename_front = os.path.join(dir, filename_front)
    filename_back = os.path.join(dir, filename_back)

    # Assign new names and correct ordering
    new_filename_front = NEW_FILENAME + str((i * 2) + 1) + FILE_EXTENSION
    new_filename_back = NEW_FILENAME + str((i * 2) + 2) + FILE_EXTENSION

    # Build absoulute path name
    new_filename_front = os.path.join(dir, new_filename_front)
    new_filename_back = os.path.join(dir, new_filename_back)

    # Rename files and correct ordering
    os.rename(filename_front, new_filename_front)
    os.rename(filename_back, new_filename_back)

# Convert the PNG files into a PDF.
if args.pdf:
    imgs = []
    for fname in sorted(os.listdir(dir)):
        if not fname.endswith(".png"):
            continue
        path = os.path.join(dir, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)

    with open(dir + "/out.pdf","wb") as f:
        f.write(img2pdf.convert(imgs))
    print("Scanned document ordered and PDF generated.")
else:
    print("Scanned document ordered.")
