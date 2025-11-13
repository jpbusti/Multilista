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
    tabla = {}  

    try:
        f = open(self, encoding='utf-8')
    except FileNotFoundError:
        print('No encontré el archivo:', self)
        return tabla

    read = csv.reader(f)
    try:
        cabecera = next(read)
    except StopIteration:
        f.close()
        return tabla

    for fila in read:
        if len(fila) < 4:
            continue  
        dept = fila[1].strip().title()  
        muni = fila[3].strip().title()  

        if dept == '' or muni == '':
            continue

        if dept not in tabla:
            tabla[dept] = []

        if muni not in tabla[dept]:
            tabla[dept].append(muni)

    f.close()
    return tabla

DIVIPOLA = divipola('DIVIPOLA.csv')


if __name__ == '__main__':
    colombia = Node(0, 'Colombia')
    multilista_colombia = ListaMultiple()
    multilista_colombia.head = colombia
    multilista_colombia.tail = colombia

    for dep in DIVIPOLA.keys():
        if dep not in DIVIPOLA:
            continue
        
        dep_node = Node(1, dep) 
        
        munis_list = ListaMultiple()
        
        for muni in DIVIPOLA[dep]:
            muni_node = Node(2, muni)  
            
            if munis_list.head is None:
                munis_list.head = muni_node
                munis_list.tail = muni_node
            else:
                muni_node.prev = munis_list.tail
                munis_list.tail.next = muni_node
                munis_list.tail = muni_node
        
        dep_node.sub_list = munis_list
        
        if multilista_colombia.head.next is None and multilista_colombia.head.id == 0:
            dep_node.prev = colombia
            colombia.next = dep_node
            multilista_colombia.tail = dep_node
        else:
            dep_node.prev = multilista_colombia.tail
            multilista_colombia.tail.next = dep_node
            multilista_colombia.tail = dep_node

    print('Colombia')
    
    current_dept = colombia.next
    dept_list = []
    while current_dept:
        dept_list.append(current_dept)
        current_dept = current_dept.next
    
    for dept in dept_list:
        print('\tDepartamento: ' + dept.name)
        
        if dept.sub_list and dept.sub_list.head:
            munis = []
            current_muni = dept.sub_list.head
            while current_muni:
                munis.append(current_muni)
                current_muni = current_muni.next
            
            for muni in munis:
                print('\t\tMunicipio: ' + muni.name)



