from PIL import Image, ImageDraw
import qrcode
data = "https://www.youtube.com/watch?v=UrtH9oe1ofQ"
img = qrcode.make(data)
img.save("My_videoQRcode.png")