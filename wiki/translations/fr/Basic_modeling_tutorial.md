# Basic modeling tutorial/fr
{{TutorialInfo/fr
|Topic= Introduction à la modélisation
|Level= Débutant
|Time= 15 minutes
|Author=[NormandC](User_Normandc.md)
|FCVersion=toutes
|Files=aucun
}}

## Introduction

Ce **tutoriel d\'introduction à la modélisation** vous montrera comment modéliser un fer angle (cornière). Une chose à savoir, FreeCAD est modulaire, et comme pour plusieurs autres logiciels de CAO, il y a souvent plus d\'une façon de faire les choses. Ici, nous explorerons deux méthodes.

## Avant de commencer 

Gardez en tête que FreeCAD est toujours à un stade précoce de développement, il est donc possible que vous ne soyez pas aussi productif qu\'avec une autre application de CAO, et il est fort probable que vous rencontriez des bogues, ou subissiez des plantages. FreeCAD offre maintenant la possiblité de créer des fichiers de sauvegarde. Le nombre de ces fichiers peut être réglé dans le menu *Édition \> Préférences*, onglet *Document*. N\'hésitez pas à allouer deux ou trois fichiers de sauvegarde jusqu\'à ce que vous soyez à l\'aise avec FreeCAD.

Sauvegardez régulièrement votre travail, et de temps en temps, sauvegardez-le sous un nom différent afin d\'avoir une copie sûre sur laquelle vous rabattre ; enfin, attendez-vous à la possibilité que certaines commandes ne vous donnent pas les résultats escomptés.

## Introduction aux techniques de modélisation 

La première technique (et celle de base) de la modélisation solide est la [géométrie de construction de solides (GCS)](http://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides). Il y a aussi une explication détaillée (dans le contexte de FreeCAD) de [Géométrie Solide Constructive](Constructive_solid_geometry/fr.md) sur le wiki. Vous construisez votre géométrie à l\'aide de formes primitives telles que des cubes, cylindres, sphères et cônes en les combinant, par soustraction d\'une forme par une autre, ou par l\'intersection de deux formes. Ces outils font partie de l\'[atelier Pièce](Part_Workbench/fr.md). Vous pouvez également appliquer des transformations aux formes, par exemple des congés (arrondis) ou chanfreins à des arêtes. Ces outils sont également dans l\'[atelier Pièce](Part_Workbench/fr.md).

Puis il y a des outils plus avancés. Vous commencez par dessiner une esquisse en 2D qu\'ensuite vous extruderez ou ferez révolutionner.

Commençons par la création d\'un pied en fer en L (cornière) pour fabriquer un établi, avec ces deux méthodes.

## 1ère méthode - par géométrie de construction de solides 

1.  Commencez avec l\'[atelier Part](Part_Workbench/fr.md) ![](images/Switch_PartWorkbench.JPG ).
2.  Si vous n\'avez pas créé un nouveau document FreeCAD (l\'essentiel de la fenêtre de FreeCAD paraît alors grisée), allez dans le menu déroulant **Fichier → Nouveau** ou cliquez sur <img alt="" src=images/Document-new.png  style="width:32px;"> **Créer un nouveau document vide**.
3.  Cliquez sur le bouton <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cube](Part_Box/fr.md) pour créer un cube.
4.  Changez ses dimensions en le sélectionnant soit dans l\'espace 3D, soit en le cliquant dans l\'onglet Projet à gauche, puis
5.  Cliquez sur l\'onglet Données en bas, et changez les valeurs de la Longueur, de la Largeur et de la Hauteur en 50mm, 50 et 750 *(voir Fig. 1.1)*. **Remarque** : *lorsque ces captures ont été faites, les propriétés étaient classées différemment, la Hauteur étant la première*.
6.  La boîte remplit maintenant la majeure partie de la vue 3D. Cliquez sur <img alt="" src=images/Std_ViewFitAll.svg  style="width:32px;"> [Tout afficher](Std_ViewFitAll/fr.md) pour adapter la vue à la boîte nouvellement créée.
7.  Vous allez maintenant soustraire la deuxième boîte de la première. Sélectionnez d\'abord la première forme (nommée Box), puis la seconde (nommée Box001), l\'ordre de sélection est important ! (Assurez-vous que les deux formes sont sélectionnées dans l\'arbre du projet. **Une chose à retenir :** en mode de navigation Inventor, **Ctrl** + clic ne fonctionne pas pour la sélection multiple. Changez votre mode de [Navigation de la souris](Mouse_navigation.md) soit CAD soit Blender).
8.  Sur la barre d\'outils Part, cliquer sur l\'outil <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Soustraction](Part_Cut/fr.md).

