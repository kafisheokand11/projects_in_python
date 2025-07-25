import random
import string
print("Welcome to the passwd genrator")

# create the lengh of passwd
len=int(input("enter the len of passwd:"))
 
# join all chars
all_char=string.ascii_letters+string.digits+string.punctuation
string.ascii_letters
# taking the random samples in the range of passwd
passwd=''.join(random.sample(all_char,len))

print("genrated password:",passwd)
