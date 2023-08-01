---
- GuiCommand:
   Name: Arch Nest
   Name/de: Arch Verschachteln
   MenuLocation: Arch - Tafelwerkzeuge - Verschachteln
   Workbenches: [Arch](Arch_Workbench/de.md)
   SeeAlso: [Arch Tafel](Arch_Panel/de.md), [Arch Tafelplatte](Arch_Panel_Sheet/de.md)
---

# Arch Nest/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das **<img src="images/Arch_Nest.svg" width=16px> [Arch Verschachteln](Arch_Nest/de.md)** Werkzeug ermöglicht die Auswahl einer flachen Form als Behälter und einer Reihe anderer flacher Formen, die innerhalb des durch die Behälterform definierten Raums organisiert werden sollen. Dies ist in der Regel für CNC Bearbeitungen erforderlich, bei denen du eine Reihe von Teilen aus einer Grundplatte ausschneiden möchtest und diese Teile so kompakt wie möglich organisieren musst, damit sie weniger Platz auf der Platte einnehmen.


</div>

Der Algorithmus hinter dem Verschachtelungswerkzeug befindet sich in ständiger Entwicklung und ist derzeit noch nicht vollständig optimiert. In der Zukunft sollte die Leistung dieses Werkzeugs viel besser werden.

<img alt="" src=images/Arch_Nest_example.jpg  style="width:600px;">

*Das obige Bild zeigt eine Reihe von Formen vor und nach dem Verschachtelungsvorgang.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Arch_Nest.svg" width=16px> [Arch Verschachteln](Arch_Nest/de.md)** Schaltfläche.
2.  Wähle ein Objekt aus, das der Behälter sein soll. Dieses Objekt muss flach und im Moment rechteckig sein.
3.  Klicke auf die **Greife Behälter** Schaltfläche, um dieses Objekt als Container zu verwenden.
4.  Wähle eine Reihe anderer flacher Objekte, die du im Behälter platzieren möchtest. Diese Objekte müssen alle flach sein und sich in derselben Ebene wie der Behälter befinden.
5.  Stelle die gewünschten Optionen unten ein.
6.  Starte den Berechnungsvorgang.
7.  Klicke am Ende der Berechnung auf die **Vorschau** Schaltfläche, um eine temporäre Ergebnisvorschau zu erhalten.
8.  Wenn du das Ergebnis anwenden möchtest (Verschiebe und Drehe die tatsächlichen Formen an ihren Platz), klicke auf **OK**.


</div>

<img alt="" src=images/Arch_Nest_panel.jpg  style="width:800px;"> 
*Aufgabenansichtspaneel für das [Arch Verschachteln](Arch_Nest/de.md) Werkzeug*

## Hinweise

-   Alle Objekte müssen eine Fläche haben
-   Im Moment arbeitet das Werkzeug nur mit flachen Objekten, die alle die gleiche Ausrichtung haben.
-   Im Moment muss der Behälter rechteckig sein.
-   Im Moment ist der Rand/Abstand zwischen den Teilen noch nicht implementiert.
-   Die Berechnung kann bei vielen Objekten sehr viel Zeit in Anspruch nehmen. Das wird in Zukunft optimiert werden.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Nest/de
