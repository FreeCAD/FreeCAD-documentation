---
- GuiCommand:/de
   Name:Image CreateImagePlane
   Name/de:Bild ErstelleBildEbene
   MenuLocation:Werkzeugleisten → Erstellen eines ebenen Bildes im 3D Raum
   Workbenches:[Bild](Image_Workbench/de.md)
   SeeAlso:[Bild Öffnen](Image_Open/de.md), [Bild Skalierung](Image_Scaling/de.md)
---

# Image CreateImagePlane/de


</div>

## Beschreibung

Das [ErstelleBildEbene](Image_CreateImagePlane/de.md) Werkzeug importiert ein [Bitmap](bitmap/de.md) Bild und platziert es auf einer der XY, YZ oder XZ Ebenen.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Image_CreateImagePlane.svg" width=16px> [Bild Ebene](Image_CreateImagePlane/de.md)** Schaltfläche.
2.  Wähle das gewünschte Bild in deinem System aus.
3.  Wähle die Ebene, auf der das Bild platziert werden soll, gib einen Versatzwert an und drücke **OK**.


</div>

Das sich ergebende BildEbenenobjekt verwendet das Verhältnis von 1 Pixel zu 1 Millimeter; damit das Bild gut dargestellt wird, sollte es eine ausreichende Auflösung haben.

Beim Import des Bildes möchtest du möglicherweise einen Versatz von `-0.1 mm` hinzufügen, um das Bild leicht hinter der Arbeitsebene zu platzieren; dies erleichtert das Nachzeichnen (Zeichnen oben) des Bildes mit den [Entwurf](Draft_Workbench/de.md) oder [Skizzierer](Sketcher_Workbench/de.md) Werkzeugen.

Wenn dem Bild anfänglich kein Versatz gegeben wird, kann seine Position immer noch im [Eigenschaftseditor](Property_editor/de.md) eingestellt werden.

## Eigenschaften


{{Properties Title|Base}}


<div class="mw-translate-fuzzy">


{{Properties Title|Basis}}

-    **Position**: gibt die Koordinaten des Basispunkts der Bildebene an.

-    **Winkel**: gibt den Drehwinkel der Bildebene an.

-    **Achse**: gibt die für den Drehwinkel verwendete Achse an.


</div>


{{Properties Title|Image Plane}}


<div class="mw-translate-fuzzy">


{{Properties Title|Bildebene}}

-    **XGröße**: gibt die Breite der Bildebene an.

-    **YGröße**: gibt die Höhe der Bildebene an.

-    **Bildebene**: gibt das Bild an, das für diese Ebene verwendet werden soll.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Image Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/de
