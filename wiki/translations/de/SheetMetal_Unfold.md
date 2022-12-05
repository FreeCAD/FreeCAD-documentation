---
- GuiCommand:/de
   Name:SheetMetal Unfold
   Name/de:SheetMetal Abwickeln
   MenuLocation:SheetMetal → Unfold
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**U**
   SeeAlso:[SheetMetal UnattendedUnfold](SheetMetal_UnattendedUnfold/de.md)
---

# SheetMetal Unfold/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Abwickeln** wickelt ein Blechobjekt ab.

## Anwendung

1.  Eine ebene Fläche eines SheetMetal-Objekts auswählen.
2.  Den Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwickeln](SheetMetal_UnattendedUnfold/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/_SheetMetal_Unfold.svg_" width=16px> [Unfold](SheetMetal_Unfold/de.md)
**
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/de.md)
**
    -   Das Tastenkürzel: **U**
3.  Einstellung der Abwicklungseinstellungen im [Aufgabenbereich](Task_panel/de.md) durch:
    -   Auswahl der Darstellungsoptionen der Abwicklungsskizze.
    -   Auswahl der Regeln für die Abwicklungsableitung mit k-Faktor:
        - Verwendung eines [Material-Datenblatts](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet).
        - Eingabe des [k-Faktors](https://github.com/shaise/FreeCAD_SheetMetal#terminology) von Hand und die Auswahl ob der Berechnung eine [ANSI- oder DIN-Norm](https://de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) zugrunde liegt.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Das SheetMetal-**Unfold**-Objekt, wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Es hat keine zusätzlichen Eigenschaften, aber sein Label hat einen Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    **Label|String**: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

## Einschränkungen

-   Die Blechobjekte sollten eine konstante Wandstärke haben.
-   Ebene Flächen sollten keine Trennlinien (?) enthalten.
-   Ebene Flächen sollten wirklich eben sein und keine B-Spline-Annäherungen.
-   Die Flächen der Bögen müssen wirklich zylindrisch sein und ebenfalls keine B-Spline-Annäherungen.
-   Das Unfold-Objekt ist nicht parametrisch. Wird das Modell geändert, muss es erneut abgewickelt werden.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Unfold/de
