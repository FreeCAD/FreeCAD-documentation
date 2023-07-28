# SheetMetal Examples/de
{{TOCright}}



## Einführung

Der Arbeitsbereich <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:24px;"> [SheetMetal](SheetMetal_Workbench/de.md) (ein [externer Arbeitsbereich](External_workbenches/de.md), der durch den [Addon-Manager](Std_AddonMgr/de.md) zur Verfügung gestellt wird) ist ziemlich mächtig geworden und verlangt jetzt nach einer angemessenen Dokumentation.

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

**Spiegeln mit einem Klon:**

1.  Das Body-Objekt in der Baumansicht auswählen.
2.  Den Befehl <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [PartDesign Klon](PartDesign_Clone/de.md) aktivieren. er fügt ein neues Body-Objekt hinzu, das ein Clone-Objekt enthält.
    Für eine 180°-Drehung setzt man die {{PropertyData/de|Winkel}} unter der Eigenschaft Placement des Körpers oder des Klons auf 180°. (Die Z-Achse ist standardmäßig voreingestellt und sollte funktionieren, wenn man, wie beschieben, auf der XZ-Ebene gestartet ist).
    <img alt="Geklonte Hälfte" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="Gedrehte geklonte Hälfte" src=images/SheetMetal_Example-02l.png  style="width:200px;">
3.  Mit dem immer noch aktiven Körper nutzt man den Befehl <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign BoolescheOperation](PartDesign_Boolean/de.md), um den Körper des Klons hinzuzufügen und beide Hälften zu vereinigen.
    <img alt="Vereinigte Hälften" src=images/SheetMetal_Example-02c.png  style="width:200px;">
4.  Mit dem Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erstellt man ein Unfold-Objekt.
    <img alt="Klammer und Abwicklung" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Abwicklung (Unfold-Objekt)" src=images/SheetMetal_Example-02d.png  style="width:200px;">
5.  Fertig!

**Spiegeln mit einem Link-Objekt:**

1.  Das Body-Objekt in der Baumansicht auswählen.
2.  Den Befehl <img alt="" src=images/Std_LinkMake.svg  style="width:16px;"> [Std VerknüpfungErstellen](Std_LinkMake/de.md) aktivieren. Er fügt ein neues Link-Objekt hinzu.
3.  Das Link-Objekt dupliziert man durch setzen der {{PropertyData/de|Element Count}} auf 2.
4.  Für eine 180°-Drehung setzt man die {{PropertyData/de|Winkel}} unter der Eigenschaft Placement eines der beiden unterverlinkten Objekte auf 180°. (Die Z-Achse ist standardmäßig voreingestellt und sollte funktionieren, wenn man, wie beschieben, auf der XZ-Ebene gestartet ist).
5.  Beide unterverlinkten Objekte in der Baumansicht auswählen.
6.  Den Befehl <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> [Part Vereinigung](Part_Fuse/de.md) aktivieren, um beide Hälften zu vereinigen.
    <img alt="Vereinigte Hälften" src=images/SheetMetal_Example-02c.png  style="width:200px;">
7.  Mit dem Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erstellt man ein Unfold-Objekt.
    <img alt="Klammer und Abwicklung" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Abwicklung (Unfold-Objekt)" src=images/SheetMetal_Example-02d.png  style="width:200px;">
8.  Fertig!


</div>


</div>



## Schelle

<img alt="" src=images/SheetMetal_Example-03.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width:200px;"> 
*Arbeitsablauf Schelle:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Bohrung](PartDesign_Hole/de.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Verrundung](PartDesign_Fillet/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}



## Sechsseitige Schale 

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



## Bleistiftklipp

<img alt="" src=images/SheetMetal_Example-05.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width:200px;"> 
*Arbeitsablauf Bleistiftklipp:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisprofil erstellen](SheetMetal_AddBase/de.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Tasche](PartDesign_Pocket/de.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Kante ansetzen](SheetMetal_AddWall/de.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Abwickeln](SheetMetal_Unfold/de.md)**.
}}



## Beispiel zu Fläche erweitern 

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



## SheetMetal Eigenschaften 

Dieser Abschnitt versucht die Eigenschaften jedes SheetMetal-Objekts, wo es möglich ist, mit einfachen Bildern zu erklären.


<div class="mw-collapsible mw-collapsed">

### BaseBend-Objekt <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

<img alt="" src=images/SheetMetal_Example-08a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08b.png  style="width:200px;">



*Ausgewählte Skizze + 
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)* 
→ BaseBend-Objekt mit Standardeinstellungen**

