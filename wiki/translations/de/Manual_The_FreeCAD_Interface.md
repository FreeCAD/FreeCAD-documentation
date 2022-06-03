# Manual:The FreeCAD Interface/de
{{Manual   *TOC/de}}

FreeCAD benutzt das [Qt Rahmenwerk](https   *//de.wikipedia.org/wiki/Qt_(Bibliothek)) um seine Oberfläche zu holen und zu verwalten. Dieses Rahmenwerk wird in einer Vielzahl von Anwendungen verwendet, so dass die FreeCAD Oberfläche sehr klassisch ist und keine besondere Schwierigkeit darstellt, sie zu verstehen. Die meisten Schaltflächen sind Standard und werden dort angezeigt, wo du sie erwartest **Datei → Öffnen, Bearbeiten → Einfügen, usw**. Hier ist das Aussehen von FreeCAD, wenn du es zum ersten Mal öffnest, gleich nach der Installation, und zeigt dir das Startzentrum   *

![](images/FreeCAD-v0-18-FirstStart.png )

Das Startcenter ist ein gefälliger \"Begrüßungsbildschirm\", der nützliche Informationen für Neueinsteiger anzeigt, wie z.B. die neuesten Dateien, an denen du gearbeitet hast, was es Neues in der FreeCAD Welt gibt oder Schnellinfos zu den gängigsten Arbeitsbereichen. Außerdem wirst Du benachrichtigt, wenn eine neue stabile Version von FreeCAD verfügbar ist.

Nach einer Weile, wenn du dich mit FreeCAD besser auskennst, hast du vielleicht Änderungen in den Einstellungen vorgenommen, so dass du dich beim Start von FreeCAD direkt in einem der Arbeitsbereiche wiederfindest, wenn ein neues Dokument geöffnet ist. Oder du schließt einfach den Reiter \"Startseite\" und erstellst ein neues Dokument   *

![](images/FreeCAD-v0-18-NewProject.png )

### Arbeitsbereiche

Beachte, dass sich einige der Symbole zwischen den beiden obigen Bildschirmaufnahmen geändert haben. Hier kommt das wichtigste Konzept der FreeCAD Oberfläche ins Spiel   * Arbeitsbereiche.

Arbeitsberiche sind Gruppen von Werkzeugen (Schaltflächen in der Symbolleiste, Menüs und andere Bedienelemente der Benutzeroberfläche), die nach Spezialgebieten gruppiert sind. Stelle dir eine Werkstatt vor, in der verschiedene Personen zusammenarbeiten   * Eine Person, die mit Metall arbeitet, eine andere mit Holz. Jeder von ihnen hat in seiner Werkstatt einen separaten Tisch mit spezifischen Werkzeugen für seine Arbeit. Sie können jedoch alle an den gleichen Objekten arbeiten. Dasselbe geschieht in FreeCAD.

Die wichtigste Steuerung der FreeCAD Oberfläche ist der Arbeitsbereichswähler, mit dem du von einem Arbeitsbereich zum anderen wechseln kannst   *

![](images/FreeCAD-v0-18-WorkbenchMenu.png )

Die Arbeitsbereiche verwirren neue Benutzer oft, da es nicht immer einfach ist, zu wissen, in welchem Arbeitsbereich man nach einem bestimmten Werkzeug suchen soll. Aber sie sind schnell zu begreifen, und nach kurzer Zeit wird es sich ganz natürlich anfühlen - wenn man erkennt, dass es ein bequemer Weg ist, die Vielzahl der Werkzeuge, die FreeCAD zu bieten hat, zu organisieren. Arbeitsbereiche sind auch vollständig anpassbar (siehe unten). Dasselbe Werkzeug kann in mehr als einem Arbeitsbereich erscheinen. Das Schaltflächensymbol für ein bestimmtes Werkzeug wird immer das gleiche sein, egal in welchem Arbeitsbereiche es erscheint.

Später in diesem Handbuch findest du auch eine Tabelle mit dem Inhalt aller Arbeitsbereiche.

### Die Oberfläche 

Lass uns einen genaueren Blick auf die verschiedenen Teile der Oberfläche werfen   *

![](images/FreeCAD-v0-18-Cube.png )

-   **Die 3D Ansicht** ist die Hauptkomponente der Oberfläche; hier werden die Objekte, mit denen du arbeitest, gezeichnet und verändert. Du kannst mehrere Ansichten desselben Dokuments (oder derselben Objekte) oder mehrere Dokumente gleichzeitig geöffnet haben. Jede dieser Ansichten kann einzeln vom Hauptfenster abgedockt werden. Du kannst Objekte oder Teile von Objekten durch Anklicken auswählen und die Ansicht mit den Maustasten verschieben, zoomen und drehen. Dies wird im nächsten Kapitel näher erläutert.

Neben der 3D Ansichtspaneel stehen folgende Informationspaneele zur Verfügung. Sie können durch Auswahl unter {{MenuCommand/de|Ansicht → Paneele}} ein- oder ausgeblendet werden. . Der Name des Paneels erscheint in der linken oberen Ecke des Paneels, wenn es angezeigt wird   *

-   **Die comco Ansicht** hat zwei Registerkarten   *
    -   Der Reiter Modell zeigt Ihnen den Inhalt und die Struktur deines Dokuments oben und die Eigenschaften (oder Parameter) des/der ausgewählten Objekts/e unten. Diese Eigenschaften sind in zwei Kategorien unterteilt   *
        -   Daten (Eigenschaften, die die Geometrie selbst betreffen)
        -   Ansicht (Eigenschaften, die das Aussehen der Geometrie auf dem Bildschirm bestimmen).
    -   Der Reiter Aufgaben ist der Bereich, in dem FreeCAD dich nach Werten fragt, die spezifisch für den Arbeitsbereich und das Werkzeug sind, die du gerade verwendest. Zum Beispiel die Eingabe eines \'Länge\'-Wertes, wenn das [Entwurf Arbeitsbereich Linienwerkzeug](Draft_Line/de.md) verwendet wird.

Es wird geleert und nach dem **OK** wieder auf den Reiter Modell gewechselt. (oder Cancel) Taste gedrückt wird. Ein Doppelklick auf das zugehörige Objekt im Reiter Modell öffnet in der Regel wieder den entsprechende Aufgabenreiter, um die Einstellungen zu ändern.
Der Aufgabenreiter hat manchmal rätselhafte und frustrierende Nebeneffekte. Wenn der Aufgabenreiter nicht leer ist, werden einige FreeCAD Operationen nicht wie erwartet funktionieren. Wenn du zum Beispiel ein einzelnes Objekt in deinem Modell hast, wie z.B. einen Würfel, öffnet ein Doppelklick darauf den Aufgabenreiter , um die Parameter, die den Würfel charakterisieren, zu ändern. Wenn du die [Auswahlansicht](#Selection_view/de.md) geöffnet hast, siehst du den internen Namen des Würfels dort aufgelistet. Der gesamte Würfel wird im 3D Paneel grün, was anzeigt, dass der gesamte Würfel ausgewählt ist. Ein Klick auf den Hintergrund hebt die Auswahl des gesamten Würfels auf und löscht die Auswahlansicht. Bislang ist dies ein normales Verhalten. Wenn du jetzt jedoch auf eine Fläche des Würfels klickst, anstatt diese Fläche auszuwählen, wird nichts ausgewählt --- da der Aufgabenreiter nicht abgeschlossen ist. Auch wenn du dort keine Änderungen an den Parametern vorgenommen hast, wartet FreeCAD das auf den **OK** (oder andere) Schaltfläche im Augabenreiter angeklickt werden.

-   **Die Berichtsansicht** ist normalerweise versteckt, aber es ist eine gute Idee, sie zu öffnen, da sie alle Informationen, Warnungen oder Fehler auflistet, um dir zu helfen, zu entschlüsseln (oder Fehler zu suchen), was du möglicherweise falsch gemacht hast.
-   **Die Python Konsole** ist ebenfalls standardmäßig versteckt. Hier kannst du mit Hilfe der [Python Sprache](https   *//en.wikipedia.org/wiki/Python_%28programming_language%29) mit dem Inhalt des Dokuments interagieren. Da jede Aktion, die du auf der FreeCAD Oberfläche durchführst, tatsächlich ein Stück Python Code ausführt, kannst du, wenn du diese geöffnet hast, die Entwicklung des Codes in Echtzeit beobachten --- so kannst du auf wunderbare und einfache Weise ein wenig Python unterwegs lernen, fast ohne es zu merken.
-   **Die Baumansicht** zeigt nur den Objektbaum an, der unter dem Modellreiter in der Combo Ansicht angezeigt wird. Er ist normalerweise ausgeblendet.
-   **Die Eigenschaftsansicht** zeigt nur die Informationen zu den Objekteigenschaften an, die unten in der Combo Ansicht angezeigt werden. Sie ist normalerweise ausgeblendet.
-   **Die Auswahlansicht** zeigt die Namen der aktuell gewählten Objekte an. Dies sind die Objekte, auf die eine Arbeitsbereichsoperation angewendet wird. Sie kann verwendet werden, um die Auswahl zu verfeinern, indem einige dieser Objekte vor der Anwendung einer Arbeitsbereichsoperation abgewählt werden. Die Auswahlansicht kann auch dazu verwendet werden, um Objekte nach Namen zu suchen und diese dann auszuwählen. Standardmäßig ist die Auswahlansicht ausgeblendet. Du kannst zwar oft das/die aktuell ausgewählte(n) Objekt(e) ermitteln, indem du dir den Objektbaum im Register Modell der Kombinationsansicht ansiehst, aber bei komplexen Operationen, die eine Mehrfachauswahl erfordern und bei denen die Auswahl schwierig ist, ist es hilfreich, diese Ansicht einzublenden, damit du sowohl die Beschriftungen sehen als auch die ausgewählten Objekte zählen kannst.

![](images/FreeCAD-v0-18-ExtrudeTask.png )

### Anpassung der Oberfläche 

Die Oberfläche von FreeCAD ist in hohem Maße anpassbar. Alle Paneele und Werkzeugleisten können an verschiedene Stellen verschoben oder übereinander gestapelt werden. Sie können auch geschlossen und bei Bedarf über das Menü Ansicht oder durch einen Rechtsklick auf einen leeren Bereich der Oberfläche wieder geöffnet werden. Es sind jedoch noch viele weitere Optionen verfügbar, wie z.B. das Erstellen von benutzerdefinierten Symbolleisten mit Werkzeugen aus einer der Arbeitsbereiche oder das Zuweisen und Ändern von Tastaturkürzeln.

Diese erweiterten Anpassungsoptionen sind über das Menü {{MenuCommand/de|Werkzeuge → Menü Anpassen}} verfügbar   *

![](images/FreeCAD-v0-18-CustomizeInterface.png )

**Weiterlesen**

-   [Erste Schritte mit FreeCAD](Getting_started/de.md)
-   [Anpassung der Oberfläche](Interface_Customization/de.md)
-   [Arbeitsbereiche](Workbenches/de.md)
-   [Mehr über Python](https   *//www.python.org)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:The FreeCAD Interface/de
