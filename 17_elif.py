# 为宝石数量赋值
stonenumber=5

# 条件：如果你拥有的宝石数量大于等于6个
if stonenumber>=6:
    
    # 结果：显示‘就拥有了毁灭宇宙的力量’的结果
    print('你拥有了毁灭宇宙的力量')
    
# 条件：如果想让宝石数量停留在5个以下，至少一个
elif 0<stonenumber<=5:

    # 结果：显示‘绯红女巫需要亲手毁掉幻视额头上的心灵宝石’的结果
    print('绯红女巫需要亲手毁掉幻视额头上的心灵宝石')

# 条件：当赋值不满足if和elif条件时，执行else下的命令，宝石数量为0个
else:

    # 结果：显示‘需要惊奇队长逆转未来’的结果
    print('需要惊奇队长逆转未来')
    
