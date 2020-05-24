from PIL import Image
import math

data = '0000000000000000000000000000000001111111000010101001000111111100010000010001000010100101000001000101110101010000011010010111010001011101011010000010110101110100010111010000001001011101011101000100000100110111100101010000010001111111010101010101010111111100000000000101011101100100000000000000010111111001010110110011000000101100001001000100001101000100000001010110111101100011101010000001101000111110011101011101000001001011100110101100101111011000000010101111010110101100101000000011110110010000000111111011110000110000010101101001111000101000011100011100111010011000101110000100110010111111000101000001000001110001100010111000110011100100001011101100111111001110000101000111001110001001101101111100110000000000010010101101110001110000011111110111000100000101010111000100000100101101101001000111000001011101011110001001011111101100010111010011000110111101001110000101110100100100000011010101000001000001001110110110011100101100011111110010000100001110100100000000000000000000000000000000000000000000000000000000000000000000'

MAX = int(math.sqrt(len(data)))
im = Image.new("RGB", (MAX * 9, MAX * 9), color=1)  # 背景白色

i = 0


def draw9x9(black=False):
    color = (255, 255, 255) if black else (0, 0, 0)
    for n in range(9):
        for j in range(9):
            im.putpixel([x + j, y + n], color)


for x in range(0, MAX * 9, 9):
    for y in range(0, MAX * 9, 9):
        if data[i] == '1':
            draw9x9()
        else:
            draw9x9(True)
        i += 1
im.show()
im.save('a.png')
