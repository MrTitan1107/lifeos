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

    He aprendido a separar las dependencias en el  contexto de la comunicación entre un base de datos y una API.
        -He creado repotory dentro de struture que donde se aloja la lógica de consulta de la base de datos. Coge un input (food: comida) lo guarda/actualiza/elimina/busca y devuelve un resultado, nada más.
        -He creado services.py que es donde se aloja la logica de negocio. Por ahora hace lo mismo que struture pero en un futuro será quien se encarga de procesar los datos optenidos a partir de las peticiones a las base de datos ( por ahora mediante CSVRepository) y aplicar la lógica de negocio. Por ejemplo. El CSVRepository he creado un método que crea un nuevo alimento a partir de un objeto Food y lo mete en la base de datos y otro que busca en la base de datos un alimento a partir de su nombre. En services utilizo esas funciónes para buscar si un alimento que quiero crear ya existe para no volverlo a crear.
        -Por ultimo he creao api/main.py que es donde se aloja la lógica de comunicación entre la API y las base de datos através de los servicios (services.py).
    
    He aprendido la importancia de usar la codificación UTF-8 al leer archivos para evitar problemas con caracteres raros como tildes o eñes.

    He aprendido que cuando quieres realizar una petición a una API en la que quieres obtener información a partir de una información enviade usar el metodo GET no siempre es lo mejor. GET mete toda la iformación que se envía en la url. Si queremos mandar un json complejo es inviable. Por eso para esos casos es mejor usar POST aunque no vayamos a cambiar nada y solo queramos una respues de la API, ya que la petición viaja en formato JSON. Esto nos permite enviar mucha más información que con GET.

   He aprendido la importancia de la validación de tipos (types) con pydantic o dataclases. 
        -Dataclases es nativo de python y se encarga de hacer más facil lo codificación de clases que se van a usar con el objetivo de almacenar información. Nor permite escribir una clase sin necesidad de escribir un __init__ y selfs por todas partes. Es util para usar dentro de python ya que es rápido y nativo. Pero tiene un problema: la validación de tipos. Si queremos validar tipos en una dataclass tenemos que hacerlo manualmente con lo que eso conlleva (mucho código y tiempo). Por eso no es recomendable usarlo para cuando va a haber interacción con el mundo exterior.
        -Pydantic: no es una librería nativa y tiene una funcionalidad parecida a dataclass con la ventaja de que al crear una clase a partir de una instacia de la clase de base de Pydantic (BaseModel) podemos trabajar igual que con dataclasses pero con validación de tipos automática ( solo hace falta declarar la variable y el tipo: name: str, y la librería se encarga de lanzar un error si el tipo no coincide ).

22/12/2025
    Hoy he aprendido que para poder crear una base de datos escalable y profesional es esencial usar SQL. Pero como python y SQL no se pueden comunicar directamente usamos SQLLite para crear una base de datos local alojada den un arichov de mi ordenador y sqlalchemy para traducir código python en consultas sql de manera automática y poder comunicarme con la base de datos con python.

    Otra cosa que he aprendido es la importancia de usar la inyección y separación de dependencias y como FastAPI nos ayuda con ello. Cuando trabajmos con una base de datos SQL no podemos usar una sola sesión para todos los usurios o las peticiones de la API por que puede haber interferencias entre las consultas de los distintos usuarios. Por eso tenemos que crear una sesión temporal por cada nueva petición de la API y eliminarla una vez ejcutada la petición.

    También he aprendido que una de las ventajas de usar una base de datos en SQL es que la propia base de datos se encarga de manera automática de crear una ID única para cada nuevo objeto "food" que introduzco en ella. Esto es mmuy util ya que aumenta la eficiencia de la búsqueda de una alimento en concreto entre todos al hacerlo a partir de los IDs de los objetos dentro de la base de datos que eestán ordenados lo que hace que la búsqueda sea mucho más rápida.
2/1/2026
    Hoy he aprendido a usar la libraría requests muy por encima para comunicarme y hacer peticiones a apis. En concreto a una api creada por mi.

    También he aprendido a usar una librería para hacer frontends de datos usando python (streamlit). La verdad es que es bastante intuitica y simple, mucho más que pyside. Imagino que tendrá sus limitaciones. Pero aun así me gusta bastante como se ve, es moderno y minimalista. 

    Hoy se a centrado en crear una interfaz (frontend) muy básica para interactuar con la api y la base de datos. He aprendido como se comunican y la importante se separa la lógica de cada una de las partes, la interfaz, la lógica de negocio y la base de datos.
4/1/2026
    He aprendido a crear un documento de requerimientos de manera automática.

    He aprendido a alojar mi aplicación en la nube.
        Por un lado el frontend en la web oficial de streamlit de manera gratuita
        Por otro lado el backend en render también de manera gratuita

    También he apredido a subir mi proyecto a github y a partir de el instalar mi aplicación en los servidores antes mencionados para que mi aplicación se convierta en una aplicación web real.