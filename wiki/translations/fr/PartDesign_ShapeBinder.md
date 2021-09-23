---
- GuiCommand:/fr
   Name:PartDesign ShapeBinder
   Name/fr:PartDesign Forme liée
   MenuLocation:Conception de pièces → Créer une forme liée
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md), [PartDesign Clone](PartDesign_Clone/fr.md)
---

# PartDesign ShapeBinder/fr

## Description

Crée un datum **Forme Liée** à l\'intérieur du corps actif. Une Forme liée est un objet de référence lié à des arêtes ou des faces provenant d\'un autre corps. Elle peut également être utilisée pour relier une esquisse d\'un corps à un autre corps. L\'objet shape binder s\'affiche en jaune translucide dans la [vue 3D](3D_view/fr.md).

Des exemples d\'utilisation seraient de construire une boîte avec un couvercle dans deux corps différents ou de faire des trous alignés entre différents corps.

<img alt="" src=images/Shapebinder_tree.png ) ![](images/Shapebinder_flow.png  style="width:600px;"> 
*Deux formes de Body.Pad004 sont sélectionnées et leurs objets de référence (datum) sont désormais disponibles dans Body001.Sketch005 en tant que géométrie externe via Body001.ShapeBinder.*

## Utilisation

Usage général:

1.  [Activer le corps](PartDesign_Body/fr#Statut_actif.md), qui doit recevoir l\'objet Forme liée (shape binder).
2.  Appuyez sur le bouton **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [Créer une forme liée](PartDesign_ShapeBinder/fr.md)**.
3.  Appuyez sur le bouton **Objet** ou sur le bouton **Ajouter une géométrie**.
4.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet ou la géométrie à copier. *Objet* sélectionnera tout le corps; *Ajouter une géométrie* sélectionnera n\'importe quel élément (sommet, arête, face).
5.  Pour supprimer la géométrie sélectionnée, appuyez sur le bouton **Supprimer la géométrie** et sélectionnez la géométrie dans la [vue 3D](3D_view/fr.md). Pour annuler, appuyez à nouveau sur le bouton.
6.  Sinon, le corps à copier peut être sélectionné avant de lancer la commande \"Créer une forme liée\".
7.  Appuyez sur **OK**.

**Exemple**

:   L\'exemple utilise la fonctionnalité ShapeBinder pour créer un trou (avec ou sans filetage) à travers plusieurs corps. Normalement, la fonction Trou de l'atelier Part Design est limitée à un seul corps. L\'exemple utilise deux cubes qui se font face mais désalignés de manière arbitraire. Les trous sont créés avec des esquisses contenant un cercle pour chaque trou (le diamètre est ignoré par la fonction trou). Lorsque vous copiez l\'esquisse sur l\'autre cube, celle-ci se trouve à la même position dans le système de coordonnées du cube local. Sur l\'image, ceci est indiqué par le cercle blanc sur le cube arrière. Ce n\'est pas ce que nous voulons, car le trou situé à cette position ne serait pas aligné sur le trou du cube avant.





:   

    :   ![](images/ShapeBinderThroughHole.png )
    :   *Exemple de configuration pour montrer comment faire des trous à travers différents corps. Le cercle blanc montre que copier des esquisses ne suffit pas.*

Voici comment vous utilisez la fonctionnalité ShapeBinder pour y parvenir:

1.  Concevez un objet selon l\'image ci-dessus. Si vous utilisez les cubes de l\'[Atelier Part](Part_Workbench/fr.md), rappelez-vous que vous devez les placer dans un conteneur \"body\". Chacun dans un conteneur de corps unique, sinon les fonctions de l\'[Atelier PartDesign](PartDesign_Workbench/fr.md) ne fonctionneraient pas. Si vous les construisez à partir d\'esquisses, le système doit créer des conteneurs de corps par défaut.
2.  Sélectionnez l\'onglet PropertiesDialog/Data pour déplacer le deuxième cube afin qu\'il touche le premier cube grâce à un déplacement latéral.
3.  Sélectionnez l\'atelier PartDesign
4.  Créez une esquisse sur la face avant du premier cube et placez un cercle n\'importe où, puis fermez l\'esquisse.
5.  Sélectionnez l\'esquisse dans l\'arborescence et appuyez sur la touche de fonction [PartDesign Perçage](PartDesign_Hole/fr.md). Auparavant, assurez-vous que le premier corps est le corps actif (double-clic).
6.  Sélectionnez un trou de taille appropriée. L\'image ci-dessus avait également sélectionné un contre-alésage. Fermez la fonction [Perçage](PartDesign_Hole/fr.md).

    :   L\'image doit maintenant ressembler à celle ci-dessus. Lorsque vous masquez le premier cube (sélectionnez et appuyez sur espace), vous constatez que le trou n'atteint pas le deuxième cube. Ce ne sera pas le cas, même si vous sélectionnez \"A travers tout\" ou ou lorsque vous entrez une très grande valeur pour la distance dans la boîte de dialogue [PartDesign Perçage](PartDesign_Hole/fr.md). Le dialogue de trou est toujours limité à un seul corps.
    :   Voici où notre ShapeBinder entre en jeu.
7.  Sélectionnez d\'abord le cube arrière. C\'est la cible où le ShapeBinder sera ajouté. Il doit être activé en double-cliquant dessus.
8.  Dans l\'arborescence, sélectionnez l\'esquisse que nous avons utilisée pour le trou. Il est important de ne pas activer le premier corps.
9.  Sélectionnez la fonction shapeBinder.

    :   Un dialogue devrait s\'ouvrir. Dans la ligne \"Objet\", le nom de notre esquisse doit être visible. Si vous avez sélectionné la fonction sans sélectionner l\'esquisse, vous pouvez appuyer sur \"Objet\" puis sélectionner l\'esquisse dans la liste. Il est recommandé de le sélectionner d\'abord pour obtenir le bon choix, surtout si vous avez plusieurs skeches avec les noms générés automatiquement Sketch001, .. \"Ajouter une géométrie\" ne nous est pas utile, car nous voulons sélectionner l\'esquisse entière. \"AddGeometry\" n\'est utilisé que si seules les pièces doivent être sélectionnées.
10. Appuyez sur **OK** pour fermer la fonction d\'esquisse et vérifiez qu\'un nouvel élément a été ajouté à l\'arborescence du deuxième cube.

    :   Lorsque vous basculez la visibilité du ShapeBinder, celle-ci est affichée en jaune dans la [vue 3D](3D_view/fr.md). Cependant, sa position est incorrecte, tout comme le cercle blanc dans l\'image est en haut. Cela est dû au paramètre par défaut du paramètre Trace.
11. Dans le PropertyView de ShapeBinder sous l\'onglet Données, définissez le paramètre **Trace Support** sur true. La valeur par défaut était false.

    :   Avec **Trace Support**, le ShapeBinder n\'est pas affecté par les transformations locales du corps cible, par exemple nos déplacements. La forme reste exactement la même que celle de l'objet original. Essayez de déplacer l\'objet avant et vous pouvez voir que ShapeBinder suit toujours à la nouvelle position.
    :   Malheureusement, nous ne pouvons pas sélectionner ShapeBinder pour un [PartDesign Perçage](PartDesign_Hole/fr.md). Par conséquent, nous créons une esquisse locale et l'utilisons pour notre trou dans le deuxième cube.
12. Sélectionnez la face avant du cube arrière et créez une nouvelle esquisse (cliquez sur OK pour la suggestion dans la boîte de dialogue).
13. Rendre toute la géométrie invisible et le ShapeBinder visible. Vous pouvez maintenant utiliser la fonction de géométrie externe et sélectionner le cercle dans le classeur de formes. Nous devons centrer le point de ce cercle.
14. Crée un nouveau cercle et place-le au centre du cercle ShapeBinders. Le rayon n\'est pas important. La fonction [Perçage](PartDesign_Hole/fr.md) utilise uniquement les points centraux des cercles (remarque: les points simples sont ignorés par la fonction Perçage, nous devons utiliser des cercles)
15. Fermez l\'esquisse et cliquez sur [PartDesign Perçage](PartDesign_Hole/fr.md). Définissez la boîte de dialogue sur les mêmes valeurs que la mise en attente initiale et appuyez sur **OK**.

Terminé.

:   Maintenant, vous avez deux trous liés dans deux corps différents. Si vous modifiez la géométrie ou la position des trous, les deux trous s\'adapteront. Ce n\'est que lorsque vous ajouterez un nouveau trou que vous devez mettre à jour l\'esquisse dans le deuxième cube pour le deuxième trou.





:   Remarques
:   il existe un autre moyen de créer un ShapeBinder: lorsque le cube arrière est activé, cliquez sur la face avant du cube devant et créez une nouvelle esquisse. Une boîte de dialogue apparaît dans laquelle vous sélectionnez \"Dependent sketch\". Cela va réellement créer une forme liée. Vous pouvez voir le paramètre **Trace Support** dans la fenêtre de propriété. C\'est quelques clics de moins que notre procédure.
:   notez également que l\'utilisation de ShapeBinder avec Sketches ne représente qu\'un sous-ensemble de ses fonctionnalités. Il est également possible d\'utiliser des parties de la géométrie 3D, comme dans l\'exemple ci-dessus.

## Options

Double-cliquez sur l\'étiquette de la Référence liée à une forme dans la [vue en arborescence](Tree_view/fr.md) du modèle ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la référence** dans le menu contextuel pour éditer ses paramètres.

## Propriétés

-    {{PropertyData/fr|Label}}: nom donné à l\'objet, ce nom peut être changé à la convenance.

-    {{PropertyData/fr|Trace Support}}: en mettant cette option à true, le Shapebinder observe les emplacements relatifs des pièces et des corps. La valeur par défaut est false. Voir l\'exemple ci-dessus pour savoir comment cela est utilisé et fonctionne. {{Version/fr|0.18}}

## Limitations

-   La sélection multiple n\'est pas supportée. Les boutons Ajouter une géométrie et Supprimer une géométrie doivent être activés pour chaque sélection. Il y a une solution de contournement pour effectuer une sélection multiple : si vous sélectionnez tous les éléments désirés *avant* de créer la forme liée, ils apparaissent dans la liste initiale.
-   Une forme liée ne peut pas servir de fonction de base.
-   La géométrie sélectionnée sur un corps doit être contiguë.
-   Si le corps à copier est sélectionné avant de lancer la commande, ou si le bouton **Objet** est utilisé, il n\'est plus possible de sélectionner uniquement des éléments de géométrie spécifiques.
-   Le placement relatif du corps cible et du corps copié n\'est pas pris en compte. L\'élément lié à la forme adoptera les mêmes coordonnées internes que le corps copié. Depuis la version 0.18, il a une nouvelle propriété \"Support de tracé\", afin de changer ce comportement pour prendre en compte les emplacements relatifs.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/fr
