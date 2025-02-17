
import qrcode 
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4) # QRCodeis function that changes functionality like border, version, error_correction, box_size, border

# note ERROR_CORRECT_H >> is a high level of error that can be corrected

qr.add_data("https://www.hackerrank.com/profile/adarshsalgaonka2") # this is varabile which store the data that we want to convert into QR code

qr.make(fit=True) # this is function that make the QR code

img = qr.make_image(fill_color="blue",back_color="white") # this is function that make the image of QR code

# fill_color >> front color of QR code
# back_color >> background color of QR code

img.save("HackerRankQR.png") # this is function that save the image of QR code


