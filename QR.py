import qrcode


print ("if you want to creat qr of image pdf follow the steps")
print("1. upload the  image ,file,,pdf to the google drive")
print("2. get the shareable link of that file")
print("3. paste that link in the url section")
url = input("Enter the URL:").strip()
file_path = "C:\\Users\\Adarsh\\OneDrive\\Desktop\\Adi study folder\\aditya python\\qrcode.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file_path)
print("QR code was generated ")

print ("if you want to creat qr of image pdf follow the steps")
print("1. upload the  image ,file,,pdf to the google drive")
print("2. get the shareable link of that file")
print("3. paste that link in the url section")