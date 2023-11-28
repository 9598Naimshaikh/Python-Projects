from flask import Flask, render_template, request, send_file
import qrcode
import base64
from io import BytesIO
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data_to_encode = request.form['data_to_encode']

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_to_encode)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to BytesIO object
        img_bytes = BytesIO()
        img.save(img_bytes)
        img_bytes.seek(0)

        # Encode the image data using base64
        img_data = base64.b64encode(img_bytes.read()).decode('utf-8')

        return render_template('index.html', data_to_encode=data_to_encode, qr_code=img_data)

    return render_template('index.html', data_to_encode=None, qr_code=None)


@app.route('/download/<data_type>/<data>')
def download_qrcode(data_type, data):
    try:
        img_data = base64.b64decode(data)
        img_bytes = BytesIO(img_data)

        # Save the image to a temporary file
        temp_filename = f'temp_qrcode_{data_type}.png'
        img_bytes.seek(0)
        img_bytes.save(temp_filename)

        return send_file(
            temp_filename,
            mimetype='image/png',
            as_attachment=True,
            download_name=f'qrcode_{data_type}.png'
        )
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
