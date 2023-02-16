import os
import os.path
name='den_tot'
openfile=[]
way=[]
way.append(os.getcwd())
for j in range(len(way)):
    ls = os.listdir(way[j])
    for i in range(len(ls)):
        print(ls[i])
        if os.path.isdir(ls[i]):
            way.append(os.getcwd()+'\\{}'.format(ls[i]))
        else:
            if name in ls[i]:
                openfile.append(way+'\\{}'.format(ls[i]))
                print(openfile)
print(openfile)
print(way)




# path = os.getcwd()
# name1 = os.listdir(path)
# for i in range(len(name1)):
#     if os.path.isdir(name1[i]):
#         path = os.getcwd()+'\\{}'.format(name1[i])
#         name2=os.listdir(path)
#         for j in range(len(name2)):
#             if os.path.isdir(name2[j]):
#                 path += '\\{}'.format(name1[i])
# print(os.getcwd()+'0501')
# if os.path.isdir('Python源代码.py'):
#     print("shi")
# else:
#     print('not')
# 返回 True 表示是目录（文件夹）