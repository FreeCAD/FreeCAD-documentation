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

Il comando **Invia alla console Python** crea una variabile nel [console Python](Python_console/it.md) che fa riferimento a un oggetto selezionato. Se viene selezionata una sottoforma dell\'oggetto, vengono create due variabili aggiuntive, una che fa riferimento alla forma dell\'oggetto e l\'altra che fa riferimento alla sottoforma stessa. Le variabili e il codice in questione possono essere utilizzati per sviluppare il codice Python.

>>> ### Begin command Std_SendToPythonConsole
>>> obj = App.getDocument("Unnamed").getObject("Box")
>>> shp = App.getDocument("Unnamed").getObject("Box").Shape
>>> elt = App.getDocument("Unnamed").getObject("Box").Shape.Edge8
>>> ### End command Std_SendToPythonConsole



*Esempio di output: è stato selezionato un bordo di un [cubo di Part](Part_Box/it.md)*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un singolo oggetto.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_SendToPythonConsole.svg" width=16px> Invia alla console Python** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_SendToPythonConsole.svg" width=16px> Invia alla console Python** dal menu contestuale della [vista ad albero](Tree_view/it.md) o della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Ctrl**+**Maiusc**+**P**.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SendToPythonConsole/it
