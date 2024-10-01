#writing an  code for the finding the vowel in string
def vowel(string):
    vowels = "aeiou"
    count = 0
    for i in string:
        if i in vowels:
            print(i)

            count += 1
    print(count)    
    if(count == 0):
        print("No vowels in the name")
name = input("enter your name: ")
vowel(name.lower())
# Output:
# enter your name: Aishwarya
