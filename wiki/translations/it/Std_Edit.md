---
- GuiCommand:/it
   Name:Std_Edit
   Name/it:Attiva/disattiva la modalità modifica
   MenuLocation:Modifica → Attiva/disattiva la modalità modifica
   Workbenches:Tutti
---

# Std Edit/it


</div>

## Descrizione

Il comando **Std Edit** attiva o disattiva la modalità di modifica di un oggetto.

## Utilizzo

1.  Se nessun oggetto è in modalità modifica: selezionare un singolo oggetto.
2.  Selezionare l\'opzione **Modifica → <img src="images/Std_Edit.svg" width=16px> Attiva/disattiva la modalità modifica** dal menu.
3.  La modalità di modifica dell\'oggetto selezionato viene attivata o disattivata.

## Note


<div class="mw-translate-fuzzy">

-   Non tutti i tipi di oggetto hanno una modalità di modifica.
-   Le funzioni disponibili in modalità modifica dipendono dal tipo di oggetto.
-   La modalità di modifica può essere attivata anche facendo doppio clic su un oggetto nella [Vista ad albero](Tree_view/it.md).


</div>

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per attivare la modalità di modifica di un oggetto, utilizzare il metodo `setEdit` dell\'oggetto documento. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

The second argument is the EditMode. The following options are available:

0 = Default
1 = Transform
2 = Cutting
3 = Color

Per disattivare la modalità di modifica di un oggetto, utilizzare il metodo `resetEdit` dell\'oggetto documento.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std Edit/it
