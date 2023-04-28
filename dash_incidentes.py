import matplotlib.pyplot as plt
import psycopg2 as pg
import json

x = []
y = []
label = []
connection = pg.connect(user="postgres", password="SDNA@2022", host="localhost", port="5432", database="Eagle2")
curs = connection.cursor()

curs.execute('SELECT areaid COUNT(*) FROM dash_incidentes GROUP BY areaid')

IncidenteXArea = curs.fetchall()

curs.close
connection.close

for raw in IncidenteXArea:
    x.append(raw[0])
    x=sorted(x)
    y.append(raw[1])
    y=sorted(y)

figura = plt.figure(figsize=(16,4))

figura.add_subplot(121)
plt.bar(x, y, label="Qtde de Incidentes", color='#3e2ed6')
plt.legend()
plt.title('Incidentes x Area (Visualização em barras)')
plt.xlabel('Areas por identificador')
plt.ylabel('Total de incidentes')

figura.add_subplot(122)
plt.plot(x,y, label='Qtde de Incidentes', color='#3e2ed6',lw='3')
plt.legend()
plt.title('Incidentes x Area (Visualização em tracejado)')
plt.xlabel('Areas por identificador')
plt.ylabel('Total de incidentes')

plt.show()

print(IncidenteXArea)