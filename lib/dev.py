from .freebie import Freebie

class Dev:
    
    def __init__(self, dev_name):
        self.name = dev_name

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.dev == self]
    
    @property
    def companies(self):
        return list({f.company.name for f in self.freebies})
    
    def received_one(self, item_name):
        
        for f in self.freebies:
            if f.item_name == item_name:
                return True
            else:
                return False

        # received_list = [f.item_name for f in self.freebies]            
        
        # return (if item_name in received_list)

    def give_away(self, dev, freebie):

        if freebie in self.freebies:
            freebie.dev = dev
            
        