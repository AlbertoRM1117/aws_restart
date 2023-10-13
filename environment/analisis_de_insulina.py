#programa que analiza el numero de caracteres que contienen varios archivos asi como elimina algunos datos de un archivo
with open('/home/ec2-user/environment/preproinsulin-seq.txt', 'r') as archivo:
    archivo_reemplazar = archivo.read()
    archivo_reemplazado = archivo_reemplazar.replace('ORIGEN','').replace('//','').replace('61','').replace('1','').replace(' ', '').replace('\n','')
   
with open('/home/ec2-user/environment/preproinsulin-seq-clean.txt', 'w') as archivo:
     archivo.write(archivo_reemplazado)

#Abrimos el archivo le asignamos un alias y luego imrpimimos el numero de caractares que contiene
with open('/home/ec2-user/environment/preproinsuline-seq-clean.txt', 'r') as i_lectura:
    total_caracter = i_lectura.read()
    print(len(total_caracter))
    i_lectura.close()
    
with open('/home/ec2-user/environment/ainsulin-seq-clean.txt', 'r') as i_lectura:
    
    total_caracter = i_lectura.read()
    print(len(total_caracter)) 
    i_lectura.close()

with open('/home/ec2-user/environment/binsulin-seq-clean.txt', 'r') as i_lectura:
    
    total_caracter = i_lectura.read()
    print(len(total_caracter))
    i_lectura.close()

with open('/home/ec2-user/environment/cinsulin-seq-clean.txt', 'r') as i_lectura:
    
    total_caracter = i_lectura.read()
    print(len(total_caracter))  
    i_lectura.close()
    

with open('/home/ec2-user/environment/lsinsulin-seq-clean.txt', 'r') as i_lectura:
    
    total_caracter = i_lectura.read()
    print(len(total_caracter))
    i_lectura.close()