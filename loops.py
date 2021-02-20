'''
# while loop

x = 0

while (x<5):
    print(x)
    x = x+1


# for loop

for x in range(5, 10):
    print(x)

# for loop over a collection 
days= ['Mon', "tue", "wed", "thu"]
for d in days:
    print (d)



# break and Continue statements

for x in range(5,10):
 #   if (x==7): break
    if (x % 2 == 0): continue
    print(x)

'''
# using enumerate()- we can get index number and variable

days= ['Mon', "tue", "wed", "thu"]

for i,d in enumerate(days):
    print (i,d)

    