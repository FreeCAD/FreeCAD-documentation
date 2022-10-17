# Continuous Integration/de
{{TOCright}}

## Kontinuierliche Integration 

Aktuell stößt das FreeCAD-Repository auf GitHub einen Build auf den beiden unten genannten [CI](https   *//de.wikipedia.org/wiki/Kontinuierliche_Integration)-Systemen an. Durch diese sind plattformübergreifend praktisch alle wichtigen Betriebssysteme (Linux, MacOSX und Windows) abgedeckt. CIs können auch für [Erprobung](Testing/de.md) verwendet werden.

### TravisCI

<img alt="" src=images/Travis-logo.png  style="width   *50px;"> Tests gegen Linux und OSX. Die Konfigurationsdatei namens [.travis.yml](https   *//github.com/FreeCAD/FreeCAD/blob/master/.travis.yml) ist im obersten Verzeichnis von FreeCAD zu finden. Aktuelle und vergangene Builds sind [hier](https   *//travis-ci.com/FreeCAD/FreeCAD/builds) zu finden.

### Appveyor

<img alt="" src=images/Appveyor.svg  style="width   *40px;"> Tests gegen Windows. Die Konfigurationsdatei namens [appveyor.yml](https   *//github.com/FreeCAD/FreeCAD/blob/master/appveyor.yml) ist im obersten Verzeichnis von FreeCAD zu finden. Aktuelle und vergangene Appveyor-Builds sind [hier](https   *//ci.appveyor.com/project/yorikvanhavre/freecad/history) zu finden.

## Tipps

\- Durch Hinzufügen von [skip ci] oder [ci skip] zu einem git-Commit wird ein CI-Build abgebrochen.

### Relevante Verweise 

-   [LGTM](LGTM.md)





 

[Category   *Developer_Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Testing](Category_Testing.md) > Continuous Integration/de
