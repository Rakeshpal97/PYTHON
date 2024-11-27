# using String function:(str.isalnum())
str1= "python1233"
print(str1.isalnum())
str2= "pythom@133"
print(str2.isalnum())
str3="13447"
print(str3.isalnum)

#using function:  (str.index())
str1="python is easy to understand"
print(str1.index("is"))
str2= str1.index("is")

#using function: str.isdigit()
str1= "rakesh12345"
print(str1.isdigit())
str2="765"
print(str2.isdigit())

# using function: str.isnumberic
str1= "87754"
print(str1.isnumeric())
str2="rakesh12467"
print(str2.isnumeric())
str3= "123-127"
print(str3.isnumeric())
str4= "rakesh 198 987"
print(str4.isnumeric())
str5= "34.67.87"
print(str5.isnumeric())

#using function:str.islower()
str1="pYtHon"
print(str1.islower())
str2="united"
print(str2.islower())
str3="python3.4.5"
print(str3.islower())

#using function: str.isupper()
str1="PYTHON"
print(str1.isupper())
str2="PYTHON1233"
print(str2.isupper())
str3="PythOn356"
print(str3.isupper())
str4="RAKESH8755"
print(str4.isupper())

# using function: len
str1= "united university"
print(len(str1))
str2="python is a programming language"
print(len(str2))

# using function: str.lower()
str1="raKEsH pAl"
print(str1.lower())
str2="pYThon654"
print(str2.lower())

# using function: str.upper()
str1="Rakeshpal"
print(str1.upper())
str2="UNITED"
print(str2.upper())
str3="united is good university876"
print(str3.upper())

# using function : replace()
name="section A"
old="section A CS"
new="section B"
str1=name.replace(old,new)
print(name)
print(str1)

# using function: str.join()
name='rakesh,''raj'
str1=''.join(name)
print(name)
print(str1)