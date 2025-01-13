# 3D view/de
## Einleitung




Die [3D-Ansicht](3D_view/de.md) von FreeCAD ist eine Instanz eines Coin3D-[Szenengraphen](Scenegraph/de.md), und stellt das wichtigste Fenster in der [Benutzeroberfläche](interface/de.md) dar. Coin3D ist eine Bibliothek, die den OpenInventor 2.1-Szenenbeschreibungsstandard implementiert.

Bestimmte Eigenschaften der Ansicht, wie Hintergrundfarbe, Art der [Mausnavigation](Mouse_navigation/de.md) und Zoom-Schritte, können im [Voreinstellungseditor](Preferences_Editor/de.md) konfiguriert werden.

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*Die [3D-Ansicht](3D_view/de.md) ist ein Bestandteil der FreeCAD- [Benutzerschnittstelle](interface/de.md). Standardmäßig zeigt sie ein kleines Widget mit Koordinatenachsen und den Navigationswürfel, ebenfalls mit Koordinatenachsen; das Raster kann durch Laden des Arbeitsbereichs [Draft](Draft_Workbench/de.md) angezeigt und konfiguriert werden.*



## Kontextmenü

Die Optionen im Kontextmenü der 3D-Ansicht hängen von den Objekten in der Auswahl und des gerade aktiven Arbeitsbereichs ab. Um dieses Menü anzuzeigen, wahlweise ein oder mehrere Objekte auswählen und dann mit der rechten Maustaste in die 3D-Ansicht klicken.

## Details

FreeCAD verwendet die Bibliothek Quarter, um Coin3D in einer Qt-Umgebung zu verwenden.

Es ist möglich, von der [Python-Konsole](Python_console.md) aus direkt mit dem Szenengraph der 3D-Ansicht zu interagieren, wenn die Python-Bibliothek Pivy verwendet wird.

Weitere Informationen finden sich in der Dokumentation für erfahrene Anwender:

-   [Szenengraph](Scenegraph/de.md), Beschreibung von Coin3D.
-   [Pivy](Pivy/de.md), Verwendung von Coin3D über die Python-Konsole.
-   [Drittanbieter-Bibliotheken](Third_Party_Libraries/de.md), die von FreeCAD verwendet werden.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ Dokumentation.


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > 3D view/de
