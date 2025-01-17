import json

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import os

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_directory = os.path.dirname(current_file_path)

# 切换到当前文件所在的目录
os.chdir(current_directory)

try:
    os.mkdir("items")
except:
    pass


def text_on_img(logo_text):
    import os

    print(os.getcwd())

    logo_text_copy = logo_text
    with open("./model_offset.json", "r") as f:
        model_offset = json.load(f)

    l = len(logo_text)
    l_sqrt = int(round((np.sqrt(l))))

    logo_text = "\n".join([logo_text[i : i + l_sqrt] for i in range(0, l, l_sqrt)])

    logo_len = len(logo_text.split("\n")[0])

    image_path_list = []
    for model, value in model_offset.items():
        img_width = model_offset[model][2] - model_offset[model][0]

        if logo_len < len(logo_text.split("\n")):
            add_len = -img_width // 10 / logo_len * 2
        else:
            add_len = img_width // 10 / logo_len / 2

        fontsize = img_width // logo_len
        logo_width = logo_len * fontsize
        # font = ImageFont.load_default(fontsize)
        # font = ImageFont.truetype("/Library/Fonts/simsun.ttc", fontsize)
        font = ImageFont.truetype("./images/No.39-ShangShouZhiZunShuFaTi-2.ttf", fontsize)

        print(model, value)
        img_path = f"./images/{model}.png"
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        draw.text(
            (model_offset[model][0], model_offset[model][1] + add_len),
            logo_text,
            font=font,
            fill=(255, 255, 255),
        )

        img_path_final = f"./items/tshirt_{model}_{logo_text_copy}.png"
        img.save(img_path_final)

        image_path_list.append(img_path_final)

    return image_path_list
