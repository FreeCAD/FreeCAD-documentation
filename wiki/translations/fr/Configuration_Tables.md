---
 TutorialInfo:
   Topic: Utilisation de tableaux de configuration
   Level: Débutant
   Time: 30 minutes
   Author: Gbroques
   FCVersion: 0.20
   Files: https://forum.freecad.org/download/file.php?id=270593 ConfigurationTableExample.FCStd
---

# Configuration Tables/fr







## Introduction

Avec la sortie de [FreeCAD V0.20](Release_notes_0.20/fr#Atelier_Spreadsheet.md), deux nouvelles fonctions puissantes ont été introduites : *[Liens](Std_LinkMake/fr.md) variants* et *[Configuration Tables](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183)*. Les tables de configuration sont un type spécial de lien variant. Elles permettent de faire varier des ensembles de paramètres prédéfinis pour un objet donné.

Auparavant, il était possible de paramétrer des objets à l\'aide de techniques telles que les feuilles de calcul, mais plusieurs instances variées de cet objet ne pouvaient pas exister en même temps, à moins de recourir à des techniques telles que la copie de fichiers ou d\'objets, ce qui pose des problèmes de maintenance. Les tables de configuration permettent de gérer ces variantes et de passer facilement de l\'une à l\'autre.

Ce tutoriel suppose que vous êtes familiarisé avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md) et l\'[atelier Sketcher](Sketcher_Workbench/fr.md). Vous devez également être familiarisé avec la [vue en arborescence](Tree_view/fr.md) et l\'[éditeur de propriétés](Property_editor/fr.md).

