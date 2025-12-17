16/12/2025
    Hoy he aprendido sobre clases. He usado dataclases que es una forma más moderna de esccribir clases en las que no tienes que escribir todo la sintaxis necesaria (con todos los self, __init__, etc.) que tradicionalmente hace una clase. Sino que python lo hace por ti. Util cuando queremos crear clases sencillas.

    Tambien he aprendido una mejor forma de leer CSV con la librería CSV que permite leer o escribir en un CSV de manera mas directa y rápida que de la manera convencional.
        -DictWriter: te permite escribir row directamente pasandole como argumento un diccionario y una lista con la cabecera.
        -DictReader: te permita convertir un CSV en un dicionario de python que tiene como claves los valores del primer row y como valores cada uno de las columnas. Mucho mas rápido que la forma tradicional
    
    Por último me introduci brevemente en el concepto de test. Como crear pequeñas porciones de código reutilizable para testear nuestro programa.

17/12/2025
    Hoy he aprendido que para la gestión de CSV con la libreria nativa de python CSV necesito especificar cuando abro el archivo que python lo lea tal cual, sin haccer interpretaciones inteligentes de los saltos de linea y los retornos de carro que hace de manera automática. Esto se hace condigurando un variable del método open : newline=``. Esto es para evitar que en el csv queden filas en blanco por tener demasiados saltos de línea.

    También ha aprendido a interactuar con una API con FastAPI. Y a crear peticiones GET,POST y DELETE mediante las que he implementado búsqueda de alimentos por nombre. 
    
    Ha aprendido como crear un servidor en mi propio ordenador aunque es algo que tengo que prácticar más, ya que solo lo he hecho una vez y no sabría hacerlo yo solo.
