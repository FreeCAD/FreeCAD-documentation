# SheetMetal Examples/de
{{TOCright}}

## Einführung

Der Arbeitsbereich Blech (SheetMetal) ist ziemlich mächtig geworden und verlangt jetzt nach einer angemessenen Dokumentation.

Um die Überfüllung der Werkzeugseiten zu vermeiden, wurde diese Seite angelegt, um Teile zu sammeln, die die speziellen Blechfunktionen darstellen und erklären.

Geplante Phasen um Inhalte zu erstellen:

1.  Bilder sammeln
2.  Beschreibungen der Arbeitsabläufe hinzufügen
3.  Detailliertere Anleitungen erstellen

## Scharnier

<img alt="" src=images/SheetMetal_Example-01.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width:200px;"> 
*Arbeitsablauf Scharnier:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Bohrung](PartDesign_Hole/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Scharnier Schritt für Schritt 


<div class="mw-collapsible-content toccolours">

1.  Ein Profil erstellen (eine Linie und einen tangential anschließenden Bogen), vorzugsweise mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md).
2.  Den Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [BasisprofilErstellen](SheetMetal_AddBase/de.md) aktivieren, um ein BaseBend-Objekt zu erstellen.
3.  Die Parameter des BaseBend-Objekts editieren:
    -   Die {{PropertyData/de|Mid Plane}} auf `True` setzen, damit das Profil symmetrisch auf beiden Seiten der Skizzenebene aufgebaut wird.
    -   Der {{PropertyData/de|radius}} und der {{PropertyData/de|thickness}} gibt man Werte nach eigener Wahl.
4.  Erstellen einer Beschnittkontur mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md).
5.  Mit dem Befehl <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Tasche](PartDesign_Pocket/de.md) entfernt man eine Hälfte des runden Bereichs.
6.  Ein Lochbild mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md) erstellen.
7.  Den Befehl <img alt="" src=images/PartDesign_Hole.svg  style="width:16px;"> [PartDesign Bohrung](PartDesign_Hole/de.md) aktivieren. Die Optionen countersink (Kegelsenkung) und counterbore (Plan-/Zylindersenkung) sollte man vermeiden, damit das Objekt abwickelbar bleibt.
8.  Mit dem Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erstellt man ein Unfold-Objekt (Abwicklungskörper).
9.  Fertig!


</div>


</div>

## Aktenklammer

<img alt="" src=images/SheetMetal_Example-02.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width:200px;"> 
*Arbeitsablauf Aktenklammer:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md)**,
klonen, umdrehen und vereinigen,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Aktenklammer Schritt für Schritt 


<div class="mw-collapsible-content toccolours">

1.  Ein Profil erstellen, vorzugsweise mit dem <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md) auf der XZ-Ebene.
    <img alt="Profile sketch" src=images/SheetMetal_Example-02e.png  style="width:300px;">
2.  Den Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [BasisprofilErstellen](SheetMetal_AddBase/de.md) aktivieren, um ein BaseBend-Objekt zu erstellen.
3.  Die Parameter des BaseBend-Objekts im Eigenschafteneditor anpassen:
    <img alt="BaseBend-Objekt und hervorgehobene Skizze" src=images/SheetMetal_Example-02f.png  style="width:200px;">
    -   Die {{PropertyData/de|Mid Plane}} auf `True` setzen, damit das Profil symmetrisch auf beiden Seiten der Skizzenebene aufgebaut wird.
    -   Die {{PropertyData/de|length}} auf 32 mm setzen.
    -   Die {{PropertyData/de|radius}} auf 2 mm setzen.
    -   Die {{PropertyData/de|thickness}} auf 0.3 mm setzen.
4.  Auswahl der Fläche zwischen den Runden Abschnitten und Aktivieren des <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketchers](Sketcher_Workbench.md).
    <img alt="Basisfläche der Skizze" src=images/SheetMetal_Example-02g.png  style="width:200px;">
5.  Den aufgewickelten Teil blendet man mit dem Befehl <img alt="" src=images/Sketcher_ViewSection.svg  style="width:16px;"> [Sketcher SchnittAnzeigen](Sketcher_ViewSection/de.md) aus.
6.  Ausschnittkontur erstellen.
    <img alt="Ausschnittkontur" src=images/SheetMetal_Example-02h.png  style="width:" height="240px;"> <img alt="Die Ausschnittkontur überlappt die ausgewählte Fläche leicht" src=images/SheetMetal_Example-02i.png  style="width:" height="240px;">
7.  Die Skizze abschließen mit dem Befehl <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Sketcher SkizzeVerlassen](Sketcher_LeaveSketch/de.md).
8.  Die Fläche erneut auswählen und die Ausschnittskizze zur Auswahl hinzufügen.
    <img alt="Fläche und Skizze ausgewählt" src=images/SheetMetal_Example-02j.png  style="width:200px;">
