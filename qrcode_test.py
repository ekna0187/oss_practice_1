import qrcode
data = "http://github.com/ekna0187/oss_practice_1"

img = qrcode.make(data)
img.save("qrcode.png")

print("QR 코드가 생성되었습니다.")