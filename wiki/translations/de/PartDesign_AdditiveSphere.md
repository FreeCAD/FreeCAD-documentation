---
- GuiCommand:
   Name: PartDesign AdditiveSphere
   Name/de: PartDesign KugelHinzufügen
   MenuLocation: Part Design - Grundkörper hinzufügen - Kugel hinzufügen
   Workbenches: [PartDesign](PartDesign_Workbench/de.md)
   Version: 0.17
   SeeAlso: [PartDesign AuswahlGrundkörperHinzufügen](PartDesign_CompPrimitiveAdditive/de.md), [PartDesign KugelAbziehen](PartDesign_SubtractiveSphere/de.md)
---

# PartDesign AdditiveSphere/de



## Beschreibung

Fügt einen Kugel-Grundkörper in den aktiven Körper (Body-Objekt) als Basisformelement ein oder vereinigt ihn mit den bereits vorhandenen Formelementen.

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_AdditiveSphere.svg" width=24px> '''Kugel'''** drücken. **Hinweis**: Die Kugel ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper hinzufügen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Kugel zu gelangen, den Abwärtspfeil neben dem Symbol anklicken und Kugel im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Sphere-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Die Kugel kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für Die Kugel (Sphere-Objekt). Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius}}: Kugelradius.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung der Kugel, normal zur Z-Achse (-90° in einer vollen Kugel)

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung im Dialog Parameter des Grundkörpers) Die obere Verkürzung der Kugel, normal zur Z-Achse (90° in einer vollen Kugel).

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des (halben) Kugelquerschnitts (360° in einer ganzen Kugel).





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/de
