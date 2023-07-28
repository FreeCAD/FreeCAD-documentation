---
- GuiCommand:/fr
   Name:PartDesign_MultiTransform
   Name/fr:PartDesign Transformation multiple
   MenuLocation:Part Design → Appliquer une transformation → Transformation multiple
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Symétrie](PartDesign_Mirrored/fr.md), [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md), [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr.md), [PartDesign Mise à l'échelle](PartDesign_Scaled/fr.md)
---

# PartDesign MultiTransform/fr

## Description

L\'outil <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:24px;"> **PartDesign Transformation multiple** crée une transformation d\'une ou plusieurs fonctions. La transformation peut inclure plusieurs transformations où chaque transformation suivante est appliquée au résultat de la transformation précédente.

Les transformations disponibles sont : <img alt="lien=PartDesign_Mirrored/fr" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [Symétrie](PartDesign_Mirrored/fr.md), <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [Répétition linéaire](PartDesign_LinearPattern/fr.md), <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:16px;"> [Répétition circulaire](PartDesign_PolarPattern/fr.md) et <img alt="lien=PartDesign_Scaled/fr" src=images/PartDesign_Scaled.svg  style="width:16px;"> [Mise à l\'échelle](PartDesign_Scaled/fr.md). Les trois premières sont également disponibles sous forme d\'outils distincts.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Une transformation de trous créée à partir d'une seule fonction trou en appliquant une transformation linéaire à 2 occurrences, suivi d'une transformation circulaire à 8 occurrences.*



## Utilisation



### Créer

1.  [Activez](PartDesign_Body#Active_status.md) le bon corps.
2.  Sélectionnez une ou plusieurs fonctions dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Transformation multiple](PartDesign_MultiTransform/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une transformation → <img src="images/PartDesign_MultiTransform.svg" width=16px> Transformation multiple** du menu.
4.  S\'il n\'y a pas de corps actif et qu\'il y a deux corps ou plus dans le document, la boîte de dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il n\'y a qu\'un seul corps, il sera activé automatiquement.
5.  Si aucune fonction n\'a été sélectionnée, le [panneau des tâches](Task_panel/fr.md) **Ajouter une fonction** s\'ouvre : sélectionnez-en une ou plusieurs (en maintenant la touche **Ctrl**) dans la liste et appuyez sur le bouton **OK**.
6.  Le [panneau des tâches](Task_panel/fr.md) **Paramètres de la transformation multiple** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
7.  Appuyez sur le bouton **OK** pour terminer.



### Modifier

1.  Effectuez l\'une des opérations suivantes :
    -   Double-cliquez sur l\'objet MultiTransform dans la [vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet MultiTransform dans la [vue en arborescence](Tree_view/fr.md) et sélectionnez **Modifier la transformation multiple** dans le menu contextuel.
2.  Le [panneau des tâches](Task_panel/fr.md) des **Paramètres de la transformation multiple** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur le bouton **OK** pour terminer.



### Combiner des transformations existantes 

Il est possible de créer un objet MultiTransform à partir de transformations existantes [Symétrie](PartDesign_Mirrored/fr.md), [Répétition linéaire](PartDesign_LinearPattern/fr.md) et [Répétition circulaire](PartDesign_PolarPattern/fr.md)

1.  Vérifiez la propriété **Originals** des transformations existantes pour vous assurer qu\'elles ont été appliquées aux mêmes fonctions.
2.  Sélectionnez ces fonctions dans la [vue en arborescence](Tree_view/fr.md).
3.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Transformation multiple ](PartDesign_MultiTransform/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une transformation → <img src="images/PartDesign_MultiTransform.svg" width=16px> Transformation multiple** dans le menu.
4.  Le [panneau des tâches](Task_panel/fr.md) de **Paramètres de la transformation multiple** s\'ouvre.
5.  Appuyez sur le bouton {{button|OK}} en haut.
6.  Modifiez la propriété **Tranformations** de l\'objet MultiTransform créé :
    1.  Cliquez dans le champ.
    2.  Appuyez sur le bouton **...** qui apparaît.
    3.  La boîte de dialogue **Lien** s\'ouvre.
    4.  Maintenez la touche **Ctrl** enfoncée et sélectionnez les transformations existantes.
    5.  Appuyez sur le bouton **OK**.
7.  Vous pouvez [Modifier](#Modifier.md) l\'objet MultiTransform, voir ci-dessus.

## Options

-   Pour ajouter des fonctions :
    1.  Appuyez sur le bouton **Ajouter une fonction**.
    2.  Sélectionnez une fonction dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
    3.  Répétez l\'opération pour ajouter d\'autres fonctions.
-   Pour supprimer des fonctions :
    1.  Appuyez sur le bouton **Supprimer un fonction**.
    2.  Effectuez l\'une des opérations suivantes :
        -   Sélectionnez une fonction dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
        -   Sélectionnez une fonction dans la liste du haut et appuyez sur la touche **Suppr**.
        -   Cliquez avec le bouton droit de la souris sur une fonction dans la liste du haut et sélectionnez **Enlever** dans le menu contextuel.
    3.  Répétez l\'opération pour supprimer d\'autres fonctions.
    4.  S\'il y a plusieurs fonctions dans la transformation, leur ordre peut être important. Voir [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Organiser_les_fonctions.md).
-   Pour ajouter des transformations :
    1.  S\'il existe des transformations existantes : sélectionnez la transformation après laquelle la nouvelle transformation doit être ajoutée.
    2.  Souris droite sur la liste **Transformations**.
    3.  Sélectionnez l\'une des options suivantes dans le menu contextuel :
        -   
            **Ajouter une symmétrie**
            
            . Voir [PartDesign Symmétrie](PartDesign_Mirrored/fr.md).

        -   
            **Ajouter une répétition linéaire**
            
            . Voir [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md).

        -   
            **Ajouter une répétition circulaire**
            
            . Voir [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr.md).

        -   
            **Ajouter une mise à l'échelle**
            
            . Voir [PartDesign Mise à l\'échelle](PartDesign_Scaled/fr.md).
    4.  La transformation sélectionnée est ajoutée à la liste et les paramètres de la transformation sont affichés sous la liste.
    5.  Ajustez les paramètres en fonction de vos besoins.
    6.  Appuyez sur **OK** de la barre en bas.
    7.  Répétez l\'opération pour ajouter d\'autres transformations.
-   Pour modifier une transformation :
    1.  Cliquez à droite sur la transformation dans la liste **Transformations**.
    2.  Sélectionnez **Modifier** dans le menu contextuel.
    3.  Ajustez les paramètres à votre convenance.
    4.  Appuyez sur **OK** de la barre en bas.
-   Pour changer l\'ordre des transformations :
    1.  Cliquez à droite sur une transformation dans la liste **Transformations**.
    2.  Sélectionnez **Monter** ou **Descendre** dans le menu contextuel.
    3.  Si la case **Réactualiser la vue** est cochée, la vue sera mise à jour en temps réel.

## Limitations

Voir [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Limitations.md).



## Exemple

Vous pouvez utiliser cet outil pour créer une pièce entièrement paramétrique qui sera symétrique par rapport à deux axes à partir d\'une esquisse.

Il peut s\'agir d\'une grande plaque de support de 150x100x10mm pour un moteur avec des trous symétriques.

<img alt="" src=images/PartDesign_MultiTransform_Example2.png  style="width:400px;">

1.  Créez un <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [corps](PartDesign_Body/fr.md) et ajoutez une <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [esquisse](PartDesign_NewSketch/fr.md) sur l\'un de ses plans de base.
2.  Dans l\'esquisse, créez la géométrie pour un quadrant de la pièce (ici le quadrant supérieur droit).
    -   Notez que les contraintes ne doivent couvrir qu\'un quart de la pièce, par exemple, au lieu de la dimension complète de {{Value|150mm}}, entrez {{Value|150/2mm}} ou {{Value|75mm}}.
    -   Assurez-vous que l\'esquisse est fermée en ajoutant des lignes le long des axes vertical et horizontal.
3.  Extrudez la pièce avec une <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md).
4.  Sélectionnez <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> **Transformation multiple**.
5.  La boîte de dialogue des tâches s\'ouvre.
6.  La dernière fonction du corps est déjà sélectionnée. Puisque nous voulons effectuer une symétrie de cette fonction, nous pouvons ignorer les boutons **Ajouter une fonction** et **Supprimer une fonction**.
7.  Cliquez à droite dans le champ **Transformations** et sélectionnez **Ajouter une fonction de symétrie** dans le menu contextuel.
8.  Pour le **Plan**, sélectionnez **Axe d'esquisse vertical**.
9.  Si la case **Mise à jour de la vue** est cochée, vous devriez maintenant voir la pièce reflétée autour d\'un axe.
10. Sélectionnez à nouveau **Ajouter une fonction de symétrie** dans le menu contextuel du champ **Transformations**.
11. Maintenant, pour le **Plan**, sélectionnez **Axe d'esquisse horizontal**.
12. Appuyez sur le bouton **OK** pour terminer.
13. Pour supprimer les arêtes le long des axes de symétrie dans le résultat final, définissez la propriété **Refine** de la nouvelle fonction sur {{Value|true}} dans l\'[éditeur de propriétés](Property_editor/fr.md).

Pour vérifier que la pièce est entièrement paramétrique, ouvrez l\'esquisse initiale avec la pièce de quart et modifiez une dimension, par exemple le diamètre d\'un trou. Après avoir fermé l\'esquisse, les trois autres trous auront été modifiés en conséquence. Cela fonctionne également avec toutes les autres dimensions. Une esquisse modélisant la pièce complète avec une seule extrusion et sans miroir serait beaucoup plus complexe et toutes les modifications ultérieures seraient plus compliquées.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/fr
