import mesa 

class SchellingAgent(mesa.Agent):
    def __init__(self,model,agent_type,unique_id):
        super().__init__(unique_id,model)

        self.type = agent_type
    def step(self):
        pass

class SchellingModel(mesa.Model):
    def __init__(self,width,height,density,minority,homophily):
        super().__init__()

        self.width = width
        self.height = height
        self.density = density
        self.homophily = homophily

    def step(self):
        pass 



model = SchellingModel(width=10, height=10, density=0.8, minority=0.2, homophily=0.4)
print("Model created successfully.")




