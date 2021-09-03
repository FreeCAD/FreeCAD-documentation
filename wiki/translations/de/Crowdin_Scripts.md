 {{TOCright}}

## Verwalten von Übersetzungen für FreeCAD 

FreeCAD nutzt den Übersetzungsdienst [Crowdin](https://crowdin.com/project/freecad) um Übesetzungen zu verwalten.

Es gibt 3 Skripten in FreeCAD/src/Tools die zur Verwaltung von Übersetzungsdateien verwendet werden:

1.  updatets.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatets.py)
2.  updatecrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatecrowdin.py)
3.  updatefromcrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatefromcrowdin.py)

### Hinweise

-   Diese Skripten werden im FreeCAD/-Wurzelverzeichnis ausgeführt.
-   Damit diese Skripte funktionieren, muss der gültige FreeCAD crowdin API-Schlüssel in der Datei ~/.crowdin-freecad enthalten sein. (aus Sicherheitsgründen steht dieser nur Personen mit Administrationsrechten im FreeCAD crowdin-Projekt zur Verfügung)
-   Aktuell sind diese Werkzeuge Python2 - kompatibel.

### updatets.py

Das updatets.py Skript erzeugt \'.ts\'-Dateien (Qt Translation Source Files) in Deinem lokalen FreeCAD/-Verzeichnis.

Es ist eingebunden in: python2 updatets.py

### updatecrowdin.py

Das updatecrowdin.py Skript schiebt Änderungen aus Deinem lokalen FreeCAD/-Verzeichnis zu crowdin (3rd party translation crowdsource translation service). Das Skript unterstützt aktuell 4 Argumente:

-   updatecrowdin.py status gibt den Status der Übersetzungen aus;
-   updatecrowdin.py update aktualisiert in crowdin die aktuelle Version der \'.ts\'-Dateien, die im Quellcode gefunden werden;
-   updatecrowdin.py build erstellt ein neues Downloadpacket auf crowdin mit allen übersetzten Begriffen (Strings);
-   updatecrowdin.py download holt das neueste Packet (build) ab;

### updatefromcrowdin.py

Das updatefromcrowdin.py Skript schiebt Änderungen aus crowdin auf Dein lokales FreeCAD/-Verzeichnis.

## Die neuesten Begriffe (strings) nach crowdin senden 

-   nur auf Linux getestet;
-   es muss eine \'.credentials\'-Datei im lokalen /home/YourUser Vezeichnis existieren. Diese einfache Textdatei enthält nur eine Zeile mit dem API-Schlüssel (key), den man von <https://crowdin.com/project/freecad/settings#api> bekommt (nur für Administratoren)
-   das Repository muß sauber sein (git pull, git stash, wenn erforderlich);
-   cd /path/to/freecad-source-code/src/Tools
-   \'python updatets.py\' befüllt alle \'.ts\'-Dateien aus dem Quellcode mit den neuesten Begriffen (strings)
-   \'python updatecrowdin.py update\' sendet alle \'.ts\'-Dateien nach crowdin. Crowdin aktualisiert nur neue Begriffe;
-   \'cd ../..\' zurück zum Wurzelverzeichnis des Quellcodes;
-   \'git checkout .\' hebt alle Änderungen an den \'.ts\'-Dateien auf; es gibt keinen Grund, sie jetzt schon festzulegen, da sie noch nicht übersetzt sind;

## Die neuesten Übersetzungen aus crowdin zusammenführen 

-   nur auf Linux getestet;
-   es muss eine \'.credentials\'-Datei im lokalen /home/YourUser Vezeichnis existieren. Diese einfache Textdatei enthält nur eine Zeile mit dem API-Schlüssel (key), den man von <https://crowdin.com/project/freecad/settings#api> bekommt (nur für Administratoren)
-   das Repository muß sauber sein (git pull, git stash, wenn erforderlich);
-   cd /path/to/freecad-source-code/src/Tools
-   \'python updatecrowdin.py build\' (erstellt eine zip-Datei auf crowdin mit allen Dateien (dies kann eine Weile dauern). Dieser Schritt kann auch auf der crowdin-Website ausgeführt werden.
-   \'python updatecrowdin.py download\' holt eine freecad.zip-Datei in dieses Verzeichnis;
-   \'mv freecad.zip \~\' verschiebt die zip-Datei ins lokale home-Verzeichnis, um zu vermeiden, dass sie später versehentlich übergeben wird;
-   (optional) das \'updatefromcrowdin.py\'-Skript öffnen und prüfen, ob die vorgegebenen Sprachen (default\_languages) alle gewünschten enthalten (im Grunde sind das mehr als 50%)
-   python updatefromcrowdin.py -z /home/YourUser/freecad.zip
-   cd ../.. (go back to the source code root folder)
-   wenn etwas schief ging oder man ist sich nicht sicher, mit \'git checkout .\' bereinigen;
-   wenn alles in Ordnung ist, (git status), mit \'git add . && git commit\' übergeben;
-   einen PR auf FreeCAD erzeugen;

## Eine Übersetzungsdatei der Website erstellen 

-   das Repository der Homepage kopieren;
-   cd /path/to/FreeCAD-homepage;
-   xgettext \--from-code=UTF-8 -o lang/homepage.pot \*.php;
-   \"homepage.po\" auf crowdin manuell mit der \'lang/homepage.pot\'-Datei aktualisieren;

## Die Übersetzungen der Website aktualisieren 

-   die freecad.zip-Datei entweder von crowdin abholen oder den Anweisungen zu \'python updatecrowdin.py download\' oben folgen;
-   cd /path/to/FreeCAD-homepage;
-   das Repository muß sauber sein (git pull, git stash, wenn erforderlich);
-   python updatefromcrowdin.py -z /path/to/freecad.zip;
-   wenn etwas schief ging oder man ist sich nicht sicher, mit \'git checkout .\' bereinigen;
-   wenn alles in Ordnung ist, (git status), mit \'git add . && git commit\' übergeben;
-   einen PR auf die FreeCAD-Homepage erzeugen;
-   nachdem die PR zusammengeführt wurde, wird einer der Administratoren per ftp das Ergebnis auf den webhost schieben.

## Verwandtes

-   [Übersetzungen](Localisation/de.md)
-   [crowdin - Verwaltung](Crowdin_Administration/de.md)
-   [Freigabeprozess](Release_process.md)




[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Administration{{\#translation:}}](Category:Administration.md)
