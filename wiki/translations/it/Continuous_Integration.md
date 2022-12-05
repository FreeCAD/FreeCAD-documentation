# Continuous Integration/it
{{TOCright}}

## Integrazione Continua 

Attualmente il repository di FreeCAD su GitHub attiverà una build sui due sistemi CI seguenti. Tra questi sistemi sono coperti praticamente tutti i principali sistemi operativi multipiattaforma Linux, MacOSX e Windows. Gli elementi della configurazione possono essere utilizzati anche per eseguire [unità test](Testing/it.md).

### TravisCI

<img alt="sinistra" src=images/Travis-logo.png  style="width:50px;"> Test su Linux e OSX. Il file di configurazione si chiama [.travis.yml](https://github.com/FreeCAD/FreeCAD/blob/master/.travis.yml) e si trova nella directory principale di FreeCAD. Per visualizzare le build attuali e passateː <https://travis-ci.com/FreeCAD/FreeCAD/builds>

### Appveyor

<img alt="" src=images/Appveyor.svg  style="width:40px;"> Test su Windows. Il file di configurazione si chiama [appveyor.yml](https://github.com/FreeCAD/FreeCAD/blob/master/appveyor.yml) e si trova nella directory principale di FreeCAD. Per visualizzare le build di Appveyor correnti e precedentiː <https://ci.appveyor.com/project/yorikvanhavre/freecad/history>

## Suggerimenti

\- Se aggiungi [skip ci] o [ci skip] a un git commit, verrà annullata una build CI.

### Collegamenti rilevanti 

-   [LGTM](LGTM.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Testing](Category_Testing.md) > Continuous Integration/it
