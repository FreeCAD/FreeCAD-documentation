---
 TutorialInfo:r
   Topic: Modélisation
   Level: Débutant
   Author: User:EmmanuelG
   Time: 1 heure
   FCVersion: 0.16 ou ultérieure
   Files: https://www.thingiverse.com/thing:2403310 Thingiverse 2403310
---

# Toothbrush Head Stand/fr







## Un problème de la vie courante 

Les brosses à dents électriques viennent rarement avec une tête, tandis que dans une famille, vous verrez souvent plusieurs têtes utilisées avec un seul moteur. Beaucoup de personnes confrontées à un problème commun nous conduisent à une variété de solutions, comme vous pouvez le voir sur Thingiverse (200 à 800 projets sont liés à cela). Voici la première réponse et comment la concevoir.

Ce tutoriel vous guidera à travers les étapes nécessaires pour modéliser la partie montrée dans l\'image ci-dessous en utilisant les outils de base de l\'[atelier Part Design](PartDesign_Workbench/fr.md) (beaucoup d\'outils et de capacités ne sont pas couverts).

![](images/TBHS-model.png )



## Première idée : un plateau 

-   A partir de la page d\'accueil, sélectionnez ![](images/Workbench_PartDesign.svg‎‎ ) \"Part Design\" ou créez un nouveau document et sélectionnez l\'atelier \"Part Design\".

![](images/TBHS-0.png )



### Créer une esquisse 

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [**Nouvelle esquisse**](Sketcher_NewSketch/fr.md). Soit à partir du menu de tâches contextuelles à gauche, soit de la barre d\'outils ci-dessus ou du menu Part Design en haut.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

Une boîte de dialogue vous invite à choisir l\'orientation de l\'esquisse et à fournir un décalage.

-   Nous allons choisir le plan XY comme indiqué dans l\'image ci-dessus (cette orientation correspond à la plaque de construction commune de la plupart des imprimantes 3D), puis cliquez sur OK.

<img alt="" src=images/TBHS-2.JPG  style="width:800px;">

Vous êtes maintenant face au plan XY vu d\'en haut, et avez accès aux outils de dessin.

-   Cliquez sur <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [**Rectangle**](Sketcher_CreateRectangle/fr.md).
-   Cliquez pour placer un premier point.
-   Cliquez pour placer le coin opposé.
-   Appuyez sur **Echap** ou cliquez sur le bouton droit de la souris pour arrêter d\'utiliser l\'outil.

<img alt="" src=images/TBHS-3.JPG  style="width:800px;">

Vous avez maintenant un rectangle mobile de dimensions non spécifiées.

-   Cliquez sur une ligne du rectangle, vous avez maintenant accès aux outils de contrainte à droite de la barre d\'outils (selon la taille de votre écran, vous devrez peut-être les faire glisser vers la gauche pour les voir tous).
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 80mm, cliquez sur OK.
-   Répétez l\'opération avec l\'autre côté du rectangle, également 80mm.

<img alt="" src=images/TBHS-4.JPG  style="width:800px;">

Maintenant vous avez un carré mobile.

-   Cliquez sur le point en bas à gauche du carré.
-   Cliquez sur l\'origine du plan XY (à l\'intersection des deux lignes épaisses).
-   Cliquez sur le bouton <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coincident**](Sketcher_ConstrainCoincident/fr.md).

<img alt="" src=images/TBHS-5.JPG  style="width:800px;">

Vous avez maintenant une esquisse totalement contrainte, comme vous l\'indique le solveur à gauche et le changement de couleur. C\'est une bonne pratique de toujours avoir une esquisse totalement contrainte.

Une esquisse sous-contrainte peut laisser la place à des changements non souhaités, si vous modifiez quelque chose par la suite.

À l\'inverse, une esquisse surcontrainte n\'est pas bonne non plus. Dans ce cas, le solveur vous avertit des contraintes redondantes et vous devez en supprimer certaines.

-   Pour quitter l\'esquisse, cliquez soit sur le bouton \"Fermer\" à gauche, soit sur l\'icône <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> dans la barre d\'outils, ou appuyez sur **Echap**.

