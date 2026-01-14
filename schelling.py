import mesa 
import numpy as np

class SchellingAgent(mesa.Agent):
    def __init__(self,model,agent_type,unique_id):
        super().__init__(unique_id,model)

        self.agent_type = agent_type
    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos,moore = True, include_center = False, radius = 1)
        similar_neighbors = 0
        for neighbor in neighbors:
            if neighbor.agent_type == self.agent_type:
                similar_neighbors += 1
        
        total_neighbors = len(neighbors)
        if total_neighbors != 0:
            if (similar_neighbors/total_neighbors) < model.homophily:
                self.model.grid.move_to_empty(self)
            else:
                pass
    

class SchellingModel(mesa.Model):
    def __init__(self,width,height,density,minority,homophily):
        super().__init__()

        self.width = width
        self.height = height
        self.density = density
        self.minority = minority
        self.homophily = homophily
        self.grid = mesa.space.SingleGrid(width,height,torus = True)
        self.schedule = mesa.time.RandomActivation(self)
        for x in range (width):
            for y in range (height):
                if self.random.random() < self.density:
                    if self.random.random() < self.minority:
                        agent_type = 1
                    else:
                        agent_type = 0
                        
                    agent = SchellingAgent(self,agent_type,unique_id=(x,y))
                    self.grid.place_agent(agent,(x,y))
                    self.schedule.add(agent)
                    
    def step(self):
        self.schedule.step()

    def get_grid_status(self):
        grid = np.zeros((self.width,self.height))
        for x in range (self.width):
            for y in range (self.height):
                agent = self.grid[x][y]
                if agent is not None:
                    grid[x][y] = 1 if agent.agent_type == 1 else 2
        return grid


    



model = SchellingModel(width=10, height=10, density=0.8, minority=0.2, homophily=0.4)
print("Model created successfully.")




