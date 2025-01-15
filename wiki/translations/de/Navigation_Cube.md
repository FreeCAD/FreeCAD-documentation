# Navigation Cube/de
## Einleitung

Der **Navigationswürfel** stellt visuelle Informationen zur Kameraausrichtung in der aktiven [3D-Ansicht](3D_view/de.md) zur Verfügung und kann zu ihrer Einstellung verwendet werden. Standardmäßig ist er sichtbar und befindet sich in der oberen rechten Ecke der Ansicht.

![](images/Navigation_Cube_Example.png )

Der Navigationswürfel besteht aus mehreren Teilen:

-   Dem [Hauptwürfel](#Hauptwürfel.md)
-   Sechs [Richtungspfeile](#Richtungspfeile.md)
-   Die [Schaltfläche Ansicht umkehren](#Schaltfläche_Ansicht_umkehren.md) (oben rechts) {{Version/de|0.20}}
-   Dem [Miniwürfel-Menü](#Miniwürfel-Menü.md) (unten rechts)
-   Den X-, Y- und Z-Achsindikatoren

Alle Elemente, außer den Achsindikatoren, können angeklickt werden.



## Anwendung



### Hauptwürfel

Der Hauptwürfel besitzt 26 Flächen: 6 Hauptflächen, 12 rechteckige Kantenflächen ({{Version/de|0.20}}), und 8 Eckflächen. Ein Klick auf eine dieser Flächen ändert die Kameraausrichtung so, dass ihre Blickrichtung senkrecht zu der ausgewählten Fläche verläuft.



### Richtungspfeile

Es gibt sechs Richtungspfeile: vier dreieckige Pfeilspitzen und zwei gebogene Pfeile. Klickt man auf einen der Dreieckigen Pfeile, wird die [3D-Ansicht](3D_view/de.md) um eine Linie senkrecht zur Pfeilrichtung gedreht. Klickt man auf einen gebogenen Pfeil, wird die [3D-Ansicht](3D_view/de.md) um die Normale der Ansicht gedreht.



### Schaltfläche Ansicht umkehren 

Klickt man auf die runde Schaltfläche in der rechten oberen Ecke des Navigationswürfels, wird die [3D-Ansicht](3D_view/de.md) um 180° um die vertikale Achse der Ansicht gedreht.



### Miniwürfel-Menü 

Ein Klick auf den kleinen Würfel in der rechten unteren Ecke des Navigationswürfels öffnet ein Menü mit folgenden Optionen:

-    **<img src="images/Std_OrthographicCamera.svg" width=16px> [Orthogonale Ansicht](Std_OrthographicCamera/de.md)**: schaltet auf die orthogonale Ansicht um.

-    **<img src="images/Std_PerspectiveCamera.svg" width=16px> [Perspektivische Ansicht](Std_PerspectiveCamera/de.md)**: schaltet auf die Perspektivansicht um.

-    **<img src="images/Std_ViewIsometric.svg" width=16px> [Isometrisch](Std_ViewIsometric/de.md)**: schaltet auf die isometrische Ansicht um.

-    **<img src="images/Std_ViewFitAll.svg" width=16px>[Einpassen](Std_ViewFitAll/de.md)**: skaliert und schwenkt die Kamera so, dass alle sichtbaren Objekte die Ansicht ausfüllen.

-    **<img src="images/Std_ViewFitSelection.svg" width=16px> [Auswahl einpassen](Std_ViewFitSelection/de.md)**: skaliert und schwenkt die Kamera so, dass alle ausgewählten Objekte die Ansicht ausfüllen. {{Version/de|1.0}}

-    **<img src="images/Std_AlignToSelection.svg" width=16px> [Auf die Auswahl ausrichten](Std_AlignToSelection/de.md)**: richtet die Kamera der Ansicht entgegen der Normale einer ebenen Fläche aus oder entgegen dem Verlauf einer geraden Kante. {{Version/de|1.0}}

-    **Beweglicher Navigationswürfel**: Wenn diese Checkbox ({{Version/de|0.21}}) aktiviert ist, kann der komplette Navigationswürfel bewegt werden, indem der Hauptwürfel an beliebiger Stelle mit der linken Maustaste angeklickt und mit gedrückt gehaltener Taste gezogen wird. Dies ist dazu gedacht, den Würfel temporär aus dem Weg zu ziehen. Die [erweiterten Parameter](#Erweiterte_Parameter.md) OffsetX und OffsetY können verwendet werden, um den Würfel dauerhaft zu versetzen, siehe unten.



## Anpassung



### Einstellungen

Der Navigationswürfel wird durch einige Einstellungen gesteuert: **Bearbeiten → Einstellungen... → Anzeige → Navigation → Navigationswürfel** {{Version/de|0.19}}. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).



### Erweiterte Parameter 

Einige erweiterte Parameter des Navigationswürfels können nicht im [Voreinstellungseditor](Preferences_Editor/de#Navigation.md) angepasst werden. Diese Parameter können von Hand im [Parametereditor](Std_DlgParameter/de.md) angepasst werden.

Farben von Hand festlegen:

1.  <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parametereditor](Std_DlgParameter/de.md) öffnen.
2.  Im Panel auf der linken Seite zu **BaseApp → Preferences → NaviCube**.
3.  Rechtsklick im Panel auf der rechten Seite und **Neue positive Ganzzahl** im Kontextmenü wählen.
4.  Den Namen einer dieser Farben eingeben:
    -   
        **BaseColor**
        
        : die Grundfarbe aller Elemente, der Standardwert ist {{Value|3806916544}} (hex: {{Value|e2e8efc0}}). Diese Farbe kann auch im \[\[Preferences_Editor/de#Navigation\|Voreinstellungseditor

\]\] festgelegt werden. {{Version/de|0.21}}

#\* **EmphaseColor**: die Farbe der Texte und Linien, die Voreinstellung hängt von der **BaseColor** ab. Sie ist entweder schwarz: {{Value|255}} (hex: {{Value|000000ff}}), oder weiß: {{Value|4294967295}} (hex: {{Value|ffffffff}}). {{Version/de|0.21}}

#\* **HiliteColor**: die Farbe, mit der die Flächen und Schaltflächen hervorgehoben werden; die Standardeinstellung ist {{Value|2867003391}} (hex: {{Value|aae2ffff}}).

1.  Der Farbwert muss als 32-Bit-Ganzzahl ohne Vorzeichen eingegeben werden. Umgerechnet in das Hexadezimalformat hat diese Ganzzahl die Form {{Value|RRGGBBAA}}. Dabei steht {{Value|AA}} für den Alphakanal (ein Maß für die Transparenz), und die anderen drei Buchstabenpaare stehen für Rot, Grün und Blau. Um einen hexadezimalen Wert in eine Ganzzahl ohne Vorzeichen umzuwandeln, kann die [Python-Konsole](Python_console/de.md) verwendet werden. Zum Beispiel durch eingeben von {{Incode|int("323232ff", 16)}}.
2.  Optional können weitere Parameter eingestellt werden.
3.  Press the **Close** button.

In der folgenden Tabelle sind die anderen erweiterten Parameter des Navigationswürfels aufgeführt, die auf ähnliche Weise eingestellt werden können. Die Informationen aus der Spalte **Art** verwenden, um in Schritt 3 ein korrektes neues Element zu erstellen.

+++++
| Name        | Description                                                                                                                   | Type    | Default |
+=============+===============================================================================================================================+=========+=========+
| BorderWidth | The width of the edges of the cube and the borders around the buttons in pixels.                                              | Float   | 1.1     |
+++++
| ChamferSize | The size of the edges and corners as a factor of the cube size. Values should be in the 0.05 - 0.18 range.                    | Float   | 0.12    |
|             |                                                                                                                               |         |         |
|             |                                                                                                                |         |         |
|             | <small>(v0.21)</small>                                                                                                               |         |         |
|             |                                                                                                                            |         |         |
+++++
| FontStretch | The font width as a percentage of the default width. Use 0 or 100 for the default font width.                                 | Integer | 0       |
+++++
| FontWeight  | The font weight. Higher values make the font more bold. The effect may depend on the font. Use 0 for the default font weight. | Integer | 0       |
+++++
| FontZoom    | The size of the labels:                                                                                                       | Float   | 0.3     |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|FontZoom &#61; 1.0}}                                                                                              |         |         |
|             |                                                                                                                            |         |         |
|             |     : Make the labels as big as possible individually.                                                                        |         |         |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|0.0 < FontZoom < 1.0}}                                                                                            |         |         |
|             |                                                                                                                            |         |         |
|             |     : Idem but limit the maximum font size.                                                                                   |         |         |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|FontZoom &#61; 0.0}}                                                                                              |         |         |
|             |                                                                                                                            |         |         |
|             |     : Idem but use the same font size for all.                                                                                |         |         |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|FontZoom < 0.0}}                                                                                                  |         |         |
|             |                                                                                                                            |         |         |
|             |     : Use the same font size for all, but scaled down.                                                                        |         |         |
|             |                                                                                                                               |         |         |
|             |                                                                                                                |         |         |
|             | <small>(v0.21)</small>                                                                                                               |         |         |
|             |                                                                                                                            |         |         |
+++++
| OffsetX     | The offset of the cube in the X direction relative to its corner position in pixels.                                          | Integer | 0       |
+++++
| OffsetY     | The offset of the cube in the Y direction relative to its corner position in pixels.                                          | Integer | 0       |
+++++
| ShowCS      | Toggles the display of the coordinate system (the X, Y and Z axis indicators).                                                | Boolean | true    |
+++++
| TextBottom  | The text on the bottom face of the cube. The default value should be translated.                                              | String  | BOTTOM  |
+++++
| TextFront   | The text on the front face of the cube. Idem.                                                                                 | String  | FRONT   |
+++++
| TextLeft    | The text on the left face of the cube. Idem.                                                                                  | String  | LEFT    |
+++++
| TextRear    | The text on the rear face of the cube. Idem.                                                                                  | String  | REAR    |
+++++
| TextRight   | The text on the right face of the cube. Idem.                                                                                 | String  | RIGHT   |
+++++
| TextTop     | The text on the top face of the cube. Idem                                                                                    | String  | TOP     |
+++++



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User%20Documentation.md) > Navigation Cube/de