<img alt="" src=images/TBHS-6.JPG  style="width:800px;">

Vous ne voyez plus que le carré, et le menu contextuel des tâches sur la gauche vous montre plus d\'options qu\'auparavant.



### Créer une protrusion 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrique** parmi les vues standard, pour mieux voir ce qui va se passer.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 4mm et cliquez sur **OK**.

<img alt="" src=images/TBHS-7.JPG  style="width:800px;">

Votre carré est désormais un volume !



### Créer une esquisse dessus 

-   Sélectionnez la face supérieure

<img alt="" src=images/TBHS-8.JPG  style="width:800px;">

La couleur de la face change (seulement la face doit changer de couleur, pas tous le volume) et vous avez plus d\'options dans le menu contextuel

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse**. Comme une face a été sélectionnée, il ne vous demandera pas de choisir un plan.

<img alt="" src=images/TBHS-9.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Cercle**](Sketcher_CreateCircle/fr.md), cliquez pour placer le centre, déplacez le pointeur et cliquez pour définir le rayon.
-   Dessinez 4 cercles sur la face (de n\'importe quelle taille)
-   Appuyez sur **Echap** ou cliquez sur le bouton droit de la souris pour arrêter d\'utiliser l\'outil (cercle).

<img alt="" src=images/TBHS-10.JPG  style="width:800px;">

-   Sélectionnez les cercles
-   Cliquez sur le bouton <img alt="" src=images/_Constraint_EqualLength.png  style="width:32px;"> [**Contrainte d\'égalité**](Sketcher_ConstrainEqual/fr.md)

<img alt="" src=images/TBHS-11.JPG  style="width:800px;">

Maintenant les cercles ont le même rayons

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [**Géométrie externe**](Sketcher_External/fr.md).
-   Cliquez sur les quatre côtés du carré, les arêtes deviendront couleur magenta.

<img alt="" src=images/TBHS-12.JPG  style="width:800px;">

Ces lignes seront les références pour positionner les cercles

-   Cliquez sur l\'outil **[<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle'''](Sketcher_ConstrainDistance/fr.md)**
-   Cliquez sur le centre d\'un cercle
-   Cliquez sur une ligne magenta du bord
-   Définissez 20mm (pour chaque cercle, vers les deux bords les plus proches)

<img alt="" src=images/TBHS-13.JPG  style="width:800px;">

-   Cliquez sur un cercle
-   Cliquez sur <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Contrainte rayon**](Sketcher_ConstrainRadius/fr.md) et mettez la valeur à 1,5 mm.

<img alt="" src=images/TBHS-14.JPG  style="width:800px;">

-   Pour quitter le sketch, cliquer \"Fermer\" <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> , ou presser **ESC** ou clic droit de la souris.

<img alt="" src=images/TBHS-15.JPG  style="width:800px;">



### Créer une protrusion 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrique** en vue standard, pour mieux voir ce qui se passe devant vos yeux ébahis.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 25mm et cliquez **OK**.

<img alt="" src=images/TBHS-16.JPG  style="width:800px;">

Vous avez la forme de base, il ne manque que les touches finales.



### Arrondir les coins 

-   En maintenant **CTRL**, cliquer sur le bord vertical de chaque coin pour en sélectionner les quatre.

N\'hésitez pas à vous aider en changeant le mode d\'affichage (juste à gauche de la Vue Axonométrique) entre <img alt="" src=images/DrawStyleWireFrame.svg  style="width:32px;"> **Filaire** et <img alt="" src=images/DrawStyleFlatLines.svg  style="width:32px;"> **Filaire et ombre**.

<img alt="" src=images/TBHS-17.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [**Congé**](PartDesign_Fillet/fr.md).
-   Mettez le rayon à 20mm.

<img alt="" src=images/TBHS-18.JPG  style="width:800px;">

C\'est mieux.



### Rendre plus robuste 

Nous devons ajouter de la matière à la base des cylindres pour qu'ils soient moins enclins à se casser. En raison de l'orientation de l'impression, ces petites surfaces seront fragiles à la jonction avec la base.

-   Sélectionnez les cercles à la base des cylindres.

