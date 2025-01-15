---
 GuiCommand:
   Name: Arch Wall
   Name/de: Arch Wand
   MenuLocation: 3D/BIM , Wand
   Workbenches: BIM_Workbench/de
   Shortcut: **W** **A**
   SeeAlso: 
---

# Arch Wall/de



## Beschreibung

Das Werkzeug **Arch Wand** erzeugt neue Wände oder baut Wände basierend auf einem anderen [Form](Part_Workbench/de.md)-basierten oder [Polygonnetz](Mesh_Workbench/de.md)-basierten Objekt. Eine Wand kann ohne ein Basisobjekt erstellt werden, wobei es sich dann wie ein räumliches Objekt verhält, mit Länge-, Breite- und Höhe-Eigenschaften. Wird auf einem existierenden Objekt aufgebaut, kann eine Wand aufgesetzt werden auf:

-   Ein **lineares 2D Objekt**, wie z. B. Linien, Drähte, Bögen oder Skizzen. In diesem Fall kannst du Dicke, Ausrichtung (rechts, links oder zentriert) und Höhe ändern. Die Eigenschaft Länge hat keine Auswirkung.
-   Eine **flache Fläche**, in diesem Fall kannst du nur die Höhe ändern. Die Eigenschaften Länge und Breite haben keine Auswirkung. Wenn die Grundfläche jedoch senkrecht ist, verwendet die Wand die Eigenschaft Breite anstelle der Höhe, so dass du Wände aus raumartigen Objekten oder Massenstudien erstellen kannst.
-   Ein **Festkörper**, in diesem Fall haben die Eigenschaften Länge, Breite und Höhe keine Auswirkung. Die Wand verwendet einfach das darunter liegende Solid als Form.
-   Ein **Polygonnetz**, in diesem Fall muss das zugrunde liegende Netz ein geschlossener, vielfältiger Körper sein.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Wände, welche jeweils auf einer Linie, einem Drahtgitter, einer Fläche, einem Körper, sowie einer Skizze aufgebaut werden*

Wände können auch Ergänzungen oder Aussparungen erhalten. Ergänzungen sind andere Objekte, deren Form mit der Wandform verschmolzen werden. Bei Aussparungen werden die Formen des anderen Objektes aus der Wand entfernt. Ergänzungen und Aussparungen können mit dem **<img src="images/Arch_Add.png" width=16px> [Hinzufügen](Arch_Add/de.md)** bzw. **<img src="images/Arch_Remove.png" width=16px> [Entfernen](Arch_Remove/de.md)** Werkzeug erzeugt werden. Ergänzungen und Aussparungen haben keinen Einfluss auf Parameter wie Höhe oder Breite, die nach wie vor änderbar sind.

Wenn sich mehrere Wände überschneiden sollen, musst du diese in eine [Etage](Arch_Floor/de.md) platziert werden, damit sich ihre Geometrien überschneiden.



## Anwendung



### Zeichnen einer neuen Wand 

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)** drücken.
    -   Den Menüeintrag **3D/BIM → <img src="images/Arch_Wall.svg" width=16px> Wand** auswählen.
    -   Das Tastaturkürzel **W** und dann **A**.
2.  Einen ersten Punkt in der 3D-Ansicht anklicken oder die Koordinaten eingeben.
3.  Einen zweiten Punkt in der 3D-Ansicht anklicken oder die Koordinaten eingeben.



### Zeichnen einer Wand auf einem ausgewählten Objekt 

1.  Ein oder mehrere Basisgeometrieobjekte (Draft-Objekt, Skizze, usw.) auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen.
3.  Die benötigten Eigenschaften wie Höhe oder Breite anpassen.



## Optionen

-   Wände haben die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch-Komponenten](Arch_Component/de.md).

-   Die Höhe, Dicke und Ausrichtung einer Wand können während des Zeichnens über den Aufgaben-Bereich festgelegt werden.

