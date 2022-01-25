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

## Beschreibung

Das [Treppen](Arch_Stairs/de.md) Werkzeug ermöglicht dir automatisch verschiedene Treppentypen zu erstellen. Aktuell werden nur gerade Treppen (mit und ohne mittiges Treppenpodest) unterstützt. Treppen können von Grund auf neu gebaut werden, oder aus einer geraden [Linie](Draft_Line/de.md), in diesem Fall folgt die Treppe der Linie. Wenn die Linie nicht horizontal ist, sondern eine vertikale Neigung hat, folgt die Treppe ebenfalls ihrer Neigung.

Siehe den [Wikipediaeintrag](http://de.wikipedia.org/wiki/Treppe) für eine Erläuterung der verschiedenen verwendeten Begriffe zum beschreiben der Treppenbauteile.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;"> 
*Zwei konstruierte Treppen, eine mit massiver Struktur und Absatz  und eine mit einer mittigen Treppenwange.*

## Optionen

-   Treppen haben die gleichen Eigenschaften und verhalten sich wie alle anderen [Arch-Komponenten](Arch_Component/de.md)

## Anwendung

1.  Auf den **<img src="images/Arch_Stairs.png" width=16px> [Treppe](Arch_Stairs/de.md)**-Button klicken oder Tasten **S** **R** drücken.
2.  Gewünschte Werte anpassen. Einige Bauteile der Treppe, wie der Treppenlauf, sind nicht sofort sichtbar, wenn Eingaben dies unmöglich machen (Treppenlaufdicke = 0).

## Eigenschaften

Basis

-    **Ausrichtung**: Die Ausrichtung der Treppe zur Basislinie, wenn diese vorhanden ist.

-    **Basis**: Die Basislinie der Treppe, wenn vorhanden.

-    **Höhe**: Die Gesamthöhe der Treppe, wenn nicht aufbauend auf einer Basisline, oder wenn die Basislinie horizontal ist.

-    **Länge**: Die Gesamtlänge der Treppe, wenn keine Basislinie definiert ist.

-    **Breite**: Die Breite der Treppe.

Stufen

-    **Überstand**: Überstand des Auftritts gegenüber der darunterliegenden Setzstufe.

-    **Stufenanzahl**: Die Anzahl der Treppenstufen (Setzstufen) der Treppe.

-    **Setzstufenhöe**: Die Höhe der Setzstufe.

-    **Auftrittsbreite**: Die Breite des Auftritts.

-    **Stufendicke**: Die Dicke der Stufen.

Treppenlauf

-    **Podeste**: Typ des Treppenpodestes.

-    **Wangenversatz**: Der Versatz zwischen Treppenrand und Treppenwange.

-    **Wangenbreite**: Breite der Treppenwange.

-    **Lauf**: Typ des Treppenlaufs.

-    **Laufdicke**: Die Höhe des Treppenlaufs.

-    **Windung**: Die Art der Treppenwindung.

## Begrenzungen

-   Momentan werden nur gerade Treppen unterstützt
-   Für runde Treppen siehe [Forum Eintrag](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534)
-   Siehe auch [Ankündigung im Forum](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564)

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Raum Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole mit der folgenden Funktion verwendet werden: 
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
