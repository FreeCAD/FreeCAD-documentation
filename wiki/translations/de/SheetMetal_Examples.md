# SheetMetal Examples/de
{{TOCright}}

## Einführung

Der Arbeitsbereich Blech (SheetMetal) ist ziemlich mächtig geworden und verlangt jetzt nach einer angemessenen Dokumentation.

Um die Überfüllung der Werkzeugseiten zu vermeiden, wurde diese Seite angelegt, um Teile zu sammeln, die die speziellen Blechfunktionen darstellen und erklären.

Geplante Phasen um Inhalte zu erstellen   *

1.  Bilder sammeln
2.  Beschreibungen der Arbeitsabläufe hinzufügen
3.  Detailliertere Anleitungen erstellen

## Scharnier

<img alt="" src=images/SheetMetal_Example-01.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width   *200px;"> 
*Arbeitsablauf Scharnier   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Bohrung](PartDesign_Hole/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Scharnier Schritt für Schritt 


<div class="mw-collapsible-content toccolours">

1.  Ein Profil erstellen (eine Linie und einen tangential anschließenden Bogen), vorzugsweise mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher](Sketcher_Workbench/de.md).
2.  Den Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *16px;"> [BasisprofilErstellen](SheetMetal_AddBase/de.md) aktivieren, um ein BaseBend-Objekt zu erstellen.
3.  Die Parameter des BaseBend-Objekts editieren   *
    -   Die {{PropertyData/de|Mid Plane}} auf `True` setzen, damit das Profil symmetrisch auf beiden Seiten der Skizzenebene aufgebaut wird.
    -   Der {{PropertyData/de|radius}} und der {{PropertyData/de|thickness}} gibt man Werte nach eigener Wahl.
4.  Erstellen einer Beschnittkontur mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher](Sketcher_Workbench/de.md).
5.  Mit dem Befehl <img alt="" src=images/PartDesign_Pocket.svg  style="width   *16px;"> [PartDesign Tasche](PartDesign_Pocket/de.md) entfernt man eine Hälfte des runden Bereichs.
6.  Ein Lochbild mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher](Sketcher_Workbench/de.md) erstellen.
7.  Den Befehl <img alt="" src=images/PartDesign_Hole.svg  style="width   *16px;"> [PartDesign Bohrung](PartDesign_Hole/de.md) aktivieren. Die Optionen countersink (Kegelsenkung) und counterbore (Plan-/Zylindersenkung) sollte man vermeiden, damit das Objekt abwickelbar bleibt.
8.  Mit dem Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erstellt man ein Unfold-Objekt (Abwicklungskörper).
9.  Fertig!


</div>


</div>

## Aktenklammer

<img alt="" src=images/SheetMetal_Example-02.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width   *200px;"> 
*Arbeitsablauf Aktenklammer   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md)**,
klonen, umdrehen und vereinigen,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Aktenklammer Schritt für Schritt 


<div class="mw-collapsible-content toccolours">

1.  Ein Profil erstellen, vorzugsweise mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher](Sketcher_Workbench/de.md) auf der XZ-Ebene.
    <img alt="Profile sketch" src=images/SheetMetal_Example-02e.png  style="width   *300px;">
2.  Den Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *16px;"> [BasisprofilErstellen](SheetMetal_AddBase/de.md) aktivieren, um ein BaseBend-Objekt zu erstellen.
3.  Die Parameter des BaseBend-Objekts im Eigenschafteneditor anpassen   *
    <img alt="BaseBend-Objekt und hervorgehobene Skizze" src=images/SheetMetal_Example-02f.png  style="width   *200px;">
    -   Die {{PropertyData/de|Mid Plane}} auf `True` setzen, damit das Profil symmetrisch auf beiden Seiten der Skizzenebene aufgebaut wird.
    -   Die {{PropertyData/de|length}} auf 32 mm setzen.
    -   Die {{PropertyData/de|radius}} auf 2 mm setzen.
    -   Die {{PropertyData/de|thickness}} auf 0.3 mm setzen.
4.  Auswahl der Fläche zwischen den Runden Abschnitten und Aktivieren des <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketchers](Sketcher_Workbench.md).
    <img alt="Basisfläche der Skizze" src=images/SheetMetal_Example-02g.png  style="width   *200px;">
