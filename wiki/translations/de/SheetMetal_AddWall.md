---
 GuiCommand:
   Name: SheetMetal AddWall
   Name/de: SheetMetal KanteAnsetzen
   MenuLocation: Sheet Metal , Kante ansetzen
   Workbenches: SheetMetal Workbench/de
   Shortcut: **W**
---

# SheetMetal AddWall/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> [Kante ansetzen](SheetMetal_AddWall/de.md) erzeugt Kanten (Falze) an den ausgewählten Flächenrändern einer Grundplatte. Durch das Ändern der {{PropertyData/de|angle}} kann aus einer Kante ein Falz werden.

Eine **Kante** (auch stehender Falz / Stehfalz genannt) besteht aus einem zylindrischen 90° Bogen und einem ebenen Streifen.

<img alt="" src=images/SheetMetal_AddWall-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-13.png  style="width:200px;"> 
*Zwei gewählte Kanten (edges) → zwei Kanten (flanges)*

Trägt man in einem zweiten Schritt die für die {{PropertyData/de|angle}} ungefähr 180° ein erhält man einen **Falz** anstelle einer Kante.

<img alt="" src=images/SheetMetal_AddWall-14.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-15.png  style="width:200px;"> 
*Zwei gewählte Kanten (edges) → zwei Falze (hems)*



## Anwendung

1.  Eine oder mehrere Randflächen einer Grundplatte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)** drücken.
    -   Den Menüeintrag **Sheet Metal → <img src="images/SheetMetal_AddWall.svg" width=16px> Kante ansetzen** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **Sheet Metal → <img src="images/SheetMetal_AddWall.svg" width=16px> Kante ansetzen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel: **W**.
3.  Das [Aufgaben-Fenster](Task_panel/de.md) **Kantenparameter** wird geöffnet (eingeführt in Version 0.5.00).
4.  Wahlweise die Schaltfläche **Auswählen** drücken, um weitere Kanten hinzuzufügen.
    -   Die Schaltfläche **Vorschau** drücken, um die Auswahl abzuschließen und die Äderungen anzuzeigen.
5.  Wahlweise die Parameter im Aufgaben-Fenster anpassen.
6.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
7.  Ein **Bend**-Objekt wird erstellt, mit einer neuen Kante (Streifen) an jeder ausgewählten Kante (Flächenrand).
8.  Wahlweise die Parameter im [Eigenschafteneditor](Property_editor/de.md) anpassen.



## Hinweise

Um eine Grundplatte zu erzeugen, wird eine geschlossene 2D-Kontur - vorzugsweise eine <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Skizze (sketch)](Sketcher_NewSketch/de.md) - mit dem Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Kante ansetzen](SheetMetal_AddBase/de.md) verwendet.

Alternativ kann eine Grundplatte (Platine) auch mit Befehlen der Arbeitsbereiche <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/de.md) oder <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/de.md) erstellt werden.

Eine Platine mit dem Arbeitsbereich [Part](Part_Workbench/de.md) erstellen:

1.  Einen Festkörper erstellen durch
    -   Anwendung des Befehls <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Würfel (Box)](Part_Box/de.md)
    -   Verwendung des Befehls <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrudieren\...](Part_Extrude/de.md) mit
        -   einem <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rechteck](Draft_Rectangle/de.md).
        -   einem <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Linienzug](Draft_Wire/de.md).
        -   einer <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Skizze](Sketcher_NewSketch/de.md).
2.  Es ist darauf zu achten, dass ein Maß der Box bzw. die Extrusionslänge der Blechstärke entspricht.

Eine Platine mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench.md) erstellen:

1.  Einen Festkörper erstellen durch
    -   Anwendung des Befehls <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Zu addierender Quader (Additive Box)](PartDesign_AdditiveBox/de.md).
    -   Verwendung des Befehls <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Aufpolsterung (Pad)](PartDesign_Pad/de.md) mit einer <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Skizze](Sketcher_NewSketch/de.md).
2.  Es ist darauf zu achten, dass ein Maß des Quaders bzw. die {{PropertyData/de|Length}} des Pads der Blechstärke entspricht.

Wenn mit <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Körper erstellen](PartDesign_Body/de.md) gestartet wird, können SheetMetal-Werkzeuge mit PartDesign-Werkzeugen wie z.B. <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Tasche](PartDesign_Pocket/de.md) oder <img alt="" src=images/PartDesign_Hole.svg  style="width:16px;"> [Bohrung](PartDesign_Hole/de.md) kombiniert werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Bend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Bend Type|Enumeration}}: \"Bend Type\". {{value|Material Outside}} (standard), {{value|Material Inside}}, {{value|Thickness Outside}}, {{value|Offset}}.

-    {{PropertyData/de|Length Spec|Enumeration}}: \"Type of Length Specification\". Art der Längenbestimmung. {{value|Leg}} (standard), {{value|Outer Sharp}}, {{value|Inner Sharp}}, {{value|Tangential}}. {{Version/de|0.21}}

-    {{PropertyData/de|angle|Angle}}: \"Bend Angle\". Biegewinkel. Standardwinkel {{value|90,00°}}.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verknüpfung zur ebenen Fläche, an die eine Kante angesetzt werden soll.

