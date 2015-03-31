# Auto QR Code Generation

The purpose of this script is to automate the generation of qr codes given a list.

#### Dependendies Required that are normally not included in the initial python setup:
* csv (for reading csv files)
* pyqrcode (for creating qr codes)
* qrtools (for decoding qr codes)

#### How to use

place csv file/s beside in the same directory as the script then run it with:

    python qr_generate.py
The csv files should have their data for qr code conversion in the first column only.

