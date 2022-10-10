import os, glob, shutil

print(os.getcwd())
PATH = "L6/L6"
os.chdir(PATH)
print(os.getcwd())

sang = 0
toi = 0

processed_folder = "C:/Users/hungt/Downloads/Compressed/data_train/" + PATH.split('/')[0] + "_processed"
os.mkdir(processed_folder)
os.chdir(processed_folder)
os.mkdir("sang")
os.mkdir("toi")
os.chdir("../")
os.chdir(PATH)


for file in glob.glob("*.jpg"):
    txt_file = os.path.splitext(file)[0] + ".txt"
    # print(txt_file)
    str = os.path.splitext(file.split('_')[2])[0]
    print(file)
    hour = int(str[8:10])
    # print(type(hour))

    if(7 < hour < 19):
        print("Sang")
        sang = sang + 1
        shutil.copy2(file, processed_folder + "/" + "sang")
        shutil.copy2(txt_file, processed_folder + "/" + "sang")
    else:
        print("Toi")
        toi = toi + 1
        shutil.copy2(file, processed_folder + "/" + "toi")
        shutil.copy2(txt_file, processed_folder + "/" + "toi")
print("Sang: ", sang)
print("Toi: ", toi)