-    {{PropertyData/de|extend1|Distance}}: \"Extend from Left Side\". Verlängern der linken Seite. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|extend2|Distance}}: \"Extend from Right Side\". Verlängern der rechten Seite. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|gap1|Distance}}: \"Gap from Left side\". Lücke von links. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|gap2|Distance}}: \"Gap from Right side\". Lücke von rechts. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|invert|Bool}}: \"Invert Bend Direction\". Biegerichtung umkehren. Standardwert: `False`.

-    {{PropertyData/de|length|Length}}: \"Length of Wall\". Schenkellänge (ab Bogen). Standardwert: {{value|10,00 mm}}.

-    **radius|Length**: \"Bend Radius\". Biegeradius (Innenradius). Der Standardwert hängt von der Eigenschaft radius des Übergeordneten Formelements ab:

    -   Jene Eigenschaft ist nicht vorhanden: Diese Eigenschaft wird auf {{value|1,00 mm}} gesetzt.
    -   Jene Eigenschaft enthält einen numerischen Wert: Ein Ausdruck, der auf jene Eigenschaft verweist, wird in dieser Eigenschaft eingefügt.
    -   Jene Eigenschaft enthält einen Ausdruck: Der Ausdruck wird in diese Eigenschaft kopiert.


{{Properties_Title/de|Parameters Ext.}}

-    {{PropertyData/de|Auto Miter|Bool}}: \"Enable Auto Miter\". Automatische Gehrung aktivieren. Standardwert: `True`.

-    {{PropertyData/de|kfactor|FloatConstraint}}: \"Location of Neutral Line. Caution: Using ANSI standards, not DIN.\". Lage der neutralen Faser nach ANSI-Norm, nicht nach DIN.  Standardwert: {{value|0,50}}. K factor (also known as neutral factor) for the bend. Used to calculate bend allowance when unfolding.

-    {{PropertyData/de|max Extend Dist|Length}}: \"Auto Miter maximum Extend Distance\". Automatische Gehrung, maximale Länge der Erweiterung. Standardwert: {{value|5,00 mm}}.

-    {{PropertyData/de|min Gap|Length}}: \"Auto Miter Minimum Gap\". Automatische Gehrung, minimale Lücke. Standardwert: {{value|0,20 mm}}.

-    {{PropertyData/de|min Relief Gap|Length}}: \"Minimum Gap to Relief Cut\". Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de|offset|Distance}}: \"Offset Bend\". Versatz der Biegung. Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|unfold|Bool}}: \"Shows Unfold View of Current Bend\". Abwicklung des aktuellen Bend-Objekts anzeigen. Standardwert:  `True` erstellt die Abwicklung des Bend-Objekts.


{{Properties_Title/de|Parameters Ex2}}

-    {{PropertyData/de|Sketch|Link}}: \"Sketch Object\". Skizzenobjekt.

-    {{PropertyData/de|sketchflip|Bool}}: \"Flip Sketch Direction\". Skizzenrichtung umkehren. Standardwert: `False`.

-    {{PropertyData/de|sketchinvert|Bool}}: \"Invert Sketch Start\". Standardwert: `False`.


{{Properties_Title/de|Parameters Ex3}}

-    {{PropertyData/de|Length List|FloatList}}: \"Length of Wall List\". Standardwert: {{value|[10.00]}}.

-    {{PropertyData/de|bend AList|FloatList}}: \"Bend Angle List\". Standardwert: {{value|[90.00]}}.


{{Properties_Title|Parameters Miterangle}}

-    {{PropertyData/de|miterangle1|Angle}}: \"Bend Miter Angle from Left Side\". Gehrungswinkel der linken Seite. Standardwinkel: {{value|0,00°}}.

-    {{PropertyData/de|miterangle2|Angle}}: \"Bend Miter Angle from Right Side\". Gehrungswinkel der rechten Seite. Standardwinkel: {{value|0,00°}}.


{{Properties_Title|Parameters Perforation}}

-    {{PropertyData/de|Nonperforation Max Length|Length}}: \"Non-Perforation Max Length\" (Maximale Länge ohne Perforation). Standardwert {{value|5 mm}}.

-    {{PropertyData/de|Perforate|Bool}}: \"Enable perforation\" (Perforation aktivieren). Standardwert `False`.

-    {{PropertyData/de|Perforation Angle|Angle}}: \"Perforation Angle\" (Perforationswinkel). Standardwert {{value|0 °}}.

-    {{PropertyData/de|Perforation initial Length|Length}}: \"Initial Perforation Length\" (Anfängliche Länge der Perforation). Standardwert {{value|5 mm}}.

-    {{PropertyData/de|Perforation Max Length|Length}}: \"Perforation Max Length\" (Maximale Länge der Perforation). Standardwert {{value|5 mm}}.


{{Properties_Title/de|Parameters Relief}}

-    {{PropertyData/de|Relief Factor|Float}}: \"Relief Factor\". Standardwert: {{value|0,70}}.

-    {{PropertyData/de|Use Relief Factor|Bool}}: \"Use Relief Factor\". Standardwert: `False`.

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

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
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



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddWall/de
