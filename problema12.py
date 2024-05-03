ar= input('Digite el nombre del archivo: ')
archivo, tipo = ar.split('.')
tipo = tipo.lower()
indice = ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']
mime = ['image/gif', 'image/jpeg', 'image/jpeg', 'image/png', 'application/pdf', 'text/plain', 'application/zip']
busqueda = indice.index(f'{tipo}')
print(mime[busqueda])