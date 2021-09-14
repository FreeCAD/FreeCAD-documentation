---
- GuiCommand:/de
   Name:Draft Drawing
   Name/de:Entwurf Zeichnung
   MenuLocation:Entwurf → Zeichnung
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md), [Form in 2D Ansicht](Draft_Shape2DView/de.md)
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug Zeichnung erlaubt es, ausgewählte Objekte auf einem Zeichenblatt zu platzieren, das mit dem [Drawing-Arbeitsbereich](Drawing_Workbench/de.md) erstellt wurde. Falls kein [Blatt](Drawing_templates/de.md) im Dokument existiert, wird ein Standardblatt erstellt.


</div>


<div class="mw-translate-fuzzy">

Diese Werkzeug arbeitet ähnlich wie das [Zeichnungsansicht](Drawing_View/de.md)-Werkzeug, ist aber für den [Draft-Arbeitsbereich](Draft_Workbench/de.md) optimiert und kann 2D-Objekte mit einer gefüllten Fläche erzeugen. Es kann mit bestimmten Objekten wie [Draft Dimension](Draft_Dimension/de.md) und [Draft Text](Draft_Text/de.md) umgehen, was das [Zeichnungsansicht](Drawing_View/de.md)-Werkzeug nicht kann.


</div>

This command is now obsolete. Use the [TechDraw Workbench](TechDraw_Workbench.md) and the [TechDraw DraftView](TechDraw_DraftView.md) command instead.

<img alt="" src=images/Draft_drawing_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">


*In eine Zeichenseite importiertes Draft-Objekt und Bemaßungen*


</div>


<div class="mw-translate-fuzzy">

## Anwendung


</div>

1.  To use this command in FreeCAD version 0.19 and later you need to add a button to a custom toolbar. See [Interface Customization](Interface_Customization.md).
2.  Select one or more objects. A separate view will be created for each object.
3.  Optionally add a [Drawing](Drawing_Workbench.md) page to the selection. If you do not, the view is inserted into the first page in the document. If there are no pages in the document a new page is created first.
4.  Press the **<img src="images/Draft_Drawing.svg" width=16px> [Draft Drawing](Draft_Drawing.md)** button.
5.  There is a bug in the FreeCAD version 0.19 version of the command. The initial value of the **Direction** property is {{Value|[0, 0, 0]}} which is not allowed. For objects on a plane parallel to the XY plane of the global coordinate system it should be changed to {{Value|[0, 0, 1]}}. After changing this property the page and the view may need to be [recomputed](Std_Refresh.md).


<div class="mw-translate-fuzzy">





</div>


 
