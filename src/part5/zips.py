f = open("readme1.txt", "w+")
f.write("Hello")
f.close()

f = open("readme2.txt", "w+")
f.write("World")
f.close()

import zipfile

comp_file = zipfile.ZipFile("comp.zip", "w")
comp_file.write("readme1.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("readme2.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile("comp.zip", "r")
zip_obj.extractall("extracted")

import shutil

dir_to_zip = "./zips"
output = "folder_zip"
shutil.make_archive(output, "zip", dir_to_zip)
shutil.unpack_archive(f"{output}.zip", "extracted2", "zip")
