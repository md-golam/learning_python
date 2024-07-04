# f = open("mytext.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("mytext.txt", "r") as f:
    # content2 = f.readline()
    # print(content2)
    # content2 = f.readline()
    # print(content2)
    content2 = f.readlines()
    for l in content2:
        print(l, end="")

# with open("newtext", "w") as f:
#     f.write(content2.upper())


