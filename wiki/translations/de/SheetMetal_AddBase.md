---
- GuiCommand:/de
   Name:SheetMetal AddBase
   Name/de:SheetMetal BasisprofilErstellen
   MenuLocation:SheetMetal → Make Base Wall
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**C** **B**
---

# SheetMetal AddBase/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Basisprofil erstellen](SheetMetal_AddBase/de.md) erzeugt ein SheetMetal-Basisobjekt aus einer Skizze.


<div class="mw-translate-fuzzy">

Er erzeugt entweder ein prismatisches Profil aus einer offenen Kontur oder eine Platine aus einem geschlossenen Umriss.


</div>

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

From a closed outline it creates a base **plate** (blank):

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">

## Anwendung

### Profile


<div class="mw-translate-fuzzy">

Dieses Werkzeug erzeugt ein Blech auf der Basis einer Skizze:

-   Eine offene Skizzenkontur wird mit einer bestimmten Länge ({{Parameter|length}}) extrudiert und erzeugt ein Blech mit einer gewählten Stärke ({{Parameter|thickness}}) und vorgegebenen Kantradius ({{Parameter|radius}}). Der Parameter {{Parameter|bend side}} bestimmt die Lage des Bleches bezüglich der Skizzenlinie.
-   Eine geschlossene Skizzenkontur wird zu einer Platine mit einer gewählten Stärke ({{Parameter|thickness}}) extrudiert. In diesem Falle werden die Parameter {{Parameter|length}} und {{Parameter|radius}} nicht benutzt.


</div>

### Plate

1.  Select a **closed outline** <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  Activate the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [SheetMetal AddBase](SheetMetal_AddBase.md) (see above).
3.  Adjust the plate\'s parameter by editing the corresponding value in the [Property editor](Property_editor.md):
    -   The property **thickness** for the thickness of the plate.

:   

    :   (The properties **length** and **radius** are not used for plates.)

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-BaseBend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standard Wert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Bend Side|Enumeration}}: Profillage. Außen, innen oder mittig (entlang der Skizzenlinie),  Werte: {{value|Outside}} (standard), {{value|Inside}}, {{value| Middle}}.

-    **Bend Sketch|Link**: \"Wall Sketch object\". Verweis zur Profil- bzw. Umriss-Skizze.

-    {{PropertyData/de|Mid Plane|Bool}}: \"Extrude Symmetric to Plane\". Ausdehnung symmetrisch zur Ebene.   `True`, das Profil dehnt sich symmetrisch zu beiden Seiten der Skizzenebene aus.

-    {{PropertyData/de|Reverse|Bool}}: \"Reverse Extrusion Direction\". Extrusionsrichtung umkehren, Standardwert: `False`.

-    {{PropertyData/de|length|Length}}: \"Length of wall\". Länge des Profils, Standardwert: {{value|100,00 mm}}.

-    {{PropertyData/de|radius|Length}}: \"Bend Radius\". Biegeradius, Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de| thickness|Length}}: \"Thickness of sheetmetal\". Blechstärke, Standardwert: {{value|1,00 mm}}.




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddBase/de
