my_list =[1,5,9,2,0,-2,6,10]
new_list=[]
while my_list:
    maximum=my_list[0]
    for x in my_list:
        if maximum < x:
            maximum = x
    new_list.append(maximum)
    my_list.remove(maximum)
print(new_list)