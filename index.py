import os, shutil
from pathlib import Path


path = Path('')
os.chdir(path)


my_list = os.listdir('input')
print(my_list)

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 50
x = list(divide_chunks(my_list, n))
print(len(x))

print('path-', path.cwd())
for i in range(len(x)):
    os.system('mkdir output'+str(i))

path1 = Path('./input')
os.chdir(path1)
for i in range(len(x)):
    for j in x[i]:
        curpath = path1.cwd()
        target = str(curpath).replace('\input', '')
        targetPath = str(target) + '\\output' + str(i) + '\\'
        print('targetPAth----', targetPath)
        print('path-----------', str(curpath) + '\\' + j)
        shutil.move(str(curpath) + '\\' + j
                        , targetPath)