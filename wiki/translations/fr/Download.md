# Download/fr
{{TOCright}}

## Version stable courante 

La version 0.20 de FreeCAD (29177) a été publiée le 14 juin 2022. Pour découvrir ses nouveautés, consultez les [notes de version](Release_notes_0.20/fr.md).

Vous pouvez trouver des checksums SHA256 pour vérifier l\'intégrité de votre téléchargement sur la [page de la release 0.20](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.20).

Les versions précédentes peuvent être téléchargées à partir de la page [releases](https   *//github.com/FreeCAD/FreeCAD/releases).

+   *   *+---+   *   *+---+   *   *+
| ![](images/Windows.png )                                                                                       |   | ![](images/Mac.png )                                                                                |   | ![](images/Linux_with_text.png )     |
|                                                                                                                      |   |                                                                                                       |   |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                               |   | [Install on Mac](Installing_on_Mac.md)                                                        |   | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                      |   |                                                                                                       |   |                                                    |
| [64-bit installer](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20/FreeCAD-0.20.0-WIN-x64-installer-1.exe) |   | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20/FreeCAD-0.20.0-OSX-i386.dmg) |   | [AppImage 64-bit](AppImage.md)             |
++---++---++

### Notes aux utilisateurs de Windows 

-   Les versions suivantes de Windows sont prises en charge    * 64-bit 7/8/10/11. Windows 32 bits n\'est pas pris en charge.
-   Une version portable qui ne nécessite pas d\'installation est disponible sur la page [releases](https   *//github.com/FreeCAD/FreeCAD/releases/).
-   Le paquet peut également être installé à partir du gestionnaire [Chocolatey](https   *//chocolatey.org/packages/freecad).

### Notes aux utilisateurs de Mac OS X 

Mac OS X 10.12 Sierra est la version minimum compatible.

### Notes aux utilisateurs de GNU/Linux 

La plupart des distributions portent FreeCAD dans leurs référentiels officiels. Toutefois, si la distribution ne suit pas un modèle de version évolutive, la version fournie peut être obsolète. À la place, vous pouvez télécharger l'AppImage ci-dessus, le marquer comme exécutable et le lancer sans installation.

Veuillez consulter la page [Installation sous Unix](Installing_on_Linux/fr.md) pour plus d\'options d\'installation, y compris les paquets quotidiens pour Ubuntu et ses dérivés.

Une version portable qui n\'a pas besoin d\'installation peut être obtenue en démarrant FreeCAD avec ces commandes    * {{Version/fr|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD-0.20.0-Linux-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD-0.20.0-Linux-x86_64.AppImage
```

Vous pourrez trouver plus d\'informations sur les variables d\'environnement de FreeCAD sur [la page de configuration](Start_up_and_Configuration/fr.md).

## Versions de développement 

FreeCAD est en développement constant.

-   Pour les utilisateurs de Linux, consultez le développement [AppImage](AppImage/fr.md).
-   Pour les versions de développement MacOS et Windows et le développement du code source, consultez la page [weekly builds](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Pour compiler le dernier code source, voir [Compiler](Compiling/fr.md).

## Modules additionnels et macros 

La communauté FreeCAD propose une multitude de modules supplémentaires et de macros. Depuis la version 0.17, ils peuvent être installés directement depuis FreeCAD à l\'aide du <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/fr
