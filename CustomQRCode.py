# With qrcode module we can make a custom QR code for a website/text easily
# Make sure to pip install qrcode
# https://pypi.org/project/qrcode/

import qrcode
codeimg = qrcode.make("http://www.google.com")
codeimg.save("QRimg.jpeg")
