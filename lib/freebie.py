
class Freebie:
    
    all = []

    def __init__(self, Dev, Company, item_name, value):
        self.dev = Dev
        self.company = Company
        self.item_name = item_name
        self.value = value

        Freebie.all.append(self)

    def print_detail(self):
        
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")
        return(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")