import mesa 

class schellingAgent(mesa.Agent):
    def __init__(self,model,agent_type,unique_id):
        super().__init__(unique_id,model)

        self.type = agent_type



