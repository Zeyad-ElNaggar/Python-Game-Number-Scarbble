#Game Description : The goal is to have a sum of 15 from the list
#.................:If none of the players reached the goal the game ends on draw
#.................:The number that has been chosen from the list can't be chosen again!



list=[1,2,3,4,5,6,7,8,9]

count1=0
count2=0
sum1=0
sum2=0

while count1<=5 and count2<=4 :

# Player 1 Turn

    print(list)
    num1=int(input("Player 1 please choose a number from your list : "))

    while num1 not in list:             #Checking if the entered number from player 1 is in the list
        num1=int(input("Sorry Player 1 the number your entered is not in the list, Try again : "))

    list.remove(num1)
    sum1+=num1
    count1+=1

        
#Checking if palyer 1 won        
    if sum1==15:
        print("Congratulaions Player 1, You Won !")
        break
    
    
    elif sum1!=15 and count1==5:            #Checking if there is a draw
        print("This game ends on draw !")
        break


# Player 2 Turn
    print(list)
    num2=int(input("Player 2 please choose a number from your list : "))

    while num2 not in list:           #Checking if the entered number from player 2 is in the list
        num2 = int(input("Sorry Player 2 the number your entered is not in the list, Try again : "))

    list.remove(num2)
    sum2 += num2
    count2 += 1
        
        
#Checking if player 2 won        
    if sum2==15:
        
        print("Congratulations Player 2, You Won !")
        break
    