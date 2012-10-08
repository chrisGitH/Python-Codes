# coding=utf-8
from PIL import Image


def create_image():
    """Función para crear una imagen de 500x500 pixeles de color blanco"""
    size = (500, 500)
    img = Image.new("L", size, "white")
    img.save("C:\img.jpeg", "JPEG")
    del img


def crop_image():
    """Función para cortar una imagen a un 90% de calidad"""
    box = (70, 90, 200, 220)
    quality = 90
    img = Image.open("C:\img.jpg")
    crop = img.crop(box)
    crop.save("C:\img_croped.jpeg", "JPEG", quality=quality)


def create_thumbnail():
    """Funcion para crear thubnails de 128x128 pixeles a un 90% de calidad"""
    size = (128, 128)
    quality = 90
    im = Image.open("C:\img.jpg")
    im.thumbnail(size, Image.ANTIALIAS)
    im.save("C:\img_thumbnail.jpeg", "JPEG", quality=quality)