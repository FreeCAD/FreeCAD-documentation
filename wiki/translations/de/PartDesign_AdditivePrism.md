---
- GuiCommand:/de
   Name:PartDesign AdditivePrism
   Name/de:PartDesign Additves Prisma
   MenuLocation:Part Design → Erzeugen eines additiven Grundkörpers → Additives Prisma
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Erzeugen eines additiven Grundelements](PartDesign_CompPrimitiveAdditive/de.md), [PartDesign Subtraktives Prisma](PartDesign_SubtractivePrism/de.md)
---

# PartDesign AdditivePrism/de

## Beschreibung

Fügt ein Prisma in den aktiven Körper (Body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width:200px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/PartDesign_AdditivePrism.svg" width=24px> '''Additives Prisma'''** Schaltfläche. **Hinweis**: das Additive Prisma ist Teil eines Symbolmenüs mit der Bezeichnung *Erstellen eines additiven Grundelements*. Nach dem Start von FreeCAD wird der Additiv Quader in der Werkzeugleiste angezeigt. Um das Prisma zu erhalten, klicke auf den Abwärtspfeil neben dem sichtbaren Symbol und wähle Additives Prisma im Menü.
2.  Stelle die Grundelement Parameter und [Anhang](Part_EditAttachment/de.md) ein.
3.  Klicke **OK**.
4.  Eine Prismafunktion wird unter dem aktiven Körper angezeigt.


</div>

## Optionen

Es ist möglich, schräge Prismen durch Angabe von Winkeln in Bezug auf den Normalenvektor des gewählten Anhangs zu erzeugen. <small>(v0.19)</small> 

Das Prisma kann nach seiner Erstellung auf zwei Arten bearbeitet werden:

-   Doppelklicke im Modellbaum darauf, oder klicke mit der rechten Maustaste und wähle **Grundelement bearbeiten** im Kontextmenü; dadurch werden die Grundelement Parameter aufgerufen.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md).

## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Befestigung**: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    **Beschriftung**: Die vom Benutzer vergebene Beschriftung für das Prismenobjekt. Ändere dies nach deinen Bedürfnissen.

-    **Polygon**: Anzahl der Seiten im Polygonquerschnitt des Prismas.

-    **Umkreisradius**: [Umkreisradius](https://de.wikipedia.org/wiki/Umkreis) des Polygonquerschnitts des Prismas.

-    **Höhe**: Höhe des Prismas.

-    **Erster Winkel**: Winkel in erster Richtung. <small>(v0.19)</small> 

-    **Zweiter Winkel**: Winkel in zweiter Richtung. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePrism/de
