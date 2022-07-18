number=int(input('Enter the number:  \n'))
fact=1
i=1
if(i<=number):
        for i in range(1,number+1):
                fact=fact*i
        print('factorial of the number is:  ')
        print(fact)