-   Wenn eine Wand an einer bestehende Wand einrastet, werden beide Wände zu einer Wand verbunden. Die Art und Weise, wie die beiden Wände miteinander verbunden werden, hängt von ihren Eigenschaften ab: Wenn sie die gleiche Breite, Höhe und Ausrichtung haben und wenn die Option \"Basisskizzen verbinden\" in den Arch-Voreinstellungen aktiviert ist, wird die resultierende Wand ein einziges Objekt sein, das auf einer Skizze basiert, die aus mehreren Segmenten besteht. Andernfalls wird die letztere Wand der ersten als Zusatz hinzugefügt.

-   Nach dem ersten Punkt **X**, **Y** oder **Z** drücken, um den zweiten Punkt auf die eingegebene Achse festzulegen.

-   Um Koordinaten manuell einzugeben, gib einfach die Zahlen ein und drücke jeweils **Eingabe** zwischen den X-, Y- und Z-Komponenten.

-    **R**drücken oder auf das Kontrollkästchen klicken, um die Schaltfläche **Relativ** zu aktivieren/deaktivieren. Wenn der Relativ-Modus eingeschaltet ist, sind die Koordinaten des zweiten Punktes relativ zum ersten Punkt. Wenn nicht, sind sie absolut, ausgehend vom (0,0,0) Ursprungspunkt.

-    **Umschalten**während des Zeichnens drücken, um den zweiten Punkt horizontal oder vertikal in Bezug zum ersten [festzulegen](Draft_Constrain/de.md).

-    **Esc**oder die Schaltfläche **Abbrechen** drücken, um den aktuellen Befehl abzubrechen.

-   Doppelklicken auf die Wand in der Baumansicht nach ihrer Erstellung erlaubt dir in den Bearbeitungsmodus wechseln und auf deine Additionen und Subtraktionen zuzugreifen und sie zu ändern.

-   Mehrschichtige Wände können leicht erstellt werden, indem mehrere Wände von derselben Grundlinie aus gebaut werden. Durch setzen ihrer Ausrichtungseigenschaft entweder auf links oder rechts und Angabe eines Versatzwertes, kannst du effektiv mehrere Wandschichten konstruieren. Wird ein Fenster in einer solchen Wandschicht plaziert, wird die Öffnung auch auf die anderen Wandschichten übertragen, die auf derselben Grundlinie basieren.

-   Wände können auch [Multimaterialien](Arch_MultiMaterial/de.md) verwenden. Wenn ein Multimaterial verwendet wird, wird die Wand mehrschichtig, wobei die durch das Multimaterial vorgegebenen Dicken verwendet werden. Bei jeder Schicht mit einer Dicke von Null wird die Dicke automatisch durch den verbleibenden Raum definiert, der durch den Wert für die Wandbreite definiert ist, nachdem die anderen Schichten abgezogen wurden.

-   Wände können für die Anzeige von Blöcken anstelle eines einzelnen Festkörpers eingestellt werden, indem ihre {{PropertyData/de|Make Blocks}} eingeschaltet wird. Die Größe und der Versatz von Blöcken kann mit verschiedenen Eigenschaften konfiguriert werden, und die Anzahl der Blöcke wird automatisch berechnet.



## Fangen

Fangen funktioniert etwas anders mit Architektur Wänden als andere Architektur und Entwurf Objekte. Wenn eine Wand ein Grundlinienobjekt hat, verankert sich das Fangen am Basisobjekt und nicht an der Wandgeometrie, so dass Wände leicht an ihrer Grundlinie ausgerichtet werden können. Wenn du jedoch speziell an der Wandgeometrie fangen möchtest, drücken von **Strg** schaltet das Fangen auf das Wandobjekt um.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Zweite Wand gefangen senkrecht zur ersten*



## Eigenschaften

Wände (Wall-Objekte) erben die Eigenschaften von [Part](Part_Workbench.md)-Objekten und besitzen die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Blocks}}

-    {{PropertyData/de|Block Height}}: Die Höhe jedes Bausteins.

-    {{PropertyData/de|Block Length}}: Die Länge jedes Bausteins.

-    {{PropertyData/de|Count Broken}}: Die Anzahl von geschnittenen (broken) Bausteinen (schreibgeschützt).

-    {{PropertyData/de|Count Entire}}: Die Anzahl von ganzen Bausteinen (schreibgeschützt).

