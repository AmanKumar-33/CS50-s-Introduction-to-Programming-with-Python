name = input("enter your name: ")

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

name = name.lower()
for i in name:
    if i in vowels:
        print(i, end='\n')
        count += 1

print(count)
if(count == 0):
    print("No vowels in the name")