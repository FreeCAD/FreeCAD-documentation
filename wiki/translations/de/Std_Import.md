---
 GuiCommand:
   Name: Std Import
   Name/de: Std Import
   MenuLocation: Datei , Import
   Workbenches: Alle
   Shortcut: **Strg**+**I**
   SeeAlso: Std_Open/de, Import_Export/de, Import_Export_Preferences/de
---

# Std Import/de



## Beschreibung

Der Befehl **Std Import** importiert Geometrie aus einem anderen Dateiformat in das aktive Dokument. Es werden viele Dateiformate unterstützt und für einige Formate gibt es mehrere Importoptionen. Siehe [Import Export](Import_Export/de.md) für weitere Informationen.


{{Version/de|0.21}}

: Wird ein Bildformat ausgewählt, erstellt der Befehl eine [Bildebene](#Bildebene.md).



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die **Datei → <img src="images/Std_Import.svg" width=16px> Importieren...** Option aus dem Menü.
    -   Verwende das Tastaturkürzel: **Ctrl**+**I**.
2.  Wähle optional das richtige Dateiformat im Dialogfeld.
3.  Wähle eine Datei.
4.  Drücke die **Öffnen** Schaltfläche.



## Optionen

-   Drücke **Esc** oder die Taste **Cancel**, um den Befehl abzubrechen.



## Hinweise

-   Um ein importiertes [Polygonnetz Objekt](Mesh_Workbench/de.md) in einen Festkörper zu konvertieren, siehe das [Importieren aus STL oder OBJ](Import_from_STL_or_OBJ/de.md) Tutoriuml.
-   Zum Importieren in ein neues Dokument kannst du den Befehl [Std Öffnen](Std_Open/de.md) verwenden.
-   Einige Arbeitsbereiche haben zusätzliche Importbefehle. Siehe: [Import Export](Import_Export/de.md).



## Einstellungen

-   Siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).
-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Voreinstellungen → Allgemein → DateiÖffnenSpeichernPfad**.
-   Der zuletzt verwendete Importfilter wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Voreinstellungen → Allgemein → DateiImportFilter**.



## Bildebene

Eine Bildebene ist die planare Darstellung eine Bildes in der [3D-Ansicht](3D_view/de.md). Sie kann z.B. bei der Erstellung eines Modells verwendet werden, das auf Fotos eines existierenden Objekts basiert.

Standardmäßig wird die Bildebene auf der globalen XY-Ebene angelegt. Die Ausgangsgröße einer Bildebene wird mit einer Auflösung von 96 Pixel/Zoll berechnet.



### Bearbeiten

1.  Zum bearbeiten einer Bildebene gibt es folgende Möglichkeiten:
    -   Ein Doppelklick auf die Bildebene In der [Baumansicht](Tree_view/de.md).
    -   Ein Rechtsklick auf die Bildebene in der Baumansicht und die Menüoption **<img src="images/Image-scaling.svg" width=16px> Bild ändern...** im Kontextmenü auswählen.

2.  Ist die Bildebene nicht parallel zu einer der XY-, XZ- oder YZ-Ebenen des globalen Koordinatensystems, wird sie parallel zur XY-Ebene ausgerichtet.

3.  Der Aufgaben-Bereich **Bildebenen-Einstellungen** wird geöffnet.

4.  Wahlweise die **XY-Ebene**, **XZ-Ebene** oder **YZ-Ebene** des globalen Koordinatensystems auswählen.

5.  
    **Richtung umkehren**aktivieren, um die Bildebene um 180° zu drehen. Die Drehachse hängt von der ausgewählten Ebene ab. Für die XY-Ebene ist es die globale X-Achse. Für die XZ- und YZ-Ebene ist es die globale Z-Achse.

6.  
    **Offset**, **X-Abstand** und **Y-Abstand** liegen relativ zum Koordinatensystem der Bildebene. Ein geringer negativer Abstand kann nützlich sein, wenn das Bild mit einer [Skizze](Sketcher_Workbench/de.md) oder [Draft](Draft_Workbench/de.md)-Geometrie nachgezeichnet wird.

7.  Wahlweise die Transparenz (**Transparency**) ändern.

8.  
    **Bildgröße**einstellen:

    -   Skalieren durch numerische Eingabe:
        1.  Wahlweise **Seitenverhältnis beibehalten** deaktivieren für uneinheitliche Skalierung.
        2.  Eine **Breite** und/oder eine **Höhe** eingeben.
    -   Skalieren durch Anklicken von Punkten:
        1.  Die Schaltfläche **Kalibrieren** drücken.

        2.  Zwei Punkte innerhalb des Bildes anklicken.

        3.  Eine Maßlinie wird angezeigt.

        4.  Die gewünschte Länge eingeben.

        5.  
            **Enter**
            
            oder die Schaltfläche **Übernehmen** drücken.

9.  Die Schaltfläche **OK** drücken, um die Änderunge zu bestätigen und den Aufgaben-Bereich zu schließen.



### Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Bildebene (Image-Plane-Objekt) wird von einem [App GeoFeature](App_GeoFeature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



#### Daten


{{TitleProperty|Image Plane}}

-    {{PropertyData/de|Image File|FileIncluded}}: Die Bilddatei, die für die Bildebene verwendet wird. Diese Datei wird in der **.FCStd**-Datei gespeichert.

-    {{PropertyData/de|XSize|Length}}: Die Breite der Bildebene.

-    {{PropertyData/de|YSize|Length}}: Die Höhe der Bildebene.



#### Ansicht


{{TitleProperty|Object Style}}

-    {{PropertyView/de|Lighting|Enumeration}}: Gibt an, wie die Bildebene in der [3D-Ansicht](3D_view/de.md) beleuchtet wird. Kann {{value|Two side}} oder {{value|One side}} sein.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/de
