# while loops

# syntax
# while <condition>:
    # block of code
# num = 0
# while num<10:
#     print('still less than 10')
#     num +=1

wishlist = ['rc car', 'molten cheese', 'cheerleaders', 'attention', 'white shirts', 'sugar laces', 'reeses pieces',
'pastel de nata']

index_length = len(wishlist)-1
counter = 0
# using to substitute the for loop
# while counter <= index_length:
#     print('Next item')
#     print(wishlist[counter])
#     counter += 1

# infinite loop
# while True:
#     print('hello')
print('To exit press 0')
while True:
    # generate a random number
    num = 14
    # ask for user input
    user_guess = int(input('Guess number: '))
    # evaluate input and respond appropiately
    # breakpoint()
    if num == user_guess:
        print('you guessed it')
        break
    elif user_guess > num:
        print('Too high')
    elif user_guess == 0:
        break
    elif user_guess < num:
        print('Too low')

