---
- GuiCommand:/de
   Name:SheetMetal AddWall
   Name/de:SheetMetal KanteAnsetzen
   MenuLocation:SheetMetal → Make Wall
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**W**
---

# SheetMetal AddWall/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> [Kante ansetzen](SheetMetal_AddWall/de.md) erzeugt am gewählten Flächenrand eine Kante (Umbug).

<img alt="" src=images/PostBend.png  style="width:320px;">

## Anwendung

Um eine Kante hinzuzufügen:

1.  Zur <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [Blech](SheetMetal_Workbench/de.md)-Arbeitsumgebung wechseln.
2.  Mit einer Basisplatte oder einem Blech starten und eine oder mehrere Randflächen auswählen, die eine Kante (Umbug) erhalten sollen.
3.  Schaltfläche <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> [Kante ansetzen](SheetMetal_AddWall/de.md) drücken, um die Kante(n) hinzuzufügen.


**Hinweis**

: Um eine Grundplatte (Platine) zu erstellen, verwendet man eine geschlossene 2D-Kontur - vorzugsweise eine <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Skizze](Sketcher_NewSketch.md) - mit dem Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Basisprofil erstellen](SheetMetal_AddBase/de.md).
Alternativ kann man eine Grundplatte auch mit einer der folgenden Methoden erstellen:

:\* Methode 1: Einen <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Würfel](Part_Box/de.md) erstellen

:\* Methode 2: Einen Festkörper extrudieren mit <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrudieren](Part_Extrude/de.md) aus wahlweise

::\* Einem <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rechteck](Draft_Rectangle/de.md)

::\* Einem <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Linienzug](Draft_Wire/de.md)

::\* Einer <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Skizze](Sketcher_NewSketch.md)

::\* Dann <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Dicke\...](Part_Thickness/de.md) verwenden, um ein Schalenobjekt zu erstellen (**Typischerweise mit der Wandstärke des Blechs.**)

:\* Methode 3: Einen <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Körper](PartDesign_Body/de.md) erstellen und Objekte der folgenden Werkzeuge hinzufügen

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Zu addierender Quader](PartDesign_AdditiveBox/de.md)

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Extrudieren](PartDesign_Pad/de.md) aus einer <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Skizze](Sketcher_NewSketch/de.md).

::\* Dann <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Dicke](PartDesign_Thickness/de.md) verwenden, um ein Schalenobjekt zu erstellen (**Typischerweise mit der Wandstärke des Blechs.**)

:   

    :   Wenn mit <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Körper erstellen](PartDesign_Body/de.md) gestartet wird, können SheetMetal-Werkzeuge mit PartDesign-Werkzeugen wie z.B. <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Tasche](PartDesign_Pocket/de.md) oder <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [Bohrung](PartDesign_Hole/de.md) gemischt werden.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Bend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften und sein Label hat eine Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Bend Type|Enumeration}}: \"Bend Type\". {{value|Material Outside}} (standard), {{value|Material Inside}}, {{value|Thickness Outside}}, {{value|Offset}}.

-    {{PropertyData/de|angle|Angle}}: \"Bend Angle\". Biegewinkel. Standardwinkel {{value|90,00°}}.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verknüpfung zur ebenen Fläche, an die eine Kante angesetzt werden soll.

-    {{PropertyData/de|gap1|Distance}}: \"Gap from Left side\". Lücke von links. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|gap2|Distance}}: \"Gap from Right side\". Lücke von rechts. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|invert|Bool}}: \"Invert Bend Direction\". Biegerichtung umkehren. Standardwert: `False`.

-    {{PropertyData/de|length|Length}}: \"Length of Wall\". Schenkellänge (ab Bogen). Standardwert: {{value|10,00 mm}}.

-    {{PropertyData/de|radius|Length}}: \"Bend Radius\". Biegeradius (Innenradius). Standardwert: {{value|1,00 mm}}.


{{Properties_Title/de|Parameters Ext.}}

-    {{PropertyData/de|Auto Miter|Bool}}: \"Enable Auto Miter\". Automatische Gehrung aktivieren. Standardwert: `True`.

-    {{PropertyData/de|extend1|Distance}}: \"Extend from Left Side\". Erweiterung von links. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|extend2|Distance}}: \"Extend from Right Side\". Erweiterung von rechts. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|kfactor|FloatConstraint}}: \"Location of Neutral Line. Caution: Using ANSI standards, not DIN.\". Lage der neutralen Faser nach ANSI-Norm, nicht nach DIN.  Standardwert: {{value|0,50}}. K factor (also known as neutral factor) for the bend. Used to calculate bend allowance when unfolding.

