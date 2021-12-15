# <img alt="Icône de l\'atelier ExplodedAssembly" src=images/ExplodedAssembly_workbench_icon.svg  style="width:64px;"> ExplodedAssembly Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/ExplodedAssembly_workbench_icon.svg  style="width:24px;"> [atelier ExplodedAssembly](ExplodedAssembly_Workbench/fr.md) est un atelier externe permettant de créer des vues éclatées et des animations d\'assemblages.

## Fonctions

-   Crée de beaux éclatés d\'assemblages graphiquement (pas de code du tout!)
-   Crée des groupes sous-éclatés
-   Donne une rotation aux vis et aux écrous pour des démontages réalistes
-   Utilise les outils d\'assemblage auxiliaires fournis pour placer vos pièces ensemble
-   Fonction A FAIRE: créer une trajectoire à partir de polylignes et d\'esquisses

## Références

-   Auteur : JMG1
-   Page d\'accueil : [ExplodedAssembly](https://github.com/JMG1/ExplodedAssembly)
-   Code source sur github : [ExplodedAssembly](https://github.com/JMG1/ExplodedAssembly)

## Outils

![](images/ExplodedAssembly-menu-orizz.png ) 
*Barre d'outils*

![](images/ExplodedAssembly-menu-vert.png ) 
*Menu*

### Outils standards 

-   <img alt="" src=images/ExplodedAssembly_CreateBoltGroup.png  style="width:32px;"> Créer un groupe de boulons
-   <img alt="" src=images/ExplodedAssembly_CreateSimpleGroup.png  style="width:32px;"> Créer un groupe simple
-   <img alt="" src=images/ExplodedAssembly_ModifyIndividualObjectTrajectory.png  style="width:32px;"> Modifier la trajectoire d\'un objet individuel
-   <img alt="" src=images/ExplodedAssembly_PlaceBefore.png  style="width:32px;"> Placer avant
-   <img alt="" src=images/ExplodedAssembly_ExplodeToSelection.png  style="width:32px;"> Exploser vers la sélection
-   <img alt="" src=images/ExplodedAssembly_Assemble.png  style="width:32px;"> Assembler
-   <img alt="" src=images/ExplodedAssembly_PlayBackwards.png  style="width:32px;"> Jouer à l\'envers
-   <img alt="" src=images/ExplodedAssembly_StopAnimation.png  style="width:32px;"> Arrêter l\'animation
-   <img alt="" src=images/ExplodedAssembly_PlayForward.png  style="width:32px;"> Lire en avant
-   <img alt="" src=images/ExplodedAssembly_Disassemble.png  style="width:32px;"> Désassembler
-   <img alt="" src=images/ExplodedAssembly_TrajectoryVisibility.png  style="width:32px;"> Visibilité de la trajectoire
-   <img alt="" src=images/ExplodedAssembly_AlignToEdge.png  style="width:32px;"> Alignement sur le bord
-   <img alt="" src=images/ExplodedAssembly_Rotate90.png  style="width:32px;"> Rotation de 90
-   <img alt="" src=images/ExplodedAssembly_PoinToPoint.png  style="width:32px;"> Pointer vers le point
-   <img alt="" src=images/ExplodedAssembly_PlaceConcentrically.png  style="width:32px;"> Placer de façon concentrique

### Outils supplémentaires 

Ces outils peuvent être ajoutés à une barre d\'outils personnalisée. Voir [Personnalisation de l\'interface](Interface_Customization/fr.md).

-   <img alt="" src=images/ExplodedAssembly_AnimationCameraEdge.png  style="width:32px;"> Bord de la caméra d\'animation
-   <img alt="" src=images/ExplodedAssembly_AnimationCameraFollow.png  style="width:32px;"> Suivi de la caméra d\'animation
-   <img alt="" src=images/ExplodedAssembly_AnimationCameraManual.png  style="width:32px;"> Manuel de la caméra d\'animation
-   <img alt="" src=images/ExplodedAssembly_WireTrajectory.png  style="width:32px;"> Trajectoire de la ligne

## Installation

### Installation automatique 

Cet atelier peut être installé à partir du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

### Depuis GitHub 

Utilisation de git sur Ubuntu et Mint :

-   Ouvrez l\'invite de commande (terminal) avec les touches **Ctrl**+**Alt**+**t**
-   Installez git : {{Incode|sudo apt-get install git}}
-   Cloner le dépôt : {{Incode|<nowiki>git clone https://github.com/JMG1/ExplodedAssembly ~/.FreeCAD/Mod/ExplodedAssembly</nowiki>}}

C\'est tout, la prochaine fois que vous lancerez FreeCAD, l\'atelier devrait être disponible.

Pour installer manuellement, téléchargez ce dépôt en ZIP et :

-   Pour Ubuntu, Mint et les OS similaires, extrayez-le à l\'intérieur de : {{FileName|/home/username/.FreeCAD/Mod}}.
-   Pour Windows, extrayez-le à l\'intérieur de : {{FileName|C:\Users\votre_nom_d'utilisateur\AppData\Roaming\FreeCAD\Mod}}.

## Liens vers l\'atelier ExplodedAssembly 

-   Forum FreeCAD : <http://forum.freecadweb.org/viewtopic.php?f=24&t=9028>
-   Vidéos : [1](https://www.youtube.com/watch?v=lzYR7I2h7KQ) [2](https://www.youtube.com/watch?v=t72qdG772Q8&feature=youtu.be)
-   Fichiers : à l\'intérieur de l\'atelier
-   Signaler les bogues : Veuillez signaler les bogues sur <https://github.com/JMG1/ExplodedAssembly/issues>

## Autres liens intéressants 

-   [Ateliers externes](External_workbenches/fr.md)
-   [Liste des macros](Macros_recipes/fr.md)




_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > ExplodedAssembly Workbench/fr
