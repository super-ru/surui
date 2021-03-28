name=input('请输入自己的英文名字：')
print(name)
print(name[::-1])
new_name=name[::-1]
print(type(new_name))
real_name=name
print(type(real_name))
print('您的英文名字是:%s;\n您的英文名字翻转式：%s'%(real_name,new_name))