# <img alt="Icône de l\'atelier FrameForge" src=images/FrameForge.svg  style="width:64px;"> FrameForge Workbench/fr




## Introduction

FrameForge est dédié à la création de cadres et de poutres, et à l\'application d\'opérations (coupes d\'onglets, coupes de finition) sur ces profils.

Le tutoriel ci-dessous est également disponible sur [GitHub](https://github.com/lukh/frameforge/blob/main/docs/tutorial.md).



## Tutoriel



### Créer le cadre 

Les poutres sont attachées aux arêtes (d\'une esquisse par exemple) ou aux lignes paramétriques. Pour commencer, nous allons créer un cadre simple.

1.  Dans un nouveau fichier, passez à l\'atelier FrameForge.
2.  Créez une esquisse et spécifiez l\'orientation XY.
    <img alt="" src=images/FrameForge_00-create-sketch.png  style="width:500px;">

    <img alt="" src=images/FrameForge_01-select-orientation.png  style="width:200px;">
3.  Dessinez un simple carré. Ce sera notre cadre.
    <img alt="" src=images/FrameForge_02-create-frame-skeleton.png  style="width:300px;">
4.  Fermer le mode d\'édition de l\'esquisse.



### Créer le profil 

1.  Lancez l\'outil Create Profile.
    <img alt="" src=images/FrameForge_10-profiles.png  style="width:300px;">

    <img alt="" src=images/FrameForge_10-profiles-task.png  style="width:300px;">

    <img alt="" src=images/FrameForge_10-profiles-task-2.png  style="width:300px;">
2.  Sélectionnez un profil dans les listes (matériau/famille/taille). Vous pouvez modifier la taille juste en dessous de la famille, l\'outil dispose d\'un grand nombre de profils prédéfinis, vous pouvez également modifier les paramètres.
    <img alt="" src=images/FrameForge_11-profiles-family.png  style="width:300px;">
3.  Dans la vue 3D, sélectionnez les arêtes auxquelles appliquer le profil.
    <img alt="" src=images/FrameForge_13-edge-selection.png  style="width:500px;">
4.  Appuyez sur **OK** dans le panneau des tâches. Vous avez maintenant quatre profils et votre premier cadre.
    <img alt="" src=images/FrameForge_14-profiles-done.png  style="width:500px;">

    <img alt="" src=images/FrameForge_14-zoom-on-profiles.png  style="width:300px;">



### Vers la 3D 

Nous pouvons construire des formes plus complexes, et il y a plusieurs façons de le faire.



#### Plus d\'esquisses (partie 1) 

Nous pouvons ajouter d\'autres esquisses à notre projet :

1.  Créez une nouvelle esquisse.
2.  Sélectionnez la même orientation que précédemment (XY).
3.  Dessinez un carré de la même taille et du même emplacement que précédemment.
4.  Modifiez la position de l\'esquisse pour la placer 400 mm au-dessus de la première.
    <img alt="" src=images/FrameForge_20-sketch-base-placement.png  style="width:300px;">

    <img alt="" src=images/FrameForge_20-sketch-base-placement-2.png  style="width:300px;">
5.  Vous pouvez maintenant utiliser à nouveau l\'outil Create Profile pour créer un autre cadre carré.
    <img alt="" src=images/FrameForge_21-stacked-frames.png  style="width:400px;">



#### Ligne paramétrique 

Vous pouvez créer des lignes paramétriques en joignant deux sommets (points). Ces lignes peuvent également être utilisées pour les profils.

1.  Pour voir les esquisses, masquez temporairement les objets du profil avec la **Barre d'espace**.
    <img alt="" src=images/FrameForge_22-hide-profiles.png  style="width:300px;">
2.  Sélectionnez deux sommets.
    ![](images/FrameForge_23-select-vertexes.png )
3.  Créez une ligne paramétrique.
    <img alt="" src=images/FrameForge_24-create-parametric-line.png  style="width:300px;">

    <img alt="" src=images/FrameForge_25-parametric-line.png  style="width:300px;">
4.  Répétez l\'opération pour les trois autres pieds du cadre.
5.  Utilisez à nouveau l\'outil Create Profile pour attacher des profils aux 4 lignes.
    1.  Lancez l\'outil Create Profile.
    2.  Sélectionnez le profil que vous souhaitez.
    3.  Sélectionnez les 4 lignes paramétriques.
    4.  Appuyer sur **OK**.

    <img alt="" src=images/FrameForge_26-cube-done.png  style="width:400px;">



#### Plus d\'esquisses (partie 2) 

Il existe une autre façon d\'ajouter des esquisses, qui permet de faire des choses plus compliquées.

Vous souhaitez parfois ajouter une esquisse à un endroit spécifique et la lier à une autre esquisse. Ainsi, lorsque vous modifiez la première esquisse, la seconde suit. Cela n\'est pas possible avec la position/placement de base, qui est une position absolue, vous devez \"mapper\" la deuxième esquisse à la première.

1.  Créez une nouvelle esquisse et réglez son orientation sur YZ.
    Pour référence, j\'ai ajouté un cercle à l\'esquisse afin que vous puissiez voir où elle se trouve.

    <img alt="" src=images/FrameForge_30-mapmode-sketch.png  style="width:300px;">
2.  Cliquez sur la propriété Map Mode :
    <img alt="" src=images/FrameForge_31-mapmode.png  style="width:300px;">

    <img alt="" src=images/FrameForge_32-mapmode-dialog.png  style="width:300px;">
3.  Vous pouvez changer le mode de carte, sélectionner les faces, les sommets et les arêtes. Ici, notre esquisse de cercle a été réalignée. Il existe de nombreuses options.
    <img alt="" src=images/FrameForge_33-mapmode.png  style="width:800px;">
4.  Vous pouvez ensuite modifier l\'esquisse et créer d\'autres lignes et cadres.



### Les biseaux et les angles 

Comme vous pouvez le constater, les jonctions ne sont pas encore bonnes. Les profils sont centrés sur le cadre et s\'arrêtent aux extrémités des arêtes.

Nous allons réaliser des angles et des biseaux. Il existe deux méthodes pour cela.



### Via la propriété Bevels 

=

C\'est l\'option préférée pour les cadres simples.

1.  Cachons tout sauf le premier cadre que nous avons créé.
    <img alt="" src=images/FrameForge_40-show-first-frame.png  style="width:500px;">
2.  Sélectionnez l\'un des profils et, dans l\'éditeur de propriétés, recherchez Bevel Start/End Cut1/Cut2.
    <img alt="" src=images/FrameForge_41-bevels.png  style="width:300px;">
3.  Il y a 4 entrées (Start/End Cut1/Cut2). Elles vous permettent de créer des biseaux sur les deux axes, au début ou à la fin du profil. Les angles négatifs fonctionnent et doivent être utilisés pour compenser les directions.
4.  Vous pouvez modifier les propriétés de plusieurs profils en même temps.
    <img alt="" src=images/FrameForge_42-batchs-bevels.png  style="width:700px;">



#### Via l\'outil Create Miter Ends 

1.  Voyons l\'autre cadre de base.
    <img alt="" src=images/FrameForge_50-base-config.png  style="width:500px;">
2.  Il faut d\'abord ajouter des décalages aux profils existants. Les décalages augmentent les dimensions des arêtes. Vous pouvez modifier les profils un par un ou les modifier tous en même temps.
    <img alt="" src=images/FrameForge_51-add-offset.png  style="width:500px;">
3.  Désélectionnez tous les objets, puis sélectionnez deux profils qui se touchent. Vous devez sélectionner des faces dans la vue 3D, et non des objets dans l\'arborescence.
    <img alt="" src=images/FrameForge_52-select-touching-profiles.png  style="width:300px;">
4.  Cliquez sur l\'outil Create Miter Ends pour créer deux profils coupés.
    <img alt="" src=images/FrameForge_53-create-miter-end.png  style="width:300px;">

    <img alt="" src=images/FrameForge_54-miter-end.png  style="width:300px;">
5.  Répétez l\'opération pour les autres coins du deuxième cadre.



#### Via l\'outil Trim Profile 

1.  Lorsque tous les profils sont à nouveau visibles, vous pouvez voir que les profils verticaux ne sont pas coupés comme ils devraient l\'être.
    <img alt="" src=images/FrameForge_60-startwith.png  style="width:300px;">

    <img alt="" src=images/FrameForge_61-bad-joint.png  style="width:300px;">
2.  Lancez l\'outil Trim Profile.
    <img alt="" src=images/FrameForge_62-endtrim.png  style="width:300px;">

    <img alt="" src=images/FrameForge_62-endtrim-task.png  style="width:300px;">
3.  Sélectionnez d\'abord le profil vertical, puis ajoutez-le en tant qu\'objet ajusté à l\'aide du bouton **<img src="images/List-add.svg" width=16px>**.
    <img alt="" src=images/FrameForge_63-select-trimmed-body-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_63-select-trimmed-body-2.png  style="width:400px;">
4.  Sélectionnez les limites d\'ajustage avec lesquelles vous souhaitez couper. Ici, j\'ai fait pivoter la vue pour sélectionner deux faces inférieures.
    <img alt="" src=images/FrameForge_64-select-trimming-boundaries-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_64-select-trimming-boundaries-2.png  style="width:400px;">
5.  Vous pouvez changer le type de coupe : droite ou suivant l\'autre profil.
    <img alt="" src=images/FrameForge_64-select-cuttype-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_64-select-cuttype-2.png  style="width:400px;">
6.  Vous pouvez également ajouter des faces pour découper l\'autre côté du profil.



### Organiser les objets 

C\'est là que le bât blesse. Je trouve l\'arborescence désordonnée. Vraiment désordonné.



#### Conteneur de Part 

J\'utilise souvent les conteneurs de Part pour regrouper des profils, des esquisses, etc.

<img alt="" src=images/FrameForge_70-part-container.png  style="width:300px;">

<img alt="" src=images/FrameForge_71-part-container.png  style="width:300px;">

Vous ne devez faire glisser qu\'un seul profil à la fois dans le conteneur. Je ne sais pas pourquoi, mais FreeCAD n\'accepte pas un glissement de groupe. Parfois, les pièces et les profils sortent du conteneur de Part.

#### Fusion

Vous pouvez fusionner des profils. Il permet de regrouper des objets.

<img alt="" src=images/FrameForge_72-fusion.png  style="width:300px;">

<img alt="" src=images/FrameForge_72-fusion-done.png  style="width:300px;">



### Utiliser des profils dans PartDesign 

1.  Pour utiliser ces profils dans PartDesign, vous devez créer une fusion puis un corps.
    <img alt="" src=images/FrameForge_80-body.png  style="width:300px;">
2.  Glissez et déposez la fusion sur le corps.
    <img alt="" src=images/FrameForge_81-basefeature.png  style="width:300px;">
3.  Vous disposez à présent d\'un corps PartDesign standard et vous pouvez utiliser PartDesign pour faire ce que vous voulez. Vous pouvez par exemple créer des trous.
    <img alt="" src=images/FrameForge_82-making-holes.png  style="width:400px;">

    <img alt="" src=images/FrameForge_83-holes-made.png  style="width:400px;">



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > FrameForge Workbench/fr
