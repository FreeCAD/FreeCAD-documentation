---
- GuiCommand:/de
   Name:PartDesign SubtractiveCylinder
   Name/de:PartDesign Abzuziehender Zylinder
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehender Zylinder
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign CompSubtraktiverGrundkörper](PartDesign_CompPrimitiveSubtractive/de.md)
---

# PartDesign SubtractiveCylinder/de


</div>

## Beschreibung

Fügt einen abzuziehenden Zylinder in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*Auf der linken Seite ist der aktive Körper (A) in grau und der abzuziehender Zylinder (B) in durchscheinenden rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/PartDesign_SubtractiveCylinder.svg" width=24px> '''Abzuziehender Zylinder'''** Schaltfläche. **Anmerkung**: Abzuziehender Zylinder ist Teil des benannten Symbols *Erzeuge einen abzuziehenden Grundkörper*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Um zur Schaltfläche Zylinder zu gelangen, klicke auf den Abwärtspfeil neben dem sichtbaren Symbol und wähle im Menü Subtraktiver Zylinder.
2.  Lege die Grundkörperparameter und [Attachment](Part_EditAttachment/de.md) fest.
3.  Klicke **OK**.
4.  Ein Zylinder erscheint unterhalb des aktiven Körpers.


</div>

## Optionen

It is possible to create skewed prisms by specifying angles in respect to the normal vector of the chosen attachment. <small>(v0.20)</small> 

Der Zylinder kann auf zwei verschieden Wege bearbeitet werden:

-   Doppelklicke ihn im Modellbaum oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü; dadurch werden die Grundkörperparameter angezeigt.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md).

## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Attachment**: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für das Zylinder-Objekt. Dies kann nach Bedarf geändert werden.

-    **Radius**: Der Wert des Radius von dem Zylinder.

-    **Angle**: Der Rotationswinkel des halben Querschnitts (360° ergeben einen vollen Zylinder).

-    **Height**: Die Länge des Zylinders entlang seiner Achse.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCylinder/de
