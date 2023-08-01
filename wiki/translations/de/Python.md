# Python/de
**FreeCAD wurde ursprünglich für die Arbeit mit Python 2.x entwickelt. Diese Reihe endete mit der Ausgabe 2.7.18 vom 20. April 2020 und wird gefolgt von Python 3. Die zukünftige Entwicklung von FreeCAD ausschließlich mit Python 3 durchgeführt, und die Abwärtskompatibilität wird nicht unterstützt.**

## Beschreibung




[Python](https://www.python.org) ist eine allgemeine, hochrangige Programmiersprache, die in großen Anwendungen sehr häufig verwendet wird, um einige Aufgaben zu automatisieren, indem man Skripte erstellt oder [Makros](macros/de.md).

In FreeCAD kann Python Code verwendet werden, um verschiedene Elemente programmgesteuert zu erstellen, ohne auf die grafische Benutzeroberfläche klicken zu müssen. Darüber hinaus sind viele Werkzeuge und Arbeitsbereiche von FreeCAD in Python programmiert.

Siehe [\|Einführung in Python](Introduction_to_Python/de.md), um mehr über die Programmiersprache Python zu erfahren, und dann [Python Skript Tutorien](Python_scripting_tutorial.md) und [FreeCAD Skriptgrundlagen](FreeCAD_Scripting_Basics.md), um das Skripting in FreeCAD zu starten.

## Lesbarkeit

Die Lesbarkeit von Python Code ist einer der wichtigsten Aspekte dieser Sprache. Die Verwendung eines klaren und konsistenten Stils innerhalb der Python Gemeinschaft erleichtert Beiträge von verschiedenen Entwicklern, da die meisten erfahrenen Python Programmierer erwarten, dass der Code auf eine bestimmte Art und Weise formatiert ist und bestimmten Regeln folgt. Beim Schreiben von Python Code ist es ratsam, [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) und [PEP257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) zu befolgen.

Diese Dokumente bieten Erklärungen in einer benutzerfreundlicheren Form:

-   [Wie man schönen Python Code mit PEP 8 schreibt](https://realpython.com/python-pep8/)
-   [Python Code dokumentieren: Ein vollständiger Leitfaden](https://realpython.com/documenting-python-code/).

## Konventionen

In dieser Dokumentation sollten einige Konventionen für Python Beispiele eingehalten werden.

Dies ist eine typische Funktionssignatur


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   Argumente mit Schlüsselwert Paaren sind optional, wobei der Standardwert in der Signatur angegeben ist. Das bedeutet, dass die folgenden Aufrufe gleichwertig sind:


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


:   In diesem Beispiel hat das erste Argument keinen Standardwert, daher sollte es immer einbezogen werden.

-   Wenn die Argumente mit dem expliziten Schlüssel angegeben werden, können die optionalen Argumente in beliebiger Reihenfolge angegeben werden. Das bedeutet, dass die folgenden Aufrufe gleichwertig sind:


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   Pythons Richtlinien betonen die Lesbarkeit von Code; insbesondere sollten Klammern unmittelbar auf den Funktionsnamen folgen, und ein Leerzeichen sollte einem Komma folgen.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   Wenn Code über mehrere Zeilen gebrochen werden muss, sollte dies mit einem Komma in Klammern oder Klammern erfolgen; die zweite Zeile sollte mit der vorherigen übereinstimmen.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   Funktionen können ein Objekt zurückgeben, das als Basis für eine andere Zeichenfunktion verwendet werden kann.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```

## Importe

Python Funktionen werden in Dateien gespeichert, die Module genannt werden. Bevor eine Funktion in diesem Modul verwendet wird, muss das Modul mit dem Befehl `import` in das Dokument aufgenommen werden.

Dies erzeugt vorangestellte Funktionen, d.h. `module.function()`. Dieses System verhindert Namenskonflikte mit Funktionen, die zwar den gleichen Namen tragen, aber aus verschiedenen Modulen stammen. Beispielsweise können die beiden Funktionen `Arch.make_window()` und `myModule.make_window()` problemlos nebeneinander existieren.

Vollständige Beispiele sollten die notwendigen Importe und die vorangestellten Funktionen beinhalten.


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



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [API](Category_API.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Python/de
