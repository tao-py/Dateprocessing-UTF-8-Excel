#数据选取
fname=input("请输入要打开的文件名称：")
a=input("请输入您要提取的核素，不同核素用空格隔开（如：U235 Np237 Am241）：")
b=a.replace(" ",",").split(",")
fo=open(fname,'r')
fi=open("所选数据-den.txt","w")
s=fo.readlines()
for i in b:
    for item in s:
        if i in item:
            fi.write(item)
    fi.write("\n")
fi.close()
fo.close()
    
