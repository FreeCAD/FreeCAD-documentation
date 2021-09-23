# Advanced TechDraw Tutorial/fr






{{TutorialInfo
|Topic=Modélisation
|Level=Utilisateur expérimenté
|Author=NormandC
|FCVersion=≥ 0.19.23300
}}

## L\'objectif en bref 

Créez des points, des lignes, des cercles, des arcs, etc\... dans des vues TechDraw et/ou des dessins \"cosmétiques\" entiers avec une précision absolue, adaptée aux outils de cotation dont l\'établi est équipé, pour générer des dessins techniques conformes et détaillés.

## Introduction

Ce tutoriel présente à l\'utilisateur expérimenté une utilisation avancée d\'outils et de techniques existants dans d\'autres ateliers pour étendre les fonctionnalités manquantes dans l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;">. [atelier TechDraw](TechDraw_Workbench/fr.md). Ce tutoriel n\'est pas un guide complet et exhaustif de l\'atelier TechDraw et de nombreux outils et fonctionnalités ne sont pas couverts. Il devrait contribuer à surmonter les difficultés rencontrées pour citer et enrichir le dessin technique à l\'aide de TechDraw. Ce tutoriel conduira les utilisateurs avancés à travers les étapes nécessaires pour produire des dessins techniques exigeants de la pièce à partir du [Tutoriel d\'introduction PartDesign](Basic_Part_Design_Tutorial/fr.md) en utilisant les outils de dessin de l\'atelier TechDraw.

1.  L\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) (lignes, polylignes, circonférences, arcs, splines, béziers, etc.), en particulier les accrochages, pour créer sur l\'objet des \"points cosmétiques\" réellement précis qui pourront ensuite être utilisés pour le dimensionnement dans TechDraw.
2.  Il est également possible d\'utiliser l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md) comme
    -   générateur de \"base-sketchTD\" (bases de croquis pour TechDraw) en 2D (par exemple, schéma de système, plans d\'étage, élévations, vues de pièces mécaniques ou d\'ensemble etc\...) ou en
    -   utilisant directement les croquis qui ont généré les modèles 3D, ou en
    -   convertissant en esquisse le \"facebinder\" généré avec l\'ébauche obtenue à partir des faces et/ou des sections des modèles 3D.
3.  Pour obtenir des sections particulières (coupes sur différents plans ou axes) à présenter sur la page dans TechDraw (il est conseillé d\'utiliser une copie de l\'objet 3D original), ensuite par la création de plans (même sur différents axes) en utilisant l\'<img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [atelier Workfeature](Workfeature_Workbench/fr.md), il est possible de sectionner la copie de l\'objet 3D avec <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part Séparer/exploser](Part_SliceApart/fr.md) pour obtenir les faces à convertir en esquisse avec <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> [Draft Draft vers Esquisse](Draft_Draft2Sketch/fr.md) puis avec l\'atelier *\'Sketcher*, les éditer pour les adapter au dessin technique que l\'on souhaite générer dans TechDraw. L\'[atelier Workfeature](Workfeature_Workbench/fr.md) (et la [Macro WorkFeatures](Macro_WorkFeatures/fr.md)) sont pleins de fonctions supplémentaires pratiques qui nous permettent de créer facilement des plans (théoriquement infinis en extension et en quantité) en sélectionnant trois points (sommets) *(rappelez-vous que pour trois points passant, un et un seul plan passe par trois points non alignés un et un seul plan passe par trois points non alignés*) est un axiome géométrique, qui confirme sans aucune ambiguïté (!) la validité et l\'importance de l\'outil WorkFeatureDev pour créer des plans précis très facilement.

(\**Ceci est tout à fait comparable à la commande Slice d\'AutoCAD [1](https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Core/files/GUID-27593C5E-4B89-41F2-872B-927D69517CBF-htm.html) qui est basée sur cet axiome. Sans pré-construction d\'un nouveau plan, un plan de coupe utilisant trois points est défini.*)

*Remarque : ces plans peuvent être réunis par chevauchement/coïncidence de deux bords en utilisant la fonction booléenne de <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Part Union](Part_Fuse/fr.md).* Les plans ainsi formés et convenablement positionnés (selon nos dispositions) seront utilisés comme **lames de coupe** <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part Séparer/exploser](Part_SliceApart/fr.md), découpant notre objet 3D en plusieurs parties selon la confirmation du plan choisi.\'\'