![Fig. 1.1 Le premièr cube](images/Tutorial-normand01.jpg )

![Fig. 1.2 Le second cube par dessus le premièr, prêt à être soustrait](images/Tutorial-normand02.jpg )

![Fig. 1.3 Après la soustraction](images/Tutorial-normand03.jpg )

Nous avons maintenant notre premier fer en L *(Fig. 1.3)*. Remarquez que dans l\'onglet *Projet* tab du panneau latéral, les deux cubes ont été remplacés par un objet « **Cut** ». En fait, les formes initiales sont toujours présentes, mais groupées sous l\'objet **Cut**. Cliquez sur le **+** situé devant, ce qui affichera leurs noms, mais en grisé *(Fig. 1.4)*. Cliquez sur l\'un ou l\'autre et appuyez sur la **barre d'espace** pour afficher la boîte dans la fenêtre de modèle. La barre d\'espace est un raccourci-clavier pour [basculer la visibilité](Std_ToggleVisibility/fr.md) des éléments. *(Fig. 1.5)*

Vous voulez changer l\'orientation du fer L ? Vous n\'avez qu\'à modifier le placement du cube **Box001**. Sélectionnez-le, rendez-le visible, et dans l\'onglet *Données*, cliquez sur le **+** devant *Placement*, puis déployez la Position, et changez les coordonnées X et Y. Appuyez sur la touche **Entrée**, masquez à nouveau la forme **Box001**, et l\'angle d\'orientation est maintenant différent. *(Fig. 1.5)* Vous pouvez également modifier n\'importe quelle des dimensions de vos formes, et l\'objet **Cut** s\'adaptera automatiquement.

