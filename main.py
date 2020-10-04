# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "www.github.org"
  
# Generate QR code 
url = pyqrcode.create(s)