---
- GuiCommand:/fr
   Name:Mesh CrossSections
   Name/fr:Mesh Coupes
   MenuLocation:Maillages → Cutting → Coupes...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Section](Mesh_SectionByPlane/fr.md)
---

# Mesh CrossSections/fr

## Description

La commande **Mesh Coupes** crée plusieurs coupes transversales sur les objets maillés. Les coupes transversales sont prises parallèlement à l\'un des principaux plans globaux (XY, XZ ou YZ). Pour chaque ensemble de sections transversales, une seule [Part Feature](Part_Feature/fr.md) est créée.

## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_CrossSections.svg" width=16px> [Coupes](Mesh_CrossSections/fr.md)
**
    -   Sélectionnez l\'option **Maillages → Cutting → <img src="images/Mesh_CrossSections.svg" width=16px> Coupes..** dans le menu.
3.  Le panneau des tâches **Coupes** s\'ouvre.
4.  Les plans qui seront utilisés pour créer les coupes sont indiqués dans la [vue 3D](3D_view/fr.md) et seront mis à jour en fonction des entrées du panneau de tâches.
5.  Sélectionnez le **Plan guide**:
    -   
        **XY**
        

    -   
        **XZ**
        

    -   
        **YZ**
        
6.  Spécifiez la **Position** du plan de guidage à partir de l\'origine. La position par défaut est basée sur le centre de la boîte englobante des objets maillés sélectionnés. Choisir un autre **Plan guide** ou activer la case à cocher **Sections** réinitialisera **Positon** à cette valeur par défaut.
7.  Cochez éventuellement la case **Sections** pour créer plusieurs sections transversales:
    -   
        **Des deux côtés**
        
        : si coché, des coupes sont créées des deux côtés du plan de guidage.

    -   
        **Count**
        
        : le nombre de sections transversales.

    -   
        **Distance**
        
        : la distance entre les sections transversales. La valeur par défaut est basée sur les dimensions du cadre de sélection, sur l\'option **Des deux côtés** et sur la valeur **Nombre**. La modification de la valeur **Nombre** réinitialisera **Distance** à cette valeur par défaut. Changer l\'option **Des deux côtés** recalculera la **Distance** ({{value|*2.0}} ou {{value|*0.5}}). Notez que la zone de saisie peut être grisée mais la valeur peut en fait être modifiée.

    -   Cochez éventuellement la case **Raccorder les arêtes si la distance est inférieure à** et spécifiez une valeur.
8.  Appuyez sur le bouton {{button|Appliquer}} pour créer l\'ensemble des sections transversales.
9.  Modifiez éventuellement un ou plusieurs paramètres et créez des ensembles supplémentaires de sections transversales.
10. Appuyez sur le bouton {{button|OK}} ou sur le bouton {{button|Annuler}} pour fermer le panneau des tâches et terminer la commande.

## Propriétés

Voir: [Part Feature](Part_Feature/fr.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh CrossSections/fr
