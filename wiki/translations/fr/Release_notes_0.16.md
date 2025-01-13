# Release notes 0.16/fr
FreeCAD 0.16 a été publié le 18 avril 2016, obtenez la depuis la page [GitHub](https://github.com/FreeCAD/FreeCAD/releases/tag/0.16). Ceci est un résumé des changements les plus intéressants. La liste complète des changements peut être trouvée dans [sur Mantis (en anglais)](http://www.freecadweb.org/tracker/changelog_page.php). Les versions plus anciennes : [0.15](Release_notes_0.15/fr.md) - [0.14](Release_notes_0.14/fr.md) - [0.13](Release_notes_0.13/fr.md) - [0.12](Release_notes_0.12/fr.md) - [0.11](Release_notes_0.11/fr.md)
<img alt="" src=images/Satnogs_Rotator_FreeCAD.jpg  style="width:1024px;">


<center>

Satnogs Rotator (https://satnogs.org/)


</center>

## Nouveautés Principales 

**Le support d\'expression** a été introduit, ce qui permet de définir des relations entre des objets par des formules. Le support d\'expression est une avancée majeur pour créer de meilleurs modèles paramétrique avec FreeCAD. Le support d\'expressions offre une interface simple pour créer des modèle pilotable avec une feuille de tableur.

<img alt="" src=images/Expressions-demo.png  style="width:300px;">

Le comportement du **solveur d\'esquisse** a été grandement amélioré. En plus d\'être plus rapide et plus stable, il ne se bloque plus sur les esquisses insolubles. Et le recalcule automatique du document après chaque petit changement dans l\'esquisse peut désormais être désactivé à la volée, ce qui facilite l\'édition d\'esquisse enterrée sous de profondes dépendances.

<img alt="" src=images/Sketcher-v0.16-demo.png  style="width:300px;">

FreeCAD supporte maintenant de nouveaux styles de navigation dont un tactile. Cela rend possible l\'utilisation de FreeCAD sans souris, sur un laptop convertible, avec un écran tactile et un stylet.

**L\'atelier FEM** a reçu des tonnes d\'améliorations. Il est démontré qu\'il est utilisable pour différents types d\'analyses mécanique.

<img alt="" src=images/Multiple_material.jpg  style="width:700px;">

## Général

-   Support des expressions/formules
-   Trois nouveaux styles de navigation : Gesture (avec le support du tactile sur Windows), Maya, et OpenCascade.
-   Liste des ateliers personnalisable (la liste peut être réordonnée et chacun des ateliers peut être masqué de la liste)
-   Outils de récupération de projet
-   Nouvelles options de sauvegarde (Rétablir, Enregistrer une copie)
-   Nouvelle page d\'accueil

## Atelier Part 

-   Nouvel outils pour fusionner des objets creux (ex: des tuyaux) : [Connecter](Part_JoinConnect/fr.md), [Intégrer](Part_JoinEmbed/fr.md) and [Découper](Part_JoinCutout/fr.md)
-   Nouvelle fonction: Créer une face à partir d\'une esquisse (paramétrique)

## Ateliers PartDesign & Sketcher 

-   Nouvelle fonction : bascule entre les [contraintes Référence et Pilote](Sketcher_ToggleDrivingConstraint/fr.md)
-   Nouvelle fonction : mode création continue (l\'outil reste actif)
-   Nouvelle fonction : contraintes Non-pilote (ou contrainte pilotée)
-   Accélération majeure
-   Contrôle avancé du solveur
-   Nouvelles fonctions : outils pour copier, faire un miroir et un réseau rectangulaire.
-   Support des [expressions/formules](Expressions/fr.md) dans les contraintes et les propriétés.



## Atelier Tableur 

-   Ajout des fonctions : round, trunc, ceil, et floor.



## Atelier Draft 

-   **Nouveau importer DXF**: L\'atelier Draft dispose d\'un tout nouveau importer DXF, codé entièrement en C++, hérité de [HeeksCad](https://github.com/Heeks/heekscad), qui n\'a plus besoin d\'être téléchargé sur Internet et qui est plus rapide et robuste avec les gros fichiers. Une option dans les préférence DXF permet de basculer sur l\'ancien importer si besoin.
-   Un nouvel **[outil Miroir](Draft_Mirror/fr.md)** permet de faire une symétrie \"à la Draft\"
-   Plusieurs **patrons DXF** ont été ajouté en correspondance avec leur modèle SVG facilitant l\'export des pages de dessins en DXF.
-   Les objets [Rectangles](Draft_Rectangle/fr.md),[Filaires et Lignes](Draft_Wire/fr.md) peuvent maintenant être **subdivisés**, permettant toute sorte de nouvelles combinaisons de forme.

<img alt="" src=images/Draft_subdivisions.jpg  style="width:1024px;">

## Atelier Drawing 

-   Un nouvel objet **[Vue tableur](Drawing_SpreadsheetView/fr.md)** permet de placer une région de cellules d\'un [tableur](Spreadsheet_Workbench/fr.md) dans une page de dessin.

<img alt="" src=images/Drawing_spreadsheetview.jpg  style="width:1024px;">

## Atelier Arch 

-   **[Support des Materiaux](Arch_SetMaterial/fr.md)**: Un objet Arch peut maintenant avoir un [matériau](material.md) associé, qui utilise le framework des matériaux intégré à FreeCAD. Ces matériaux sont partagés entre les ateliers. Ils sont pleinement supporté lors de l\'import et l\'export IFC.
-   La **[Section plane](Arch_SectionPlane/fr.md)** peut maintenant faire une coupe dans la vue 3D montrant en temps réel la section.

<img alt="" src=images/Arch_clip_plane.jpg  style="width:1024px;">

-   Plusieurs améliorations de l**\'importer IFC** comme de nouvelles options pour traiter les gros fichier IFC, un meilleur support des extrusions (maintenant détectées à l\'import) et des segments courbe, le support des annotations 2D. L\'import des IFC Analytic a été ajouté. Pour l\'instant l\'import des géométrie de représentation de tout les objets analytique sont supporté.
-   Meilleurs **options de maillage** pour les formats DAE et IFC.
-   Un nouvel outil [Arch Schedule/fr](Arch_Schedule/fr.md) permet de créer différent type de liste de matériaux à partir d\'une maquette BIM.
-   **Les attributs IFC** peuvent maintenant être importés, édités et exportés. Il s\'agit d\'un objet Tableur attaché à un objet Arch.

## Atelier FEM 

-   Les commandes dans **l\'interface** FEM ont maintenant des raccourcis clavier. Une page de préférence FEM à été ajoutée. Le chemin de l'exécutable CalculiX fait partie de ces préférences.
-   **Conteneurs d\'analyse dans l\'interface** Les membres d\'une analyse utilise le glisser/déposer. Ils peuvent être déplacer dans ou en dehors d\'un conteneur d\'analyse. Depuis qu\'il y a le support de multiples analyses, les membres peuvent être déplacés dans une autre analyse. Les contraintes multiple peuvent être créées dans une analyse.
-   **Analyse en un clic dans l\'interface** Un bouton pour lancer en un clic une analyse a été ajouté à l\'interface graphique utilisateur. Il purge les résultats, écrit un fichier d\'entrée CalculiX et réalise l\'analyse avec le solveur sélectionné. Il est détecté si le multithreading est disponible pour CalculiX et utilise le maximum de thread possible.
-   **Fichier d\'entrée** L\'éditeur intégré de FreeCAD supporte l\'édition des fichiers d\'entrée CalculiX (\*.inp). La coloration syntaxique a été implémenté aussi.
-   **Objet maillage Netgen** L\'interface et l\'éditeur de propriété des objets maillage Netgen a été revu. Le maillage tétraédrique de premier et second ordre est supporté tout comme la possibilité d\'ajuster les paramètres de maillage.
-   **Objets contrainte de force et contrainte fixe** Il est maintenant possible d\'ajouter des forces et des fixations sur les arêtes et les points.
-   **Objet contrainte de pression** Un nouvel objet pour le chargement de pression a été ajouté. La pression (chargement surfacique) est passée directement à CalculiX ce qui signifie que le chargement ponctuel sur les nœuds n\'est pas calculé par FreeCAD mais par CalculiX.
-   **Objet de contrainte de déplacement** Un nouvel objet pour contraindre les déplacements a été ajouté. Une contrainte de déplacement peut être ajoutée aux nœuds, arêtes et faces. Pour les analyses de coques et de barres il est possible de fixer les degrés de libertés de rotation.
-   **Objet Section de Poutre** Le nouvel objet section de poutre permet de définir des section rectangulaire pour les poutre FEM. Cela supporte différentes sections en une seule analyse en définissant la forme de référence pour chaque section.
-   **Objet Épaisseur de Coque** Le nouvel objet épaisseur de coque permet de définir l\'épaisseur d\'une coque plate. Comme avec la section de poutre cela supporte de multiple épaisseur en une analyse en définissant les formes de références.
-   **Objet Matériau** Les matériaux multiples sont supportés pour les arêtes, les coques, les maillages solides. Comme pour les objets section de poutre et épaisseur de coque, un maillage FEM approprié est nécessaire pour utilisé les matériaux multiple.
-   **Objet Solveur** En tant que base pour des solveurs multiple l\'objet Solveur a été implémenté. Toutes les propriétés de l'analyse sont déplacées vers le solveur.
-   **Analyse de Fréquence** On peut faire une analyse de fréquence. Le nombre de valeur eigen et de forme eigen peut être ajusté dans la fenêtre des préférences.
-   **View provider** Les maillages FEM de type coques et poutres peuvent être vus dans FreeCAD ainsi que les résultats de l\'analyse.
-   **API Python** Ajout de méthodes pour travailler avec les maillages FEM et réaliser des analyses depuis python.
-   **Macro GMSH** La [Macro_GMSH](Macro_GMSH.md) est un développement externe interessant qui rend possible le maillage avec GMSH. C\'est très pratique pour ceux qui ne peuvent pas installé ou compiler Netgen ou pour le maillage de coques et d\'arêtes.
-   **Améliorations générales** En raison de la forte augmentation du développement, il y a eu des tonnes d\'améliorations sur la base du code du module FEM.



## Atelier Path 

![](images/Exercise_path_02.jpg )

Un nouvel [Atelier Path](Path_Workbench/fr.md) a été ajouté à FreeCAD. Cet atelier bien qu\'encore en développement implémente déjà quelques opérations CNC et permet d\'exporter le fichier [G-code](https://en.wikipedia.org/wiki/G-code) vers diverse variété de machines CNC.

Dans son état actuel, l\'atelier permet de créer des profiles et des poches autour d\'objets basés sur [Part](Part_Workbench/fr.md), de créer des chemin complexe en joignant plusieurs partie de chemin, inspecter et éditer le G-code de chaque chemin, gérer la banque d\'outils et choisir entre différents scripts pre-post-processing lors de l\'import et l\'export de G-code. Il propose aussi une [API Python](Path_scripting/fr.md) complète.



## Modules Additionnels 

Plusieurs nouveaux [ateliers complémentaires](https://github.com/FreeCAD/FreeCAD-addons) ont été créés par des membres de la communauté. Ces ateliers s\'installe très facilement sur une installation existante de FreeCAD. Parmi eux on trouve :

-   Un [atelier Animation](https://github.com/microelly2/Animation) qui vous permet de créer des animations depuis vos modèles FreeCAD, en définissant le mouvement de la caméra et en exportant une séquence d\'images.
-   Une [Kerkythea macro Export Kerkythea](https://github.com/marmni/FreeCAD-Kerkythea) qui permet d\'exporter votre document FreeCAD vers le [logiciel de rendu gratuit Kerkythea](http://www.kerkythea.net/cms/).
-   Un [Menu](http://forum.freecadweb.org/viewtopic.php?f=22&t=10892%7CPie) (menu circulaire) toujours en développement est disponible.
-   Finalement, un [dépôt d\'extensions](https://github.com/FreeCAD/FreeCAD-addons) a été créé pour rassembler tout les ateliers, modules et macros intéressantes qui fleurissent autour de FreeCAD. Ce dépôt propose un utilitaire qui installe et met à jour ces extensions pour vous.

![](images/Macro_installer_02.jpg )



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.16/fr
