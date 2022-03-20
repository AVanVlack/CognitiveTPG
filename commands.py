"""
Hex commands for TPG printer

Author: Drew VanVlack

"""

# Printer Actions

CUT_FULL = b"\x1B\x69"
CUT_PARTIAL = b"\x1B\x6D"
CLEAR_PRINTER = b"\x10"
RESET_PRINTER = b"\x1b\x40"
GENERATE_TONE = b"\x1b\x07"
INITIALIZE = b"\x1b\x40"

PRINT_TEST = b"\x1F\x74"

# Print and Feed
PRINT_FEED = b"\x0A"
PRINT_RETURN = b"\x0D"
FEED_LINE = b"\x14"  # 14 n
FEED_DOT = b"\x15"  # 15 n
PRINT_ONE = b"\x17"

# Posistioning
JUSTIFY = b"\x1B\x61"
TAB = b"\x09"

# Text characteristics
DOUBLE_WIDE = b"\x12"
SINGLE_WIDE = b"\x13"
ROTATE_90 = b"\x1B\x12"
CHARACTER_SIZE = b"\x1D\x21"  # 1D 21 n
PRINT_MODE = b"\x1B\x21"  # 1B 21 n
UNDERLINE = b"\x1B\x2D"  # 1B 2D n
EMPHASIZE = b"\x1B\x45"  # 1B 45 n
INVERT = b"\x1D\x42"  # 1D 72 n
SMOOTH = b"\x1D\x62"  # 1D 62 n
FONT = b"\x1D\xF1\x01"  # 1D F1 01 FSID
# Barcodes
# - QR Code
PRINT_QR = b"\x1D\x28\x6B\x03\x00\x31\x51\x30"  # 1D 28 6B 03 00 31 51 30
SIZE_QR = b"\x1D\x28\x6B\x03\x00\x31\x43"
MODEL_QR = b"\x1D\x28\x6B\x04\x00\x31\x41\x32\x00"  # 1D 28 6B 04 00 31 41 n1 n2
QR_SEP = b"\x31\x50\x30"
ERROR_QR = b"\x1D\x28\x6B\x03\x00\x31\x45"
STORE_QR = b"\x1D\x28\x6B"  # 1D 28 6B qL qH 31 50 30 f1….fk

# - 2D Codes
HRI_POS = b"\x1D\x48"  # 1D 48 n --- n = 0-3
HRI_PITCH = b"\x1D\x66"  # 1D 66 n --- n = 0,1
BAR_HEIGHT = b"\x1D\x68"  # 1D 68 n --- n = 1-255
PRINT_BARCODE = b"\x1D\x6B"
