import os

import sys
sys.path.append('./final_image')

folder_path = "."

folder_list = os.listdir(folder_path)
for folder_name in folder_list:
    print("folder_name== ", folder_name)
    if (folder_name == ".DS_Store"):
        print("-----------------------.DS_Store--------------------------")
        os.remove(folder_path + "/" + ".DS_Store")

    else :
        file_path = folder_path + "/" + folder_name 
        print("file_path== ", file_path)
        file_list = os.listdir(file_path)          

        print("-------------------------------------------------")
        print(folder_name + " have " + str(len(file_list)) + " files.")
        print("file_path : " + file_path)
        
        count = 1
        for file_name in file_list :
            _, file_extension = os.path.splitext(file_name)
            old_name = file_path + "/" + file_name
            new_name = file_path + "/" + str(count) + file_extension  

            try:
                os.rename(old_name, new_name)
                print("success : " + file_name + " -> " + str(count) + file_extension)
            except:
                print("fail : " + file_name + " -> " + str(count) + file_extension)
                print("=========files already renamed original(abcde.jpg) to number(1.jpg)===========")
                
            count = count + 1


        file_list = os.listdir(file_path)
        count = 1
        for file_name in file_list :
            _, file_extension = os.path.splitext(file_name)
            old_name = file_path + "/" + file_name 
            new_name = file_path + "/" + folder_name + "_" + str(count) + file_extension

            try:
                os.rename(old_name, new_name)
                print("success : " + file_name + " -> " + folder_name + "_" + str(count) + file_extension)
            except:
                print("fail : " + file_name + " -> " + folder_name + "_" + str(count) + file_extension)
                print("=========files already renamed number(1.jpg) to new_name(hood_T_1.jpg)===========")
                break
            count = count + 1
        break