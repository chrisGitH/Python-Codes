import glob, os
import Image


def create_image():
    size = (500, 500)
    img = Image.new("L", size, "white")
    img.save("C:\img.jpeg", "JPEG")
    del img


def crop_image():
    box = (70, 90, 200, 220)
    quality = 100
    img = Image.open("C:\img.jpg")
    crop = img.crop(box)
    crop.save("C:\img_croped.jpeg", "JPEG", quality=quality)


def create_thumbnail():
    size = (128, 128)
    quality = 100
    im = Image.open("C:\img.jpg")
    im.thumbnail(size, Image.ANTIALIAS)
    im.save("C:\img_thumbnail.jpeg", "JPEG", quality=quality)