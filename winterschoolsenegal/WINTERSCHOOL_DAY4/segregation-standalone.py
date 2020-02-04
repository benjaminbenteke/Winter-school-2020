from pylab import *

n = 1000   # number of agents
r = 0.1    # neighbourhood radius
th = 0.5   # threshold for moving to another neighbourhood

class agent:
    pass



# generate a population of agents
def initialize():
    global agents
    agents = []
    for i in range(n):
        ag = agent()
        ag.type = randint(2)
        ag.x = random()
        ag.y = random()
        agents.append(ag)
        
def observe():
    global agents
    cla() # clear axis
    white = [ag for ag in agents if ag.type == 0]
    black = [ag for ag in agents if ag.type == 1]
    plot([ag.x for ag in white], [ag.y for ag in white], 'wo')
    plot([ag.x for ag in black], [ag.y for ag in black], 'ko')
    axis('image')
    axis([0, 1, 0, 1])
    
    if t%50 == 0:   # print only submultiples of 15000
        xticks(fontsize=15)
        yticks(fontsize=15)
        title('Time ' + str(t/50), fontsize=16)
        savefig('./frames/' + str(t/50) + '.png', bbox_inches = 'tight', pad_inches = 0)
    
# exhaustive search is used for detecting neighbours 
def update():
    global agents
    ag = agents[randint(n)]
    # list comprehension method for checking if agents are close enough to the focal agent 
    neighbours = [nb for nb in agents if (ag.x - nb.x)**2 + (ag.y - nb.y)**2 < r**2 and nb != ag]
    if len(neighbours) > 0:
        q = len([nb for nb in neighbours if nb.type == ag.type])/float(len(neighbours))
        if q < th:
            ag.x, ag.y = random(), random()

t=0
initialize()
observe()

for t in range(1, 201):
    update()
    observe()
