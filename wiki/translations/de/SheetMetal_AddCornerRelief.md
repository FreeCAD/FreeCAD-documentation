---
- GuiCommand:/de
   Name:SheetMetal AddCornerRelief
   Name/de:SheetMetal EckentlastungHinzufügen
   MenuLocation:SheetMetal → Add Corner Relief
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**C** **R**
---

# SheetMetal AddCornerRelief/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md) fügt einer Ecke einen Ausschnitt zur Eckentlastung hinzu.

## Anwendung

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-CornerRelief-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften und sein Label hat eine Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|ReliefSketch|Enumeration}}: \"Corner Relief Type\". {{value|Circle}} (standard), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{PropertyData/de|Size|Length}}: \"Size of Shape\". Größe der Form, Standardwert: {{value|3,00 mm}}.

-    {{PropertyData/de|Size Ratio|Float}}: \"Size Ratio of Shape\". Größenverhältnis der Form, Standardwert: {{value|1,50}}.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verweis zu dem Kantenpaar, das die Lage der Eckentlastung bestimmt.

-    {{PropertyData/de|kfactor|FloatConstraint}}: \"Neutral Axis Position\". Lage der neutralen Faser, Standardwert: {{value|0,50}}.


{{Properties_Title/de|Parameters1}}

-    {{PropertyData/de|Sketch|Link}}: \"Corner Relief Sketch\".

-    {{PropertyData/de|XOffset|Distance}}: \"Gap from side one\". Abstand von der ersten Seite, Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|YOffset|Distance}}: \"Gap from side two\". Abstand von der zweiten Seite, Standardwert: {{value|0,00 mm}}.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief/de
