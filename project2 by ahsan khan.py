#input text

text = input('Enter a string: ')
#length calculate

length = len(text)
#string  is a palindrome untill the middle
flag = True

for i in range(0,length//2):
    if text[i] != text[length-1-i]:
        flag = False
        break
# condition and output
if flag == True:
    print('word is a palindrome')
else:
    print('word is not a palindome')
# examples of palindrome are " rotator, madam , civic"