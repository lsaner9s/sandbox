import mesa 

class SchellingAgent(mesa.Agent):
    def __init__(self,model,agent_type,unique_id):
        super().__init__(unique_id,model)

        self.agent_type = agent_type
    def step(self):
        pass

class SchellingModel(mesa.Model):
    def __init__(self,width,height,density,minority,homophily):
        super().__init__()

        self.width = width
        self.height = height
        self.density = density
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
                        
                    agent = SchellingAgent()
                    self.grid.place_agent(agent,(x,y))
                    self.schedule.add(agent)
                        
                        
    def step(self):
        self.schedule.step()

    



model = SchellingModel(width=10, height=10, density=0.8, minority=0.2, homophily=0.4)
print("Model created successfully.")




