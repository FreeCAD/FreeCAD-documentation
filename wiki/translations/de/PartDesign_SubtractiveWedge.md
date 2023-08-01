---
- GuiCommand:
   Name:PartDesign SubtractiveWedge
   Name/de:PartDesign KeilAbziehen
   MenuLocation:Part Design - Grundkörper abziehen - Keil
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGrundkörperAbziehen](PartDesign_CompPrimitiveSubtractive/de.md), [PartDesign KeilHinzufügen](PartDesign_AdditiveWedge/de.md)
---

# PartDesign SubtractiveWedge/de



## Beschreibung

Fügt einen Keil-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveWedge_example.svg ) *Auf der linken Seite ist der aktive Körper (A) in Grau und der abzuziehender Keil (B) in durchscheinendem Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractiveWedge.svg" width=24px> '''Keil'''** drücken. **Hinweis**: Der Keil ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper abziehen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Keil zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Keil im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Wedge-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Der Keil kann nach der Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

Wenn die voreingestellte Positionierung verwendet wird, entsprechen die Eingaben folgenden Eigenschaften:

-    {{PropertyData/de|X min/max}}: Ausdehnung der Grundfläche in X-Richtung

-    {{PropertyData/de|Y min/max}}: Ausdehnung von Grund- bis Deckelfläche in Y-Richtung

-    {{PropertyData/de|Z min/max}}: Ausdehnung der Grundfläche in Z-Richtung

-    {{PropertyData/de|X2 min/max}}: Ausdehnung der Deckelfläche in X-Richtung

-    {{PropertyData/de|Z2 min/max}}: Ausdehnung der Deckelfläche in Z-Richtung



## Pyramiden

Keile können zur Erstellung von Pyramiden verwendet werden, wenn die {{PropertyData/de|X2 min/max}} und die {{PropertyData/de|Z2 min/max}} beide so gesetzt werden, dass min = max.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/de
