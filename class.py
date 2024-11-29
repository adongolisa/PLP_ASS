class Superhero:
    def __init__(self, name, alias, superpower, weakness, level=1):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.weakness = weakness
        self.level = level
    
    def display_identity(self):
        return f"{self.alias}, also known as {self.name}, has the power of {self.superpower}."

    def battle_cry(self):
        return f"{self.alias} shouts: 'For justice!'"

    def train(self):
        self.level += 1
        return f"{self.alias} has trained hard! Level increased to {self.level}."