9.  Den Befehl <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md) aktivieren, um den aufgewickelten Teil (entlang seiner Oberfläche) auszuschneiden.
    <img alt="Fertige erste Hälfte" src=images/SheetMetal_Example-02b.png  style="width:200px;">
10. Eine Seite ist nun fertig. Jetzt muss noch eine Möglichkeit zum Spiegeln des Objekts gefunden werden.

**Mögliche Spiegelungsoptionen:**

-   Der Befehl <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [PartDesign Spiegeln](PartDesign_Mirrored/de.md) versagt, da er aus irgendwelchen Gründen nicht mit SheetMetal-Objekten umgehen kann. So geht es also nicht.
-   Der Befehl <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [Part Spiegeln](Part_Mirror/de.md) erzeugt ein gespiegeltes Teil, aber dieses ist nicht mehr abwickelbar. So geht es also auch nicht.
-   Ein Weg der funktionieren kann ist die Verwendung eines Klones. Dieser kann zwar nicht gespiegelt werden, aber auf ihn kann Achsensymmetrie angewendet werden (Drehung um 180°).
-   Ein anderer funktionierender Weg ist die Verwendung eines Link-Objekts.

**Mirror using a clone:**

1.  Select the body from the tree view.
2.  Use the <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [PartDesign Clone](PartDesign_Clone.md) command. It adds a new body containing a clone object.
    To apply a 180° turn set the **Angle** under the Placement property of either the body or the clone to 180°. (Z axis is default and should be fine if you started on the XZ plane as described).
    <img alt="Cloned half" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="Flipped cloned half" src=images/SheetMetal_Example-02l.png  style="width:200px;">
3.  With the body still active, use the <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign Boolean operation](PartDesign_Boolean.md) command to add the body of the clone and fuse both halves.
    <img alt="Fused halves" src=images/SheetMetal_Example-02c.png  style="width:200px;">
4.  Activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) command to get an Unfold object.
    <img alt="Clip and Unfold object" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Unfold object" src=images/SheetMetal_Example-02d.png  style="width:200px;">
5.  Done!

**Mirror using a link object:**

1.  Select the body from the tree view.
2.  Use the <img alt="" src=images/Std_LinkMake.svg  style="width:16px;"> [Make link](Std_LinkMake.md) command. This adds a new link object.
3.  Duplicate the link object by setting the property **Element Count** to 2.
4.  To apply a 180° turn set the **Angle** under the Placement property of either of the sub-linked objects to 180°. (Z axis is default and should be fine if you started on the XZ plane as described).
5.  Select both sub-linked objects in the tree view.
6.  Activate the <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> [Part Fuse](Part_Fuse.md) command to fuse both halves.
    <img alt="Fused halves" src=images/SheetMetal_Example-02c.png  style="width:200px;">
7.  Activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) command to get an Unfold object.
    <img alt="Clip and Unfold object" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Unfold object" src=images/SheetMetal_Example-02d.png  style="width:200px;">
8.  Done!


</div>


</div>


<div class="mw-translate-fuzzy">

## Schelle


</div>

<img alt="" src=images/SheetMetal_Example-03.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width:200px;"> 
*Arbeitsablauf Schelle:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Bohrung](PartDesign_Hole/de.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Verrundung](PartDesign_Fillet/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}


<div class="mw-translate-fuzzy">

## Sechsseitige Schale 


</div>

<img alt="" src=images/SheetMetal_Example-04.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width:200px;"> 
*Workflow Hex Bowl:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width:200px;">

Wenn eine Eckentlastung hinzugefügt wurde (rechte Seite), kann es nötig sein den wert der Eigenschaft **Size** anzupassen.


<div class="mw-translate-fuzzy">

## Bleistiftklipp


</div>

<img alt="" src=images/SheetMetal_Example-05.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width:200px;"> 
*Arbeitsablauf Bleistiftklipp:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}


<div class="mw-translate-fuzzy">

## Beispiel zu Fläche erweitern 


</div>

<img alt="" src=images/SheetMetal_Example-06.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width:200px;"> 
*Arbeitsablauf Beispiel zu Fläche erweitern:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

Für die zweite Anwendung von **Fläche erweitern** wird eine Skizze mit zwei Konturen für die Form der Erweiterung(en) verwendet; und mit dem Setzen des Wertes von \"use subtraction\" auf true liefert sie auch die Form der Ausschnitte.

## USB-Massekontakt 

<img alt="" src=images/SheetMetal_Example-07.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width:200px;"> 
*Arbeitsablauf USB-Massekontakt:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Fläche erweitern](SheetMetal_Extrude/de.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}

(Die Zugentlastung ist nur eine künstlerische Darstellung von dem, was in einem echten Stecker versteckt sein kann)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/de
