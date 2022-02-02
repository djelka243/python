

import qrcode.constants
import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)
qr.add_data('https://www.facebook.com/djelka243/')
qr.make(fit=True)

img = qr.make_image(fill_color="bleue", back_color="while")
img.save('qrcode2.png')
