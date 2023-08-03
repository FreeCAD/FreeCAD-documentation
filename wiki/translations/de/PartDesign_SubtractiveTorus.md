---
 GuiCommand:
   Name: PartDesign SubtractiveTorus
   Name/de: PartDesign TorusAbziehen
   MenuLocation: Part Design , Grundkörper abziehen , Torus
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/de, PartDesign_AdditiveTorus/de
---

# PartDesign SubtractiveTorus/de



## Beschreibung

Fügt einen Torus-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveTorus_example.svg ) *Auf der linken Seite ist der aktive Körper (A) in Grau und der abzuziehende Torus (B) in durchscheinendem Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractiveTorus.svg" width=24px> '''Torus'''** drücken. **Hinweis**: Der Torus ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper abziehen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Torus zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Torus im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Torus-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Der Torus kann nach seiner Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von Grundkörper bearbeiten im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für den Torus (Torus-Objekt). Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius1}}: Der Radius des imaginären Orbits, auf dem das Querschnittsprofil den Mittelpunkt umrundet. (Der Abstand vom Mittelpunkt des Torus zum Mittelpunkt des umlaufenden Profils)

-    {{PropertyData/de|Radius2}}: Der Radius des kreisförmigen Profils, welches die Torusform bestimmt.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Der Winkel des unteren Halbbogens des kreisförmigen Profils (-180° für einen ganzen Torus). Ein Fehler in der Programmierung verusacht unerwartete Ergebnisse bei Änderung von Angle1.

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung im Dialog Parameter des Grundkörpers) Der Winkel des oberen Halbbogens des kreisförmigen Querschnittsprofils (180° für einen ganzen Torus). Ein Fehler in der Programmierung verusacht unerwartete Ergebnisse bei Änderung von Angle2.

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter:* im Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des kreisförmigen Profilquerschnitts (360° für einen ganzen Torus).





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveTorus/de
