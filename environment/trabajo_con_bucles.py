import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight = False

#El bucle while tiene la condicion que si la varieable es diferente de True se va a ejecutar
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    #Si el numero ingresado es igual al a al numero almacenado en number nos imprimira 
    #que es correcto y la variable isGuesRigth tendra el valor true por lo tanto saldra del bucle
    #de lo contrario nos imprimira que lo volvamos a intentar 
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


