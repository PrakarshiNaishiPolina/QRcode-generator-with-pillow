import qrcode
from PIL import Image

def generate_qrcode(data,output_path,size=300):
     qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15,border=4)

     qr.add_data(data)
     qr.make(fit=True)

     img=qr.make_image(fill_color="black",back_color="white")
     img=img.resize((size,size),Image.Resampling.NEAREST)
     img.save(output_path)
     print(f"QR code saved at {output_path}")
     img.show()


generate_qrcode(data="https://praksnaish.com",output_path="qrcode.png",size=300)

