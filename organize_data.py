#link de como manipular arquivo csv em python
#https://realpython.com/python-csv/
import sys
import csv

#dicionário por estado e unidade federativa
capital_dic={
'Acre': [],
'Alagoas': [],
'Amapá': [],
'Amazonas':[],
'Bahia':[],
'Ceará': [],
'Distrito Federal':[],
'Espírito Santo':[],
'Goiás':[],
'Maranhão':[],
'Mato Grosso':[],
'Mato Grosso do Sul':[],
'Minas Gerais':[],
'Pará':[],
'Paraíba':[],
'Paraná':[],
'Pernambuco':[],
'Piauí':[],
'Rio de Janeiro':[],
'Rio Grande do Norte':[],
'Rio Grande do Sul':[],
'Rondônia':[],
'Roraima':[],
'Santa Catarina': [],
'São Paulo':[],
'Sergipe': [],
'Tocantins': []
}

with open('data/brazil_covid19.csv', "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        #dados originais
        #date, hour, state, suspects, refuses, cases, deaths
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        #novos campos
        new_cases = 0
        new_deaths = 0
        if (capital_dic[row["state"]]):
            new_cases = int(row["cases"]) - int(capital_dic[row["state"]][-1]["cases"])
            new_deaths = int(row["deaths"]) - int(capital_dic[row["state"]][-1]["deaths"])
        capital_dic[row["state"]].append({'date': row["date"], 'hour': row["hour"], 'state': row["state"], 'cases': row["cases"], 'newcases': new_cases, 'deaths': row["deaths"], 'newdeaths': new_deaths})
        #print(f'\t{row["state"]} has {row["cases"]} cases, and {row["deaths"]} deaths.')
        line_count += 1
    print(f'Processed {line_count} lines.')

#salvando o novo arquivo
with open('data/remake_brazil_covid19.csv', mode='w',newline='\n', encoding='utf-8') as csv_file:
    fieldnames = ['date', 'hour', 'state', 'cases', 'newcases', 'deaths','newdeaths']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for state in capital_dic:
        for row in capital_dic[state]:
            writer.writerow(row)