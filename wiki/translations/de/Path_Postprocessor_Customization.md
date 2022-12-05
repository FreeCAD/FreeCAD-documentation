# Path Postprocessor Customization/de
}





{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

FreeCAD verwendet als interne Darstellungen für die erzeugten Pfade so genannte G-Codes. Sie können solche Dinge beschreiben wie: Geschwindigkeit und Vorschübe, Anhalten des Motors usw\... Aber das Wichtigste sind die Bewegungen, die sie beschreiben. Diese Bewegungen sind ziemlich einfach: Sie können gerade Linien oder Kreisbögen sein. Anspruchsvollere Kurven wie B-Splines werden bereits von FreeCADs <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Pfad Arbeitsbereich](Path_Workbench/de.md) angenähert.


</div>

## Was der Postprozessor für dich tun kann 


<div class="mw-translate-fuzzy">

Viele Fräsen verwenden ebenfalls G-Codes zur Steuerung des Fräsprozesses. Sie mögen fast wie die internen Codes aussehen, aber es kann einige Unterschiede geben:

-   die Maschine kann eine spezielle Startsequenz haben
-   es kann eine spezielle Stoppsequenz haben
-   Bögen können mit einem relativen oder einem absoluten Mittelpunkt definiert werden
-   es kann Zeilennummern in einem bestimmten Format erfordern
-   es kann so genannte Festzyklen für vordefinierte Unterprozesse wie Bohren verwenden
-   Vielleicht bevorzugst du die Ausgabe deines G-Codes entweder in metrischen oder zölligen Einheiten.
-   Es könnte nützlich sein, vor dem Aufruf eines Werkzeugwechsels eine Reihe von Bewegungen durchzuführen, um die Aktion für den Bediener zu erleichtern.
-   Vielleicht möchtest du Kommentare zur besseren Lesbarkeit hinzufügen oder sie unterdrücken, um das Programm klein zu halten.
-   Möglicherweise möchtest du eine benutzerdefinierte Kopfzeile einfügen, um das Programm für zukünftige Referenzen zu identifizieren oder zu dokumentieren.
-   \...


</div>

Darüber hinaus gibt es weitere Sprachen zur Steuerung einer Fräse, wie z.B. HPGL, DXF oder andere.

Der Postprozessor ist ein Programm, das die internen Codes in eine vollständige Datei übersetzt, die auf deine Maschine hochgeladen werden kann.

## Vorbereitung zum Schreiben deines eigenen Postprozessors 

Du kannst mit einem sehr einfachen Modell beginnen, das zeigt, wie deine Maschine gerade Linien und Bögen liest. Bereite es mit einem beliebigen Programm vor, das für deine Maschine geeignet ist.

Eine Datei für solche Pfade, die bei (0,0,0) beginnen und in Richtung Y gehen, wäre hilfreich. Stelle sicher, dass sich das Werkzeug selbst entlang dieser Bahn bewegt, d.h. es darf keine Werkzeugradiuskompensation angewendet werden.

![](images/Path_PostProcessorSketch.png )

Der Pfad in FreeCAD würde wie folgt aussehen. Bitte beachte den kleinen blauen Pfeil, er zeigt die Startrichtung an. Für einen allerersten Versuch dürftest du nur eine Ebene in der XY-Ebene angeben.

![](images/Path_PostProcessorModel.png )


<div class="mw-translate-fuzzy">

Du kannst dir dann die Datei anschauen und sie mit der Ausgabe bestehender Postprozessoren wie **linux_cnc_post.py** oder **grbl_post.py** und versuche selbst, sie anzupassen, oder lade deine auf das Pfadforum <https://forum.freecadweb.org/viewforum.php?f=15> hoch, um Hilfe zu bekommen.


</div>

## Namenskonvention


<div class="mw-translate-fuzzy">

