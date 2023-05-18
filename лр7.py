from PIL import Image, ImageFilter
def zadan():

 image = Image.open('dog.png')
 image.show()
 width, height = image.size
 forma = image.format
 mode = image.mode

 print("ширина", width)
 print("высота", height)
 print("формат", forma)
 print("цветовая модель", mode)

def zadan2():

    image = Image.open('dog.png')
    image.show()
    new = image.resize((image.width // 3, image.height // 3))
    new.save("new.png")
    con = image.rotate(180)
    con.save('newflip.png')
    con = image.transpose(Image.FLIP_LEFT_RIGHT)
    con.save("newflip1.png")



def zadan3():


    names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for file in names:
        with Image.open(file) as img:
            img.load()
            new1 = img.filter(ImageFilter.CONTOUR)
            new1.show()
            new1.save('new' + file)


def zadan4():
    image1 = Image.open("water.png")
    new1 = image1.resize((image1.width // 4, image1.height // 4))
    img = Image.open("1.jpg")
    img.paste(new1)
    img.save("waterdog.jpg")

zadan(), zadan2(), zadan3() ,zadan4()


