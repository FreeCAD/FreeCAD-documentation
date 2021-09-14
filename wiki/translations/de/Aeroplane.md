# Aeroplane/de

 {{TutorialInfo/de
|Topic=Part Arbeitsbereich
|Level=Anfänger
|Time=10 Minuten
|Author=Hughthecat
|FCVersion=
|Files=
}}

## Erste Schritte 

Wir werden im <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md) arbeiten - wähle ihn aus den Menüs über {{MenuCommand/de|Ansicht → Arbeitsbereich → Part}} oder über den [ Arbeitsbereichwähler](Workbench_Selector/de.md).

-   Erstelle ein neues leeres Dokument.
-   Wechsle zur <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [isometrischen Ansicht](Std_ViewIsometric/de.md).
-   Schalte das Achsenkreuz ein **ON** (über Ansichtsmenü).
-   Stelle sicher, dass du die [Combo Ansicht](Combo_view/de.md) hast, die (über **Ansicht → Ansichten**) anzeigt.

-   Erstelle einen Zylinder, durch Klicken auf die <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Zylinder](Part_Cylinder/de.md) Schaltfläche.
-   Wähle es aus, durch Klicken auf Zylinder in der Projektansicht.
-   Klicke auf den Datenreiter in der Projektansicht.

Ändere die Höhe auf 20 mm und den Radius auf 2 mm.

Klicke auf [Platzierung](Placement/de.md) (beachte das kleine **[+]**) und eine Schaltfläche mit drei Punkten erscheint **...**. Klicke darauf. (Du kannst auch wählen: **Menü → Bearbeiten → Platzierung**) Die Aufgabenanzeige erscheint.

<img alt="" src=images/HTCaeroplane01.png  style="width:300px;">

Wenn du mit den XYZ Achsen nicht vertraut bist, dann spiele mit den Zahlen im Übersetzungsfeld. Wenn die Wiedergabe beendet ist, klicke auf die **Reset** Schaltfläche.

## Weitere Schritte 

<img alt="" src=images/HTCaeroplane02.png  style="width:400px;">

Wir werden den Zylinder nun so drehen, dass er auf der X Achse liegt. Dazu muss er um die Y Achse gedreht werden. Im Feld Drehung sollte \"Drehachse mit Winkel\" stehen. Ändere also die Achse auf Y und erhöhe den Winkel, bis er 90 erreicht. Klicke auf **OK**.

Ich spiele an dieser Stelle gerne (und oft!) mit dem Drehen der Ansicht, also tue das unbedingt. Du solltest die \'Naht\' des Zylinders auf der Unterseite finden.

<img alt="" src=images/HTCaeroplane03.png  style="width:400px;">

Wir werden nun einen Quader hinzufügen und verändern, also klicke auf die Schaltfläche <img alt="" src=images/Part_Box.png  style="width:32px;">[Quader](Part_Box/de.md). Wähle ihn durch anklicken des Quaders in der Projektansicht aus. Ändere die Höhe auf 1 mm, die Länge auf 5 mm und die Breite auf 20 mm.

Klicke auf [Platzierung → **...**](Placement/de.md), um die Aufgabenansicht zu bekommen. Gib in das Übersetzungsfeld Y: -10 und Z: -1 ein. Klicke auf **OK**

Wir werden diese beiden Formen nun mit einer Booleschen Operation zusammenführen. Klicke auf die <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolesche Operation](Part_Boolean.md) Schaltfläche und der Aufgabenbetrachter zeigt den Auswahlschalter für Boolesche Operationen an.

Stelle sicher, dass Vereinigung ausgewählt ist und dass der Zylinder und der Quader in den beiden Formlisten jeweils einmal angekreuzt sind. Klicke auf **Anwenden**. Klicke auf **Schließen**. Du hast nun ein einzelnes Objekt mit dem Namen **Fusion(Verschmelzung)**.




Lass uns noch einen weiteren Quader einfügen, um das Modell zu vervollständigen. Erstellen Sie wie zuvor einen Würfel, wählen Sie ihn im Modellbaum aus und ändern Sie die Höhe in 5 mm, die Länge in 3 mm und die Weite in 1 mm. Zusätzlich muss der neue Quader um -0.5 mm in Y-Richtung verschoben werden.

Wir müssen jetzt unsere Fusion (Verschmelzung) zu Box001 zusammenfügen, also werden wir es auf dem schnellen Weg machen. Klicke im Projektbetrachter auf Fusion und **Strg**+klicke auf Box001. Dadurch werden beide Teile zusammen ausgewählt. Klicke nun auf das <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Verschmelzen](Part_Fuse/de.md) Schaltfläche, um **Fusion001** zu erhalten.

Du solltest jetzt ein einfaches Flugzeugmodell haben. Rechtsklicke auf **Fusion001** und benenne es in **Flugzeug** um.

<img alt="" src=images/HTCaeroplane04.png  style="width:500px;">

Meiner Ansicht nach müssen die Flügel noch etwas weiter nach vorne verschoben werden. Beim Auswählen des Flugzeugs und ändern der X-Koordinate verschiebt sich jedoch das ganze Objekt.

Erweitere Flugzeug (klicke auf die Schaltfläche **[+]** neben dem Flugzeug) und erweitere Fusion (Verschmelzung).

Klicke auf Kasten und erhalte deren [Positionierung in Aufgaben](Placement/de.md). Beachte, dass es bereits Y: -10 und Z: -1 in der Übersetzung hat. Ändere die X Übersetzung in 3 und klicke auf **Anwenden**. So ist es besser. Klicke auf **OK**.




