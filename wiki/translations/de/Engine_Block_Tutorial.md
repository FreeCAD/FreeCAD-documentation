---
- TutorialInfo:/de
   Topic:Part Arbeitsbereich
   Level:Anfänger
   Time:1 Stunde
   Author:Andrewbuck40
   FCVersion:0.14.3700
   Files:
}}

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:600px;">

Dies ist ein einführendes Tutorium zur Modellierung in FreeCAD. Der Zweck dieses Tutoriums ist es, dich in die primitiven Datentypen für parametrische Objekte, boolesche Operationen, 2D Zeichnen und den Prozess der Umwandlung von 2D Entwürfen in 3D Modelle einzuführen. Als Arbeitsbeispiel werden wir den einfachen Motorblock und das Kurbelgehäuse modellieren, wie oben zu sehen.

## Erste Schritte 

Öffne zunächst FreeCAD, gehe zu **Datei → Neu**, um ein neues Dokument zu erstellen, und dann **Datei → Speichern**, um es irgendwo auf Ihrem Computer zu speichern, ich habe mein Projekt **\"Engine\"** genannt. Du wirst feststellen, dass nach dem Speichern des Projekts in der *Baumansicht* auf der linken Seite des Bildschirms der Name des Projekts angezeigt wird, an dem du gerade arbeitest. Du kannst mehr als ein Projekt gleichzeitig geöffnet haben, und jedes Projekt wird als Basis eines Baumes in der Baumansicht angezeigt.

## Ausräumen des Blocks 

Beginnen wir nun mit der Arbeit am eigentlichen Modell. Wir beginnen mit dem Hinzufügen eines Kastens für den Gesamtumriss des Motorblocks. Dazu müssen wir dem Modell ein *Teil* hinzufügen, gehe zu **Ansicht → Arbeitsbereich → Part** und wähle den [Part Arbeitsbereich](Part_Workbench/de.md). Nachdem du den Arbeitsbereich ausgewählt hast, wirst du feststellen, dass du oben auf der Werkzeugleiste einen anderen Satz von Schaltflächen erhältst. Blättere durch einige der anderen Arbeitsbereiche, um sich mit dem Arbeitsbereichsystem vertraut zu machen, und kehre dann zum Part Arbeitsbereich zurück.

### Der Rohling 

Im Arbeitsbereich *Part* sind mehrere Werkzeuge für primitive Objekte wie Quader, Kugeln, Kegel, usw. zu sehen. Klicken Sie auf den Würfel (<img alt="" src=images/Part_Box.svg  style="width:16px;">), um einen Würfel in das Modell einzufügen. Jedes der primitiven Objekte hat mehrere Standardeinstellungen, die beim Einfügen festgelegt werden. Wenn Sie wollen, können Sie die verschiedenen Primitive einmal durchprobieren, um jedes einmal gesehen zu haben. Mit der Entf-Taste können die ausgewählten Objekte wieder gelöscht werden. Die Auswahl des Objekts ist dabei auf zwei verschiedene Arten möglich: Entweder durch Anklicken des Objekts in der 3D-Ansicht oder durch einen Klick auf den passenden Eintrag im Modellbaum. Bei gleichzeitig gehaltener **Strg**-Taste lassen sich auch mehrere Objekte nacheinander auswählen. Innerhalb der 3D-Ansicht lässt dich mit dem Mausrad rein- und rauszoomen. Mit der mittleren Mausaste lässt dich die Ansicht verschieben und wenn neben der mittleren Maustaste auch noch die rechte Maustaste gehalten wird, wird die Ansicht gedreht. Mit den Tasten 0-6 des Nummernpads kann zwischen verschiedenen voreingestellten Ansichten gewechselt werden (z.B. axometrisch, von oben, usw.). Investieren Sie ein paar Minuten, um sich mit der Navigation in 3D vertraut zu machen.

:   *Weiterführende Literatur: [Mausnavigation](Mouse_navigation/de.md)*

Sobald du deinen Würfel hast und mit der Funktionsweise der Maus vertraut bist, beginnen wir mit der Einrichtung der Abmessungen des CAD Modells. Wähle den *Würfel*, durch daraufklicken in der Baumansicht, und klicke dann auf den *Datenreiter\' der*Eigenschaftsansicht*, die sich unter der Baumansicht befindet (gehe zu **Ansicht → Paneele → Combo Ansicht**, wenn du diese geschlossen hast). Im \"Datenreiter\" kannst du die Eigenschaften des in der Strukturansicht ausgewählten Objekts ändern. Je nachdem, welche Art von Objekt du auswählst, gibt es verschiedene Parameter, die du im \"Datenreiter\" einstellen kannst. Für einen Kasten benötigen wir 3 Vektoren, einen für seine Position im 3D Raum, einen weiteren für seine Orientierung und einen dritten, um die Abmessungen des Kastens festzulegen. Für eine Kugel könntest du den Mittelpunkt und den Radius angeben; Kegel haben einen Radius, eine Höhe und eine Position und so weiter. Wir bauen einen kleinen 2-Zylinder Motorblock, also stelle die Größe und die Position des Kastens auf die folgenden Werte ein (stelle sicher, dass du die XYZ unter*Position*einstellst, die unter*Achse\'\' stellen die Rotationsachse ein, und die Standardwerte sind das, was wir wollen):

