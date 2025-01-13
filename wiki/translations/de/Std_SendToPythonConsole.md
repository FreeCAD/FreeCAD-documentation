---
 GuiCommand:
   Name: Std SendToPythonConsole
   Name/de: Std AnPythonKonsoleSenden
   MenuLocation: Bearbeiten ,  An Python-Konsole senden
   Workbenches: Alle
   Shortcut: **Ctrl**+**Shift**+**P**
   Version: 0.19
---

# Std SendToPythonConsole/de



## Beschreibung

Der Befehl **Std AnPythonKonsoleSenden** erstellt Variablen in der [Python-Konsole](Python_console/de.md), die auf ein ausgewähltes Objekt und auf seine ausgewählten Teilformen verweisen, zusammen mit ein paar nützlichen anderen Referenzen. Die Variablen und der dazugehörige Kode können zur Entwicklung von Python-Skripten verwendet werden.

Abhängig von dem ausgewählten Objekt und seiner ausgewählten Teilformen, falls vorhanden, werden die folgenden Variablen erstellt:

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



*Beispielausgabe: eine Kante, eine Fläche und ein Eckpunkt eines [Part Würfels](Part_Box/de.md) wurden ausgewählt*



## Anwendung

1.  Ein einzelnes Objekt oder eine bzw. mehrere Teilformen, die zu einem einzelnen Objekt gehören, auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Bearbeiten → <img src="images/Std_SendToPythonConsole.svg" width=16px> An Python-Konsole senden** auswählen.
    -   Den Menüeintrag **<img src="images/Std_SendToPythonConsole.svg" width=16px> An Python-Konsole senden** aus dem Kontextmenü der [Baumansicht](Tree_view/de.md) oder dem Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Das Tastaturkürzel **Strg**+**Shift**+**P**.
3.  Falls erforderlich öffnet sich die [Python-Konsole](Python_console/de.md).
4.  Die [Python-Konsole](Python_console/de.md) erhält den Fokus der Tastatur.



## Hinweise

-   Jedes Mal, wenn der Befehl ausgeführt wird, werden alle vorher erzeugten Variablen gelöscht.

-   If the selected object is a Link ({{Incode|App::Link}}) and the Linked object is derived from the {{Incode|Part::Feature}} class, the {{Incode|shp}} variable will be the shape of the Linked object. If the Link has been transformed or scaled and you want to access the scaled/transformed shape, you can do so with this code:

:   
    
```pythonlnk_shp = Part.getShape(lnk)```
    





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std SendToPythonConsole/de