![Fig. 1.4 L\'opération **Cut** conserve ses objets originaux (les cubes)](images/Tutorial-normand04.jpg )

![Fig. 1.5 Les cubes originaux peuvent être rendus visible](images/Tutorial-normand05.jpg )

Par ailleurs, nous pouvons ajouter des congés afin de rendre le fer en L plus réaliste, à l\'aide de l\'outil <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Congé](Part_Fillet/fr.md). *(Fig. 1.6)* En sélectionnant l'arête à modifier (d\'1 clic), on peu en sélectionner plusieurs (touche Ctrl+clic) qui auront le même rayon

![Fig. 1.6 Les arêtes avec congés](images/Tutorial-normand06.jpg )

## 2ème méthode - par l\'extrusion d\'une esquisse 

Avec cette méthode, nous commençons par dessiner un profil 2D. Activez l\'[atelier Draft](Draft_Workbench/fr.md) ![](images/Switch_DraftWorkbench.JPG ).

-   Si vous n\'avez pas créé de nouveau document FreeCAD (l\'essentiel de la fenêtre FreeCAD paraît alors grisé), aller dans le menu Fichier → Nouveau ou cliquer sur Créer un nouveau document vide <img alt="" src=images/Document-new.png  style="width:32px;">.

### Réglage du plan de travail 

Ensuite nous devons régler le [plan de travail](Draft_SelectPlane/fr.md). Selon votre version de FreeCAD, vous trouverez tout juste au dessous et à droite de la barre d\'outils un bouton identifié « **None** » ou encore « **Auto** ». Cliquez-le, et à sa gauche apparaîtra le texte « Commande active : Sélectionnez un plan de travail », puis un champ texte et une série de boutons. Nous dessinerons ce profil sur la vue en plan, en sélectionnant XY. Le bouton « None » montrera maintenant « top » comme plan actif.

Sélectionnez l\'outil <img alt="" src=images/Draft_Wire.png  style="width:32px;"> [Filaire (ligne filaire à plusieurs points)](Draft_Wire/fr.md), et commencez à dessiner un profil, en utilisant les champs texte pour les positions X et Y. Cochez la case « Relatif », ainsi que la case « Rempli ».

### Dessiner le profil 

1.  Sélectionnez l\'outil <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [DWire (points multiples)](Draft_Wire/fr.md).
2.  Cochez les cases \"Relative\" et \"Filled\".
3.  Plutôt que de dessiner la forme dans la vue 3D, nous entrerons des coordonnées dans les champs de saisie \"Global X\", \"Global Y\" et \"Global Z\". Le processus est le suivant:
    1.  Cliquez dans le champ de saisie \"Global X\";
    2.  Entrez une valeur comme indiqué dans la liste ci-dessous et appuyez sur **TAB** pour accéder au champ de saisie \"Global Y\";
    3.  Entrez la valeur \"Global Y\" et appuyez sur la touche **TAB** pour accéder au champ de saisie \"Global Z\";
    4.  Dans le champ \"Global Z\", laissez la valeur zéro et appuyez sur la touche **ENTER** pour valider les coordonnées du point;
    5.  Répétez les 5 points suivants.
    6.  \* **Coordonnées** (X, Y, Z)

-   1er point: 0,0
-   2ème point: 50,0
-   3ème point: 0,10
-   4ème point: -40,0 **Note:** \"sous FreeCAD 0.16, un bogue supprime le point précédent lors de la saisie du signe moins (-) dans le champ. Une solution de contournement est de saisir une valeur positive, puis de placer le curseur devant le nombre et ajouter le signe moins. (Ce bogue est résolu dans la version 0.17)\"
-   5ème point: 0,40
-   6ème point: -10,0
-   Cliquez sur le bouton **Fermer** pour fermer le profil (Seul les profils fermés sont extrudable). Vous devriez maintenant avoir le profil ci-dessous, nommé **DWire** dans l\'onglet Projet :

![Fig. 1.7 Le Wire de départ](images/Tutorial-normand07.jpg )

Passez en vue axonométrique en appuyant sur la touche **0** (zéro) du pavé numérique.

### Extruder le profil 

Activez l\'<img alt="" src=images/Workbench_Part.svg  style="width:32px;">[atelier Pièce](Part_Workbench/fr.md) soit depuis le [sélecteur de plan de travail](Std_Workbench/fr.md), soit depuis le menu **{{StdMenu|[Affichage](Std_View_Menu/fr.md)** → Atelier → Part}}.

Cliquez sur l\'outil <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extruder](Part_Extrude/fr.md).

Dans l\'onglet Projet, sélectionnez l\'objet **Wire**, puis entrez la valeur désirée, par exemple 750mm. Laissez la direction Z. Cliquez sur « Appliquer ». Un objet **Extrude** devrait apparaître dans l\'onglet Projet *(fig. 1.8)*

![Fig. 1.8 L\'objet extrudé](images/Tutorial-normand08.jpg )

Si cette méthode requiert moins d\'opération que la première, elle présente un léger inconvénient : pour modifier la forme, il faut modifier l\'objet Wire, ce qui est moins aisé que l\'édition des formes primitives telles que les cubes de la méthode précédente.

Il y a plusieurs autres façons de le faire ! J\'espère que ces deux exemples vous permettront de démarrer. Vous aurez sûrement des problèmes en cours de route (je l\'ai fait quand j\'ai appris FreeCAD pour la première fois et je possède une expérience de CAO 3D), mais n\'hésitez pas à poser des questions sur le [forum FreeCAD](https://forum.freecadweb.org) !

### Note sur le bouton Plan de travail 

L\'étiquette sur votre bouton peut-être être différente en fonction de votre version et aussi de ce que vous faisiez précédemment. L\'étiquette de bouton pourrait être \"**Top**\", \"**Front**\", \"**Side**\", \"**None**\" ou une représentation vectorielle telle que **d(0.0,0.0,1.0)**. Elle peut également être vide. Par exemple :

![Select Plane None](images/DraftPlaneNone.png )

![Select Plane Top](images/DraftPlaneTop.png )

![Sélectionnez Afficher le plan](images/DraftPlaneView.png )  Après avoir appuyé sur le bouton, les options seront étendues dans l\'une des configurations suivantes.

![**Select Plane** paramètres comme indiqué dans le mode du panneau Tâches.](images/DraftPlaneTasks.png )

![**Select Plane** paramètres comme indiqué dans le mode Barre d\'outils.](images/DraftPlaneToolbarMode.png ) 

Les instructions ci-dessus fonctionneront, quelle que soit l\'étiquette sur le bouton.


{{Tutorials navi

}}

---
[documentation index](../README.md) > Basic modeling tutorial/fr
