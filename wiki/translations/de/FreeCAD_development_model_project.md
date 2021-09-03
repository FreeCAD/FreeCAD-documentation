


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Diese Seite ist auf den Übergang des FreeCAD Codes in eine GIT Paketquelle und ein leistungsfähigeres Entwicklungsmodell ausgerichtet. Sie folgt den Regeln des \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\] Prozesses. Die Projekte sind im [Entwicklungsfahrplan](Development_roadmap/de.md) gesammelt.

## Zweck und Prinzipien {#zweck_und_prinzipien}

Dieses Projekt zielt darauf ab, ein neues Entwicklungs- und Verwaltungsmodell für FreeCAD zu definieren. Wir kommen zu einem Punkt, an dem eine SVN Paketquelle schwer zu verwalten ist. Arbeiten mit Patches ist ärgerlich und kompliziert für Leute, die bereit sind, Code beizutragen. Jedem den Schreibzugriff auf das SVN Repo zu ermöglichen, ist gefährlich. Menschen können unbeabsichtigt etwas im Basissystem brechen oder schmackhafte Entscheidungen erzwingen.

Ich schaue mir also den Linux Entwicklungsprozess an, der im Moment vielleicht zu groß für unsere Schuhe ist, aber nichtsdestotrotz! Das bedeutet Git als verteiltes Versionskontrollsystem (DVCS), Mailinglisten und Unterbetreuer (Leutnants).

## Ergebnis

## Ideenfindung

### Git

-   Verwendung von Git als neues Versionskontrollsystem
-   SVN beibehalten (zumindest für eine Weile)
    -   es als eine Art Freigabe Paketquelle verwenden, um die ppa Arbeitsabläufe und die schönen Revisionsnummern zu erhalten
    -   SVN einschränken schreibt an Werner, Yorik und Jurgen (offizieller Baum)
    -   alle anderen Dinge, wie Entwicklung, Zweige, Experimente gehen in Git!
    -   **Option:** wechseln komplett zu Git
        -   würde einige Sicherheiten in Versionsnummerierung und ppa Builds geben\....
-   würde allen Interessierten Schreibrechte (Push) geben

### Entwicklungs Mailingliste {#entwicklungs_mailingliste}

Das Forum hat seine Grenzen, ich würde die eine oder mehrere Mailinglisten verwenden, um Zweige zu verwalten und Anfragen zu ziehen. Das hat Vorteile:

-   kann offline arbeiten
-   benutze die leistungsfähige Suche des Mail Clients
-   keine Einschränkungen bei Anhängen und Größen

### Verantwortlichkeiten klären {#verantwortlichkeiten_klären}

Wir werden bald mehr und mehr Entwickler werden und die Nutzer werden widersprüchliche Funktionswünsche haben. Wir brauchen eine Struktur und Verantwortlichkeiten, um solche Anfragen und eingehende Anfragen zu filtern und zu entscheiden. Code.

#### Intensivieren

Adrian Przekwas:
Öffentlichkeitsarbeit - G+, Youtube,
Tutorien - [http://freecad-tutorial.blogspot.com](http://freecad-tutorial.blogspot.com)
Übersetzungen (unsicher) - Polnisch (Wiki, Crowdin)

Yorik van Havre:
Software: Arch Modul, Daft Modul, Bildgestaltung
Dokumentation: allgemeine Wiki Organisation und  Gestaltung
Übersetzung: französisch, niederländisch, brasilianisches  portugiesisch
Publicity: articles on [http://yorik.uncreated.net/guestblog.php](http://yorik.uncreated.net/guestblog.php), G+, facebook

## Organisieren

Die beschlossenen Regeln und Informationen gehen an das [FreeCAD Entwicklungsmodell](FreeCAD_development_model/de.md) Dokument.

## Nächste Handlungen {#nächste_handlungen}



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
