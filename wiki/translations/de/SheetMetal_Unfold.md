---
 GuiCommand:
   Name: SheetMetal Unfold
   Name/de: SheetMetal Abwickeln
   MenuLocation: SheetMetal , Unfold
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **U**
   SeeAlso: SheetMetal_UnattendedUnfold/de
---

# SheetMetal Unfold/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Abwickeln** wickelt ein Blechobjekt ab.



## Anwendung

1.  Eine ebene Fläche eines SheetMetal-Objekts auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/_SheetMetal_Unfold.svg_" width=16px> [Unfold](SheetMetal_Unfold/de.md)** drücken.
    -   Den Menüeintrag **Sheet Metal → <img src="images/SheetMetal_Unfold.svg" width=16px> Abwickeln** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **Sheet Metal → <img src="images/SheetMetal_Unfold.svg" width=16px> Abwickeln** im Kontextmenü auswählen.
    -   Das Tastaturkürzel: **U**.
3.  Das [Aufgaben-Fenster](Task_panel/de.md) **SheetMetal-Ojekt abwickeln** wird geöffnet.
4.  Abwicklungseinstellungen im [Aufgaben-Fenster](Task_panel/de.md) anpassen:
    -   Wahlweise die Darstellungsoptionen der Abwicklungsskizze aktivieren und die Farben einstellen.
    -   Wahlweise die Option **Skizze exportieren** aktivieren.
    -   Wenn kein **Material Definition Sheet** verwendet wird (siehe [Hinweise](#Hinweise.md)):
        1.  Die Option **Material Definition Sheet** auf {{Value|Manual K-Factor}} stellen.
        2.  Wahlweise die Radioknöpfe ANSI oder DIN umschalten (siehe [Hinweise](#Hinweise.md)).
        3.  Den Wert für den K-Factor anpassen (siehe [Hinweise](#Hinweise.md)).
    -   Wahlweise den Transparenzwert für die Abwicklung anpassen.
5.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
6.  Ein **Unfold**-Objekt wird erstellt.
7.  Wahlweise die Parameter im [Eigenschafteneditor](Property_editor/de.md) anpassen.



## Hinweise

-   Siehe die Abschnitte [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet) und [K-factor](https://github.com/shaise/FreeCAD_SheetMetal#physical-material-definitions) der Projektseite für weitere Informationen.
-   Eine Erklärung der Wertebereich von ISO- und ANSI-K-Faktoren siehe Tabelle auf [dieser](https://de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) Seite.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Das SheetMetal-**Unfold**-Objekt, wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Es hat keine zusätzlichen Eigenschaften.



## Einschränkungen

-   Die Blechobjekte sollten eine konstante Wandstärke haben.
-   Ebene Flächen sollten keine Trennlinien (?) enthalten.
-   Ebene Flächen sollten wirklich eben sein und keine B-Spline-Annäherungen.
-   Die Flächen der Bögen müssen wirklich zylindrisch sein und ebenfalls keine B-Spline-Annäherungen.
-   Versionen vor 0.5.00: Das Unfold-Objekt ist nicht parametrisch. Wird das Modell geändert, muss es erneut abgewickelt werden.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Unfold/de
