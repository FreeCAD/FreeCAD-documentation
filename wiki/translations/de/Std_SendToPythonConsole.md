---
- GuiCommand:/de
   Name:Std SendToPythonConsole
   Name/de:Std SendeAnPythonKonsole
   MenuLocation:Bearbeiten → Sende an Python Konsole
   Workbenches:Alle
   Shortcut:**Ctrl**+**Shift**+**P**
   Version:0.19
---

# Std SendToPythonConsole/de

## Beschreibung


<div class="mw-translate-fuzzy">

Der **Std SendeAnPythonKonsole** Befehl erstellt eine Variable in der [Python Konsole](Python_console/de.md), die auf ein ausgewähltes Objekt verweist. Wenn eine Unterform des Objekts ausgewählt wird, werden zwei zusätzliche Variablen erstellt, von denen eine auf die Form des Objekts und die andere auf die Unterform selbst verweist. Die Variablen und der damit verbundene Code können zur Entwicklung von Python Code verwendet werden.


</div>

Depending on the selected object and its selected subshapes, if any, the following variables are created:

+++
| Variable name   | Referenced object(s)                                                                                                                                    |
+=================+=========================================================================================================================================================+
|  | The document containing the selected object                                                                                                             |
| {{Incode|doc}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | The selected Link object (only created if the selected object is a Link)                                                                                |
| {{Incode|lnk}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | Depending on the selected object:                                                                                                                       |
| {{Incode|obj}}  | The selected object itself (if the selected object is not a Link)                                                                                       |
|              | The Linked object (if the selected object is a Link)                                                                                                    |
+++
|  | Depending on the type of {{Incode|obj}}:                                                                                                  |
| {{Incode|shp}}  | The {{Incode|Shape}} property of {{Incode|obj}} (for objects derived from the {{Incode|Part::Feature}} class) |
|              | The {{Incode|Mesh}} property of {{Incode|obj}} (for Mesh objects)                                                           |
|                 | The {{Incode|Points}} property of {{Incode|obj}} (for Points objects)                                                       |
+++
|  | The first selected subshape (only created if at least one subshape is selected)                                                                         |
| {{Incode|sub}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | A list containing all subshapes (only created if two or more subshapes are selected)                                                                    |
| {{Incode|subs}} |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++

>>> ### Begin command Std_SendToPythonConsole
>>> try:
>>>     del(doc,lnk,obj,shp,sub,subs)
>>> except Exception:
>>>     pass
>>> 
>>> doc = App.getDocument("Unnamed")
>>> lnk = doc.getObject("Link")
>>> obj = lnk.getLinkedObject()
>>> shp = obj.Shape
>>> sub = obj.getSubObject("Edge10")
>>> subs = [obj.getSubObject("Edge10"),obj.getSubObject("Face3"),obj.getSubObject("Vertex5"),]
>>> ### End command Std_SendToPythonConsole


<div class="mw-translate-fuzzy">



*Beispielausgabe: eine Kante eines [Part Quaders](Part_Box/de.md) wurde ausgewählt*


</div>

## Verwendung


<div class="mw-translate-fuzzy">

1.  Wähle ein einzelnes Objekt aus.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Wähle die **Bearbeiten → <img src="images/Std_SendToPythonConsole.svg" width=16px> Sende an Python Konsole** Option aus dem Menü.
    -   Wähle die Option {{MenuCommand/de|<img src="images/Std_SendToPythonConsole.svg" width=16px> Sende an Python Konsole}} Option aus dem [Baumansicht](Tree_view/de.md) Kontextmenü oder [3D Ansicht](3D_view/de.md) Kontextmenü.
    -   Verwende die Tastaturkürzel: **Strg**+**Shift**+**P**.


</div>

## Notes

-   All previously created variables are deleted each time the command is run.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SendToPythonConsole/de
