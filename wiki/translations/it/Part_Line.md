---
 GuiCommand:
   Name: Part_Line
   Name/it: Part Linea
   MenuLocation: Parte , Part_Primitives/it , Linea
   Workbenches: Part_Workbench/it, OpenSCAD_Workbench/it
   SeeAlso: Part_Primitives/it
---

# Part Line/it



## Descrizione

Una <img alt="" src=images/Part_Line.svg  style="width:24px;"> **Part Linea** è una linea parametrica che può essere creata con il comando <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Part Primitive](Part_Primitives/it.md). Le coordinate dei punti iniziale e finale sono relative al sistema di coordinate definito dalla proprietà **Placement**.

<img alt="" src=images/Part_Line_Example.png  style="width:400px;">



## Utilizzo

Vedere [Part Primitive](Part_Primitives/it#Utilizzo.md).



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Linea deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Attachment}}

L\'oggetto ha le stesse proprietà di collegamento di un [Part Part2DObject](Part_Part2DObject/it#Dati.md).


{{TitleProperty|Vertex 1 - Start}}

-    **X1|Distance**: la coordinata X del punto iniziale della linea. Il valore predefinito è {{Value|0mm}}.

-    **Y1|Distance**: la coordinata Y del punto iniziale della linea. Il valore predefinito è {{Value|0mm}}.

-    **Z1|Distance**: la coordinata Z del punto iniziale della linea. Il valore predefinito è {{Value|0mm}}.


{{TitleProperty|Vertex 2 - Finish}}

-    **X2|Distance**: la coordinata X del punto finale della linea. Il valore predefinito è {{Value|10mm}}.

-    **Y2|Distance**: la coordinata Y del punto finale della linea. Il valore predefinito è {{Value|10mm}}.

-    **Z2|Distance**: la coordinata Z del punto finale della linea. Il valore predefinito è {{Value|10mm}}.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Script di Part](Part_scripting/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

È possibile creare una Part Linea con il metodo {{Incode|addObject()}} del documento:


```python
line = FreeCAD.ActiveDocument.addObject("Part::Line", "myLine")
```

-   Dove {{Incode|"myLine"}} è il nome dell\'oggetto.
-   La funzione restituisce l\'oggetto appena creato.

Esempio:


```python
import FreeCAD as App

doc = App.activeDocument()

line = doc.addObject("Part::Line", "myLine")
line.X1 = 1
line.Y1 = 3
line.Z1 = 6
line.X2 = 2
line.Y2 = 3
line.Z2 = 9

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Line/it
