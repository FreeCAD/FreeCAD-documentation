---
 GuiCommand:
   Name: Part_Circle
   Name/it: Part Cerchio
   MenuLocation: Parte , Part_Primitives/it , Cerchio
   Workbenches: Part_Workbench/it, OpenSCAD_Workbench/it
   SeeAlso: Part_Primitives/it
---

# Part Circle/it



## Descrizione

Un <img alt="" src=images/Part_Circle.svg  style="width:24px;"> **Part Cerchio** è una forma parametrica che può essere creata con il comando <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Part Primitive](Part_Primitives/it.md) . Nel sistema di coordinate definito dalla sua proprietà **Placement**, il cerchio giace sul piano XY con il centro nell\'origine.

Un Part Cerchio è infatti un arco circolare chiuso in senso antiorario, può essere trasformato in un arco modificando le sue proprietà **Angle1** e/o **Angle2**.

<img alt="" src=images/Part_Circle_Example.png  style="width:400px;">



## Utilizzo

Vedere [Part Primitive](Part_Primitives/it#Utilizzo.md).

In alternativa è possibile creare un cerchio parziale selezionando tre punti:

1.  Nel pannello delle azioni del comando <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Primitive](Part_Primitives/it.md) selezionare l\'opzione **<img src="images/Part_Circle.svg" width=16px> Cerchio** dal menu a tendina.
2.  Premere il pulsante **Da tre punti**.
3.  Selezionare tre vertici nella [Vista 3D](3D_view/it.md). Non è necessario tenere premuto il tasto **Ctrl**.
4.  Viene creato un cerchio.
5.  I vertici selezionati vengono utilizzati solo al momento della creazione per calcolare il **Radius** e il **Placement** del cerchio.



## Esempio

![Part Cerchio dall\'esempio di scripting](images/Part_Circle_Scripting_Example.png )

Qui viene mostrato un oggetto Part Cerchio creato con l\'[esempio di scripting](#Script.md) riportato di seguito.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Cerchio deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Attachment}}

L\'oggetto ha le stesse proprietà di collegamento di un [Part Part2DObject](Part_Part2DObject/it#Dati.md).


{{TitleProperty|Base}}

-    **Radius|Length**: il raggio del cerchio o dell\'arco circolare. Il valore predefinito è {{Value|2mm}}.

-    **Angle1|Angle**: l\'angolo iniziale dell\'arco circolare. Intervallo valido: {{Value|0° &lt; valore &lt;&#61; 360°}}. Il valore predefinito è {{Value|0°}}.

-    **Angle2|Angle**: l\'angolo finale dell\'arco circolare. Intervallo valido: {{Value|0° &lt; valore &lt;&#61; 360°}}. Il valore predefinito è {{Value|360°}}. Se **Angle1** e **Angle2** sono uguali, o se un angolo è {{Value|0°}} e l\'altro {{Value|360°}}, viene creato un cerchio completo.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Script di Part](Part_scripting/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

È possibile creare una Part Cerchio con il metodo {{Incode|addObject()}} del documento:


```python
circle = FreeCAD.ActiveDocument.addObject("Part::Circle", "myCircle")
```

-   Dove {{Incode|"myCircle"}} è il nome dell\'oggetto.
-   La funzione restituisce l\'oggetto appena creato.

Esempio:


```python
import FreeCAD as App

doc = App.activeDocument()

circle = doc.addObject("Part::Circle", "myCircle")
circle.Radius = 10
circle.Angle1 = 45
circle.Angle2 = 225
circle.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 45, 10))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle/it
