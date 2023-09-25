import os
import re
import requests
import glob


def mkdir(file_path):
    file_path = file_path
    isExists = os.path.exists(file_path)
    if not isExists:
        os.makedirs(file_path)
        return file_path


def get_image(md_file):
    img_list = []
    with open(md_file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = re.sub(r"png#.*", "png", line)
            if ('](https://' in line and 'png' in line):
                line = line.split('(')[1].rstrip()
                img_list.append(line)
    return img_list


def img_download(img_list):
    for url in img_list:
        img_name = url.split('/')[-1]
        img_path = "./images/"
        img_name2 = img_path + img_name
        r = requests.get(url, stream=True, timeout=5)
        if r.status_code == 200:
            print(img_name)
            print(img_path)
            print(img_name2)
            mkdir(img_path)
            open(img_name2, 'wb').write(r.content)
            print(img_name2 + " download success!")
        else:
            print(img_name2 + "download failed!")


def new_md(md_file, new_file, ServerPath):
    with open(md_file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            with open(new_file, "a", encoding="utf-8") as f:
                if ('](https://' in line and 'png' in line):
                    line = re.sub(r"png#.*", "png)", line)
                    url = line.split('/')[-1].rstrip()
                    url = ServerPath + url
                    line = re.sub(r"https?://[^\s/$.?#].[^\s]*\.(?:png|jpe?g|gif)", url, line)
                    line = line.split(')')[0] + ')'
                    line = line.replace("image.png", "")
                    f.write(line.rstrip())
                else:
                    f.write(line)


if __name__ == "__main__":
    # 获取用户输入的文件名
    filename = input("请输入文件名（不含扩展名）：")
    mdfile_list = glob.glob(filename + ".md")
    ServerPath = input("请输入服务器路径（OSS or WebServer）：")
    for md_file in mdfile_list:
        img_list = get_image(md_file)
        img_download(img_list)
        new_md(md_file, filename + "_new.md", ServerPath)
