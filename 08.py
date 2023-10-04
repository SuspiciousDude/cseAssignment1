# Password generator
import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
upperAlpha = 'ABCDEFGGHIJKLMNOPQRSTUVWXYZ'
upperAlphaList = list(upperAlpha)
lowerAlpha = upperAlpha.lower()
lowerAlphaList = list(lowerAlpha)
specialChar = ['!','@','#','$','%','^','&','*','(',')','~','`','-','_','+','=','[',']','{','}','|',';',':','"',"'",'<',',','>','.','?','/']

passWord = ''

for _ in range(2):
    passWord += random.choice(numbers)
    passWord += random.choice(upperAlphaList)
    passWord += random.choice(lowerAlphaList)
    passWord += random.choice(specialChar)

print(passWord)