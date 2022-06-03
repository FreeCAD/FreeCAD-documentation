# Continuous Integration/pl
{{TOCright}}

## Continuous Integration 

Currently the FreeCAD repository on GitHub will trigger a build on the below two CI systems. Between these systems pretty much all the main cross-platforms OSs are coveredː Linux, MacOSX, and Windows. CIs can also be used to run [unit tests](Testing.md).

### TravisCI

<img alt="" src=images/Travis-logo.png  style="width   *50px;"> Tests against Linux and OSX. The config file is called [.travis.yml](https   *//github.com/FreeCAD/FreeCAD/blob/master/.travis.yml) and it lives in the top directory of FreeCAD. To view current and past buildsː <https   *//travis-ci.org/FreeCAD/FreeCAD/builds>

### Appveyor

<img alt="" src=images/Appveyor.svg  style="width   *40px;"> Tests against Windows. The config file is called [appveyor.yml](https   *//github.com/FreeCAD/FreeCAD/blob/master/appveyor.yml) and it lives in the top directory of FreeCAD. To view current and previous Appveyor buildsː <https   *//ci.appveyor.com/project/yorikvanhavre/freecad/history>

## Tips

\- If you add [skip ci] or [ci skip] to a git commit it will cancel a CI build.

### Relevant Links 

-   [LGTM](LGTM.md)





 

[Category   *Developer\_Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Testing](Category_Testing.md) > Continuous Integration/pl
