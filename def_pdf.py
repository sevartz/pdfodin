from PIL import Image
import os
data=['image1.jpg', 'image2.jpg', 'image3.jpg']
ls = []
for file in data:
    print(file)
    file = Image.open(file)
    file.save('output.pdf', save_all=True, append_images=[*ls])
    ls.append(file)
