---
 GuiCommand:
   Name: Sketcher ToggleActiveConstraint
   Name: Sketcher Attiva/disattiva vincolo
   Workbenches: Sketcher_Workbench/it
   MenuLocation: Schizzo , Vincoli Sketcher , Attiva/disattiva vincolo
   Shortcut: **K** **Z**
   Version: 0.19
   SeeAlso: Sketcher_ToggleDrivingConstraint/it
---

# Sketcher ToggleActiveConstraint/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:24px;"> [Sketcher Attiva/disattiva vincolo](Sketcher_ToggleActiveConstraint/it.md) attiva o disattiva i vincoli selezionati. La disattivazione dei vincoli consente di testare altre disposizioni geometriche senza eliminare i vincoli.

Questo strumento è simile a [Sketcher Attiva/disattiva vincolo di guida/riferimento](Sketcher_ToggleDrivingConstraint/it.md), ma contrariamente a quello strumento funziona anche per i vincoli geometrici ed i valori dei vincoli dimensionali disattivati ​​vengono conservati.



## Utilizzo

1.  Selezionare uno o più vincoli.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> [Attiva/disattiva vincolo](Sketcher_ToggleActiveConstraint/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Attiva/disattiva vincolo** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Attiva/disattiva vincolo** dalla menu contestuale.

    -   Nella sezione **Vincolo** della [Finestra di dialogo Sketchcher](Sketcher_Dialog/it.md) selezionare l\'opzione **Attiva** o **Disattiva** dal menu contestuale. L\'opzione offerta dipende dallo stato del vincolo sotto il cursore.

    -   Usare la scorciatoia da tastiera: **K** quindi **Z**.
3.  I vincoli selezionati attivi vengono disattivati ​​e diventano grigi (predefinito [color](Sketcher_Preferences/it#Appearance.md)), mentre i vincoli selezionati disattivati ​​vengono attivati ​​e tornano al rosso (colore predefinito).



## Esempio

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:400px;"> 
*Uno schizzo completamente vincolato‎.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:400px;"> 
*Uno dei vincoli angolari è stato disattivato, lo schizzo non è più completamente vincolato.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:400px;"> 
*La geometria non vincolata può essere spostata. Il vincolo disattivato è ancora disponibile e può essere riattivato per ritornare allo schizzo completamente vincolato.*



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo stato attivo di un vincolo può essere controllato in [macro](macros/it.md) e dalla [Console Python](Python_console/it.md). 
```python
SketchObject.toggleActive(index)
```

Utilizzare il metodo `toggleActive` di un [Oggetto schizzo](Sketcher_SketchObject/it.md) esistente e l\'`index` del vincolo per attivarlo o disattivarlo. L\'indice inizia da `0` fino a `N-1`, dove `N` è il numero totale di vincoli.

Esempio: 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/it
