from collections import namedtuple


CompanyParams = namedtuple('CompanyParams', 'id name income1 income2 income3 income4')
companies_quantity = int(input('Введите количество предприятий для расчета прибыли: '))
company_list = []
param_list = []
for company in range(companies_quantity):
    str_income = input('Введите название предприятия и через пробел введите '
                       'прибыль данного предприятия за каждый квартал: ')
    param_list.append(company+1)
    param_list.extend(str_income.split())
    company_info = CompanyParams._make(param_list)
    company_list.append(company_info)
    param_list = []
companies_income = {}
i = 1
for company in company_list:
    companies_income[i] = int(company.income1) + int(company.income2) + int(company.income3) + int(company.income4)
    i += 1
print(f'за год {companies_income}')
avg_income = sum(companies_income.values())/companies_quantity
print(f'Среднее {avg_income}')
print(f'Компании ниже {avg_income} это '
      f'{[el.name for el in company_list if el.id in [id for id in companies_income.keys() if companies_income[id] < avg_income]]}')
print(f'Компании выше {avg_income} это '
      f'{[el.name for el in company_list if el.id in [id for id in companies_income.keys() if companies_income[id] > avg_income]]}')