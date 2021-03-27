import re

from bs4 import BeautifulSoup

with open("blank/basic.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")
# title = soup.title
# print(title)
# print(title.text)
# print(title.string)
# 12345678   f71fb1bafdd1ae54d1d64de58fea0ad5786c2599


# .find() .find_all()

# page_h1 = soup.find("h2")
# print(page_h1)

# page_all_h1 = soup.find_all("h2")
# print(page_all_h1)

# for item in page_all_h1:
#     print(item.text)

grid_item = soup.find_all(class_="grid-item")
print(grid_item)