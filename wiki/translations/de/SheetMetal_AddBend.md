---
- GuiCommand:
   Name:SheetMetal AddBend
   Name/de:SheetMetal BiegungHinzufügen
   MenuLocation:SheetMetal → Make Bend
   Workbenches:[SheetMetal (Blech)](SheetMetal_Workbench/de.md)
   Shortcut:**S** **B**
   SeeAlso:[SheetMetal Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md), [SheetMetal Stoß hinzufügen](SheetMetal_AddJunction/de.md)
---

# SheetMetal AddBend/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> [Biegung hinzufügen](SheetMetal_AddBend/de.md) tauscht scharfe Kanten zwischen zwei Abschnitten (Grundplatte/Kanten/Falze) eines SheetMetal-Objekts gegen runde Biegungen aus. Ohne diese Bögen wären das Objekt nicht abwickelbar.

Dieser Befehl ist der dritte von drei Schritten, um ein Schalenobjekt, das mit dem Arbeitsbereich [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erzeugt wurde, in ein abwickelbares SheetMetal-Objekt umzuwandeln:

1.  [SheetMetal Entlastungsausschnitt hizufügen](SheetMetal_AddRelief/de.md)
2.  [SheetMetal Stoß hinzufügen](SheetMetal_AddJunction/de.md)
3.  [SheetMetal Biegung hinzufügen](SheetMetal_AddBend/de.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:200px;"> 
*Biegung hinzufügen - Scharfe Kanten durch Bögen ersetzen*

## Anwendung

1.  Eine oder mehrere Kanten auswählen.
2.  Den Befehl <img alt="" src=images/_SheetMetal_AddBend.svg  style="width:16px;"> **Biegung hinzufügen** aktivieren durch:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddBend.svg" width=16px> [Biegung hinzufügen](SheetMetal_AddBend/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Biegung hinzufügen**.
    -   Das Tastenkürzel: **S** dann **R**.

<img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-08.png  style="width:200px;">

## Hinweise

Die Befehle <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Stoß hinzufügen](SheetMetal_AddJunction/de.md)** und <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Biegung hinzufügen](SheetMetal_AddBend/de.md)** funktionieren am besten mit hohlen Quadern, d.h. Schalenobjekten mit einer konstanten Wandstärke und nur 90° Winkeln zwischen den Flächen.

Siehe [SheetMetal Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de#Hinweise.md) für Hinweise zur Erstellung von Schalenobjekten aus Quadern.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-SolidBend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften und sein Label hat eine Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standard Wert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|base Object|LinkSub}}: \"Base object\". Verknüpfungen zu den Kanten, die gebogen werden sollen.

-    {{PropertyData/de|radius|Length}}: \"Bend Radius\". Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de|thickness|Length}}: \"Thickness of sheetmetal\". Standardwert: {{value|1,00 mm}}.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBend/de
