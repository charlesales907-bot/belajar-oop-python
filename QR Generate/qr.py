import qrcode

url = "https://forms.gle/hzcW7HndEyLeFtaCA"

img = qrcode.make(url)
img.save("kuisioner.png")







# qr = qrcode.QRCode(

#     version=1,  # Mengontrol ukuran matriks QR (1 = 21x21)
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,  # Ukuran piksel tiap kotak
#     border=4,  # Ketebalan garis tepi

# )


# # Generate and save the QR code
# url = "https://lintar.untar.ac.id/"

# qr.add_data(url)
# qr.make(fit=True)
# img = qr.make_image(fill_color="white", back_color="navy")
# img.save("lintar_qr.png")

