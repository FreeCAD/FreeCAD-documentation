# Raytracing project/fr
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


<div class="mw-translate-fuzzy">


**(2020) Cette page fait référence à une tentative de mise à jour de l'[Atelier Raytracing](Raytracing_Workbench/fr.md), proposé vers 2012. Son auteur d'origine n'ayant jamais terminé la mise en œuvre, ces informations sont obsolètes et ne doivent pas être considérées comme actuelles.
</div>

<div class="mw-translate-fuzzy">
Un nouveau développement est en cours dans l'[https://github.com/FreeCAD/FreeCAD-render Atelier Render], un remplacement complet en Python pour l'[Atelier Raytracing](Raytracing_Workbench/fr.md).
**


</div>


{{TOCright}}

Ce projet est le développement de **FreeCAD Raytracing**. Il suit les règles de la [Getting things done](https://en.wikipedia.org/wiki/Getting_Things_Done) processus. Les projets sont collectées dans le feuille [de route de développement](Development_roadmap/fr.md).


<div class="mw-translate-fuzzy">

## Buts et principes 

Ce projet vise à mettre à jour le [module de rendu](Raytracing_Workbench/fr.md) en cours, qui est actuellement utilisé par [povray](http://www.povray.org/), un moteur de rendu partiel qui donne des résultats satisfaisants, et, permettre l\'utilisation d\'un moteur de rendu plus moderne tel que [Lux Render](http://www.luxrender.net/en_GB/index), [Yafaray](http://www.yafaray.org/), [Indigo](http://www.indigorenderer.com/).


</div>

Également fournir une interface générique, pour permettre des rendus de fonds (profondeur de champ) multiples, pour être utilisé, pour la visualisation des caractéristiques au sein de FreeCAD. Fournir une interface de programmation plus générique, pour permettre une création de plugins de rendu plus facile.

L\'interface permettra à la fois l\'exécution de rendus extérieurs, **open source** et **propriétaires**, qui seront utilisés, par la génération d\'un fichier de scène compatible, et, le lancement d\'un processus distinct en arrière-plan. La sortie peut alors être visualisée directement à l\'intérieur FreeCAD, en ouvrant le fichier de sortie temporaire (si disponible).

Chaque moteur de rendu, sera un plugin dans une interface générique, et, fournira des matériaux compatibles, des modes de rendu.

## Résultat

Affichages visuels réalistes !!! Produire des résultats de haute qualité, des objets affichés dans le document de FreeCAD, et, fournir une interface très simple, avec des préréglages pour permettre une initialisation rapide pour le rendu et les prévisualisations.

L\'interface utilisateur devrait permettre la création de situations plus complexes, et, peut-être donner un aperçu des changements, ou des modifications, tels que l\'éclairage, la position. Toutefois, l\'objectif n\'est pas de fournir une suite de rendu très complet.

## Réflexions

Une bibliothèque de documents **\"doit\"** être créée pour chaque plug-in de rendu, avec ses préréglages. Les propriétés des matériaux peuvent être modifiées. Les préréglages de scène devraient permettre aux utilisateurs inexpérimentés au Rendu, de produire des visuels de haute qualité en peu de temps.

## Organisation

L\'intégration de rendu [Lux render](http://www.luxrender.net/en_GB/index) dans l\'inteface générique, est en cours de création et test, un moteur de rendu non [biaisé](http://www.larousse.fr/dictionnaires/francais/biaisé_biaisé/9022) sera d\'abord mis en œuvre. Les travaux en cours sont complétés par [Github Render Branch](https://github.com/mrlukeparry/freecad/tree/render).

**Actuellement, il est possible de faire des rendu d\'objets avec Lux Render :**

![](images/LuxRenderOutput.png )

Ici en vedette, une pièce qui a été créée à l\'aide **PartDesign/Sketcher**, rendu à l\'aide du nouveau **render workbench**, en cours d\'élaboration dans **Lux Render**. Lux Render permet des effets sympas, comme la création de la profondeur de champ [DOF (Depth of Field)](http://wiki.blender.org/index.php/Doc:FR/2.4/Manual/Render/Camera/Depth_Of_Field), pour améliorer le réalisme.

## Actions suivantes 

-   Créer l\'abstraction pour assurer l\'interface entre les moteurs de rendu (Terminé)

-   Mettre en place une interface pour la description des documents génériques et la collecte de ces documents (Terminé)

-   Mettre en place une interface décrivant les presets de rendu (Terminé)

-   Mettre en place une interface décrivant les modèles (Terminé)

-   Mettre en place une fonctionnalité permettant de stocker toutes ces informations de façon permanente

-   Mettre en œuvre l\'enregistrement des propriétés des matériaux

-   Créer un environnement de postes de travail pour la sortie de l\'affichage (Terminé)

-   Créer des boîtes à outils pour modifier les propriétés de rendu (Terminé)

-   Créer des boîtes à outils pour naviguer, modifier et appliquer des matériaux aux caractéristiques des pièces (Terminé)

-   Création de scripts automake (WIP)

-   Supprimer les dépendances GUI de Raytracing/App

¬ Structure de données d\'e boîtes englobantes

¬ ne devrait pas utiliser coin3d SbBox3f

¬ QWidget inclus dans QProcess pour une raison quelconque ?

-   Supprimer les dépendances GUI de Raytracing/App

¬Structure de données boîte englobante

¬ ne devrait pas utiliser coin3d SbBox3f

¬ QWidget inclus dans QProcess pour une raison quelconque ?

-   Test de compatibilité avec Windows (en cours)

¬ Mise à jour de Libpack pour inclure QT 4.7 - QT 4.8

¬ supprimer les Erreurs et avertissements du compilateur

-   Mise en œuvre permettant d\'économiser des propriétés matérielles

-   Nettoyage de l\'interface QML

-   Création de Templates de rendu, rendu matériel, rendu Presets

-   Créer une scène blender à convertisseur de template lux

-   Convertir en matériels LuxBlender .lbm ([LuxBlender](http://www.luxrender.net/lrmdb/en/material/)) matériaux utiles

-   Créer Python bindings pour le rendu de matériaux, caméras, lumières

-   Créer un document objet de RenderCamera

-   Permettre l\'importer de modèle de rendu de la scène dans la fonctionnalité.

-   Répertoires de préréglage/matériel/template défini par l\'utilisateur

-   Améliorer le View Provider

-   Convertir Povray/Yafaray pour utiliser la nouvelle Infrastructure du Module de rendu

-   Tests



[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing project/fr