:   {\    class:wikitable border=1

\|- \| X: 0.0 mm \|\| Länge: 140.0 mm \|- \| Y: -40.0 mm \|\| Breite: 80.0 mm \|- \| Z: 0.0 mm \|\| Höhe: 110.0 mm \|- \|}

Jetzt, wo du deinen Motorblock richtig dimensioniert hast, sollten wir ihm einen aussagekräftigeren Namen geben. Wähle ihn in der Baumansicht aus und klicke entweder mit der rechten Maustaste, um ihn umzubenennen, oder drücke die Taste **F2** auf deiner Tastatur. Benenne dieses Teil **Billet** (engl.: Rohling).

### Der erste Zylinder 

Als nächstes werden wir den ersten Zylinder durch den gesamten Motorblock herausschneiden. Dazu fügen wir dem Modell einen Zylinder in der Größe hinzu, die wir aufbohren wollen, und führen dann eine boolesche Operation durch, um das Material vom Block zu \"subtrahieren\". Klicke auf die Schaltfläche Zylinder hinzufügen (<img alt="" src=images/Part_Cylinder.svg  style="width:16px;">), um einen neuen Zylinder zu erstellen, wähle ihn dann in der Baumansicht aus und lege seine Eigenschaften wie folgt fest:

:   {\    class:wikitable border=1

\|- \| X: 40.0 mm \|\| Höhe: 110.0 mm \|- \| Y: 0.0 mm \|\| Radius: 25.0 mm \|- \| Z: 0.0 mm \|\| \|- \|}

Sobald die Maße richtig eingegeben wurden, sollten die beiden Endflächen des Zylinders auf der Ober- und Unterseite des Blocks sichtbar sein. Benennen Sie das Objekt **Cylinder 1**.

### Der zweite Zylinder 

Der zweite Zylinder könnte auf demselben Wege erstellt werden wie der erste, es ist jedoch einfacher, den ersten zu Kopieren, da sich beide nur in der X-Koordinate unterscheiden. Um den Zylinder zu kopieren, muss er zunächst im Modellbaum ausgewählt werden und anschließend **Bearbeiten → Auswahl duplizieren** angeklickt werden. Im Modellbaum sollte nun ein zweiter Zylinder erscheinen, der in **Cylinder 2** umbenannt wird. In der 3D-Ansicht ist er noch nicht zu sehen, weil er vom ersten Zylinder überdeckt wird. Wählen Sie nun den zweiten Zylinder und änder Sie seine X-Koordinate in 100 mm. Der Zylinder sollte sich dabei automatisch in der 3D-Ansicht bewegen. Um die beiden Zylinder sichtbar zu machen, kann der Block durch Auswahl und anschließendes Drücken der Leertaste verübergehend unsichtbar gemacht werden (versteckte Objekte werden im Modellbaum in der Farbe Grau angezeigt).

### Ausbohren der Zylinder 

<img alt="" src=images/_Engine_Block_Tutorial_-_Bored_Block.png  style="width:300px;">

Nun, da beide Zylinder an ihrem Platz sind, wollen wir sie benutzen, um den Block auf die entsprechenden Maße aufzubohren. Dazu werden wir *boolesche Operationen* auf unsere 3 Grundkörper anwenden. Wir beginnen damit, dass wir aus den beiden Zylindern eine Vereinigung machen, so dass wir sie als Gruppe vom Block subtrahieren können. Wähle **Zylinder 1** in der Baumansicht und dann ***STRG**+Linksklick*, um auch **Zylinder 2** zu wählen. Drücke nun die Schaltfläche Vereinigen (<img alt="" src=images/Part_Fuse.svg  style="width:16px;">) , um die Objekte miteinander zu verschmelzen. Du wirst feststellen, dass es in der Baumansicht jetzt ein neues Objekt mit dem Namen *Fusion* gibt. Wenn du auf den Ausklapppfeil neben *Fusion* klickst, siehst du die beiden Zylinder, aber sie werden grau dargestellt. Statt \"Fusion\" benennen wir das Objekt in \"Zylinder\" um, damit es später leichter zu finden ist. Jetzt bohren wir den Motorblock auf. Wähle den **Rohling** und *dann* wähle die **Zylinder** und drücke die Schaltfläche Ausschneiden (<img alt="" src=images/Part_Cut.svg  style="width:16px;">). Die beiden ausgewählten Objekte werden wieder wie bei der Vereinigungsoperation kombiniert, und das einzelne resultierende Objekt erhält den Namen *Cut* (den du in **Gebohrter Block** umbenennen solltest). Drücke die Taste *2* auf dem Ziffernblock, und du solltest jetzt in der Lage sein, geradewegs durch die Zylinder nach unten auf die andere Seite des Motorblocks zu schauen, dann *Mittelklick+Linksklick+Ziehen*, um deinen Motorblock zu betrachten. Auf der rechten Seite siehst du, wie das fertige Produkt aussehen sollte. Beachte, dass ich die Baumansicht auf der linken Seite erweitert habe, um die einzelnen Grundkörper anzuzeigen, und dass ich **Zylinder 2** zur Untersuchung im *Daten* reiter der *Eigenschaftsansicht* ausgewählt habe.

