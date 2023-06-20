import os
import imageio

file_list=sorted(os.listdir("image2"))

IMAGES=[]
for file_name in file_list:
    file_path=file_path = r'C:\Users\mahdi\Desktop\projects\pylearn.tamrin\assignment8\image2\\' + file_name

    image=imageio.imread(file_path)
    IMAGES.append(image)

print(IMAGES)
imageio.mimsave("my_output.gif",IMAGES,duration=0.4)