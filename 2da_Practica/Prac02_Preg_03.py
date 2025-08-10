""" Se requiere verificar una lista de números de diferentes países, el
área de soporte al cliente recibe diariamente ciento de números en
distintos formatos. Estos números pueden venir con o sin código,
espacios, guines, paréntesis, o hasta textos no válido
- Crear la función de normalizar_telefonos(numeros, pais_defecto) la
cual para sus parámetros tendrá las siguientes especificaciones:
numeros: lista con números telefónicos
pais_defecto: en caso no tenga un número un prefijo lo agrega de
acuerdo al país ( “PE”->”+51”, “AR”->”+54”, “CL”->”+56”)
Si el prefijo no existe entre los ya mencionados indicar un mensaje
que no es válido y que debe ingresar un prefijo válido
- Devolverá un dict con:
“válidos”: una lista de números con formato: +<código><numeroNacional>
“invalidos”: lista con los números o valores inválidos y al inicio de esa
lista agregar el valor de “NO VÁLIDOS”
- No mutará la lista de entrada original """

lista = [1]
numeros = ["5198765432","98765432","54 11 1234-5678","(56) 2 2345 6789","123","ABC123","+52 1 123 4567"]


def normalizar_telefonos(numeros):
    codigos_pais = { "PE": "+51","AR": "+54","CL": "+56"  }
    resultado = {
        "validos": [],
        "invalidos": ["NO VÁLIDOS"]
    }
    for numero in numeros:
        num_nacional = numero.split("+")[0]
        if len(num_nacional) >= 8:
            resultado["validos"].append(

 print(normalizar_telefonos(lista))