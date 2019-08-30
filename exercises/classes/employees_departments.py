class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

class Company:
    def __init__(self, name, address, industry):
        self.business_name = name
        self.address = address
        self.industry = industry
        self.employees = list()



NSS = Company("Nashville Software School", "301 Plus Park", "Developer Bootcamp")
HCA = Company("Hospital Corp. of America", "123 Broadway St.", "Healthcare")

Jeff = Employee("Jeff Hill", "Software Developer", "5/20/2019")
Renee = Employee("Renee Glick", "CEO", "3/12/15")
Derek = Employee("Derek Brooks", "CIO", "4/14/19")
John = Employee("Johnathan Johnson", "Accounting", "5/12/14")
April = Employee("April West", "Janitor", "5/12/13")

NSS.employees.append(Jeff)
NSS.employees.append(Renee)
HCA.employees.append(Derek)
HCA.employees.append(John)
HCA.employees.append(April)
# print(NSS.create_company())
print(f'{NSS.business_name} is in the {NSS.industry} industry and has the following employees')
for employee in NSS.employees:
    print(f'* {employee.name}')

print(f'{HCA.business_name} is in the {HCA.industry} industry and has the following employees')
for employee in HCA.employees:
    print(f'* {employee.name}')
