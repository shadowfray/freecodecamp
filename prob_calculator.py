#Shadowfray
'''
This program is a classic drawn balls from a hat probability problem.
We estimate the solution using a Montecarlo simulation via the
experiment function.
A given hat is a class so we can have multiple hats, and has a built in
function to draw the balls from it. The hat can take any number of balls,
using the **kwargs variable to handle it.
'''

import random
import copy

class Hat:
    def __init__(self,**kwargs):
        self.balls ={} 
        self.hat_contents = [] #represent each ball as an item in the list
        
        for key, value in kwargs.items():
            self.balls[key] = value

        #adds each ball as an item in the list
        for i in self.balls.keys():
            for j in range(self.balls[i]):
                self.hat_contents.append(i)

    #draw balls from hat
    def draw(self, num):
        balls_drawn = []

        #randomly chooses a ball, removes it from the hat
        for i in range(num):
            choice = random.choice(self.hat_contents)
            balls_drawn.append(choice)
            self.balls[choice] -= 1
            self.hat_contents.remove(choice)

        return balls_drawn

#conducts a montecarlo sim
def experiment(hat, #an instance of the Hat class
               expected_balls, #a dictionary of the balls we want to draw
               num_balls_drawn, #the number of balls we draw
               num_experiments #how many sims we do
               ):
    success_count = 0

    #handles each sim
    for experiment in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)

        #If we don't meet the criteria this is set to false
        enough_balls = True
        for i in expected_balls.keys():
            if expected_balls[i] > drawn_balls.count(i):
                enough_balls = False

        if enough_balls == True:
            success_count += 1

    return (success_count / num_experiments)

