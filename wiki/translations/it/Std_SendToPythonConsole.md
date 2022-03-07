---
- GuiCommand:/it
   Name:Std_SendToPythonConsole
   Name/it:Invia alla console Python
   MenuLocation:Modifica → Invia alla console Python
   Workbenches:Tutti
   Shortcut:**Ctrl**+**Maiusc**+**P**
   Version:0.19
---

# Std SendToPythonConsole/it

## Descrizione


<div class="mw-translate-fuzzy">

Il comando **Invia alla console Python** crea una variabile nel [console Python](Python_console/it.md) che fa riferimento a un oggetto selezionato. Se viene selezionata una sottoforma dell\'oggetto, vengono create due variabili aggiuntive, una che fa riferimento alla forma dell\'oggetto e l\'altra che fa riferimento alla sottoforma stessa. Le variabili e il codice in questione possono essere utilizzati per sviluppare il codice Python.


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



*Esempio di output: è stato selezionato un bordo di un [cubo di Part](Part_Box/it.md)*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un singolo oggetto.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_SendToPythonConsole.svg" width=16px> Invia alla console Python** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_SendToPythonConsole.svg" width=16px> Invia alla console Python** dal menu contestuale della [vista ad albero](Tree_view/it.md) o della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Ctrl**+**Maiusc**+**P**.


</div>

## Notes

-   All previously created variables are deleted each time the command is run.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SendToPythonConsole/it