## Avant de commencer 

Les ateliers qui sont utilisés pour générer les dessins des exemples ci-joints sont :
\* <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)

-   <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md)
-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md)
-   <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [atelier Workfeature](Workfeature_Workbench/fr.md)
-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md)

## La tâche 

Les étapes de la démarche :

1.  Création de l\'objet ou des objets 3D selon les canons de la modélisation traditionnelle ;
2.  Création possible de copies indépendantes ou simples, à utiliser par exemple pour la création de sections continues spécifiques positionnées sur plusieurs plans ou axes, et qui ensuite, grâce à l\'utilisation des fonctions \"facebinder\", \"Draft to Sketch\", Shape 2D View, etc. nous permettront de produire des \"esquisses\" parfaitss, puis de les éditer pour les rendre (en créant ad hoc des \"points ou des lignes cosmétiques\") utilisables dans TechDraw ; à ces sketches j\'ai donné le nom de \"base-sketchTD\" ;
3.  insertion / création de \"base-sketchTD\" dans les couches d\'appartenance (aussi avec \"drag and drop\") ;
4.  création de la page de dessin avec son modèle ;
5.  création de la vue avec TechDraw : sélectionnez la couche ou le dossier de regroupement (qui contient la \"base-sketchTD\") dans la structure, puis cliquez sur le bouton \"insérer vue\" ; TechDraw insérera le contenu de la couche ou du dossier de regroupement dans la vue. Pour une création correcte, la \"base-sketchTD\" doit être perpendiculaire à la vue du moniteur/de l\'écran ; je précise que tout ce que nous ajouterons ultérieurement dans le calque ou dans le dossier de regroupement, ou toute modification de la \"base-sketchTD\", sera mis à jour en temps réel dans la vue TechDraw. Gardez à l\'esprit que les mises à jour et / ou les modifications peuvent affecter les dimensions déjà introduites ou les lignes cosmétiques créées avec l\'outil spécifique de TechDraw dans la vue.
6.  Une fois que le \"base-sketchTD\" a été défini dans la vue, nous pouvons passer à la cotation avec les outils TechDraw appropriés ;

Il est possible d\'insérer le \"base-sketchTD\" aussi dans les vues du groupe de projection:

-   sélectionnez la vue de projection -\> onglet propriétés -\> Données -\> section d\'enregistrement \"Projection\" -\> Source cliquez sur le bouton avec les trois points et ajoutez directement la \"base-sketchTD\" ou la couche qui la contient.

:   Il faut noter que la \"base-sketchTD\" doit être positionnée sur la face la plus haute du modèle/objet, sinon elle sera cachée et sera invisible dans TechDraw.

Les sections obtenues à partir des vues ne semblent pas avoir cette possibilité. Lorsqu\'il est nécessaire de créer des points cosmétiques précis adaptés au dimensionnement (par exemple des points de tangence), ils peuvent être générés :

-   dans \"Sketcher\" par des lignes de construction et en insérant des cercles avec un diamètre / rayon infinitésimal (0.00001) aux extrémités, ceux-ci seront vus par TechDraw comme des points / sommets appropriés pour la cotation ;
-   dans le projet, avec la même méthode, être inséré dans le calque ou le groupe de dossiers correspondant ;

:   une fois que le \"base-sketchTD\" a été modifié ou que l\'objet Draft a été ajouté dans le calque ou le dossier-groupement, TechDraw mettra automatiquement à jour la vue, si cela ne se produit pas, mettez à jour manuellement avec la commande appropriée.

Pour insérer des remplissages de section ou des motifs :
faites attention aux lignes créées sur les faces qui coupent deux ou plusieurs arêtes, elles sont vues par TechDraw comme des éléments de séparation de la face qui affectent la création des remplissages ou des motifs. Cela se produit par exemple lors de la création des lignes extérieures qui définissent le fil d\'un trou, cette ligne empêchera le remplissage ou le motif de s\'étendre plus loin en l\'empêchant d\'arriver sur celle qui définit le pré-trou. Dans ce cas, il est préférable de créer des points cosmétiques à travers des lignes de construction en insérant des cercles de rayon infinitésimal dans les sommets qui seront vus par TechDraw comme des points cosmétiques et ensuite les joindre dans TechDraw avec créer une ligne cosmétique par deux points.
Toutes les lignes et / ou chemins (y compris cosmétiques) qui sont affichés dans les vues peuvent être édités dans la mise en forme par la commande \"Change Apparence of selected Lines\" de TechDraw.
Pour créer des sections continues spécifiques sur différents axes ou plans, j\'ai utilisé l\'atelier \"WorkFeatureDev\" qui permet de créer des plans \"solides\", avec une épaisseur de \"0\", en sélectionnant trois sommets. Ces plans peuvent être joints par une arête commune ou superposée en utilisant les fonctions booléennes de l\'atelier \"Part\" et ensuite utilisés pour trancher / sectionner le modèle solide par la commande \"Slice apart\" du même atelier. Les faces des objets découpés peuvent être convenablement exploitées pour la création, avec la fonction \"Facebinder\", des \"base-sketchTD \"s pour produire des vues de section spécifiques dans TechDraw et donc pour pouvoir les dimensionner et les détailler.
Je crois avoir rendu public chaque \"truc\" (ou plutôt système) expérimenté pour pouvoir utiliser des outils plus spécifiques (non fournis pour TechDraw) et créer des dessins techniques professionnels de haute qualité sans aucune limite, rendant l\'atelier TechDraw plus efficace et adaptable à tout besoin , selon toute vraisemblance au même niveau (sinon plus flexible et puissant) que les pairs commerciaux.
Il faut dire, ce qui n\'est pas négligeable, qu\'avec ce système il est possible de créer des fichiers 2D entiers et de les citer avec TechDraw de la même manière que \"LibreCad\" ou \"Autocad LT\" ou d\'autres cads bidimensionnels.
J\'espère avoir été suffisamment clair (si la traduction le permet) en expliquant la procédure (\" truc / système \") que je crois \" plus facile à faire qu\'à dire \", puisqu\'il s\'agit de pouvoir entrer des dessins 2D dans les vues des TD créés avec \" Draft \" et/ou avec \" Sketcher \" simplement en les sélectionnant dans la structure et en créant une vue dans le TD avec la commande appropriée \" créer une vue \" ; mais j\'ai pensé faire quelque chose d\'agréable et de plus technique en décrivant la procédure, certes, de manière \" simplifiée \" pour créer un minimum de flux de travail organisé.
A chacun de nous, avec imagination et inventivité, de l\'optimiser au maximum pour obtenir le meilleur résultat.
Je vous joins les fichiers de quelques exemples de flux de travail de dessins techniques (irréalisables avec TechDraw uniquement) dont ont été tirées les images présentées ci-dessous.
En espérant avoir été utile, bon travail et bonne expérimentation !

## Remarques

## Perspectives futures 

Cependant, le chemin décrit pourrait représenter le point de départ (ou l\'idée) d\'écrire du code supplémentaire pour automatiser le système et l\'intégrer directement dans TechDraw avec les fonctions de bouton / commande appropriées.

## Liens

-   [Macro WorkFeatures](https://wiki.freecadweb.org/Macro_WorkFeatures) Page wiki sur les macros.
-   [FreeCAD atelier WorkFeature](https://github.com/Rentlau/WorkFeature-WB) Dépôt vers code source
-   [TechDraw without limits = Layout autocad](https://forum.freecadweb.org/viewtopic.php?t=54499) (en anglais) Fil de discussion
-   [TechDraw : - come utilizzare gli strumenti Draft/Snaps per creare \" vertici/punti cosmetici \"](https://forum.freecadweb.org/viewtopic.php?f=28&t=53329) Fil de discussion en langue italienne


{{Tutorials navi

}} {{TechDraw Tools navi}} 
