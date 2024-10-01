class Package:
    def __init__(self,number,sender,recipient,weight):
        self.number = number
        self.recipient = recipient
        self.sender = sender
        self.weight = weight

def main(): 
    Packages = [
        Package(number = 1,sender = "asms",recipient="rans",weight= 10),
        Package(number = 3,sender = "xnas",recipient = "asndn",weight =20)
    ] 
    for Package in Packages:
        print(f"packages{Package.number}: {Package.sender} to {Package.recipient}, {Package.weight}")


