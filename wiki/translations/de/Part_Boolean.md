---
- GuiCommand:/de
   Name:Part Boolean
   Name/de:Part Boolesche Operationen
   MenuLocation:Formteil → Bool'sche Operationen → Boolesche Operation...
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Schneiden](Part_Cut/de.md), [Part Verschmelzen](Part_Fuse/de.md), [Part Schnittmenge](Part_Common/de.md), und [Part Abschnitt](Part_Section/de.md)
---

# Part Boolean/de

## Beschreibung


**[<img src=images/Part_Boolean.svg style="width:16px"> [Part Bool'sche Operationen](Part_Boolean/de.md)**

ist ein generisches boolesches Multifunktionswerkzeug. Es erlaubt dir die Objekte und die durchzuführende Operation in einem einzigen Dialog anzugeben.

Für einen schnelleren Zugriff auf diese Operationen benutze **[<img src=images/Part_Cut.svg style="width:16px"> [Part Schneiden](Part_Cut/de.md)**, **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Verschmelzung](Part_Fuse/de.md)**, **[<img src=images/Part_Common.svg style="width:16px"> [Part Gemeinsam](Part_Common/de.md)** und **[<img src=images/Part_Section.svg style="width:16px"> [Abschnitt](Part_Section/de.md)**.

![](images/PartBooleansDialog.png )



*Dialog zur Auswahl von Objekten und der auszuführenden booleschen Operation.*

## Anwendung

Siehe die einzelnen Befehle:

-    **<img src="images/Part_Cut.svg" width=16px> [Part Schneiden](Part_Cut/de.md)
**
    

-    **<img src="images/Part_Fuse.svg" width=16px> [Part Vereinigen](Part_Fuse/de.md)
**
    

-    **<img src="images/Part_Common.svg" width=16px> [Part Gemeinsam](Part_Common/de.md)
**
    

-    **<img src="images/Part_Section.svg" width=16px> [Part Abschnitt](Part_Section/de.md)
**
    

Siehe auch das {{MenuCommand/de|Part → Create a copy [Form aufbereiten](Part_RefineShape/de.md)}}-Menü.

## Koplanare Probleme 

Die booleschen Operationen werden vom internen Geometriekernel, der [OpenCASCADE Technologie](OpenCASCADE/de.md) (OCCT), durchgeführt. Diese Bibliothek hat manchmal Probleme, boolesche Ergebnisse zu erzeugen, wenn sich die Eingabeobjekte eine Kante oder eine Fläche teilen. Um sicherzugehen, dass die boolesche Operation erfolgreich ist, wird empfohlen, dass sich die Formen deutlich überschneiden; das bedeutet, dass in den meisten Fällen eine Form vorstehen oder größer als die andere Form sein sollte.

In Fällen von Koplanarität können, selbst wenn die erste boolesche Operation erfolgreich ist, nachfolgende boolesche Operationen fehlschlagen. In diesem Fall liegt das Problem möglicherweise nicht in der zuletzt durchgeführten Operation, sondern in den älteren, d.h. in den verschachtelten Operationen, wie in der [Baumansicht](Tree_view/de.md) angegeben. Zur Behebung dieser Probleme wird empfohlen, das **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part PrüfeGeometrie](Part_CheckGeometry/de.md)** Werkzeug zu verwenden, um alle Objekte auf Probleme zu untersuchen.

<img alt="" src=images/Part_Boolean_cut_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_cut_coplanar_2.png  style="width:500px;">



*Links: Formen, die eine gemeinsame Fläche haben, ein boolescher Schnitt kann zu falschen Ergebnissen führen. Rechts: Formen, die sich deutlich überschneiden, wird ein boolescher Schnitt in den meisten Fällen erfolgreich sein.*

<img alt="" src=images/Part_Boolean_fusion_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_fusion_coplanar_2.png  style="width:500px;">



*Links: Formen, die eine gemeinsame Fläche haben, eine boolesche Vereinigung kann zu falschen Ergebnissen führen. Rechts: Formen, die sich deutlich überschneiden, wird die boolesche Vereinigung in den meisten Fällen erfolgreich sein.*

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Boolean/de
