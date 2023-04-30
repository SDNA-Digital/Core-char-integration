import json
import psycopg2 as pg

x = []
y = []
label=[]
connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
curs = connection.cursor()
curs.execute('SELECT areaid as "Area ID", areanome as "Area", COUNT(*) as "Qtde Incidentes" FROM dash_incidentes GROUP BY areaid, areanome')

columns = [col[0] for col in curs.description]
results = []
for row in curs.fetchall():
    result_dict = {}
    for i, value in enumerate(row):
        result_dict[columns[i]] = value
    results.append(result_dict)

curs.close
connection.close

json_result = json.dumps(results, indent=4)
with open('resultado.json', 'w') as arquivo:
    arquivo.write(json_result)