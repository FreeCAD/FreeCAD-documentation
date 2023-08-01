---
- GuiCommand:
   Name:Std_SendToPythonConsole
   Name/it:Invia alla console Python
   MenuLocation:Modifica - Invia alla console Python
   Workbenches:Tutti
   Shortcut:**Ctrl**+**Maiusc**+**P**
   Version:0.19
---

# Std SendToPythonConsole/it



## Descrizione

Il comando **Invia alla console Python** crea variabili nella [console Python](Python_console/it.md) che fanno riferimento a un oggetto selezionato e alle sue forme secondarie selezionate, insieme ad altri riferimenti utili. Le variabili e il codice coinvolti possono essere utilizzati nello sviluppo del codice Python.

A seconda dell\'oggetto selezionato e delle sue forme secondarie selezionate, se presenti, vengono create le seguenti variabili:

+++
| Variable name   | Referenced object(s)                                                                                                                                   |
+=================+========================================================================================================================================================+
|  | Il documento contenente l\'oggetto selezionato                                                                                                         |
| {{Incode|doc}}  |                                                                                                                                                        |
|              |                                                                                                                                                        |
+++
|  | L\'oggetto Link selezionato (creato solo se l\'oggetto selezionato è un Link)                                                                          |
| {{Incode|lnk}}  |                                                                                                                                                        |
|              |                                                                                                                                                        |
+++
|  | A seconda dell\'oggetto selezionato:                                                                                                                   |
| {{Incode|obj}}  | L\'oggetto selezionato stesso (se l\'oggetto selezionato non è un collegamento)                                                                        |
|              | L\'oggetto collegato (se l\'oggetto selezionato è un collegamento)                                                                                     |
+++
|  | A seconda del tipo di {{Incode|obj}}:                                                                                                    |
| {{Incode|shp}}  | La proprietà {{Incode|Shape}} di {{Incode|obj}} (per oggetti derivati ​​dalla classe                                         |
|              | {{Incode|Part::Feature}})                                                                                                                |
|                 | La proprietà {{Incode|Mesh}} di {{Incode|obj}} (per gli oggetti Mesh)                                                      |
|                 | La proprietà {{Incode|Points}} di {{Incode|obj}} (per oggetti Points)                                                      |
+++
|  | La prima forma secondaria selezionata (creata solo se è selezionata almeno una forma secondaria)                                                       |
| {{Incode|sub}}  |                                                                                                                                                        |
|              |                                                                                                                                                        |
+++
|  | Un elenco contenente tutte le forme secondarie (creato solo se sono selezionate due o più forme secondarie)                                            |
| {{Incode|subs}} |                                                                                                                                                        |
|              |                                                                                                                                                        |
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



*Esempio di output: un bordo, una faccia e un vertice di un [Link](Std_LinkMake/it.md) a un [Part Box](Part_Box/it.md) sono stati selezionati*



## Utilizzo

1.  Selezionare un singolo oggetto o una o più sottoforme appartenenti a un singolo oggetto.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_SendToPythonConsole.svg" width=16px> Invia alla console Python** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_SendToPythonConsole.svg" width=16px> Invia alla console Python** dal menu contestuale della [vista ad albero](Tree_view/it.md) o della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Ctrl**+**Maiusc**+**P**.
3.  Se necessario, si apre la [Python console](Python_console/it.md).
4.  La [Python console](Python_console/it.md) riceve il focus della tastiera.



## Note

-   Tutte le variabili create in precedenza vengono eliminate ogni volta che viene eseguito il comando.

-   Se l\'oggetto selezionato è un Link ({{Incode|App::Link}}) e l\'oggetto Linked è derivato dalla classe {{Incode|Part::Feature}}, la variabile {{Incode|shp}} sarà la forma dell\'oggetto collegato. Se il Link è stato trasformato o ridimensionato e si vuole accedere alla forma ridimensionata/trasformata, lo si può fare con questo codice:

:   
    
```pythonlnk_shp = Part.getShape(lnk)```
    





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SendToPythonConsole/it
