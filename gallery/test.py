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
    # 获取文件列表及其修改时间
    image_names = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):  # 你可以根据需要修改文件类型
            full_path = os.path.join(folder_path, filename)
            modification_time = os.path.getmtime(full_path)
            image_names.append((filename, modification_time))

    # 根据修改时间排序，从新到旧
    image_names.sort(key=lambda x: x[1], reverse=True)

    # 返回只包含文件名的列表
    return [name for name, _ in image_names]

folder_path = "images"
image_names = get_sorted_image_names(folder_path)
with open("index.md", "w", encoding='utf-8') as f:
    f.write(prefix)
    count = len(image_names)
    for name in image_names:
        count = count - 1

        name_without_extension = os.path.splitext(name)[0]
        if name_without_extension.startswith("IMG_"):
            name_without_extension = ""

        if count == 0:
            formatted_string = f'''        ["gallery/images/{name}","gallery/images/{name}",{name_without_extension}]'''
        else:            
            formatted_string = f'''        ["gallery/images/{name}","gallery/images/{name}",{name_without_extension}],\n'''
        f.write(formatted_string)
    f.write(postfix)
