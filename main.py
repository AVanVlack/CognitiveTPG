'''
Prints to a TPG Network Recipt Printer

Author: Drew VanVlack
Date:   1/25/2022
'''
import time
from TPG import TPG


printer = TPG("192.168.69.79", dev=True)

printer.init()

# printer.test()

# printer.music()

#printer.barcode_qr("Some super secret data: 33939282811182")

printer.text_smoothing()
printer.justification("center")
printer.send_image()
time.sleep(1)
printer.print_image()
printer.text_size(17)
printer.text("Ambrosia QSR", lf=True)
printer.text_size(00)
printer.bold()
printer.text("IT Department", lf=True)
printer.feed(1)

printer.invert()
printer.text(" Receipt Printer Refurbishment ", lf=True)
printer.justification("left")
printer.invert(False)
printer.bold(False)
printer.feed(1)

line_items = [["Printhead:", "Good, Cleaned"], ["Platen Roller:", "Good, 408c"], ["Cabinet :", "Good, Cleaned"], ["Mechanical:", "Tested OK"], ["Accessorys:", "Lid, RD"], [
    "Network Test:", "Completed OK"], ["Settings:", "LPI, Quality"]]

for item in line_items:
    printer.tab(1)
    printer.text(item[0])
    printer.tab(1)
    printer.text(item[1], lf=True)

printer.feed(3)

printer.justification("center")
printer.barcode("H183701016", 14, hri_posistion=2, hri_pitch=0, height=60)
printer.feed(8)
printer.cut()

# printer.print()
printer.close()
