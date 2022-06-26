a=0
c = int(input(" Enter the no. whose multiples you want to add"))
b = int(input(" Enter the desired range"))
for i in range (1, b + 1 ):
        if c%i == 0:
            a = i + a
print (" The sum of multiples of {} upto {} is {} ".format(c,b,a))
        


        


