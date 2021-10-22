---
- GuiCommand:/de
   Name:SheetMetal AddJunction
   Name/de:SheetMetal StoßHinzufügen
   MenuLocation:SheetMetal → Make Junction
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**S** **J**
---

# SheetMetal AddJunction/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Der Befehl <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> **Stoß hinzufügen**\...


</div>

This command is the second of three steps to convert a shell object made with the [Part Workbench](Part_Workbench.md) or [PartDesign Workbench](PartDesign_Workbench.md) into an unfoldable sheet metal object:

1.  [SheetMetal AddRelief](SheetMetal_AddRelief.md)
2.  [SheetMetal AddJunction](SheetMetal_AddJunction.md)
3.  [SheetMetal AddBend](SheetMetal_AddBend.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;">


<div class="mw-translate-fuzzy">



*Kante mit Stoß versehen*


</div>

## Anwendung


<div class="mw-translate-fuzzy">

Eine Kante zwischen zwei Flächen durch einen Stoß ersetzen:

:   (Das englische Original muss überarbeitet werden\...)

1.  Start with a base plate or sheet, select a corner vertex to apply relief
2.  Click on the <img alt="" src=images/SheetMetal_Junction.svg  style="width:24px;"> **Junction** tool to add a junction cut to corner.


</div>

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">

## Notes

The commands <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **_**, and <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal AddBend](SheetMetal_AddBend.md)** work best with hollow cuboids i.e. shell objects with a constant thickness and only 90° angles between faces.

See [SheetMetal AddRelief](SheetMetal_AddRelief#Notes.md) for hints about creating shell objects of cuboids.

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




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddJunction/de
