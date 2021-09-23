---
- GuiCommand:/ro
   Name/ro:TechDraw Dimension Link
   MenuLocation:TechDraw → Dimension Link
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw NewView](TechDraw_NewView.md), [TechDraw NewProjGroup](TechDraw_NewProjGroup.md)
---

# TechDraw LinkDimension/ro


</div>

## Descriere

Instrumentul Dimension Link crează o legătură între geometria 3D și 1 sau mai multe Dimensiuni pe o Pagină. Legătura permite Dimensiunii să utilizeze valorile 3D actuale în locul valorilor proiectate 2D.

The Link Dimension tool creates a link between 3D geometry and one or more existing projected Dimensions on a Page. This link allows the Dimension to use actual 3D values instead of 2D projected values.

The Link Dimension tool\'s most common use is in dimensioning isometric views in a ProjectionGroup. The projected length of an Edge in an isometric view will, of course, not necessarily equal the actual length of the Edge. In an orthogonal view the projected and actual lengths will be equal.

The link instructs the Dimension to compute it\'s value directly from the 3D geometry.

## Cum se folosește 

1.  Creați Dimensiunea dvs. pe pagina de desen, ca de obicei.
2.  Selectați geometria (ex Edge) în vizualizarea modelului 3D care se potrivește dimensiunilor dvs..
3.  Apăsați butonul **<img src="images/TechDraw_Dimension_Link.png" width=24px> [Dimension Link](TechDraw_Dimension_Link.md)
**
4.  Se va deschide un dialog. Selectați 1 sau mai multe Dimensiuni care să se lege la geometria 3D selectată.
5.  Apăsați \"OK\"




1.  Create an appropriate dimension on the drawing page using any of [TechDraw LengthDimensionh](TechDraw_LengthDimension.md), [TechDraw HorizontalDimension](TechDraw_HorizontalDimension.md), etc. This dimension will be in the right place on the Page, but will show the projected dimension value.
2.  Select the geometry in the 3D view, for example, an edge, that corresponds to the projected geometry of your dimension.
3.  Press the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link Dimension](TechDraw_LinkDimension.md)** button.
4.  A dialog will open. Select one or more Dimensions to be linked to the selected 3D geometry.
5.  Press **OK**.

After the link operation is completed the **MeasureType** property of the dimension changes from `Projected` to `True`.

## Limitări

1.  Legăturile dimensionale sunt foarte sensibile la problema \"Topological Naming\". Se recomandă să conectați dimensiunile la unul din ultimii pași ai procesului dvs.
2.  Instrumentul Link nu vă împiedică să creați legături ilogice.
3.  În prezent, nu există nicio modalitate de rupere a unui link. Puteți redefini MeasureType înapoi la Projected și Dimensiunea va folosi valoarea proiectată în locul valorii efective.

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that linking dimensions be one of the last steps in your drawing process.

The link tool will not stop you from making illogical links, so you need to choose the correct edge from the 3D view when creating the link.

There is currently no way to break a link; you can change the **MeasureType** back to `Projected` so that the dimension will use the projected value instead of the linked value.

Note that if the Dimension to be linked is based on two vertices, you should select two vertices in the 3D view. Similarly if the Dimension is based on an edge, you should select an edge in the 3D view.

## Proprietăți

1.  Proprietatea MeasureType a Dimensiunii legate a fi schimbată din \"Projected\" în \"True\".




1.  The MeasureType property of a linked Dimension will be changed from \"Projected\" to \"True\".

## Script

Dimensiunile pot fi legate de geometria 3D folosind Python.


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Link Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
to be defined
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/ro
