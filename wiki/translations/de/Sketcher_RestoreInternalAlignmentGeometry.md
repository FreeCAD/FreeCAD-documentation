---
- GuiCommand:
   Name:Sketcher RestoreInternalAlignmentGeometry
   MenuLocation:Sketch → Sketcher tools → Show/hide internal geometry
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:Ctrl+Shift+E
   SeeAlso:[Sketcher Ellipse](Sketcher_CreateEllipseByCenter.md), [Sketcher Internal Alignment Constraint](Sketcher_ConstrainInternalAlignment.md)
---

## Beschreibung

Der Befehl löscht unbenutzte Elemente, die an der Innengeometrie ausgerichtet sind, oder erstellt die fehlenden Elemente neu.


<div class="mw-translate-fuzzy">

## Kurzanleitung


</div>


<div class="mw-translate-fuzzy">

-   Wähle ein Element einer Skizze aus, das die innenliegende Ausrichtung unterstützt (derzeit nur Ellipse/Bogen und B-Spline).
-   Rufe den Befehl auf, indem du auf eine Schaltfläche in der Symbolleiste klickst, den Menübefehl auswählst oder die Tastenkombination verwendest.

Sind für das ausgewählte Element freie Ausrichtungsplätze vorhanden, wird eine neue Konstruktionsgeometrie erstellt und an den verfügbaren Stellen ausgerichtet. Sind alle Ausrichtungsplätze belegt, wird die unbenutzte Innengeometrie gelöscht (das Element wird als unbenutzt behandelt, wenn es an nichts anderes gebunden ist).


</div>

## Beispiel


<div class="mw-translate-fuzzy">

Erstelle eine neue Ellipse. Neue Ellipsen sind immer vollgepackt. Du siehst eine Ellipse und eine Reihe von Konstruktionsgeometrien: Hauptdurchmesser, Nebendurchmesser, Brennpunkte.


</div>





{{Sketcher Tools navi

}}  
