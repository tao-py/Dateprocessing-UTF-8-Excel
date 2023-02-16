#数据选取
i=0
while i==0:
    fname=input("请输入要打开的文件名称：")
    a=eval(input("请输入您要选取文件内数据所在行数的范围\n最小行："))
    b=eval(input("最大行："))
    fo=open(fname,'r')
    fi=open("{}-tally.txt".format(fname[0:3]),"w")
    s=fo.readlines()
    ls=s[a-1:b]
    for item in ls:
        fi.write(item)
    fi.close()
    fo.close()
    i=eval(input("输入数字“0”继续进行数据提取，输入任意数字结束程序"))

    
