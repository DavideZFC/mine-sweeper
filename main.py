from classes.MineSweeper import *
from classes.Agent import *

m=4
n=4
mines=2
env = MineSweeper(m=m, n=n, mines=mines)
agent = Agent(m=m, n=n, mines=mines)
done = False
while not done:
    x, y = input("Enter two coordinates: ").split()
    table, done = env.step(int(x),int(y))
    env.render()
    agent.update(table)
    agent.show_boundary()