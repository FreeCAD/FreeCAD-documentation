# Basic modeling tutorial/de
---
 TutorialInfo:e
   Thema:  Einführung in die Modellierung
   Level:  Anfänger
   Time:  15 Minuten
   Autor: User:Normandc
   FCVersion: jede
   Dateien: keine
}}



## Einführung

Dieses Tutorium grundlegende Modellierung zeigt dir, wie du einen Eisenwinkel modellierst. Eine Sache, die du wissen solltest, ist, dass FreeCAD modular aufgebaut ist, und wie bei vielen anderen CAD Programmen gibt es immer mehr als eine Möglichkeit, Dinge zu tun. Wir werden hier zwei Methoden untersuchen.

Diese Anleitung wurde mit FreeCAD 0.15 geschrieben.

## Bevor wir beginnen 

Denke daran, dass FreeCAD sich noch in einem frühen Entwicklungsstadium befindet, so dass du möglicherweise nicht so produktiv bist wie mit einer anderen CAD Anwendung, und du wirst sicherlich auf Fehler stoßen oder Abstürze erleben. FreeCAD hat nun die Möglichkeit, Sicherungsdateien zu speichern. Die Anzahl dieser Sicherungsdateien kann im Einstellungsdialog festgelegt werden. Zögere nicht, 2 oder 3 Sicherungsdateien zuzulassen, bis du weisst, wie man mit FreeCAD umgeht.

Speichere deine Arbeit häufig, von Zeit zu Zeit unter einem anderen Namen, damit du auf eine \"sichere\" Kopie zurückgreifen kannst, und sei auf die Möglichkeit vorbereitet, dass einige Befehle nicht die erwarteten Ergebnisse liefern könnten.

## Einführung Modellierungstechniken 

Die erste  Technik der Volumenmodellierung ist Konstruktive Festkörpergeometrie . Es gibt auch eine detaillierte Erklärung  von Konstruktive Volumenkörpergeometrie im Wiki. Du arbeitest mit Grundformen wie Würfeln, Zylindern, Kugeln und Kegeln, um deine Geometrie zu konstruieren, indem du sie kombinierst, eine Form von der anderen subtrahierst oder sie schneidest. Diese Werkzeuge sind Teil des Part Arbeitsbereichs. Du kannst auch Transformationen auf Formen anwenden, wie z. B. das Anwenden von Rundungen oder Fasen an Kanten. Diese Werkzeuge sind ebenfalls in der  Part Arbeitsbereich enthalten.

Dann gibt es fortgeschrittenere Werkzeuge. Du beginnst, indem du ein 2D Profil zeichnest, das du entweder extrudierst oder drehst.

Beginnen wir also damit, dass wir versuchen, mit diesen 2 Methoden einige eiserne Füße für einen Tisch zu machen.

## 1. Methode - Durch konstruktive Festkörpergeometrie 

1.  Beginne mit dem Part Arbeitsbereich !.
2.  Wenn du kein neues FreeCAD Dokument geöffnet hast , klicke im Aufklappmenü auf **Datei , Neu** oder klicke auf das !{width="24"} **Neu**-Symbol.
3.  Klicke auf die !{width="32"} Kasten Schaltfläche zum Erstellen eines Kastens
4.  Ändere seine Abmessungen, indem du ihn entweder im 3D Raum auswählst oder indem du ihn auf dem Projektreiter links anklickst, dann
5.  Klicke unten auf den Datenreiter und ändere die Werte für Länge, Breite und Höhe auf 50 mm, 50 und 750 *Hinweis*\': *Damals, als diese Aufnahmen gemacht wurden, waren die Eigenschaften anders angeordnet, wobei die Höhe an erster Stelle stand*.
6.  Der Kasten füllt jetzt den größten Teil der 3D Ansicht aus. Klicke auf !{width="32"} Fit All , um die Ansicht an den neu erstellte Kasten anzupassen.
7.  Erstelle einen zweiten Kasten auf die gleiche Weise, aber mit den Werten L=40, B=40 und H=750 mm. Standardmäßig wird dieser Kasten dem ersten Kasten überlagert. **
8.  Du wirst nun den zweiten Kasten vom ersten subtrahieren. Wähle zuerst die erste Form , dann die zweite Form , die Reihenfolge der Auswahl ist wichtig!  entweder auf **CAD** oder auf **Blender**).
9.  Auf der Part Arbeitsbereichswerkzeugleiste klicke auf das !{width="32"} Schnitt Werkzeug.

