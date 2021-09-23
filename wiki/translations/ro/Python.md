# Python/ro



<div class="mw-translate-fuzzy">


**(November 2018) 
FreeCAD a fost proiectat inițial pentru a lucra cu Python 2. Multe funcții lucrează cu Python 3, dar unele nu funcționează. Efectuarea suportului deplin al FreeCAD Python 3 este o lucrare în desfășurare.**


</div>

## Descriere


{{TOCright}}

[Python](https://www.python.org) este un limbaj de programare cu scop general, care este foarte frecvent utilizat în aplicații mari pentru a automatiza anumite sarcini prin crearea de scripturi sau [macros](macros/ro.md).

În programul FreeCAD, codul Python poate fi folosit pentru a crea diverse elemente programabil, fără a fi nevoie să faceți clic pe interfața grafică a utilizatorului. În plus, multe instrumente și ateliere de lucru ale programului FreeCAD sunt programate în Python.

A se vedea [Introduction to Python](Introduction_to_Python/ro.md) pentru a afla despre limbajul de programare Python și apoi [Python scripting tutorial](Python_scripting_tutorial/ro.md) și [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/ro.md) pentru a porni scripting-ul în FreeCAD.

## Readability


<div class="mw-translate-fuzzy">

Atunci când se scrie codul în Python, este de preferat să se urmeze [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).


</div>

These documents present explanations in a more user-friendly way:

-   [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
-   [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/).

## Convenții

În această documentație, ar trebui urmate câteva convenții pentru exemplele Python.

Aceasta este o semnătură tipică a funcției


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   Argumentele cu perechi cheie-valoare sunt opționale, cu valoarea implicită indicată în semnătură. Aceasta înseamnă că următoarele apeluri sunt echivalente:


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


:   În acest exemplu, primul argument nu are o valoare implicită, așa că trebuie întotdeauna inclus.

-   Atunci când argumentele sunt date cu cheia explicită, argumentele opționale pot fi date în orice ordine. Aceasta înseamnă că următoarele apeluri sunt echivalente:


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   Normele lui Python subliniază lizibilitatea codului; în special, parantezele trebuie să urmeze imediat numele funcției, iar un spațiu trebuie să urmeze după o virgulă.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   Dacă codul trebuie să fie rupt în mai multe rânduri, acest lucru trebuie făcut cu o virgulă între paranteze pătrate sau paranteze; a doua linie trebuie aliniată cu cea anterioară.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   Funcțiile pot returna un obiect care poate fi folosit ca bază a unei alte funcții de desen.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```

## Importuri

Funcțiile Python sunt stocate în fișiere numite module. Înainte de a utiliza orice funcție din modulul respectiv, modulul trebuie inclus în document cu instrucțiunea `import`.


<div class="mw-translate-fuzzy">

Aceasta creează funcții prefixate, `module.function()`. Acest sistem previne conflictele de nume cu funcții numite aceleași, dar care provin de la diferite module. De exemplu, două funcții `Arch.makeWindow()` și `myModule.makeWindow()` pot coexista fără probleme.


</div>

Exemplele complete ar trebui să includă importurile necesare și funcțiile prefixate.


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
