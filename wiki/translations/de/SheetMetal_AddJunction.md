---
- GuiCommand:
   Name: SheetMetal AddJunction
   Name/de: SheetMetal StoßHinzufügen
   MenuLocation: SheetMetal -> Make Junction
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **S** **J**
   SeeAlso: SheetMetal_AddRelief/de, SheetMetal_AddBend/de
---

# SheetMetal AddJunction/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [Stoß hinzufügen](SheetMetal_AddJunction/de.md) erzeugt einen offenen Stoß zwischen zwei Abschnitten (Kanten/Falze) eines SheetMetal-Objekts. Ohne diese Stöße wären (zusammenhängende) Abschnitte, die mit derselben Grundplatte verbunden sind, nicht abwickelbar.

Dieser Befehl ist der zweite von drei Schritten, um ein Schalenobjekt, das mit dem Arbeitsbereich [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erzeugt wurde, in ein abwickelbares SheetMetal-Objekt umzuwandeln:

1.  [SheetMetal Entlastungsausschnitt hizufügen](SheetMetal_AddRelief/de.md)
2.  [SheetMetal Stoß hinzufügen](SheetMetal_AddJunction/de.md)
3.  [SheetMetal Biegung hinzufügen](SheetMetal_AddBend/de.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Stoß hinzufügen - Kanten aufschneiden*

## Anwendung

1.  Eine oder mehrere Kanten auswählen.
2.  Den Befehl <img alt="" src=images/_SheetMetal_AddJunction.svg  style="width:16px;"> **Stoß hinzufügen** aktivieren durch:
    -   Die Schaltfläche **<img src="images/_SheetMetal_AddJunction.svg_" width=16px> [Stoß hinzufügen](SheetMetal_AddJunction/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/_SheetMetal_AddJunction.svg_" width=16px> Stoß hinzufügen**.
    -   Das Tastenkürzel: **S** dann **J**.

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">

## Hinweise

Die Befehle <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Stoß hinzufügen](SheetMetal_AddJunction/de.md)** und <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Biegung hinzufügen](SheetMetal_AddBend/de.md)** funktionieren am besten mit hohlen Quadern, d.h. Schalenobjekten mit einer konstanten Wandstärke und nur 90° Winkeln zwischen den Flächen.

Siehe [SheetMetal Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de#Hinweise.md) für Hinweise zur Erstellung von Schalenobjekten aus Quadern.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Junction-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften und sein Label hat einen Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Verweise zu den Kanten, die die Position der Stöße bzw. Lücken bestimmen.

-    **gap|Length**: \"Junction Gap\". Standardwert: {{value|2,00 mm}}. Spaltweite des hinzuzufügenden Stoßes.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddJunction/de
