# Continuous Integration/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

## Integrare continuă 

În prezent, repo-ul FreeCAD de pe GitHub va declanșa o construire pe cele două sisteme CI de mai jos. Între aceste sisteme, aproape toate principalele platforme OS-uri sunt acoperite de Linux, MacOSX și Windows. CI-urile pot fi, de asemenea, folosite pentru a rula [ unit tests](Testing.md).


</div>


<div class="mw-translate-fuzzy">

### TravisCI

<img alt="" src=images/Travis-logo.png  style="width:50px;"> Testeză comportamentul sub Linux și OSX. Fișierul de configurare se numește [.travis.yml](https://github.com/FreeCAD/FreeCAD/blob/master/.travis.yml) și se află în directorul de bază al FreeCAD. Pentru a vedea versiunea curentă și cele trecute: <https://travis-ci.org/FreeCAD/FreeCAD/builds>


</div>

### Appveyor

<img alt="" src=images/Appveyor.svg  style="width:40px;"> Testează sub Windows. Fișierul de configurare se numește [appveyor.yml](https://github.com/FreeCAD/FreeCAD/blob/master/appveyor.yml) și trăiește în directorul de top al FreeCAD. Appveyor construiește <https://ci.appveyor.com/project/yorikvanhavre/freecad/history>

## Sugestii

Dacă adăugaţi [skip ci] sau [ci skip] pentru comiterea unui \"git\", aceasta va anula o formare a CI.

### Relevant Links 

-   [LGTM](LGTM.md)


<div class="mw-translate-fuzzy">


{{docnav|Testing|Branding}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Testing](Category_Testing.md) > Continuous Integration/ro