!Abb. 1.1 Der erste Kasten

!Abb. 1.2 Der zweite Kasten über dem ersten Kasten, bereit zur Subtraktion

!Abb. 1.3 Nach dem Ausschneiden

Du hast jetzt deinen ersten Eisenwinkel **. Du wirst feststellen, dass im Projektreiter auf der linken Seite beide Kästchen durch ein \"Cut\"  Objekt ersetzt wurden. Eigentlich sind sie nicht verschwunden, sondern unter dem \"Cut\"  Objekt gruppiert. Klicke auf die **+** Schaltfläche davor, und du wirst sehen, dass beide Kästchen immer noch da sind, aber ausgegraut **. Wenn du auf eines der beiden Kästchen klickst und die **Leertaste** drückst, wird es angezeigt. Die Leertaste schaltet Sichtbarkeit der ausgewählten Objekte um. **

Willst du nicht, dass der Winkel so ausgerichtet wird? Du musst nur die Platzierung der Box001-Form ändern. Wähle sie aus, blende sie ein, und im Datenreiter klicke auf das **+** vor Platzierung, erweitere dann den Positionsparameter und ändere seine X und Y Koordinaten. Drücke auf **Enter**, blende die Form Box001 wieder aus, und dein Winkelausrichtung ist jetzt anders. ** Du kannst sogar die Abmessungen einer deiner Formen ändern, und das Schnittobjekt wird aktualisiert.

!Abb. 1.4 Der Schneidevorgang behält seine ursprünglichen Objekte  bei bei")

!Abb. 1.5 Du kannst die Originalkästen weiterhin sichtbar machen

Übrigens können wir unter Verwendung des !{width="32"} Verrundung Werkzeugs Rundungen zum Winkel hinzufügen, damit er realistischer wird **

!Abb. 1.6 Die abgerundeten Kanten

## 2. Methode - Durch Extrudieren eines Profils 

Diese Methode erfordert, dass du mit dem Zeichnen eines 2D Profils beginnst. Dazu musst du den Entwurf Arbeitsbereich aktivieren. !.

1.  Wenn du kein neues FreeCAD Dokument geöffnet hast , klicke im Aufklappmenü auf **Datei , Neu** oder klicke auf das !{width="24"} **Neu**-Symbol.

### Setzen der Arbeitsebene 

Zuerst müssen wir festlegen, auf welcher Arbeitsebene wir unsere Profile entwerfen.

1.  Finde die unten gezeigte Symbolleiste. Abhängig von Deinen Draft-Voreinstellungen kann es unter der Hauptleiste, bzw. links oder rechts daneben sein.

    :   !
2.  Drücke den **Auto**-Button 
3.  Abhängig von Deinen Draft-Voreinstellungen öffnet das einen **Ebene auswählen**-Dialog im seitlichen Aufgaben-Panel oder eine horizontale Werkzeugleiste mit der Bezeichnung \"aktiver Befehl: **Ebene wählen**\".
4.  Wir lassen den Wert der *Offset*-Eigenschaft bei Null.
5.  Drücke den **XY**-Button, um die Arbeitsebene auf XY zu setzen. Dies schließt das Aufgaben-Panel oder die ausgeklappten Buttons. Der \"Auto\"-Button trägt nun die Bezeichnung \"Top\", um dies als die aktive Arbeitsebene anzuzeigen.

### Entwerfen des Profils 

