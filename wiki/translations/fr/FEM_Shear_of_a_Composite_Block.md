# FEM Shear of a Composite Block/fr
---
- TutorialInfo:/fr
   Topic:Analyse d'éléments finis
   Level:Débutant/intermédiaire
   Time:30 minutes
   Author:[http://www.freecadweb.org/wiki/index.php?title=User: HarryvL]
   FCVersion:0.17.12960 ou plus récente
}}

## Introduction

Dans ce tutoriel, nous analysons la déformation par cisaillement d\'un bloc composite constitué d\'un noyau rigide noyé dans une matrice souple. Il démontre l\'utilisation des BooleanFragments et du CompoundFilter pour créer des solides pour le bloc et la matrice à partir de deux cubes concentriques. Ce flux de travail permet de définir des régions maillées, des matériaux et des conditions limites distincts pour le bloc et la matrice extérieure. Pour sélectionner les régions internes, nous nous basons sur la macro de Markus Hovorka (https://github.com/drhooves/SelectionTools). Les résultats de CalculiX montrent clairement l\'effet du noyau rigide sur la réponse du bloc composite.

## Géométrie

D\'abord nous créons deux cubes concentriques, un de taille 10mm et l\'autre de 5mm. Ceci est fait dans l\'atelier \"Part\". Par défaut le cube est situé à l\'origine \[0, 0, 0\], donc le cube plus petit doit être réduit et déplacé en modifiant les valeurs dans l\'onglet Données du panneau de propriété. Pour rendre le cœur visible, la Transparence du bloc extérieur est mise à 50 dans le panneau Vue de propriété. Le résultat est présenté ci-dessous.

<img alt="" src=images/Pic1.png  style="width:700px;">

Ensuite, mettez en surbrillance les deux blocs dans l\'arborescence et créez des Fragments booléens (Pièce → Scinder → Fragments booléens). Dans l\'\"onglet des Donnees de la fenêtre des propriétés\", changez le mode en CompSolid. Mettez maintenant en évidence les fragments booléens dans l\'arborescence des objets et créez un Filtre composé (Pièce → Composé → Filtre composé).

<img alt="" src=images/Pic2.png  style="width:700px;">

## Maille et Régions de Maille 

À partir de l\'atelier FEM, nous créons un conteneur Analysis. Celui-ci contiendra toutes les définitions requises pour l\'analyse CalculiX et ses résultats. Notez que ce conteneur Analysis doit être activé (cliquez avec le bouton droit de la souris et sélectionnez \"Activate analysis\") chaque fois que vous rechargez le fichier ou après être passé d\'une autre analyse à une autre. Pour démarrer le processus de maillage, mettez en évidence le CompoundFilter dans l\'arborscence des objets et activez le dialogue de maillage \"Mesh → Maillage FEM à partir d\'une forme avec Gmsh\". Quittez la boîte de dialogue en cliquant sur OK.

Un objet Mesh est maintenant créé dans l\'arborscence des objets. Mettez cet objet en surbrillance et créez un objet Mesh Region via \"Mesh → Région de maillage FEM\". Ouvrez la boîte de dialogue de cette région de maillage en double-cliquant et cochez le bouton radio à Solid. Cliquez ensuite sur le bouton \"Add Reference\" et sélectionnez l\'objet CompoundFilter dans la fenêtre graphique. Cela devrait ajouter une référence à \"CompoundFilter:Solid1\" dans la liste des objets de la région de maillage. Enfin, spécifiez la taille maximale des éléments pour cette région (5 mm dans l\'analyse actuelle). Quittez la boîte de dialogue en cliquant sur OK.

<img alt="" src=images/Pic3.png  style="width:700px;">

Créer ensuite un nouvel objet Mesh comme ci-dessus et utilisez la macro de sélection (le raccourci S, E) pour choisir l\'objet Cube_Core dans la fenêtre graphique. Cette fois la liste de référence devrait montrer \"CompoundFilter:Solid2\", comme ci-dessous. Nous avons choisi une taille d\'élément maximale de 1mm.

Remarque1 : la sélection de \"CompoundFilter:Solid2\" exige la sélection d\'une de ses faces.

