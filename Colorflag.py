from PIL import Image, ImageDraw


def hexes():
    string = input("Enter string to be converted to flag: ")
    lst = []
    for i in string:
        lst.append(format(ord(i), "x"))
    length = 3
    temp = lst + ['00'] * length
    sub = ['#' + temp[n] + temp[n + 1] + temp[n + 2] for n in range(0, len(lst), length)]
    return sub


cols = hexes()
print(cols)

RED = '#FF0000'
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def flag(width=800, height=400):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    length = len(cols)
    w = width / length
    count = 0
    for i in cols:
        draw.rectangle((count * w, 0, (count + 1) * w, height), i)
        count += 1
    flag.show()


flag()
