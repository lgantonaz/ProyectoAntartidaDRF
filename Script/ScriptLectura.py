import os,shutil,requests,re
from datetime import datetime

nuevo_path= os.path.dirname(os.path.realpath(__file__)) + '/Nuevos/'
cargado_path= os.path.dirname(os.path.realpath(__file__)) + '/Cargados/'


for file in os.listdir(nuevo_path):
    try:
        print('try')
        nombre_sensor = file.split(' ')[0]
        time = file.split(' ')[1].replace('.',':')
        date = file.split(' ')[2].replace('.txt', '')
        dateTime = date+ ' ' + time
        dateTime = datetime.strptime(dateTime, '%Y-%m-%d %H:%M')
        with open(nuevo_path +file) as f:
            lectura = [x for x in f.read().split(';') if x]
            lectura = [re.findall(r'\d+|\D+', medicion) for medicion in lectura]
        nuevaLectura = {
            'nombre_sensor': nombre_sensor,
            'fecha_lectura': dateTime,
            'lectura': lectura
            }
        r = requests.post('http://127.0.0.1:8000/api/nuevaLectura/', data=nuevaLectura)
        shutil.move(nuevo_path+file,cargado_path)
    except:
        print('except')
    else:
        print('else')
    finally:
        print('finally')