Remarque2 : si vous avez des difficultés à choisir \"CompoundFilter:Solid2\" c\'est peut-être parce que vous avez oublié de mettre le mode BooleanFragments à CompSolid.

<img alt="" src=images/Pic4.png  style="width:700px;">



## Affectation des matériaux 

Un matériau est attribué aux régions Mesh via un objet SolidMaterial. Dans ce tutoriel, nous affectons deux matériaux : un pour la matrice et un pour le noyau.

Commencez par sélectionner le CompoundFilter dans l\'arborescence des objets. Créez ensuite un objet SolidMaterial via l\'option de menu \"Model → FEM material for solid\". Ouvrez la boîte de dialogue et cochez le bouton radio pour Solid, appuyez sur \"Add Reference\" et sélectionnez l\'objet CompoundFilter dans la fenêtre graphique. La liste des références devrait maintenant afficher \"CompoundFilter:Solid1\", comme précédemment. Nous attribuons un matériau ABS à la matrice, avec un module de Young d\'environ 1 % de celui de l\'acier.

<img alt="" src=images/Pic5.png  style="width:700px;">

Répétez la procédure ci-dessus pour le noyau (\"CompoundFilter:Solid2\") à l\'aide de la macro de sélection. Cette fois, nous assignons l\'acier CalculiX-Steel, qui est beaucoup plus rigide que le matériau ABS pour la matrice.



## Support coulissant 

Pour créer une condition de \"cisaillement simple\" pour le bloc composite, les déformations aux limites ne doivent pas être contraintes. Pour ce faire, le bloc est placé sur un support coulissant. Cela laisse trois degrés de liberté dans le plan du support (2 translations et une rotation) et ceux-ci seront contraints plus tard. (Remarque : comme le plan empêche la déformation de la face, il induit toujours une contrainte mineure, qui pourrait être éliminée par un choix différent des conditions limites). Pour créer une condition limite de glissement, ajoutez un objet FemConstraintDisplacement (Model → Mechanical Constraints → Constraint displacement). La boîte de dialogue étant ouverte, sélectionnez d\'abord la face à laquelle les conditions limites doivent être appliquées, puis cliquez sur le bouton Ajouter. Comme le bloc est autorisé à glisser dans le plan x-y, seul le bouton radio \"Fixe\" pour \"Displacement z\" est sélectionné et les autres boutons radio sont tous laissés à \"Libre\".

<img alt="" src=images/Pic6.png  style="width:700px;">



## Noeuds fixes 

Pour empêcher le mouvement du corps rigide dans le plan de glissement, il faut éliminer trois degrés de liberté indépendants. Pour cela, un sommet du plan de glissement est contraint dans les directions x et y (éliminant 2 degrés de liberté) et un sommet est fixé dans la direction x (éliminant le dernier degré de liberté). Pour ce faire, deux objets FemConstraintDisplacement supplémentaires sont créés et le résultat est illustré ci-dessous.

<img alt="" src=images/Pic7.png  style="width:700px;">

## Forces de cisaillement 

L\'étape finale de la définition de l\'analyse est l\'application des charges. Pour créer une condition de cisaillement simple, un ensemble de charges de cisaillement est appliqué comme indiqué ci-dessous. Chaque charge est choisie comme étant de 1000 N et en considérant les directions d\'application, l\'équilibre des forces et des moments est atteint pour tous les degrés de liberté de translation et de rotation. Dans FC, cela nécessite l\'ajout de quatre objets FemConstraintForce (Model → Mechanical Constraints → Constraint force) - un pour chaque face. La boîte de dialogue étant ouverte, appuyez d\'abord sur le bouton Ajouter une référence, puis sélectionnez la face à laquelle la condition limite doit être appliquée (Remarque : cette séquence est différente de celle utilisée avec FemConstraintDisplacement). Par défaut, cela crée un ensemble de forces perpendiculaires à la face (c\'est-à-dire une force normale). Pour changer cela en une force de cisaillement, appuyez sur le bouton de direction et sélectionnez une arête du cube qui va dans la direction souhaitée. Si la force résultante pointe dans la direction opposée à celle requise, sélectionnez le bouton radio pour \"Reverse direction\".

<img alt="" src=images/Pic8.png  style="width:700px;">



## Analyse CalculiX 

Maintenant que toutes les régions maillées, le matériau et les conditions aux limites ont été définis, nous sommes prêts à analyser la déformation du bloc avec CalculiX. Activez l\'analyse en faisant un clic droit sur \"Activate analysis\", ouvrez la boîte de dialogue de CalculiX en double-cliquant sur l\'objet CalculiXccxTools et sélectionnez un répertoire pour les fichiers temporaires créés par FC et CCX. Écrivez le fichier d\'entrée CCX et vérifiez s\'il y a des messages d\'avertissement ou d\'erreur.

<img alt="" src=images/PIC9.png  style="width:700px;">

Ensuite, l\'analyse peut être lancée en appuyant sur le bouton RunCalculiX. Si tout se passe bien, la fenêtre de sortie CCX devrait afficher les messages suivants.

<img alt="" src=images/Pic10.png  style="width:700px;">



## Résultats CalculiX 

Une fois l\'analyse terminée, double-cliquez sur l\'objet \"CalculiX_static_results\" et sélectionnez l\'option \"Abs displacement\". Le déplacement maximal de \~ 0,08 mm apparaîtra dans la boîte de sortie correspondante. Comme le déplacement maximal est relativement faible par rapport aux dimensions du bloc (\<1% de la taille du bloc), les déplacements doivent être mis à l\'échelle. Cela peut être fait sous la rubrique \"Displacement\" en cochant le bouton radio \"Show\" et en mettant à l\'échelle le déplacement par un facteur de - disons - 20. Le déplacement maximum sera maintenant exagéré à environ 20% de la taille de la boîte. Après avoir fermé la fenêtre de dialogue, le maillage déformé peut être rendu à nouveau visible en mettant en surbrillance l\'objet Result_mesh et en appuyant sur la barre d\'espacement.

<img alt="" src=images/Figure_11_Deformed_Mesh.png  style="width:700px;">

Pour étudier la déformation du noyau, nous devons découper le bloc. Ceci peut être fait en créant un filtre de coupe. Pour activer cette fonctionnalité, nous devons d\'abord créer un \"pipeline de post-traitement\" en mettant en surbrillance l\'objet \"CalculiX_static_results\" et en choisissant \"Results → Post Pipeline from Result\" dans le menu. Ensuite, avec le pipeline sélectionné, créez un filtre Warp (Results → Warp filter), définissez Vector=Displacement et Value=20 pour mettre à l\'échelle le déplacement et Mode d\'affichage = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" pour afficher des contours de déplacement colorés. Appuyez sur Appliquer et OK. Comme étape finale, ajoutez un filtre d\'écrêtage (Results → Clip filter) et créez un plan avec une origine \[5.0,2.5,5.0\] et une normale \[0,1,0\], c\'est-à-dire au niveau d\'une face du noyau avec une normale dans la direction y. Cochez le bouton radio \"Cut Cells\" pour créer une surface plane. Comme précédemment, définissez Mode d\'affichage = \"Surface with Edges\", Champ de coloration = \"Displacement\", Vecteur = \"Magnitude\" pour afficher les contours de déplacement colorés. Appuyez sur Appliquer et OK. Enfin, faites en sorte que le filtre de distorsion soit invisible pour ne montrer que le bloc découpé.

<img alt="" src=images/Figure12_Deformed_Mesh_Clipped_View_(2).png  style="width:700px;">

D\'après le résultat, il est clair que le noyau reste largement indéformé et aide à résister à la déformation de la matrice souple (comparez l\'angle de cisaillement de la partie colorée en bleu à celui de la partie colorée en vert). Ce qui est également mis en évidence, c\'est que dans des conditions de cisaillement simple, les faces du bloc composite se déforment, ce qui implique que la condition de limite de glissement à la base du cube fournit une contrainte excessive.



## Travaux complémentaires 

Les défis suivants peuvent être intéressants à relever à titre d\'exercice supplémentaire :

1\) Corriger la contrainte excessive imposée par la condition de frontière glissante.

2\) Essayer de créer des conditions limites de contact entre le noyau et la matrice pour voir si une séparation se produit.

Le fichier FC pour ce tutoriel est joint ci-dessous comme point de départ.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=26517&start=20>

Amusez-vous bien!


{{FEM Tools navi

}} {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Shear of a Composite Block/fr
