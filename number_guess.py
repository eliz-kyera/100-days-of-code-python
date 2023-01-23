import random 

top_of_range= input("Type a number: ")

if top_of_range.isdigit():
    top_of_range= int(top_of_range)

    if top_of_range <= 0:
        print('Please enter a number greater than 0 next time.')
        quit()

else: 
    print('Please type a number next time')
    quit()

    # keep asking the user for a guess for the number

rand_num= random.randint(0, top_of_range)
print(rand_num)

# r= random.randrange(-4, 10)
# print(r)