# Part Cylinder/it
---
- GuiCommand:/it   Name:Part Cylinder   Name/it:Cilindro   MenuLocation:Parte → Primitive → Cilindro   Workbenches:[SeeAlso:[[Part_CreatePrimitives/it|Crea primitive](Part_Workbench/it___Parte]].md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Crea un cilindro parametrico. Attualmente, nell\'ambiente Parte, ci sono due modi per creare un cilindro.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Attivare l\'ambiente **<img src="images/Workbench_Part.svg" width=16px> [Parte](Part_Workbench/it.md)**.
2.  Richiamare il comando Cilindro in uno di questi modi:
    -   Premere il pulsante **<img src="images/Part_Cylinder.svg" width=24px>
**
    -   Usare **Part → Primitive → Cilindro** dal menu principale.


</div>


<div class="mw-translate-fuzzy">

**Risultato:** Un cilindro pieno centrato su una faccia coincidente con l\'origine globale (punto 0,0,0), con un raggio di 2 mm e un\'altezza di 10 mm.


</div>

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="a cylinder created with the Cylinder tool" src=images/cylinder.png  style="width:650px;">


<div class="mw-translate-fuzzy">

## Opzioni

Le proprietà possono essere successivamente modificate nella scheda dati del cilindro:


</div>

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small> 

## Scripting

A Part Cylinder can be created using the following function:


```python
cylinder = FreeCAD.ActiveDocument.addObject("Part::Cylinder", "myCylinder")
```

-   Where {{Incode|"myCylinder"}} is the name for the object.
-   The function returns the newly created object.


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/it
