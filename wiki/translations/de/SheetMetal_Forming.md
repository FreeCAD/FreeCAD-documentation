---
- GuiCommand:/de
   Name:SheetMetal Forming
   Name/de:SheetMetal Prägen 
   MenuLocation:SheetMetal → Make Forming in Wall
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**M** **F**
---

# SheetMetal Forming/de

## Beschreibung

DerBefehl <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> **Prägen** erstellt ein geprägtes Formelement in einer Blechfläche und verwendet dafür ein separates Festkörperobjekt .

Die rückseitige ebene Fläche des formgebenden Festkörpers und die zu prägenden Fläche werden benutzt, um die geprägte Form zu platzieren und auszurichten, d.h. ihre lokalen Koordinatensysteme haben standardmäßig den gleichen Ursprung und die gleiche Ausrichtung.  Der Winkel um die Z-Achse und der Versatz in X-, Y- und Z-Richtung lassen sich durch ändern der Parameterwerte im [Eigenschafteneditor](Property_editor/de.md) einstellen.

Eine Skizze kann hinzugefügt werden, um das eingeprägte Formelement zu vervielfältigen und in regelmäßigen oder unregelmäßigen Mustern einzufügen (unter Verwendung der Mittelpunkte von Kreisen oder Kreisbögen)

Eine kleine Auswahl von Objekten, die erstellt werden können:

<img alt="" src=images/SheetMetal_Forming-08.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-09.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-10.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-11.png  style="width:200px;"> 
*Durchprägungen, Kiemen, Durchzüge, Stege*

## Anwendung

### Durchprägung

1.  Eine Fläche des SheetMetal-Objekts auswählen, die geprägt (durchgesetzt) werden soll
2.  Die **Unterseite** (Rückseite) des formgebenden Festkörpers auswählen
    -   **Hinweis:** Nicht die Taste **Steuerung**/**Befehl** vergessen!
3.  Den Befehl <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Prägen](SheetMetal_Forming/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/SheetMetal_Forming.svg" width=16px> [Prägen](SheetMetal_Forming/de.md)
**
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_Forming.svg" width=16px> Prägen
**
    -   Das Tastenkürzel: **M** dann **F**

### Kiemen

1.  Eine Fläche des SheetMetal-Objekts auswählen, die geprägt (durchgesetzt) werden soll
2.  Die **Unterseite** (Rückseite) des formgebenden Festkörpers auswählen
3.  Eine **Seitenfläche**, die an die Unterseite angrenzt auswählen, um den Bereich zu markieren, der aufgeschnitten werden soll
    -   **Hinweis:** Nicht die Taste **Steuerung**/**Befehl** vergessen!
4.  Den Befehl <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Prägen](SheetMetal_Forming/de.md) aktivieren (siehe oben):

### Steg

1.  Eine Fläche des SheetMetal-Objekts auswählen, die geprägt (durchgesetzt) werden soll
2.  Die **Unterseite** (Rückseite) des formgebenden Festkörpers auswählen
3.  Eine **Seitenfläche**, die an die Unterseite angrenzt, auswählen, um den Bereich zu markieren, der aufgeschnitten werden soll
4.  Die gegenüberliegende **Seitenfläche**, die an die Unterseite angrenzt, auswählen, um den anderen Bereich zu markieren, der aufgeschnitten werden soll
    -   **Hinweis:** Nicht die Taste **Steuerung**/**Befehl** vergessen!
5.  Den Befehl <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Prägen](SheetMetal_Forming/de.md) aktivieren (siehe oben):

### Durchzug

1.  Eine Fläche des SheetMetal-Objekts auswählen, die geprägt und gestanzt werden soll
2.  Die **Unterseite** (Rückseite) des formgebenden Festkörpers auswählen
3.  Die der Unterseite gegenüberliegende **Oberseite** auswählen, um den Bereich zu markieren, der ausgestanzt werden soll
    -   **Hinweis:** Nicht die Taste **Steuerung**/**Befehl** vergessen!
4.  Den Befehl <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Prägen](SheetMetal_Forming/de.md) aktivieren (siehe oben):

### Verfvielfältigen und Anordnen 

Um das geprägte Formelement zu vervielfältigen und nach einem Muster anzuordnen, kann eine **Skizze**, die Kreise und Bögen enthält, zu der Eigenschaft {{PropertyData/de|Sketch}} des *WallForming*\'-Objekts hinzugefügt werden.

Die Mittelpunkte der Kreise und Bögen werden verwendet, um Positionen vorzugeben, an denen Instanzen der geprägten Formelemente eingesetzt werden; sie haben keinen Einfluss auf die Ausrichtung der Instanzen.

Die Ausrichtung hängt weiterhin von der Ausrichtung der zuerst ausgewählten Fläche ab.

### Ausrundungen hinzufügen 

