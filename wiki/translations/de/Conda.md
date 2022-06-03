# Conda/de
## Einführung


{{TOCright}}

Diese Seite soll Conda als Paket-, Abhängigkeits- und Umgebungsmanager für FreeCAD vorstellen.

Momentan katalogisiert diese Seite hauptsächlich Links zu relevanten Diskussionen im FreeCAD Forum und anderen Orten im Web, aber die Hoffnung besteht darin, die wichtigsten Punkte aus diesen Verweisen auf dieser Seite zu dokumentieren.

Es gibt auch ein (engl.) [Video Tutorial](https   *//www.youtube.com/watch?v=sCs8xlrw2nM) mit dem Inhalt dieser Seite.

## Motivation

Die Motivation für den Einsatz von Conda ist vielfältig, ebenso wie der Zweck von Conda.

Lasse es uns aufschlüsseln.

### Conda als Paketverwalter 

Zuerst ist Conda ein Paketmanager - ähnlich wie apt oder pip.

Das bedeutet, dass wir **Pakete** mit einem einfachen conda install von verschiedenen [Kanälen](https   *//docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html#what-is-a-conda-channel) wie z.B. [conda-forge](https   *//conda-forge.org/) installieren können.

Conda Forge ist analog zu [the Python Paket Index (PyPI)](https   *//pypi.org/), einem Gemeinschaftskanal, der aus Tausenden von Mitwirkenden besteht, und dient [Freecad](https   *//anaconda.org/conda-forge/freecad) als Conda Paket.

### Conda als ein Abhängigkeitsverwalter 

Als nächstes ist Conda ein Abhängigkeitsverwalter, ebenfalls ähnlich wie apt oder pip.

Conda kann die Abhängigkeiten verwalten und die Abhängigkeiten für ein Projekt wie FreeCAD installieren.

Warum nicht einfach pip verwenden? pip funktioniert wirklich gut für die Verwaltung der Abhängigkeiten von Projekten, die *nur* Python verwenden.

Conda arbeitet für mehrere Sprachen und ist daher besser geeignet, um die Abhängigkeiten von Projekten wie FreeCAD zu verwalten, die Abhängigkeiten über eine Vielzahl von Sprachen wie C / C++ und Python haben.

### Conda als ein Umgebungsverwalter 

Conda hat das Konzept einer [Umgebung](https   *//docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html), die die einzigartige Kombination von Paketen und Versionen darstellt, die zum Betrieb einer Software benötigt wird. Zum Beispiel ein FreeCAD Arbeitsbereich.

Mit Umgebungen können Sie diese leicht \"aktivieren\" und \"deaktivieren\" oder zwischen Versionen von Paketen wechseln, die für bestimmte Software benötigt werden.

Dies ist nützlich, um zu testen, wie sich ein Arbeitsbereich mit einem bestimmten Satz von Paketen verhält. Zum Beispiel, wie verhält sich ein Arbeitsbereich in FreeCAD 18.4 gegenüber 19?

Conda Umgebungen ermöglichen es dir, dieselbe exakte Umgebung auf verschiedenen Rechnern zu reproduzieren.

Zum Beispiel mehrere lokale Entwicklerrechner oder ein entfernter Build Server, der von Travis CI bereitgestellt wird.

## Conda einrichten 

1\. [Miniconda einrichten](https   *//docs.conda.io/en/latest/miniconda.html).

2\. Überprüfe, ob deine Installation erfolgreich war und machen dich mit dem conda **CLI**\' vertraut. $ conda --help

## Einrichtung von FreeCAD mit Conda 

Zuerst musst du entscheiden, ob du eine **stabile** Version von FreeCAD installierst oder mit dem neuesten **instabilen** Code von FreeCAD master experimentieren willst.

Stabile freigegebene Versionen von FreeCAD werden auf dem conda-forge Kanal angeboten, während die neueste Version von FreeCAD master auf dem Kanal freecad/label/dev angeboten wird.

  Conda Kanal           Stabil?
   
  conda-forge         Ja ✔️
  freecad/label/dev   Nein ❌

Zweitens, da du leicht dedizierte Umgebungen in conda erstellen kannst, ist es empfehlenswert, eine für FreeCAD zu erstellen.

Der create Befehl ermöglicht es dir, eine Umgebung aus einer Liste von angegebenen Paketen zu erstellen. In unserem Fall wollen wir eine Umgebung namens \"fcenv\" (engl. FreeCAD environment; kurz für FreeCAD Umgebung) aus dem Paket freecad erstellen und conda anweisen, nach dem Paket freecad mit dem Kanal conda-forge zu suchen. 
```python
conda create --name fcenv --channel conda-forge freecad
``` **Tip   *** Du kannst alternativ conda anweisen, immer conda-forge zu suchen, wenn du Pakete mit dem folgenden Befehl installierst   * 
```python
conda config --add channels conda-forge
``` Die wöchentlichen Bauten können über den Kanal freecad/label/dev wie folgt installiert werden   * 
```python
conda create --name fcenv-dev --channel freecad/label/dev freecad
```

## FreeCAD Forum Diskussion 

-   [Lasse uns über Conda sprechen](https   *//forum.freecadweb.org/viewtopic.php?t=39656)
-   [Verpackungslösung   * (ana)conda](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=15197)
-   [FreeCAD Conda Verteilung](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=45582)

## Siehe Auch 

-   <https   *//docs.conda.io/en/latest/>
-   <https   *//conda-forge.org/docs/>
-   <https   *//docs.conda.io/projects/conda-build/en/latest/>
-   <https   *//anaconda.org/conda-forge/freecad>
-   <https   *//anaconda.org/freecad/freecad>
-   <https   *//github.com/FreeCAD/FreeCAD_Conda>
-   <https   *//github.com/FreeCAD/FreeCAD-AppImage>

[Category   *Developer\_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Conda/de
