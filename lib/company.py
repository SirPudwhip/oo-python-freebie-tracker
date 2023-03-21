from .freebie import Freebie


class Company:

    all = []

    def __init__(self, name_string, founding_year):
        self.name = name_string
        self.year = founding_year

        Company.all.append(self)

    @property
    def freebies(self):
        
        return [f for f in Freebie.all if f.company == self]
    
    @property
    def devs(self):

        return list({f.dev for f in self.freebies})

    def give_freebie(self, dev, item_name, value):

        Freebie(dev, self, item_name, value)
    
    @classmethod
    def oldest_company(cls):
        
        # company_list = []

        # for c in cls.all:

        #     company_list.append({c: c.year})
        
        # sorted(company_list, )

        ###############################

        # This DEFINITELY needs to be refactored 

        company_list = [c.year for c in cls.all]

        oldest_company = []

        for c in cls.all:
            if c.year == sorted(company_list)[0]:
                oldest_company.append(c)

        return oldest_company[0]
        ##################################

        # print(cls.all.sort(key = getattr("year")).year)