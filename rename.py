import os

path = os.chdir("Image_Downloads\lldikti4_dot_id")

i = 0
for file in os.listdir(path):
    new_file_name = "lldikti{}.jpg".format(i)
    os.rename(file, new_file_name)
    i += 1
