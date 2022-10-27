class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        residual = self.draft - (self.crew)*1.5
        if residual > 20:
            return True 
        else: 
            return False

Titanic = Ship(400, 10)
Titanic.is_worth_it()


