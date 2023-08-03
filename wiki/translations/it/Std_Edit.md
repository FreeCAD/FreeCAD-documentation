---
 GuiCommand:
   Name: Std_Edit
   Name/it: Modalità modifica
   MenuLocation: Modifica , Attiva/disattiva Modalità modifica
   Workbenches: Tutti
---

# Std Edit/it



## Descrizione

Il comando **Std Edit** attiva o disattiva la modalità di modifica di un oggetto.



## Utilizzo

1.  Se nessun oggetto è in modalità modifica: selezionare un singolo oggetto.
2.  Selezionare l\'opzione **Modifica → <img src="images/Std_Edit.svg" width=16px> Attiva/disattiva la modalità modifica** dal menu.
3.  Viene attivata la modalità di modifica predefinita dell\'oggetto selezionato o viene disattivata la modalità di modifica esistente.



## Note

-   Alcuni strumenti saranno disabilitati (in grigio) nell\'interfaccia utente mentre è attiva la modalità di modifica di un oggetto.
-   Non tutti i tipi di oggetto hanno una modalità di modifica.
-   Le funzioni disponibili in modalità modifica dipendono dal tipo di oggetto.
-   La modalità di modifica di un oggetto può essere attivata anche facendo doppio clic su di esso nella [Vista albero](Tree_view/it.md). In tal caso la modalità di modifica utilizzata può essere definita con il comando [Impostazione modalità Modifica](Std_UserEditMode/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per attivare la modalità di modifica di un oggetto, utilizzare il metodo `setEdit` dell\'oggetto documento. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

Il secondo argomento è EditMode. Sono disponibili le seguenti opzioni:

0 = Predefinito
1 = Trasforma
2 = Taglio
3 = Colore

Per disattivare la modalità di modifica di un oggetto, utilizzare il metodo `resetEdit` dell\'oggetto documento.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Edit/it
