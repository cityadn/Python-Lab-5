def reverse(str1):
    reversal = str1[3] + str1[2]+ str1[1] + str1[0]
    return reversal

str1 = input("Enter a 4 letter word:")
while len(str1) != 4:
    str1 = input("Enter a 4 letter word:")
print(reverse(str1))