## Drehungen

Klicke auf Flugzeug und rufe dessen [Positionierung in Aufgaben](Placement/de.md) auf. Ändere im Abschnitt Rotation den Eintrag \'Rotationsachse mit Winkel\' in \'Euler Winkel\', da diese wesentlich einfacher zu handhaben sind.

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Gierung** ist die Drehung um die **Z-Achse**, also eine Drehung von links nach rechts (der Gierungswinkel ist der Winkel **Psi ψ**).  ![](images/Tache_Placement_Tangage_fr_Mini.gif )**Steigung** ist die Drehung um die **Y-Achse**, also nach oben und nach unten (der Steigungswinkel ist der Winkel **Phi φ**).  ![](images/Tache_Placement_Roulis_fr_Mini.gif )**Roll** ist die Drehung um die **X-Achse**, also das Absenken eines Flügels und gleichzeitiges Erhöhen des anderen Flügels (der Rollwinkel ist der Winkel **Thêta θ**). 

Es gibt jedoch auch hier einige wichtige Sachen, die man in Erinnerung behalten sollte:

-   Positive Drehungen sind im Uhrzeigersinn, wenn man vom Koordinatenursprung in Richtung einer positiven Achse blickt. Oder anders ausgedrückt: Positive Drehungen sind gegen den Uhrzeigersinn, wenn man von der positiven Achse auf den Koordinatenursprung blickt.

-   Obwohl die drei Bezeichnungen Gierung, Nicken und Rollen sind, stimmt das nicht wirklich. Gierung, Nicken und Rollen sind Referenzen zu den \"Körperkoordinaten\" eines Objekts im 3D Raum. Die Bezeichnungen sollten Kurs, Höhe und Kurvenlage sein oder sogar Drehwinkel, Neigung und Querneigung, weil sie sich tatsächlich auf die \"Raumkoordinaten\" des 3D sSystem beziehen. Dies sind die \"Tait-Bryan Winkel\". Wenn du weitere Informationen wünschst, versuche [1](https://de.wikipedia.org/wiki/Eulersche_Winkel) bzw. [2](https://de.wikipedia.org/wiki/Roll-Nick-Gier-Winkel).

-   Bei dem Flugzeug in seiner gegenwärtigen Position gelten einfache Regeln. Gierung ist die Rotation um die Z-Achse, also links und rechts. Nicken ist Rotation um die Y-Achse, also Nase hoch und runter. Rollen ist Rotation um die X-Achse, also Flügel auf und ab. Das stimmt für den Anfang, aber später ist das nicht mehr zutreffend!

Spielen Sie ein wenig mit den YPR-Zahlen. Sie brauchen die Werte nur um ein paar Grad zu ändern, um ein Gefühl dafür zu bekommen. Setzen Sie sie zurück, wenn Sie fertig sind.

Jetzt werden wir sehen, warum die Gieren-Nicken-Rollen-Bezeichnungen nicht wirklich zutreffen. Ändern Sie den Rollen-Wert auf 90°. Gieren sollte die Nase des Flugzeugs hoch und runter bewegen und Nicken sollte es hin und her bewegen \"von außerhalb des Flugzeugs gesehen\", was uns Position betrifft. Stimmt das? Nein! Nicken ändert das Gieren und Gieren ändert das Nicken. Ok, zurücksetzen.

Eine bessere Beschreibung von Rotationen ist, dass Gieren Ihre geografische Länge (longitude) verändert, Nicken Ihre geografische Breite (latitude) und Rollen die Richtung (Nord, Süd, Ost, West), in die Sie fliegen. Oder Sie lesen [Axes conventions](http://en.wikipedia.org/wiki/Axes_conventions) (en) für weitere Beschreibungen.

Ok, zurück zum Thema. Änder Gieren auf 45° und Nicken auf -30°. Klicke auf OK zur Ausführung der Operation. Gehe zurück zur [Positionierungsaufgabe](Placement/de.md) und schaue auf die Rotationsbox. Sie ist zurückgekehrt zu \'Rotationsachse mit Winkel\' und zeigt einige merkwürdige Achsen- und Winkelwerte. Meine hatte Achsenwerte: (0.219493,-0.529904,0.819161) und Winkel: 53.65°. Die drei Werte in Klammern sind die XYZ Komponenten eines Einheitenvektors im 3D Raum. Das ist die Achse, um die unser ursprüngliches Flugzeug zu unserem endgültigen Flugzeug gedreht wurde. Der Winkel gibt an, wie sehr es gedreht wurde. Clever, hm, aber nicht sehr nett! Es war Euler, der zeigte, dass man eine Reihe von XYZ Drehungen zu einer Drehung um eine Achse kombinieren kann.

Hier gibt es weitere Vorschläge für das Spielen mit dem Flugzeug:

-   Ändere die Z Lage (und Anwenden) dann ändere die YPR Nummern, um schau was die Auswirkung ist. Versuche dann, die X und Y Positionen zu ändern und zu rotieren.
-   Ändere das X Zentrum (und Anwenden), ändere dann die YPR Nummern und schau, was die Auswirkung ist. Versuche dann, die Y und Z Zentren zu ändern und zu rotieren.

Ich hoffe, dass dieses kleine Tutorial dir geholfen hat, ein Gefühl für Rotationen zu bekommen.


{{Tutorials navi

}}  
