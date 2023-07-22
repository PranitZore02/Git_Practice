def sum_of_no(lst):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    return total

print("the file")

lst=[1,2,3,4,5,6]
result=sum_of_no(lst)
print(f'the sum of the given no is {result}')