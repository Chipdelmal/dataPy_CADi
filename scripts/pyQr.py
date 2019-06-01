# -*- coding: utf-8 -*-

###############################################################################
# "qrCode" example
###############################################################################
#  Objectives:
#   To create and export a qr code from jupyter
#  Source:
#   https://github.com/mnooner256/pyqrcode
#   https://pypi.org/project/PyQRCode/
#   https://github.com/mnooner256/pyqrcode
#   https://pythonhosted.org/PyQRCode/
###############################################################################

# Load library
import pyqrcode

# Creating and saving the QR code for a URL
url = pyqrcode.create('https://github.com/Chipdelmal')
url.svg('./images/qrURL.svg', scale=15, module_color="#7D007D")
url.png(
    './images/qrURL.png',
    scale=20,
    module_color=(0, 0, 0, 0),
    background=(0xff, 0xff, 0xff)
)


# The error parameter sets the error correction level of the code. Each level
#   has an associated name given by a letter: L, M, Q, or H; each level can
#   correct up to 7, 15, 25, or 30 percent of the data respectively.
# The version parameter specifies the size and data capacity of the code.
#   Versions are any integer between 1 and 40, where version 1 is the smallest
#   QR code, and version 40 is the largest.
# Mode parameter sets how the contents will be encoded. As mentioned above,
#   three of the five possible encodings have been written.
url = pyqrcode.create(
    'https://github.com/Chipdelmal',
    error="H",
    version=10
)
url.png(
    './images/qrURLH.png',
    scale=20,
    module_color=(0, 0, 0, 0),
    background=(0xff, 0xff, 0xff)
)
