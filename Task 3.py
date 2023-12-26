import winsound

file_name = input("Name the file:")
file_ext = file_name.split(".")
print("file extension is: " + repr(file_ext[-1]))
color_list = ["Red","Green","White" ,"Black"]
print("%s %s" % (color_list[0],color_list[-1]))
