# Toothbrush Head Stand/fr
 {{TutorialInfo/fr|Topic=Modélisation|Level=Débutant|Author=[EmmanuelG](User:EmmanuelG.md)|Time=1 heure|FCVersion=0.16 ou ultérieure|Files=[https://www.thingiverse.com/thing:2403310 Thingiverse 2403310]}}

## Un problème de la vie courante 

Les brosses à dents électriques viennent rarement avec une tête, tandis que dans une famille, vous verrez souvent plusieurs têtes utilisées avec un seul moteur. Beaucoup de personnes confrontées à un problème commun nous conduisent à une variété de solutions, comme vous pouvez le voir sur Thingiverse (200 à 800 projets sont liés à cela). Voici la première réponse et comment la concevoir.

Ce tutoriel vous guidera à travers les étapes nécessaires pour modéliser la partie montrée dans l\'image ci-dessous en utilisant les outils de base de l\'[atelier Part Design](PartDesign_Workbench/fr.md) (beaucoup d\'outils et de capacités ne sont pas couverts).

![](images/TBHS-model.png )

## Première idée: un plateau 

-   A partir de la page d\'accueil, sélectionnez ![](images/Workbench_PartDesign.svg‎‎ ) \"Part Design\" ou créez un nouveau document et sélectionnez l\'espace de travail \"Part Design\".

![](images/TBHS-0.png )

### Créer une esquisse 

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [**Nouvelle esquisse**](Sketcher_NewSketch/fr.md). Soit à partir du menu de tâches contextuelles à gauche, soit de la barre d\'outils ci-dessus ou du menu Part Design en haut.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

Une boîte de dialogue vous invite à choisir l\'orientation de l\'esquisse et à fournir un décalage (si on ne veut pas que le dessin soit placer à XOY=0 (ou XOZ ou YOZ)).

-   Nous allons sélectionner le plan XY comme indiqué dans l\'image ci-dessus (cette orientation correspond à la plaque de construction commune de la plupart des imprimantes 3D), puis cliquez sur **OK**.

<img alt="" src=images/TBHS-2.JPG  style="width:800px;">

Vous êtes maintenant face au plan XY vu d\'en haut, et avez accès aux outils de dessin.

Cliquez sur le bouton <img alt="Sketcher_CreateRectangle.svg" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [**Rectangle**](Sketcher_CreateRectangle/fr.md).

-   Cliquez pour placer un premier point.
-   Cliquez pour placer le coin opposé.
-   Appuyez sur **Echap** ou cliquez sur le bouton droit de la souris pour arrêter d\'utiliser l\'outil.

<img alt="" src=images/TBHS-3.JPG  style="width:800px;">

Vous avez maintenant un rectangle mobile de dimensions non spécifiées.

Cliquez sur une ligne du rectangle, vous avez maintenant accès aux outils de contrainte à droite de la barre d\'outils (en fonction de la taille de votre écran, vous devrez peut-être les faire glisser vers la gauche pour les voir tous)

-   Cliquez sur le bouton **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle'''](Sketcher_ConstrainDistance.md)**
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 80mm, cliquez sur **OK**.
-   Répétez avec l\'autre côté du rectangle, également 80 mm.

<img alt="" src=images/TBHS-4.JPG  style="width:800px;">

Maintenant vous avez un carré mobile de 80mm de coté

-   Cliquez sur le point en bas à gauche du carré.
-   Cliquez sur l\'origine du plan XY (à l\'intersection des deux lignes épaisses).
-   Cliquez sur le bouton <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coincident**](Sketcher_ConstrainCoincident/fr.md).

<img alt="" src=images/TBHS-5.JPG  style="width:800px;">

Vous avez maintenant un croquis totalement contraint, comme vous le dit le solveur sur la gauche et le changement de couleur (vert) dont un des sommets est confondu avec l\'origine des axes XOY et les cotés horizontaux et verticaux. C\'est une bonne pratique de toujours avoir un croquis totalement contraint.

Un croquis sous-contraint peut laisser place à des changements non désirés, si vous modifiez quelque chose plus tard. Au contraire, un croquis trop contraint n\'est pas bon non plus. Dans ce cas, le solveur vous avertit des contraintes redondantes et vous devez supprimer certaines d\'entre elles.

-   Pour quitter l\'esquisse, cliquez sur le bouton **"Fermer"** à gauche ou sur l\'icône <img alt="" src=images/_Sketcher_LeaveSketch.png  style="width:32px;"> dans la barre d\'outils, ou appuyez sur **ESC**, ou bouton droit de la souris (gauche pour gauchers).

<img alt="" src=images/TBHS-6.JPG  style="width:800px;">

Vous ne voyez maintenant que le carré et le menu contextuel de gauche vous montre plus d\'options qu\'avant.

### Créer un volume (pad) 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrique** parmi les vues standard, pour mieux voir ce qui va se passer.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 4mm et cliquez sur **OK**.

<img alt="" src=images/TBHS-7.JPG  style="width:800px;">

Votre carré est désormais un volume !

### Créer un nouveau dessin sur une face 

-   Sélectionnez la face supérieure

<img alt="" src=images/TBHS-8.JPG  style="width:800px;">

La couleur de la face change (seulement la face doit changer de couleur, pas tous le volume) et vous avez plus d\'options dans le menu contextuel

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse**. Comme une face a été sélectionnée, il ne vous demandera pas de choisir un plan.

<img alt="" src=images/TBHS-9.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Cercle**](Sketcher_CreateCircle/fr.md), cliquez pour placer le centre, déplacez le pointeur et cliquez pour définir le rayon.
-   Dessinez 4 cercles sur la face (de n\'importe quelle taille)
-   Appuyez sur **Echap** ou cliquez sur le bouton droit de la souris pour arrêter d\'utiliser l\'outil (cercle).

<img alt="" src=images/TBHS-10.JPG  style="width:800px;">

-   Sélectionnez les cercles (un par un en maintenant la touche Ctrl enfoncée)
-   Cliquez sur le bouton \"Rayon de la barre de contraintes et répopndre \"oui\" à la boite de dialogue demandant si les cercles doivent être égaux <img alt="" src=images/_Constraint_EqualLength.png  style="width:32px;"> [**Égalité**](Sketcher_ConstrainEqual/fr.md)

<img alt="" src=images/TBHS-11.JPG  style="width:800px;">

Maintenant les cercles ont le même rayons

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [**Géométrie externe**](Sketcher_External/fr.md).
-   Cliquez sur les quatre côtés du carré, les arêtes deviendront couleur magenta.

<img alt="" src=images/TBHS-12.JPG  style="width:800px;">

Ces lignes seront les références pour positionner les cercles

-   Utilisez la contrainte de longueur **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle'''](Sketcher_ConstrainDistance/fr.md)** pour les positionner à 20 mm des lignes.

<img alt="" src=images/TBHS-13.JPG  style="width:800px;">

-   Cliquez sur un cercle
-   Cliquez sur le bouton Contrainte **<img src=images/Constraint_Radius.png style="width:32px"> ['''radiale'''](Sketcher_ConstrainRadius/fr.md)** et donnez la valeur de 1,5 mm.

<img alt="" src=images/TBHS-14.JPG  style="width:800px;">

-   Pour quitter le sketch, cliquer \"Fermer\" <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> , ou presser **ESC** ou clic droit de la souris.

<img alt="" src=images/TBHS-15.JPG  style="width:800px;">

### Créer un volume 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrique** en vue standard, pour mieux voir ce qui se passe devant vos yeux ébahis.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 25mm et cliquez **OK**.

<img alt="" src=images/TBHS-16.JPG  style="width:800px;">

Vous avez la forme de base, juste une touche finale\....

### Arrondir les coins 

-   Enfoncer la touche Ctrl **CTRL** et cliquez sur les quatre arrêtes verticales .

N\'hésitez pas à vous aider en changeant le mode d\'affichage Barres tâches (en haut) onglet \"Affichage, ligne \"Style de représentation , Choisir \"Filaire

<img alt="_DrawStyleWireFrame.svg" src=images/_DrawStyleWireFrame.svg  style="width:32px;"> **Wireframe** et <img alt="_DrawStyleFlatLines.svg" src=images/_DrawStyleFlatLines.svg  style="width:32px;"> **Filaire et ombre**.

<img alt="" src=images/TBHS-17.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [**Congé**](PartDesign_Fillet/fr.md).
-   Mettez le rayon à 20mm.

<img alt="" src=images/TBHS-18.JPG  style="width:800px;">

Encore mieux!

### Rendre plus robuste 

Nous devons ajouter du matériaux à la base des cylindres pour les rendre moins cassants. En raison de l\'orientation de l\'impression, ces petites surfaces seront fragiles à la jonction avec la base.

Sélectionner les cercles à la bases des cylindres

<img alt="" src=images/TBHS-19.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [**Chanfrein**](PartDesign_Chamfer/fr.md).
-   Mettez la valeur à 2 mm.

<img alt="" src=images/TBHS-20.JPG  style="width:800px;">

### Chanfreiner les angles 

-   Sélectionnez la face inférieure de la base, additionner un chanfrein <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **chanfrein** de 0,5 mm (ça c\'est pour l\'esthétique).

La première couche de plastique est souvent écrasée un peu trop, ceci compensera cela et vous fera gagner du temps dans le nettoyage du modèle. Si la première couche est correcte, cela ne fera que l\'améliorer

<img alt="" src=images/TBHS-21.JPG  style="width:800px;">

-   Sélectionnez les angles de la face supérieure (Enfoncer la touche **CTRL**).

<img alt="" src=images/TBHS-23.JPG  style="width:800px;">

-   Additionnez un chanfrein de <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **chanfrein** 1mm. Juste pour l'esthétique.

<img alt="" src=images/TBHS-22.JPG  style="width:800px;">

Vous avez remarqué que nous avons changé plusieurs fois de mode de représentation pour tour à tour mieux voir les arêtes et le résultat.

Tadaam youp\' la boom !

## Exporter en .STL 

-   Dans la vue combiner à gauche, dans l\'arborescence, cliquez sur la dernière opération **"Chanfrein"**.

<img alt="" src=images/TBHS-24.JPG  style="width:800px;">

-   Maintenant sélectionnez \"Export\" dans la barre des tâche en haut à gauche et exporter le fichier au format .STL.
-   Il n\'y a plus qu\'a l\'imprimer sur une imprimante 3D :-)

-   N\'oubliez pas de l\'enregistrer en tant que fichier dessin aussi, si vous voulez l\'archiver sur votre PC !

## Inspiration

Le modèle ci-dessous est un bon exercice pour utiliser Freecad.

Il y a une quantité de possibilités , nous allons en utiliser une seconde qui sera meilleur

<img alt="" src=images/TBHS-v2.jpg  style="width:800px;">

Ne soyons pas étonnés d\'avoir de nouvelles idées Par exemple : avoir plus de place entre chaque brosse

Dans cette seconde version, nous allons utiliser d\'autres outils, par exemple \"Répétition linéaire\"

## Seconde idée : une bande annulaire 

-   Créez un nouveau document et sélectionnez ![](images/Workbench_PartDesign.svg‎‎ ) *Part Design* workbench.

### Créer un sketch 

-   Créer une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse** dans le plan XY.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

-   Dessinez un oblong <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Créer une rainure**](Sketcher_CreateSlot/fr.md)
    -   Cliquez pour placer le premier centre
    -   Bougez la souris pour donner de la longueur et un rayon
    -   Cliquez pour donner le second centre.

<img alt="" src=images/TBHS2-1.JPG  style="width:800px;">

Maintenant nous avons un oblong mobile et sans dimensions spécifiées

-   Cliquez sur une des lignes horizontales de l\'oblong
-   Cliquez sur le bouton **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle '''](Sketcher_ConstrainDistance/fr.md)**
-   Dans la boite de dialogue. donnez une dimension. Entrer 75 mm, cliquez sur **OK**.
    -   Pour un stand de trois tête, compter 25mm pour chaque, mais vous pouvez mettre plus

<img alt="" src=images/TBHS2-2.JPG  style="width:800px;">

Cliquez en un point de la ligne horizontale Cliquez en un point de l\'autre ligne horizontale Cliquez sur le bouton **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle '''](Sketcher_ConstrainDistance/fr.md)** Dans la boite de dialogue indiquer la longueur 29 mm, cliquez sur le bouton **OK**. <img alt="" src=images/TBHS2-3.JPG  style="width:800px;">

-   Dessinez un autre oblong <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Créer une rainure**](Sketcher_CreateSlot/fr.md) autour de la première rainure.

