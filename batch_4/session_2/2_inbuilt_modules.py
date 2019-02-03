import os
import shutil

print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.listdir("/Users/chaitanya/CB/python_training/python-sessions/batch_4/"))


for f in os.listdir("/Users/chaitanya/CB/python_training/python-sessions/batch_4/"):
    print("/Users/chaitanya/CB/python_training/python-sessions/batch_4/" + f)
    print(os.path.join("/Users/chaitanya/CB/python_training/python-sessions/batch_4/", f))


# src = "/Users/chaitanya/CB/python_training/python-sessions/batch_4/session_2/tmp.txt"
# dst = "/Users/chaitanya/CB/python_training/python-sessions/batch_4/session_2/tmp_2.txt"
# shutil.copy(src,dst)

src_folder = "/Users/chaitanya/CB/python_training/python-sessions/batch_4/session_2/tmp"
# dest_folder =  "/Users/chaitanya/CB/python_training/python-sessions/batch_4/session_2/tmp/tmp_new"
#  check here if directory is already exists..
dest_folder = os.path.join(src_folder,"tmp_new")
dirs = os.listdir(src_folder)
os.mkdir(dest_folder)


print("$$$$$$$$$$$$$$$$$$")
for f in dirs:
    src = os.path.join(src_folder, f)
    dst = os.path.join(dest_folder, f)

    # print(src)
    print(dst)
    shutil.copy(src,dst)

# download this using urllib and save it in local using shutil
# https://github.com/chaitanyaubijawe/python/archive/master.zip
# https://docs.python.org/3/library/urllib.html
# Python  mkdules :
# zip
# urllib
# shutil
# os
