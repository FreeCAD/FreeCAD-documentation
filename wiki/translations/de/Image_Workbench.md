# Image Workbench/de

 

<img alt="Bild Arbeitsbereichssymbol" src=images/Workbench_Image.svg  style="width:128px;">

## Einführung


{{TOCright}}

Der <img alt="" src=images/Workbench_Image.svg  style="width:24px;"> [Bild Arbeitsbereich](Image_Workbench/de.md) verwaltet verschiedene Arten von [Bitmap](bitmap/de.md) Bildern und ermöglicht, diese in FreeCAD zu öffnen.

## Werkzeuge

-   <img alt="" src=images/Image_Open.svg  style="width:32px;"> [Öffnen](Image_Open/de.md): Öffnet ein Bild mit einem neuen Ansichtsfenster.
-   <img alt="" src=images/Image-import-to-plane.svg  style="width:32px;"> [Import zu Ebene](Image_CreateImagePlane/de.md): Importieren eines Bildes in eine Ebene in der 3D Ansicht.
-   <img alt="" src=images/Image-scale.svg  style="width:32px;"> [Skalierung](Image_Scaling/de.md): Skaliert ein Bild, das in eine Ebene importiert wurde.

## Funktionen

-   Wie bei einer [Skizze](Sketcher_Workbench/de.md) kann ein importiertes Bild an eine der Hauptebenen XY, XZ oder YZ angehängt und mit einem positiven oder negativen Versatz versehen werden.
-   Das Bild wird im Verhältnis von 1 Pixel zu 1 Millimeter importiert.
-   Die Empfehlung lautet, das importierte Bild in einer angemessenen Auflösung zu haben.

## Arbeitsablauf

Eine Hauptanwendung dieses Arbeitsbereichs ist das Nachzeichnen über das Bild mit den [Entwurf](Draft_Workbench/de.md) oder [Skizzierer](Sketcher_Workbench/de.md) Werkzeugen, um einen Festkörper basierend auf den Konturen des Bildes zu erzeugen.

Die Abtastung eines Bildes funktioniert am besten, wenn das Bild einen kleinen negativen Versatz, z.B. -0,1 mm, von der Bearbeitungsebene hat. Das bedeutet, dass das Bild leicht hinter der Ebene liegt, auf der Du Deine 2D-Geometrie zeichnest, so dass Du nicht auf das Bild selbst zeichnest.

Der Versatz des Bildes kann beim Import eingestellt oder später über seine Eigenschaften geändert werden.





{{Image Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
