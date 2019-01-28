import os

# importing required modules
from zipfile import ZipFile

from shutil import copyfile, copyfileobj

# specifying the zip file name
file_name = "code.zip"

# opening the zip file in READ mode

# zip.close()
# printing all the contents of the zip file
# zip.printdir()
#
# # extracting all the files
# print('Extracting all the files now...')
# zip.extract("Users/chaitanya/CB/python_training/python-sessions/batch_1/training_sessions/mitesh/A_inheritance.py")
# print('Done!')




# print(os.name)
# get current working directory....
# print(os.getcwd())

# get list of files and dirs in any dir...

path = os.getcwd()
# print(os.listdir(path))
# create a zip file with name : code.zip

zip = ZipFile(file_name, 'w')
src_zip_file  = os.path.join(path, file_name)

for fileName in os.listdir(path):
    if(fileName == "scope_test.py" or fileName == "Person.py"):
        print(fileName)
        print(path)
        print(os.path.join(path, fileName))


        # zip.write(path  + "/" + fileName)
        zip.write(os.path.join(path, fileName))
        print()
# close the file after adding all files inside zip file.
zip.close()


extractedDir = os.path.join(path , "extracted")
#/Users/chaitanya/CB/python_training/python-sessions/batch_1/training_sessions/mitesh/extracted/abc.zip

if not os.path.isdir(extractedDir):
    os.mkdir(extractedDir)

copyfile(src_zip_file, extractedDir + "/code.zip")






import urllib.request
import shutil
url = 'https://github.com/chaitanyaubijawe/python/archive/master.zip'
response = urllib.request.urlopen(url)
# with urllib.request.urlopen(url) as response, open("file_name.zip", 'wb') as out_file:
out_file = open("file_name.zip", 'wb')

shutil.copyfileobj(response, out_file)
out_file.close()


# data = response.read()      # a `bytes` object
# output_file = open("my_code.zip", "w")
# # for data in response.iter_content(chunk_size=512):
# #     if data:
# output_file.write(response)
# output_file.close()

# text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
