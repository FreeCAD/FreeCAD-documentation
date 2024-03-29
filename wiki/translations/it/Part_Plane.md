---
 GuiCommand:
   Name: Part Plane
   Name/it: Part Piano
   MenuLocation: Parte , Part_Primitives/it , Piano
   Workbenches: Part_Workbench/it, OpenSCAD_Workbench/it
   SeeAlso: Part_Primitives/it
---

# Part Plane/it



## Descrizione

Un <img alt="" src=images/Part_Plane.svg  style="width:24px;"> **Part Piano** è un piano rettangolare parametrico che può essere creato con il comando <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Part Primitive](Part_Primitives/it.md). Nel sistema di coordinate definito dalla sua proprietà **Placement**, il piano giace sul piano XY con l\'angolo anteriore sinistro all\'origine e il bordo anteriore parallelo all\'asse X.

<img alt="" src=images/Part_Plane_Example.png  style="width:400px;">



## Utilizzo

Vedere [Part Primitive](Part_Primitives/it#Utilizzo.md).



## Esempio

![Part Piano dall\'esempio di scripting](images/Part_Plane_Scripting_Example.png )

Qui viene mostrato un oggetto Part Piano creato con l\'[esempio di scripting](#Script.md) riportato di seguito.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Piano deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Attachment}}

L\'oggetto ha le stesse proprietà di collegamento di un [Part Part2DObject](Part_Part2DObject/it#Dati.md).


{{TitleProperty|Plane}}

-    **Length|Length**: la lunghezza del piano. Questa è la dimensione nella sua direzione X. Il valore predefinito è {{Value|10mm}}.

-    **Width|Length**: la larghezza del piano. Questa è la dimensione nella sua direzione Y. Il valore predefinito è {{Value|10mm}}.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Script di Part](Part_scripting/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

È possibile creare una Part Piano con il metodo {{Incode|addObject()}} del documento:


```python
plane = FreeCAD.ActiveDocument.addObject("Part::Plane", "myPlane")
```

-   Dove {{Incode|"myPlane"}} è il nome dell\'oggetto.
-   La funzione restituisce l\'oggetto appena creato.

Esempio:


```python
import FreeCAD as App

doc = App.activeDocument()

plane = doc.addObject("Part::Plane", "myPlane")
plane.Length = 4
plane.Width = 8
plane.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(20, 75, 60))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/it
