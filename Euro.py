from flask import Flask, render_template,url_for
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, static_folder='C:\\Users\\danim\\Desktop\\REGLADO\\templates')#index siempre tiene que estar una carpeta por debajo para que lo coja python
#/mnt/chromeos/MyFiles/Downloads/WEB_SCRAP/templates para Chromeos
# Función para hacer web scraping
import datetime

def scrape_website():
    url = 'https://femp-fondos-europa.es/fondos-europeos-ng-eu/convocatorias-ng-eu-2/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    europa_list = []  # Lista para almacenar las subvenciones
    # Encuentra todos los elementos table
    
    for table in soup.find_all('table'):
        # Encuentra todos los elementos tr dentro de la tabla
        #for tr in table.find_all('tr'):
            # Encuentra todos los elementos td dentro de la fila
            
            for tr in table.find_all('tr'):
                # Extrae el texto y el enlace de cada elemento y añádelo a la lista
             
                if tr.find('td'):
                    td=tr.text.strip()
                    lista_split=td.split('\n')
                    filas = {}
                    if len(lista_split)==8:
        
                    
                        lista_filtrada=lista_split
                        
                  
                        filas = [lista_filtrada[0], lista_filtrada[2], lista_filtrada[4], lista_filtrada[5],lista_filtrada[7]]


                        
                        europa_list.append(filas)
    return europa_list
@app.route('/')
def home():
    # Llamamos a la función de scraping
    
    europa = scrape_website()
    
    return render_template('index.html', europa=europa)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