### Der wichtigste Vorteil des parametrischen Modellierens 

Nun da die Bohrungen des Blocks fertig sind, nehmen wir uns einen Moment, um einen wichtigen Vorteil des parametrischen Modellierens zu sehen. Nehmen wir dazu an, wir würden während der Entwicklung des Produkts irgendwann zu dem Schluss kommen, dass die Zylinder etwas vergrößert werden müssen. Weil die Vereinigung der Zylinder und das Ausschneiden selbiger als Gruppierung im Modellbaum angezeigt werden, können wir die Zylindergröße auch im Nachhinein einfach variieren, wobei FreeCAD das Vereinigen und das Ausschneiden der Zylinder und letzten Endes das 3D-Modell automatisch an die Änderung anpasst. Probieren Sie dies aus, indem Sie den Radius und die Position der Zylinder variieren und dabei die Änderungen des 3D-Modells beachten. Am Ende sollten die ursprünglichen Werte jedoch wiederhergestellt werden.

## Das Kurbelgehäuse 

### Rohling und Lagerdeckel 

In diesem Abschnitt widmen wir uns nun dem Kurbelgehäuse unterhalb des Motorblocks. Fügen Sie einen neuen Würfel ein, benennen Sie ihn um in **Kurbelgehäuse Rohling** und geben Sie ihm die folgenden Eigenschaften:

:   {\    class:wikitable border=1

\|- \| X: 0.0 mm \|\| Länge: 140.0 mm \|- \| Y: -50.0 mm \|\| Breite: 100.0 mm \|- \| Z: -85.0 mm \|\| Höhe: 85.0 mm \|- \|}

Um das Kurbelgehäuse von dem anderen zu unterscheiden, geben wir einem von ihnen eine andere Farbe. Du kannst die Farbe ändern, indem du in der Baumansicht mit der rechten Maustaste auf das zu ändernde Objekt klickst. Du kannst selbst eine Farbe zuweisen oder dem Objekt eine zufällige Farbe geben (wähle wieder zufällig, wenn dir die Farbe nicht gefällt).

Füge einen weiteren Kasten mit der Bezeichnung **Lageraussparung** hinzu, gib ihm die folgenden Eigenschaften und schneide dann den **Lageraussparung** vom **Kurbelgehäuserohling** weg (d.h. wähle zuerst den Rohling aus):

:   {\    class:wikitable border=1

\|- \| X: 0.0 mm \|\| Länge: 140.0 mm \|- \| Y: -40.0 mm \|\| Breite: 80.0 mm \|- \| Z: -85.0 mm \|\| Höhe: 30.0 mm \|- \|}

Benennen Sie das resultierende *Cut* Objekt um in **Carved crankcase**.

### Herausarbeiten der Lager 

Als nächstes werden wir einen halbkreisförmigen Platz für den Sitz der Kurbelwelle und einen Freiraum im Gehäuse für die Drehung der Welle erzeugen. Wir beginnen mit einem Zylinder, wobei die Orientierung des Zylinders diesmal horizontal sein soll. Das heißt wir müssen herausfinden, wie der Zylinder entsprechend gedreht und passend zum Motorblock ausgerichtet werden kann. Ein Blick auf das Koordinatenkreuz in der unteren rechten Ecke der 3D Ansicht führt zu der Erkenntnis, dass der Zylinder in Richtung der x Achse zeigen muss. Der Zylinder muss also gegenüber seiner Standardorientierung um 90° um die y Achse gedreht werden. Erstelle einen Zylinder, nenne ihn **Crankshaft carve** und gib ihm die folgenden Eigenschaften (wichtig: anders als bisher, wird die Orientierung diesmal auch geändert!):

:   {\    class:wikitable border=1

\|- \| Achse X: 0.0 mm \|\| Winkel: 90.0 Grad \|- \| Achse Y: 1.0 mm \|\| \|- \| Achse Z: 0.0 mm \|\| \|- \| Position X: 0.0 mm \|\| Höhe: 140.0 mm \|- \| Position Y: 0.0 mm \|\| Radius: 20.0 mm \|- \| Position Z: -55.0 mm \|\| \|- \|}

Schneide das neue Objekt aus dem vorhandenen Gehäuse **Carved crankcase** aus und nenne das sich ergebende Objekt **Crankcase with journals**.

### Fertigstellen des Kurbelgehäuses 

