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

Ein Blechteil abwickeln:

1.  Zum Arbeitsbereich <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [SheetMetal](SheetMetal_Workbench.md) wechseln.
2.  Auswahl einer ebenen Fläche des Blechteils. **Hinweis**: Die Fläche sollte eine Ebene und die Wandstärke kontant sein.
3.  Die Schaltfläche <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Unfold** anklicken, um ein Menü im Aufgabenbereich anzuzeigen, mit dem die Abwicklungseinstellungen verwaltet werden.
4.  Auswahl der Darstellungsoptionen der Abwicklungsskizze.
5.  Auswahl der Regeln für die Abwicklungsableitung mit [k-Faktor](https://github.com/shaise/FreeCAD_SheetMetal#terminology):
    -   Verwendung eines [Material-Datenblatts](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet)
    -   Oder Eingabe des [k-Faktors](https://github.com/shaise/FreeCAD_SheetMetal#terminology) von Hand und die Auswahl ob der Berechnung eine ANSI- oder DIN-Norm zugrunde liegt.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Dieses Werkzeug erstellt ein Unfold-Objekt und hat keinen eigenen Repräsentanten in der [Baumansicht](Tree_view/de.md) oder sonstwo und hat daher auch keine Eigenschaften.

Das **Unfold**-Objekt, andererseits, wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Es hat keine zusätzlichen Eigenschaften, aber sein Label hat einen Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    **Label|String**: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

## Einschränkungen

-   Blechobjekte sollten eine konstante Wandstärke haben
-   Flat faces should be planar with no split lines
-   Bend angles should be radius with cylindrical faces
-   Das Unfold-Objekt ist bisher nicht parametrisch.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Unfold/de
