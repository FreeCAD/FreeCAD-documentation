# Continuous Integration/es
{{TOCright}}


<div class="mw-translate-fuzzy">

## Integración continua 

Actualmente, el repositorio de FreeCAD en GitHub activará una compilación en los dos sistemas de CI a continuación. Entre estos sistemas, casi todos los principales sistemas operativos multiplataformas están cubiertos: Linux, MacOSX y Windows. Los CI también se pueden usar para ejecutar [unit tests](Testing.md)..


</div>

### TravisCI

<img alt="" src=images/Travis-logo.png  style="width:50px;"> Tests against Linux and OSX. The config file is called [.travis.yml](https://github.com/FreeCAD/FreeCAD/blob/master/.travis.yml) and it lives in the top directory of FreeCAD. To view current and past buildsː <https://travis-ci.org/FreeCAD/FreeCAD/builds>

### Appveyor

<img alt="" src=images/Appveyor.svg  style="width:40px;"> Tests against Windows. The config file is called [appveyor.yml](https://github.com/FreeCAD/FreeCAD/blob/master/appveyor.yml) and it lives in the top directory of FreeCAD. To view current and previous Appveyor buildsː <https://ci.appveyor.com/project/yorikvanhavre/freecad/history>

## Consejos

\- Si agrega [skip ci] o [ci skip] a un git commit, se cancelará una compilación de CI.

### Relevant Links 

-   [LGTM](LGTM.md)


<div class="mw-translate-fuzzy">


{{docnav|Testing|Branding}}


</div>


 

_ _

---
[documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > Continuous Integration/es
