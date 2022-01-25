# Basic modeling tutorial/de
---
- TutorialInfo:/de
   Thema: Einführung in die Modellierung
   Level: Anfänger
   Time: 15 Minuten
   Autor:[NormandC](User_Normandc.md)
   FCVersion:jede
   Dateien:keine
}}

## Einführung

Dieses Tutorium grundlegende Modellierung zeigt dir, wie du einen Eisenwinkel modellierst. Eine Sache, die du wissen solltest, ist, dass FreeCAD modular aufgebaut ist, und wie bei vielen anderen CAD Programmen gibt es immer mehr als eine Möglichkeit, Dinge zu tun. Wir werden hier zwei Methoden untersuchen.

## Bevor wir beginnen 

Denke daran, dass FreeCAD sich noch in einem frühen Entwicklungsstadium befindet, so dass du möglicherweise nicht so produktiv bist wie mit einer anderen CAD Anwendung, und du wirst sicherlich auf Fehler stoßen oder Abstürze erleben. FreeCAD hat nun die Möglichkeit, Sicherungsdateien zu speichern. Die Anzahl dieser Sicherungsdateien kann im Einstellungsdialog festgelegt werden. Zögere nicht, 2 oder 3 Sicherungsdateien zuzulassen, bis du weisst, wie man mit FreeCAD umgeht.

Speichere deine Arbeit häufig, von Zeit zu Zeit unter einem anderen Namen, damit du auf eine \"sichere\" Kopie zurückgreifen kannst, und sei auf die Möglichkeit vorbereitet, dass einige Befehle nicht die erwarteten Ergebnisse liefern könnten.

## Einführung Modellierungstechniken 

Die erste (und grundlegende) Technik der Volumenmodellierung ist [Konstruktive Festkörpergeometrie (CSG)](http://en.wikipedia.org/wiki/Constructive_solid_geometry). Es gibt auch eine detaillierte Erklärung (im Kontext von FreeCAD) von [Konstruktive Volumenkörpergeometrie](Constructive_solid_geometry/de.md) im Wiki. Du arbeitest mit Grundformen wie Würfeln, Zylindern, Kugeln und Kegeln, um deine Geometrie zu konstruieren, indem du sie kombinierst, eine Form von der anderen subtrahierst oder sie schneidest. Diese Werkzeuge sind Teil des [Part Arbeitsbereichs](Part_Workbench/de.md). Du kannst auch Transformationen auf Formen anwenden, wie z. B. das Anwenden von Rundungen oder Fasen an Kanten. Diese Werkzeuge sind ebenfalls in der [ Part Arbeitsbereich](Part_Workbench/de.md) enthalten.

Dann gibt es fortgeschrittenere Werkzeuge. Du beginnst, indem du ein 2D Profil zeichnest, das du entweder extrudierst oder drehst.

Beginnen wir also damit, dass wir versuchen, mit diesen 2 Methoden einige eiserne Füße für einen Tisch zu machen.

## 1. Methode - Durch konstruktive Festkörpergeometrie 

1.  Beginne mit dem [Part Arbeitsbereich](Part_Workbench/de.md) ![](images/Switch_PartWorkbench.JPG ).
2.  Wenn du kein neues FreeCAD Dokument geöffnet hast (der größte Teil des FreeCAD Fensters ist ausgegraut), klicke im Aufklappmenü auf **Datei → Neu** oder klicke auf <img alt="" src=images/Document-new.png  style="width:32px;"> **Ein neues leeres Dokument erstellen** Symbol.
3.  Klicke auf die <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Kasten](Part_Box/de.md) Schaltfläche zum Erstellen eines Kastens
4.  Ändere seine Abmessungen, indem du ihn entweder im 3D Raum auswählst oder indem du ihn auf dem Projektreiter links anklickst, dann
5.  Klicke unten auf den Datenreiter und ändere die Werte für Länge, Breite und Höhe auf 50 mm, 50 und 750 *(siehe Abb. 1.1)*\' **Hinweis**: *Damals, als diese Aufnahmen gemacht wurden, waren die Eigenschaften anders angeordnet, wobei die Höhe an erster Stelle stand*.
6.  Der Kasten füllt jetzt den größten Teil der 3D Ansicht aus. Klicke auf <img alt="" src=images/Std_ViewFitAll.svg  style="width:32px;"> [Fit All](Std_ViewFitAll/de.md) , um die Ansicht an den neu erstellte Kasten anzupassen.
7.  Erstelle einen zweiten Kasten auf die gleiche Weise, aber mit den Werten L=40, B=40 und H=750 mm. Standardmäßig wird dieser Kasten dem ersten Kasten überlagert. *(siehe Abb. 1.2)*
8.  Du wirst nun den zweiten Kasten vom ersten subtrahieren. Wähle zuerst die erste Form (genannt Box), dann die zweite Form (genannt Box001), die Reihenfolge der Auswahl ist wichtig! (Stelle sicher, dass beide Formen im Projektbaum ausgewählt sind. **Eine Sache, die du dir merken solltest:** im Inventor Navigationsmodus, **Strg** + Klick funktioniert nicht bei Mehrfachauswahl. Schalte [Maus Navigation](Mouse_navigation/de.md) entweder auf **CAD** oder auf **Blender**).
9.  Auf der Part Arbeitsbereichswerkzeugleiste klicke auf das <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Schnitt](Part_Cut/de.md) Werkzeug.

