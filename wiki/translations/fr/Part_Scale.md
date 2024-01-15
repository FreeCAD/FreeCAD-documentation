---
 GuiCommand:
   Name: Part Scale
   Name/fr: Part Échelle
   MenuLocation: Part , Échelle...
   Workbenches: Part_Workbench/fr
   Version: 0.22
   SeeAlso: Draft_Clone/fr, Draft_Scale/fr
---

# Part Scale/fr



## Description

**Part Échelle** met à l\'échelle les formes selon un facteur spécifié dans toutes les directions ou selon des facteurs distincts dans chaque direction principale. Dans le cas de facteurs distincts, les formes peuvent être déformées.

![400px](images/Part_Scale_demo.png) 
*Exemples de mise à l'échelle*



## Utilisation

1.  Sélectionner une ou plusieurs formes dans la [vue 3D](3D_view/fr.md) ou dans la [vue en arborescence](Tree_view/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyer sur le **<img src="images/Part_Scale.svg" width=16px> [Échelle...](Part_Scale/fr.md)**.
    -   Sélectionner l\'option **Part → <img src="images/Part_Scale.svg" width=16px> Échelle...** dans le menu.
3.  Un [panneau des tâches](#Panneau_des_tâches.md) s\'ouvre.
4.  Choisir soit **Échelle uniforme** soit **Échelle non uniforme**.
5.  Définir le(s) facteur(s) d\'échelle.
6.  Cliquer sur **OK**.

La sélection peut également être effectuée après le lancement de la commande, en sélectionnant une ou plusieurs formes dans la liste du [panneau des tâches](#Panneau_des_tâches.md).

La vue en arborescence répertorie autant d\'objets Échelle qu\'il y a de formes sélectionnées. Chaque forme saisie est placée sous son objet Scale.



## Panneau des tâches 

![](images/Part_Scale_dialog.png )

-   Le bouton **OK** crée l\'objet mis à l\'échelle et ferme le panneau des tâches.
-   Le bouton **Fermer** ferme le panneau des tâches sans rien faire.
-   Le bouton **Appliquer** crée les objets mis à l\'échelle, mais ne ferme pas le panneau des tâches. Vous pouvez ensuite sélectionner une autre forme dans la liste du bas et créer d\'autres objets à l\'échelle.
-   La liste des **Forme**s : sélectionner ici les formes à mettre à l\'échelle. Si plusieurs formes sont sélectionnées, plusieurs objets Scale sont créés.



## Remarques

-   Une mise à l\'échelle non uniforme transformera toutes les arêtes en courbes B-spline et toutes les faces en surfaces B-spline. Ces dernières sont plus lourdes à calculer.
-   Les points et les sommets ne peuvent pas être mis à l\'échelle car ils sont sans dimension.
-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être mis à l\'échelle.
-   Le panneau des tâches n\'offre pas encore d\'aperçu. **Appliquer** créera un objet à l\'échelle chaque fois que vous cliquez dessus, ce qui peut être utile en tant qu\'aperçu. Ils resteront cependant et un autre objet mis à l\'échelle sera créé lorsque vous cliquerez sur **OK**. [Annuler](Std_Undo/fr.md) peut être utile pour les nettoyer avant de cliquer sur **OK**.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Part Échelle est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Scale}}

-    **Base|Link**: forme d\'entrée (la forme sur laquelle Part Échelle a été appliquée).

-    **Uniform|Bool**: contrôle la mise à l\'échelle uniforme ou non uniforme

-    **Uniform Scale|Float**: facteur d\'échelle pour la mise à l\'échelle uniforme

-    **XScale|Float**: facteur d\'échelle en X pour une mise à l\'échelle non uniforme.

-    **YScale|Float**: facteur d\'échelle en Y, idem.

-    **ZScale|Float**: facteur d\'échelle en Z, idem.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Scale/fr