Zuletzt werden wir 2 Endkästen ausschneiden, so dass die Kolbenstangen vom Kurbelgehäuse bis in den Motorblock reichen können. Mache zwei Objekte mit den Namen **Box carve 1** und **Box carve 2** mit den folgenden Eigenschaften; du kannst auch **Box carve 1** duplizieren und einfach die X Koordinate ändern, um den zweiten Carver zu erhalten. Vereinige sie zu einem Objekt namens **Box carvers** und schneide dieses Objekt vom **Kurbelgehäuse mit Zapfen\'\' ab und nenne das Endergebnis**Kurbelgehäuse**. Denke daran, dass du den**Gebohrten Block\'\'\' ausblenden kannst, indem du ihn markierst und die Leertaste drückst, damit du sehen kannst, was du tust.

:   {\    class:wikitable border=1

\|- \| X: 15.0 mm \|\| Länge: 50.0 mm \|- \| Y: -25.0 mm \|\| Breite: 50.0 mm \|- \| Z: -55.0 mm \|\| Höhe: 55.0 mm \|- \|}

:   {\    class:wikitable border=1

\|- \| X: 75.0 mm \|\| Länge: 50.0 mm \|- \| Y: -25.0 mm \|\| Breite: 50.0 mm \|- \| Z: -55.0 mm \|\| Höhe: 55.0 mm \|- \|}

<img alt="" src=images/_Engine_Block_Tutorial_-_Crankcase.png  style="width:300px;">

Auf der rechten Seite ist im Bild zu sehen, wie das Endergebnis nun aussehen sollte. Der Modellbaum wurde zur besseren Übersicht der Bool\'schen Operationen vollständig aufgeklappt. Die einzelnen Parameter der dafür verwendeten Primitive können nach wie vor geändert werden, wobei das Gesamtmodell automatisch angepasst wird. Wir könnten das Gehäuse nun genauer ausarbeiten, aber dies soll fürs Erste reichen. Als nächstes werden wir mittels 2D Zeichnungen die Kopfbolzen konstruieren und das Gewicht des Motorblocks reduzieren, indem wir unnötige Bereiche des Rohlings entfernen.

## 2D Entwurf der Zylinderkopfdichtung 

Für die Kopfbolzen und die Form des Motorblocks werden wir wiederum Bool\'sche Operationen nutzen, um Material an den richtigen Stellen zu entfernen. Wenn wir darüber nachdenken, so kommen wir zu dem Schluss, dass alle Kopfbolzen identisch aussehen und sich nur im Ort unterscheiden. Daraus folgt, dass wir die Form des Kopfbolzens nur einmal auf dem Motorblock zeichnen müssen und ihn als Muster wiederverwenden können.

### Eingabe des 2D Zeichenmodus 

Zuerst müssen wir zum 2D Zeichnungs Arbeitsbereich wechseln. Um dies vom Teilemodus aus zu tun, kannst du *2D Zeichnung* aus der Ausklappbox oben auswählen, in der derzeit *Part* steht. Wenn Du die Ausklappbox nicht finden kannst (nicht alle Arbeitsbereiche zeigen die Ausklappbox an), kannst du auch einen Arbeitsbereich aus dem Menüeintrag **Ansicht → Arbeitsbereich** auswählen. Auch wenn wir 2D Zeichnungen anfertigen, werden wir sie im 3D Fenster zeichnen, indem wir FreeCAD mitteilen, in welche Ebene wir die Zeichnungen projizieren wollen. Nachdem du den 2D Zeichnungs Arbeitsbereich direkt über der rechten oberen Ecke der 3D Ansicht ausgewählt hast, klicke auf die Schaltfläche ganz links, die eine der folgenden Angaben enthält: {keine, oben, vorne, größe oder d(\..., \..., \..., \...)}. Sobald du darauf klickst, erscheint auf der linken Seite der Leiste ein Textfeld, in das du einen Ebenenversatz eingeben kannst, sowie 5 Schaltflächen: XY, XZ, YZ, Ansicht und Keine. Die ersten drei sind die Standardansichten von oben, von vorne und von der Seite, der Eintrag *Ansicht* verwendet die Ebene senkrecht zur Blickrichtung der Kamera (die Ansichtsebene der Kamera), und der letzte projiziert nicht in eine Ebene und ermöglicht dir die vollständige Definition der XYZ Koordinaten für jeden Punkt, den du zeichnest. Wir wollen einen Ebenenversatz von 110 einstellen (gib ihn ein und drücke die Eingabetaste) und dann auf die Schaltfläche XY klicken, um die Zeichnung auf die XY Ebene zu projizieren, die sich 110 mm oberhalb der Z Achse befindet, die der Oberseite des Motorblocks entspricht. Nachdem wir FreeCAD mitgeteilt haben, welche Ebene eingezeichnet werden soll, können wir nun mit der Konstruktion der Kopfdichtung beginnen.

