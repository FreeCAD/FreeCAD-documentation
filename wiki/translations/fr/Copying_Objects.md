# Copying Objects/fr
## Présentation

Comme beaucoup d\'autres programmes informatiques, FreeCAD a la possibilité de couper, copier et coller des objets. Les objets [Documents](Document_structure/fr.md) peuvent être librement copiés dans un document ou entre documents en utilisant les fonctions <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Std Copier](Std_Copy/fr.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Std Coller](Std_Paste/fr.md) et [Std Dupliquer une sélection](Std_DuplicateSelection/fr.md).

![centre](images/Copy_past_duplicate.png )

Veuillez considérer que les objets copiés-collés ne dépendent pas de l\'original. Si vous voulez des clones dépendants, veuillez utiliser <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Draft Cloner](Draft_Clone/fr.md) ou <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [PartDesign Clone](PartDesign_Clone/fr.md). Si vous n\'avez besoin ni d\'un clone dépendant ni d\'une réplique paramétrique, vous pouvez également utiliser <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [Part Copie simple](Part_SimpleCopy/fr.md). Pour les clones à motifs, veuillez regarder dans [Autres méthodes](Copying_Objects/fr#Autres_m.C3.A9thodes.md) de cette page.



## Copier des objets liés 

-   Si un objet à copier a des liens avec des objets qui ne sont pas dans la sélection, FreeCAD demandera si les objets non sélectionnés doivent être inclus dans l\'opération de copie.



## Trouver et positionner un ou des objets collés 

Après une opération de copier-coller, l\'emplacement des nouveaux objets dans la [vue 3D](3D_view/fr.md) peut ne pas être évident. Cela est dû au fait que les nouveaux objets ont la même propriété de [Placement](Placement/fr.md) que leurs originaux. Basculez la propriété Visibility (**Barre d'espace**) pour masquer les originaux, puis déplacez les copies à leur emplacement correct, par exemple en utilisant <img alt="" src=images/Std_TransformManip.svg  style="width:24px;"> [Std Transformer](Std_TransformManip/fr.md) ou <img alt="" src=images/Std_Placement.svg  style="width:24px;"> [Std Positionner](Std_Placement/fr.md).



## Autres méthodes 

Comme la plupart des choses dans FreeCAD, il y a plusieurs façons de faire une copie. Pour plus d\'idées, consultez :

-   PartDesign : [Symétrie](PartDesign_Mirrored/fr.md), [Répétition linéaire](PartDesign_LinearPattern/fr.md), [Répétition circulaire](PartDesign_PolarPattern/fr.md), [Transformations multiples](PartDesign_MultiTransform/fr.md)
-   Part : [Miroir](Part_Mirror/fr.md), [Copie simple](Part_SimpleCopy.md)
-   Draft : [Décaler](Draft_Offset/fr.md), [Échelle](Draft_Scale/fr.md), [Réseau orthogonal](Draft_OrthoArray/fr.md), [Réseau selon une courbe](Draft_PathArray/fr.md), [Cloner](Draft_Clone/fr.md), [Miroir](Draft_Mirror/fr.md)



---
⏵ [documentation index](../README.md) > Copying Objects/fr
