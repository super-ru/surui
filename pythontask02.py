M_grade=input('请输入您的数学成绩：')
Y_grade=input('请输入您的语文成绩：')
E_grade=input("请输入您的英语成绩：")
Z_grade=input('请输入您的综合成绩：' )
if M_grade >Y_grade:
    if M_grade >E_grade:
        if M_grade>Z_grade:
            print('您的最高一门成绩是:%s'%(M_grade))
        else:
            print('您的最高一门成绩是:%s'%(Z_grade))
    else:
        if E_grade >Z_grade:
            print('您的最高一门成绩是:%s' % (E_grade))
        else:
            print('您的最高一门成绩是:%s' % (Z_grade))
elif Y_grade >E_grade:
    if Y_grade>Z_grade:
        print('您的最高一门成绩是:%s' % (Y_grade))
    else:
        print('您的最高一门成绩是:%s' % (Z_grade))
elif E_grade>Z_grade:
    print('您的最高一门成绩是:%s' % (E_grade))
else:
    print('您的最高一门成绩是:%s' % (Z_grade))

