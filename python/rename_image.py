import os


path = "./python/cv_data/figure"
middle = "/train"
name_list = os.listdir(path)


for catagori in name_list:
    
    if catagori == "train_data" or catagori == "test_data":
        continue
    image_list = os.listdir(path + "/" + catagori + middle)
    for idx, image_name in enumerate(image_list):
        os.rename(path + "/" + catagori + middle + "/" + str(image_name), path + "/" + catagori + middle + "/" + catagori + "." + str(idx) + ".png")


        


            

            
                