![Abb. 1.1 Der erste Kasten](images/Tutorial-normand01.jpg )

![Abb. 1.2 Der zweite Kasten über dem ersten Kasten, bereit zur Subtraktion](images/Tutorial-normand02.jpg )

![Abb. 1.3 Nach dem Ausschneiden](images/Tutorial-normand03.jpg )

Du hast jetzt deinen ersten Eisenwinkel *(Abb. 1.3)*. Du wirst feststellen, dass im Projektreiter auf der linken Seite beide Kästchen durch ein \"Cut\" (Schnitt) Objekt ersetzt wurden. Eigentlich sind sie nicht verschwunden, sondern unter dem \"Cut\" (Schnitt) Objekt gruppiert. Klicke auf die **+** Schaltfläche davor, und du wirst sehen, dass beide Kästchen immer noch da sind, aber ausgegraut *(Abb. 1.4)*. Wenn du auf eines der beiden Kästchen klickst und die **Leertaste** drückst, wird es angezeigt. Die Leertaste schaltet [Sichtbarkeit](Std_ToggleVisibility/de.md) der ausgewählten Objekte um. *(Abb. 1.5)*

Willst du nicht, dass der Winkel so ausgerichtet wird? Du musst nur die Platzierung der Box001-Form ändern. Wähle sie aus, blende sie ein, und im Datenreiter klicke auf das **+** vor Platzierung, erweitere dann den Positionsparameter und ändere seine X und Y Koordinaten. Drücke auf **Enter**, blende die Form Box001 wieder aus, und dein Winkelausrichtung ist jetzt anders. *(Abb. 1.5)* Du kannst sogar die Abmessungen einer deiner Formen ändern, und das Schnittobjekt wird aktualisiert.

![Abb. 1.4 Der Schneidevorgang behält seine ursprünglichen Objekte (die Kästen) bei](images/Tutorial-normand04.jpg )

![Abb. 1.5 Du kannst die Originalkästen weiterhin sichtbar machen](images/Tutorial-normand05.jpg )

Übrigens können wir unter Verwendung des <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Verrundung](Part_Fillet/de.md) Werkzeugs Rundungen zum Winkel hinzufügen, damit er realistischer wird 
*(Abb. 1.6)*

![Abb. 1.6 Die abgerundeten Kanten](images/Tutorial-normand06.jpg )

## 2. Methode - Durch Extrudieren eines Profils 

Diese Methode erfordert, dass du mit dem Zeichnen eines 2D Profils beginnst. Dazu musst du den [Entwurf Arbeitsbereich](Draft_Workbench/de.md) aktivieren. ![](images/Switch_DraftWorkbench.JPG ).

-   Wenn du kein neues FreeCAD Dokument geöffnet hast (der größte Teil des FreeCAD Fensters sieht ausgegraut aus), klicke im Aufklappmenü auf Datei → Neu oder klicke auf <img alt="" src=images/Document-new.png  style="width:32px;"> **Erstelle ein neues leeres Dokument** Symbol.

### Setzen der Arbeitsebene 

Zuerst müssen wir festlegen, auf welcher [Arbeitsebene](Draft_SelectPlane/de.md) wir unsere Profile entwerfen.

1.  Finde die unten gezeigte Symbolleiste. Abhängig von Deinen Draft-Voreinstellungen kann es unter der Hauptleiste, bzw. links oder rechts daneben sein.

    :   ![](images/DraftPlaneAuto.png )
