# Download/fr
{{TOCright}}

## Version stable courante 

La version 0.19.3 initiale de FreeCAD (24366) a été publiée le 04 décembre 2021. Pour découvrir les nouveautés, consultez les [notes de version](Release_notes_0.19/fr.md).

Vous pouvez trouver des checksums SHA256 pour vérifier l\'intégrité de votre téléchargement sur la [0.19.3 page des releases](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.3).

Les versions précédentes peuvent être téléchargées à partir de la page [releases](https://github.com/FreeCAD/FreeCAD/releases).

+:---------------------------------------------------------------------------------------------------------------------------------:+---+:---------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------:+
| ![](images/Windows.png )                                                                                                    |   | ![](images/Mac.png )                                                                                          |   | ![](images/AppImage-logo.png ) |
|                                                                                                                                   |   |                                                                                                                 |   |                                            |
| Install on Windows                                                                                                                |   | Install on Mac                                                                                                  |   | Install on Linux                           |
|                                                                                                                                   |   |                                                                                                                 |   |                                            |
| [64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD-0.19.3-WIN-x64-installer-2.exe) (includes installer) |   | [macOS 64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-OSX-x86_64-conda.dmg) |   | [AppImage 64-bit](AppImage.md)     |
+-----------------------------------------------------------------------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------------------------------+---+--------------------------------------------+

### Notes aux utilisateurs de Windows 

-   Les versions suivantes de Windows sont prises en charge : 7/8/10/11.
-   Une version portable qui ne nécessite pas d\'installation est disponible sur la page [releases](https://github.com/FreeCAD/FreeCAD/releases/).
-   Le paquet peut également être installé à partir du gestionnaire [Chocolatey](https://chocolatey.org/packages/freecad).

### Notes aux utilisateurs de MacOS X 

MacOS OS X 10.12 Sierra est la version minimum compatible.

### Note aux utilisateurs de GNU/Linux 

La plupart des distributions portent FreeCAD dans leurs référentiels officiels. Toutefois, si la distribution ne suit pas un modèle de version évolutive, la version fournie peut être obsolète. À la place, vous pouvez télécharger l'AppImage ci-dessus, le marquer comme exécutable et le lancer sans installation.

Veuillez consulter la page [Installation sous Unix](Installing_on_Linux/fr.md) pour plus d\'options d\'installation, y compris les paquets quotidiens pour Ubuntu et ses dérivés.

Une version portable qui n\'a pas besoin d\'installation peut être obtenue en démarrant FreeCAD avec ces commandes : {{Version/fr|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-24366-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-24366-Linux-Conda_glibc2.12-x86_64.AppImage
```

Vous pourrez trouver plus d\'informations sur les variables d\'environnement de FreeCAD sur [la page de configuration](Start_up_and_Configuration/fr.md).

## Versions de développement 

FreeCAD est en développement constant.

-   Pour les utilisateurs de Linux, consultez le développement [AppImage](AppImage/fr.md).
-   Pour les versions de développement MacOS et Windows et le développement du code source, consultez la page [weekly builds](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Pour compiler le dernier code source, voir [Compiler](Compiling/fr.md).

## Modules additionnels et macros 

La communauté FreeCAD propose une multitude de modules supplémentaires et de macros. Depuis la version 0.17, ils peuvent être installés directement depuis FreeCAD à l\'aide du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

---
[documentation index](../README.md) > Download/fr
