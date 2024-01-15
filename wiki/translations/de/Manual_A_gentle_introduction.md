# Manual:A gentle introduction/de
{{Manual:TOC}}

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) ist eine populäre, quelloffene Programmiersprache, die sehr oft als Skriptsprache in Anwendungen eingebettet ist, so auch in FreeCAD. Sie hat eine Reihe von Eigenschaften, die sie für uns FreeCAD-Anwender geeignet machen: Sie ist sehr leicht zu erlernen, besonders für Leute, die noch nie programmiert haben und sie ist in viele andere Anwendungen eingebettet. Das macht sie zu einem wertvollen Werkzeug, das sich zu lernen lohnt, da sie auch in anderen Programmen wie [Blender](http://www.blender.org), [Inkscape](http://www.inkscape.org) oder [GRASS](http://grass.osgeo.org/) verwendet werden kann.

FreeCAD macht umfangreichen Gebrauch von Python. Damit kann auf fast alle Funktionen von FreeCAD zugegriffen werden, um sie zu steuern. So können beispielsweise neue Objekte erstellt, ihre Geometrie geändert, ihr Inhalt analysiert und sogar neue Bedienelemente, Werkzeuge und Bedienfelder erstellt werden. Einige FreeCAD-Arbeitsbereiche und die meisten Addon-Arbeitsbereiche sind vollständig in Python programmiert. FreeCAD enthält eine fortschrittliche Python-Konsole, die über den Menüeintrag **Ansicht-\>Paneele-\>Python-Konsole** zur Verfügung steht. Sie ist oft nützlich, um Operationen durchzuführen, für die es noch keine Schaltfläche in der Symbolleiste gibt, oder um Formen auf Probleme zu überprüfen oder um sich wiederholende Aufgaben durchzuführen:

![](images/Exercise_python_01.jpg )

Aber die Python-Konsole hat noch eine andere sehr wichtige Verwendung: Jedes Mal, wenn du eine Schaltfläche in der Werkzeugleiste drückst oder andere Operationen in FreeCAD ausführst, wird ein Teil des Python-Codes in der Konsole ausgegeben (wenn die Option **Skriptbefehle in Python-Konsole anzeigen** in den Voreinstellungen unter **Bearbeiten → Einstellungen... → Python → Makro** aktiviert ist) und ausgeführt. Wenn du die Python-Konsole offen lässt, kannst du buchstäblich sehen, wie sich der Python-Code bei der Arbeit entfaltet, und im Handumdrehen, fast ohne es zu wissen, wirst du etwas von der Sprache Python lernen.

FreeCAD verfügt auch über ein [Makro-System](Macros/de.md), mit dem du Aktionen aufzeichnen kannst, die später wiedergegeben werden können. Dieses System verwendet ebenfalls die Python-Konsole, indem es einfach alles aufzeichnet, was darin gemacht wird.

In diesem Kapitel werden wir ganz allgemein die Sprache Python entdecken. Wenn du daran interessiert bist, mehr zu erfahren, hat das FreeCAD-Dokumentations-Wiki einen ausführlichen Abschnitt zum Thema [Python-Programmierung](Power_users_hub/de.md).



### Python-Code schreiben 

Es gibt zwei einfache Möglichkeiten, Python-Code in FreeCAD zu schreiben: Von der Python-Konsole aus (**Ansicht → Paneele → Python-Konsole**), oder vom Makro-Editor aus (**Makro → Makros... → Erstellen**). In der Konsole schreibst du nacheinander Python-Befehle, die ausgeführt werden, wenn du die Eingabetaste drückst, während Makros ein komplexeres Skript aus mehreren Zeilen enthalten können, das nur dann ausgeführt wird, wenn das Makro von demselben Makro-Fenster aus gestartet wird.

In diesem Kapitel wirst du beide Methoden verwenden können, aber es wird dringend empfohlen, die Python-Konsole zu verwenden, da sie dich sofort über alle Fehler informiert, die du beim Tippen machst.

Wenn du Python zum ersten Mal verwendest, solltest du diese kurze [Einführung in die Python-Programmierung](Introduction_to_Python/de.md) liest, bevor du weitermachst, wird sie die grundlegenden Konzepte von Python klarer machen.



### Handhabung von FreeCAD Objekten 

Beginnen wir damit, ein neues leeres Dokument zu erstellen:

doc = FreeCAD.newDocument()

Wenn du dies in der FreeCAD-Python-Konsole eingibst, wirst du, sobald du \"FreeCAD.\" eintippst (das Wort FreeCAD gefolgt von einem Punkt), bemerken, dass sich ein Fenster öffnet, das ermöglicht den Rest deiner Zeile schnell automatisch vervollständigen zu können. Besser noch, jeder Eintrag in der Autovervollständigungsliste hat eine QuickInfo, die erklärt, was er tut. Dies macht es sehr einfach, die verfügbaren Funktionen zu erkunden. Bevor du \"newDocument\" wählst, wirf einen Blick auf die anderen verfügbaren Optionen.

![](images/Exercise_python_02.jpg )

Sobald du **Enter** drückst, wird unser neues Dokument erstellt. Dies ist ähnlich wie das Drücken der Schaltfläche \"Neues Dokument\" in der Werkzeugleiste. In Python wird der Punkt verwendet, um etwas anzuzeigen, das in etwas anderem enthalten ist (newDocument ist eine Funktion, die sich innerhalb des FreeCAD-Moduls befindet). Das sich öffnende Fenster zeigt dir daher alles, was in \"FreeCAD\" enthalten ist. Wenn du nach \"newDocument\" anstelle der Klammern einen Punkt hinzufügen würdest, würde es dir alles anzeigen, was in der Funktion \"newDocument\" enthalten ist. Die Klammern sind obligatorisch, wenn du eine Python-Funktion, wie diese hier, aufrufst. Wir werden das weiter unten besser veranschaulichen.

Kommen wir nun zurück zu unserem Dokument. Lasse uns sehen, was wir damit machen können. Gib Folgendes ein und untersuche die verfügbaren Optionen:

doc.

Normalerweise sind Namen, die mit einem Großbuchstaben beginnen, Attribute: Sie enthalten einen Wert. Namen, die mit einem Kleinbuchstaben beginnen, sind Funktionen (auch Methoden genannt): sie \"tun etwas\". Namen, die mit einem Unterstrich beginnen, sind normalerweise für den internen Gebrauch des Moduls da, und du solltest sie ignorieren. Lasse uns eine der Methoden verwenden, um ein neues Objekt zu unserem Dokument hinzuzufügen:

box = doc.addObject("Part::Box","myBox")

Unser Kasten wird in der Baumansicht hinzugefügt, aber in der 3D-Ansicht passiert noch nichts, weil beim Arbeiten von Python aus das Dokument nie automatisch neu berechnet wird. Wir müssen dies manuell tun, wann immer es erforderlich ist:

doc.recompute()

Jetzt ist unser Kasten in der 3D-Ansicht erschienen. Viele der Schaltflächen auf der Werkzeugleiste, mit denen in FreeCAD Objekte hinzugefügt werden können, tun eigentlich zwei Dinge: das Objekt hinzufügen und neu berechnen. Versuche nun, mit der entsprechenden Schaltfläche im Arbeitsbereich Part eine Kugel hinzuzufügen, und du wirst sehen, wie die beiden Zeilen des Python-Codes nacheinander ausgeführt werden.

Du kannst eine Liste aller möglichen Objekttypen wie Part::Box abfragen:

doc.supportedTypes()

Lass uns nun den Inhalt unseres Kastens erkunden:

box.

Du wirst sofort ein paar sehr interessante Dinge sehen, wie zum Beispiel:

box.Height 

Dadurch wird die aktuelle Höhe unseres Kastens ausgegeben. Versuchen wir nun, das zu ändern:

box.Height = 5 

Wenn du dein Kästchen mit der Maus markierst, siehst du, dass im Eigenschafteneditor unter dem **Daten**-Reiter unsere Eigenschaft **Höhe** mit dem neuen Wert erscheint. Alle Eigenschaften eines FreeCAD-Objekts, die in den Reitern **Daten** und **Ansicht** erscheinen, sind auch von Python direkt zugänglich, und zwar über ihren Namen, wie wir es bei der Eigenschaft Höhe getan haben. Auf die Dateneigenschaften wird z.B. direkt vom Objekt selbst aus zugegriffen:

box.Length 

Ansichtseigenschaften werden in einem **ViewObject** gespeichert. Jedes FreeCAD-Objekt verfügt über ein ViewObject, das die visuellen Eigenschaften des Objekts speichert. Wenn FreeCAD ohne seine grafische Schnittstelle ausgeführt wird (z.B. wenn es von einem Terminal mit der Befehlszeilenoption -c gestartet wird oder wenn es von einem anderen Python-Skript aus verwendet wird), ist das ViewObject nicht verfügbar, da es überhaupt keine bildliche Darstellung gibt.

Versuche das folgende Beispiel, um auf die Linienfarbe unserer Kiste zuzugreifen:

box.ViewObject.LineColor 



### Vektoren und Platzierungen 

Vektoren sind ein grundlegendes Konzept in jeder 3D-Anwendung. Es ist eine Liste von 3 Zahlen (x, y und z), die einen Punkt oder eine Position im 3D-Raum beschreiben. Mit Vektoren können viele Dinge gemacht werden, wie z.B. Additionen, Subtraktionen, Projektionen und vieles mehr. In FreeCAD funktionieren Vektoren wie folgt:

myvec = FreeCAD.Vector(2,0,0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0,3,0)
sumvec = myvec.add(othervec)

Ein weiteres gemeinsames Merkmal von FreeCAD-Objekten ist ihre **Platzierung**. Wie wir in früheren Kapiteln gesehen haben, hat jedes Objekt eine Placement-Eigenschaft, die die Position (Base) und die Orientierung (Rotation) des Objekts enthält. Diese Eigenschaften lassen sich von Python aus leicht manipulieren, z.B. um unser Objekt zu verschieben:

print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5,5,0)
box.Placement = otherpla

**Mehr lesen**

-   [Python](https://www.python.org)
-   [Makros](Macros/de.md)
-   [Einführung in Python](Introduction_to_Python/de.md)
-   [Python Skripterstellung Tutorium](Python_scripting_tutorial/de.md)
-   [Hauptanwenderzentrum](Power_users_hub/de.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:A gentle introduction/de
