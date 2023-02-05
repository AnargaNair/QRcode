import pyqrcode
import png
from pyqrcode import QRCode

#string which represents the QR code
s="www.google.org"

#Generate the QR code
url= pyqrcode.create(s)

#Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg",scale=8)
#Create and save the png file naming "myqr.png"
url.png("myqr.png",scale=6)