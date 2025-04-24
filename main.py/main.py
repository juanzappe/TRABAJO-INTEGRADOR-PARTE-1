from pathlib import Path
import csv

ruta_archivo = Path(__file__).parent.parent / 'EPH_usu_3er_Trim_2024_txt' / 'usu_individual_T324.csv'

with open(ruta_archivo, 'r') as file:
    csv_reader = csv.reader(file,delimiter= ';')
    header = next(csv_reader)
    
    indice_ch04 = header.index('CH04')
    pondera = header.index('PONDERA')
    cant_varones = 0
    cant_mujeres = 0

    for line in csv_reader:
        if line[indice_ch04] == '1':
            cant_varones += int(line[pondera]) 
        else:
            cant_mujeres += int(line[pondera])
       
print(f'Hay {cant_varones} varones y {cant_mujeres} mujeres.')

