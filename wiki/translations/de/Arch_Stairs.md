---
- GuiCommand:/de
   Name:Arch Stairs
   Name/de:Arch Treppe
   MenuLocation:Arch → Treppe
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**S** **R**
   Version:0.14
   SeeAlso:[Arch Struktur](Arch_Structure/de.md), [Arch Ausstattung](Arch_Equipment/de.md)
---

# Arch Stairs/de

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Das [Treppen](Arch_Stairs/de.md) Werkzeug ermöglicht dir automatisch verschiedene Treppentypen zu erstellen. Aktuell werden nur gerade Treppen (mit und ohne mittiges Treppenpodest) unterstützt. Treppen können von Grund auf neu gebaut werden, oder aus einer geraden [Linie](Draft_Line/de.md), in diesem Fall folgt die Treppe der Linie. Wenn die Linie nicht horizontal ist, sondern eine vertikale Neigung hat, folgt die Treppe ebenfalls ihrer Neigung.


</div>


<div class="mw-translate-fuzzy">

Siehe den [Wikipediaeintrag](http://de.wikipedia.org/wiki/Treppe) für eine Erläuterung der verschiedenen verwendeten Begriffe zum beschreiben der Treppenbauteile.


</div>

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">



*Zwei konstruierte Treppen, eine mit massiver Struktur und Absatz  und eine mit einer mittigen Treppenwange.*


</div>



## Optionen


<div class="mw-translate-fuzzy">

-   Treppen haben die gleichen Eigenschaften und verhalten sich wie alle anderen [Arch-Komponenten](Arch_Component/de.md)


</div>

## Usage


<div class="mw-translate-fuzzy">

## Anwendung

1.  Auf den **<img src="images/Arch_Stairs.png" width=16px> [Treppe](Arch_Stairs/de.md)**-Button klicken oder Tasten **S** **R** drücken.
2.  Gewünschte Werte anpassen. Einige Bauteile der Treppe, wie der Treppenlauf, sind nicht sofort sichtbar, wenn Eingaben dies unmöglich machen (Treppenlaufdicke = 0).


</div>

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;"> 
*Complex stairs based on a selection of lines and wired as shown on the left.<br>
In red the wires used for the landings at Z&equals;1500mm, Z&equals;3000mm and Z&equals;4500mm.<br>
In black the lines connecting them used for the flights.
*



## Eigenschaften

### Data


{{TitleProperty|Segment and Parts}}

-    **Abs Top|Vector**: (read-only) The absolute top level the stairs lead to.

-    **Last Segment|Link**: Last segment (flight or landing) of an Arch Stairs connecting to this segment. The start level of the stairs will be the end level of this last segment.

-    **Outline Left|VectorList**: The left outline of the stairs.

-    **Outline Left All|VectorList**: The left outline of all segments of the stairs.

-    **Outline Right|VectorList**: The right outline of the stairs.

-    **Outline Right All|VectorList**: The right outline of all segments of the stairs.

-    **Railing Height Left|Length**: Height of the left railing of the stairs or landing.

-    **Railing Height Right|Length**: Height of the right railing of the stairs or landing.

-    **Railing Left|LinkHidden**: The left railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Offset of the left railing from the edge of the stairs or landing.

-    **Railing Offset Right|Length**: Offset of the right railing from the edge of the stairs or landing.

-    **Railing Right|LinkHidden**: The right railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.


{{TitleProperty|Stairs}}


<div class="mw-translate-fuzzy">

-    **Ausrichtung**: Die Ausrichtung der Treppe zur Basislinie, wenn diese vorhanden ist.

-    **Basis**: Die Basislinie der Treppe, wenn vorhanden.

-    **Höhe**: Die Gesamthöhe der Treppe, wenn nicht aufbauend auf einer Basisline, oder wenn die Basislinie horizontal ist.

-    **Länge**: Die Gesamtlänge der Treppe, wenn keine Basislinie definiert ist.

-    **Breite**: Die Breite der Treppe.


</div>


<div class="mw-translate-fuzzy">

Stufen


</div>


<div class="mw-translate-fuzzy">

-    **Überstand**: Überstand des Auftritts gegenüber der darunterliegenden Setzstufe.

-    **Stufenanzahl**: Die Anzahl der Treppenstufen (Setzstufen) der Treppe.

-    **Setzstufenhöe**: Die Höhe der Setzstufe.

-    **Auftrittsbreite**: Die Breite des Auftritts.

-    **Stufendicke**: Die Dicke der Stufen.


</div>


<div class="mw-translate-fuzzy">

Treppenlauf


</div>


<div class="mw-translate-fuzzy">

-    **Podeste**: Typ des Treppenpodestes.

-    **Wangenversatz**: Der Versatz zwischen Treppenrand und Treppenwange.

-    **Wangenbreite**: Breite der Treppenwange.

-    **Lauf**: Typ des Treppenlaufs.

-    **Laufdicke**: Die Höhe des Treppenlaufs.

-    **Windung**: Die Art der Treppenwindung.


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Begrenzungen

-   Momentan werden nur gerade Treppen unterstützt
-   Für runde Treppen siehe [Forum Eintrag](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534)
-   Siehe auch [Ankündigung im Forum](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Raum Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole mit der folgenden Funktion verwendet werden:


</div>


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/de
