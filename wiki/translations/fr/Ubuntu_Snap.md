# Ubuntu Snap/fr


## Introduction

Un package [Ubuntu Snap](Ubuntu_Snap/.md), ou simplement [Snap](Ubuntu_Snap/fr.md) est un format de distribution similaire à [AppImage](AppImage/fr.md) en ce qu\'il est destiné à être un \"package installable universel\" pour déployer le logiciel pour les systèmes Linux. Les snaps ont été introduits par Ubuntu mais ils sont destinés à fonctionner dans toutes les distributions Linux tant que le démon Snap, ou `snapd`, est disponible dans le système cible.

Un package Snap a deux caractéristiques principales:

-   Les programmes sont mis en bac à sable afin de ne pas interférer avec le reste de votre système d\'exploitation.
-   Les programmes sont mis à jour automatiquement en arrière-plan afin d\'obtenir la dernière version de l\'application.

Pour d\'autres façons d\'installer le logiciel, voir [Installation sous Linux](Installing_on_Linux/fr.md).

## Installation

Depuis la v0.19, l\'utilisation de Snaps est expérimentale. Les Snaps actuels sont générés et hébergés par des bénévoles.

Dans tous les systèmes où Snaps doit être installé, le démon Snap doit être installé en premier. Le package est normalement appelé `snapd`.

Pour Debian/Ubuntu et les systèmes similaires qui utilisent le gestionnaire APT, le démon est installé comme suit: {{Code|lang=bash|code=
sudo apt install snapd
}}

Pour installer la version stable de Snap, utilisez: {{Code|lang=bash|code=
sudo snap install freecad
}}

Pour installer la version de développement de Snap, utilisez: {{Code|lang=bash|code=
sudo snap install --edge freecad-ppd
}}

## Liens

Plus d\'informations sur les efforts en cours pour gérer Snaps.

-   [0.19 Snap Preview a besoin de \"testeurs\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), ancien Snap de **vejmarie**
-   [Discussion: Discussion: état du composant logiciel Snap (Snap Packaging)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), version plus récente du Snap par **ppd**



