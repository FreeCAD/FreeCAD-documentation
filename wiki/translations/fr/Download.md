# Download/fr
## Version stable actuelle 

La version 0.21.2 de FreeCAD a été publiée le 14 novembre 2023. Pour connaître les nouveautés, voir les [notes de version](Release_notes_0.21/fr.md).

Vous pouvez trouver les checksums SHA256 pour vérifier l\'intégrité de votre téléchargement sur la [page GitHub de la release 0.21.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.21.2).

Les versions précédentes peuvent être téléchargées à partir de la page [GitHub releases](https://github.com/FreeCAD/FreeCAD/releases).

+::+::+::+
| ![](images/Windows.png )                                                                                                | ![](images/Mac.png )                                                                                                | ![](images/Linux_with_text.png )                                                                        |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [Install instructions](Installing_on_Windows.md)                                                                      | [Install instructions](Installing_on_Mac.md)                                                                  | [Install instructions](Installing_on_Linux.md)                                                                |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-WIN-x64-installer-1.exe)        | [ARM (M1/M2) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-arm64.dmg)  | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-x86_64.AppImage)   |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Windows-x86_64.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-intel-x86_64.dmg) | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-aarch64.AppImage) |
++++



### Remarques pour les utilisateurs de Windows 

-   Les versions suivantes de Windows sont prises en charge : 64-bit 7/8/10/11. Windows 32 bits n\'est pas pris en charge.
-   Le paquet peut également être installé à partir du gestionnaire [Chocolatey](https://chocolatey.org/packages/freecad). Le paquet Chocolatey n\'est actuellement pas à jour.



### Remarques pour les utilisateurs de macOS 

-   MacOS 10.12 Sierra est la version minimale supportée.
-   Pour macOS 12 et les versions antérieures, l\'image disque Intel non signée doit être utilisée, la version signée ne fonctionne pas sur ces systèmes.



### Remarques pour les utilisateurs de GNU/Linux 

La plupart des distributions portent FreeCAD dans leurs dépôts officiels. Toutefois, si la distribution ne suit pas un modèle de version évolutive, la version fournie peut être obsolète. À la place, vous pouvez télécharger l'AppImage ci-dessus, la marquer comme exécutable et la lancer sans installation.

Veuillez consulter la page [Installation sous Unix](Installing_on_Linux/fr.md) pour plus d\'options d\'installation, y compris les paquets quotidiens pour Ubuntu et ses dérivés.

Une version portable qui n\'a pas besoin d\'installation peut être obtenue en démarrant FreeCAD avec ces commandes :


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Vous pourrez trouver plus d\'informations sur les variables d\'environnement de FreeCAD sur [la page de configuration](Start_up_and_Configuration/fr.md).



## Versions de développement 

FreeCAD est en développement constant.

-   Pour les versions de développement et le code source de développement, voir la page [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).
-   Pour compiler le dernier code source, voir [compilation](Compiling/fr.md).



## Modules supplémentaires et macros 

La communauté FreeCAD propose une multitude de modules supplémentaires et de macros. Depuis la version 0.17, ils peuvent être installés directement depuis FreeCAD à l\'aide du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).



---
⏵ [documentation index](../README.md) > Download/fr
