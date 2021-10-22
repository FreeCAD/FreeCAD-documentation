# Macro FCGear/fr
**Cette macro a été convertie en atelier appelé [atelier FCGear](FCGear_Workbench/fr.md). Veuillez utiliser l'atelier au lieu de cette macro car il est maintenu.**


{{Macro/fr
|Name= Macro FCGear
|Icon=FCGear_workbench_icon.svg
|Description=Atelier additionnel pour créer des engrenages de différents types.
|Author=looooo
|Version=1.0
|Date=2015-10-27
}}

## Description

Atelier additionnel pour créer des engrenages de différents types. Les types suivants sont créés, engrenages développants, crémaillère a taille droite, engrenages cycloïde, engrenages coniques.

![FCGear](images/FCGear_00.png ) 
*FCGear*

## Installation

-   git clone <https://github.com/looooo/freecad.gears.git>
-   créez un lien ou copiez le dossier freecad.gears dans /.FreeCAD/Mod (sudo ln -s (path\_to\_FCGear)/gear (path\_to\_freecad)/Mod)

Note:

-   dézippez le fichier FCGear.zip, et
-   copiez le répertoire **gear** complet dans /FreeCAD/Mod
    -   Avec Windows vous devez rendre les fichiers visibles
    -   Sous Linux en général chemin est usr/lib/FreeCAD/Mod.

Vous devez ouvrir .Mod en mode administrateur et vous devez donner les droits d'accès à tous les fichiers de "gear"

-   Pour que FCGear fonctionne, il faut que \"numpy\" soit installé, numpy est installé d\'office depuis la version 0.15.4671 de FreeCAD, FCGear ne fonctionnera pas sur les anciennes versions de FreeCAD

## Création d\'un engrenage 

-   sélectionnez l\'atelier gear
-   cliquez sur le symbole gear
-   adaptez les parametres à vos besoins

<img alt="Involutegear" src=images/Involutegear.png  style="width:100px;"><img alt="FCGear\_involutegear\_par" src=images/FCGear_involutegear_par.png  style="width:300px;"> <img alt="Involuterack" src=images/Involuterack.png  style="width:100px;"><img alt="FCGear\_involuterack\_par" src=images/FCGear_involuterack_par.png  style="width:300px;">

<img alt="Cycloidegear" src=images/Cycloidegear.png  style="width:100px;"><img alt="FCGear\_cycloide\_par" src=images/FCGear_cycloide_par.png  style="width:300px;"> <img alt="Bevelgear" src=images/Bevelgear.png  style="width:100px;"><img alt="FCGear\_bevel\_par" src=images/FCGear_bevel_par.png  style="width:300px;">

## Liens

-   [FCGear](https://github.com/looooo/FCGear)
-   [Forum topic](http://forum.freecadweb.org/viewtopic.php?f=3&t=12878&start=20)

---
[documentation index](../README.md) > Macro FCGear/fr