Il existe également une [version vidéo de ce tutoriel](https://www.youtube.com/watch?v=m9C_ahIVKOI).



## Exemple

Pour mieux comprendre les tables de configuration, prenons l\'exemple suivant.

Imaginez un simple écrou hexagonal d\'un diamètre \"principal\" de 10 mm (M10).

Nous pouvons réutiliser le même dessin, créer un lien, puis varier certains paramètres pour créer un écrou hexagonal M12.

Pour notre exemple, nous décrirons les différences entre ces deux variantes avec 3 paramètres :

1.  diamètre du trou central
2.  largeur entre les coins
3.  et l\'épaisseur.

Les valeurs particulières des paramètres de nos variantes sont décrites dans ce tableau :

  Variant   Diameter   WidthAcrossCorners   Thickness
     
  M10       10         18.48                8.4
  M12       12         20.78                10.8



## Instructions

1.  Créez une nouvelle [feuille de calcul](Spreadsheet_CreateSheet/fr.md) avec une ligne d\'en-tête. Laissez la deuxième ligne vide. Cette ligne contiendra la configuration actuelle et sera automatiquement remplie plus tard. Ajoutez les paramètres pour M10 et M12 dans les lignes 3 et 4 :
    ![](images/Variant-link-spreadsheet-table-example-before-configuration-table.png )
2.  Utilisez l\'[atelier PartDesign](PartDesign_Workbench.md) pour créer un [corps](PartDesign_Body/fr.md) et une [esquisse](PartDesign_NewSketch/fr.md) pour l\'écrou hexagonal. La contrainte dimensionnelle sera ajoutée dans une étape ultérieure.
    ![](images/Variant-link-example-hex-nut-sketch-unconstrained.png ).
3.  Faites une [protrusion](PartDesign_Pad/fr.md) de l\'esquisse. Accepter la valeur par défaut de la longueur.
4.  Cliquez avec le bouton droit de la souris sur la cellule A2 de la feuille de calcul et sélectionnez **Table de configuration...** dans le menu contextuel.
5.  La fenêtre de dialogue **Table de configuration** s\'ouvre.
6.  Saisissez ce qui suit :
    ![](images/Variant-link-example-setup-configuration-table.png )

    Ceci remplit la deuxième ligne du tableau, ajoute une nouvelle propriété **Configuration** au corps et y lie la table de configuration.
7.  Appuyez sur le bouton **OK**.
8.  Si la cellule A2 affiche {{Value|#PENDING}}, vous pouvez cliquer avec le bouton droit de la souris sur la feuille de calcul dans la [vue en arborescence](Tree_view/fr.md) et choisir **Recompute object** pour afficher la valeur correcte.
9.  Définissez un alias pour les 3 cellules de la ligne 2 sous Diameter, WidthAcrossCorners et Thickness. Chaque alias doit correspondre à l\'en-tête de colonne de la cellule.
    ![](images/Variant-link-spreadsheet-table-example.png )

    ![](images/Variant-link-spreadsheet-table-example.png ).
10. Contraignez l\'esquisse avec deux contraintes et liez les [expressions](Expressions/fr.md) {{Value|Spreadsheet.Diameter}} et {{Value|Spreadsheet.WidthAcrossCorners}} :
    ![](images/Variant-link-example-hex-nut-sketch.png )
11. Lier {{Value|Spreadsheet.Thickness}} à la **Length** de la protrusion.
12. Créez une [sous forme liée](PartDesign_SubShapeBinder/fr.md).
13. Dans la [vue en arborescence](Tree_view/fr.md), faites glisser le Binder hors du corps et déposez-le sur le nœud Document.
14. Déposez le corps sur le Binder pour définir sa propriété **Support** sur le corps. Le dépôt est nécessaire car cette propriété est en lecture seule par défaut.
15. Définissez la **Bind Copy on Change** à {{Value|Enabled}} du Binder.
16. Sélectionnez {{Value|M12}} pour la propriété **Configuration** du Binder.
17. Définissez **Use Binder Style** à `False` du Binder.
18. Changez **Placement** du Binder pour qu\'il soit éloigné du corps.
19. Une fois terminé, vous devriez avoir quelque chose comme ce qui suit :
    <img alt="" src=images/Variant-link-finished-example-document.png  style="width:500px;">

    .



### Utiliser Std Lien au lieu de PartDesign Sous forme liée 

Pour le lien variant, vous pouvez également utiliser un [Std Lien](Std_LinkMake/fr.md) au lieu d\'un [PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md) :

1.  Les étapes préparatoires 1 à 10 mentionnées ci-dessus sont les mêmes.
2.  Créez un lien vers le corps.
3.  Passez la **Link Copy On Change** à {{Value|Enabled}} sur le lien.
4.  Suivez les étapes 16, 18 et 19 mentionnées ci-dessus.



## Points clés et considérations 

-   Comme dit, un lien variant peut être créé à l\'aide d\'un [Std Lien](Std_LinkMake/fr.md) ou d\'une [PartDesign PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md). Realthunder explique la différence [ici](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183) :{{quote|text=Au lieu de dupliquer l'objet lié avec toute sa hiérarchie, la [sous forme liée](PartDesign_SubShapeBinder/fr.md) fera une copie aplatie de l'objet muté. Une autre différence avec le lien est que la [sous forme liée](PartDesign_SubShapeBinder.md) synchronisera toutes les modifications de l'objet original avec la copie, même si les configurations sont différentes, alors que pour le lien, une fois copiés, les deux objets deviennent indépendants.}}
    
-   Bien que construits sur des liens, les liens variants ne sont pas \"bon marché\" comme les liens normaux, car ils créent des copies de l\'objet original. Des conseils sont fournis par Realthunder [ici](https://forum.freecadweb.org/viewtopic.php?p=532130#p532130) et [ici](https://forum.freecadweb.org/viewtopic.php?p=358582#p358582) :{{quote|text=[Lorsque] vous utilisez un lien pour des configurations alternatives, vous devez savoir qu'il crée une copie de l'objet original... il serait préférable de créer un seul lien "variant" pour chaque [variant] afin d'éviter les doublons inutiles. Ou mieux, utilisez une sous forme liée... Et encore une fois, créez une [sous forme liée](PartDesign_SubShapeBinder/fr.md) pour chaque configuration.}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Spreadsheet](Category_Spreadsheet.md) > Configuration Tables/fr
