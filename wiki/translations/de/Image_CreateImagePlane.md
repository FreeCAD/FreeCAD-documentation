---
- GuiCommand:
   Name: Image CreateImagePlane
   Name/de: Image BildebeneErstellen
   MenuLocation: 
   Workbenches: [Image (Bild)](Image_Workbench/de.md)
   SeeAlso: [Image Öffnen](Image_Open/de.md), [Image BildebeneSkalieren](Image_Scaling/de.md)
---

# Image CreateImagePlane/de

## Beschreibung

Das Werkzeug [BildebeneErstellen](Image_CreateImagePlane/de.md) importiert ein [Bitmap](bitmap/de.md) Bild und platziert es auf einer XY-, YZ- oder XZ-Ebene.

## Anwendung

1.  Schaltfläche **<img src="images/Image_CreateImagePlane.svg" width=16px> [Bildebene erstellen](Image_CreateImagePlane/de.md)** drücken.
2.  Das gewünschte Bild aus dem eigenen System auswählen.
3.  Die Ebene auswählen, auf der das Bild platziert werden soll, einen Versatzwert angeben und **OK** drücken.

Das entstandene ImagePlane-Objekt verwendet das Verhältnis von 1 Pixel zu 1 mm; damit das Bild gut dargestellt wird, sollte es eine ausreichend hohe Auflösung haben.

Beim Import des Bildes sollte man möglichst einen Versatz von `-0.1 mm` hinzufügen, um das Bild leicht hinter der Arbeitsebene zu platzieren; dies erleichtert das Nachzeichnen (Darüberzeichnen) des Bildes mit den Werkzeugen der Arbeitsbereiche [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md).

Wenn das Bild nicht schon zu Beginn ein Versatz erhält, kann seine Position immer noch im [Eigenschafteneditor](Property_editor/de.md) angepasst werden.

## Eigenschaften


{{Properties Title/de|Basis}}

-    {{PropertyData/de|Position}}: gibt die Koordinaten des Basispunkts der Bildebene an.

-    {{PropertyData/de|Winkel}}: gibt den Drehwinkel der Bildebene an.

-    {{PropertyData/de|Achse}}: gibt die für den Drehwinkel verwendete Achse an.


{{Properties Title/de|Image Plane}}

-    {{PropertyData/de|Image File}}: gibt das Bild an, das für diese Ebene verwendet werden soll.

-    {{PropertyData/de|XSize}}: gibt die Breite der Bildebene an.

-    {{PropertyData/de|YSize}}: gibt die Höhe der Bildebene an.





{{Image Tools navi

}}



---
⏵ [documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/de
