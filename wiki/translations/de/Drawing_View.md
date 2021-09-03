---
- GuiCommand:/de
   Name:Drawing View
   Name/de:Drawing View
   Workbenches:[Drawing](Drawing_Workbench/de.md), Complete
   MenuLocation:Zeichnung → Ansicht in Zeichnung einfügen
   Shortcut:Keine
   SeeAlso:[Drawing Landscape A3](Drawing_Landscape_A3/de.md)---


{{VeryImportantMessage|Die Entwicklung des Drawing-Arbeitsbereich wurde gestoppt und ein neuer in v0.17 eingeführter TechDraw-Arbeitsbereich zielt darauf, es zu ersetzen. Beide Module stehen in v0.17 zur Verfügung, aber das Drawing-Arbeitsbereich könnte in zukünftigen Ausgaben entfernt werden.}}

Dieses Werkzeug erstellt eine neue Ansicht des ausgewählten Objekts im aktiven Zeichenblatt.

<img alt="Ein Zeichenblatt mit drei Ansichten: Front, Draufsicht und isometrisch." src=images/Drawing_Views.png  style="width:500px;">

### Anwendung

Wähle ein Objekt entweder in der 3D-Ansicht oder dem Projektbaum, klicke dann auf das Zeichnungsansichtswerkzeug. Als Standard wird eine Draufsicht im Maßstab 1:1 (reale Größe) links oben auf der Seite platziert. Möglicherweise ist sie nicht sichtbar, weil sie viel zu groß oder viel zu klein für die Seite ist.

Ein **Ansicht**-Objekt wird zum **Seite**-Ojekt des Projektbaums hinzugefügt. Für untergeordnete Ansichcten wird eine dreistellige Zahl an den Namen angehängt. Klicke auf den Pfeil vor den Seite-Objekt, um es aufzuklappen und den Inhalt anzuzeigen.

Wenn nur das Objekt im Projektbaum ausgewählt ist, wird die Ansicht zur ersten Seite des Projekts hinzugefügt. Wenn es mehrere Seiten im Projekt gibt, dann wähle bitte das Objekt aus und die Seite, zu der es hinzugefügt werden soll. Klicke dann auf das Icon, um die Ansicht zur ausgewählten Seite hinzuzufügen.

### Ändern einer existierenden Ansicht {#ändern_einer_existierenden_ansicht}

Klappe das Seite-Objekt im Projektbaum auf und wähle die Ansicht. Deren Parameter können in der Eigenschaftenansicht im Daten-Reiter geändert werden.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Isometric view with smooth lines visibility off](images/Drawing_View_Iso.png‎  style="width:150px;"> <img alt="Isometric view with smooth lines visibility on" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width:150px;">

-   **Label**\'\': ändert die Bezeichnung der Ansicht im Projektbaum. Du kannst auch auf die Ansicht in der Struktur klicken und mit der rechten Maustaste auf → Umbenennen klicken oder **F2** drücken.
-   **Rotation**\': dreht die Ansicht. Beispielsweise erfordert eine isometrische Ansicht eine Drehung um 60 Grad (siehe auch Parameter Richtung unten).
-   **Scale**\': setzt den Maßstab der Ansicht.
-   **X**\': setzt die horizontale Position der Ansicht auf der Seite in Millimetern.
-   **Y**\': setzt die vertikale Position der Ansicht auf der Seite in Millimetern. Bitte beachte, dass sich die Koordinate (0,0) oben links auf der Seite befindet, d.h. je höher die Zahl, desto niedriger ist der Wert auf der Seite.
-   **Direction**\': ändert die Blickrichtung. Es wird durch xyz-Werte gesetzt, die einen Vektor definieren, der normal zur Seite ist. Die Draufsicht wird (0,0,1) und die Isometrie (1,1,1,1) sein. Die Werte können negativ sein.
-   **Show Hidden Lines**\': Schaltet die Sichtbarkeit der versteckten Linien ein oder aus, indem man *True* oder *False* wählt.
-   **Show Smooth Lines**\': Schaltet die Sichtbarkeit der glatten Linien ein oder aus, indem Sie *True* oder *False* wählen. Glatte Linien werden auch als Tangentialkanten bezeichnet. Diese Kanten zeigen Oberflächenveränderungen zwischen tangentialen Oberflächen an.

### Zeichenansichtsassistent

Um ein Zeichnungsblatt mit Standardansichten automatisch zu erstellen, verwenden Sie das [Automatic drawing Macro](Macro_Automatic_drawing.md). 

### Anderes

Falls Du nach der Umschaltung in perspektivisch-orthogonal in der 3D-Ansicht suchst, probiere [Std PerspektivKamera](Std_PerspectiveCamera/de.md) und [Std OrthogonaleKamera](Std_OrthographicCamera/de.md)


{{docnav/de
|[Neue Zeichnung einfügen → A3 Querformat](Drawing_Landscape_A3/de.md)
|[Bemerkung](Drawing_Annotation/de.md)
|[Drawing-Arbeitsbereich](Drawing_Workbench/de.md)
|IconL=Drawing_Landscape_A3.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Annotation.png
}}


{{Drawing Tools navi

}} 
