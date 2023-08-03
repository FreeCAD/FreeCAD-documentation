---
 GuiCommand:
   Name: TechDraw  ActiveView
   Name/de: TechDraw AktiveAnsicht
   MenuLocation: TechDraw , Views From Other Workbenches , Aktive Ansicht einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_Image/de
---

# TechDraw ActiveView/de



## Beschreibung

Das Werkzeug **TechDraw AktiveAnsicht** fügt eine Bitmap-Abbildung des aktiven 3D-Fensters in ein Zeichnungsblatt ein.

![](images/TechDraw_ActiveView_example.png ) 
*Eine einfache Ansicht aus dem 3D-Modell.*



## Anwendung

1.  Zur richtigen [3D-Ansicht](3D_view/de.md) wechseln.
2.  Wenn sich mehrere Zeichnungsblätter im Dokument befinden, kann man das gewünschte Blatt in der [Baumansicht](Tree_view/de.md) auswählen.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ActiveView.svg" width=16px> [Aktive (3D-)Ansicht einfügen](TechDraw_ActiveView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Views From Other Workbenches → <img src="images/TechDraw_ActiveView.svg" width=16px> Aktive (3D-)Ansicht einfügen** auswählen.
4.  Wenn sich mehrere Zeichnungsblätter im Dokument befinden und noch kein Blatt ausgewählt wurde, öffnet sich der Dialog **Blattauswahl** {{Version/de|0.20}}:
    1.  Das gewünschte Zeichnungsblatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
5.  Der Aufgabenbereich **Aktive Ansicht wird TD-Ansicht** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
6.  Die Schaltfläche **OK** drücken.



## Optionen

Folgendes kann eingestellt werden:

-    **Crop**: Wenn aktiviert, wird die erstellte Abbildung beschnitten.

-    **Width**: Die Beschnittbreite (in mm) für die Abbildung.

-    **Height**: Die Beschnitthöhe (in mm) für die Abbildung.

-    **No Background**: Wenn aktiviert, erhält die Abbildung einen transparenten Hintergrund.

-    **Solid Background**: Wenn aktiviert, erhält die Abbildung einen einfarbigen Hintergrund in der ausgwählten Farbe.

-    **Use 3d Background**: Wenn aktiviert, erhält die Abbildung den Hintergrund der 3D-Ansicht.



## Hinweise

-   Aktive Ansichten sind statisch; nach der Erzeugung werden sie nicht mehr aktualisiert, wenn sich das 3D-Modell ändert.
-   Eine aktive Ansicht ist im Grunde ein [Bild](TechDraw_Image/de.md). Seine {{PropertyData/de|Scale Type}} wird daher immer als {{Value|Custom}} (benutzerdefiniert) voreingestellt.
-   In {{VersionMinus/de|0.20}} war AktiveAnsicht ein [Symbol](TechDraw_Symbol/de.md).



## Eigenschaften

Siehe [TechDraw Bild](TechDraw_Image/de#Eigenschaften.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/de
