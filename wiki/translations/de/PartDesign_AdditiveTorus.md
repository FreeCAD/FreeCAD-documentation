---
- GuiCommand:/de
   Name:PartDesign AdditiveTorus
   Name/de:PartDesign Additiver Torus
   MenuLocation:Part Design → Erzeugen eines zusätzlichen geometrischen Körpers → Zu addierender Torus
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   Siehe auch:[PartDesign CompPrimitiveAdditive](PartDesign_CompPrimitiveAdditive/de.md)
---

# PartDesign AdditiveTorus/de

## Beschreibung

Fügt den Grundkörper Torus in den aktiven Körper (Body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditiveTorus_example.png  style="width:200px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_AdditiveTorus.svg" width=24px> '''Additiver Torus'''** klicken. **Hinweis**: der Additive Torus ist Teil eines Symbolmenüs mit der Bezeichnung **Additives Grundelement erstellen**.

Nach dem Start von FreeCAD ist der Additive Quader derjenige, der in der Werkzeugleiste angezeigt wird. Um den Torus zu erhalten, klicke auf den Abwärtspfeil neben dem sichtbaren Symbol und wähle im Menü Additiver Torus.

1.  Setze die Grundelementparameter und [Anhang](Part_EditAttachment/de.md).
2.  Klicke auf **OK**.
3.  Ein Torus Formelement erscheint unter dem aktiven Körper.


</div>

## Optionen

Der Torus kann auf zwei verschiedene Weisen bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Torus-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius1}}: Der Radius des imaginären Orbits, auf den das Querschnittsprofil den Mittelpunkt umrundet. (Der Abstand von dem Mittelpunkt des Torus zu dem Mittelpunkt des umlaufenden Profils)

-    {{PropertyData/de|Radius2}}: Der Radius von dem kreisförmigen Profil, welches die Torusform bestimmt.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Der Winkel des unteren Halbbogens des kreisförmigen Profils (-180° in einem vollen Torus). Ein Fehler in der Programmierung verusacht unerwartete Ergebnisse bei Änderung von Angle1.

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung in dem Dialog Parameter des Grundkörpers) Der Winkel des oberen Halbbogens des kreisförmigen Querschnittsprofils (180° in einem vollen Torus). Ein Fehler in der Programmierung verusacht unerwartete Ergebnisse bei Änderung von Angle2.

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des kreisförmigen Profilquerschnitts (360° in einem vollen Torus).


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveTorus/de
