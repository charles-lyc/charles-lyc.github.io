import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

prefix = '''---
title: Gallery
albums: [
'''

postfix = '''
        ]
---

{% aplayer "Summer菊次郎的夏天" "久石让,ロンドン交響楽団" "Summer - 久石让,ロンドン交響楽団.mp3" "autoplay" %}

'''

def get_sorted_image_names(folder_path):
    image_extensions = [".jpg", ".jpeg", ".png", ".bmp",".gif",".webp"]
    image_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(tuple(image_extensions)):
                image_names.append(file)
    image_names.sort()
    return image_names

folder_path = "images"
image_names = get_sorted_image_names(folder_path)
with open("index.md", "w", encoding='utf-8') as f:
    f.write(prefix)
    count = len(image_names)
    for name in image_names:
        count = count - 1
        name_without_extension = os.path.splitext(name)[0]
        if count == 0:
            formatted_string = f'''        ["gallery/images/{name}","gallery/images/{name}",{name_without_extension}]'''
        else:            
            formatted_string = f'''        ["gallery/images/{name}","gallery/images/{name}",{name_without_extension}],\n'''
        f.write(formatted_string)
    f.write(postfix)
