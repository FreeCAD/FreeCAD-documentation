---
- GuiCommand:/de
   Name:SheetMetal AddFoldWall
   Name/de:SheetMetal Abkanten
   MenuLocation:SheetMetal → Fold a Wall
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**C** **F**
---

# SheetMetal AddFoldWall/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> [Abkanten](SheetMetal_AddFoldWall/de.md) kantet eine Blechplatte (Platine) entlang einer gewählten Linie mit einem vorgegebenen Radius ab.

Er kann mit einer zuvor zugeschnittenen Platine verwendet werden, um

-   eine perforierte Biegezone zu erzeugen.
-   ebene Abschnitte innerhalb der Biegezone und darüber hinausgehend zu erzeugen wie z.B. Zapfen oder Laschen. (erfordert Lücken in der Biegelinie)

<img alt="" src=images/SheetMetal_AddFoldWall-13.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*Vorab beschnittene Platine und Biegelinie mit zwei Lücken → perforierte Biegezone mit einigen weiterhin ebenen Geometrien*

## Anwendung

1.  Die Fläche auswählen, die abgekantet werden soll.
2.  Die **Ctrl**-Taste (bzw. die**Command** Taste für macOS) drücken und halten.
3.  Eine komplanare <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) auswählen (d.h. eine auf derselben Ebene liegende) für die (Abschnitte der) **Biegelinie** (vorzugsweise aus der [Baumansich](Tree_view/de.md)).
4.  Die **Ctrl**-Taste (bzw. die**Command** Taste für macOS) loslassen.
5.  Den Befehl <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> **SheetMetal Abkanten** aktivieren durch
    -   Die Schaltfläche **<img src="images/SheetMetal_AddFoldWall.svg" width=16px> [Abkanten](SheetMetal_AddFoldWall/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_AddFoldWall.svg" width=16px> Abkanten** menu option.
    -   Das Tastenkürzel: **C** dann **F**.
6.  Den Wert der Eigenschaft {{PropertyData/de|Position}} verändern, um die Lage der Biegung im Bezug auf die Biegelinie einzustellen.

<img alt="" src=images/SheetMetal_AddFoldWall-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*Biegelinie(n) in der Mitter der Perforation liegend → Damit die Biegung gleichfalls zentriert bleibt, muss die {{PropertyData/de|Position* auf {{value|middle}} gesetzt werden}}

### Hinweise

-   Die Biegelinienskizze muss **komplanar** zu der ausgewählten Fläche sein.

-   Die Biegelinienabschnitte müssen zueinander kollinear sein.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Fold-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Bend Line|Link}}: \"Bend Reference Line List\". Verknüpfung zu den Biegelinienobjekten.

-    {{PropertyData/de|Position|Enumeration}}: \"Bend Line Position\". Lage der Biegelinie. {{value|forward}} (standard), {{value|middle}}, {{value|backward}}.

-    {{PropertyData/de|angle|Angle}}: \"Bend Angle\". Biegewinkel. Standardwinkel: {{value|90,00°}}.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Basisobjekt. Verknüpfung zu der ebenen Fläche, die gekantet wird.

-    {{PropertyData/de|invert|Bool}}: \"Invert Bend Direction\". Biegerichtung umkehren. Standardwert: `False`

-    {{PropertyData/de|invertbend|Bool}}: \"Invert Solid Bend Direction\". Abzukantende Seite wechseln. Standardwert:  `True` tauscht die Seite neben der Biegelinie, die gekantet wird.

-    {{PropertyData/de|kfactor|FloatConstraint}}: \"Neutral Axis Position\". Lage der neutralen Faser. Standardwert: {{value|0,50}}.

-    {{PropertyData/de|radius|Length}}: \"Bend Radius\". Biegeradius. Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de|unfold|Bool}}: \"Unfold Bend\". Abwickeln. Standardwert: `False`

## Beispiel

<img alt="" src=images/SheetMetal_AddFoldWall-01.png  style="width:300px;"> 
*Ein einfacher Klipp*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Vorbereitung

Dieser Klipp wird aus einer Platine hergestellt, die dreimal abgekantet wird, d.h. es müssen vier Skizzen vorbereitet werden:

:   \- Eine für den Platinenzuschnitt
:   \- Eine für die Kantung an der Vorderkante
:   \- Eine für die Kantung nach oben
:   \- Eine für die Kantung nach unten

Der einfachste Weg, um sicherzustellen, dass eine Fläche der Platine (Rohling) und alle Biegelinien komplanar sind, ist das Erstellen aller Skizzen auf derselben Ebene - der X-Y-Ebene in diesem Falle.

Die Biegelinien könnten mit einem anderen Werkzeug erstellt werden, aber hey, wir haben einen <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench.md)!

<img alt="" src=images/SheetMetal_AddFoldWall-21.png  style="width:280px;"> <img alt="" src=images/SheetMetal_AddFoldWall-20.png  style="width:200px;"> 
*Skizzen auf ihrer gemeinsamen Ebene und ihre Darstellung im Konstruktionsbaum*

## Arbeitsablauf

1.  Eine Platine erzeugen
    1.  Die Skizze für den Platinenzuschnitt auswählen
    2.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-02.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-03.png  style="width:280px;"> 
2.  Abkanten der Vorderkante
    1.  **Unterseite** der Platine auswählen
    2.  Die **Skizze** namens ***Tip Fold line*** auswählen (vorzugsweise aus der Baumansicht)  (und nicht die Steuerung- bzw. Befehlstaste vergessen)
    3.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-10.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-04.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-05.png  style="width:280px;">
    4.  Die Kante sollte 90° nach unten zeigen, d.h. einige werte des Eigenschaftenfensters müssen geändert werden z.B.:  - Der Wert des *Biegewinkels* **angle** auf 60°  - Der Wert für *Biegerichtung umkehren* **invert** auf true für eine Kantung nach oben  
3.  Abkanten nach unten
    1.  **Unterseite** der Platine auswählen
    2.  Die **Skizze** namens ***Down-Fold line*** auswählen (vorzugsweise aus der Baumansicht)
    3.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-11.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-06.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-07.png  style="width:280px;">
    4.  Den Wert des *Biegewinkels* **angle** auf 92° setzen
    5.  Wenn die falsche Seite des Teiles bewegt wurde, den Wert für *Abzukantende Seite wechseln* **invertbend** auf true setzen  
4.  Abkanten nach oben
    1.  **Unterseite** der Platine auswählen
    2.  Die **Skizze** namens ***Up-Fold line*** auswählen (vorzugsweise aus der Baumansicht)
    3.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-12.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-08.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-09.png  style="width:280px;">
    4.  Den Wert des *Biegewinkels* **angle** auf 80° setzen
    5.  Wenn die Kantung nach unten ausgeführt wurde, Wert für *Biegerichtung umkehren* **invert** auf true setzen
    6.  Falls nötig, den Wert für *Abzukantende Seite wechseln* **invertbend** auf true setzen  

Fertig!

Achtung!: Im wirklichen Leben muss die Kantung nach oben vor der Kantung nach unten erfolgen. Nur die virtuelle CAD-Welt erlaubt es, durch feste Werkstoffe hindurch zu biegen. Auf diesem Weg ändert sich die Lage des feststehenden Bereiches nicht.  Alle Skizzen liegen auf derselben Ebene, um Skizzen, die bewegten Flächen zugeordnet sind, zu vermeiden.


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddFoldWall/de
