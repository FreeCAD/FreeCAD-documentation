---
 TutorialInfo:e
   Topic: Arbeitsbereich BIM
   Level: Fortgeschritten
   Time: 120 Minuten
   Author: Pablo Gil
   FCVersion: 0.19.x
   Files: 
}}

## Einführung

Es war eine so harte Nachforschung darüber, wie man eine Arbeitskopie von IfcOpenShell python unter OSX/macOS erhält, um IFC Dateien zu importieren/exportieren, dass ich dieses Tutorial weitergebe, falls es mehr Leuten hilft. Mein System ist OSX 10.11.6, 64bits mit Python 2.7.11, es könnte für dich funktionieren, wenn du auch OSX hast, da sie oft 64bit sind, aber von meinem abweichen können. Die Prozedur könnte sehr ähnlich sein, wenn du Linux oder Windows verwendest, aber es gibt wahrscheinlich einige Unterschiede.



## Anforderungen

-   IfcOpenShell
-   FreeCAD v0.19 oder höher

## Schritte

1\. Lade das vollständige GitHub Projekt unter <https://github.com/IfcOpenShell/IfcOpenShell> herunter oder klone es 

:   
    `git Klon https://github.com/IfcOpenShell/IfcOpenShell
---

# Import/Export IFC - compiling IfcOpenShell/de

     

2\. Gehe in einem Terminal zum Ordner **/nix/** und starte das Skript. Unter OSX wird es ausgeführt mit: 
```python
cd nix/
./build-all.sh
``` Es wird zwischen 30 und 120 Minuten dauern, bis alles kompiliert ist. Es ist nicht die intelligenteste Art, [IfcOpenShell](IfcOpenShell/de.md) zu kompilieren, aber dieses einfache Skript kompiliert alle Abhängigkeiten, Python Versionen usw.

3\. Sobald es beendet ist (ich kann mich jetzt nicht mehr erinnern, aber es wird etwas wie \"Built IfcOpenShell\...\" ausgegeben und es kehrt zu deiner Eingabeaufforderung zurück), du wirst einen neuen Ordner {**/IfcOpenShell/build/**} voller Dateien und Ordner haben. Meiner persönlichen Erfahrung nach wurde das nix \"build-all.sh\" Skript vor zwei Wochen nicht erfolgreich beendet, aber nachdem ich es gestern mit den neuesten Updates ausprobiert habe, hat es gut funktioniert, so dass ich vermute, du könntest etwas Ähnliches erleben, falls die Entwicklung weiter geht\... Jetzt hast du also alles, was du brauchst, aber du mußt noch etwas Handarbeit leisten, um es zum Laufen zu bringen:

4\. Öffne FreeCAD und öffne die [Python Konsole](Python_console/de.md) und [Berichtsansicht](Report_view/de.md). Schreibe dann Folgendes in die Python Konsole: 
```python
import sys
print sys.path
``` Du erhälst eine laaaaange Zeile mit allen Pfaden, die FreeCAD liest. Du könntest IfcOpenShell vielleicht in jedem dieser Pfade installieren, aber ich schlage vor, du platzierst es in einem, in dem du einen **/site-packages/** nach einem **/Python/** oder **/python-something/** findest. In meinem Fall war es **/Library/Python/2.7/site-packages**. (Hinweis: Du findest Pfade innerhalb deines Anwendungsverzeichnisses, aber ich schlage vor, sie nicht zu verwenden, da IfcOpenShell dann nur für diese Anwendung verfügbar ist)

5\. Sobald du den Ort gefunden hast, an dem du es installieren willst/musst, gehe mit deinem Dateibrowser (Finder in OSX) dorthin. Das heißt, gehe in den Ordner **/site-packages/**

:   
    {{incode|cd site-packages/`
    

6\. Öffne ein neues Dateibrowserfenster und navigiere zu deinem heruntergeladenen GitHub Projekt: **/IfcOpenShell/src/ifcopenshell-python/**\' und kopiere den vollständigen Ordner **/ifcopenshell/**

7\. Füge ihn in den **/site-packages/** Ordner ein. Jetzt solltest du so etwas haben wie: 
```python
/site-packages/ifcopenshell/__init__.py
/site-packages/ifcopenshell/entity_instance.py
/site-packages/ifcopenshell/file.py
/site-packages/ifcopenshell/geom/app.py
/site-packages/ifcopenshell/geom/main.py
/site-packages/ifcopenshell/geom/occ_utils.py
/site-packages/ifcopenshell/geom/__init__.py
/site-packages/ifcopenshell/guid.py
```

8\. Jetzt müssen wir die Dateien innerhalb des Ordners /build/ auswählen, sie sind: 
```python
_ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` aber da wir alles zusammengestellt haben, musst du diejenige auswählen, die mit deiner FreeCAD Python Version übereinstimmt. Überprüfe die erste Zeile in der Ansicht deiner FreeCAD [ Python Konsole](Python_console/de.md). In meinem Fall war es Python 2.7.11.

9\. Lasse uns nun die Dateien an die Stelle kopieren, die deiner Python Version entspricht. In meinem Fall war das der Fall: 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```

10\. Füge sie in **/site-packages/ifcopenshell/** ein

11\. Überprüfe ob alles an seinem Platz ist: 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

\(1\) aus dem GitHub Projekt
(2) aus /build/ Ordner

12\. FreeCAD schließen und erneut öffnen

## Testen

Nun, da es installiert ist, wollen wir prüfen, ob alles wie erwartet funktioniert:

12.1 in die Python Konsole schreiben: 
```python
import ifcopenshell
from ifcopenshell import geom
``` wenn es keinen Fehler auswirft, bedeutet dies, dass es korrekt installiert sein könnte

12.2 Gehe zum [Handbuch BIM-Modellierung](Manual:BIM_modeling/de.md) (Yoriks FreeCAD-Manual), navigiere zum unteren Teil der Seite und lade die folgenden Dateien zum Testen herunter: 
```python
house.FCStd
house.ifc
```

12.3 Öffne **house.FCStd**, wähle das Stammobjekt \"Gebäude\" und exportiere s (**Datei → Export**), wobei der Dateityp auf \"Industry Foundation Classes (\*.ifc)\" gesetzt wird. Drücke **Save** und wenn es funktioniert und in der [Berichtsansicht](Report_view/de.md) keinen Fehler auslöst, dann funktioniert es.

12.4 Abschließender Test, importiere **house.ifc** in eine neue Datei, also öffne eine neue Datei und importiere diese Datei\... es wird eine Weile dauern.

13\. Viel Spaß an BIM mit FreeCAD!

## Abschließende Gedanken 

Meine Meinung ist, dass FreeCAD selbst vorkompilierte Versionen von IfcOpenShell mit der Distribution gebündelt haben sollte, weil es eine totale Qual ist, es selbst zu bauen, und der durchschnittliche Benutzer wird es nicht tun (er weiß nicht, wie man GitHub kompiliert, verwaltet usw.), aber na ja, vielleicht in der Zukunft.

Ich hoffe, es hilft Euch.

Tschüss



## Verweise

-   Verwandter Forumsbeitrag [Diskussion](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell/de.md)


{{Userdocnavi

}}



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > [3rd_Party](Category_3rd_Party.md) > [File_Formats](Category_File_Formats.md) > Import/Export IFC - compiling IfcOpenShell/de