<img alt="" src=images/TBHS2-4.JPG  style="width:800px;">

-   Mettre le centre du second en coïncidence avec le premier en utilisant l\'outil <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coincident**](Sketcher_ConstrainCoincident/fr.md).

<img alt="" src=images/TBHS2-5.JPG  style="width:800px;">

-   Cliquez sur un extrémité horizontale du second oblong
-   Cliquez sur l\'extrémité horizontale la plus proche du premier
-   Cliquez sur le bouton \"longueur **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle '''](Sketcher_ConstrainDistance/fr.md)**
-   Dans la boite de dialogue donner la valeur. Entrez 3 mm, cliquez sur **OK**.

<img alt="" src=images/TBHS2-6.JPG  style="width:800px;">

-   Pour avoir un dessin entièrement contraint:
    -   Cliquez sur le point central le plus éloigné du second oblong
    -   Cliquez sur l\' origine du plan XY
    -   Cliquez sur le bouton <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coïncidence**](Sketcher_ConstrainCoincident/fr.md)

le dessin doit avoir passer au vert! <img alt="" src=images/TBHS2-7.JPG  style="width:800px;">

-   Pour quitter le sketcher, cliquez sur le bouton **Close** à gauche, ou sur l\'**<img src=images/Sketcher_LeaveSketch.png style="width:32px"> icône** de la barre d\'outils, ou **ESC** ou le bouton droit de la souris.

