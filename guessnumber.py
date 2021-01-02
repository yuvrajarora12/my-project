guessnumber = 3

guesschances = 0
count = 3

while(count):
    userguess = input("guess the number between one to ten you only have three chances")
    if(userguess == '3'):
        print("congratulations you won the game")

    elif(userguess > '3'):
        print("you guess is bigger")
        guesschances = guesschances+1
        print("now you only have", guesschances - 3, "chances")
        


    elif(userguess < '3'):
        print("you guess is lower")        
        guesschances = guesschances+1
        print("now you only have", guesschances-3, "chances")
        


    elif(guesschances == '3'):
        print("you lose")
    count = count-1
