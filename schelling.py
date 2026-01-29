import mesa 
import numpy as np

def happines_ratio(model):
    happy_agents = 0
    if not model.agents: return 0
    for agent in model.agents:
        if agent.happy == True:
            happy_agents += 1
    
    average_happiness = happy_agents/len(model.agents)
    return average_happiness


class SchellingAgent(mesa.Agent):
    def __init__(self,model,agent_type,unique_id):
        super().__init__(model)
        self.unique_id = unique_id
        self.agent_type = agent_type
        self.happy = True
    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos,moore = True, include_center = False, radius = 1)
        similar_neighbors = 0
        for neighbor in neighbors:
            if neighbor.agent_type == self.agent_type:
                similar_neighbors += 1
        
        total_neighbors = len(neighbors)
        if total_neighbors != 0:
            if (similar_neighbors/total_neighbors) < self.model.homophily:
                self.happy= False
                self.model.grid.move_to_empty(self)
            else:
                self.happy = True
                pass
    

class SchellingModel(mesa.Model):
    def __init__(self,width,height,density,minority,homophily):
        super().__init__()

        self.width = width
        self.height = height
        self.density = density
        self.minority = minority
        self.homophily = homophily
        self.datacollector = mesa.DataCollector(model_reporters={"Happiness Ratio: ": happines_ratio},agent_reporters={})
        self.grid = mesa.space.SingleGrid(width,height,torus = True)
        for x in range (width):
            for y in range (height):
                if self.random.random() < self.density:
                    if self.random.random() < self.minority:
                        agent_type = 1
                    else:
                        agent_type = 0
                        
                    agent = SchellingAgent(self,agent_type,unique_id=(x,y))
                    self.grid.place_agent(agent,(x,y))
                    
                    
    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)

    def get_grid_status(self):
        grid = np.zeros((self.width,self.height))
        for x in range (self.width):
            for y in range (self.height):
                agent = self.grid[x][y]
                if agent is not None:
                    grid[x][y] = 1 if agent.agent_type == 1 else 2
        return grid


    


if __name__ == "__main__":
        model = SchellingModel(width=10, height=10, density=0.8, minority=0.2, homophily=0.4)
        print("Model created successfully.")




