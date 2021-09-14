# Python/es

 {{VeryImportantMessage|FreeCAD fue originalmente diseñado para trabajar con Python 2.x. Esta serie terminó con la versión 2.7.18 del 20 de abril de 2020 y es sucedida por Python 3. El desarrollo posterior de FreeCAD se hará exclusivamente con Python 3, y no se apoyará la compatibilidad hacia atrás.}}

## Descripción


{{TOCright}}

[Python](https://www.python.org) es un lenguaje de programación de propósito general y de alto nivel que se utiliza muy comúnmente en grandes aplicaciones para automatizar algunas tareas mediante la creación de scripts o [macros](macros/es.md).

En FreeCAD, el código Python se puede utilizar para crear varios elementos de forma programada, sin necesidad de hacer clic en la interfaz gráfica de usuario. Además, muchas herramientas y ambientes de trabajo de FreeCAD están programados en Python.

Ver [Introducción a Python](Introduction_to_Python/es.md) para aprender sobre el lenguaje de programación Python, y luego [Python Tutorial de guión](Python_scripting_tutorial/es.md) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md) para empezar a hacer scripts en FreeCAD.

## Legibilidad

La legibilidad del código Python es uno de los aspectos más importantes de este lenguaje. El uso de un estilo claro y consistente dentro de la comunidad Python facilita las contribuciones de los diferentes desarrolladores, ya que la mayoría de los programadores experimentados de Python esperan que el código tenga un formato determinado y siga ciertas reglas. Al escribir código Python, es aconsejable seguir [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) y [PEP257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).

Estos documentos presentan las explicaciones de una manera más fácil de usar:

-   [Cómo escribir un hermoso código Python con PEP 8](https://realpython.com/python-pep8/)
-   [Documenting Python Code: Una Guía Completa](https://realpython.com/documenting-python-code/).

## Convenciones

En esta documentación deben seguirse algunas convenciones para los ejemplos de Python.

Esta es una signatura de función típica


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   Los argumentos con pares clave-valor son opcionales, con el valor por defecto indicado en la firma. Esto significa que las siguientes llamadas son equivalentes:


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


:   En este ejemplo, el primer argumento no tiene un valor por defecto, por lo que debe incluirse siempre.

-   Cuando los argumentos se dan con la clave explícita, los argumentos opcionales pueden darse en cualquier orden. Esto significa que las siguientes llamadas son equivalentes:


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   Las directrices de Python hacen hincapié en la legibilidad del código; en particular, los paréntesis deben seguir inmediatamente al nombre de la función, y un espacio debe seguir a una coma.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   Si es necesario dividir el código en varias líneas, debe hacerse con una coma dentro de paréntesis o corchetes; la segunda línea debe alinearse con la anterior.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   Las funciones pueden devolver un objeto que puede ser utilizado como base de otra función de dibujo.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```

## Importaciones

Funciones de Python se almacenan en archivos llamados módulos. Antes de utilizar cualquier función en ese módulo, el módulo debe ser incluido en el documento con la instrucción `import`.

Esto crea funciones prefijadas, es decir, `module.function()`. Este sistema evita los choques de nombres con funciones que se llaman igual pero que provienen de módulos diferentes. Por ejemplo, las dos funciones `Arch.make_window()` y `myModule.make_window()` pueden coexistir sin problema.

Ejemplos completos deben incluir las importaciones necesarias y las funciones prefijadas.


```python
import FreeCAD as App
import Draft

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 1, 0)
p3 = App.Vector(2, 0, 0)
Wire = Draft.make_wire([p1, p2, p3], closed=True)
```


```python
import FreeCAD as App
import Draft
import Arch

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 0, 0)
p3 = App.Vector(1, 1, 0)
p4 = App.Vector(0, 2, 0)
pointslist = [p1, p2, p3, p4]

Wire = Draft.make_wire(pointslist, closed=True, face=True)
Structure = Arch.make_structure(Wire, name="Big pillar")
```


{{Powerdocnavi

}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:API Documentation](Category:API_Documentation.md) [Category:Python Code](Category:Python_Code.md) [Category:Glossary](Category:Glossary.md)
