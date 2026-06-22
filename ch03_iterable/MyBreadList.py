breads = list()  # 또는 breads = []
breadString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
breadList = breadString.split(",")

for item in breadList:
    breads.append(item)

print(type(breads))
print(breads)