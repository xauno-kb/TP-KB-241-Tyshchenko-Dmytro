# strip() – видаляє пробіли (або вказані символи) з початку і кінця рядка
s1 = "   hello world   "
print("strip():", s1.strip())  

# capitalize() – робить першу літеру рядка великою, а всі інші маленькими
s2 = "pYTHON is Fun"
print("capitalize():", s2.capitalize())  

# title() – робить першу літеру кожного слова великою
s3 = "python programming language"
print("title():", s3.title())  

# upper() – перетворює всі літери на великі
s4 = "Hello World"
print("upper():", s4.upper())  

# lower() – перетворює всі літери на малі
s5 = "Hello World"
print("lower():", s5.lower()) 


assert s1.strip() == "hello world"
assert s2.capitalize() == "Python is fun"
assert s3.title() == "Python Programming Language"
assert s4.upper() == "HELLO WORLD"
assert s5.lower() == "hello world"