5.  Den aufgewickelten Teil blendet man mit dem Befehl <img alt="" src=images/Sketcher_ViewSection.svg  style="width   *16px;"> [Sketcher SchnittAnzeigen](Sketcher_ViewSection/de.md) aus.
6.  Ausschnittkontur erstellen.
    <img alt="Ausschnittkontur" src=images/SheetMetal_Example-02h.png  style="width   *" height="240px;"> <img alt="Die Ausschnittkontur überlappt die ausgewählte Fläche leicht" src=images/SheetMetal_Example-02i.png  style="width   *" height="240px;">
7.  Die Skizze abschließen mit dem Befehl <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width   *16px;"> [Sketcher SkizzeVerlassen](Sketcher_LeaveSketch/de.md).
8.  Die Fläche erneut auswählen und die Ausschnittskizze zur Auswahl hinzufügen.
    <img alt="Fläche und Skizze ausgewählt" src=images/SheetMetal_Example-02j.png  style="width   *200px;">
9.  Den Befehl <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width   *16px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md) aktivieren, um den aufgewickelten Teil (entlang seiner Oberfläche) auszuschneiden.
    <img alt="Fertige erste Hälfte" src=images/SheetMetal_Example-02b.png  style="width   *200px;">
10. Eine Seite ist nun fertig. Jetzt muss noch eine Möglichkeit zum Spiegeln des Objekts gefunden werden.

**Mögliche Spiegelungsoptionen   ***

-   Der Befehl <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *16px;"> [PartDesign Spiegeln](PartDesign_Mirrored/de.md) versagt, da er aus irgendwelchen Gründen nicht mit SheetMetal-Objekten umgehen kann. So geht es also nicht.
-   Der Befehl <img alt="" src=images/Part_Mirror.svg  style="width   *16px;"> [Part Spiegeln](Part_Mirror/de.md) erzeugt ein gespiegeltes Teil, aber dieses ist nicht mehr abwickelbar. So geht es also auch nicht.
-   Ein Weg der funktionieren kann ist die Verwendung eines Klones. Dieser kann zwar nicht gespiegelt werden, aber auf ihn kann Achsensymmetrie angewendet werden (Drehung um 180°).
-   Ein anderer funktionierender Weg ist die Verwendung eines Link-Objekts.

**Spiegeln mit einem Klon   ***

1.  Das Body-Objekt in der Baumansicht auswählen.
2.  Den Befehl <img alt="" src=images/PartDesign_Clone.svg  style="width   *16px;"> [PartDesign Klon](PartDesign_Clone/de.md) aktivieren. er fügt ein neues Body-Objekt hinzu, das ein Clone-Objekt enthält.
    Für eine 180°-Drehung setzt man die {{PropertyData/de|Winkel}} unter der Eigenschaft Placement des Körpers oder des Klons auf 180°. (Die Z-Achse ist standardmäßig voreingestellt und sollte funktionieren, wenn man, wie beschieben, auf der XZ-Ebene gestartet ist).
    <img alt="Geklonte Hälfte" src=images/SheetMetal_Example-02b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="Gedrehte geklonte Hälfte" src=images/SheetMetal_Example-02l.png  style="width   *200px;">
3.  Mit dem immer noch aktiven Körper nutzt man den Befehl <img alt="" src=images/PartDesign_Boolean.svg  style="width   *16px;"> [PartDesign BoolescheOperation](PartDesign_Boolean/de.md), um den Körper des Klons hinzuzufügen und beide Hälften zu vereinigen.
    <img alt="Vereinigte Hälften" src=images/SheetMetal_Example-02c.png  style="width   *200px;">
4.  Mit dem Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erstellt man ein Unfold-Objekt.
    <img alt="Klammer und Abwicklung" src=images/SheetMetal_Example-02m.png  style="width   *200px;"> <img alt="Abwicklung (Unfold-Objekt)" src=images/SheetMetal_Example-02d.png  style="width   *200px;">
5.  Fertig!

**Spiegeln mit einem Link-Objekt   ***

