# Copying Objects/fr

 {{TOCright}}

## Vue d\'ensemble 

Comme beaucoup d\'autres logiciels, FreeCAD est également capable de copier/couper et coller des objets (paragraphes, cellules de feuille de calcul, images, etc.). Les objets [documents](Document_structure/fr.md) peuvent être librement copiés dans un document ou entre des documents à l\'aide des commandes **<img src="images/Std_Copy.svg" width=24px> [Copier](Std_Copy/fr.md)**, **<img src="images/Std_Paste.svg" width=24px> [Coller](Std_Paste/fr.md)** et **[Dupliquer une sélection](Std_DuplicateSelection/fr.md)**.

![centre](images/Copy_past_duplicate.png )

Veuillez considérer que les objets copiés-collés ne dépendent pas de l\'original. Si vous voulez des clones dépendants, veuillez utiliser <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Draft Clone](Draft_Clone/fr.md) ou <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [PartDesign Clone](PartDesign_Clone/fr.md). Si vous avez besoin d\'un clone dépendant ou d\'un réplica paramétrique, vous pouvez également utiliser <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [Part Copie simple](Part_SimpleCopy/fr.md). Pour les clones à motifs, veuillez regarder dans [Autres méthodes](Copying_Objects/fr#Autres_m.C3.A9thodes.md) de cette page.

## Copier des objets liés 

Les objets [Document](Document_structure/fr.md) peuvent être liés à d\'autres objets (par exemple, une fonctionnalité Pad est liée à son esquisse et une fonctionnalité Fusion est liée à ses objets composants). Cela signifie que vous devez choisir avec soin les objets à copier.

Si un objet est sélectionné sans ses enfants, ses enfants ne sont pas automatiquement dupliqués par Copier/Coller ou la sélection Dupliquer. Dans ce cas, l\'objet copié peut présenter un comportement inattendu en raison de liens attendus n\'étant pas présents.

En général, la pratique recommandée consiste à sélectionner tous les objets dépendants lors de la copie d\'un objet parent.

## Recherche et positionnement d\'objet(s) collé(s) 

Après l\'opération Copier/Coller, il peut ne pas être évident de voir où le nouvel objet est situé dans la fenêtre du Document. C\'est parce que le nouvel objet a la même [position](Placement/fr.md) que l\'original. Basculez la propriété de Visibilité (**Barre d'espace**) pour cacher l\'original. Ensuite, utilisez la boîte de dialogue Placement pour déplacer la copie à sa position correcte.

## Autres méthodes 

Comme la plupart des choses dans FreeCAD, il y a plusieurs façons de faire une copie. Pour plus d\'idées, consultez:

-   PartDesign: [Symétrie](PartDesign_Mirrored/fr.md), [Répétition linéaire](PartDesign_LinearPattern/fr.md), [Répétition circulaire](PartDesign_PolarPattern/fr.md), [Transformations multiples](PartDesign_MultiTransform/fr.md)
-   Part: [Miroir](Part_Mirror/fr.md), [Copie simple](Part_SimpleCopy.md)
-   Draft: [Décalage](Draft_Offset/fr.md), [Echelle](Draft_Scale/fr.md), [Réseau orthogonal](Draft_OrthoArray/fr.md), [Réseau selon une courbe](Draft_PathArray/fr.md), [Clone](Draft_Clone/fr.md), [Miroir](Draft_Mirror/fr.md)

## Remarques

-   Si un objet à copier a des liens avec des objets qui ne sont pas dans la sélection, FreeCAD demandera si les objets non sélectionnés doivent être inclus dans l\'opération de copie. {{Version/fr|0.14}}

## Plus

-   [Copier](Std_Copy/fr.md)
-   [Coller](Std_Paste/fr.md)
-   [Dupliquer une sélection](Std_DuplicateSelection/fr.md)



