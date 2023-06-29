# 从命令行中读取多个文件,将这些文件整成一个gif
import sys
from PIL import Image

images = []

for file in sys.argv[1:]:
    print(f"the file name = {file}")
    image = Image.open(file)
    images.append(image)

# 表示将数据都写到 custome.gif文件中.存放所有的俄信息.后面添加images[1]中的元素,每个图片停留200ms,同时无限循环.
images[0].save(
    "customer.gif" ,save_all=True,append_images=[images[1]],duration=200,loop=0
)

