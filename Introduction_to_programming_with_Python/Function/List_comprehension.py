def main():
    yell("this", "is", "cs50")


def yell(*words):
    # an alternative way to in list //"word.upper() for word in words"
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
     main()
