# def k(sum):
#     if sum%2==0:
#         return True
#     else:
#         return False
# print(k(69)) #False coz it is odd number. in this we are taking single singel valuse when we have multiple value do linke this

"when we have multiple values use the filter comand"
# def k(sum):
#     if sum%2==0:
#         return True
#     else:
#         return False
# list1=[12,74,89,37,20]
# r=list(filter(k,list1))
# print(r) #[12,74,20] it will print this number coz this are even number if we want odd then do this
"odd numbers"
# def l(sum):
#     if sum%2!=0:
#         return True
#     else:
#         return False
# list2=[12,35,79,64,30]
# r=list(filter(l,list2))
# print(r) #[35,79] it will print odd numbers this is the method for printing for odd numbers

"if we want the number direct from the user i,e. input"
def l(sum):
    if sum%2==0:
        return True
    else:
        return False
z=[int(x)for x in input().split()]
r=list(filter(l,z))
print(r)