---
- GuiCommand:/de
   Name:PartDesign AdditiveEllipsoid
   Name/de:Additives Ellipsoid
   MenuLocation:Part Design → Erzeugen eines zusätzlichen Grundkörpers → Additives Ellipsoid
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign CompAdditivesGrundelement](PartDesign_CompPrimitiveAdditive/de.md)
---

# PartDesign AdditiveEllipsoid/de

## Beschreibung

Fügt den Grundkörper Ellipsoid in den aktiven Körper (Body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditiveEllipsoid_example.png  style="width:200px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/PartDesign_AdditiveEllipsoid.svg" width=24px>  '''Additiver Ellipsoid'''** Schaltfläche. **Hinweis**: der Additive Ellipsoid ist Teil eines Symbolmenüs mit der Bezeichnung *Erstellen eines additiven Grundelements*. Nach dem Start von FreeCAD wird der Additiv Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Ellipsoid zu gelangen, klicke auf den Abwärtspfeil neben dem sichtbaren Symbol und wähle Additiv Zylinder im Menü.
2.  Stelle die Grundelement Parameter und [Anhang](Part_EditAttachment/de.md) ein.
3.  Klicke **OK**.
4.  Eine Ellipsoidfunktion wird unter dem aktiven Körper angezeigt.


</div>

## Optionen

Das Ellipsoid kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Attachment**: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für das Ellipsoid-Objekt. Dies kann nach Bedarf geändert werden.

-    **Radius1**: Der Wert des Radius entlang der vertikalen Achse des Ellipsoids, in der Voreinstellung parallel zur Z-Achse.

-    **Radius2**: Der Wert des Radius der Längsachse, in der Voreinstellung parallel zur X-Achse.

-    **Radius3**: Der Wert des Radius entlang der Breite, in der Voreinstellung parallel zu der Y-Achse. In der Voreinstellung mit einen Wert von Null ist das Ellipsoid ein [abgeplattetes Rotationsellipsoid](https://de.wikipedia.org/wiki/Rotationsellipsoid). Dies hat die gleiche Form, als wäre Radius 3 identisch mit Radius2.

-    **Angle1**: (mit *V-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung des Ellipsoids, normal zur Z-Achse (-90° in einem vollen Rotationsellipsoid)

-    **Angle2**: (ohne Beschriftung in dem Dialog Parameter des Grundkörpers) Die obere Verkürzung des Ellipsoids, normal zur Z-Achse (90° in einem vollen Rotationsellipsoid).

-    **Angle3**: (mit *U-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des halben elliptischen Querschnitts (360° in einem vollen Rotationsellipsoid).


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveEllipsoid/de
