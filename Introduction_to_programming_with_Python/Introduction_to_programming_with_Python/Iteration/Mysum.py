mysum =0
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
for i in range (start,end +1):
    mysum += i
print("The sum of numbers from",start,"to",end,"is",mysum)