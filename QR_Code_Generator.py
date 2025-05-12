# Method no 1 : Simple qr code without specifing any color or border of QR.
import qrcode as qr
import qrcode.console_scripts
import qrcode.constants
image = qr.make("https://chatgpt.com/") # Link or Sentence which QR has to be made
image.save("Chatgpt.png")

# # Method no 2 : Customize qr code with customize any color or border of QR.
import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=1,)
qr.add_data("Hamza is a  boy")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save("Chatgpt.png")
