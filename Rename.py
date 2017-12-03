import os,re,shutil

k=os.getcwd()
convert=re.compile('(\(\d*\))(.*)')
# z=convert.search("(877)abkjagbkag(347)")
# print(z.group(2))
for folderName, subfolders, filenames in os.walk(k):
    for filename in filenames:
        z = convert.search(filename)
        if z!=None:
            print(z.group(2))
            shutil.move(os.path.join(folderName,filename),os.path.join(folderName,z.group(2)))
