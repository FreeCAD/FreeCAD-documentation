---
- GuiCommand:
   Name: Std UserEditMode
   Name/it: Impostazioni Modalità modifica
   MenuLocation: Modifica -> Impostazione modalità modifica -> ...
   Workbenches: Tutti
   Version: 0.20
   SeeAlso: Std_Edit/it
---

# Std UserEditMode/it



## Descrizione

Il comando **Impostazione Modalità modifica** definisce la modalità di modifica da utilizzare quando si fa doppio clic su un oggetto nella [Vista albero](Tree_view/it.md).



## Utilizzo

1.  Nel menu andare su **Modifica → Impostazioni Modalità modifica** e selezionare una modalità di modifica.



## Modalità di modifica disponibili 



### <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> Predefinito 

L\'oggetto verrà modificato utilizzando la sua modalità predefinita. Questa modalità di modifica è definita internamente per essere la più appropriata per il tipo di oggetto. Ad esempio, sarà la modifica delle proprietà della forma per [Part primitive](Part_Primitives/it.md) e [PartDesign features](PartDesign_Feature/it.md), la modifica del posizionamento per [Part booleans](Part_Boolean/it.md), ecc.



### <img alt="" src=images/Std_UserEditModeTransform.svg  style="width:24px;"> Trasforma 

L\'oggetto avrà il suo posizionamento modificabile con il comando [Trasforma](Std_TransformManip/it.md).



### <img alt="" src=images/Std_UserEditModeCutting.svg  style="width:24px;"> Taglio 

Questa modalità di modifica è implementata come disponibile ma attualmente non sembra essere utilizzata da nessun oggetto.



### <img alt="" src=images/Std_UserEditModeColor.svg  style="width:24px;"> Colore 

L\'oggetto avrà il colore delle sue singole facce modificabile con il comando [Impostare il colore delle facce](Part_FaceColors/it.md).



## Note

-   Non tutti gli oggetti supportano tutte le modalità di modifica. Se la modalità selezionata non è supportata dall\'oggetto, verrà utilizzata la sua modalità di modifica predefinita.



## Preferenze

-   L\'ultima modalità di modifica è memorizzata: **Strumenti → Modifica parametri... → BaseApp → Preferenze → Generale → UserEditMode**. È un valore intero. I valori possibili sono {{Incode|0}} (Predefinito), {{Incode|1}} (Trasforma), {{Incode|2}} (Taglio) o {{Incode|3}} (Colore). Il valore predefinito è {{Incode|0}}.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per elencare le modalità di modifica disponibili:


```python
import FreeCADGui
FreeCADGui.listUserEditModes()
```

Per ottenere la modalità di modifica attiva:


```python
import FreeCADGui
FreeCADGui.getUserEditMode()
```

Per impostare la modalità di modifica attiva:


```python
import FreeCADGui
FreeCADGui.setUserEditMode(MODENAME) # Where MODENAME is a string available in the list of edit modes
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std UserEditMode/it
