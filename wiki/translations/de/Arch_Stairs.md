---
 GuiCommand:
   Name: Arch Stairs
   Name/de: Arch Treppe
   MenuLocation: 3D/BIM , Treppe
   Workbenches: BIM_Workbench/de
   Shortcut: **S** **R**
   Version: 0.14
   SeeAlso: 
---

# Arch Stairs/de



## Beschreibung

Das Werkzeug [Treppe](Arch_Stairs/de.md) ermöglicht verschiedene Arten von Treppen automatisch zu erstellen. Gerade Treppen (mit und ohne mittiges Podest) können von Grund auf neu erstellt werden. Komplexere Treppen erfordern Basisobjekte.

Siehe den [Wikipediaeintrag Treppe](https://de.wikipedia.org/wiki/Treppe) für eine Erläuterung der verschiedenen verwendeten Begriffe zum beschreiben der Treppenbauteile.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;"> 
*Zwei konstruierte Treppen, eine mit massiver Struktur und Absatz  und die andere mit einer mittigen Treppenwange.*



## Optionen

-   Treppen haben die gleichen Eigenschaften und verhalten sich wie alle anderen [Arch-Komponenten](Arch_Component/de.md)



## Anwendung

1.  Wahlweise ein oder mehrere Basisobjekte auswählen, z.B. [Draft Linien](Draft_Line/de.md), [Draft Linienzüge](Draft_Wire/de.md) und [Skizzen](Sketch/de.md):
    -   Draft-Linienzüge oder Skizzen mit zwei und mehr Abschnitten werden verwendet, um Podeste zu erstellen. Sie müssen auf einer Ebene liegen, die parallel zur globalen XY-Ebene verläuft. Z.B. ein U-förmiger Linienzug für ein Podest mit einer halben Drehung (180°) und ein L-förmiger Linienzug für ein Eckpodest (90°).
    -   Draft-Linien und Skizzen mit einer einzelnen Kante werden verwendet, um Treppen zu erstellen.
    -   Haben die Knoten aller Linien und Linienzüge korrekte Z-Koordinaten, verwendet die erstellte Treppe diese Informationen. Eine Skizze (parallel zur XY-Ebene) mit einer einzelnen Kante oder eine Draft-Linie ohne Abweichung in Z funktioniert auch für ein Podest; Die Höhe wird dann für die Konstruktion des Podests verwendet.
    -   Die Basisobjekt müssen in der richtigen Reihenfolge ausgewählt werden, beginnend mit dem untersten Objekt.
2.  Die Schaltfläche **<img src="images/Arch_Stairs.png" width=16px> [Treppe](Arch_Stairs/de.md)** drücken oder das Tastaturkürzel **S**, **R**.
3.  Die gewünschten Werte anpassen. Einige Bauteile der Treppe, wie die Struktur, sind nicht sofort sichtbar, wenn irgendeine der Eigenschaften dies unmöglich macht, wie eine Wandstärke der Struktur von 0.

<img alt="" src=images/Stairs_and_Landing_02.png  style="width:600px;">

<img alt="" src=images/Stairs_and_Landing_01.png  style="width:600px;">

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;">



*Eine komplexe Treppe, die auf einer Auswahl von Linien und Linienzügen basiert, wie links gezeigt.<br>
Rot: die Linienzüge für die Podeste auf Z &equals; 1500 mm, Z &equals; 3000 mm and Z &equals; 4500 mm.<br>
Schwarz: die Linien, die sie verbinden und für die Treppen verwendet werden.
*



## Eigenschaften



### Daten


{{TitleProperty|Segment and Parts}}

-    **Abs Top|Vector**: (read-only) The absolute top level the stairs lead to.

-    **Last Segment|Link**: Last segment (flight or landing) of an Arch Stairs connecting to this segment. The start level of the stairs will be the end level of this last segment.

-    **Outline Left|VectorList**: The left outline of the stairs (read-only).

-    **Outline Left All|VectorList**: The left outline of all segments of the stairs (read-only).

-    **Outline Right|VectorList**: The right outline of the stairs (read-only).

-    **Outline Right All|VectorList**: The right outline of all segments of the stairs (read-only).

-    **Railing Height Left|Length**: Height of the left railing of the stairs or landing.

-    **Railing Height Right|Length**: Height of the right railing of the stairs or landing.

-    **Railing Left|LinkHidden**: The left railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Offset of the left railing from the edge of the stairs or landing.

-    **Railing Offset Right|Length**: Offset of the right railing from the edge of the stairs or landing.

-    **Railing Right|LinkHidden**: The right railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.


{{TitleProperty|Stairs}}

-    {{PropertyData/de|Align|Enumeration}}: Die Ausrichtung der Treppe zur Basislinie. Wird nur verwendet, wenn eine Basislinie festgelegt ist. Kann {{value|Left}} (links), {{value|Right}} (rechts) oder {{value|Center}} Mitte.

-    {{PropertyData/de|Height|Length}}: Die Gesamthöhe der Treppe. Wird nur verwendet, wenn eine Basislinie festgelegt ist oder wenn die Basislinie horizontal ist. Wird ignoriert, wenn die {{PropertyData/de|Riser Height Enforce}} nicht Null ist.

-    {{PropertyData/de|Length|Length}}: Die Gesamtlänge der Treppe, wenn keine Basislinie festgelegt ist. Wird ignoriert, wenn die {{PropertyData/de|Tread Depth Enforce}} nicht Null ist.

-    {{PropertyData/de|Width|Length}}: Die Breite der Treppe.

-    {{PropertyData/de|Width of Landing|FloatList}}: Wenn die {{PropertyData/de|Number Of Steps}} (Anzahl der Stufen) 1 ist, wird das Treppenobjekt als Treppenabsatz eingesetzt. Ist dies der Fall und die Basislinie besteht aus mehreren Abschnitten, wird die Breite des ersten Abschnitts des Treppenabsatzes der {{PropertyData/de|Width}} entsprechen, die Breiten folgender Abschnitte entsprechen denen dieser Liste.


{{TitleProperty|Steps}}

-    {{PropertyData/de|BlondelRatio|Float}}: (schreibgeschützt) Das errechnete Steigungsverhältnis (Blondel ratio). Dieses Verhältnis sollte für bequeme Stufen zwischen 62 und 64 cm bzw. 24.5 und 25.5 Zoll liegen.

-    {{PropertyData/de|Landing Depth|Length}}: Die Tiefe des Absatzes des Stockwerks, wenn in der {{PropertyData/de|Landings}} aktiviert. Übernimmt standardmäßig den wert der {{PropertyData/de|Width}}, wenn 0.

-    {{PropertyData/de|Nosing|Length}}: Überstand des Auftritts (nosing) gegenüber der darunterliegenden Setzstufe.

-    {{PropertyData/de|Number Of Steps|Integer}}: Die Anzahl der Treppenstufen (Setzstufen) der Treppe. Muss mindestens 2 für eine einzelne Treppe sein oder 4 für 2 Treppen mit einem Absatz dazwischen.

-    {{PropertyData/de|Riser Height|Length}}: (schreibgeschützt) Die Höhe der Setzstufen. Ist die {{PropertyData/de|Riser Height Enforce}} 0, wird sie berechnet ({{PropertyData/de|Height}} / {{PropertyData/de|Number of Steps}}). Andernfalls hat sie denselben Wert, wie die {{PropertyData/de|Riser Height Enforce}}.

-    {{PropertyData/de|Riser Height Enforce|Length}}: Die erzwungene Höhe der Setzstufe.

-    {{PropertyData/de|Riser Thickness|Length}}: Die Wandstärke der Setzstufen.

-    {{PropertyData/de|Tread Depth|Length}}: (schreibgeschützt) Die Tiefe des Auftritts. Ist die {{PropertyData/de|Tread Depth Enforce}} 0, wird sie berechnet ({{PropertyData/de|Length}} / **Number of Steps**). Andernfalls hat sie denselben Wert, wie die {{PropertyData/de|Tread Depth Enforce}}.

-    {{PropertyData/de|Tread Depth Enforce|Length}}: Die erzwungene Tiefe des Auftritts.

-    {{PropertyData/de|Tread Thickness|Length}}: Die Wandstärke des Auftritts.


{{TitleProperty|Structure}}

-    {{PropertyData/de|Connection Down Start Stairs|Enumeration}}: Die Art der Verbindung zwischen der unteren Bodenplatte und dem Beginn der Treppe. Kann {{value|HorizontalCut}}, {{value|VerticalCut}} oder {{value|HorizontalVerticalCut}} sein.

-    {{PropertyData/de|Connection End Stairs Up|Enumeration}}: Die Art der Verbindung zwischen dem Ende der Treppe und der Bodenplatte im oberen Stockwerk. Kann {{value|toFlightThickness}} oder {{value|toSlabThickness}} sein.

-    {{PropertyData/de|Down Slab Thickness|Length}}: Die Dicke der unteren Bodenplatte.

-    {{PropertyData/de|Flight|Enumeration}}: die Treppenlaufrichtung nach dem Podest. Kann {{value|Straight}}, {{value|HalfTurnLeft}} oder {{value|HalfTurnRight}} sein.

-    {{PropertyData/de|Landings|Enumeration}}: Die Art der Podeste. Kann {{value|None}} oder {{value|At center}} sein ({{value|At each corner}} ist noch nicht implementiert).

-    {{PropertyData/de|Stringer Overlap|Length}}: Die Überlappung der Wangen über die Unterseite der Auftrittflächen.

-    {{PropertyData/de|Stringer Width|Length}}: Die Breite der Wangen.

-    {{PropertyData/de|Structure|Enumeration}}: Die Art der Struktur der Stufen. Kann {{value|None}}, {{value|Massive}}, {{value|One stringer}} oder {{value|Two stringers}} sein.

-    {{PropertyData/de|Structure Offset|Length}}: Der Abstand zwischen der Begrenzung der Treppe und der Struktur.

-    {{PropertyData/de|Structure Thickness|Length}}: Die Dicke der Struktur.

-    {{PropertyData/de|Up Slab Thickness|Length}}: Die Dicke der oberen Bodenplatte.

-    {{PropertyData/de|Winders|Enumeration}}: Die art der Wendelung. Nicht implementiert.



## Einschränkungen

-   Momentan stehen nur gerade Treppen, solche mit einer halben Drehung nach rechts oder links und Podeste zur Verfügung.
-   Siehe [Beitrag im Forum](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) bezüglich Wendeltreppen
-   Siehe [Ankündigung im Forum](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564)



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Treppe kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden: 
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```

-   Erstellt ein `stairs` Objekt aus dem gegebenen `baseobj`.
-   Wenn `baseobj` nicht gegeben ist, werden `length`, `width`, `height` und `steps` verwendet, um einen Festkörper zu erstellen.

Beispiel: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Stairs/de
