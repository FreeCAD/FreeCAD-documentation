 {{VeryImportantMessage|Roboter sind von Natur aus gefährlich, da sie automatisch viel Schaden anrichten können. Verwende sie mit äußerster Vorsicht!}}

## Übersicht

Wiederkehrende Aufgaben können mit Hilfe von Robotern oder Bots automatisiert werden, d.h. mit Softwareprogrammen, die selbstständig auf dem Wiki arbeiten.

Die natürlichen und am häufigsten verwendeten Roboter für Wiki Seiten werden von MediaWiki unter dem Paketnamen Pywikibot zur Verfügung gestellt. Siehe [Handbuch:Pywikibot](http://www.mediawiki.org/wiki/Manual:Pywikibot) für die vollständigen Informationen.

Kurz gesagt, Pywikibot ist eine Sammlung von Python Skripten, die die native Wiki API verwenden können, um auf Wiki Seiten zu agieren. Um die API Liste für das FreeCAD Wiki zu sehen, besuche <http://www.freecadweb.org/wiki/api.php>

Um Pywikibot verwenden zu können, musst du dies tun:

1.  installiere das Pywikibot Paket
2.  konfiguriere Pywikibot so, dass es im FreeCAD Wiki funktioniert
3.  starte die Skripte, die du für die anstehende Aufgabe benötigst

Es gibt eine Fülle von Informationen über die Installation, Konfiguration und Benutzung von Pywikibot. Bitte beachte jedoch, dass diese Informationen zwar nützlich, aber auch irreführend sein können, da sie Anweisungen vermischen, die sich auf zwei verschiedene Pywikibot Codebasen und verschiedene Versionen der Pywikibot Skriptsammlung beziehen.

Im Folgenden findest du die grundlegenden Anweisungen zum Einrichten und Verwenden von Pywikibot im FreeCAD Wiki. Damit kannst du die gängigsten Aufgaben durchführen. Für fortgeschrittene Nutzung findest du das [Handbuch:Pywikibot](http://www.mediawiki.org/wiki/Manual:Pywikibot) und den Python Quellcode.

## Einrichtung

Gehe zu <http://tools.wmflabs.org/pywikibot/> und lade {{FileName|package/pywikipedia/core.zip}} herunter (das Projekt steht auch unter github, gerrit, usw., aber dies ist ein einfacher Weg, um ein vollständig in sich geschlossenes Paket zu erhalten).

Entpacke den Inhalt in deinem bevorzugten Verzeichnis.

Wenn du die Bibliotheken nicht in deine Python Bibliotheken installieren willst, bist du fertig (wenn du sie immer noch installieren willst, überprüfe die Datei {{FileName|INSTALL}} im Basisverzeichnis).

Pywikibot funktioniert mit Python 2.6 und 2.7 ohne Probleme. Python 3 wurde bisher nicht mit FreeCAD wiki getestet und funktioniert ebenfalls.

## Konfiguration

Du musst den folgenden Python Code als Datei mit dem Namen {{FileName|user-config.py}} in dem Basisverzeichnis speichern, in das du entpackt hast {{FileName|package/pywikipedia/core.zip}} (zur Verdeutlichung: im gleichen Verzeichnis, in dem sich bereits eine Datei namens {{FileName|user-config.py.sample}} befindet).


```python
# -*- coding: cp437  -*-
family = 'freecadwiki'
mylang = 'en'
usernames['freecadwiki']['en'] = u'<<yourWikiUserName>>'
#usernames['freecadwiki']['freecadwiki'] = u'<<yourWikiUserName>>'
console_encoding = 'cp437'
```

Im obigen Code:

-   ersetze *\<\>* durch deinen Wiki-Benutzernamen
-   ersetze *cp437* durch dein *console\_encoding*. Um dein \"console encoding\" unter Windows bzw. Linux herauszufinden, starte den Python-Interpreter und gib {{SystemInput|import sys}} gefolgt von {{SystemInput|print sys.stdout.encoding}} ein. Python wird dein {{SystemOutput|console_encoding}} auf dem Bildschirm anzeigen.

Dann musst du den folgenden Python-Code in einer Datei unter dem Namen {{FileName|freecadwiki_family.py}} im Unterverzeichnis {{FileName|/pywikibot/families}} (zusammen mit den anderen {{FileName|family_xxx.py}} Dateien) speichern.


```python
# -*- coding: utf-8  -*-

__version__ = '$Id: 7f3891c3bbbfbd69c0b005de953514803d783d92 $'

from pywikibot import family


# The MediaWiki family
# user-config.py: usernames['mediawiki']['mediawiki'] = 'User name'
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'freecadwiki'

        self.langs = {
            'en': 'www.freecadweb.org',
        }

    def scriptpath(self, code):
        return 'wiki'

    def path(self, code):
        return '/index.php' #The path of index.php, look at your wiki address. 
     
    def apipath(self, code):
        return '/api.php' #The path of api.php

    def version(self, code):
        # Replace with the actual version being run on your wiki
        return '1.20.3'

    def protocol(self, code):
        """
        Can be overridden to return 'https'. Other protocols are not supported.
        """
        return 'http'
        #return 'https' # My server uses https
```

## Anwendung

Du kannst nun die Pywikibot-Skripte ausführen. Die Skripte selbst sind im {{FileName|/scripts}}-Unterverzeichnis enthalten.

Um die Skripte auszuführen, öffne eine Shell und gehe zum Basisverzeichnis (der Installation, NICHT des {{FileName|/scipts}}-Unterverzeichnisses) und gib ein


{{SystemInput|python pwb.py <<scriptname>>.py -<<parameter>>}}

wo du natürlich \"\<\>\" durch den Namen des Skripts ersetzt, das du ausführen willst und \"\<\" durch den/die erforderlichen Parameter für das Skript.

Für eine Beschreibung von Anwendung und Parametern für ein beliebiges Skript benutze einfach den Parameter \"-help\". Um bspw. eine Beschreibung für das {{FileName|replace.py}}-Skript zu erhalten, tippe


{{SystemInput|python pwb.py replace.py -help}}

Es gibt einen weiteren sehr hilfreichen Parameter, der für alle diese Skripte gültig ist, genannt \"-simulate\", der es dir erlaubt, Befehle auszuprobieren, ohne das Wiki zu verändern. Benutze ihn, bevor du \'live\' gehst.

## Beispiele

Dieser Befehl loggt sich in das Wiki ein


{{SystemInput|pwb.py login.py}}

Dieser Befehl druckt eine Liste aller Seiten, die einen Verweis auf SourceForge enthalten


{{SystemInput|pwb.py listpages.py -weblink:sourceforge.net}}

Dieser Befehl ersetzt alle Verweise auf das alte SourceForge Forum durch einen Verweis auf das neue freecadweb.org bereitgestellte Forum


{{SystemInput|pwb.py replace.py -weblink:sourceforge.net/apps/phpbb/free-cad "sourceforge.net/apps/phpbb/free-cad" "forum.freecadweb.org"}}

Dieser Befehl druckt eine Liste aller Seiten, die das Wort \"PartDesign\" enthalten, beginnend mit der Seite \"2d Drafting Module\" und weiter alphabetisch geordnet


{{SystemInput|pwb.py listpages.py -start:"2d Drafting Module" -grep:PartDesign}}

Dieser Befehl ersetzt alle sicheren Verweise auf das alte SourceForge Forum durch einen Verweis auf das neue freecadweb.org bereitgestellte Forum auf den übersetzten Seiten.


{{SystemInput|pwb.py replace.py -start:Translations:! "https://sourceforge.net/apps/phpbb/free-cad" "http://forum.freecadweb.org"}}

## FreeCAD Wiki Verwandte Befehle {#freecad_wiki_verwandte_befehle}

Zählt alle Seiten, in denen eine bestimmte Wiki Vorlage verwendet wird


{{SystemInput|python3 pwb.py templatecount -count GuiCommand}}

Alle Seiten auflisten, in denen eine bestimmte Wiki Vorlage verwendet wird


{{SystemInput|python3 pwb.py templatecount -list GuiCommand}}

Ersetze eine Zeichenfolge in allen Seiten, die in der Kategorie Arch aufgeführt sind (a/k/a )


{{SystemInput|python3 pwb.py replace.py -cat:Arch}}

[Category:Arch](Category:Arch.md) [Category:Administration{{\#translation:}}](Category:Administration.md) [Category:Developer{{\#translation:}}](Category:Developer.md)
