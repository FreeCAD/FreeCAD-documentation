# LuxCoreRender/fr
**LuxCoreRender n'est pas officiellement pris en charge par l'[atelier Raytracing](Raytracing_Workbench/fr.md) mais par le nouvel [https   *//github.com/FreeCAD/FreeCAD-render atelier Render], qui est destiné à le remplacer. L'atelier Render peut être installé via le [Gestionnaire des extensions](Std_AddonMgr/fr.md).**

# Description

[LuxCoreRender](https   *//luxcorerender.org) est un moteur de rendu basé sur la physique, qui redémarre le [LuxRender](LuxRender/fr.md) désormais obsolète. Il n\'est pas officiellement supporté par l\'[atelier Raytracing](Raytracing_Workbench/fr.md), bien qu\'il puisse fonctionner.

# Installation

## Atelier Raytracing 


**Officiellement, l'[atelier Raytracing](Raytracing_Workbench/fr.md) ne fonctionne pas avec LuxCoreRender, mais uniquement avec l'ancien [LuxRender](LuxRender/fr.md). De plus, l'[atelier Raytracing](Raytracing_Workbench/fr.md) est remplacé par le nouvel [https   *//github.com/FreeCAD/FreeCAD-render atelier Render], qui est destiné à le remplacer. L'atelier Render peut être installé via le [Gestionnaire des extensions](Std_AddonMgr/fr.md). L'information ici est fournie parce que par défaut FreeCAD est toujours livré (à partir de 0.19-24276) avec l'atelier Raytracing**

.

### Version stable 

LuxCoreRender est en cours de développement actif, donc pour savoir quelle est la [dernière version stable vérifiez sur GitHub](https   *//github.com/LuxCoreRender/LuxCore/releases/latest).

#### Linux

***Binaires compilés***

Si votre distribution l\'a dans les dépôts officiels, vous pouvez installer LuxCoreRender et toutes les dépendances relatives via le gestionnaire de paquets. De telles distributions incluent    * [Arch Linux (AUR)](https   *//aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender), [Fedora](https   *//src.fedoraproject.org/rpms/luxcorerender).

Sinon, il est possible de télécharger les binaires officiels de la [dernière version stable de GitHub](https   *//github.com/LuxCoreRender/LuxCore/releases/latest). Le fichier sera quelque chose comme *luxcorerender-{numéro de version}-linux64.tar.bz2*. La solution la plus rapide (bien que ce ne soit pas la meilleure pratique) est d\'extraire le contenu de l\'archive dans un emplacement approprié, comme *\~/LuxCoreRender*. Si nécessaire, changez les permissions des fichiers pour que votre utilisateur puisse exécuter les fichiers que vous venez d\'extraire.

***Compilation à partir de la source***

Si votre distribution n\'a pas LuxCoreRender dans ses dépôts et que les binaires officiels ne fonctionnent pas sur votre ordinateur, ou si vous le souhaitez, il est possible de compiler LuxCoreRender à partir des sources. [La dernière version stable](https   *//github.com/LuxCoreRender/LuxCore/releases/latest) inclut la source, qui sera quelque chose comme \'luxcorerender-{numéro de version}.tar.bz2\'\'.

***Configuration de FreeCAD***

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Raytracing Préférences](Raytracing_Preferences/fr.md).

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, habituellement c\'est */usr/bin/luxcoreui* (ou si vous l\'avez installé manuellement quelque chose comme *\~/LuxCoreRender/luxcoreui*) et appliquez.

#### macOS

[Vérifiez sur GitHub la dernière version stable](https   *//github.com/LuxCoreRender/LuxCore/releases/latest), faites défiler vers le bas jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier macOS. Ce sera quelque chose comme *luxcorerender-{numéro de version}-mac64.dmg*.

#### Windows

[Vérifiez sur GitHub pour la dernière version stable](https   *//github.com/LuxCoreRender/LuxCore/releases/latest), descendez jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier Windows. Ce sera quelque chose comme *luxcorerender-{numéro de version}-win64.zip*.

Vérifiez ensuite dans la note au-dessus des actifs s\'il y a des notes sur les dépendances pour l\'utilisateur Windows. Par exemple, pour [utiliser LuxRender 2.5](https   *//github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5), vous devez installer le [Microsoft Visual C++ Redistributable for Visual Studio 2017](https   *//aka.ms/vs/15/release/vc_redist.x64.exe) et le [Intel C++ redistributable](https   *//software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).

Après avoir installé les dépendances, extrayez l\'archive téléchargée dans un dossier approprié, comme *C   *Tools\\LuxCoreRender*. Évitez d\'utiliser des dossiers système comme *C   *Program Files* ou *C   *Program Files (x86)*.

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Préférences de Raytracing ](Raytracing_Preferences/fr.md).

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, ce sera quelque chose comme *C   */Tools/LuxCoreRender/luxcoreui.exe* et appliquez.

### Version de développement 

LuxCoreRender est en développement actif, donc pour savoir quelle est la [dernière version de développement](https   *//github.com/LuxCoreRender/LuxCore/releases), vous devez vérifier manuellement sur GitHub la dernière version marquée comme Pre-release.

#### Linux 

***Binaires compilés***

Si votre distribution l\'a dans les dépôts officiels, vous pouvez installer la version de développement de LuxCoreRender et toutes les dépendances relatives via le gestionnaire de paquets. De telles distributions incluent    * [Arch Linux (AUR)](https   *//aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender).

Sinon, il est possible de télécharger les binaires officiels de la [dernière version de développement, marquée comme Pre-release, depuis GitHub](https   *//github.com/LuxCoreRender/LuxCore/releases). Le fichier sera quelque chose comme *luxcorerender-{numéro de version}-linux64.tar.bz2* ou *luxcorerender-latest-linux64.tar.bz2*. La solution la plus rapide (bien que ce ne soit pas la meilleure pratique) est d\'extraire le contenu de l\'archive dans un emplacement approprié, comme *\~/LuxCoreRender*. Si nécessaire, changez les permissions des fichiers pour que votre utilisateur puisse exécuter les fichiers que vous venez d\'extraire.

***Compilation à partir de la source***

Si votre distribution n\'a pas le développement de LuxCoreRender dans les dépôts et que les binaires officiels ne fonctionnent pas sur votre ordinateur, ou si vous le souhaitez, il est possible de compiler LuxCoreRender à partir des sources. [Vérifiez GitHub pour la dernière version de développement, marquée comme Pre-release](https   *//github.com/LuxCoreRender/LuxCore/releases) qui inclut la source, qui sera quelque chose comme \'luxcorerender-{numéro de version}.tar.bz2\'\'.

***Configuration de FreeCAD***

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Préférences de Raytracing](Raytracing_Preferences/fr.md).

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, habituellement c\'est */usr/bin/luxcoreui* (ou si vous l\'avez installé manuellement quelque chose comme *\~/LuxCoreRender/luxcoreui*) et appliquez.

#### macOS 

[Vérifiez sur GitHub la dernière version de développement](https   *//github.com/LuxCoreRender/LuxCore/releases), marquée comme Pre-release, descendez jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier Windows. Ce sera quelque chose comme *luxcorerender-{numéro de version}-mac64.dmg* ou *luxcorerender-latest-mac64.dmg*.

#### Windows 

[Vérifiez sur GitHub la dernière version de développement](https   *//github.com/LuxCoreRender/LuxCore/releases), marquée comme Pre-release, descendez jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier Windows. Ce sera quelque chose comme *luxcorerender-{numéro de version}-win64.zip* ou *luxcorerender-latest-win64.zip*.

Vérifiez ensuite dans la note au-dessus des actifs s\'il y a des notes sur les dépendances pour l\'utilisateur Windows. Par exemple, pour [utiliser LuxRender 2.5rc1](https   *//github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5rc1), vous devez installer le [Microsoft Visual C++ Redistributable for Visual Studio 2017](https   *//aka.ms/vs/15/release/vc_redist.x64.exe) et le [Intel C++ redistributable](https   *//software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).

Après avoir installé les dépendances, extrayez l\'archive téléchargée dans un dossier approprié, comme *C   *Tools\\LuxCoreRender*. Évitez d\'utiliser des dossiers système comme *C   *Program Files* ou *C   *Program Files (x86)*.

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Raytracing Préférences](Raytracing_Preferences/fr.md).

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, ce sera quelque chose comme *C   */Tools/LuxCoreRender/luxcoreui.exe* et appliquez.

## Atelier Render 

Pour le moment, il n\'y a pas de différences significatives entre l\'atelier Raytracing et l\'atelier Render dans la partie concernant l\'installation du logiciel externe, donc référez-vous à la [section atelier Raytracing](LuxCoreRender/fr#Atelier_Raytracing.md) pour installer LuxCoreRender et à cette section pour la configuration de l\'atelier Render.

Tout d\'abord, installez l\'atelier Render via le [Gestionnaire des extensions](Std_AddonMgr/fr.md) et redémarrez FreeCAD.

#### Linux 

Après avoir installé le Render Workbench et LuxCoreRender, lancez FreeCAD, ouvrez le [Réglage des préférences](Preferences_Editor/fr.md), [chargez l\'atelier Render](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les préférences de Render.

Définissez le chemin de l\'interface LuxCore pour qu\'il pointe vers votre installation de LuxCoreRender, habituellement c\'est */usr/bin/luxcoreui* (ou si vous l\'avez installé manuellement quelque chose comme *\~/LuxCoreRender/luxcoreui*) et appliquez.

#### Windows 

Après avoir installé le Render Workbench et LuxCoreRender, lancez FreeCAD, ouvrez le [Réglage des préférences](Preferences_Editor/fr.md), [chargez l\'atelier Render](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les préférences de Render.

Définissez le chemin de la commande LuxCore (cli), quelque chose comme *C   */Tools/LuxCore/pyluxcoretool.exe* et le chemin de l\'interface LuxCore, quelque chose comme *C   */Tools/LuxCore/luxcoreui.exe*, puis appliquez.



---
![](images/Right_arrow.png) [documentation index](../README.md) > LuxCoreRender/fr
