





{{TOCright}}

## Intégration continue 

Actuellement, le dépôt FreeCAD sur GitHub déclenchera une construction sur les deux systèmes de CI ci-dessous. Avec ces systèmes, les principaux systèmes d\'exploitation sont couverts : Linux, MacOSX et Windows. Les CIs peuvent également être utilisés pour exécuter des [tests unitaires](Testing/fr.md).

### TravisCI

<img alt="" src=images/Travis-logo.png  style="width:50px;"> Tests sous Linux et OSX. Le fichier de configuration s\'appelle [.travis.yml](https://github.com/FreeCAD/FreeCAD/blob/master/.travis.yml) et il se trouve dans le répertoire principal de FreeCAD. Pour afficher les versions actuelles et antérieures : <https://travis-ci.org/FreeCAD/FreeCAD/builds>

### Appveyor

<img alt="" src=images/Appveyor.svg  style="width:40px;"> Tests sous Windows. Le fichier de configuration s\'appelle [appveyor.yml](https://github.com/FreeCAD/FreeCAD/blob/master/appveyor.yml) et il est dans le répertoire principal de FreeCAD. Pour afficher les versions actuelles et précédentes d\'Appveyor : <https://ci.appveyor.com/project/yorikvanhavre/freecad/history>

## Conseils

\- Si vous ajoutez [skip ci] ou [ci skip] à un git commit, cela annulera la compilation du CI.

### Liens pertinents 

-   [LGTM](LGTM/fr.md)





 

[Category:Developer\_Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Testing{{\#translation:}}](Category:Testing.md)
