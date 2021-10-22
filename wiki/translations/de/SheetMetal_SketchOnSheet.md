---
- GuiCommand:/de
   Name:SheetMetal SketchOnSheet
   Name/de:SheetMetal SkizzeAufBlech
   MenuLocation:SheetMetal → Sketch On Sheet metal
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**M** **S**
---

# SheetMetal SketchOnSheet/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> _ verwendet.

Im Gegensatz zu dem Befehl <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Tasche](PartDesign_Pocket/de.md), wo Löcher entlang der Skizzennormalen (lokale Z-Achse) ausgeschnitten werden, verhält sich dieses Werkzeug, als ob es das Blechobjekt abwickeln, die Löcher ausschneiden und letztlich die Abwicklung rückgängig machen würde.

## Anwendung

1.  Eine **planare Fläche** auswählen
2.  Eine komplanare <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) (d.h. eine auf derselben Ebenen liegende) als **Lochbild** auswählen (vorzugsweise aus der [Baumansicht](Tree_view/de.md)).
    -   **Hinweis:** Nicht die Taste **Steuerung**/**Befehl** vergessen!
3.  Den Befehl <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md)
**
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_SketchOnSheet.svg" width=16px> Sketch On Sheet metal
**
    -   Das Tastenkürzel: **M** dann **S**

## Hinweis

-   Die Skizze kann mehr als nur eine Kontur enthalten.
-   Jede Kontur muss die ebene Fläche wenigstens berühren, andernfalls würde sie gar kein Loch ausschneiden.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-SketchOnSheet-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Sketch|Link}}: \"Sketch on Sheetmetal\". Verknüpfung zum Lochbild bzw. zur Ausschnittskizze.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verknüpfung zur ebenen Fläche, auf der der Ausschnitt beginnt.

-    {{PropertyData/de|kfactor|FloatConstraint}}: \"\--wrong naming in english original!\--\". Standardwert: {{value|0,50}}.

## Beispiel

<img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:300px;"> 
*Ein einfaches Dingens*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Vorbereitung

Dieses Dingens besteht aus einem Blechprofil mit hinzugefügten Löchern.  Es müssen also eine Skizze für das Blech und eine für das Lochbild vorbereitet werden.  Eine gerade Linie der ersten Skizze muss komplanar zu der anderen Skizzenebene sein,  dies ergibt die Fläche und die komplanare Skizze, die in den weiteren Schritten benutzt werden.

<img alt="" src=images/SheetMetal_SketchOnSheet-01.png  style="width:200px;"> 
*Nur eine Kontur und ein Lochbild*

## Arbeitsablauf

1.  Ein gekantetes Blechobjekt erstellen
    1.  Die Skizze für die **Kontur** auswählen  <img alt="" src=images/SheetMetal_SketchOnSheet-02.png  style="width:240px;">
    2.  Die Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_SketchOnSheet-03.png  style="width:240px;">  
2.  Ein paar Löcher ausschneiden
    1.  Die **ebene Fläche** auswählen
    2.  Die Skizze mit dem **Lochbild** auswählen  <img alt="" src=images/SheetMetal_SketchOnSheet-04.png  style="width:240px;">
    3.  Die Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:240px;">   Fertig!  
3.  Einige Hinweise
    1.  Man sollte prüfen, ob die Materialstärke des gekanteten Objekts in die richtige Richtung aufgebaut wurde.  <img alt="" src=images/SheetMetal_SketchOnSheet-06.png  style="width:240px;">   Die gelbe Kontur sollte auf der oberen Fläche der Bodenkante liegen (wie dargestellt).  Um die Richtung umzukehren, muss der Wert der Eigenschaft **Bend Side** geändert werden (Outside \<-\> Inside).  
    2.  **Lochkonturen**, die die verwendete ebene Fläche nicht berühren werden keine Löcher in das gekantete Objekt schneiden.  <img alt="" src=images/SheetMetal_SketchOnSheet-07.png  style="width:240px;">  Das untere Rechteck berührt die besagte Fläche gerade eben noch und erzeugt einen Ausschnitt, während die obere Langlochkontur dieses nicht macht.


</div>


</div>




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal SketchOnSheet/de
