def main():
    x = get_int("Friction: ")
    print(f"x is {x}")


def get_int(prompt):
        
          
        while True:
            try:

                return int(input(prompt))
            # print(f"x is {x}")
            except ValueError:
                # print("x is not an integer")
                 pass
             
main()
    
# print(f"x is {x}")