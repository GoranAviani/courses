#Question 21
#Level 3
#Question
#A robot moves in a plane starting from the original point (0,0).
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of
#movement and original point. If the distance is a float, then just print the nearest integer.
#Example:
#If the following tuples are given as input to the program:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Then, the output of the program should be:
#2
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

import math

class Robot():
    def __init__(self,):
        self.coordinates = {"vertical": 0, "horizontal":0 }

    def user_input(self):
        userInput = None

        while userInput != "X":
            userInput = input("Enter step: ")
            userInput = userInput.upper()
            userInput = tuple(userInput.split(" "))
            if userInput[0] in ["X","L"]:
                self.position_result()
            elif userInput[0] in ["UP", "DOWN","LEFT","RIGHT"]:
                self.calculation(userInput[0], int(userInput[1]))
            else:
                print("I dont understand command")

    def calculation(self, command1, length):
        if command1 == "UP":
            self.coordinates["vertical"]+=length
        elif command1 == "DOWN":
            self.coordinates["vertical"]-=length
        elif command1 == "RIGHT":
            self.coordinates["horizontal"]+=length
        elif command1 == "LEFT":
            self.coordinates["horizontal"]-=length

        self.position_result()

    def position_result(self):
        print("robot is verticaly {0} and horizontaly {1} from [0,0]" .format(self.coordinates["vertical"],self.coordinates["horizontal"]))
        print(round(math.sqrt((self.coordinates["vertical"] **2)+ (self.coordinates["horizontal"] **2))))
robot1 = Robot()
robot1.user_input()