1.  Zur Arbeitsumgebung <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/de.md) wechseln
2.  Eine Kante auf der Oberseite des SheetMetal-Objekts auswählen, die verrundet werden soll
3.  Den Befehl <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Verrundung](PartDesign_Fillet/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/PartDesign_Fillet.svg" width=16px> [ Verrundung](PartDesign_Fillet/de.md)
**
    -   Den Menüeintrag {{MenuCommand/de|Teile-Konstruktion → Modifikationen → <img src="images/PartDesign_Fillet.svg" width=16px> Verrundung}}
4.  Die Eigenschaft des Fillet-Objekts  (Dies ist einigermaßen **wichtig** für die nächste Verrundung)
5.  Eine Kante auf der Unterseite des SheetMetal-Objekts auswählen, die verrundet werden soll
6.  Den Befehl <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Verrundung](PartDesign_Fillet/de.md) aktivieren (siehe oben)

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-WallForming-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Suppress Feature|Bool}}: \"Suppress Forming Feature\". Prägung unterdrücken. Standardwert ist `False`.

-    {{PropertyData/de|angle|Angle}}: \"Tool Position Angle\". Winkel des formgebenden Werkzeugs. Standardwinkel: {{value|0,00°}}.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verknüpfung zu der ebenen Fläche, die geprägt werden soll.

-    {{PropertyData/de|offset|VectorDistance}}: \"Offset from Center of Face\". Abstand vom Flächenzentrum. Standard: {{value|[0,00 mm, 0,00 mm, 0,00 mm]}}.

-    {{PropertyData/de|thickness|Distance}}: \"Thickness of Sheetmetal\". Dicke des {{PropertyData/de|Base Feature||hidden}}.

-    {{PropertyData/de|tool Object|LinkSub}}: \"Forming Tool Object\". Verknüpfung zu der ebenen Fläche, die verwendet wird, um das formgebende Werkzeug zu positionieren.


{{Properties_Title/de|Parameters1}}

-    **Sketch|Link**: \"Point Sketch on Sheetmetal\". Verknüpfung zu der Skizze, die die Informationen enthält, wie die Instanzen des formgebenden Werkzeugs vervielfältigt und verteilt werden. (Die Mittelpunkte von Kreisen und Bögen werden verwendet, um die Instanzen zu erstellen und zu positionieren)

## Beispiel

<img alt="" src=images/SheetMetal_Forming-01.png  style="width:300px;"> <img alt="" src=images/SheetMetal_Forming-02.png  style="width:300px;"> 
*Eine sechsseitige Schale mit geprägtem Mittelteil*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Vorbereitung

Diese Schale besteht aus einem gekanteten Blechobjekt und einem durchgeprägten Formelement; beide müssen schon fertig vorbereitet sein.

Es ist hier nicht nötig mit komplanaren Skizzen zu arbeiten.

<img alt="" src=images/SheetMetal_Forming-03.png  style="width:200px;"> 
*Blechschale und prägendes Objekt*

## Arbeitsablauf

1.  Die Fläche des SheetMetal-Objekts auswählen, die eingeprägt werden soll
2.  Die **Rückseite** des formgebenden Objekts auswählen  (Nicht die Taste <img alt="" src=images/SheetMetal_Forming-04.png  style="width:240px;">
3.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_Forming-05.png  style="width:240px;">
4.  Die scharfen Kanten verrunden:
    -   Die Schale umdrehen und eine oder mehrere Kanten für die kleineren Innenradien auswählen
    -   Schaltfläche <img alt="" src=images/SheetMetal_Forming-12.png  style="width:240px;"> **\--\>** <img alt="" src=images/SheetMetal_Forming-02.png  style="width:240px;">
    -   Die Schale wieder umdrehen und eine oder mehrere Kanten für die größeren Außenradien auswählen
    -   Schaltfläche <img alt="" src=images/SheetMetal_Forming-13.png  style="width:240px;"> **\--\>** <img alt="" src=images/SheetMetal_Forming-01.png  style="width:240px;">   Fertig!  
5.  Ausrichtung und Position verändern (sollte vor dem Verrunden erfolgen)
    -   Aktivieren des <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> WallForming-Objekts im [Konstruktionsbaum](Tree_view/de.md)
    -   Den Wert der  <img alt="" src=images/SheetMetal_Forming-14.png  style="width:240px;">
    -   Den Wert der  <img alt="" src=images/SheetMetal_Forming-06.png  style="width:240px;">  Hier sieht man deutlich, dass es nicht sinnvoll ist, die geprägte Geometrie in eine Bereich außerhalb der gewählte Fläche zu verschieben.  
    -   Den Wert der  <img alt="" src=images/SheetMetal_Forming-07.png  style="width:240px;">  Wenigstens stürzt FreeCAD nicht ab, wenn ein Teil aus zwei einzelnen Körpern besteht\...  
6.  Einige Hinweise
    1.  Die Höhe des formgebenden Festkörpers bestimmt die Tiefe der geprägten Form.  Das heißt, dass das Ändern des Parameters **offset, z** nicht das gewünschte Ergebnis bringt.
    2.  Die geprägte Geometrie ist ein Schalenobjekt, d.h. sie hat eine konstante Wandstärke.  Und deshalb muss die Oberfläche des formgebenden Körper aufdickbar sein, andernfalls wird das Werkzeug keine Prägung erzeugen können.
    3.  Wenn die Außenkanten zuerst verrundet werden, kann das Objekt in in mehrere Teile aufgetrennt werden, wenn die Radien zu groß eingestellt wurden.


</div>


</div>




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Forming/de
