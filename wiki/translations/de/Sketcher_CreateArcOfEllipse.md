---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/de: Sketcher EllipsenbogenErstellen
   MenuLocation: Skizze , Skizzengeometrien , Ellipsenbogen erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/de
---

# Sketcher CreateArcOfEllipse/de



## Beschreibung

Das Werkzzeug <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:24px;"> [Ellipsenbogen erstellen](Sketcher_CreateArcOfEllipse/de.md) erstellt einen Ellipsenbogen.

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Ellipsenbogen (weiß) mit interner Geometrie (dunkelgelb)*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Ellipsenbogen erstellen](Sketcher_CreateArcOfEllipse/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> Ellipsenbogen erstellen** auswählen.
    -   Das Tastaturkürzel **G** dann **E** dann **A**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Den Mittelpunkt des Bogens auswählen.
4.  Einen Endpunkt einer der Achsen auswählen; dies legt auch einen der Radien fest.
5.  Den Startpunkt des Bogens auswählen; dies legt auch den anderen Radius des Bogens fest.
6.  Den Endpunkt des Bogens auswählen.
7.  Der Ellipsenbogen wird erstellt inklusive der internen Geometrie (Hauptachse, Nebenachse und zwei Fokus-Punkte).
8.  Läuft das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md):
    1.  Wahlweise weitere Kreise erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Die Elemente der internen Geometrie können gelöscht werden. Sie können jederzeit mit [Sketcher RestoreInterna/delInterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry.md) wiederhergestellt werden.
-   Einmal erstellt, sind Haupt- und Nebenachse eines Ellipsenbogens fest zugeordnet und können nicht durch Ändern der Längen getauscht werden. Dies ist eine Folge der Parametrisierung des Gleichungslösers und des gleichen strengen Verhaltens von [OpenCASCADE](OpenCASCADE/de.md). Ein Ellipsenbogen muss gedreht werden, um die Achsen zu tauschen.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/de
