def func(x):
    if x%2==0:
        return True
    else:
        return False
list1=[0,5,13,15,20,18,19]
print(list(filter(func,list1)))

result=list(filter(lambda x: x%2==0,list1))
print(result)