Als Letztes muss die 3D Ansicht eingerichtet werden. Obwohl alle von uns angefertigten Zeichnungen in unsere definierte 2D Ebene projiziert werden, können wir die Ebene, auf der wir zeichnen, aus jedem beliebigen Winkel betrachten (einschließlich der anderen Seite der Ebene, so dass wir \"rückwärts\" zeichnen). Da wir gesagt haben, dass die Ebene diejenige ist, die koplanar zur Oberseite des Motorblocks verläuft, sollten wir die 3D Ansicht wahrscheinlich in diese Richtung oder zumindest grob in diese Richtung schauen lassen. Drücke die Taste 2 auf dem Ziffernblock, um die Draufsicht zu betrachten (beachte, dass auf dem Ziffernblock benachbarte Tasten entgegengesetzte Ansichten sind, so dass 1 und 4 von vorne-hinten, 2 und 5 von oben-unten und 3 und 6 von rechts-links sind). Wenn du den Motor von oben nach unten betrachtest, kannst du ihn durch Ziehen mit der mittleren Maustaste zentrieren, um die Ansicht zu verschieben. Im 2D Zeichenmodus schließlich können wir Teile der Zeichnung an den Ecken des Motorblocks, der Mitte der Zylinder usw. fangen lassen. Damit dies am besten funktioniert, sollten wir das Kurbelgehäuse ausblenden, damit die Zeichnungen nur an dem Teil fangen, an dem wir gerade arbeiten (drücke die Leertaste, um das ausgewählte Objekt ein-/auszublenden).

### Auslegen der Kopfbolzen 

Nun, da die richtige Ebenenprojektion und Ansicht eingerichtet ist, fügen wir 2D Zeichnungselemente auf die gleiche Weise hinzu, wie wir Grundelemente hinzugefügt haben. Klicke auf die *Kreis hinzufügen* Schaltfläche (<img alt="" src=images/Draft_Circle.svg  style="width:16px;">) und bewege die Maus in der 3D Ansicht. Du musst FreeCAD dann die XY Position für den Mittelpunkt des Kreises und den Radius mitteilen. Für diese beiden Messungen kannst du sie entweder mit der Maus eingeben (indem du den Anweisungen in der Statusleiste unten links folgst), oder du kannst die Werte in die Texteingabefelder eingeben, die oberhalb der Baumansicht erscheinen. Fahre fort und füge ein paar zufällige Kreise oben auf dem Motor hinzu, sowie ein paar nicht auf dem Motor, d.h. gerade draußen in dem leeren Raum, der deine Ansicht des Motors umgibt. Nachdem du dies getan hast, drehe die Kamera um die Oberseite des Motorblocks und schaue dir die von dir gezeichneten Kreise an. Achte darauf, wie \"flach\" sie in der Ebene sind, in die wir sie projiziert haben, und diese Ebene stimmt mit der Oberseite des Motorblocks überein; dies wird wichtig sein, wenn wir die Zeichnung extrudieren, um den Motor zu formen. Nun, da du siehst, wie man 2D Elemente hinzufügt, kannst du die Testkreise, die du hinzugefügt hast, löschen, und wir beginnen mit der Eingabe des eigentlichen Kopf Layouts. Beachte, dass, wenn dein Kreis innerhalb des Motorblocks verschwindet, deine Zeichnungsprojektionsebene nicht richtig auf den XY Modus eingestellt ist, mit einem Versatz von 110 mm.

Entwurfselemente mit der Maus hinzuzufügen ist schnell und einfach, aber nicht sehr präzise. Für den eigentlichen Entwurf werden wir die Maus deshalb nur für eine grobe Einschätzung der richtigen Koordinaten nutzen und die tatsächlichen Koordinaten in die Textfelder eintragen. Stellen Sie die Ansicht von oben wieder her, klicken Sie auf das Kreiswerkzeug und bewegen Sie die Maus in der oberen linken Ecke des Motorblocks. Es scheint, als wäre X=10, Y=30 ein guter Mittelpunkt für den Kreis. (Wichtig: Die z-Koordinate sollte dabei unverändert bleiben. Ist sie es nicht, so ist beim Festlegen der Skizzierebene ein Fehler aufgetreten. Die Ebene sollte nochmals neu festgelegt werden).

Nun da Sie wissen, wie man die Koordinaten der Zeichenelemente einfach ermittelt, können Sie ohne Probleme ein Bolzenmuster oder andere zweidimensionale Entwürfe erstellen. Für unseren drei Kopfbolzen werden wir die in der nachfolgenden Tabelle gezeigten Koordinaten verwenden. Beachten Sie, dass beim Eingeben der Werte in die Textfelder mit der Eingabetaste zum nächsten Textfeld gewechselt werden kann. Die Maus sollte dabei nicht bewegt werden, da sonst die Koordinaten überschrieben werden. Beim Zeichnen der Kreise sollte zudem die Option *Gefüllt* aktiviert sein. Falls es mit der z-Koordinate der Kreise Probleme geben sollte, so hilft es unter Umständen, die Zeichenebene auf der Höhe Z=0 zu erstellen und für die Kreise manuell eine Höhe von 110 mm einzugeben.

:   {\    class:wikitable border=1

\|- \| X1: 10 \|\| Y1: 25 \|\| Radius: 2.5 mm \|- \| X2: 70 \|\| Y2: 25 \|\| Radius: 2.5 mm \|- \| X3: 130 \|\| Y3: 25 \|\| Radius: 2.5 mm \|}

Nennen Sie die drei Kreise **Bolt 1** bis **Bolt 3**.

### Die andere Seite des Blocks 

Nun da die ersten drei Bolzen auf der einen Seite des Motorblocks platziert sind, benötigen wir noch drei weitere auf der anderen Seite. Dabei gibt es drei Möglichkeiten:

-   Wir könnten weitere Kreise wie zuvor einfügen und bei der Y-Koordinate den negativen Wert von vorhin verwenden.
-   Wir könnten die drei vorhanderen Kreise selektieren, dann über **Bearbeiten → Auswahl duplizieren** kopieren und die Y-Koordinaten von Hand ändern.
-   Wir können das Werkzeug *Spiegelung* <img alt="" src=images/Part_Mirror.png  style="width:16px;"> des Arbeitsbereichs [Part](Part_Workbench/de.md) verwenden.

Da du den ersten und zweiten Weg bereits kennen solltest, werden wir für dieses Beispielmodell den dritten Weg wählen. Jede der drei Methoden hat ihre eigenen Vor- und Nachteile, aber eine gute Bedienungsregel ist, dass einfache Modelle (wie dieses) wahrscheinlich die erste oder zweite Methode verwenden sollten, während Modelle mit viel Duplikation und/oder Duplikation sehr komplizierter Formen/Objekte wahrscheinlich die dritte Methode verwenden sollten.

Auch wenn es also ein bisschen übertrieben ist, werden wir diese Bolzen zur Demonstration spiegeln. Wechsle zurück zum Part Arbeitsbereich (beachte, dass du jederzeit zum *Vollständigen* Arbeitsbereich wechseln kannst, um alle Werkzeuge auf einmal zu sehen, wenn du lieber nicht hin- und herwechseln möchtest (veraltet seit v0.17)), indem du zu **Ansicht → Arbeitsbereich** gehst. Markiere die drei Schraubenkreise in der Baumansicht und drücke dann die Schaltfläche Spiegeln (<img alt="" src=images/Part_Mirror.svg  style="width:16px;">). Sobald du die Schaltfläche Spiegeln gedrückt hast, solltest du bemerken, dass eine neue Anzeige namens *Comboansicht* im Fensterbereich unterhalb der Strukturansicht erscheint. Viele der Werkzeuge benötigen zusätzliche Eingaben, bevor sie ausgeführt werden können, und in der Comboansicht kannst du diese Parameter eingeben. Du kannst die Kombinationsansicht vergrößern, indem du die Trennlinie, die sie von der Eigenschaftsansicht trennt, nach oben oder unten ziehst. Wähle **Bolzen 1** aus der Liste in der Kombinationsansicht, setzen die *Spiegelebene* auf XZ und drücke dann auf OK (mache dasselbe für Bolzen 2 und 3).

An dieser Stelle sollten Sie einen einfachen Motorblock mit ausgebohrten Zylindern und Markierungen der Kopfbolzen haben.

### Ausschneiden des überschüssigen Rohlingmaterials 

Nun da die Löcher für die Kopfbolzen markiert sind, können wir den äußeren Rohling des Motorblocks in eine passendere Form schneiden. Dies macht den Motor leichter, ermöglicht eine bessere Kühlung und verringert den Stahlverbrauch zum Herstellen des Motors. Ebenso wie bei den Kopfbolzen werden wir zunächst eine zweidimensionale Skizze der erwünschten Form des Blocks erstellen. Die dafür notwendige Spline-Kurve könnten wir mit der Maus zeichnen oder alternativ wieder eine Hybridmethode verwenden, bei der die Maus nur für das Abschätzen der richtigen Koordinaten verwendet wird und die endgültigen Koordinaten über die Textfelder eingegeben werden. Eine interessantere Vorgehensweise ist es, den so genannten *Konstruktionsmodus* des Arbeitsbereichs *Draft* zu nutzen, um einige Orientierungshilfen einzuzeichnen, an denen anschließend die fertige Spline-Kurve einrasten kann.

Als Anhaltspunkt werden wir zwei regelmäßige Polygone für jeden Zylinder zeichnen, wobei die Polygone konzentrisch mit dem Zylinder sind. Wechsle zunächst in die Draufsicht des Motorblocks, blende das Kurbelgehäuse aus, wechsle zurück zur 2D Entwurf Arbeitsbereich, wähle die auf 110 mm versetzte Bezugsebene und den XY Ebenenmodus (oder den Modus *Keine*, wenn du dies bevorzugen) und klicke auf die Schaltfläche *Konstruktionsmodus* in der Befehlsleiste (die Schaltfläche für den Konstruktionsmodus sieht aus wie eine Kelle und befindet sich direkt über der oberen rechten Ecke der 3D Ansicht). Der Konstruktionsmodus funktioniert genau wie der normale Modus, mit der Ausnahme, dass alle 2D Zeichnungsobjekte, die im Konstruktionsmodus erstellt werden, in einer anderen Farbe gezeichnet und automatisch in eine separate Gruppe in der Baumansicht gesetzt werden. Dies ermöglicht es dir, deine Hilfszeichnungen auszublenden und nur die wirklichen Dinge wie Schraubenlochmarkierungen zurückzulassen, indem du die Konstruktionsgruppe ausblendest, oder alle Hilfsobjekte zu löschen, indem du einfach die Gruppe löschst.

:   *Weiterführend: [ Konstruktionsmodus](Draft_ToggleConstructionMode/de.md)*

Nun, da deine Zeichenebene korrekt eingerichtet ist und du dich im Konstruktionsmodus befindest, klicke auf die Schaltfläche *Regelmäßiges Polygon* (<img alt="" src=images/Draft_Polygon.svg  style="width:16px;">) und bewege die Maus bei gedrückter STRG Taste entlang der Kante des linken Zylinders. Du solltest sehen, dass ein kleiner schwarzer Punkt entweder am Rand des Zylinders oder in der Mitte des Zylinders gefangen wird, je nachdem, wo sich die Maus auf dem Umfang befindet. Bewege den Mauszeiger so, dass der schwarze Punkt in der Mitte des Zylinders gefangen ist, und klicke mit der linken Maustaste. Dadurch wird der Mittelpunkt des Polygons in die Mitte des Zylinders gesetzt, das Programm fragt uns nach der Anzahl der Kanten des Polygons und dem Radius, in den es eingeschrieben ist. Ein wenig mit der Maus zu untersuchen, sieht so aus, als wäre ein Radius von 30 gut (also gib das ein) und gib 14 für die Anzahl der Seiten ein, aber lasse diesmal das Kästchen *Gefüllt* unmarkiert. Wenn du den Fang nicht auf die Mitte des Zylinders fangen lassen kannst (ich hatte Probleme mit meinem), kannst du die Koordinaten immer manuell eingeben (X=40, Y=0, Z=110). Füge ein zweites Polygon hinzu, ebenfalls zentriert auf dem linken Zylinder, aber dieses sollte 22 Seiten und einen Radius von 45 mm haben. Füge schließlich die gleichen zwei Polygone über dem rechten Zylinder hinzu (zentriert bei X=100, Y=0, Z=110). Wenn du fertig bist, solltest du zwei \"Achterfiguren\" haben, die die Zylinder und Kopfschrauben umgeben. (Beachte, dass das Programm derzeit nicht wirklich nach der Anzahl der Kanten fragt, so dass du nur den Mittelpunkt und den Radius festlegst und dann die Anzahl der Flächen in der Eigenschaftsansicht ändern musst).

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline.png  style="width:300px;">

Nun, da wir unsere Führungspolygone an Ort und Stelle haben, sind wir bereit, die Spline Kurve einzuzeichnen, die die Außenform des Motorblocks definiert. Da diese Kurve Teil des endgültigen Objekts sein wird, kannst du den Konstruktionsmodus ausschalten, indem du auf die gleiche Schaltfläche klickst, die du zum Einschalten gedrückt hast. Klicke nun auf die *BSpline hinzufügen* Schaltfläche (<img alt="" src=images/Draft_BSpline.svg  style="width:16px;">) und beginne mit dem Zeichnen der BSpline durch *STRG+Linksklick* an jeder Stelle, an der du einen Kontrollpunkt für die Spline-Kurve hinzufügen möchtest. Du möchtest, dass dein erster Kontrollpunkt am äußersten linken Punkt des inneren Führungspolygons für den linken Zylinder liegt. Fahre fort, Kontrollpunkte entlang der gesamten Spline Kurve hinzuzufügen, bis du auf den letzten Punkt *vor* klickst, den du zu zeichnen begonnen hast, und klicke dann auf die Schaltfläche *Schließen* oben an der Stelle, an der du die Position und den Radius für die 2D Kreise eingegeben hast, die wir für die Kopfschrauben gezeichnet haben. Wenn du auf diese \"Schließen\" Schaltfläche klickst, ist das Zeichnen der Kontrollpunkte für die Spline Kurve beendet und die Enden werden zu einer geschlossenen Schleife verbunden. Es ist sehr wichtig, dass du solche Schleifen richtig schließt, wenn du vorhast, sie in feste Objekte zu extrudieren, wie wir es bei diesem Objekt tun werden. Bei offenen Spline Kurven kannst du einfach auf die Schaltfläche \"Fertigstellen\" anstelle der Schaltfläche \"Schließen\" klicken, wenn du mit dem Zeichnen fertig bist. Auf der rechten Seite siehst du, wie die fertige Spline Kurve aussehen sollte, kurz bevor du die \"Schließen\" Schaltfläche drückst (ich habe alle Liniensegmente bis auf das letzte gezeichnet, und mein Mauszeiger ist gerade dabei, auf die \"Schließen\" Schaltfläche zu klicken, um die Spline Kurve zu beenden). Beachte auch, dass ich das Kästchen *Gefüllt* angekreuzt habe, damit die resultierende Spline Kurve eine feste Platte und nicht nur einen leeren Ring bildet; dies muss getan werden, um sie in eine feste Form zu extrudieren, die an den Enden gekappt wurde.

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline_Edit_Mode.png  style="width:300px;">

Die Kontrollpunkte sind in diesem Bild nicht zu sehen, daher habe ich ein zweites Bildschirmfoto hinzugefügt, der den fertigen Spline im Bearbeitungsmodus zeigt (klicke auf die Schaltfläche *Bearbeitungsmodus*, um die Bearbeitung für das ausgewählte Objekt ein- oder auszuschalten, schalte es aus, wenn du mit der Bearbeitung fertig bist, oder überspringe diesen Schritt einfach, wenn du mit deiner Motorblockform zufrieden bist). Beachte auch, dass sich am äußersten linken Rand der Spline Kurve eine Diskontinuität befindet, auch wenn sie ordnungsgemäß geschlossen ist. Dies ist ein Fehler im Programmverhalten und wird derzeit behoben, so dass deine Spline Kurve etwas anders aussehen kann, wenn du eine neuere Version der Software verwendest, als die derzeit verfügbar ist.

### Extrudieren der 2D Kopfkonstruktion in unser 3D Modell, um die Konstruktion abzuschließen 

Nun nähern wir uns der endgültigen Konstruktion des Motors. Kehre zum Part Arbeitsbereich zurück und klicke auf die *Skizze extrudieren* Schaltfläche (<img alt="" src=images/Part_Extrude.svg  style="width:16px;">). Wähle in dem sich öffnenden Combofeld mit \"STRG+Linksklick\" die 6 Kopfschrauben und die Spline Kurve für die Extrusion aus. Die Standardrichtung ist die positive Z Achse. Wir möchten, dass die negative Z Achse das Kopfdesign \"nach unten\" und in den Motorblock extrudiert, also stelle die Richtung auf X=0, Y=0 und Z=-1 ein und gib dann 110 für die Länge (die Höhe des Motorblocks) ein. Nachdem du alle eingegebenen Werte erhälst und auf OK geklickt hast, werden die Kreise für die Bolzen nach unten bis für die Zylinder extrudiert, und die Keilnut wird nach unten extrudiert, um eine Art Zylinder mit \"geriffelten\" Kanten zu erzeugen. Markiere und verberge den **Bohrungsblock**, so dass du den extrudierten Spline sehen kannst, und verberge dann dieses Objekt, so dass du die Zylinder mit 6 Kopfschrauben sehen kannst. Du siehst, dass sehr anspruchsvolle 3D Formen hergestellt werden können, indem man mit einer 2D Zeichnung beginnt und Teile davon nach unten extrudiert. Wir könnten sogar verschiedene Teile der Zeichnung in unterschiedlichem Umfang extrudieren, um z.B. Bohrungen in Bolzenlöchern vorzunehmen, die nur teilweise durch den Block gehen, aber separate Wassermäntel schneiden, die ganz durchgehen. Zu diesem Zeitpunkt werden alle deine extrudierten Objekte einfach \"Extrudieren001\...\" genannt, so dass du sie durchgehst und jedes von ihnen benennst, damit du sie im nächsten Abschnitt identifizieren kannst (ich werde meine *Kopfschraubenbohrung 1* bis *6* benennen und den Spline **Extrudierter Spline** benennen, ich schlage vor, dieselben Namen auch in deinem Modell zu verwenden). Nun, da du deine extrudierten Formen hast, sind es nur noch ein paar boolesche Operationen, um das endgültige Blockdesign zu erzeugen. Gehe durch und zeige die Hauptkomponenten (den *Bohrungsblock* und das *Kurbelgehäuse*) und alle deine neu erstellten extrudierten Objekte.

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:300px;">

Jetzt, wo wir 3D Objekte für die Bohrungsöffnungen und die äußere Form haben, können wir das Ganze mit ein paar booleschen Operationen zusammenfügen. Wähle deine 6 extrudierten Kopfbolzen in der Baumansicht aus und verbinde sie zu einem Verbund (benenne das resultierende Objekt **Kopfbolzenbohrungsöffnungen**). Wähle dann den \"Bohrblock\" und die \"Kopfbolzenbohrungsöffnungen\" in dieser Reihenfolge aus und führe einen Schnitt durch (wie beim Ausbohren der Zylinder), nenne das resultierende \"Schnitt\"-Objekt \"Block mit Kopfbolzen\". Wähle schließlich den *Block mit Kopfbolzen* und den *\'Extrudierten Spline* und drücke die *Schnitt herstellen* Schaltfläche (<img alt="" src=images/Part_Common.svg  style="width:16px;">), und benenne das resultierende Objekt *\'Motorblock*.

Dein endgültiges Objekt sollte wie auf dem Bild rechts aussehen.


{{clear
---

# Engine Block Tutorial/de

 }



---
![](images/Right_arrow.png) [documentation index](../README.md) > Engine Block Tutorial/de