2.  Drücke den **Auto**-Button (ggf. mit \"None\" bezeichnet)
3.  Abhängig von Deinen Draft-Voreinstellungen öffnet das einen **Ebene auswählen**-Dialog im seitlichen Aufgaben-Panel oder eine horizontale Werkzeugleiste mit der Bezeichnung \"aktiver Befehl: **Ebene wählen**\".
4.  Wir lassen den Wert der *Offset*-Eigenschaft bei Null.
5.  Drücke den **XY**-Button, um die Arbeitsebene auf XY zu setzen. Dies schließt das Aufgaben-Panel oder die ausgeklappten Buttons. Der \"Auto\"-Button trägt nun die Bezeichnung \"Top\", um dies als die aktive Arbeitsebene anzuzeigen.

### Entwerfen des Profils 

1.  Wähle das <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [EDraht (Mehrpunkt-Entwurfsdraht)](Draft_Wire/de.md) Werkzeug.
2.  Aktiviere die \"Relativ\" und \"Gefüllt\" Kästchen.
3.  Anstatt die Form in der 3D Ansicht zu zeichnen, werden wir die Koordinaten in die *Globales X*-, *Globales Y*- und *Globales Z*-Eingabefelder eintragen. Das funktioniert wie folgt:
    1.  Klicke in das *Globales X* Eingabefeld;
    2.  Gibt einen Wert wie in der folgenden Liste aufgeführt ein und drücke **Tab**, um in das *Globales Y* Feld zu wechseln;
    3.  Gib den *Globales Y* Wert ein und drücke **Tab**, um in das *Globales Z* Feld zu wechseln;
    4.  Belasse den Nullwert im *Globales Z* Feld und drücke **Enter**, um die Koordinaten des Punktes zu validieren;
    5.  Wiederhole das für die nächsten fünf Punkte.
        -   **Koordinaten** (X, Y, Z)
        -   1\. Punkt: 0, 0, 0
        -   2\. Punkt: 50, 0, 0
        -   3\. Punkt: 0,10, 0
        -   4\. Punkt: -40, 0, 0 **Anmerkung:** *In FreeCAD 0.16 gibt es einen Fehler, der den vorigen Punkt entfernt, wenn das Minuszeichen ins Eingabefeld eingetragen wird. Eine Übergangslösung ist, einen positiven Wert einzugeben, dann den Cursor vor die Zahl zu setzen und das Minuszeichen zu tippen (dieser Fehler ist in v0.17 behoben)*
        -   5\. Punkt: 0, 40, 0
        -   6\. Punkt: -10, 0, 0
        -   Drücke die **Schließen** Taste, um das Profil zu schließen. Du solltest jetzt dieses Profil mit dem Titel **DWire** im Modellreiter haben:

![Abb. 1.7 Der Basislinienzug](images/Tutorial-normand07.jpg )

Drücke die **0** (Null) Taste auf der Zifferntastatur, um die Ansicht auf axonometrisch einzustellen.

### Extrudieren des Profils 

Aktiviere den <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part Arbeitsbereich](Part_Workbench/de.md) entweder über die [Arbeitsbereichswähler](Std_Workbench/de.md) oder über **[[Std View Menu/de   Ansicht]] → Arbeitsbereich → Part** Menü.

Klicke auf das **![](images/)**_Werkzeug.

Wähle auf dem Aufgabenreiter auf der linken Seite das Objekt **Draht** aus. Gib dann die gewünschte Länge ein, sagen wir 750 mm. Lasse die Richtung bei Z = 1. Drücke **OK**. Du solltest jetzt ein **Extrudieren** Objekt im Modellreiter *(Abb. 1.8)* haben.

![Abb. 1.8 Die extrudierte Skizze](images/Tutorial-normand08.jpg )

Diese Methode hat einen kleinen Nachteil gegenüber der ersten Methode: Um die Form oder die Maße des Objekts zu ändern, muss die Skizze geändert werden, was mit einem größeren Aufwand verbunden ist als eine Änderung bei der ersten Methode.

Und es gibt noch ein paar andere Möglichkeiten, dies zu tun! Ich hoffe, dass dir diese beiden Beispiele den Einstieg erleichtern. Auf dem Weg dorthin wirst du sicher auf einige Schwierigkeiten stoßen (das habe ich, als ich das erste Mal FreeCAD lernte, und ich habe 3D CAD Erfahrung), aber zögere nicht, Fragen im [FreeCAD-Forum](https://forum.freecadweb.org) zu stellen!

### Anmerkung zur schaltfläche Entwurf Arbeitsebene 

Die Beschriftung deiner Schaltfläche kann unterschiedlich sein, je nach deiner Version und auch abhängig davon, was du vorher gemacht hast. Die Beschriftung der Schaltfläche könnte lauten: \"Oben\", \"Vorne\", \"Seite\", \"Keine\" oder eine Vektordarstellung wie d(0.0,0.0,1.0). Sie kann auch leer sein. Zum Beispiel:

![Ebene Keine auswählen](images/DraftPlaneNone.png )

![Ebene oben auswählen](images/DraftPlaneTop.png )

![Select Plane View](images/DraftPlaneView.png )  Nach Drücken des Buttons werden die Optionen abhängig von den Voreinstellungen wie folgt ausgeklappt:

![**Ebene wählen** Parameter wie im Ausgaben-Panel-Modus](images/DraftPlaneTasks.png ) oder ![**Ebene wählen** Parameter wie im Werkzeugleisten-Modus](images/DraftPlaneToolbarMode.png ) 

Die obigen Anweisungen werden funktionieren, unabhängig von der Beschriftung Deines Buttons.


  {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Category_Part.md) > Basic modeling tutorial/de
