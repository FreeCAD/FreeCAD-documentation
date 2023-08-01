---
- GuiCommand:
   Name: PartDesign ShapeBinder
   Name/fr: PartDesign Forme liée
   MenuLocation: Part Design - Créer une forme liée
   Workbenches: [PartDesign](PartDesign_Workbench/fr.md)
   Version: 0.17
   SeeAlso: [PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md), [PartDesign Clone](PartDesign_Clone/fr.md)
---

# PartDesign ShapeBinder/fr

## Description

L\'outil **PartDesign Forme liée** crée une forme liante référençant la géométrie d\'un seul objet parent. Une Forme liée est utilisée à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md) pour référencer une géométrie extérieure au corps. L\'utilisation d\'une géométrie externe directement dans un corps n\'est pas autorisée et entraînera des erreurs hors champ.

Une Forme liée suivra le placement relatif de la géométrie référencée, ce qui est utile dans le contexte de la création d\'[assemblages](Assembly/fr.md), si sa propriété **Trace Support** est mise à {{True}}. Consultez l\'[Exemple](#Exemple.md) ci-dessous pour comprendre comment cela fonctionne.

La géométrie référencée peut être soit un objet unique (par exemple un [Part Cube](Part_Box/fr.md), un [PartDesign Corps](PartDesign_Body/fr.md), ou une [PartDesign Esquisse](PartDesign_NewSketch/fr.md) ou une [PartDesign Fonction](PartDesign_Feature/fr.md) à l\'intérieur d\'un corps), soit un ou plusieurs sous-éléments (faces, arêtes ou sommets) appartenant au même objet parent. Le choix de la géométrie à sélectionner dépend de l\'utilisation prévue de la Forme liée. Pour une opération booléenne, vous devrez sélectionner un solide. Pour une opération de protrusion, une face ou une esquisse peut être utilisée. Et pour la géométrie externe dans une esquisse, ou pour attacher une esquisse, toute combinaison de sous-éléments peut être appropriée. La géométrie référencée peut également appartenir au corps dans lequelle la Forme liée est imbriquée.

<img alt="" src=images/Shapebinder_flow.png  style="width:600px;"> 
*À partir de deux faces sélectionnées, une Forme liée est créée dans un corps encore vide. La géométrie de la Forme liée peut ensuite être utilisée comme géométrie externe dans une esquisse de ce corps.*



## Utilisation

1.  [Activer le corps](PartDesign_Body/fr#Statut_actif.md), la Forme liée doit être imbriquée dedans.
2.  Sélectionnez éventuellement un seul objet, ou un ou plusieurs sous-éléments appartenant au même objet parent. Les sous-éléments ne peuvent être sélectionnés que dans la [Vue 3D](3D_view/fr.md).
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [Créer une forme liée ](PartDesign_ShapeBinder/fr.md)**.
    -   Sélectionnez l\'option **Part Design → <img src="images/PartDesign_ShapeBinder.svg" width=16px> Créer une forme liée ** dans le menu.
4.  Le panneau de tâches **Paramètres de la forme liée** s\'ouvre.
5.  Sélectionnez éventuellement un objet, ce n\'est pas nécessaire si vous voulez sélectionner des sous-éléments :
    1.  Appuyez sur le bouton **Objet**.
    2.  Sélectionnez un objet dans la [Vue en arborescence](Tree_view/fr.md) ou la [Vue 3D](3D_view/fr.md).
    3.  Tous les sous-éléments précédemment sélectionnés seront supprimés.
    4.  Si un corps est sélectionné ici, il sera impossible de sélectionner des sous-éléments car ils appartiennent à un objet différent, à savoir le [Tip (fonction résultante)](PartDesign_Body/fr#Tip_.28fonction_r.C3.A9sultante.29.md) du corps.
6.  Vous pouvez sélectionner des sous-éléments :
    1.  Appuyez sur le bouton **Ajouter une géométrie**.
    2.  Sélectionnez un sous-élément dans la [Vue 3D](3D_view/fr.md).
    3.  Vous devez appuyer sur le bouton **Ajouter une géométrie** pour chaque sous-élément que vous souhaitez ajouter.
    4.  Seuls les sous-éléments appartenant au même objet parent peuvent être sélectionnés. Si nécessaire, utilisez le bouton **Objet** pour sélectionner un autre objet parent.
7.  En option, vous pouvez supprimer des sous-éléments :
    1.  Appuyez sur le bouton **Supprimer une géométrie**.
    2.  Sélectionnez un sous-élément dans la [Vue 3D](3D_view/fr.md).
    3.  Vous devez appuyer sur le bouton **Supprimer une géométrie** pour chaque sous-élément que vous souhaitez supprimer.
    4.  Appuyez sur le bouton **OK**.

## Options

Pour modifier un classeur de formes, double-cliquez dessus dans l\'arborescence, ou cliquez dessus avec le bouton droit de la souris et sélectionnez **Modifier la forme liée** dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md)



## Remarques

-   Une Forme liée peut être retirée du corps dans lequel elle est imbriquée et déposée sur le nœud de document <img alt="" src=images/Document.svg  style="width:16px;"> dans l\'arborescence. Une telle Forme liée non imbriquée peut être utilisée comme une [fonction de base](PartDesign_Body/fr#Base_Feature.md) pour un nouveau corps.
-   Une Forme liée créée à partir d\'une esquisse peut avoir une \"direction d\'outil\" opposée. Par exemple, une [Protrusion](PartDesign_Pad/fr.md) créée à partir de l\'esquisse peut s\'étendre dans la direction +Y, tandis qu\'une [Protrusion](PartDesign_Pad/fr.md), ayant les mêmes propriétés, créé à partir d\'une Forme liée s\'étend dans la direction -Y. L\'activation de la propriété (ou de la case à cocher) **Reversed** résoudra ce problème.



## PartDesign Sous forme liée vs. PartDesign Forme liée 

Voir [PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr#PartDesign_Sous_forme_li.C3.A9e_vs._PartDesign_Forme_li.C3.A9e.md).



## Propriétés

-    **Support|LinkSubListGlobal**: support pour la géométrie.

-    **Trace Support|Bool**: valeur par défaut est {{False}}. Lorsque {{True}}, la forme liée respecte les placements relatifs des pièces et des corps (en manipulant les valeurs de sa propriété cachée **Placement**).



## Exemple

Cet exemple utilise la fonction Forme liée pour réaliser un trou (avec ou sans filetage) à travers plusieurs corps. Normalement, la fonction Trou de l\'atelier Part Design est limitée à un seul corps. L\'exemple utilise deux cubes se faisant face mais désalignés de manière arbitraire. Les trous sont créés à l\'aide d\'esquisses contenant un cercle pour chaque trou (le diamètre est ignoré par la fonction de trou). Lorsque vous copiez l\'esquisse sur l\'autre cube, elle sera à la même position dans le système de coordonnées local du cube. Dans l\'image, cela est illustré par le cercle blanc sur le cube arrière. Ce n\'est pas ce que nous voulons, car le trou à cette position ne serait pas aligné avec le trou du cube avant.

![](images/ShapeBinderThroughHole.png ) 
*Exemple de montage pour montrer comment faire des trous à travers différents corps. Le cercle blanc montre qu'il ne suffit pas de copier les esquisses*

Voici comment utiliser la fonction Forme liée pour y parvenir :

1.  Préparez un montage comme dans l\'image ci-dessus. Si vous utilisez les cubes de l\'[atelier Part](Part_Workbench/fr.md), n\'oubliez pas que vous devez les placer dans un conteneur de corps. Chacun d\'entre eux doit être placé dans un seul conteneur de corps. Sinon, les fonctions de [PartDesign](PartDesign_Workbench/fr.md) ne fonctionneraient pas. Si vous les construisez à partir d\'esquisses, le système devrait créer des conteneurs de corps par défaut.
2.  Dans l\'[Éditeur de propriétés](Property_editor/fr.md), modifiez le placement du deuxième cube de sorte qu\'il touche le premier cube avec un déplacement latéral.
3.  Sélectionnez l\'atelier PartDesign.
4.  Créez une esquisse sur la face avant du premier cube, placez un cercle n\'importe où et fermez l\'esquisse.

Sélectionnez l\'esquisse dans la vue en arborescence et appuyez sur le bouton **<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**. Assurez-vous auparavant que le premier corps est le [corps actif](PartDesign_Body/fr#Statut_actif.md), (double-cliquez).

1.  Sélectionnez un trou de taille appropriée. Dans l\'image ci-dessus, le contre-trou a également été sélectionné. Fermez la fonction [Perçage](PartDesign_Hole/fr.md).

    :   L\'image devrait maintenant ressembler à celle ci-dessus. Lorsque vous masquez le premier cube (sélectionnez et appuyez sur espace), vous pouvez voir que le trou n\'atteint pas le deuxième cube. Il ne le fera pas, même si vous sélectionnez **A travers tout**, ou si vous entrez une distance vraiment importante dans le panneau de tâches de [Perçage](PartDesign_Hole/fr.md). Le trou est toujours limité à un seul corps.
    :   C\'est ici que notre Forme liée entre en jeu.
2.  Tout d\'abord, sélectionnez le cube arrière. C\'est la cible où la Forme liée sera ajoutée. Elle doit être [activée](PartDesign_Body/fr#Statut_actif.md) avant, donc assurez-vous qu\'elle a été double-cliquée.
3.  Dans l\'arborescence, sélectionnez l\'esquisse que nous avons utilisée pour le trou. Il est important de ne pas activer le premier corps.
4.  Sélectionnez la fonction Forme liée.

    :   Un panneau de tâches devrait s\'ouvrir. A la ligne **Objet**, le nom de notre esquisse devrait être visible. Si vous aviez sélectionné la fonction sans sélectionner l\'esquisse, vous pourriez appuyer sur **Objet** et sélectionner ensuite l\'esquisse dans la liste. Il est recommandé de la sélectionner en premier afin d\'obtenir la bonne, surtout si vous avez de nombreux esquisses avec des noms générés automatiquement tels que Sketch001 et suivants. La fonction **Ajouter une géométrie** n\'est pas utile pour nous, car nous voulons sélectionner toute l\'esquisse. L\'option **Ajouter une géométrie** est utilisée si seules certaines parties doivent être sélectionnées.
5.  Appuyez sur **OK** pour fermer le panneau des tâches et vérifier qu\'un nouvel élément a été ajouté à la vue en arborescence du second cube.

    :   Lorsque vous basculez la visibilité de la Forme liée, elle apparaît en jaune dans la [Vue 3D](3D_view/fr.md). Cependant, elle est sur la mauvaise position, tout comme le cercle blanc dans l\'image ci-dessus. Cela est dû au réglage par défaut du paramètre Trace.
6.  Dans la PropertyView de la Forme liée, dans l\'onglet Data, réglez le paramètre **Trace Support** sur true. La valeur par défaut était false.

    :   Avec **Trace Support** vrai, la Forme liée n\'est pas affectée par les transformations locales du corps cible, par exemple nos translations. La forme reste exactement à l\'endroit où se trouvait la forme originale de l\'objet frontal. Essayez de déplacer l\'objet frontal et vous pourrez constater que la Forme liée suit toujours la nouvelle position.
7.  Sélectionnez la Forme liée dans la vue en arborescence et appuyez sur le bouton **<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**. Si vous entrez les mêmes valeurs que pour le trou initial, vous remarquerez qu\'aucun trou n\'est créé dans le deuxième cube. Cela est dû au fait que, dans certains cas, la Forme liée a une \" direction d\'outil \" opposée à celle de l\'esquisse référencée. Pour résoudre ce problème, cochez la case Inverser. Appuyez sur **OK** pour terminer.
8.  Vous avez maintenant des trous liés dans deux corps différents. Si vous modifiez la position du cercle dans l\'esquisse, les deux trous s\'adapteront. Vous pouvez même ajouter de nouveaux cercles dans l\'esquisse pour créer d\'autres trous liés.





{{PartDesign_Tools_ navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/fr
