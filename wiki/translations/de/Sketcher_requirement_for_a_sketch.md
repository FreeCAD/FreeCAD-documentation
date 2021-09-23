# Sketcher requirement for a sketch/de
{{TutorialInfo/de
|Topic=Skizze
|Level=Anfänger
|Author=[Maker](User:Maker.md)
|Time=
|FCVersion=
}}

## Mindestanforderung an eine Skizze 

Das Erzeugen eines Körpers im Arbeitsbereich PartDesign ist bereits und **nur** mit Hilfe einer geschlossenen Kurve (Profil) möglich. Die vollständige Bestimmung all ihrer Abmessungen und Eigenschaften (*vollständig beschränkt*) ist dafür noch nicht erforderlich.

Dass eine geschlossene Kurve vorliegt, ist nicht selbstverständlich und nicht erkennbar. Beim Anschluss eines Kreisbogens an eine Gerade z.B. werden die beiden Endpunkte nur übereinander liegend erstellt. Sie müssen mit dem Werkzeug <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [Deckungsgleiche](Sketcher_ConstrainCoincident/de.md) Beschränkung zu einem einzigen, Gerade und Kreisbogen tatsächlich verbindenden Punkt gemacht werden.

![](images/Skizze2a.png )


*Eine einfache Skizze. 
Links: Kurve nur an vier Stellen (rot, automatische Beschränkungen beim Zeichnen mit <img src=images/_Sketcher_CreatePolyline.svg style="width:32px"> [Polylinie](Sketcher_CreatePolyline/de.md)) geschlossen. 
Mitte: Warnung - ... gebrochene Fläche (gebrochene Kurve). 
Rechts: Kurve an den verbleibenden vier Stellen geschlossen (grün)*

Konsequentes parametrisches Arbeiten bedeutet allerdings, dass die Skizze vollständig bestimmt wird.

## Vollständiges Definieren einer Skizze 

Selbst eine noch relativ einfache Skizze kann schon Dutzende von Unbestimmtheiten (in der Combo-Ansicht als Zahl von \"Freiheitsgraden\" angegeben) enthalten. Sie erst am Ende alle gemeinsam zu beseitigen, ist eine relativ unübersichtliche Arbeit.

![](images/Skizze4a.png )


*Eine einfache Skizze; vollständig bestimmt durch 25 Beschränkungen, von denen nur 5 Bemaßungsbeschränkungen sind.*

Diese Arbeit ist übersichtlicher und einfacher, wenn man die \"Freiheiten\" jedes zugefügten geometrischen Elements sofort eliminiert, d.h. dieses *vermaßt* (also Werte für Dimensionen und Platzierungen angibt). Die jeweils vorläufige Vollständigkeit ist erreicht, wenn alle Linien grün angezeigt werden.

Wenn man bis zum Ende des Zeichnens mit dem Bestimmen abwartet, so findet man verbliebene \"Freiheiten\", indem man die Punkte und Linien mit dem Mauszeiger anfasst und feststellt, wo sie noch nicht fixiert sind. Bei endgültiger Vollständigkeit wird die gesamte Zeichnung grün angezeigt.

Stellt man versehentlich eine *Überregelung* her, erscheint eine Warnung in der Combo-Ansicht mit der Auffoderung, entsprechende Maßnahmen (constraints) rückgängig zu machen.


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher requirement for a sketch/de
