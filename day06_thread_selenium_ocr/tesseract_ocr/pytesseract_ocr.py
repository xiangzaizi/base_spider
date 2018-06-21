# -*- coding:utf-8 -*-

from PIL import Image
import pytesseract

# 中文
data1 = Image.open("test.jpg")
text = pytesseract.image_to_string(data1, lang="chi_sim")
print text

# 英文
# print(pytesseract.image_to_string(Image.open("tesseracttest.jpg")))
