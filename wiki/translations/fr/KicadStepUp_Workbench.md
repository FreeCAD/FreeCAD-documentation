# <img alt="Icône de l\'atelier externe KicadStepUp" src=images/Kicad-StepUp-tools-WB.svg  style="width:64px;"> KicadStepUp Workbench/fr


{{TOCright}}

## Introduction

L\'atelier KicadStepUp a pour but d\'aider les utilisateurs de KiCad et de FreeCAD à collaborer dans la conception électrique (ECAD) et mécanique (MCAD).

## Contexte

Kicad ([site Web](https://kicad-pcb.org/)) est une suite d\'automatisation de conception électronique Open Source. Il permet de concevoir un circuit électrique et de créer un circuit imprimé monocouche ou multicouche en utilisant une vaste bibliothèque de pièces. Le point important est que l\'utilisation de FreeCAD et KicadStepUp est le moyen officiel de Kicad de créer des pièces 3D pour des composants électriques pour Kicad. Les bibliothèques sont hébergées [ici](https://kicad.github.io/) et donc tout le monde peut créer et archiver des pièces.

La philosophie de l\'interface graphique de KiCAD est un peu différente de celle de FreeCAD, en particulier lorsqu\'il s\'agit de créer des éléments et de les déplacer. Cependant, comme Kicad est utilisé en production depuis des années, il existe une excellente documentation, par ex. un très bon document \"Getting Started\". De plus, chaque outil a son propre manuel.

Si on ne connaît pas encore [Kicad](https://kicad-pcb.org/), il est recommandé de compléter un PCB autonome selon le [Guide de démarrage](https://docs.kicad-pcb.org/5.1/en/getting_started_in_kicad/getting_started_in_kicad.pdf) pour comprendre les concepts. Bien que certains sujets comme l\'ajout de nouveaux schémas et empreintes à une bibliothèque locale semblent peu intéressants pour le débutant, dans la pratique, ils sont souvent rencontrés rapidement après le démarrage d\'un projet sérieux.

Pour tous ces concepts [Kicad](https://kicad-pcb.org/), on peut trouver une fonctionnalité quelconque dans l\'atelier KicadStepUp. Donc, en sachant cela, il est beaucoup plus facile de comprendre comment utiliser cet atelier.

## Fonctionnalités


{{emphasis|En cours}}

-   Chargez la carte kicad et les pièces dans FreeCAD et exportez-les vers STEP (ou IGES) pour une collaboration ECAD MCAD complète
-   Charger l\'empreinte kicad\_mod dans FreeCAD pour aligner facilement et précisément le modèle mécanique sur l\'empreinte kicad
-   Convertissez le modèle STEP 3D de pièces, carte, boîtier en VRML avec les propriétés des matériaux pour une meilleure utilisation dans kicad
-   Vérifiez les interférences et les collisions pour la conception de l\'enceinte et de l\'empreinte
-   Concevez un nouveau circuit imprimé avec FreeCAD Sketcher et le mettre sur une carte kicad\_pcb existante
-   Tirer un circuit imprimé à partir d\'une carte kicad\_pcb, le modifier dans FC Sketcher et le repousser vers kicad
-   Concevez une nouvelle empreinte dans FreeCAD pour obtenir la puissance de Sketch dans les empreintes
-   Générez des fichiers VRML compatibles avec Blender

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width:800px;">

## Installation

KicadStepUp fait partie des [ateliers externes](external_workbenches/fr.md) et peut être installé automatiquement à l\'aide de <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addon](Addon_Manager/fr.md) fourni avec FreeCAD 0.17 dans le menu **Outils → Gestionnaire d'Addon**.

## Utilisation


{{emphasis|En cours}}

### Approche générale 

L\'idée de base de KicadStepUp est de synchroniser les données entre les deux applications. Pour un usage domestique, vous pouvez avoir ouvert FreeCAD et Kicad en même temps. Une utilisation professionnelle travaille sur les mêmes fichiers (par exemple sur un serveur central) et dispose de spécialistes en CAO mécanique (MCAD) travaillant dans FreeCAD et d\'experts en électronique en CAO électrique (ECAD).

KicadStepUp convertira les fichiers FreeCAD standard en fichiers Kicad et vice versa. De cette façon, chaque application peut fonctionner avec ses fichiers de données natifs. Les projets peuvent être utilisés sans l\'autre application ou KicadStepUp installé. C\'est aussi la raison pour laquelle aucun plugin du côté Kicad n\'est requis.

Comprendre les petits détails du flux de travail, il est utile de noter que les différences entre les deux programmes imposent des difficultés pour un échange de données complet.
Un exemple est que le Sketcher utilisé dans Kicad pour définir le contour du tableau est beaucoup plus limité que FreeCAD Sketcher, afin de synchroniser les aller-retours, le contenu du modèle ne peut pas être plus complexe que ce que Kicad Sketcher peut gérer. D\'un point de vue FreeCAD, cela signifie que vous risquez de perdre des données. KicadStepUp propose des solutions de contournement qui pourraient être plus difficiles à comprendre si vous n\'avez pas ce contexte.

### Processus de base 

Une collaboration peut être démarrée avec un projet nouveau ou existant. Nous considérons ici un nouveau projet pour garder les choses simples:

1.  Créez un nouveau projet Kicad où vous le souhaitez. Appelons-le \"KsuTest\"
2.  Ouvrez l\'éditeur PCB et créez sur le calque \"Edit.Cuts\" un contour fermé. La forme n\'a pas d\'importance, nous l\'écraserons de toute façon.
3.  Créez un nouveau fichier FreeCAD pour le PCB, le nom n\'a pas d\'importance. \*
4.  Créez un schéma avec un contour du PCB souhaité. Nommons le \"pcb design\" (mais cela pourrait être n\'importe quel autre nom) et mettons au moins un cercle dedans pour un trou.

    :   Vous pouvez utiliser toutes les fonctionnalités de FreeCAD pour inclure des trous, des découpes et une forme extérieure à d\'autres composants que vous pourriez avoir. Nous supposons ici que vous utiliserez les fonctions d\'esquisse comme géométrie de cotation, de contraintes et de travail dans votre esquisse.
    :   Si vous utilisez PartDesign WB pour créer l\'esquisse, il n\'est pas nécessaire de créer un corps PartDesign, car nous n\'allons pas remplir cette esquisse.
5.  Passer à l\'atelier KicadStepUp
6.  Sélectionnez le croquis \"PCB design\"
7.  Sélectionnez le bouton de la barre d\'outils \"Push Sketch to PCB Edge\" ou le menu *ksu PushPull/ksu Push Sketch to PCB*
    -   D\'abord une boîte de dialogue s\'ouvrira avec les valeurs par défaut \"Edge.Cuts\" pour le calque et \"0.16\" pour la largeur de ligne. Conservez ces valeurs par défaut.
    -   Ensuite, une boîte de dialogue de fichier s\'ouvre. Cliquez sur votre projet Kicad \"KsuTest\", où vous devriez voir un fichier \"KsuTest.kucad\_pcb\". C\'est le fichier PCB avec le contour temporaire que nous avons créé auparavant. Sélectionnez est et confirmez pour remplacer l\'ancien fichier.
        Maintenant, une boîte de dialogue devrait dire \"new Edge pushed to kicad board!\"

        :   Si vous avez oublié la 2ème étape, l\'opération push risque d\'échouer car un fichier pcb doit exister et il ne doit pas être vide.
8.  Fermez et rouvrez l\'éditeur de PCB dans Kicad. \*\*

    :   La forme de l\'esquisse FreeCAD doit apparaître.
9.  parcourez le cercle avec la souris et appuyez sur *m* sur le clavier pour déplacer le cercle. Cliquez pour placer à une autre position. Appuyez sur le bouton Enregistrer de la barre d\'outils en haut à gauche.
10. Passez à FreeCAd et sélectionnez dans le KicadStepUp Workbech le bouton outil \"Pull Sketch from PCB\" ou le menu *ksu PushPull/ksu Pull Sketch from PCB*
    -   La première boîte de dialogue avec le calque par défaut \"Edge.Cuts\" et trois choix s\'ouvriront. Sélectionnez le choix \"replace PCB and Sketch in current document\" \*\*\*
    -   Ensuite, une boîte de dialogue de fichier devrait afficher à nouveau le fichier \"KsuTest.kucad\_pcb\". Sélectionnez-le et appuyez sur *Open*

        :   Vous devriez voir votre PCB comme un modèle 3D. Notez que le trou s\'est déplacé par rapport à votre esquisse \"pcb design\".
        :   Dans l\'arborescence apparaît une nouvelle structure avec un *Part Container* jaune avec le nom de fichier Kicad et dans un autre *Part Container* avec \"Board\_Geoms\_e63b\" (la partie avec le numéro probablement différent). Dans le deuxième conteneur, il y a les trois fichiers suivants. Ne changez aucun nom dans cette structure, car KicadStepUp les utilise pour trouver les pièces à mettre à jour.
        :   N\'oubliez pas de sauvegarder votre fichier




    Local_CS_e63b    le PCB d'origine
                         identique à l'origine dans l'esquisse de "conception de circuits imprimés"
    Pcb_e63b         l'objet 3D avec le PCB.
                          Ne modifiez pas, il sera écrasé par KicadStepUp
    PCB_Sketch_e63b  le schéma avec toutes les parties du schéma "PCB Design" que Kicad a reconnu.
                          tous les autres ont été supprimés. Notez également que si vous modifiez cette esquisse
                          et recalculer l'objet 3D ne changera pas.

Essayez de faire un autre aller-retour PushPull: ajustez votre esquisse de *conception de circuits imprimés* aux modifications de Kicad, ajoutez d\'autres modifications et recommencez. Faites-le plusieurs fois pour apprécier la rapidité et la nature de cette procédure en très peu de temps.

Vous pouvez maintenant utiliser le nouveau fichier PCB 3D pour aligner des composants 3D en tant que connecteurs, boutons, commutateurs, attaches, etc\... ou l\'ajouter à votre assemblage si vous avez un projet plus important.

Cela ne montre que le fonctionnement très basique de KicadStepUp. Il vous manque encore beaucoup à ce stade, par exemple les empreintes et les pièces 3D. Mais à partir de là, il est beaucoup plus facile de commencer à explorer KicadStepUp par vous-même. Utilisez le fichier PDF de la documentation dans le menu *ksu Tools/Demo*

:   \'\'Remarques:
    -   Tant que le nom de la structure créée (et de ses parties) reste inchangé, toutes les interactions de flux de travail mettront simplement à jour la structure. Si vous modifiez des noms, une nouvelle structure sera créée à chaque fois.
    -   Il n\'est pas nécessaire que Kicad fonctionne pour mettre à jour les fichiers de projet Kicad. En fait, Kicad n\'a même pas besoin d\'être installé sur le PC.
    -   L\'approche standard consiste à utiliser le même croquis des deux côtés Kicad et Freecad. Toutes les modifications seront synchronisées avec l\'autre application. C\'est la façon la plus naturelle et la plus propre de travailler avec KicadStepUp.
        Cependant, cela pose un problème si vous souhaitez utiliser l\'une des fonctionnalités suivantes dans votre esquisse pour définir la forme de votre PCB: dimensions, contraintes géométriques, géométrie de travail (lignes bleues) ou géométrie liée externe. Il n\'y a pas de moyen propre de le faire, car Kicad ne connaît aucune des fonctionnalités. Cela signifie que lors de l\'aller-retour entre les applications, l\'une de ces fonctionnalités sera supprimée. Il n\'y a pas de vraie solution à ce problème, juste une sélection de l\'une des nombreuses solutions de contournement. Donc, si vous souhaitez utiliser l\'une de ces fonctionnalités, cela signifie que vous définissez la forme du PCB dans FreeCAD uniquement et que vous synchronisez d\'une manière avec Kicad. Toutes les modifications de contour effectuées dans Kicad doivent être ajoutées manuellement du côté FreeCAD. Cela peut avoir du sens, par exemple si des changements futurs du côté mécanique sont beaucoup plus probables que du côté électrique. Il y a plusieurs façons de le faire
        -   Placez l\'esquisse de conception dans la structure KicadStepUp, puis sélectionnez \"remplacer le PCB et conserver Sketch dans curr. Doc\" à chaque fois que vous importez de Kicad.
        -   Conservez l\'esquisse de conception en dehors de la structure KicadStepUp. Ignorez l\'esquisse importée de Kicad.

    :   Le deuxième choix a l\'avantage que les changements dans Kicad peuvent être attribués à l\'esquisse originale et l\'esquisse FreeCAD est protégée contre un choix d\'importation accidentellement erroné. Le flux de travail décrit utilise cette approche pour s\'assurer que le problème est bien compris. À partir de là, il est facile de passer à la modification de l\'esquisse fournie par KicadStepUp sans aucune des fonctionnalités FreeCAD les plus avancées.

    -   Pour utiliser KicadStepUp avec un assemblage FreeCAD (\> V0.19), vous pouvez ajouter un nouveau fichier pour le PCB. Une fois que le flux de travail ci-dessus a été exécuté, ajoutez l\'objet 3D pour le PCB à votre assemblage comme n\'importe quelle autre pièce mécanique. Assurez-vous d\'enregistrer le fichier lorsqu\'il a été mis à jour par KicadStepUp (KicadStepUp écrit dans la mémoire FreeCAD et non dans les fichiers FreeCAD).

-   Veuillez consulter [kicad StepUp cheat sheet](https://github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf) pour d\'autres fonctions.

## Références

-   Auteur: Github: [\@easyw](https://github.com/easyw) \| FreeCAD Forums: [kicad StepUp: ECAD MCAD bidirectional collaboration](https://forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Code source sur GitHub: <https://github.com/easyw/kicadStepUpMod>

## Remarque annexe et ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), de ce fait, beaucoup de personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page [ateliers externes](external_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux, et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, tenez vous au courant!




[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)

---
[documentation index](../README.md) > KicadStepUp Workbench/fr