Für ein Dateiformat **<filename>** sollte der Postprozessor den Namen **<filename>_post.py** erhalten. Bitte beachte, dass die Nachsilbe und die Erweiterung **_post.py** klein geschrieben werden müssen.


</div>

The new name should be reflected at the head of the parser arguments list in the **<filename>_post.py** file, e.g.:


{{Code|lang=text|code=
parser = argparse.ArgumentParser(prog="grbl", add_help=False)
}}

Wenn du testest, leg es in dein Makroverzeichnis. Wenn es gut funktioniert, erwäge bitte, es anderen zur Verfügung zu stellen (poste es im FreeCAD Pfad Forum), damit es in Zukunft in die FreeCAD Distribution aufgenommen werden kann.

## Andere vorhandene Postprozessoren 


<div class="mw-translate-fuzzy">

Zum Vergleich kannst du dir die Postprozessoren ansehen, die mit deiner FreeCAD Installation geliefert werden. Sie befinden sich unter dem Mod Verzeichnis in Path/PathScripts/post. Weit verbreitet sind die Postprozessoren [linuxcnc](http://linuxcnc.org/) und [grbl](https://github.com/grbl/grbl). Das Studium ihres Codes kann hilfreiche Einblicke geben.

-   Unter Linux lautet der Pfad /usr/share/freecad/Mod/Path/PathScripts/post


</div>


<div class="mw-translate-fuzzy">

## Programmierung deines eigenen Postprozessors 

In diesem Beitrag werden einige Interna des linuxcnc Postprozessors diskutiert. Die gleiche Struktur wird auch in anderen Postprozessoren verwendet.


</div>

This post discusses some internals from the linuxcnc postprocessors. The same strucure is used in other postprocessors as well.

Beim ansehen von linuxcnc_post.py, siehst du die Exportfunktion (ab 0.19.20514 ist es in Zeile 156)


```python
def export(objectslist, filename, argstring):
    # pylint: disable=global-statement
    ...
    gcode = ""
    ...
    ...
```

sammelt es Schritt für Schritt die verarbeiteten G-Codes in der Variablen \"gcode\" und erledigt den Gesamtexport der nachbearbeitbaren Objekte (Operationen, Werkzeuge, Aufträge usw.). Die Exportfunktion erledigt den hochrangigen Kram wie Kommentare und Kühlmittel, aber alle Objekte, die mehrere Pfadbefehle haben (Werkzeugwechsel und Operationen), werden an die Parse Funktion delegiert (ab 0.19.20514 ist es in Zeile 288).


```python
def parse(pathobj):
    ...
    out = ""
    lastcommand = None
    ...
    ...
```

Ähnlich der \"Export\" Funktion werden die G-Codes in der Variablen \"out\" gesammelt geparst. In der Variablen \"command\" werden die Befehle, wie sie in der Funktion \"inspect G-code\" des Pfad Arbeitsbereichs zu sehen sind, gespeichert und können zur weiteren Bearbeitung untersucht werden.


```python
        for c in pathobj.Path.Commands:

            command = c.Name
```

Es erkennt die verschiedenen G, M, F, S und andere G-Codes. Indem es sich den letzten Befehl in der Variablen \"lastcommand\" merkt, kann es nachfolgende Wiederholungen von modalen Befehlen unterdrücken.

Sowohl \"parse\" als auch \"export\" dienen lediglich der Formatierung von Zeichenketten und deren Verkettung zu der endgültigen Ausgabe.

Du wirst sehen, dass beide Funktionen auch die Funktion \"Zeilennummer()\" aufruft. Wenn der Benutzer Zeilennummern wünscht, gibt die Funktion \"linenumber\" die Zeichenkette zurück, die an der entsprechenden Stelle eingefügt werden soll, andernfalls gibt sie eine leere Zeichenkette zurück, so dass nichts hinzugefügt wird.

## Verwandtes


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Post.svg  style="width:24px;"> [Pfad PostProzess](Path_Post/de.md)


</div>





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Postprocessor Customization/de
