first_number = int(input("enter the first nuumber "))
second_number= int(input("enter the second number"))
limit=int(input("enter the limit of the sereis"))
for i in range(limit+1):
    sum=first_number+second_number
    first_number=second_number
    second_number=sum
    print (sum,end="")
