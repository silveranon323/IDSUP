# twodlist=[["Jitesh","Frans","Lise"],[123,546,274]]
# print(twodlist[0][1:3])
# print(twodlist[1][1:3])


# integer_list = [1,2,3]
# heterogenous_list=["string",0.1,True]
# list_oflists=[integer_list,heterogenous_list,[]]
# print(integer_list)
# print(heterogenous_list)
# print(len(integer_list))
# list_sum= sum(integer_list)
# print(list_sum)

x=[0,1,2,3,4,5,6,7,8,9]
zero=x[0]
print(zero)
z=x[-1]
print(z)
y=x[-2]
print(y)
x[0]=-1
print(x)

# slicing the fist three elements

first_three=x[:3]
print(first_three)

three_to_end=x[3:]
print(three_to_end)
last_three=x[-3:]
print(last_three)
without_first_and_last=x[1:-1]
print(without_first_and_last)
copy_of_x=x
print(copy_of_x)
every_third=x[::3]
print(every_third)
five_to_three= x[5:2:-1]
print(five_to_three)

my_list=[1,2,3,4,5,6]
print(3 in my_list)
print(6 in my_list)
print(3 not in my_list)
print(6 not in my_list)

# listconcatenation
x=[1,2,3]
y=[4,5,6]
x.extend(y)
y=x+[4,5,6]
print(x)
print(y)
x.append(0)
print("After appending '0'", x)
x,y=[1,2]
print(x)
print(y)
_,y=[1,6]
print(y)
