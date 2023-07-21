

class player_manager:
    '''
    Manages player information using json database
    
    Attributes
    ----------------
    self.hp: int
        Player's health
    self.xy: list
        Position of the player
    self.inventory: dict
        Objects of the player
    self.wardrobe: dict
        Armour and weapon

    Methods
    -------
    '''

    def __init__(self, player_db) -> None:
        self.hp = player_db["HP"]
        self.xy = player_db["xy"]
        self.inventory = player_db["inventory"]
        self.wardrobe = player_db["wardrobe"]
    
    def damage(self, x):
        self.hp -= x
    
    def add_object(self, object):
        # checks if the inventory is full
        if sum(self.inventory.values())<100:
            if object in self.inventory.keys():
                self.inventory[object] +=1
        
        