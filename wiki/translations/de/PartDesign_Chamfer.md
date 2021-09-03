---
- GuiCommand:/de
   Name:PartDesign Chamfer
   Name/de:PartDesign Fase
   MenuLocation:Part Design → Apply a dress up feature (Verschönerung) → Fase
   Workbenches:[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   SeeAlso:[Verrundung](PartDesign_Fillet/de.md), [Part Fase](Part_Chamfer/de.md)
---


</div>

## Beschreibung

Dieses Werkzeug erzeugt Fasen an den ausgewählten Kanten eines Objekts. Im Projektbaum wird ein neuer separater Faseneintrag (gefolgt von einer fortlaufenden Nummer, wenn bereits Fasen im Dokument vorhanden sind) angelegt.

## Anwendung


<div class="mw-translate-fuzzy">

-   Wähle eine einzelne Kante, mehrere Kanten oder eine Fläche auf einem Objekt und starte dann das Werkzeug entweder durch Klicken auf die Schaltfläche **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Fase'''** oder über das Menü **PartDesign → Fase**. Im Fall das du eine Fläche ausgewählt hast, werden alle ihre Kanten zum Anfasen berücksichtigt.
-   Im erscheinenden [Aufgabenpaneel](Task_panel/de.md) kannst du die Fase auf 3 Arten definieren:
    -   **Gleicher Abstand**: Die Fasenkanten sind gleich weit von der Körperkante entfernt.
    -   **Zwei Abstände**: Die Abstände der Fasenkante zur Körperkante werden angegeben. Die Abstandsrichtung kann umgedreht werden. <small>(v0.19)</small> 
    -   **Abstand und Winkel**: Es wird ein Abstand von der Fasenkante zur Körperkante angegeben. Die zweite Fasenkante wird durch den Winkel der Fase definiert. Die Abstandsrichtung kann umgedreht werden. <small>(v0.19)</small> 
-   Wenn du weitere Kanten oder Flächen hinzufügen möchtest, klicke auf die **Hinzufügen** Schaltfläche und wähle Kanten und/oder Flächen aus.
-   Wenn du Kanten oder Flächen entfernen möchtest
    -   wähle entweder die Kante/Fläche in der Liste des Dialogs und drücke die **DEL** Taste. *Hinweis*: Da es mindestens eine Kante für das Formelement geben muss, kann die letzte verbleibende Kante oder Fläche in der Liste nicht entfernt werden.
    -   oder klicke auf die **Entfernen** Schaltfläche. Alle Kanten und Flächen, die zuvor ausgewählt wurden, werden violett hervorgehoben. Wähle die zu entfernende Kante oder Fläche aus.
-   Klicke auf **OK**, um zu bestätigen.
-   Bei einer Kette von Kanten, die tangential zueinander verlaufen, kann eine einzelne Kante gewählt werden; die Fase breitet sich entlang der Kette aus.
-   Um die Fase nach der Validierung der Funktion zu bearbeiten, doppelklicke entweder auf die Fasenbeschriftung im Projektbaum oder klicke mit der rechten Maustaste darauf und wähle **Fase bearbeiten**.


</div>

## PartDesign Fase vs. Part Fase 

**Die PartDesign Fase ist nicht zu verwechseln mit ihrem [Part Arbeitsbereich Gegenstück](Part_Chamfer/de.md)**. Obwohl sie das gleiche Symbol haben, sind sie nicht identisch und werden nicht auf die gleiche Weise verwendet. Der Hauptunterschied besteht darin, dass PartDesign Fase einen separaten Faseneintrag (gefolgt von einer fortlaufenden Nummer, falls bereits Fasen vorhanden sind) im Projektbaum für den aktuellen Körper erstellt. Die Part Fase wird zum Elternobjekt des Objekts, auf das sie angewendet wurde.





{{PartDesign Tools navi

}} 