-    {{PropertyData/de|Joint}}: Die Breite der Fugen, der leere Raum zwischen Bausteinen.

-    {{PropertyData/de|Make Blocks}}: Aktiviert die Erstellung von Bausteinen (blocks).

-    {{PropertyData/de|Offset First}}: Der horizontale Abstand der ersten und aller ungeraden Reihen von Bausteinen.

-    {{PropertyData/de|Offset Second}}: Der horizontale Abstand der zweiten und aller geraden Reihen von Bausteinen.


{{TitleProperty|Component}}

Siehe [Arch Komponente](Arch_Component/de#Eigenschaften.md).


{{TitleProperty|IFC}}

Siehe [Arch Komponente](Arch_Component/de#Eigenschaften.md).


{{TitleProperty|IFC Attributes}}

Siehe [Arch Komponente](Arch_Component/de#Eigenschaften.md).


{{TitleProperty|Wall}}

-    {{PropertyData/de|Align}}: Die Ausrichtung der Wand an ihrer Basislinie: Left, Right oder Center (links, rechts oder mittig). Die Richtung der individuellen Kanten des Basisobjekts (Sketch/ArchSketch) wird berücksichtigt und ergibt eine genauere Kontrolle über jeden Wandabschnitt. Siehe folgendes Diagram. Kreisbögen (arcs) in Skizzen verlaufen immer gegen den Uhrzeigersinn. Wenn ein gekrümmter Abschnitt einer Wand links ausgerichtet ist, entspricht die innere Kante des Abschnitts dem Kreisbogen der Skizze. Siehe auch **Override Align**.

-    {{PropertyData/de|Area}}: Flächeninhalt der ganzen Wand; eine Unterteilung in Bausteine macht keinen Unterschied. (Schreibgeschützt).

-    {{PropertyData/de|Face}}: Der Index der Fläche des zu benutzenden Basisobjekts. Falls der Wert nicht gesetzt wurde oder 0 ist, wird das gesamt Objekt benutzt.

-    {{PropertyData/de|Height}}: Die Höhe der Wand. Wird ignoriert, wenn die Wand auf einem Festkörper basiert. Wenn auf Null gesetzt und die Wand befindet sich in einem [Geschoss](Arch_Floor/de.md)-Objekt dessen Höhe festgelegt ist, übernimmt die Wand automatisch den Wert der Geschosshöhe.

-    {{PropertyData/de|Length}}: Die Länge der Wand. Der Wert kann geändert werden, wenn die Wand auf einer Skizze ohne Randbedingungen mit einer einzelnen Kante, oder auf einem [Draft Linienzug](Draft_Wire/de.md) mit einer einzelnen Kante basiert, andernfalls ist der Wert schreibgeschützt. {{Version/de|1.0}} Der Wert ist präziser, wenn die Eigenschaft schreibgeschützt ist. Er basiert auf dem Mittelwert der Wand, falls Abschnitte unterschiedliche {{PropertyData/de|Width}}, {{PropertyData/de|Align}} und/oder {{PropertyData/de|Offset}} aufweisen. Man beachte, dass weiterhin Ungenauigkeiten auftreten können, wenn die Wand kompliziert ist, sie z.B. T-Stöße und Selbstdurchdringungen aufweist. In solchen Fällen ist es ratsam, die {{PropertyData/de|Horizontal Area}} für weitere Berechnungen zu verwenden.

-    {{PropertyData/de|Normal}}: Die Extrusionsrichtung für die Wand. Wenn auf (0,0,0) gesetzt, wird die Extrusionsrichtung automatisch festgelegt.

-    {{PropertyData/de|Offset}}: Der Abstand zwischen der Wand und ihrer Grundlinie fest. Das funktioniert nur, wenn die Eigenschaft **Override Align** auf Right (rechts) oder Left (links) gesetzt ist. Die Richtung der individuellen Kanten des Basisobjekts (Sketch/ArchSketch) wird berücksichtigt und ergibt eine genauere Kontrolle über jeden Wandabschnitt. Siehe auch **Override Offset**.

-    {{PropertyData/de|Override Align}}: Dies überschreibt das Attribut **Align**, um die Ausrichtung jedes Abschnitts der Wand einzeln festzulegen; wird ignoriert, wenn das Basisobjekt Informationen zur Ausrichtung über die Methode getAligns() zur Verfügung stellt (Ist ein Wert weder \'Links, Rechts noch MItte\', wird der Wert von \'Align\' verwendet). ERWEITERUNG durch ArchSketch: GUI-Werkzeug \'Edit Wall Segment Align\' wird durch das externe <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [SketchArch Add-on](https://github.com/paullee0/FreeCAD_SketchArch) zur Verfügung gestellt, um den Anwender die Werte interaktiv eingeben zu lassen. \'Toponaming-Tolerant\' wenn ArchSketch als Basis eingesetzt wird (und das SketchArch Add-on installiert ist). Warnung: Nicht \'Toponaming-Tolerant\' wenn nur eine Skizze eingesetzt wird.

-    {{PropertyData/de|Override Width}}: Dies überschreibt das Attribut **Width**, um die Breite für jeden Wandabschnitt einzeln festzulegen; wird ignoriert, wenn das Basisobjekt Informationen zur Breite über die Methode getWidths() zur Verfügung stellt. (Ist ein Wert null, wird der Wert von \'Width\' verwendet). ERWEITERUNG durch ArchSketch: GUI-Werkzeug \'Edit Wall Segment Width\' wird durch das externe <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [SketchArch Add-on](https://github.com/paullee0/FreeCAD_SketchArch) zur Verfügung gestellt, um den Anwender die Werte interaktiv eingeben zu lassen. \'Toponaming-Tolerant\' wenn ArchSketch als Basis eingesetzt wird (und das SketchArch Add-on installiert ist). Warnung: Nicht \'Toponaming-Tolerant\' wenn nur eine Skizze eingesetzt wird.

-    {{PropertyData/de|Override Offset}}: ({{Version/de|1.0}}) Dies überschreibt das Attribut **Offset**, um den Abstand für jeden Wandabschnitt einzeln festzulegen; wird ignoriert, wenn das Basisobjekt Informationen zum Abstand über die Methode getOffsets() zur Verfügung stellt.(Ist ein Wert null, wird der Wert von \'Offset\' verwendet). ERWEITERUNG durch ArchSketch: GUI-Werkzeug \'Edit Wall Segment Offset\' wird durch das externe <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [SketchArch Add-on](https://github.com/paullee0/FreeCAD_SketchArch) zur Verfügung gestellt, um den Anwender die Werte interaktiv eingeben zu lassen. \'Toponaming-Tolerant\' wenn ArchSketch als Basis eingesetzt wird (und das SketchArch Add-on installiert ist). Warnung: Nicht \'Toponaming-Tolerant\' wenn nur eine Skizze eingesetzt wird. Die Eigenschaft wird ignoriert, wenn der Basis-ArchSketch die ausgewählten Kanten zur verfügung stellt.

-    {{PropertyData/de|Width}}: Die Breite der Wand. Wird ignoriert, wenn die Wand auf einer Fläche oder einem Festkörper basiert. Siehe auch **Override Width**.

<img alt="" src=images/Sketch_vs_Wall.jpg  style="width:480px;">



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Wand-Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden:


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Erzeugt ein `Wall`-Objekt aus dem gegebenen `baseobj`, welches ein [Draft-Objekt](Draft_Workbench/de.md), eine [Skizze](Sketcher_Workbench/de.md), eine Fläche oder ein Körper sein kann.

-   Falls kein `baseobj` angegeben wurde, können die numerische Werte für Länge, Breite und Höhe vorgegeben werden.
    -   Falls angegeben, kann `face` genutzt werden, um den Index einer Fläche des zugrundeliegenden Objekts anzugeben, auf dem diese Wand erstellt wird, anstatt das komplette Objekt zu verwenden.

-    `align`kann auf `"Center"`, `"Left"` oder `"Right"` gesetzt werden.

-   Liefert `None` zurück, falls die Operation fehlschlägt.

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Wall/de