<img alt="" src=images/SheetMetal_Example-08b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08c.png  style="width:200px;">



*{{PropertyData/de|length* bearbeiten: Standardlänge → Reduzierte Länge}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08h.png  style="width:200px;">



*{{PropertyData/de|Mid Plane* von {{False}} auf `True` umschalten: Extrusion in eine Richtung → Symmetrische Extrusion}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;">



*{{PropertyData/de|Reverse* von {{False}} auf `True` umschalten: Standardrichtung → Umgekehrte Richtung}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08f.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08g.png  style="width:200px;">



*{{PropertyData/de|Bend Side* auswählen: {{value|Outside}} (Standard) → {{value|Inside}} → {{value| Middle}}}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08i.png  style="width:200px;">



*{{PropertyData/de|radius* bearbeiten: Standardradius → Vergrößerter Radius.<br>
Diese Eigenschaft entspricht dem Innenradius der Bögen, die an Knotenpunkten erstellt werden, an denen der Übergang zweier Kanten in der Skizze nicht tangential ist.}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08j.png  style="width:200px;">



*{{PropertyData/de|thickness* bearbeiten: Standardwandstärke → Vergrößerte Wandstärke}}


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Bend-Objekt <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Das Bend-Objekt besteht aus aus einem Sätzen aus jeweils einem zylindrischen Bogen und einem ebenen Streifen. Jedes dieser Paare beginnt an einer ausgewählten Kante einer Platine (ebener Blechabschnitt).

<img alt="" src=images/SheetMetal_Example-09a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09b.png  style="width:200px;">



*Ausgewählte Kanten + 
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/de.md)* 
→ Bend-Objekte mit Standardeinstellungen <br>
(Zwei Bend-Objekte in zwei separaten Körpern.)**

Die {{PropertyData/de|radius}} bearbeiten, um den inneren Radius aller Bogenstücke des Bend-Objekts zu verändern. (Siehe BaseBend-Objekt weiter oben)

Die {{PropertyData/de|length}} bearbeiten, um die Länge aller ebenen Streifen des Bend-Objekts, die an die Bogenstücke anschließen, zu verändern.

:   Man sollte die {{PropertyData/de|length}} nicht mit der Kantenlänge (flange length) verwechseln, die sich aus der Summe aus Länge, Radius und Wandstärke (den Eigenschaften length, radius, und thickness) ergibt (nur für 90° Winkel).

<img alt="" src=images/SheetMetal_Example-09b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;">



*Die {{PropertyData/de|invert* von `False` auf `True` umschalten: Kanten entsprechend den Standardeinstellungen (Bend objects) → Umgekehrte Kanten}}

<img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09e.png  style="width:200px;">



*Die {{PropertyData/de|angle* bearbeiten: Standardwinkel (90°) → Vergrößerter Winkel → Verkleinerter Winkel}}

Man muss sich nicht um den Beschnitt der Kanten kümmern, da **Auto Miter** (automatische Gehrung) standardmäßig aktiviert ist.
Wenn deaktiviert, sieht das Ergebnis so aus:

<img alt="" src=images/SheetMetal_Example-09m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09f.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09g.png  style="width:200px;">



*Die {{PropertyData/de|Auto Miter* von `True` auf `False` umschalten: Standardwinkel (90°) → Vergrößerter Winkel → Verkleinerter Winkel<br>
(Auf einzelne Kanten (flanges) hat **auto Miter** keine Auswirkung)}}

Um eine die Kante (edge) einer Kante (flange) von Hand mit einer Gehrung zu versehen, verwendet man **miterangle1** und **miterangle1**:

<img alt="" src=images/SheetMetal_Example-09m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09n.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09o.png  style="width:200px;">



*Die {{PropertyData/de|miterangle1* and **miterangle2** bearbeiten: Keine Gehrung (Standard) → Gehrung mit unterschiedlichen positiven Winkeln, → Symmetrische Gehrung mit negativen Winkeln}}

Die Gehrung betrifft nur die ebenen Streifen, nicht die Bogenstücke.

:   (Es verläuft über die gesamte Länge der Kanten (edges) und kann daher nicht zum Anfasen der Kanten (edges) der Kanten (flanges) verwendet werden)

Um die verschiedenen Möglichkeiten von **Bend Type** darzustellen, wird ein Hilfsquader eingesetzt, der auf derselben Ebene steht, wie die Platine und der die gleiche Höhe hat, wie das Bend-Objekt (seine Kantenlänge).

<img alt="" src=images/SheetMetal_Example-09h.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09i.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09j.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09k.png  style="width:200px;">



*Die **Bend Type* auswählen: {{value|Material Outside**  (Standardwert) → {{value|Material Inside}} → {{value|Thickness Outside}} → {{value|Offset}}}}

-   Outside: (Außerhalb) Der Bogen beginnt an der ausgewählten Kante (edge) (Das ganze Bend-Objekt liegt außerhalb des Quaders).
-   Inside: (Innerhalb) Die Außenseite der Kante (flange) endet an der Oberfläche des Quaders (Das ganze Bend-Objekt liegt innerhalb des Quaders).
-   Thickness Outside: (Wandstärke außerhalb) Die Innenseite des Bogens endet an der Oberfläche des Quaders (Nur der ebene Streifen tritt aus der Oberfläche des Quaders hervor).
-   Offset: (Versatz) Abhängig vom Wert der {{PropertyData/de|offset}} wird der Bogen von seiner Standardposition in Richtung nach außen versetzt.

:   Für positive Werte wird eine Erweiterung eingefügt (hervorgehobener Streifen).
:   Negative Werte sind erlaubt, um den Bogen nach innen zu bewegen.

Wenn nicht die ganze Länge einer Kante (edge) verwendet werden soll, können **gap1** und **gap2** verwendet werden.

<img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09l.png  style="width:200px;">



*Die {{PropertyData/de|gap1* und {{PropertyData/de|gap2}} bearbeiten: Kanten entsprechend den Standardeinstellungen → Kanten(flanges) mit unterschiedlichen Werten für gap1 und gap2}}

Wenn die Länge einer Lücke (gap) den Wert der {{PropertyData/de|min Relief Gap}} erreicht oder überschreitet, wird ein Entlastungsausschnitt zur Lücke hinzugefügt .
Die Entlastungsausschnitte werden durch die {{PropertyData/de|relief Type}} (Art des Ausschnitts), die {{PropertyData/de|reliefd}} (Tiefe des Ausschnitts), und die {{PropertyData/de|reliefw}} (Breite des Ausschnitts) gesteuert, die nur dann aktiv sind, wenn ein Wert für eine Lücke angegeben wurde.

<img alt="" src=images/SheetMetal_Example-09p.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09q.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09r.png  style="width:200px;">



*Die {{PropertyData/de|reliefd* und die {{PropertyData/de|reliefw}} bearbeiten: Standardwerte → Ausschnitttiefe vergrößert → Ausschnitttiefe und -Breite vergrößert}}

<img alt="" src=images/SheetMetal_Example-09r.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09s.png  style="width:200px;">



*Die {{PropertyData/de|relief Type* von {{value|Rectangle}} auf {{value|Round}} umschalten: Standardmäßiger rechteckiger Entlastungsausschnitt → Runder Entlastungsausschnitt}}

Die Option rund wird nur dann angewendet, wenn die Ausschnitttiefe größer als die Ausschnittbreite ist.

Die {{PropertyData/de|Use Relief Factor}} von `False` (Standardwert) auf `True` umschalten, um die Werte der {{PropertyData/de|reliefd}} und der {{PropertyData/de|reliefw}} automatisch einzusetzen. Beide werden auf die (ererbte) Wandstärke des Objekts multipliziert mit dem Wert der {{PropertyData/de|Relief Factor}} gesetzt.

:   In diesem Falle ist die Option rund nutzlos, da die Ausschnitttiefe und die Ausschnittbreite gleich groß sind. (Siehe oben)

Eine neue {{PropertyData/de|Length Spec}} {{Version/de|0.21}} ermöglicht es, auszuwählen, wie die Länge des Bend-Objekts gemessen wird:

<img alt="" src=images/SheetMetal_Example-09t.png  style="width:500px;"> 
*Seitenansicht auf vier 120°-Kanten mit der Vorgabelänge (10 mm) und unterschiedlichen Werten der {{PropertyData/de|Length Spec*: <br> Nur der ebene Streifen {{value|Leg}} (Standard), Außenmaß zur theoretischen Ecke {{value|Outer Sharp}}, Innenmaß zur theoretischen Ecke {{value|Inner Sharp}}, Außenmaß bie Bogen {{value|Tangential}}}}

Mit der ausgewählten Option {{value|Tangential}} entspricht die {{PropertyData/de|length}} der Kantenhöhe (flange length).


{{value|Outer Sharp}}

und {{value|Tangential}} sind gleich für 90°-Winkel.


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Extend-Objekt <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Ein Extend-Objekt verlängert eine SheetMetal-Platine an einer oder mehreren ausgewählten Randflächen oder Kanten.

<img alt="" src=images/SheetMetal_Example-10a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10b.png  style="width:200px;">



*Ausgewählte Randflächen und Kanten + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [KanteVerlängern](SheetMetal_Extrude/de.md)* 
→ Ein Extend-Objekt mit Standardeinstellungen.**

Hier tritt ein erstes Problem auf: Obwohl die {{PropertyData/de|Refine}} (Aufbereiten) auf `True` gesetzt ist, zeigen zwei der Verlängerungen noch ihre Nahtlinien. Nur die Verlängerung des zuletzt ausgewählten Elements werden durch Aufbereiten entfernt.

Um alle Verlängerungen aufzubereiten, müssen sie einzeln erstellt werden:

<img alt="" src=images/SheetMetal_Example-10c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10f.png  style="width:200px;">



*3x ausgewählte Randfläche oder Kante + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [KanteVerlängern](SheetMetal_Extrude/de.md)* 
→ Drei Extend-Ojekte komplett aufbereitet und mit Standardeinstellungen.**

Veränderte Eigenschaften betreffen alle kanten, die in der zugehörigen {{PropertyData/de|base Object}} des Extension-Objekts gelistet sind.

Die {{PropertyData/de|length}} anpassen, um die Länge der Verlängerung einzustellen.

<img alt="" src=images/SheetMetal_Example-10h.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-10g.png  style="width:200px;">



*Die {{PropertyData/de|gap1* und {{PropertyData/de|gap2}} anpassen, um die Breite der Verlängerung zu verringern.<br>
Links: Extension-Objekt mit 3 Kanten. Rechts: Eins der Extension-Objekte mit einer einzelnen Kante.}}

Eine Skizze mit der {{PropertyData/de|Sketch}} verknüpfen, um die Form einer Verlängerung zu erweitern. Die {{PropertyData/de|length}}, {{PropertyData/de|gap1}} und {{PropertyData/de|gap2}} werden ignoriert, sobald eine Skizze verknüpft wurde. (Dies scheint mit noch ungebogenen Platinen nicht zu funktionieren).

<img alt="" src=images/SheetMetal_Example-10i.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10j.png  style="width:200px;">



*Eine ausgewählte Skizze auf der zu erweiternden Kante liegend → Resultierende Erweiterung*

Es ist deutlich zu erkennen, dass es egal ist, welche Kante für das Extend-Objekt ausgewählt wurde, die Form des Flansches wird überall erweitert, wo Skizzengeometrie hervorsteht, die neue Form kann sogar Elemente ohne Verbindung zum originalen Flansch enthalten. Mehrfache Konturen sind kein Problem, aber es wird nicht in den Flansch hineingeschnitten.

Dieses Beispiel zeigt, dass Konstrukteure für ihre Konstruktion verantwortlich sind und sich nicht auf die Ergebnisse ihrer Werkzeuge verlassen sollten, die in diesem Falle keinen Sinn machen. Die Skizze direkt am Flansch angebracht ist auch problematisch aufgrund des Problems der topologischen Benennung, aber dafür ist eine Lösung in Sicht.

Aber es gibt bessere Anwendungsfälle für dieses Werkzeug, die fast ganz geschlossene Formen beinhalten, so wie eins der Beispiele auf der Seite [SheetMetal KanteVerlängern](SheetMetal_Extrude/de.md):

<img alt="" src=images/SheetMetal_Example-10k.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10l.png  style="width:200px;">



*Ein fast geschlossenes Profil → Die hinzugefügte Erweiterung ist standardmäßig mit der gegenüberliegenden Seite verschmolzen und bildet so ein geschlossenes Profil (ein Rohr), das nicht abwickelbar ist.*

<img alt="" src=images/SheetMetal_Example-10l.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10m.png  style="width:200px;">



*Eine rechteckige Skizze mit der {{PropertyData/de|Sketch* verknüpft: Geschlossenes Profil → Profil mit rechteckiger Erweiterung, noch immer verschmolzen}}

<img alt="" src=images/SheetMetal_Example-10m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10n.png  style="width:200px;">



*Die {{PropertyData/de|Use Subtraction* auf {{true}} umschalten, um einen (kaum sichtbaren) Spalt zwischen dem Extension-Objekt und der gegenüberliegenden Seite zu erhalten, dann den Wert der {{PropertyData/de|Offset}} erhöhen, um den Spalt aufzuweiten:<br>
Verschmolzenes Profil → Profil mit verzahnter Erweiterung; dieses Endergebnis ist abwickelbar}}


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/de
