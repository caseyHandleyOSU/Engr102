class Participant:
    def __init__(self, age, industry, salary, currency, country, experience, education):
        self.age = age
        self.industry = industry
        self.salary = int(salary.replace(',',''))
        self.currency = currency
        self.country = country
        self.experience = experience
        self.education = education
        
    

    def __str__(self):
        return "This participant is {0} years old and works in {1}. They make ${2} {3} yearly, working in {4} with {5} years of experience. Their education level is: {6}".format(self.age, self.industry, self.salary, self.currency, self.country, self.experience, self.education)