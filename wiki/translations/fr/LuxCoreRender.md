


<div class="mw-translate-fuzzy">


{{VeryImportantMessage|LuxCoreRender n'est pas officiellement pris en charge par l'[atelier Raytracing](Raytracing_Workbench.md) mais par le nouvel [https://github.com/FreeCAD/FreeCAD-render atelier Render], qui est destiné à le remplacer. Il ne doit pas être confondu avec le [Projet Render](Render_project/fr.md), arrêté et dépassé. L'atelier Render peut être installé via le [Gestionnaire d'Addon](Std_AddonMgr/fr.md).}}


</div>


<div class="mw-translate-fuzzy">

# Description

[LuxCoreRender](https://luxcorerender.org) est un moteur de rendu basé sur la physique, qui redémarre le [LuxRender](LuxRender/fr.md) désormais obsolète. Il n\'est pas officiellement supporté par l\'[atelier Raytracing](Raytracing_Workbench/fr.md), bien qu\'il puisse fonctionner.


</div>

[LuxCoreRender](https://luxcorerender.org) is a physically based rendering engine, reboot of the now outdated [LuxRender](LuxRender.md). It is not officially supported by the [Raytracing Workbench](Raytracing_Workbench.md), although it might work.


<div class="mw-translate-fuzzy">

# Installation

## Atelier Raytracing {#atelier_raytracing}


{{VeryImportantMessage|Officiellement, l'[atelier Raytracing](Raytracing_Workbench/fr.md) ne fonctionne pas avec LuxCoreRender, mais uniquement avec l'ancien [atelier Raytracing](LuxRender]]. De plus, l'[[Raytracing_Workbench/fr.md) est remplacé par le nouvel [projet Render](https://github.com/FreeCAD/FreeCAD-render atelier Render]], qui est destiné à le remplacer. Il ne doit pas être confondu avec le [[Render_project/fr.md), arrêté et dépassé. Le atelier Render Workbench peut être installé via le [Gestionnaire d'Addon](Std_AddonMgr/fr.md). L'information ici est fournie parce que par défaut FreeCAD est toujours livré (à partir de 0.19-24276) avec l'atelier Raytracing}}

.


</div>

## Raytracing Workbench {#raytracing_workbench}


{{VeryImportantMessage|Officially the [Raytracing workbench](Raytracing_Workbench.md) does not work with LuxCoreRender, only with the outdated [LuxRender](LuxRender.md). Also the [Raytracing workbench](Raytracing_Workbench.md) is being superseded by the new [https://github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. This must not be confused with the halted and outdated [Render project](Render_project.md). The Render Workbench can be installed through the [Addon Manager](Std_AddonMgr.md). The information here is provided because by default FreeCAD is still shipped (as of 0.19-24276) with the Raytracing Workbench}}

### Stable Version {#stable_version}


<div class="mw-translate-fuzzy">

### Version stable {#version_stable}

LuxCoreRender est en cours de développement actif, donc pour savoir quelle est la [dernière version stable vérifiez sur GitHub](https://github.com/LuxCoreRender/LuxCore/releases/latest).


</div>

#### Linux


<div class="mw-translate-fuzzy">

#### Linux {#linux_1}

***Binaires compilés***


</div>

Si votre distribution l\'a dans les dépôts officiels, vous pouvez installer LuxCoreRender et toutes les dépendances relatives via le gestionnaire de paquets. De telles distributions incluent : [Arch Linux (AUR)](https://aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender), [Fedora](https://src.fedoraproject.org/rpms/luxcorerender).

Sinon, il est possible de télécharger les binaires officiels de la [dernière version stable de GitHub](https://github.com/LuxCoreRender/LuxCore/releases/latest). Le fichier sera quelque chose comme *luxcorerender-{numéro de version}-linux64.tar.bz2*. La solution la plus rapide (bien que ce ne soit pas la meilleure pratique) est d\'extraire le contenu de l\'archive dans un emplacement approprié, comme *\~/LuxCoreRender*. Si nécessaire, changez les permissions des fichiers pour que votre utilisateur puisse exécuter les fichiers que vous venez d\'extraire.

***Compilation à partir de la source***

Si votre distribution n\'a pas LuxCoreRender dans ses dépôts et que les binaires officiels ne fonctionnent pas sur votre ordinateur, ou si vous le souhaitez, il est possible de compiler LuxCoreRender à partir des sources. [La dernière version stable](https://github.com/LuxCoreRender/LuxCore/releases/latest) inclut la source, qui sera quelque chose comme \'luxcorerender-{numéro de version}.tar.bz2\'\'.

***Configuration de FreeCAD***


<div class="mw-translate-fuzzy">

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Raytracing Préférences](Raytracing_Preferences/fr.md).


</div>

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, habituellement c\'est */usr/bin/luxcoreui* (ou si vous l\'avez installé manuellement quelque chose comme *\~/LuxCoreRender/luxcoreui*) et appliquez.

#### macOS


<div class="mw-translate-fuzzy">

#### macOS {#macos_1}

[Vérifiez sur GitHub la dernière version stable](https://github.com/LuxCoreRender/LuxCore/releases/latest), faites défiler vers le bas jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier macOS. Ce sera quelque chose comme *luxcorerender-{numéro de version}-mac64.dmg*.


</div>

#### Windows


<div class="mw-translate-fuzzy">

#### Windows {#windows_1}

[Vérifiez sur GitHub pour la dernière version stable](https://github.com/LuxCoreRender/LuxCore/releases/latest), descendez jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier Windows. Ce sera quelque chose comme *luxcorerender-{numéro de version}-win64.zip*.


</div>

Vérifiez ensuite dans la note au-dessus des actifs s\'il y a des notes sur les dépendances pour l\'utilisateur Windows. Par exemple, pour [utiliser LuxRender 2.5](https://github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5), vous devez installer le [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://aka.ms/vs/15/release/vc_redist.x64.exe) et le [Intel C++ redistributable](https://software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).


<div class="mw-translate-fuzzy">

Après avoir installé les dépendances, extrayez l\'archive téléchargée dans un dossier approprié, comme *C:\\Tools\\LuxCoreRender*. Évitez d\'utiliser des dossiers système comme *C:\\Program Files* ou *C:\\Program Files (x86)*.


</div>


<div class="mw-translate-fuzzy">

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Raytracing Préférences](Raytracing_Preferences/fr.md).


</div>

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, ce sera quelque chose comme *C:/Tools/LuxCoreRender/luxcoreui.exe* et appliquez.

### Development Version {#development_version}


<div class="mw-translate-fuzzy">

### Version de développement {#version_de_développement}

LuxCoreRender est en développement actif, donc pour savoir quelle est la [dernière version de développement](https://github.com/LuxCoreRender/LuxCore/releases), vous devez vérifier manuellement sur GitHub la dernière version marquée comme Pre-release.


</div>

#### Linux {#linux_2}


<div class="mw-translate-fuzzy">

#### Linux {#linux_3}

***Binaires compilés***


</div>

Si votre distribution l\'a dans les dépôts officiels, vous pouvez installer la version de développement de LuxCoreRender et toutes les dépendances relatives via le gestionnaire de paquets. De telles distributions incluent : [Arch Linux (AUR)](https://aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender).

Sinon, il est possible de télécharger les binaires officiels de la [dernière version de développement, marquée comme Pre-release, depuis GitHub](https://github.com/LuxCoreRender/LuxCore/releases). Le fichier sera quelque chose comme *luxcorerender-{numéro de version}-linux64.tar.bz2* ou *luxcorerender-latest-linux64.tar.bz2*. La solution la plus rapide (bien que ce ne soit pas la meilleure pratique) est d\'extraire le contenu de l\'archive dans un emplacement approprié, comme *\~/LuxCoreRender*. Si nécessaire, changez les permissions des fichiers pour que votre utilisateur puisse exécuter les fichiers que vous venez d\'extraire.

***Compilation à partir de la source***

Si votre distribution n\'a pas le développement de LuxCoreRender dans les dépôts et que les binaires officiels ne fonctionnent pas sur votre ordinateur, ou si vous le souhaitez, il est possible de compiler LuxCoreRender à partir des sources. [Vérifiez GitHub pour la dernière version de développement, marquée comme Pre-release](https://github.com/LuxCoreRender/LuxCore/releases) qui inclut la source, qui sera quelque chose comme \'luxcorerender-{numéro de version}.tar.bz2\'\'.

***Configuration de FreeCAD***


<div class="mw-translate-fuzzy">

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Raytracing Préférences](Raytracing_Preferences/fr.md).


</div>

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, habituellement c\'est */usr/bin/luxcoreui* (ou si vous l\'avez installé manuellement quelque chose comme *\~/LuxCoreRender/luxcoreui*) et appliquez.

#### macOS {#macos_2}


<div class="mw-translate-fuzzy">

#### macOS {#macos_3}

[Vérifiez sur GitHub la dernière version de développement](https://github.com/LuxCoreRender/LuxCore/releases), marquée comme Pre-release, descendez jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier Windows. Ce sera quelque chose comme *luxcorerender-{numéro de version}-mac64.dmg* ou *luxcorerender-latest-mac64.dmg*.


</div>

#### Windows {#windows_2}


<div class="mw-translate-fuzzy">

#### Windows {#windows_3}

[Vérifiez sur GitHub la dernière version de développement](https://github.com/LuxCoreRender/LuxCore/releases), marquée comme Pre-release, descendez jusqu\'à la section *Assets* (développez-la si nécessaire) et téléchargez le fichier Windows. Ce sera quelque chose comme *luxcorerender-{numéro de version}-win64.zip* ou *luxcorerender-latest-win64.zip*.


</div>

Vérifiez ensuite dans la note au-dessus des actifs s\'il y a des notes sur les dépendances pour l\'utilisateur Windows. Par exemple, pour [utiliser LuxRender 2.5rc1](https://github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5rc1), vous devez installer le [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://aka.ms/vs/15/release/vc_redist.x64.exe) et le [Intel C++ redistributable](https://software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).


<div class="mw-translate-fuzzy">

Après avoir installé les dépendances, extrayez l\'archive téléchargée dans un dossier approprié, comme *C:\\Tools\\LuxCoreRender*. Évitez d\'utiliser des dossiers système comme *C:\\Program Files* ou *C:\\Program Files (x86)*.


</div>


<div class="mw-translate-fuzzy">

Après avoir installé LuxCoreRender, lancez FreeCAD, ouvrez [Réglage des préférences](Preferences_Editor/fr.md), [charger l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les [Raytracing Préférences](Raytracing_Preferences/fr.md).


</div>

Définissez le chemin de l\'exécutable Luxrender pour qu\'il pointe vers votre installation de LuxCoreRender, ce sera quelque chose comme *C:/Tools/LuxCoreRender/luxcoreui.exe* et appliquez.

## Render Workbench {#render_workbench}


<div class="mw-translate-fuzzy">

## Atelier Render {#atelier_render}

Pour le moment, il n\'y a pas de différences significatives entre l\'atelier Raytracing et l\'atelier Render dans la partie concernant l\'installation du logiciel externe, donc référez-vous à la [section atelier Raytracing](LuxCoreRender/fr#Atelier_Raytracing.md) pour installer LuxCoreRender et à cette section pour la configuration de l\'atelier Render.


</div>


<div class="mw-translate-fuzzy">

Tout d\'abord, installez Render Workbench via le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) et redémarrez FreeCAD.


</div>

#### Linux {#linux_4}


<div class="mw-translate-fuzzy">

#### Linux {#linux_5}

Après avoir installé le Render Workbench et LuxCoreRender, lancez FreeCAD, ouvrez le [Réglage des préférences](Preferences_Editor/fr.md), [chargez l\'atelier Render](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les préférences de Render.


</div>

Définissez le chemin de l\'interface LuxCore pour qu\'il pointe vers votre installation de LuxCoreRender, habituellement c\'est */usr/bin/luxcoreui* (ou si vous l\'avez installé manuellement quelque chose comme *\~/LuxCoreRender/luxcoreui*) et appliquez.

#### Windows {#windows_4}


<div class="mw-translate-fuzzy">

#### Windows {#windows_5}

Après avoir installé le Render Workbench et LuxCoreRender, lancez FreeCAD, ouvrez le [Réglage des préférences](Preferences_Editor/fr.md), [chargez l\'atelier Render](Preferences_Editor/fr#Ateliers_non_charg.C3.A9s.md) et allez dans les préférences de Render.


</div>

Définissez le chemin de la commande LuxCore (cli), quelque chose comme *C:/Tools/LuxCore/pyluxcoretool.exe* et le chemin de l\'interface LuxCore, quelque chose comme *C:/Tools/LuxCore/luxcoreui.exe*, puis appliquez.
