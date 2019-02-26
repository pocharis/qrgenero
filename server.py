# Import QR Code library
# from flask_qrcode import QRcode
from flask import Flask, render_template, request
import qrcode
app = Flask(__name__)
from flask_bootstrap import Bootstrap

Bootstrap(app)
# QRcode(app)

@app.route("/")
def home():
    
    return render_template("index.html")

    
@app.route("/generate", methods=['post', 'get'])
def generate():
    message = ''
    if request.method == 'POST':
        textcode = request.form.get('textcode')  # access the data inside 
       
        if textcode != '':
            message = textcode
        else:
            message = "You entered nothing"


     # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 6,
        border = 4,
    )

    # The data that you want to store
    data = message

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("./static/image.png")
    return render_template("index.html", message = message)
