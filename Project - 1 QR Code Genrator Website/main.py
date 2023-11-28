# Todo: pip install qrcode

# Import the qrcode library, which is used for generating QR codes.
import qrcode


# Todo: Normal Uses !
# Define a function named generate_qr_code that takes data and qr_name as parameters.
# def generate_QrCode(data, qr_name):
#     qr_img = qrcode.make(data)
#     qr_img.save(qr_name)

# Todo: Advanced Uses !

# Define a function named generate_qr_code that takes data and qr_name as parameters.
def generate_QrCode(data, img_filename):
    # Create a QRCode object with specific parameters (version, error correction, box size, border).
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Add the data to the QRCode object.
    qr.add_data(data)

    # Generate the QR code to fit the data.
    qr.make(fit=True)

    # Create an image of the QR code with specified fill and background colors.
    img = qr.make_image(fill_color="red",back_color="white")

    # Save the generated QR code image to the specified filename.
    img.save(img_filename)


if __name__ == '__main__':
    data_url = "https://www.youtube.com/@codewithnaim529/videos"
    qr_filename = "hello.png"
    generate_QrCode(data_url, qr_filename)
