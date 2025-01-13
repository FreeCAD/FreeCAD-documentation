# <img alt="Icône de l\'atelier externe KicadStepUp" src=images/Kicad-StepUp-tools-WB.svg  style="width:64px;"> KicadStepUp Workbench/fr




## Introduction

L\'atelier KicadStepUp a pour but d\'aider les utilisateurs de KiCad et de FreeCAD à collaborer dans la conception électrique (ECAD) et mécanique (MCAD).



## Contexte

KiCad ([site web](https://docs.kicad.org/8.0/fr/)) est une suite Open Source d\'automatisation de conception électronique. Elle permet à l\'utilisateur de concevoir un schéma électronique, puis un circuit imprimé (PCB) simple ou multicouche à l\'aide d\'une vaste bibliothèque de pièces. Utiliser FreeCAD avec l\'atelier KicadStepUp est la méthode officielle de KiCad pour créer des pièces 3D pour les composants électroniques de KiCad. Les bibliothèques sont hébergées [ici](https://gitlab.com/kicad/libraries), de sorte que tout le monde peut créer et enregistrer des pièces.

La philosophie de l\'interface graphique de KiCad est un peu différente de celle de FreeCAD, surtout lorsqu\'il s\'agit de créer des éléments et de les déplacer. Cependant, comme KiCad est utilisé en production depuis des années, il existe une excellente documentation, par exemple, un très bon document \"Getting Started\". En outre, chaque outil dispose de son propre manuel.

Si vous ne connaissez pas encore [KiCad](https://docs.kicad.org/8.0/fr/), il est recommandé de réaliser un circuit imprimé seul en suivant le [Guide de démarrage](https://docs.kicad.org/8.0/fr/getting_started_in_kicad/getting_started_in_kicad.html) pour comprendre les concepts en jeu. Bien que certains sujets tels que l\'ajout de nouveaux schémas et d\'empreintes à une bibliothèque locale semblent peu intéressants pour le débutant, dans la pratique, ils sont souvent rencontrés rapidement après le démarrage d\'un projet sérieux.

Vous trouverez tous ces concepts de [KiCad](https://docs.kicad.org/8.0/fr/) dans l\'atelier KicadStepUp. En les connaissant, il est donc beaucoup plus facile de comprendre comment utiliser cet atelier.



## Fonctions


{{emphasis|En cours}}

-   Chargez la carte et les pièces de KiCad dans FreeCAD et exportez-les en STEP (ou IGES) pour une collaboration ECAD MCAD complète.
-   Chargez l\'empreinte de KiCad dans FreeCAD pour aligner facilement et précisément le modèle mécanique sur l\'empreinte de KiCad.
-   Convertissez le modèle 3D STEP des pièces, des cartes et des boîtiers en VRML avec les propriétés des matériaux pour une utilisation optimale dans KiCad.
-   Vérifiez les interférences et les collisions pour la conception des boîtiers et des empreintes.
-   Concevez une nouvelle carte de circuits imprimés avec l\'[atelier Sketcher](Sketcher_Workbench/fr.md) de FreeCAD et poussez la vers un circuit imprimé existant de KiCad.
-   Récupérez un bord de PCB d\'une carte de PCB de KiCad, l\'éditer dans l\'atelier Sketcher de FreeCAD et le repousser dans KiCad.
-   Concevez une nouvelle empreinte dans FreeCAD pour bénéficier de la puissance de Sketch dans les empreintes.
-   Générez des fichiers VRML compatibles avec Blender.

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width:800px;">

## Installation

KicadStepUp fait partie des [ateliers externes](External_workbenches/fr.md) et peut être installé automatiquement à l\'aide du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md), fourni avec FreeCAD 0.17 et ultérieurement, dans le menu **Outils → Gestionnaire des extensions**.



## Utilisation


{{emphasis|En cours}}



### Approche générale 

L\'idée de base de KicadStepUp est de synchroniser les données entre les deux applications. Pour un usage domestique, vous pouvez avoir FreeCAD et KiCad fonctionnant en même temps. Les utilisateurs professionnels peuvent travailler sur les mêmes fichiers (par exemple sur un serveur central) et avoir des spécialistes de la CAO mécanique (MCAD) travaillant dans FreeCAD et des experts en électronique en CAO électrique (ECAD).

KicadStepUp convertit les fichiers FreeCAD standard en fichiers KiCad et vice versa. Ainsi, chaque application peut travailler avec ses fichiers de données natifs. Les projets peuvent être utilisés sans que l\'autre application ou KicadStepUp soit installé. C\'est aussi la raison pour laquelle aucun plugin n\'est nécessaire du côté de KiCad.

Il est important de noter que les différences entre les deux programmes imposent quelques difficultés pour un échange de données complet.
Un exemple est que le Sketcher utilisé dans KiCad pour définir le contour de la carte est très limité par rapport à l\'atelier Sketcher de FreeCAD. Donc, pour pouvoir synchroniser dans les deux sens, le contenu du schéma ne peut pas être plus complexe que ce que le Sketcher de KiCad peut gérer. Du point de vue de FreeCAD, cela signifie que vous pouvez éviter d\'utiliser certaines des fonctions d\'esquisse de FreeCAD. KicadStepUp propose des solutions de contournement qui peuvent être plus difficiles à comprendre si vous n\'avez pas cette expérience.



### Processus de base 

Une collaboration peut être entamée avec un nouveau projet ou un projet existant. Nous considérons ici un nouveau projet pour garder les choses simples :

1.  Créez un nouveau projet KiCad où vous voulez. Appelons-le \"KsuTest\".
2.  Ouvrez l\'éditeur de PCB et créez sur la couche \"Edit.Cuts\" un contour fermé. La forme n\'a pas d\'importance, nous allons l\'écraser de toute façon.
3.  Créez un nouveau fichier FreeCAD pour le PCB, le nom n\'a pas d\'importance. \*
4.  Créez une esquisse avec un contour du PCB désiré. Nommons le \"pcb design\" (mais cela peut être n\'importe quel autre nom) et mettons au moins un cercle pour un trou.

    :   Vous pouvez utiliser n\'importe quelle fonction de FreeCAD pour inclure des trous, des découpes, et la forme extérieure d\'autres composants que vous pourriez avoir. Nous supposons ici que vous utiliserez les fonctions du Sketcher comme la cotation, les contraintes et la géométrie de travail dans votre esquisse.
    :   Si vous utilisez l\'atelier PartDesign pour créer l\'esquisse, il n\'est pas nécessaire de créer un corps PartDesign, car nous n\'allons pas protruser cette esquisse.
5.  Passez à l\'atelier KicadStepUp.
6.  Sélectionnez l\'esquisse \"pcb design\".
7.  Sélectionnez le bouton de la barre d\'outils \"Push Sketch to PCB Edge\" ou le menu *ksu PushPull/ksu Push Sketch to PCB*.
    -   Une boîte de dialogue s\'ouvre d\'abord avec les valeurs par défaut \"Edge.Cuts\" pour la couche et \"0.16\" pour la largeur des lignes. Gardez ces valeurs par défaut.
    -   Ensuite une boîte de dialogue de fichier va s\'ouvrir. Cliquez sur votre projet KiCad \"KsuTest\", où vous devriez voir un fichier \"KsuTest.kucad_pcb\". C\'est le fichier PCB avec le contour temporaire que nous avons créé auparavant. Sélectionnez-le et confirmez pour remplacer l\'ancien fichier.
        Maintenant une boîte de dialogue devrait dire \"new Edge pushed to kicad board !\"

        :   Si vous avez oublié la 2ème étape, l\'opération de transfert peut échouer car un fichier pcb doit exister et il ne doit pas être vide.
8.  Fermez et ré-ouvrez l\'éditeur de PCB dans KiCad. \*\*

    :   La forme de l\'esquisse de FreeCAD devrait apparaître.
9.  Passez au-dessus du cercle avec la souris et appuyez sur *m* sur le clavier pour déplacer le cercle. Cliquez pour le placer dans une autre position. Appuyez sur le bouton \"Enregistrer\" de la barre d\'outils en haut à gauche.
10. Passez à FreeCAD et sélectionnez dans la zone de travail KicadStepUp le bouton d\'outil \"Pull Sketch from PCB\" ou le menu *ksu PushPull/ksu Pull Sketch from PCB*.
    -   Une première boîte de dialogue avec le calque par défaut \"Edge.Cuts\" et trois choix s\'ouvre. Select choice \"replace PCB and Sketch in current document\" \*\*\*
    -   Ensuite, une boîte de dialogue devrait afficher à nouveau le fichier \"KsuTest.kicad_pcb\". Sélectionnez-le et appuyez sur *Ouvrir*.

        :   Vous devriez voir votre PCB sous la forme d\'un modèle 3D. Notez que le trou s\'est déplacé par rapport à votre croquis \"pcb design\".
        :   Dans l\'arborscence apparaît une nouvelle structure avec un *Part Container* jaune avec le nom de fichier KiCad et dans un autre *Part Container* avec \"Board_Geoms_e63b\" (la pièce avec le numéro probablement différent). Dans le deuxième conteneur, il y a les trois fichiers suivants. Ne changez aucun nom dans cette structure, car KicadStepUp les utilise pour trouver les pièces à mettre à jour.
        :   N\'oubliez pas de sauvegarder votre fichier




    Local_CS_e63b    le PCB d'origine identique à l'origine dans l'esquisse de "conception de circuits imprimés"
    Pcb_e63b         l'objet 3D avec le PCB. Ne modifiez pas, il sera écrasé par KicadStepUp
    PCB_Sketch_e63b  le schéma avec toutes les parties du schéma "PCB Design" que KiCad a reconnu. Toutes les autres ont été supprimées. Notez également que si vous modifiez cette esquisse et
                     recalculez, l'objet 3D ne changera pas.

Essayez de faire un autre aller-retour PushPull : adaptez votre esquisse de \"conception de PCB\" aux modifications apportées par KiCad, ajoutez une autre modification et recommencez. Faites-le plusieurs fois pour apprécier à quel point cette procédure devient rapide et naturelle en très peu de temps.

Vous pouvez maintenant utiliser le nouveau fichier PCB 3D pour aligner des composants 3D en tant que connecteurs, boutons, commutateurs, attaches, etc\... ou l\'ajouter à votre assemblage si vous avez un projet plus important.

Ceci ne montre que la façon très basique dont KicadStepUp fonctionne. Il vous manque encore beaucoup de choses à ce stade, par exemple les empreintes et les pièces 3D, mais à partir de là, il est beaucoup plus facile de commencer à explorer KicadStepUp par vous-même. Utilisez le fichier PDF de documentation dans le menu *ksu Tools/Demo*.

:   \'\'Remarques :
    -   Tant que le nom de la structure créée (et de ses parties) reste inchangé, toute interaction avec le flux de travail ne fera que mettre à jour la structure. Si vous modifiez un nom, une nouvelle structure sera créée à chaque fois.
    -   Il n\'est pas nécessaire que KiCad soit en cours d\'exécution pour mettre à jour les fichiers de projet KiCad. En fait, KiCad ne doit même pas être installé sur le PC.
    -   L\'approche standard consiste à utiliser la même esquisse des deux côtés, KiCad et Freecad. Toute modification sera synchronisée avec l\'autre application. C\'est la façon la plus naturelle et la plus propre de travailler avec KicadStepUp.
        Cependant, cela pose un problème si vous voulez utiliser l\'une des fonctions suivantes dans votre esquisse pour définir la forme de votre PCB : dimensions, contraintes géométriques, géométrie de construction (lignes bleues), ou géométrie externe liée. Il n\'existe aucun moyen propre de le faire, car KiCad ne connaît aucune de ces fonctions. Cela signifie que lors de l\'aller-retour entre les applications, n\'importe laquelle de ces fonctions sera supprimée. Il n\'y a pas de véritable solution à ce problème, il suffit de choisir l\'une des nombreuses solutions de contournement. Donc, si vous voulez utiliser l\'une de ces fonctions, cela signifie que vous devez définir la forme du PCB dans FreeCAD uniquement et synchroniser dans une seule direction vers KiCad. Toute modification de contour effectuée dans KiCad doit être ajoutée manuellement du côté de FreeCAD. Cela peut avoir un sens, par exemple si les changements futurs du côté mécanique sont beaucoup plus probables que du côté électrique. Il y a plusieurs façons de le faire :
        -   Placez l\'esquisse à l\'intérieur de la structure KicadStepUp, et sélectionnez \"replace PCB and keep Sketch in curr. doc\" à chaque fois que vous réimportez depuis Kicad.
        -   Gardez l\'esquisse de conception en dehors de la structure KicadStepUp. Ignorez l\'esquisse importée de KiCad.

    :   Le deuxième choix présente l\'avantage que les modifications apportées dans KiCad peuvent être retracées jusqu\'à l\'esquisse originale et que l\'esquisse FreeCAD est protégée contre un mauvais choix d\'importation accidentel. Le flux de travail décrit utilise cette approche pour s\'assurer que le problème est bien compris. A partir de là, il est facile de passer à la modification de l\'esquisse fournie par KicadStepUp, sans aucune des fonctions plus avancées de FreeCAD.

    -   Pour utiliser KicadStepUp avec un assemblage FreeCAD (\> V0.19) vous pouvez ajouter un nouveau fichier pour le PCB. Après avoir exécuté une nouvelle la procédure ci-dessus, ajoutez l\'objet 3D pour le PCB à votre assemblage comme n\'importe quelle autre pièce mécanique. Assurez-vous de sauvegarder le fichier lorsqu\'il a été mis à jour par KicadStepUp (Important : KicadStepUp écrit dans la mémoire de FreeCAD, pas dans les fichiers FreeCAD).

\'\'

-   Veuillez consulter [KicadStepUp Cheat Sheet](https://github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf) pour d\'autres fonctions.



## Références

-   Auteur: Github: [\@easyw](https://github.com/easyw) \| FreeCAD Forums: [kicad StepUp: ECAD MCAD bidirectional collaboration](https://forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Code source sur GitHub: <https://github.com/easyw/kicadStepUpMod>



## Remarque annexe et ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), de ce fait, beaucoup de personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page [ateliers externes](external_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux, et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, tenez vous au courant!



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > KicadStepUp Workbench/fr
