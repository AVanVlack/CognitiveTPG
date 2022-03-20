'''
Prints to a TPG Network Recipt Printer

Author: Drew VanVlack
Date:   1/25/2022
'''

import socket
import commands as c
import image as im


class TPG:
    """
    Builds and sends commands to printer
    process_type:string - buffer, direct
    """

    def __init__(self, address, port=9001, process_type="buffer", dev=False):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.process_type = process_type
        self.address = address
        self.port = port
        self.payload = b""
        self.dev = dev
        try:
            self.connection.connect(
                (self.address, self.port))
        except:
            print("Error with the connection")

    def init(self):
        self.append(c.INITIALIZE)

    def text(self, data, lf=False):
        """Print text"""
        self.append(bytearray(data, 'ascii'))
        if (lf):
            self.append(c.PRINT_FEED)

    def text_size(self, size):
        """
        Text Size: 1-8
        """
        self.append(c.CHARACTER_SIZE + bytes([size]))

    def underline(self, line=True):
        """
        Underlines text for one line
        """
        self.append(c.UNDERLINE + bytes([line]))

    def invert(self, invert=True):
        """Inverts the image"""
        self.append(c.INVERT + bytes([invert]))

    def bold(self, bold=True):
        """
        Bold text
        """
        self.append(c.EMPHASIZE + bytes([bold]))

    def text_smoothing(self, state=True):
        self.append(c.SMOOTH + bytes([state]))

    def cut(self, size="full"):
        """Cut paper command: Full, Partial"""
        if size == 'partial':
            self.append(c.CUT_FULL)
        else:
            self.append(c.CUT_FULL)

    def clear(self):
        """Clears the Printer"""
        pass

    def reset(self):
        """Resets the Printer"""
        pass

    def set_font(self, font):
        self.append(c.FONT + bytes([font]))

    def test(self):
        """Prints text recipe"""
        self.print_bytes(c.PRINT_TEST)

    def append(self, command):
        """Appends or Prints the command depending on the process type"""
        if self.process_type == "store":
            self.payload += command
        else:
            self.print_bytes(command)

    def print_bytes(self, command):
        """Sends raw data to printer"""
        self.connection.send(command)
        if self.dev:
            print(command.hex())

    def print(self):
        """Prints and clears soft buffer"""
        self.print_bytes(self.payload)
        self.payload = b""

    def justification(self, position):
        """
        Justification: left, center, right
        """
        pos = ["left", "center", "right"].index(position)
        self.append(c.JUSTIFY + bytes([pos]))

    def tab(self, number=1):
        """
        Tabs to a given tab
        """
        for i in range(number):
            self.append(c.TAB)

    def music(self):
        """Plays a tone"""
        self.append(c.GENERATE_TONE)

    def close(self):
        """Closes the connection"""
        self.connection.close()

    def barcode_qr(self, data, size=3, error_correction=1):
        """
        Prints a QR code
        Size: 1-10
        Error Correction: 1-4 1=low 7%, 2=medium 15%, 3=quality 25%, 4=high 30%
        """
        byte_data = bytearray(data, 'ascii')
        data_len = len(byte_data) + 3
        data_ql = int(data_len % 256).to_bytes(1, 'big')
        data_qh = int(data_len / 256).to_bytes(1, 'big')
        print('h', data_ql.hex())

        qr_store = c.STORE_QR + data_ql + data_qh + c.QR_SEP + byte_data
        qr_size = c.SIZE_QR + bytes([size])
        qr_error = c.ERROR_QR + bytes([error_correction + 29])

        self.append(c.MODEL_QR)
        self.append(qr_size)
        self.append(qr_error)
        self.append(qr_store)
        self.append(c.PRINT_QR)

    def barcode(self, data, code, hri_posistion=0, hri_pitch=0, height=216):
        """
        Prints a barcode
        Type: 1 UPC-A, 2 UPC-E, 3 EAN13, 4 EAN8, 5 CODE39, 6 ITF, 7 CODEBAR
                8  CODE93, 9 CODE128, 10 CODE128 AC, 11 PDF417, 13 Code EAN 128 AC, 14 GS1
        HRI Position: 0-3
        HRI Pitch: 0, 1
        Height: 1-255
        """
        byte_data = bytearray(data, 'ascii')
        data_len = len(byte_data)

        print_barcode = c.PRINT_BARCODE + \
            bytes([code + 64]) + data_len.to_bytes(1, 'big') + byte_data

        self.append(c.HRI_POS + bytes([hri_posistion]))
        self.append(c.HRI_PITCH + bytes([hri_pitch]))
        self.append(c.BAR_HEIGHT + bytes([height]))
        self.append(print_barcode)

    def feed(self, amount, size="line"):
        """
        Feed n amount of lines or n amount of dots
        By: line, dot
        """
        if size == "line":
            self.append(c.FEED_LINE + bytes([amount]))
        else:
            self.append(c.FEED_DOT + bytes([amount]))

    def send_image(self):
        bmp = bytearray(im.image)
        # bml = [bmp[i:i+10] for i in range(0, len(bmp), 10)]
        self.append(b'\x1d\x2A' + bytes([20]) + bytes([20]) + bmp)

    def print_image(self):
        self.append(b'\x1D\x2f\x00')