<img alt="" src=images/TBHS2-8.JPG  style="width:800px;">

### Créer un volume 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrique** de la barre d\'outils \"Vues, pour avoir un meilleur spectacle devant vos yeux émerveillés.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 30mm et cliquez sur **OK**.

<img alt="" src=images/TBHS2-9.JPG  style="width:800px;">

### Créer un dessin par dessus 

-   Sélectionnez la face supérieure (seulement la face, pas tout le volume)

<img alt="" src=images/TBHS2-10.JPG  style="width:800px;">

-   Créez une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse**. Comme la face est sélectionnée, il ne demandera pas de créer un nouveau plan

<img alt="" src=images/TBHS2-11.JPG  style="width:800px;">

-   Dessinez un hexagone <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [**Hexagone**](Sketcher_CreateHexagon/fr.md)
    -   Cliquez pour placer le centre
    -   Bougez la souris pour placer le rayon (attention de ne pas placer le rayon sur un des axes, le dessin peu parfois s\'effondrer sur son centre)
    -   Cliquez pour finir

<img alt="" src=images/TBHS2-12.JPG  style="width:800px;">

-   Cliquez sur un des coté de l\' hexagone, le plus prés de l\'horizontal
-   Cliquez sur le bouton <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> [**Contrainte horizontale**](Sketcher_ConstrainHorizontal/fr.md)

<img alt="" src=images/TBHS2-13.JPG  style="width:800px;">

-   Cliquez sur le centre de l\' hexagone
-   Cliquez sur la ligne horizontale du plan XY
-   Cliquez sur le bouton **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle'''](Sketcher_ConstrainDistance/fr.md)**
-   Dans la boite de dialogue donner une dimension. Entrer 15 mm, Cliquez **OK**.

<img alt="" src=images/TBHS2-14.JPG  style="width:800px;">

-   Cliquez sur le centre de l\' hexagone
-   Cliquez sur la vertical du plan XY
-   Cliquez sur le bouton **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle '''](Sketcher_ConstrainDistance/fr.md)**
-   Dans la boite de dialogue, donner une dimension. Entrez 10 mm. Cliquez sur **OK**.

