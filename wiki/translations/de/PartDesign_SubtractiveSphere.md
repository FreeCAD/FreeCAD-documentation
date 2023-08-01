---
- GuiCommand:/de
   Name:PartDesign SubtractiveSphere
   Name/de:PartDesign KugelAbziehen
   MenuLocation:Part Design → Grundkörper abziehen → Kugel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGrundkörperAbziehen](PartDesign_CompPrimitiveSubtractive/de.md), [PartDesign KugelHinzufügen](PartDesign_AdditiveSphere/de.md)
---

# PartDesign SubtractiveSphere/de



## Beschreibung

Fügt einen Kugel-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveSphere_example.svg ) *Auf der linken Seite ist der aktive Körper (A) in Grau und die abzuziehende Kugel (B) in durchscheinenden Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractiveSphere.svg" width=24px> '''Kugel'''** drücken. **Hinweis**: Die Kugel ist Teil eines Symbolmenüs mit der Bezeichnung Grundkörper abziehen. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Kugel zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Kugel im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Sphere-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Die Kugel kann nach der Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für Die Kugel (Sphere-Objekt). Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius}}: Kugelradius.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung der Kugel, normal zur Z-Achse (-90° für eine ganze Kugel)

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung im Dialog Parameter des Grundkörpers) Die obere Verkürzung der Kugel, normal zur Z-Achse (90° für eine ganze Kugel).

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des (halben) Kugelquerschnitts (360° für eine ganze Kugel).





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveSphere/de
