# Brother Duplex Scan Utility for MacOS
Helps organize duplex scan results captured by Brother (probably works for other brands too) Automatic document feeder (ADF) reader on MacOS. Works with the PNG file format.

It aims to reduce paper wastage and save the environment by encouraging duplex printing and seamless scanning using ADF.

![Scanner MacOS](res/scanner.png?raw=true)

# Usage

1. Scan the front pages using the ADF.
2. Flip the document and scan the back pages.
3. For a 5-page duplex document, the files are named ```Scan - Scan 9```. Make sure all the scanned documents are in same folder.
4. Execute the following command to corretly organize the scanned pages where path is the input directory of the document.
```
scanorganizer.py [-h] path [--pdf]
```
5. The results are stored in the same directory. It includes ordered PNG files and a output PDF file.

# Parameters

| Name | Argument | Description |
| ---- | -------- | --- |
| `--pdf` |       | Convert the PNG files into a PDF |
| `-h` |          | Print a help message and exit |

# Dependencies

* img2pdf