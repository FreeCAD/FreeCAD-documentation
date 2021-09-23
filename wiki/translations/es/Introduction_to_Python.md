# Introduction to Python/es
{{TOCright}}

## Introducción

Este es un breve tutorial para los nuevos en [Python](http://es.wikipedia.org/wiki/Python). Python es un lenguaje de programación de código abierto y multiplataforma [lenguaje de programación](http://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n). Tiene varias características que lo hacen diferente de otros lenguajes de programación, y muy accesible para los nuevos usuarios:

-   Ha sido diseñado para que sea legible por los seres humanos, lo que hace que sea relativamente fácil de aprender y entender.
-   Es interpretado, lo que significa que los programas no necesitan ser compilados antes de ser ejecutados. El código de Python puede ser ejecutado inmediatamente, incluso línea por línea si lo desea.
-   Puede ser incrustado en otros programas como un lenguaje de scripting. FreeCAD tiene un intérprete de Python incrustado. Puedes escribir código Python para manipular partes de FreeCAD. Esto es muy potente, significa que puedes construir tus propias herramientas.
-   Es extensible, puedes conectar fácilmente nuevos módulos en tu instalación de Python y extender su funcionalidad. Por ejemplo, hay módulos que permiten a Python leer y escribir imágenes, comunicarse con Twitter, programar tareas para que las realice tu sistema operativo, etc.

o siguiente es una introducción muy básica, y de ninguna manera un tutorial completo. Pero esperamos que proporcione un buen punto de partida para una mayor exploración de FreeCAD y sus mecanismos. Te recomendamos encarecidamente que introduzcas los fragmentos de código de abajo en un intérprete de Python.

## El intérprete 

Por lo general, cuando se escriben programas de ordenador, se abre un editor de texto o su entorno de programación especial (que es básicamente un editor de texto con algunas herramientas adicionales), se escribe el programa, luego se compila y se ejecuta. A menudo se cometieron uno o más errores durante la entrada, por lo que su programa no funcionará. Puede que incluso aparezca un mensaje de error indicando lo que ha fallado. Entonces vuelves a tu editor de texto, corriges los errores, ejecutas de nuevo, repitiendo hasta que tu programa funcione como es debido.

En Python todo ese proceso se puede hacer de forma transparente dentro del intérprete de Python. El intérprete es una ventana de Python con un prompt de comandos, donde puedes simplemente escribir código Python. Si has instalado Python en tu ordenador (descárgalo desde el [Python página web](https://www.python.org/) si estás en Windows o Mac, instálalo desde tu repositorio de paquetes si estás en GNU/Linux), tendrás un intérprete de Python en tu menú de inicio. Pero, como ya se ha mencionado, FreeCAD también tiene un intérprete de Python incorporado: la [Consola de Python](Python_console/es.md).

![](images/FreeCAD_Python_console.png ) *La consola de FreeCAD Python*

Si no la ve, haga clic en **Ver → Paneles → Consola de Python**. La consola de Python puede cambiar de tamaño y también desacoplarse.

El intérprete muestra la versión de Python, y luego un símbolo `>>` que es el prompt del comando. Escribir código en el intérprete es sencillo: una línea es una instrucción. Cuando pulses **Intro**, tu línea de código se ejecutará (después de haber sido compilada instantánea e invisiblemente). Por ejemplo, trata de escribir esto:


```python
print("hello")
```


`print()`

es un comando de Python que, obviamente, imprime algo en la pantalla. Al pulsar **Enter**, se ejecuta la operación y se imprime el mensaje `"hola"`. Si se produce un error, por ejemplo, escribamos:


```python
print(hello)
```

Python te lo dirá inmediatamente. En este caso Python no sabe qué es `hello`. Los caracteres `" "` especifican que el contenido es una cadena, jerga de programación para un trozo de texto. Sin ellos, el comando `print()` no reconoce `hello`. Pulsando la flecha hacia arriba puedes volver a la última línea de código y corregirla.

El intérprete de Python también tiene un sistema de ayuda incorporado. Supongamos que no entendemos qué ha ido mal con `print(hello)` y queremos información específica sobre el comando:


```python
help("print")
```

Obtendrá una larga y completa descripción de todo lo que puede hacer el comando `print()`.

Ahora que entiendes el intérprete de Python, podemos continuar con las cosas más serias.

[inicio](#top.md)

## Variables

Muy a menudo en la programación se necesita almacenar un valor bajo un nombre. Ahí es donde entran las variables. Por ejemplo, escribe esto:


```python
a = "hello"
print(a)
```

Probablemente entiendas lo que ha pasado aquí, hemos guardado la cadena `"hello"` bajo el nombre `a`. Ahora que `a` es conocido podemos usarlo en cualquier lugar, por ejemplo en el comando `print()`. Podemos usar cualquier nombre que queramos, sólo tenemos que seguir algunas reglas simples, como no usar espacios o puntuación y no usar palabras clave de Python. Por ejemplo, podemos escribir:


```python
hello = "my own version of hello"
print(hello)
```

Ahora `hello` ya no es un indefinido. Las variables pueden ser modificadas en cualquier momento, por eso se llaman variables, su contenido puede variar. Por ejemplo:


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```

Cambiamos el valor de `myVariable`. También podemos copiar variables:


```python
var1 = "hello"
var2 = var1
print(var2)
```

Es aconsejable dar nombres significativos a sus variables. Después de un tiempo no recordarás qué representa tu variable llamada `a`. Pero si la nombras, por ejemplo, `myWelcomeMessage` recordarás fácilmente su propósito. Además, tu código está un paso más cerca de ser auto-documentado.

El caso es muy importante, `myVariable` no es lo mismo que `myvariable`. Si se introdujera `print(myvariable)` se obtendría un error como no definido.

[inicio](#top.md)

## Números

Por supuesto, los programas de Python pueden tratar con todo tipo de datos, no sólo con cadenas de texto. Una cosa es importante, Python debe saber con qué tipo de datos está tratando. Vimos en nuestro ejemplo de imprimir hola, que el comando `print()` reconoció nuestra cadena `"hello"`. Al usar `" " `, especificamos que lo que sigue es una cadena de texto.

Siempre podemos comprobar el tipo de datos de una variable con el comando `type()`:


```python
myVar = "hello"
type(myVar)
```

Nos dirá que el contenido de `myVar` es un `'str'`, que es la abreviatura de cadena. También tenemos otros tipos de datos básicos como números enteros y flotantes:


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```

Python sabe que 10 y 20 son números enteros, por lo que se almacenan como `'int'`, y Python puede hacer con ellos todo lo que puede hacer con los enteros. Mira los resultados de esto:


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```

Aquí forzamos a Python a considerar que nuestras dos variables no son números sino trozos de texto. Python puede sumar dos trozos de texto, aunque en ese caso, por supuesto, no realizará ninguna aritmética. Pero estábamos hablando de números enteros. También hay números de coma flotantes. La diferencia es que los números de coma flotantes pueden tener una parte decimal y los números enteros no:


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Número entero y Número de coma flotante pueden mezclarse sin problemas:


```python
total = var1 + var2
print(total)
print(type(total))
```

Como `var2` es un Número de coma flotante, Python decide automáticamente que el resultado debe ser también un Número de coma flotante. Pero hay casos en los que Python no sabe qué tipo usar. Por ejemplo:


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```

Esto resulta en un error, `varA` es una cadena y `varB` es un Número entero, y Python no sabe qué hacer. Sin embargo, podemos forzar a Python a convertir entre tipos:


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```

Ahora que ambas variables son cadenas la operación funciona. Observe que hemos \"encadenado\" `varB` en el momento de la impresión, pero no hemos cambiado `varB` en sí. Si quisiéramos convertir `varB` permanentemente en una cadena, tendríamos que hacer lo siguiente


```python
varB = str(varB)
```

También podemos usar `int()` y `float()` para convertir a entero y a flotante si queremos:


```python
varA = "123"
print(int(varA))
print(float(varA))
```

Habrás notado que hemos utilizado el comando `print()` de varias maneras. Hemos impreso variables, sumas, varias cosas separadas por comas, e incluso el resultado de otro comando de Python. Quizás también hayas visto que estos dos comandos:


```python
type(varA)
print(type(varA))
```

tienen el mismo resultado. Esto es porque estamos en el intérprete, y todo se imprime automáticamente. Cuando escribamos programas más complejos que se ejecuten fuera del intérprete, no se imprimirán automáticamente, por lo que tendremos que utilizar el comando `print()`. Teniendo esto en cuenta, dejemos de usarlo aquí. A partir de ahora simplemente escribiremos:


```python
myVar = "hello friends"
myVar
```

[inicio](#top.md)

## Listas

Otro tipo de datos útil es una lista. Una lista es una colección de otros datos. Para definir una lista utilizamos `[ ]`:


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

Como puede ver, una lista puede contener cualquier tipo de datos. Puedes hacer muchas cosas con una lista. Por ejemplo, contar sus elementos:


```python
len(myOtherList)
```

O recuperar un elemento:


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

Mientras que el comando `len()` devuelve el número total de elementos de una lista, el primer elemento de una lista siempre está en la posición `0`, por lo que en nuestra `myOtherList` `"Bob"` estará en la posición `2`. Podemos hacer mucho más con las listas, como ordenar los elementos y eliminar o añadir elementos.

Curiosamente, una cadena de texto es muy similar a una lista de caracteres en Python. Intenta hacer esto:


```python
myvar = "hello"
len(myvar)
myvar[2]
```

Normalmente, lo que se puede hacer con las listas también se puede hacer con las cadenas. De hecho, tanto las listas como las cadenas son secuencias.

Además de las cadenas, los enteros, los flotadores y las listas, hay más tipos de datos incorporados, como los diccionarios, e incluso puedes crear tus propios tipos de datos con clases.

[inicio](#top.md)

## Indentación

Un uso importante de las listas es la posibilidad de \"navegar\" por ellas y hacer algo con cada elemento. Por ejemplo, mira esto:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```

Hemos iterado (jerga de programación) a través de nuestra lista con el comando `for in` y hemos hecho algo con cada uno de los elementos. Observe la sintaxis especial: el comando `for` termina con `:` indicando que lo siguiente será un bloque de uno o más comandos. En el intérprete, inmediatamente después de introducir la línea de comando que termina con `:`, el prompt de comando cambiará a `...` lo que significa que Python sabe que hay más por venir.

¿Cómo sabrá Python cuántas de las siguientes líneas deberán ejecutarse dentro de la operación `for in`? Para ello, Python se basa en la indentación. Las siguientes líneas deben comenzar con un espacio en blanco, o varios espacios en blanco, o un tabulador, o varios tabuladores. Y mientras la indentación sea la misma, las líneas se considerarán parte del bloque `for in`. Si empiezas una línea con 2 espacios y la siguiente con 4, habrá un error. Cuando haya terminado, simplemente escriba otra línea sin sangría, o pulse **Enter** para volver del bloque `for in`.

La indentación también ayuda a la legibilidad del programa. Si usas sangrías grandes (por ejemplo, usa tabuladores en lugar de espacios) cuando escribas un programa grande, tendrás una visión clara de qué se ejecuta dentro de qué. Veremos que otros comandos también utilizan bloques de código con indentación.

El comando `for in` puede utilizarse para muchas cosas que deben hacerse más de una vez. Por ejemplo, puede combinarse con el comando `range()`:


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
    print(number)
    total = total + number
print("----")
print(total)
```

Si ha ejecutado los ejemplos de código en un intérprete copiando y pegando, encontrará que el bloque de texto anterior arrojará un error. En su lugar, copie hasta el final del bloque sangrado, es decir, el final de la línea `total <nowiki>=</nowiki> total + number` y luego pegue en el intérprete. En el intérprete pulsa {{Key|Intro}} hasta que desaparezca el aviso de los tres puntos y se ejecute el código. A continuación, copia las dos últimas líneas seguidas de otro **Intro**. Debería aparecer la respuesta final.

Si escribe en el intérprete `help(range)` verá:


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Aquí los corchetes denotan un parámetro opcional. Sin embargo, se espera que todos sean enteros. A continuación forzaremos que el parámetro del paso sea un entero usando `int()`:


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number)):
    print(float(i) / number)
```

Otro ejemplo `range()`:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```

El comando `range()` también tiene esa extraña particularidad de que comienza con `0` (si no especificas el número inicial) y que su último número será uno menos que el número final que especifiques. Eso sí, para que funcione bien con otros comandos de Python. Por ejemplo:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```

Otro uso interesante de los bloques indentados es con el comando `if`. Este comando ejecuta un bloque de código sólo si se cumple una determinada condición, por ejemplo:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```

Por supuesto, esto siempre imprimirá la frase, pero pruebe a sustituir la segunda línea por


```python
if "Lucky" in alldaltons:
```

Entonces no se imprime nada. También podemos especificar una sentencia `else`:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```

[inicio](#top.md)

## Funciones

Hay muy pocos [standard Python commands](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) y ya conocemos varios de ellos. Pero puedes crear tus propios comandos. De hecho, la mayoría de los módulos adicionales que puedes conectar a tu instalación de Python hacen precisamente eso, añadir comandos que puedes utilizar. Un comando personalizado en Python se llama función y se hace así:


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```

El comando `def()` define una nueva función, le das un nombre, y dentro del paréntesis defines los argumentos que la función utilizará. Los argumentos son los datos que se pasarán a la función. Por ejemplo, mira el comando `len()`. Si sólo escribes `len()`, Python te dirá que necesita un argumento. Lo cual es obvio: quieres saber la longitud de algo. Si escribes `len(myList)` entonces `myList` es el argumento que pasas a la función `len()`. Y la función `len()` está definida de tal manera que sabe qué hacer con este argumento. Hemos hecho lo mismo con nuestra función `printsqm`.

El nombre `myValue` puede ser cualquier cosa, y sólo se utilizará dentro de la función. Es sólo un nombre que le das al argumento para poder hacer algo con él. Al definir los argumentos también le dices a la función cuántos debe esperar. Por ejemplo, si haces esto:


```python
printsqm(45, 34)
```

habrá un error. Nuestra función estaba programada para recibir un solo argumento, pero recibió dos, `45` y `34`. Intentemos otro ejemplo:


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Aquí hicimos una función que recibe dos argumentos, los suma y devuelve ese valor. Devolver algo es muy útil, porque podemos hacer algo con el resultado, como almacenarlo en la variable `myTotal`.

[inicio](#top.md)

## Módulos

Ahora que tienes una buena idea de cómo funciona Python, necesitarás saber una cosa más: cómo trabajar con archivos y módulos

Hasta ahora, hemos escrito las instrucciones de Python línea por línea en el intérprete. Obviamente, este método no es adecuado para programas más grandes. Normalmente el código de los programas Python se almacena en archivos con la extensión {{FileName|.py}}. Los cuales son simplemente archivos de texto plano y cualquier editor de texto (Linux gedit, emacs, vi o incluso el Bloc de notas de Windows) puede ser utilizado para crear y editarlos.

Hay varias formas de ejecutar un programa Python. En Windows, basta con hacer clic con el botón derecho en el archivo, abrirlo con Python y ejecutarlo. Pero también puedes ejecutarlo desde el propio intérprete de Python. Para ello, el intérprete debe saber dónde está tu programa. En FreeCAD la forma más fácil es colocar tu programa en una carpeta que el intérprete de Python de FreeCAD conozca por defecto, como la carpeta del usuario de FreeCAD {{FileName|Mod}}:

-   En Linux suele ser {{FileName|/home/<username>/.FreeCAD/Mod/}}.
-   En Windows es {{FileName|%APPDATA%\FreeCAD\Mod}}, que suele ser {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod}}.
-   En Mac OSX suele ser {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Mod/}}.

Vamos a añadir una subcarpeta allí llamada {{FileName|scripts}} y luego escribir un archivo como este:


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```

Guarda el archivo como {{FileName|myTest.py}} en la carpeta {{FileName|scripts}}, y en la ventana del intérprete escribe:


```python
import myTest
```

sin la extensión {{FileName|.py}}. Esto ejecutará el contenido del archivo, línea por línea, tal como si lo hubiéramos escrito en el intérprete. Se creará la función suma y se imprimirá el mensaje. Los archivos que contienen funciones, como el nuestro, se llaman módulos.

Cuando escribimos una función `sum()` en el intérprete, la ejecutamos así:


```python
sum(14, 45)
```

Pero cuando importamos un módulo que contiene una función `sum()` la sintaxis es un poco diferente:


```python
myTest.sum(14, 45)
```

Es decir, el módulo se importa como un \"contenedor\", y todas sus funciones están dentro de ese contenedor. Esto es muy útil, porque podemos importar muchos módulos, y mantener todo bien organizado. Básicamente, cuando veas `something.somethingElse`, con un punto en medio, significa que `somethingElse` está dentro de `something`.

También podemos importar nuestra función sum() directamente al espacio principal del intérprete:


```python
from myTest import *
sum(12, 54)
```

Casi todos los módulos hacen eso: definen funciones, nuevos tipos de datos y clases que puedes utilizar en el intérprete o en tus propios módulos de Python, ¡porque nada te impide importar otros módulos dentro de tu módulo!

¿Cómo sabemos qué módulos tenemos, qué funciones hay dentro y cómo usarlas (es decir, qué tipo de argumentos necesitan)? Ya hemos visto que Python tiene una función `help()`. Haciendo:


```python
help("modules")
```

nos dará una lista de todos los módulos disponibles. Podemos importar cualquiera de ellos y navegar por su contenido con el comando `dir()`:


```python
import math
dir(math)
```

Veremos todas las funciones contenidas en el módulo `math`, así como cosas extrañas llamadas `__doc__`, `__file__`, `__name__`. Cada función en un módulo bien hecho tiene un `__doc__` que explica cómo usarlo. Por ejemplo, vemos que hay una función `sin()` dentro del módulo de matemáticas. ¿Quieres saber cómo usarla? 
```python
print(math.sin.__doc__)
```

Puede que no sea evidente, pero a cada lado de `doc` hay dos caracteres de subrayado.

Y finalmente un último consejo: Cuando trabajes en código nuevo o existente, es mejor no usar la extensión de archivo de macro de FreeCAD, {{FileName|.FCMacro}}, sino usar la extensión estándar {{FileName|.py}}. Esto es porque Python no reconoce la extensión {{FileName|.FCMacro}}. Si usas {{FileName|.py}} tu código puede cargarse fácilmente con `import`, como ya hemos visto, y también recargarse con `importlib.reload()`:


```python
import importlib
importlib.reload(myTest)
```

Sin embargo, hay una alternativa:


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

[inicio](#top.md)

## Empezando con FreeCAD 

Esperemos que ahora tengas una buena idea de cómo funciona Python, y puedas empezar a explorar lo que FreeCAD tiene que ofrecer. Las funciones de Python de FreeCAD están todas bien organizadas en diferentes módulos. Algunas de ellas ya están cargadas (importadas) cuando inicias FreeCAD. Sólo tienes que probar:


```python
dir()
```

[inicio](#top.md)

## Notas

-   FreeCAD fue diseñado originalmente para trabajar con Python 2. Desde que Python 2 llegó al final de su vida en 2020, el desarrollo futuro de FreeCAD se hará exclusivamente con Python 3, y no se soportará la compatibilidad hacia atrás.
-   Se puede encontrar mucha más información sobre Python en el [tutorial oficial de Python](https://docs.python.org/3/tutorial/index.html) y en la [referencia oficial de Python](https://docs.python.org/3/reference/).

[inicio](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Introduction to Python/es
