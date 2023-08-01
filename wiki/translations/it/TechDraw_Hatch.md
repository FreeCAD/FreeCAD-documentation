# TechDraw Hatch/it
---
- GuiCommand:   Name: TechDraw Hatch   Name/it: Tratteggio da modello   Workbenches: [MenuLocation: TechDraw - Tratteggio da modello   Shortcut:    SeeAlso: [[TechDraw_GeometricHatch/it|Tratteggio geometrico](TechDraw_Workbench/it___TechDraw]].md), [Tipi di tratteggio](TechDraw_Hatching/it.md)---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Tratteggio da modello riempie una regione chiusa di una vista con un modello di tratteggio. I modelli possono essere in file formato [SVG](SVG/it.md) o [bitmap](bitmap/it.md). Al contrario lo strumento <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md) utilizza un file di pattern PAT specifico, vedere i [tipi di tratteggio](TechDraw_Hatching/it.md) per i dettagli.


</div>

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*Esempio di tratteggio SVG su una faccia*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una regione chiusa in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_Hatch.svg" width=16px> [Tratteggio da modello](TechDraw_Hatch/it.md)**.
3.  Si apre una finestra di dialogo in cui è possibile selezionare il motivo, una scala per il motivo, uno spessore di linea e il colore.


</div>



## Note


<div class="mw-translate-fuzzy">

-   Il tratteggio è vulnerabile al problema della \"[denominazione topologica](Topological_naming_problem/it.md)\". Per maggiori informazioni vedere lo strumento [Lunghezza](TechDraw_LengthDimension/it.md). La pratica migliore è di posticipare il tratteggio fino a quando il disegno non è stabile.
-   Esempi di [SVG](SVG/it.md) sono disponibili localmente in:


</div>


:   
    
```python
    $INSTALL_DIR/data/Mod/TechDraw/Patterns
    
```
    


<div class="mw-translate-fuzzy">

dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio


</div>


:   
    
```python
    /usr/share/freecad/data/Mod/TechDraw/Patterns
    
```
    


<div class="mw-translate-fuzzy">

e anche in [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).


</div>



## Proprietà

-    {{PropertyData/it|Source}}: La vista e la faccia che devono ricevere il tratteggio.

-    {{PropertyData/it|Hatch Pattern}}: Il percorso completo e il nome del file del modello SVG.

-    {{PropertyView/it|Hatch Color}}: Il colore in cui viene visualizzato il tratteggio.

-    {{PropertyView/it|Hatch Scale}}: Modifica la dimensione del modello di tratteggio.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Hatch può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
hatch = FreeCAD.ActiveDocument.addObject("TechDraw::DrawHatch", "Hatch")
hatch.Source = (view1, ["Face0"])
hatch.HatchPattern = hatchFileSpec
page.addView(hatch)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/it
