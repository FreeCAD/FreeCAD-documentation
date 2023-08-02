---
- GuiCommand:
   Name: SheetMetal AddRelief
   Name/de: SheetMetal EntlastungsausschnittHinzufügen
   MenuLocation: SheetMetal -> Make Relief
   Workbenches: SheetMetal Workbench/de
   Shortcut: **S** **R**
   SeeAlso: SheetMetal_AddJunction/de, SheetMetal_AddBend/de
---

# SheetMetal AddRelief/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Relief.svg  style="width:16px;"> [Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md) erzeugt Eckentlastungen, Ausschnitte an den Eckpunkten, an denen sich drei Abschnitte (Grundplatte/Kanten/Falze) eines SheetMetal-Objekts treffen. Ohne diese Entlastungen wäre das Objekt nicht abwickelbar.

Dieser Befehl ist der erste von drei Schritten, um ein Schalenobjekt, das mit dem Arbeitsbereich [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erzeugt wurde, in ein abwickelbares SheetMetal-Objekt umzuwandeln:

1.  [SheetMetal Entlastungsausschnitt hizufügen](SheetMetal_AddRelief/de.md)
2.  [SheetMetal Stoß hinzufügen](SheetMetal_AddJunction/de.md)
3.  [SheetMetal Biegung hinzufügen](SheetMetal_AddBend/de.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Entlastungsausschnitt hinzufügen - Ecken abschneiden*

## Anwendung

1.  Einen oder mehrere Eckpunkte auswählen.
2.  Den Befehl <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddRelief.svg" width=16px> [Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Entlastungsausschnitt hinzufügen**.
    -   Das Tastenkürzel: **S** dann **R**.

<img alt="" src=images/SheetMetal_ConvertShellObject-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;">

## Hinweise

Die Befehle <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Stoß hinzufügen](SheetMetal_AddJunction.md)** und <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Biegung hinzufügen](SheetMetal_AddBend.md)** funktionieren am besten mit hohlen Quadern, d.h. Schalenobjekten mit einer konstanten Wandstärke und nur 90° Winkeln zwischen den Flächen.

Schalenobjekte können mit Befehlen der Arbeitsbereiche <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/de.md) oder <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/de.md) erstellt werden.

Zum Erstellen eines hohlen Quaders mit dem Arbeitsbereich [Part](Part_Workbench/de.md):

1.  Einen Festkörper erstellen durch
    -   Anwendung des Befehls <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Würfel (Box)](Part_Box/de.md)
    -   Verwendung des Befehls <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrudieren\...](Part_Extrude/de.md) mit
        -   einem <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rechteck](Draft_Rectangle/de.md).
        -   einem <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Linienzug](Draft_Wire/de.md).
        -   einer <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Skizze](Sketcher_NewSketch/de.md).
2.  Den Befehl <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Dicke\...](Part_Thickness.md) verwenden, um aus dem Festkörper ein Schalenobjekt zu erzeugen (typischerweise mit einer Wandstärke, die der Blechstärke entspricht).

Zum Erstellen eines hohlen Quaders mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md):

1.  Einen Festkörper erstellen durch
    -   Anwendung des Befehls <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Zu addierender Quader](PartDesign_AdditiveBox/de.md).
    -   <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad/de.md) mit einer <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Skizze](Sketcher_NewSketch/de.md).
2.  Den Befehl <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Dicke](PartDesign_Thickness/de.md) verwenden, um aus dem Festkörper ein Schalenobjekt zu erzeugen (typischerweise mit einer Wandstärke, die der Blechstärke entspricht).

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Relief-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften und sein Label hat eine Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verweise zu den Eckpunkten, die die Lage der Entlastungsausschnitte bestimmen.

-    {{PropertyData/de|relief|Length}}: \"Relief Size\". Größe der Entlastungsausschnitte, Standardwert: {{value|2,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddRelief/de