<img alt="" src=images/TBHS2-15.JPG  style="width:800px;">

-   Cliquez sur le cercle bleu de l\' hexagone
-   Cliquez sur le bouton **<img src=images/Constraint_Radius.png style="width:32px"> ['''Rayon'''](Sketcher_ConstrainRadius/fr.md)**
-   Dans la boite de dialogue donner une valeur. Entrer 8mm, Cliquez sur **OK**.

<img alt="" src=images/TBHS2-16.JPG  style="width:800px;">

-   Quittez le sketcher comme précédemment en cliquant sur le ** <img src=images/Sketcher_LeaveSketch.png style="width:32px">** sur la barre d\'outils, ou pressez sur **ESC**.

<img alt="" src=images/TBHS2-17.JPG  style="width:800px;">

### Créer le trou 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrique** de la barre d\'outil \"Vues\", toujours pour une meilleur vision.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [**Cavité**](PartDesign_Pocket/fr.md).
-   Sélectionnez *au premier* sur le menu déroulant et cliquer sur le **OK**.

<img alt="" src=images/TBHS2-18.JPG  style="width:800px;"> Si vous sélectionnez \"à travers tout\", vous aurez un trou identique de chaque coté

### Répétition linéaire 

-   Dans l\'arborescence du tableau combiné à gauche, sélectionnez la dernière opération \"Pocket.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**Répétition linéaire**](PartDesign_LinearPattern/fr.md).
-   Donnez la longueur totale 55mm et 3 occurrences (la première compte il y en aura donc trois en tout) également répartie sur 55mm et cliquez **OK**.

<img alt="" src=images/TBHS2-19.JPG  style="width:800px;">

### Créer un sketch par dessus 