1.  Das Body-Objekt in der Baumansicht auswählen.
2.  Den Befehl <img alt="" src=images/Std_LinkMake.svg  style="width   *16px;"> [Std VerknüpfungErstellen](Std_LinkMake/de.md) aktivieren. Er fügt ein neues Link-Objekt hinzu.
3.  Das Link-Objekt dupliziert man durch setzen der {{PropertyData/de|Element Count}} auf 2.
4.  Für eine 180°-Drehung setzt man die {{PropertyData/de|Winkel}} unter der Eigenschaft Placement eines der beiden unterverlinkten Objekte auf 180°. (Die Z-Achse ist standardmäßig voreingestellt und sollte funktionieren, wenn man, wie beschieben, auf der XZ-Ebene gestartet ist).
5.  Beide unterverlinkten Objekte in der Baumansicht auswählen.
6.  Den Befehl <img alt="" src=images/Part_Fuse.svg  style="width   *16px;"> [Part Vereinigung](Part_Fuse/de.md) aktivieren, um beide Hälften zu vereinigen.
    <img alt="Vereinigte Hälften" src=images/SheetMetal_Example-02c.png  style="width   *200px;">
7.  Mit dem Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erstellt man ein Unfold-Objekt.
    <img alt="Klammer und Abwicklung" src=images/SheetMetal_Example-02m.png  style="width   *200px;"> <img alt="Abwicklung (Unfold-Objekt)" src=images/SheetMetal_Example-02d.png  style="width   *200px;">
8.  Fertig!


</div>


</div>

## Schelle

<img alt="" src=images/SheetMetal_Example-03.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width   *200px;"> 
*Arbeitsablauf Schelle   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Bohrung](PartDesign_Hole/de.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Verrundung](PartDesign_Fillet/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

## Sechsseitige Schale 

<img alt="" src=images/SheetMetal_Example-04.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width   *200px;"> 
*Workflow Hex Bowl   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width   *200px;">

Wenn eine Eckentlastung hinzugefügt wurde (rechte Seite), kann es nötig sein den wert der Eigenschaft **Size** anzupassen.

## Bleistiftklipp

<img alt="" src=images/SheetMetal_Example-05.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width   *200px;"> 
*Arbeitsablauf Bleistiftklipp   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

## Beispiel zu Fläche erweitern 

<img alt="" src=images/SheetMetal_Example-06.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width   *200px;"> 
*Arbeitsablauf Beispiel zu Fläche erweitern   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

Für die zweite Anwendung von **Fläche erweitern** wird eine Skizze mit zwei Konturen für die Form der Erweiterung(en) verwendet; und mit dem Setzen des Wertes von \"use subtraction\" auf true liefert sie auch die Form der Ausschnitte.

## USB-Massekontakt 

<img alt="" src=images/SheetMetal_Example-07.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width   *200px;"> 
*Arbeitsablauf USB-Massekontakt   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

(Die Zugentlastung ist nur eine künstlerische Darstellung von dem, was in einem echten Stecker versteckt sein kann)

## SheetMetal Eigenschaften 

Dieser Abschnitt versucht die Eigenschaften jedes SheetMetal-Objekts, wo es möglich ist, mit einfachen Bildern zu erklären.


<div class="mw-collapsible mw-collapsed">

### BaseBend-Objekt <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

<img alt="" src=images/SheetMetal_Example-08a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08b.png  style="width   *200px;">



*Ausgewählte Skizze + 
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)* 
→ BaseBend-Objekt mit Standardeinstellungen**

<img alt="" src=images/SheetMetal_Example-08b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08c.png  style="width   *200px;">



