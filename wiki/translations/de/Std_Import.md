---
- GuiCommand:
   Name: Std Import
   Name/de: Std Import
   MenuLocation: Datei - Import
   Workbenches: Alle
   Shortcut: **Strg**+**I**
   SeeAlso: [Std Öffnen](Std_Open/de.md), [Import Export](Import_Export/de.md), [Import Export Einstellungen](Import_Export_Preferences/de.md)
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

1.  To edit an Image Plane do one of the following:
    -   Double-click the Image Plane in the [Tree view](Tree_view.md).
    -   Right-click the Image Plane in the Tree view and select **<img src="images/Image-scaling.svg" width=16px> Change image...** from the context menu.

2.  If the Image Plane is not plane-parallel to the XY, XZ or YZ plane of the global coordinate system, it is realigned to be plane-parallel to the XY plane.

3.  The **Image plane settings** task panel opens.

4.  Optionally select the **XY-Plane**, **XZ-Plane** or **YZ-Plane** of the global coordinate system.

5.  Check **Reverse direction** to rotate the Image Plane 180°. The rotation axis depends on the selected plane. For the XY plane it is the global X axis. For the XZ and YZ plane it is the global Z axis.

6.  The **Offset**, **X distance** and **Y distance** are relative to the coordinate system of the Image Plane. A small negative offset can be useful when tracing the image with a [sketch](Sketcher_Workbench.md) or [Draft](Draft_Workbench.md) geometry.

7.  Optionally change the **Transparency**.

8.  
    **Image size**options:

    -   Scale by numerical input:
        1.  Optionally uncheck **Keep aspect ratio** for unequal scaling.
        2.  Enter a **Width** and/or **Height**.
    -   Scale by picking points:
        1.  Press the **Calibrate** button.
        2.  Pick two points inside the image.
        3.  A dimension line is displayed.
        4.  Enter the desired dimension.
        5.  Press **Enter** or the **Apply** button.

9.  Press the **OK** button to confirm the changes and close the task panel.



### Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Bildebene (Image-Plane-Objekt) wird von einem [App GeoFeature](App_GeoFeature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



#### Daten


{{TitleProperty|Image Plane}}

-    **Image File|FileIncluded**: The image file used for the Image Plane. This file is stored in the **.FCStd** file.

-    **XSize|Length**: The width of the Image Plane.

-    **YSize|Length**: The height of the Image Plane.



#### Ansicht


{{TitleProperty|Object Style}}

-    **Lighting|Enumeration**: How the Image Plane is illuminated in the [3D view](3D_view.md). Can be {{value|Two side}} or {{value|One side}}.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/de
