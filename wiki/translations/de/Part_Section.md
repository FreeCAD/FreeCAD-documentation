---
- GuiCommand:/de
   Name:Part Section
   Name/de:Part Schnittkurve
   MenuLocation:Formteil → Schnittkurve
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Querschnitte](Part_CrossSections/de.md)
---

# Part Section/de

## Beschreibung


<div class="mw-translate-fuzzy">

Extrahiert eine Schnittkurve aus der Überschneidung zweier ausgewählter Formen, wobei die zweite als Schnittebene verwendet wird. Diese Operation ist voll parametrisch und die Komponenten können modifiziert und das Ergebnis neu berechnet werden.


</div>

-   An intersection of two solids/faces results in one or more section lines.
-   An intersection of two lines, or a line and a solid/face, results in one or more points.

![](images/PartSection1_it.png ) 
*A cube sectioned with a cylinder*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle das Basisobjekt aus
2.  Wähle das Beschnittwerkzeug
3.  Klicke auf **Part** → **<img src="images/Part_Section.svg" width=24px> Schnittkurve** aus dem oberen Menü.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Section object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|Link**: Link to the first object.

-    **Tool|Link**: Link to the second object.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"Shape history\".

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after this boolean operation\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: Approximate the output edges.

## Verknüpfungen


<div class="mw-translate-fuzzy">

Zum Erzeugen von Abschnitten mit einer Schnittebene siehe <img alt="" src=images/Part_CrossSections.svg  style="width:24px;"> [Querschnitte](Part_CrossSections/de.md).


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/de
