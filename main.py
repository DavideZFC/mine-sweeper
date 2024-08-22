from classes.MineSweeper import *

env = MineSweeper(m=4,n=4, mines=2)
done = False
while not done:
    x, y = input("Enter two coordinates: ").split()
    done = env.step(int(x),int(y))
    env.render()