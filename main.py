import arxiv
import os
import getpass
from IPython.display import HTML, display
from PIL import Image
import base64
from paddlex import create_model
from pdf2image import convert_from_path
import cv2
import numpy as np
from dotenv import load_dotenv
import json
import os
pdf_path = r'pdf'
image_path = r"image"
env_path = './.env'
load_dotenv(dotenv_path=env_path, verbose=True)
key = os.getenv("key")
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


from IPython.display import HTML, display

def plt_img_base64(img_base64):
    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'

    # Display the image by rendering the HTML
    display(HTML(image_html))


image_path = r"image\test.png"
# image_path_encode = encode_image(image_path)
image_base64 = encode_image(image_path)
plt_img_base64(image_base64)

def layoutdetect(image_path):
    model_name = "PP-DocLayout-S"
    output_dir = "./output/"
    model = create_model(model_name)
    output = model.predict(image_path, batch_size=1, layout_nms=True)
    file_name = image_path.split('/')[-1].split('.')[0]
    # print("file_name : ", file_name)

    for res in output:
        res.print()
        res.save_to_img(save_path=f"{file_name}_label.png")
        res.save_to_json(save_path=f"{file_name}_label.json")

    return f"{file_name}_label.png", f"{file_name}_label.json"

image_base64 = encode_image(res_detect_path)
plt_img_base64(image_base64)

def layoutdetect(image_path):
    model_name = "PP-DocLayout-S"
    output_dir = "./output/"
    model = create_model(model_name=model_name)
    output = model.predict(image_path, batch_size=1, layout_nms=True)
    file_name = image_path.split('/')[-1].split('.')[0]

    for res in output:
        res.print()
        res.save_to_img(save_path=output_dir)
        res.save_to_json(save_path=f"{output_dir}/{file_name}_res.json")

    return f"{output_dir}/{file_name}_res.json"


def extract_image_and_table(pdf_path, output_dir, extract_path):
    # 获取文件名称，不包含路径和后缀
    file_li = pdf_path.split('/')[-1].split('.')
    file_name = pdf_path.split('/')[-1].split('.')[0]
    if len(file_li) > 2:
        file_name = file_name + '.' + pdf_path.split('/')[-1].split('.')[1]

    # 如果存在以{file_name}开头的文件在output_dir中，跳过
    # 如果存在以{file_name}开头的文件在extract_path中，跳过
    import os
    final_li_filename = []
    # 获取output_dir下的所有文件名
    res = os.listdir(extract_path)
    for item in res:
        # 如果包含{file_name}，跳过
        if item.startswith(f"{file_name}"):
            print(f"{file_name} exists, skip")
            final_li_filename.append(extract_path + "/" + item)
    if len(final_li_filename) > 0:
        print("之前已经抓取过，跳过")
        return final_li_filename

    images = convert_from_path(pdf_path,
                               poppler_path=r'D:\model\AI-application\extrect_image\t-layout\poppler-24.08.0\Library\bin')
    print(f"Number of images: {len(images)}")
    # print(images[0])

    all_images_path = []
    for i, image in enumerate(images):
        image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        Image.fromarray(image_np).save(f'{output_dir}/{file_name}_{i}.png', 'PNG')

        # layout_result = model.detect(image_np)
        _, res_detect_path = layoutdetect(f'{output_dir}/{file_name}_{i}.png')
        with open(res_detect_path, 'r') as f:
            layout_result = json.load(f)
        box = layout_result["boxes"]

        blocks = [b for b in box if b["label"] == "image"]

        for j, block in enumerate(blocks):
            coordinate = block["coordinate"]

            x1 = int(coordinate[0])
            y1 = int(coordinate[1])
            x2 = int(coordinate[2])
            y2 = int(coordinate[3])

            cropped_image = Image.fromarray(image_np).crop((x1, y1, x2, y2))
            cropped_image.save(f'{extract_path}/{file_name}_image_{i}_{j}.png', 'PNG')
        all_images_path.append(f'{extract_path}/{file_name}_image_{i}_{j}.png')

        blocks = [b for b in box if b["label"] == "chart"]

        for j, block in enumerate(blocks):
            coordinate = block["coordinate"]
            x1 = int(coordinate[0])
            y1 = int(coordinate[1])
            x2 = int(coordinate[2])
            y2 = int(coordinate[3])

            cropped_image = Image.fromarray(image_np).crop((x1, y1, x2, y2))

            cropped_image.save(f'{extract_path}/{file_name}_chart_{i}_{j}.png', 'PNG')
            all_images_path.append(f'{extract_path}/{file_name}_chart_{i}_{j}.png')

        blocks = [b for b in box if b["label"] == "table"]

        for j, block in enumerate(blocks):
            coordinate = block["coordinate"]
            x1 = int(coordinate[0])
            y1 = int(coordinate[1])
            x2 = int(coordinate[2])
            y2 = int(coordinate[3])

            cropped_image = Image.fromarray(image_np).crop((x1, y1, x2, y2))

            cropped_image.save(f'{extract_path}/{file_name}_table_{i}_{j}.png', 'PNG')
            all_images_path.append(f'{extract_path}/{file_name}_table_{i}_{j}.png')

        print("all_images_path : ", all_images_path)

        return all_images_path