-    {{PropertyData/de|max Extend Dist|Length}}: \"Auto Miter maximum Extend Distance\". Automatische Gehrung, maximale Länge der Erweiterung. Standardwert: {{value|5,00 mm}}.

-    {{PropertyData/de|min Gap|Length}}: \"Auto Miter Minimum Gap\". Automatische Gehrung, minimale Lücke. Standardwert: {{value|0,10 mm}}.

-    {{PropertyData/de|miterangle1|Angle}}: \"Bend Miter Angle from Left Side\". Gehrungswinkel von links. Standardwinkel: {{value|0,00°}}.

-    {{PropertyData/de|miterangle2|Angle}}: \"Bend Miter Angle from Right Side\". Gehrungswinkel von rechts. Standardwinkel: {{value|0,00°}}.

-    {{PropertyData/de|offset|Distance}}: \"Offset Bend\". Versatz der Biegung. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|unfold|Bool}}: \"Shows Unfold View of Current Bend\". Abwicklung der aktuellen Kante anzeigen. Standardwert:  `True` erzeugt die Abwicklung der Kante.


{{Properties_Title/de|Parameters Ex2}}

-    {{PropertyData/de|Sketch|Link}}: \"Sketch Object\". Skizzenobjekt.

-    {{PropertyData/de|sketchflip|Bool}}: \"Flip Sketch Direction\". Skizzenrichtung umkehren. Standardwert: `False`.

-    {{PropertyData/de|sketchinvert|Bool}}: \"Invert Sketch Start\". Standardwert: `False`.


{{Properties_Title/de|Parameters Ex3}}

-    {{PropertyData/de|Length List|FloatList}}: \"Length of Wall List\". Standardwert: {{value|[10,00]}}.

-    {{PropertyData/de|bend AList|FloatList}}: \"Bend Angle List\". Standardwert: {{value|[90,00]}}.


{{Properties_Title/de|Parameters Relief}}

-    {{PropertyData/de|Relief Factor|Float}}: \"Relief Factor\". Standardwert: {{value|0,70}}.

-    {{PropertyData/de|Use Relief Factor|Bool}}: \"Use Relief Factor\". Standardwert: `False`.

-    {{PropertyData/de|min Relief Gap|Length}}: \"Minimum Gap to Relief Cut\". Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de|relief Type|Enumeration}}: \"Relief Type\". {{value|Rectangle}} (standard), {{value|Round}}. Enabled only when a gap value is set.

-    {{PropertyData/de|reliefd|Length}}: \"Relief Depth\". Standardwert: {{value|1,00 mm}}. Enabled only when a gap value is set.

-    {{PropertyData/de|reliefw|Length}}: \"Relief Width\". Standardwert: {{value|0,80 mm}}. Enabled only when a gap value is set.

## Beispiel

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;"> 
*Eine einfache Schale*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Vorbereitung

Diese Schale besteht aus einer rechteckigen Platine mit an ihren Umrisskanten (-Linien) angefügten Kanten. Also muss eine Skizze für die Platine vorbereitet werden.

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> <img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
*Nur eine rechteckige Kontur*

### Arbeitsablauf

1.  Eine Platine erstellen
    1.  Die Konturskizze auswählen  <img alt="" src=images/SheetMetal_AddWall-03.png  style="width:240px;">
    2.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_AddWall-04.png  style="width:240px;">  (Die Platine wird in Z-Richtung aufgedickt)  
2.  Kanten an die Umrisskanten anfügen
    1.  Auswahl der **Umrisskanten** der Platine  <img alt="" src=images/SheetMetal_AddWall-05.png  style="width:240px;">
    2.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_AddWall-06.png  style="width:240px;">
    3.  Wenn die Kanten mit 90° nach unten zeigen, setzt man den Wert der Eigenschaft **invert** auf true, um die Richtung umzukehren (und den von **length** auf einen niedrigeren Wert für kürzere Kanten)  <img alt="" src=images/SheetMetal_AddWall-01.png  style="width:240px;">  
3.  Noch mehr Kanten hinzufügen
    1.  Die **oberen Umrisskanten** auswählen  <img alt="" src=images/SheetMetal_AddWall-08.png  style="width:240px;">
    2.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_AddWall-09.png  style="width:240px;"> 
    3.  Die Kanten sind jetzt ein wenig zu lang (aber schön beschnitten), also muss die Eigenschaft **length** auf einen niedrigeren Wert gesetzt werden  <img alt="" src=images/SheetMetal_AddWall-10.png  style="width:240px;">
    4.  Sollen die Kanten nach außen aufgestellt werden, muss der Wert **invert** auf true gesetzt werden  <img alt="" src=images/SheetMetal_AddWall-11.png  style="width:240px;">

Fertig!


</div>


</div>




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category:SheetMetal.md) > SheetMetal AddWall/de