*{{PropertyData/de|length* bearbeiten   * Standardlänge → Reduzierte Länge}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08h.png  style="width   *200px;">



*{{PropertyData/de|Mid Plane* von {{False}} auf `True` umschalten   * Extrusion in eine Richtung → Symmetrische Extrusion}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;">



*{{PropertyData/de|Reverse* von {{False}} auf `True` umschalten   * Standardrichtung → Umgekehrte Richtung}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08f.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08g.png  style="width   *200px;">



*{{PropertyData/de|Bend Side* auswählen   * {{value|Outside}} (Standard) → {{value|Inside}} → {{value| Middle}}}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08i.png  style="width   *200px;">



*{{PropertyData/de|radius* bearbeiten   * Standardradius → Vergrößerter Radius.<br>
Diese Eigenschaft entspricht dem Innenradius der Bögen, die an Knotenpunkten erstellt werden, an denen der Übergang zweier Kanten in der Skizze nicht tangential ist.}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08j.png  style="width   *200px;">



*{{PropertyData/de|thickness* bearbeiten   * Standardwandstärke → Vergrößerte Wandstärke}}


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Bend object <img alt="" src=images/SheetMetal_AddWall.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

A Bend object consists of sets of one cylindrical bend and one planar strip each. Each pair extends from a selected edge of a blank.

<img alt="" src=images/SheetMetal_Example-09a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09b.png  style="width   *200px;">



*Selected edges + 
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)* 
→ Bend objects with default settings <br>
(Two Bend objects in two separate bodies.)**

Edit **radius** to vary the inner radius of all bends supplied by a Bend object. (See BaseBend object above)

Edit **length** to vary the length of all planar strips extending from the bends of a Bend object.

   *   Don\'t confuse the **length** with a flange length which is the sum of this length, radius, and thickness (90° only).

<img alt="" src=images/SheetMetal_Example-09b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;">



*Switch **invert* from {{FALSE** to `True`   *Default flanges (Bend objects) → Inverted flanges}}

<img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09e.png  style="width   *200px;">



*Edit **angle*   *Default angle (90°) → Enlarged angle → Decreased angle**

We don\'t have to care about trimming the edges, because **Auto Miter** is activated by default.
If deactivated, the result would look like this   *

<img alt="" src=images/SheetMetal_Example-09m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09f.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09g.png  style="width   *200px;">



*Switch **Auto Miter* from {{TRUE** to `False`   * Default angle (90°) → Enlarged angle → Decreased angle<br>
(Auto Miter has no effect on single flanges)}}

To manually miter a flange edge **miterangle1** and **miterangle2** are used   *

<img alt="" src=images/SheetMetal_Example-09m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09n.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09o.png  style="width   *200px;">



*Edit **miterangle1* and {{PropertyData|miterangle2**   * No miter (default) → Differently mitered edges, positive angle → Symmetrically mitered edges, negative angles}}

Mitering only effects the planar strips, not the bends.

   *   (It takes the whole edge into account and so cannot be used to chamfer flange edges)

To display the different choices of **Bend Type** we introduce an auxiliary cuboid that extrudes from the same outline as the blank and has the same height as the Bend object (its flange length).

<img alt="" src=images/SheetMetal_Example-09h.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09i.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09j.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09k.png  style="width   *200px;">



*Select **Bend Type*   * {{value|Material Outside** (default) → {{value|Material Inside}} → {{value|Thickness Outside}} → {{value|Offset}}}}

-   Outside   * The bend starts at the selected edge (The whole Bend object lies outside the cuboid).
-   Inside   * The outer side of the bend ends on the cuboid surface (The whole Bend object lies inside the cuboid).
-   Thickness Outside   * The inner side of the bend ends on the cuboid surface (only the planar strip is protruding from the cuboid surface).
-   Offset   * According to the value of **offset** the bend is moved in outward direction from its default position.

   *   An extension is inserted for positive values (high-lighted strip).
   *   Negative values are allowed to move the bend inwards.

If we don\'t want to use the whole length of an edge we can use **gap1** and **gap2**.

<img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09l.png  style="width   *200px;">



*Edit **gap1* and {{PropertyData|gap2**   * Default flanges → Flanges with different values for gap1 and gap2}}

If the length of a gap reaches or extends the value of **min Relief Gap**, a relief will be added to the gap.
Reliefs are controlled by **relief Type**, **reliefd** (relief depth), and **reliefw** (relief width) which are enabled only when a gap value is set.

<img alt="" src=images/SheetMetal_Example-09p.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09q.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09r.png  style="width   *200px;">



*Edit **reliefd* and {{PropertyData|reliefw**   * Default values → Relief depth enlarged → Relief depth and width enlarged}}

<img alt="" src=images/SheetMetal_Example-09r.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09s.png  style="width   *200px;">



*Switch **relief Type* from {{value|Rectangle** to {{value|Round}}   * Default rectangular relief → Round relief}}

The round option will only be applied, if the relief depth is larger than the relief width.

Switch **Use Relief Factor** from `False` (default) to `True` to set the values of **reliefd** and **reliefw** automatically. Both are set to the object\'s (inherited) thickness multiplied by the value of **Relief Factor**.

   *   In this case the round option is useless, since the relief depth is as large as the relief width. (See above)


</div>


</div>

[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/de
