# Исходные данные: Папка с изображениями, названными по имени автора 
# Цель: Написать Python-скрипт, который программным образом обработает каждое 
# изображение из исходных данных, добавив имя автора в качестве подписи, 
# взятое из названия изображения. (см. приложение)
# И далее сохранит изображения (оставив изначальное название) в папке, 
# указанной при запуске скрипта из терминала (по умолчанию сохраняет 
# в `./output-images/`)
# Требования: Выравнивание текста по правому нижнему углу. 
# Шрифт и размер шрифта по предпочтению


import sys
import os
from PIL import Image, ImageDraw, ImageFont
import os.path

try:
    directory= r'C:\\Users\\aitur\Desktop\\Picture\\non_watermark'
    for file in os.listdir(directory):
        picture = directory + "/" + file
        image_to_work = Image.open(picture)
        draw = ImageDraw.Draw(image_to_work)

        # choose font type for text
        text = file  # all watermarked images  will be  with extension '.jpg'
        width, height = image_to_work.size
        font = ImageFont.truetype('arial.ttf', 60)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth -margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)

        # display watermarked images
        image_to_work.show()

        # saving in one folder
        image_to_work.save("output-images/{}".format(text))
except OSError:
    print('File not found!')