<img alt="" src=images/TBHS-19.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [**Chanfrein**](PartDesign_Chamfer/fr.md).
-   Mettez la valeur à 2 mm.

<img alt="" src=images/TBHS-20.JPG  style="width:800px;">



### Chanfreiner les bords 

-   Sélectionnez la face sous la base, ajoutez un <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Chanfrein** de 0,5mm.

La première couche de plastique est souvent écrasée un peu trop, ceci compensera cela et vous fera gagner du temps dans le nettoyage du modèle. Si la première couche est correcte, cela ne fera que l\'améliorer

<img alt="" src=images/TBHS-21.JPG  style="width:800px;">

-   Sélectionnez les angles de la face supérieure (Enfoncer la touche **CTRL**).

<img alt="" src=images/TBHS-23.JPG  style="width:800px;">

-   Ajoutez un dernier <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **chanfrein** de 1mm. Juste pour l'esthétique.

<img alt="" src=images/TBHS-22.JPG  style="width:800px;">

Et voilà!



## Exporter en .STL 

-   Dans la vue combinée de gauche, sélectionnez la vue arborescente au lieu du menu contextuel des tâches, cliquez sur la dernière caractéristique (le chanfrein).

<img alt="" src=images/TBHS-24.JPG  style="width:800px;">

-   Maintenant vous pouvez sélectionner \"Exporter\...\" dans le menu Fichier en haut à gauche, et sélectionner le format de fichier .STL.
-   Imprimez-le simplement :-)

## Inspiration

Le modèle ci-dessus constitue un bon point de départ pour utiliser FreeCAD, mais comme un support de tête de brosse à dents, il a ses défauts : à cause de l\'orientation de l\'impression et de la petite surface, les bâtons sont susceptibles de se casser.

Inspirés par la variété des solutions proposées par d\'autres personnes, nous allons réaliser cette deuxième version qui sera bien meilleure.

<img alt="" src=images/TBHS-v2.jpg  style="width:800px;">

Ne vous inquiétez pas, il est souvent nécessaire de passer par plusieurs révisions pour une idée (par exemple : une fois le prototype de la photo utilisé, nous avons ajouté plus d\'espace entre les têtes pour qu\'elles ne se touchent pas).

Dans cette deuxième partie, vous apprendrez également à utiliser d\'autres outils, comme la puissante *Répétition linéaire*.



## Deuxième idée : un groupe 

-   Créez un nouveau document et sélectionnez l\'atelier ![](images/Workbench_PartDesign.svg‎‎ ) *Part Design*.



### Créer une esquisse 

-   Créez une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse** dans le plan XY.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

-   Dessinez un oblong <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Contour oblong**](Sketcher_CreateSlot/fr.md)
    -   Cliquez pour placer le premier centre
    -   Bougez la souris pour donner de la longueur et un rayon
    -   Cliquez pour donner le second centre.

<img alt="" src=images/TBHS2-1.JPG  style="width:800px;">

Maintenant nous avons un contour oblong mobile et sans dimensions spécifiées

-   Cliquez sur l\'une des lignes horizontales du contour oblong
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 75mm, cliquez sur OK.
    -   Pour un support à 3 têtes, comptez 25mm pour chacune, si vous en voulez plus

<img alt="" src=images/TBHS2-2.JPG  style="width:800px;">

-   Cliquez sur un point de la ligne horizontale
-   Cliquez sur un point de l\'autre ligne horizontale
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 29mm, cliquez sur OK.

<img alt="" src=images/TBHS2-3.JPG  style="width:800px;">

-   Dessinez un <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Contour oblong**](Sketcher_CreateSlot/fr.md) autour du premier emplacement.

<img alt="" src=images/TBHS2-4.JPG  style="width:800px;">

-   Faites coïncider les centres du deuxième emplacement avec les centres du premier emplacement avec <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Contrainte de coïncidence**](Sketcher_ConstrainCoincident/fr.md).

<img alt="" src=images/TBHS2-5.JPG  style="width:800px;">

-   Cliquez sur un point de la ligne horizontale du premier emplacement.
-   Cliquez sur un point de la ligne horizontale la plus proche du deuxième emplacement.
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 3mm, cliquez sur OK.

