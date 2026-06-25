#Leer archivo para obtener información de la minera y visualizar
with open('minerales.txt', 'r') as file:
    for line in file:
        print(line.strip())# strip() elimina saldo de linea y split() divide la linea en partes usando el espacio cim
        
#Procesar la data, calcular total de cada mineral y generamos reporte
minerales = {}
with open('minerales.txt', 'r') as file:
    for line in file:
        partes = line.strip().split('-') #divide la linea usando guion como separador
        if len(partes)==2: #verificamos
            mineral = partes[0].strip() #obtenemos nombre del mineral
            cantidad = int(partes[1].strip()) #obtenemos cantidad y convertimos a entero
            if mineral in minerales:
                minerales[mineral] += cantidad #si el mineral existe, sumamos.
            else:
                minerales[mineral] = cantidad #si no existe, se agrega al diccionario.
#Mostramos el resultado y lo copiamos en reporte_mineral.txt
with open('reporte_mineral.txt', 'w') as report_file:
     for mineral, cantidad in minerales.items():
         report_file.write(f'{mineral}: {cantidad}\n')#escribimos el resultado en el archivo


         

