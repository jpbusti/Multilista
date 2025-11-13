import csv
from flask import Flask, render_template
from ListaMultiple import ListaMultiple
from Node import Node
import csv

app = Flask(__name__)
@app.route('/')
def root():
    markers = [
        {
            'lat': 6.246631,
            'lon': -75.581775,
            'popup': 'This is the middle of the map.'
        }
    ]
    return render_template('index.html', markers=markers)

def divipola(self):
    # Diccionario con estructura: {departamento: [{municipio, lat, lon}, ...]}
    diccionario = {}  
    
    f = open(self, encoding='utf-8')
    read = csv.reader(f)
    
    c = next(read)
    
    for fila in read:
        dept = fila[1].strip().title()  
        muni = fila[3].strip().title()  
        lon = fila[5].strip()
        lat = fila[6].strip()
        if dept not in diccionario:
            diccionario[dept] = []
        
        muni2 = {
            'municipio': muni,
            'lat': lat,
            'lon': lon
        }
        
        existe = False
        for m in diccionario[dept]:
            if m['municipio'] == muni:
                existe = True
                break
        
        if not existe:
            diccionario[dept].append(muni2)

    f.close()
    return diccionario

DIVIPOLA = divipola('DIVIPOLA.csv')

colombia = Node(0, 'Colombia',-74.297333,4.570868)
multilista_colombia = ListaMultiple()
multilista_colombia.head = colombia
multilista_colombia.tail = colombia

for dep in DIVIPOLA.keys():
    dep_node = Node(1, dep, '0', '0')  
    
    munis_list = ListaMultiple()
    
    for muni in DIVIPOLA[dep]:
        muni_node = Node(2, muni['municipio'], muni['lat'], muni['lon'])  
        

        if munis_list.head is None:
            munis_list.head = muni_node
            munis_list.tail = muni_node
        else:
            muni_node.prev = munis_list.tail
            munis_list.tail.next = muni_node
            munis_list.tail = muni_node
    
    dep_node.sub_list = munis_list
    
    if multilista_colombia.head.next is None:
        dep_node.prev = colombia
        colombia.next = dep_node
        multilista_colombia.tail = dep_node
    else:
        dep_node.prev = multilista_colombia.tail
        multilista_colombia.tail.next = dep_node
        multilista_colombia.tail = dep_node
print('Colombia')

current_dept = colombia.next
while current_dept:
    print('\tDepartamento: ' + current_dept.name)
    
    if current_dept.sub_list and current_dept.sub_list.head:
        current_muni = current_dept.sub_list.head
        while current_muni:
            print('\t\tMunicipio: ' + current_muni.name)
            current_muni = current_muni.next
    
    current_dept = current_dept.next

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)



