my_list =[1,5,9,2,0,-2,6,10]
new_list=[]
while my_list:
    min=my_list[0]
    for x in my_list:
        if min>x:
            min=x
    new_list.append(min)
    my_list.remove(min)
print(new_list)

