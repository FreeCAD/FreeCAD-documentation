# Part Cone/it
---
- GuiCommand:/it   Name:Part Cone   Name/it:Cono   MenuLocation:Parte → Primitive → Cono   Workbenches:[SeeAlso:[[Part_CreatePrimitives/it|Crea primitive](Part_Workbench/it___Parte]].md)---


</div>

## Descrizione

Crea un tronco di cono parametrico.

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;">


<div class="mw-translate-fuzzy">



*Sopra: un cono di Parte con il parametro "Angolo" impostato su 270° e tutti gli altri parametri con i valori predefiniti.*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Attivare l\'ambiente **<img src="images/Workbench_Part.svg" width=16px> [Parte](Part_Workbench/it.md)**.
2.  Richiamare il comando Cono in uno di questi modi:
    -   Premere il pulsante <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Cono](Part_Cone/it.md)
    -   Usare **Part → Primitive → Cono** dal menu principale.


</div>


<div class="mw-translate-fuzzy">

**Risultato:** I valori predefiniti creano un tronco di cono parametrico, definito dai parametri `Radius1`, `Radius2`, `Height` e `Angle`. Il cono predefinito viene posizionato nell\'origine (punto 0,0,0) al momento della creazione. Il parametro angolo consente la creazione di una porzione di cono (è impostato di default a 360°) e il raggio 1 e 2 corrispondono al raggio base e superiore del tronco di cono.


</div>

The cone properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cone in the [Tree view](Tree_view.md).


<div class="mw-translate-fuzzy">

## Opzioni

+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/PartConeProperty_en.png ) |                                                                                                                                                                                         |
|                                                        | **Cone**                                                                                                                                                                                           |
|                                                        |                                                                                                                                                                                                     |
|                                                        | -   **Radius 1:** raggio dell\'arco o del cerchio che definisce la faccia inferiore                                                                                                                    |
|                                                        | -   **Radius 2:** raggio dell\'arco o del cerchio che definisce la faccia superiore                                                                                                                    |
|                                                        | -   **Height:** l\'altezza del cono                                                                                                                                                                    |
|                                                        | -   **Angle:** il numero di gradi dell\'arco che definisce le facce superiore e inferiore del cono. Il valore 360° predefinito crea facce circolari, un valore inferiore crea una porzione di un cono. |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>

-    **Radius 1**: Radius of the arc or circle defining the lower face

-    **Radius 2**: Radius of the arc or circle defining the upper face

-    **Height**: Height of the Part Cone

-    **Angle**: Number of degrees of the arc or circles defining the upper and lower faces of the truncated cone. The default 360° creates circular faces, a lower value will create a portion of a cone as defined by upper and lower faces each with edges defined by an arc of the number of degrees and two radii.

## Scripting

A Part Cone can be created using the following function:


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Where {{Incode|"myCone"}} is the name for the object.
-   The function returns the newly created object.


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/it
