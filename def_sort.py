def sort_num(num1,num2,num3):
  if num1>num2:
    num1,num2=num2,num1
  if num1>num3:
    num1,num3=num3,num1
  if num2>num3:
    num2,num3=num3,num2
  print(num1,num2,num3)
sort_num(90,27,67)
