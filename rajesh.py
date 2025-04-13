# LCM program 
# num1=int(input("enter the first element"))
# num2=int(input("enter the second element"))
# while num2!=0:
#     num1,num2=num2,num1%num2
#     print(num1)

#program of reversed number

# num=int(input("enter the element"))
# rev=0
# while num>0:
#     remainder=num%10
#     rev=rev*10+remainder
#     num=num//10
#     print("reversed of a number is:",reversed)
# number=int(input("enter the element"))
# if number <=1:
#     print(number,"is not prime")
# else:
#     for i in range(2,number):
#         if number%i==0:
#             print(number,"is not prime")
#             break
#         else:
#             print(number ,"is prime")

# hCF program
# num1=int(input("enter the first element"))
# num2=int(input("enter the second element"))
# while num2!=0:
#     num1,num2=num2,num1%num2
#     print(num1)


    # program of Automorphic number
    # num= int(input("enter the element"))
    # square=num*num
    # str_num=str(num)
    # str_square=str(square)
    # if str_square.endswith(str_num):
    #     print(f"{num} is an automorphic number:")
    # else:
    #     print(f"{num} is not an automorphic num")
    
            
# program of harshad number:
num=int(input("enter a number"))
sum_of_dighits=sum(int(digit) for digit in str(num))
if num%sum_of_dighits==0:
    print(f"{num} is not a harshad number")
else:
    print(f"{num} is not a harshad number")


        
        


