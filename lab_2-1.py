# Author: SMR (AMDG) 1/10/21
def double_stuff(lst):
    for index, value in enumerate(lst):
        lst[index]=2*value
    return lst
def test_case():
    l1=[1,2,3,4]
    l2=[1.1,2,3.14,4]
    l3=[1,"a",2,"b"]

print(double_stuff(l1)==[2,4,6,8])
print(double_stuff(l2)==[2.2,4,6.28,8])
print(double_stuff(l3)==[2,"aa",4,"bb"])

test_case()
# Getting Name Error: 'l1' is not defined.. not sure why considering I defined in the previous lines