-   Sélectionnez la face inférieure

<img alt="" src=images/TBHS2-20.JPG  style="width:800px;">

-   Créez une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Nouvelle esquisse**. Comme la face est sélectionnée, il ne demandera pas de choisir un plan.

<img alt="" src=images/TBHS2-21.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Cercle**](Sketcher_CreateCircle/fr.md), cliquez pour placer le centre et bougez la souris pour obtenir un rayon.

<img alt="" src=images/TBHS2-22.JPG  style="width:800px;">

-   Cliquez sur le centre du cercle
-   Cliquez sur la ligne horizontale du plan XY
-   Cliquez sur le bouton **<img src=images/Constraint_Length.png style="width:32px"> ['''Contrainte dimensionnelle '''](Sketcher_ConstrainDistance/fr.md)**
-   Dans la boite de dialogue donnez une valeur. Entrez 15mm, et cliquez **OK**.

<img alt="" src=images/TBHS2-23.JPG  style="width:800px;">

-   Cliquez au centre du cercle
-   Cliquez sur la verticale du plan XY
-   Cliquez sur le bouton **<img src=images/Constraint_Length.png  style="width: 32px"> ['''Distance'''](Sketcher_ConstrainDistance/fr.md)**
-   Une boîte de dialogue vous invite à définir une dimension. Entrez 10mm, cliquez sur **OK**.

<img alt="" src=images/TBHS2-24.JPG  style="width:800px;">

-   Clquez sur le cercle
-   Cliquez sur le bouton **<img src=images/Constraint_Radius.png style="width:32px"> ['''Rayon'''](Sketcher_ConstrainRadius/fr.md)**
-   Dans la boite de dialogue donner un rayon. Entrer 3.5 mm, cliquer **OK**.

<img alt="" src=images/TBHS2-25.JPG  style="width:800px;">

-   Quittez le sketch en cliquant sur le bouton **<img src=images/Sketcher_LeaveSketch.png style="width:32px">** de la barre d\'outils, ou pressez sur **ESC**.

<img alt="" src=images/TBHS2-26.JPG  style="width:800px;">

### Créer une protrusion 

-   Cliquez sur le bouton <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrique** parmi les vues standard, pour mieux voir la vue.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Protrusion**.
-   Entrez 4 mm et cliquer **OK**.

<img alt="" src=images/TBHS2-27.JPG  style="width:800px;">

### Répétition linéaire 

-   Dans l\'arborescence à gauche, sélectionnez la dernière opération.
-   Cliquez sur le bouton <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**Répétition linéaire**](PartDesign_LinearPattern/fr.md)..
-   Entrez une valeur de 55mm et 3 occurrences et cliquez **OK**.

<img alt="" src=images/TBHS2-28.JPG  style="width:800px;">

### Draft

-   Sélectionnez le bord de chaque piliers ronds

<img alt="" src=images/TBHS2-29.JPG  style="width:800px;">

-   Cliquez sur le bouton <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [**Dépouille**](PartDesign_Draft/fr.md).
-   Mettez un angle à 40°.
-   Cliquez sur Plan neutre \"Neutral plane\" et sélectionnez la face sur laquelle le dessin sera créé.
-   Cochez \"Invert the draft direction\".

<img alt="" src=images/TBHS2-30.JPG  style="width:800px;">

Nous aurions pu utiliser l\'outil chanfrein pour obtenir quelque chose de similaire

Chanfrein = à gauche/Draft = à droite

<img alt="" src=images/TBHS2-30-chamfer.JPG  style="width:200px;"><img alt="" src=images/TBHS2-30-draft.JPG  style="width:200px;">

### Finitions

-   Enfoncez le bouton \"Ctrl **CTRL** sélectionnez les faces supérieures et inférieures.

<img alt="" src=images/TBHS2-31-bottom.JPG  style="width:200px;"><img alt="" src=images/TBHS2-31-top.JPG  style="width:200px;">

-   -   Ajoutez un <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Chanfrein** de 0,5 mm.

<img alt="" src=images/TBHS2-31.JPG  style="width:800px;">

Parfait !

## Exportation en format .STL 

-   Voir le premier exemple.

<img alt="" src=images/TBHS2-32.JPG  style="width:800px;">

-   Exportez sous un autre nom ou remplacer le premier s\'il vous convient mieux
-   N\'oubliez pas non plus d\'enregistrer ce nouveau plan en tant que dessin


{{Tutorials navi

}} {{PartDesign Tools navi}} {{Sketcher Tools navi}} 
