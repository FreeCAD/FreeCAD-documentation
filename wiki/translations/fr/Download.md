# Download/fr
 {{TOCright}}

## Version stable courante 

La version 0.19.2 initiale de FreeCAD (24291) a été publiée le 22 avril 2021. Pour découvrir les nouveautés, consultez les [notes de version](Release_notes_0.19/fr.md).

Vous trouverez la somme de contrôle SHA256 (pour vérifier l\'intégrité de votre téléchargement) et la version portable pour Windows sur la [page Github des Releases 0.19.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Les versions précédentes peuvent être téléchargées à partir de la page [releases](https://github.com/FreeCAD/FreeCAD/releases).

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| [64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-installer1.exe) (includes installer) |   | [macOS](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD_0.19-24291-macOS-x86_64-conda.dmg) 64-bit |   | [AppImage](AppImage.md) 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+

### Notes aux utilisateurs de Windows 

-   L\'installateur 32 bits (x86) est compatible avec les versions de Windows suivantes : 7/8/10.
-   L\'installateur 64 bits (x64) est compatible avec les versions de Windows suivantes : 7/8/10.
-   Une version portable ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)), qui n\'a pas besoin d\'installation, est à la page des publications.
-   Le paquet peut également être installé à partir du gestionnaire [Chocolatey](https://chocolatey.org/packages/freecad).

### Notes aux utilisateurs de MacOS X 

MacOS OS X 10.12 *Sierra* est la version minimum compatible.

### Note aux utilisateurs de GNU/Linux 

La plupart des distributions portent FreeCAD dans leurs référentiels officiels. Toutefois, si la distribution ne suit pas un modèle de version évolutive, la version fournie peut être obsolète. À la place, vous pouvez télécharger l'AppImage ci-dessus, le marquer comme exécutable et le lancer sans installation.

Veuillez consulter la page [Installation sous Unix](Installing_on_Linux/fr.md) pour plus d\'options d\'installation, y compris les paquets quotidiens pour Ubuntu et ses dérivés.

Une version portable qui n\'a pas besoin d\'installation peut être obtenue en démarrant FreeCAD avec ces commandes : {{Version/fr|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

Vous pourrez trouver plus d\'informations sur les variables d\'environnement de FreeCAD sur [la page de configuration](Start_up_and_Configuration/fr.md).

## Versions de développement 

FreeCAD est en développement constant.

-   Pour les utilisateurs de Linux, consultez le développement [AppImage](AppImage/fr.md).
-   Pour les versions de développement MacOS et Windows et le développement du code source, consultez la page [weekly builds](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Pour compiler le dernier code source, voir [Compiler](Compiling/fr.md).

## Modules additionnels et macros 

La communauté FreeCAD propose une multitude de modules supplémentaires et de macros. Depuis la version 0.17, ils peuvent être installés directement depuis FreeCAD à l\'aide du [Gestionnaire d\'Addons](AddonManager/fr.md) <img alt="" src=images/AddonManager.svg  style="width:22px;">.