<img alt="" src=images/TBHS2-6.JPG  style="width:800px;">

-   Pour rendre l\'esquisse entièrement contrainte
    -   Cliquez sur le point inférieur gauche de le deuxième contour oblong
    -   Cliquez sur l\'origine du plan XY
    -   Cliquez sur <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Contrainte de coïncidence**](Sketcher_ConstrainCoincident/fr.md)

<img alt="" src=images/TBHS2-7.JPG  style="width:800px;">

-   Pour quitter l\'esquisse, cliquez soit sur le bouton \"Fermer\" à gauche, soit sur l\'icône <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> dans la barre d\'outils, ou appuyez sur **Echap**.

<img alt="" src=images/TBHS2-8.JPG  style="width:800px;">



### Créer une protrusion 

-   Cliquez sur <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrique** parmi les vues standards, pour mieux voir ce qui va se passer.
-   Cliquez sur <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 30mm et cliquez sur OK.

<img alt="" src=images/TBHS2-9.JPG  style="width:800px;">



### Créer une esquisse dessus 

-   Sélectionnez la face supérieure

<img alt="" src=images/TBHS2-10.JPG  style="width:800px;">

-   Créez une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse**. Comme une face a été sélectionnée, il ne vous sera pas demandé de choisir un plan.

<img alt="" src=images/TBHS2-11.JPG  style="width:800px;">

-   Dessinez un <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [**Hexagone**](Sketcher_CreateHexagon/fr.md)
    -   Cliquez pour placer le centre
    -   Déplacez pour définir le rayon
    -   Cliquez pour définir

<img alt="" src=images/TBHS2-12.JPG  style="width:800px;">

-   Cliquez sur un des coté de l\' hexagone, le plus prés de l\'horizontal
-   Cliquez sur le bouton <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> [**Contrainte horizontale**](Sketcher_ConstrainHorizontal/fr.md)

<img alt="" src=images/TBHS2-13.JPG  style="width:800px;">

-   Cliquez sur le centre de l\'hexagone
-   Cliquez sur la ligne horizontale du plan XY
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 15 mm, cliquez sur OK.

<img alt="" src=images/TBHS2-14.JPG  style="width:800px;">

-   Cliquez sur le centre de l\' hexagone
-   Cliquez sur la vertical du plan XY
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 10 mm, cliquez sur OK.

<img alt="" src=images/TBHS2-15.JPG  style="width:800px;">

-   Cliquez sur le cercle bleu de l\'hexagone
-   Cliquez sur <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Contrainte rayon**](Sketcher_ConstrainRadius/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 8mm, cliquez sur OK.

<img alt="" src=images/TBHS2-16.JPG  style="width:800px;">

-   Pour quitter l\'esquisse, cliquez soit sur le bouton \"Fermer\" à gauche, soit sur l\'icône <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> dans la barre d\'outils, ou appuyez sur **Echap**.

<img alt="" src=images/TBHS2-17.JPG  style="width:800px;">



### Créer un trou 

-   Cliquez sur <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrique** parmi les vues standards, pour mieux voir ce qui va se passer.
-   Cliquez sur <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [**Cavité**](PartDesign_Pocket/fr.md).
-   Sélectionnez *au premier* dans le menu déroulant et cliquez sur OK.

<img alt="" src=images/TBHS2-18.JPG  style="width:800px;">



### Répétition linéaire 

-   Dans la vue combinée de gauche, sélectionnez la vue arborescente au lieu du menu contextuel des tâches, cliquez sur la fonction pocket.
-   Cliquez sur <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**Répétition linéaire**](PartDesign_LinearPattern/fr.md).
-   Définissez la longueur à 55mm et les occurrences à 3, puis cliquez sur OK.

<img alt="" src=images/TBHS2-19.JPG  style="width:800px;">



### Créer une esquisse dessus 

-   Sélectionner la face interne

<img alt="" src=images/TBHS2-20.JPG  style="width:800px;">

-   Créez une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse**. Comme une face a été sélectionnée, il ne vous sera pas demandé de choisir un plan.