1.  Wähle das !{width="32"} EDraht  Werkzeug.
2.  Aktiviere die \"Relativ\" und \"Gefüllt\" Kästchen.
3.  Anstatt die Form in der 3D Ansicht zu zeichnen, werden wir die Koordinaten in die *Globales X*-, *Globales Y*- und *Globales Z*-Eingabefelder eintragen. Das funktioniert wie folgt:
    1.  Klicke in das *Globales X* Eingabefeld;
    2.  Gibt einen Wert wie in der folgenden Liste aufgeführt ein und drücke **Tab**, um in das *Globales Y* Feld zu wechseln;
    3.  Gib den *Globales Y* Wert ein und drücke **Tab**, um in das *Globales Z* Feld zu wechseln;
    4.  Belasse den Nullwert im *Globales Z* Feld und drücke **Enter**, um die Koordinaten des Punktes zu validieren;
    5.  Wiederhole das für die nächsten fünf Punkte.
        -   **Koordinaten** 
        -   1\. Punkt: 0, 0, 0
        -   2\. Punkt: 50, 0, 0
        -   3\. Punkt: 0,10, 0
        -   4\. Punkt: -40, 0, 0 **Anmerkung:** *In FreeCAD 0.16 gibt es einen Fehler, der den vorigen Punkt entfernt, wenn das Minuszeichen ins Eingabefeld eingetragen wird. Eine Übergangslösung ist, einen positiven Wert einzugeben, dann den Cursor vor die Zahl zu setzen und das Minuszeichen zu tippen *
        -   5\. Punkt: 0, 40, 0
        -   6\. Punkt: -10, 0, 0
        -   Drücke die **Schließen** Taste, um das Profil zu schließen. Du solltest jetzt dieses Profil mit dem Titel **DWire** im Modellreiter haben:

!Abb. 1.7 Der Basislinienzug

Drücke die **0**  Taste auf der Zifferntastatur, um die Ansicht auf axonometrisch einzustellen.

### Extrudieren des Profils 

Aktiviere den !{width="32"} Part Arbeitsbereich entweder über die Arbeitsbereichswähler oder über **Std View Menu/de   Ansicht , Arbeitsbereich , Part**{: mediawiki} Menü.

Klicke auf das **Image:Part_Extrude.svg   32px Part_Extrude/de**{: mediawiki} Werkzeug.

Wähle auf dem Aufgabenreiter auf der linken Seite das Objekt **Draht** aus. Gib dann die gewünschte Länge ein, sagen wir 750 mm. Lasse die Richtung bei Z = 1. Drücke **OK**. Du solltest jetzt ein **Extrudieren** Objekt im Modellreiter ** haben.

!Abb. 1.8 Die extrudierte Skizze

Diese Methode hat einen kleinen Nachteil gegenüber der ersten Methode: Um die Form oder die Maße des Objekts zu ändern, muss die Skizze geändert werden, was mit einem größeren Aufwand verbunden ist als eine Änderung bei der ersten Methode.

Und es gibt noch ein paar andere Möglichkeiten, dies zu tun! Ich hoffe, dass dir diese beiden Beispiele den Einstieg erleichtern. Auf dem Weg dorthin wirst du sicher auf einige Schwierigkeiten stoßen , aber zögere nicht, Fragen im FreeCAD-Forum zu stellen!

### Anmerkung zur schaltfläche Entwurf Arbeitsebene 

Die Beschriftung deiner Schaltfläche kann unterschiedlich sein, je nach deiner Version und auch abhängig davon, was du vorher gemacht hast. Die Beschriftung der Schaltfläche könnte lauten: \"Oben\", \"Vorne\", \"Seite\", \"Keine\" oder eine Vektordarstellung wie d. Sie kann auch leer sein. Zum Beispiel:

!Ebene Keine auswählen

!Ebene oben auswählen

!Select Plane View  Nach Drücken des Buttons werden die Optionen abhängig von den Voreinstellungen wie folgt ausgeklappt:

!**Ebene wählen** Parameter wie im Ausgaben-Panel-Modus oder !**Ebene wählen** Parameter wie im Werkzeugleisten-Modus 

Die obigen Anweisungen werden funktionieren, unabhängig von der Beschriftung Deines Buttons.


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Basic modeling tutorial/de
