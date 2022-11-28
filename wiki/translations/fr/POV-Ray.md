# POV-Ray/fr
**Le développement de POV-Ray semble être arrêté. La dernière version stable est 3.7.0.8 (2018-05-27), la dernière version de développement est 3.8.0-x (2019-02-19), le [https   *//github.com/POV-Ray/povray/ official project on GitHub] a été édité la dernière fois le 2019-03-08. Veuillez supprimer cet avertissement si la situation change**

# Description

POV-Ray (The Persistence of Vision Raytracer) est l\'un des deux moteurs de rendu pris en charge par l\'[atelier Raytracing](Raytracing_Workbench.md) avec [LuxRender](LuxRender/fr.md). Il est également pris en charge par le nouvel [atelier Render](https   *//github.com/FreeCAD/FreeCAD-render), ainsi que par [LuxCoreRender](LuxCoreRender.md), Appleseed, Blender Cycles et Intel Ospray Studio (expérimental).

# Installation

## Atelier Raytracing 


**L'[atelier Raytracing](Raytracing_Module/fr.md) a été remplacé par le nouvel [https   *//github.com/FreeCAD/FreeCAD-render atelier Render], qui est destiné à le remplacer. L'atelier Render peut être installé via le [Gestionnaire des extensions](Std_AddonMgr/fr.md). L'information ici est fournie parce que par défaut FreeCAD est toujours livré (à partir de 0.19-24276) avec l'atelier Raytracing**

.

### Version stable 

La dernière version stable de POV-Ray fournie avec des binaires est la 3.7.0.0 (2013-11-06), la première à être un logiciel libre, publié sous la licence AGPL3 (ou ultérieure). La dernière version stable de POV-Ray, publiée uniquement sous forme de code source, est la 3.7.0.8 (2018-05-27).

#### Linux

***Binaires compilés***

Si votre distribution le possède dans les dépôts officiels, vous pouvez installer POV-Ray et toutes les dépendances relatives via le gestionnaire de paquets. De telles distributions incluent    * [Arch Linux](https   *//archlinux.org/packages/community/x86_64/povray/), [Debian](https   *//packages.debian.org/search?keywords=povray), [Gentoo](https   *//packages.gentoo.org/packages/media-gfx/povray), [openSUSE](https   *//software.opensuse.org/package/povray), [Ubuntu](https   *//packages.ubuntu.com/search?keywords=povray).

***Compilation à partir de la source***

Si votre distribution n\'a pas POV-Ray dans les dépôts, ou si vous le souhaitez, il est possible de compiler POV-Ray à partir des sources. [Télécharger le code source de POV-Ray 3.7.0.8 depuis GitHub](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.7.0.8.tar.gz).

***Configuration de FreeCAD***

Après avoir installé POV-Ray, lancez FreeCAD, ouvrez le [Réglage des préférences](Preferences_Editor/fr.md), [chargez l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_disponibles.md) et allez dans les [Préférences de Raytracing](Raytracing_Preferences/fr.md).

Définissez le chemin de l\'exécutable de POV-Ray pour qu\'il pointe vers votre installation de POV-Ray, généralement c\'est */usr/bin/povray*, et appliquez.

#### macOS

Il n\'existe pas de binaire officiel de POV-Ray 3.7 ou plus récent pour macOS, si vous souhaitez le compiler à partir des sources, vous devrez probablement vous débrouiller seul.

Les [binaires disponibles les plus récents](http   *//www.povray.org/redirect/www.povray.org/ftp/pub/povray/Old-Versions/Official-3.62/Macintosh/povpmac.zip) sont de l\'ancienne source fermée POV-Ray 3.6x.

#### Windows

La dernière version stable de POV-Ray ayant compilé des binaires Windows est POV-Ray 3.7.0.0. [Téléchargez-la depuis GitHub](https   *//github.com/POV-Ray/povray/releases/download/v3.7.0.0/povwin-3.7-agpl3-setup.exe), lancez le programme d\'installation et suivez les étapes proposées.

Par défaut, le dossier de destination est *C   *Program Files\\POV-Ray\\v3.7*, avec les documents et les scènes dans *C   *Users\\{votre utilisateur}\\Documents\\POV-Ray\\v3.7*.

Après avoir installé POV-Ray, lancez FreeCAD, ouvrez le [Réglage des préférences](Preferences_Editor/fr.md), [chargez l\'atelier Raytracing](Preferences_Editor/fr#Ateliers_disponibles.md) et allez dans les [Préférences de Raytracing](Raytracing_Preferences/fr.md).

Définissez le chemin de l\'exécutable de POV-Ray pour qu\'il pointe vers votre installation de POV-Ray, généralement c\'est *C   */Program Files/POV-Ray/v3.7/bin/pvengine64.exe*, et appliquez.

Ensuite, avant d\'essayer d\'effectuer un rendu, démarrez POV-Ray séparément et [définissez les restrictions d\'E/S (I/O) conformément à la documentation de POV-Ray](https   *//wiki.povray.org/content/Documentation   *Windows_Section_2.1), sinon le rendu ne fonctionnera pas correctement (ou ne fonctionnera pas du tout).

### Version en cours de développement 

Le développement semble avoir été interrompu, mais les dernières versions expérimentales et le code source sont disponibles. Comme il s\'agit d\'une version expérimentale, il est déconseillé de l\'utiliser dans des environnements de production.

#### Linux 

Il n\'y a pas de binaires de développement officiels pour POV-Ray, vous devez le compiler à partir des sources. La dernière version de la branche de développement officielle est [POV-Ray v3.8.0-alpha.10064268](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-alpha.10064268.tar.gz).

Les dernières versions de développement (qui ne font pas partie de la branche de développement officielle) sont [POV-Ray v3.8.0-x.freetype.3](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.freetype.3.tar.gz) et [POV-Ray v3.8.0-x.10064738](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.10064738.tar.gz).

#### macOS 

Il n\'y a pas eu de version macOS de POV-Ray depuis la version 3.6x à code source fermé. Vous pouvez essayer de le compiler à partir des sources, mais sachez que ce n\'est peut-être même pas possible.

La dernière version de la branche de développement officielle est [POV-Ray v3.8.0-alpha.10064268](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-alpha.10064268.zip).

Les dernières versions de développement (qui ne font pas partie de la branche de développement officielle) sont [POV-Ray v3.8.0-x.freetype.3](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.freetype.3.zip) et [POV-Ray v3.8.0-x.10064738](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.10064738.zip).

#### Windows 

Tout d\'abord, vous devez installer POV-Ray 3.7, voir [les instructions d\'installation de la version stable](POV-Ray/fr#Windows.md). Ensuite, ouvrez le répertoire d\'installation de POV-Ray, par défaut *C   *Program Files\\POV-Ray\\v3.7*, et dans le sous-répertoire *bin* renommez l\'exécutable de POV-Ray, afin de ne pas le remplacer. Par exemple, renommez-le en BAK-pvengine64.exe.

Téléchargez ensuite la version de développement de POV-Ray que vous souhaitez utiliser. La dernière version de la branche de développement officielle est [POV-Ray v3.8.0-alpha.10064268-av69](https   *//github.com/POV-Ray/povray/releases/download/v3.8.0-alpha.10064268/povray-3.8.0-alpha.10064268-av691-Win64.7z).

Les dernières versions de développement (qui ne font pas partie de la branche de développement officielle) sont [POV-Ray v3.8.0-x.freetype.3-av693](https   *//github.com/POV-Ray/povray/releases/download/v3.8.0-x.freetype.3/povray-3.8.0-x.freetype.3-av693-Win64.7z) et [POV-Ray v3.8.0-x.10064738-av694](https   *//github.com/POV-Ray/povray/releases/download/v3.8.0-x.10064738/povray-3.8.0-x.10064738-av694-Win64.7z).

Extrayez l\'archive téléchargée (si vous ne disposez pas d\'un logiciel adapté, utilisez [7-Zip](https   *//www.7-zip.org/)) et copiez l\'exécutable POV-Ray dans le dossier *bin* de votre installation POV-Ray 3.7.

## Atelier Render 

Pour l\'instant, il n\'y a pas de différences significatives entre le Raytracing Workbench et le Render Workbench dans la partie concernant l\'installation du logiciel externe, donc reportez-vous à la [section atelier Raytracing](POV-Ray/fr#Atelier_Raytracing.md) pour installer POV-Ray et à cette section pour la configuration de l\'atelier Render.

Tout d\'abord, installez l\'atelier Render via le [Gestionnaire des extensions](Std_AddonMgr/fr.md) et redémarrez FreeCAD.

#### Linux 

Après avoir installé l\'atelier Render et POV-Ray, lancez FreeCAD, ouvrez le [Preferences Editor](Preferences_Editor.md), [chargez l\'atelier Render](Preferences_Editor/fr#Ateliers_disponibles.md) et allez dans les préférences de Render.

Définissez le chemin de l\'exécutable de POV-Ray pour qu\'il pointe vers votre installation de POV-Ray, généralement c\'est */usr/bin/povray*, et appliquez.

#### Windows 

Après avoir installé l\'atelier Render et POV-Ray, lancez FreeCAD, ouvrez le [Preferences Editor](Preferences_Editor.md), [chargez l\'atelier Render](Preferences_Editor/fr#Ateliers_disponibles.md) et allez dans les préférences de Render.

Définissez le chemin de l\'exécutable de POV-Ray pour qu\'il pointe vers votre installation de POV-Ray, généralement c\'est *C   */Program Files/POV-Ray/v3.7/bin/pvengine64.exe*, et appliquez.

Ensuite, avant d\'essayer d\'effectuer un rendu, démarrez POV-Ray séparément et [définissez les restrictions d\'E/S (I/O) conformément à la documentation de POV-Ray](https   *//wiki.povray.org/content/Documentation   *Windows_Section_2.1), sinon le rendu ne fonctionnera pas correctement (ou ne fonctionnera pas du tout).



---
![](images/Right_arrow.png) [documentation index](../README.md) > POV-Ray/fr