<img alt="" src=images/TBHS2-21.JPG  style="width:800px;">

-   Cliquez sur <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Cercle**](Sketcher_CreateCircle/fr.md), cliquez pour placer le centre, déplacez le pointeur et cliquez pour définir le rayon.

<img alt="" src=images/TBHS2-22.JPG  style="width:800px;">

-   Cliquez sur le centre du cercle
-   Cliquez sur la ligne horizontale du plan XY
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 15mm, cliquez sur OK.

<img alt="" src=images/TBHS2-23.JPG  style="width:800px;">

-   Cliquez sur le centre du cercle
-   Cliquez sur la ligne horizontale du plan XY
-   Cliquez sur <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Contrainte dimensionnelle**](Sketcher_ConstrainDistance/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 10mm, cliquez sur OK.

<img alt="" src=images/TBHS2-24.JPG  style="width:800px;">

-   Cliquez sur le centre du cercle
-   Cliquez sur <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Contrainte rayon**](Sketcher_ConstrainRadius/fr.md)
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 3.5mm, cliquez sur OK.

<img alt="" src=images/TBHS2-25.JPG  style="width:800px;">

-   Pour quitter l\'esquisse, cliquez soit sur le bouton \"Fermer\" à gauche, soit sur l\'icône <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> dans la barre d\'outils, ou appuyez sur **Echap**.

<img alt="" src=images/TBHS2-26.JPG  style="width:800px;">



### Créer une protrusion 

-   Cliquez sur <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrique** parmi les vues standards, pour mieux voir ce qui va se passer.
-   Cliquez sur <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 4mm et cliquez sur OK.

<img alt="" src=images/TBHS2-27.JPG  style="width:800px;">



### Répétition linéaire 

-   Dans la vue combinée de gauche, sélectionnez la vue arborescente au lieu du menu contextuel des tâches, cliquez sur la fonction pad.
-   Cliquez sur <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**Répétition linéaire**](PartDesign_LinearPattern/fr.md).
-   Définissez la longueur à 55mm et les occurrences à 3, puis cliquez sur OK.

<img alt="" src=images/TBHS2-28.JPG  style="width:800px;">



### Dépouille

-   Sélectionnez le côté de chaque protrusion arrondie

<img alt="" src=images/TBHS2-29.JPG  style="width:800px;">

-   Cliquez sur <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [**Dépouille**](PartDesign_Draft/fr.md).
-   Réglez l\'angle de dépouille à 40°.
-   Cliquez sur \"Plan neutre\" et sélectionnez la face sur laquelle l\'esquisse est dessinée.
-   Cochez \"Inverser le sens de la dépouille\".

<img alt="" src=images/TBHS2-30.JPG  style="width:800px;">

Nous aurions pu utiliser un chanfrein pour faire quelque chose de similaire, mais la dépouille est plus appropriée dans ce cas.

Chanfrein = gauche / Ébauche = droite

<img alt="" src=images/TBHS2-30-chamfer.JPG  style="width:200px;"><img alt="" src=images/TBHS2-30-draft.JPG  style="width:200px;">



### Finitions

-   En maintenant **CTRL**, vous sélectionnez les faces inférieure et supérieure.

<img alt="" src=images/TBHS2-31-bottom.JPG  style="width:200px;"><img alt="" src=images/TBHS2-31-top.JPG  style="width:200px;">

-   -   Ajoutez un <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Chanfrein** de 0,5mm.

<img alt="" src=images/TBHS2-31.JPG  style="width:800px;">

Parfait !



## Exporter en .STL 

-   Dans la vue combinée de gauche, sélectionnez la vue arborescente au lieu du menu contextuel des tâches, cliquez sur la dernière caractéristique (le chanfrein).

<img alt="" src=images/TBHS2-32.JPG  style="width:800px;">

-   Vous pouvez maintenant sélectionner \"Exporter\...\" dans le menu Fichier en haut à gauche, et choisir le format de fichier .STL.
-   Imprimez-la à la place de la première version ou pour la remplacer si elle finit par se casser ;-)


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Toothbrush Head Stand/fr
