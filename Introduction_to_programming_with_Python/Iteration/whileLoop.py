# writing an code where a boy stuck in a maze and he has to find a way out of it
count = 0
where = input("You are lost in forest which side you want to go left or right: ")
while(where == "right"):
    count +=1
    print("You are in a maze")
    if(count > 2):
        print("😞")
    where = input("Which side you want to go left or right: ")
print("You are out of maze")

# while True:
#     print("Moooooo")