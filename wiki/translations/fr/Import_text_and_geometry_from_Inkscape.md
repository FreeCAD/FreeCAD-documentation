 {{TutorialInfo/fr
|Topic= Importer texte et géométrie depuis Inkscape
|Level= Débutant
|Time= 30 minutes
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Introduction

Ce tutoriel est censé montrer comment importer du texte ou de la géométrie créé avec inkscape via svg-format dans FreeCAD.
Inkscape 0.91 et FreeCAD 0.16.6704 sur Windows sont utilisés pour ces opérations.

## Conseils généraux pour l\'importation à partir de inkscape {#conseils_généraux_pour_limportation_à_partir_de_inkscape}

-   l\'import svg dans FreeCAD ne peut pas gérer un fichier svg avec une résolution de plus de 45 dpi, alors vérifiez les paramètres dans inkscape
-   lors de l\'importation d\'objets chemin qui n\'apparaissent pas très lisses dans la vue 3D dans FreeCAD , cela peut être dû aux paramètres de FreeCAD pour la vue de la forme.
    -   dans FreeCAD, choisissez {{KEY | Édition}} → {{KEY | Préférences}} → {{KEY | Conception de pièce}} → {{KEY | Vue de la Forme}}
    -   en ce qui concerne \"Tesselation\" (mosaïque), la \"Déviation maximale pour la zone de délimitation du modèle\", la valeur par défaut est \"0,5%\"
    -   le réglage de cette valeur à une valeur inférieure augmentera la douceur du modèle dans la vue 3D (et utilisera plus de performances du PC)
    -   n\'utilisez pas de valeurs inférieures à \"0,01%\", cela entraînera probablement un crash de FreeCAD
    -   dans ce cas, la suppression des fichiers \"system.cfg\" et \"user.cfg\" dans votre répertoire FreeCAD-user résoudra ce problème

## Importation de texte à partir de inkscape {#importation_de_texte_à_partir_de_inkscape}

-   Dans inkscape, après avoir inséré du texte (et peut-être en appliquant des effets comme plier ou autre chose), assurez-vous de
    -   sélectionnez votre texte et choisissez {{KEY | Chemin}} → {{KEY | Objet en chemin}}
    -   dégroupez vos objets
    -   Enregistrer sous \"Format de fichier SVG simple (\* .svg)\"
-   ouvrez le fichier dans FreeCAD, en choisissant l\'option \"SVG en tant que géométrie (importSVG)\"
-   un objet chemin pour chaque lettre/numéro/signe sera créé dans l\'arborescence
-   utilisez l\'outil [Draft](Draft_Workbench/fr.md) [ Mettre à niveau](Draft_Upgrade/fr.md) sur chaque objet chemin pour créer des faces
-   Utilisez les outils pad ou [Part](Part_Workbench/fr.md) [extrusion](Part_Extrude/fr.md) sur les faces pour obtenir des solides
-   vous pouvez fusionner vos objets ou utiliser des composés sur eux en fonction de vos travaux prévus

## Importation de géométrie à partir de inkscape {#importation_de_géométrie_à_partir_de_inkscape}

Puisque inkscape et FreeCAD semblent avoir des approches différentes sur la façon d\'appliquer des dimensions sur l\'objet svg, le flux de travail recommandé semble être :

-   dégrouper tous les objets dans inkscape
-   sélectionnez tous les objets dans inkscape
-   appliquer un style de contour avec une largeur de 0 mm (oui, bien zéro millimètre) à tous les objets
-   Enregistrez au format de fichier \"Inkscape SVG (\*.svg)\" ou \"SVG simple (\*.svg)\"
-   ouvrez le fichier dans FreeCAD, en choisissant l\'option \"SVG en tant que géométrie (importSVG)\"
-   les dimensions des objets dans inkscape et dans FreeCAD devraient maintenant être identiques

## Crédits

Merci aux utilisateurs \"freecad-heini-1\" et \"herbk\" pour avoir testé et fourni des commentaires précieux.




