""" - Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""

lista = ["  juan pérez ", "MARÍA", " miguel ", "ana", "Juan Piero", " Sofía ", "LUIS", "roger", "roger"]

def normalizar_nombres(nombres):
    cantidad = len(nombres)
    procesados = []
    for nombre in nombres:
        nombre1 = nombre.title().strip()
        #nombre1 = nombre.strip()
        procesados.extend(nombre1.split())
        #procesados.append(nombre)
    listafinal = []
    for nombre in procesados:
        if nombre not in listafinal:
            listafinal.append(nombre)

    return listafinal


print(normalizar_nombres(lista))