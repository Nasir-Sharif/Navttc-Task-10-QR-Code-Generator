import pyqrcode
from pyqrcode import QRCode

#String which represent the QR code
content = input("Enter Your URl : ")

#Generate Qr code
url = pyqrcode.create(content)

# SVG file create
file_name = input("Enter Your file name : ")
file_name = file_name + ".svg"
url.svg(file_name, scale = 5)
print(url.terminal(quiet_zone=1))