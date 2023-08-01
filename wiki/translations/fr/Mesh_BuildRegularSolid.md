---
- GuiCommand:/fr
   Name:Mesh BuildRegularSolid
   Name/fr:Mesh Solide régulier
   MenuLocation:Maillages → Solide régulier...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
---

# Mesh BuildRegularSolid/fr

## Description

La commande **Solide régulier** crée un solide paramétrique, maillé régulier.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_BuildRegularSolid.svg" width=16px> [Solide régulier...](Mesh_BuildRegularSolid/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Solide régulier...** du menu.
2.  La boîte de dialogue **Solide régulier** s\'ouvre.
3.  Sélectionnez d\'abord un type d\'objet maillé dans la liste déroulante :
    -   
        **<img src="images/Mesh_Cube.svg" width=16px> Cube
**
        

    -   
        **<img src="images/Mesh_Cylinder.svg" width=16px> Cylindre
**
        

    -   
        **<img src="images/Mesh_Cone.svg" width=16px> Cône
**
        

    -   
        **<img src="images/Mesh_Sphere.svg" width=16px> Sphère
**
        

    -   
        **<img src="images/Mesh_Ellipsoid.svg" width=16px> Ellipsoïde
**
        

    -   
        **<img src="images/Mesh_Torus.svg" width=16px> Tore
**
        
4.  Spécifiez les paramètres requis. Les paramètres disponibles dépendent du type d\'objet maillé. Voir [Propriétés](#Properties.md).
5.  Pour les maillages avec des surfaces courbes: une valeur **Numérisation** plus élevée donne un maillage plus fin.
6.  Appuyez sur le bouton **Créer** pour créer l\'objet maillage.
7.  Créez éventuellement plus d\'objets maillés.
8.  Appuyez sur le bouton **Fermer** pour fermer la boîte de dialogue et terminer la commande.



## Remarques

-   Les objets maillés créés avec cette commande sont paramétriques. A chaque fois qu\'ils sont recalculés, par exemple après avoir changé l\'un de leurs paramètres, leur maillage est reconstruit. Cela signifie que les manipuler avec des commandes telles que [Mesh Affinage](Mesh_RemeshGmsh/fr.md), [Mesh Echelle](Mesh_Scale/fr.md) etc\... n\'a généralement pas de sens.



## Propriétés

Les objets maillés créés avec cette commande héritent de toutes les propriétés [Mesh Feature](Mesh_Feature/fr.md). De plus, chaque type d\'objet maillé a un certain nombre de propriétés pour contrôler son comportement paramétrique :

### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Cube 



#### Données


{{TitleProperty|Cube}}

-    **Height|FloatConstraint**: hauteur du cube.

-    **Length|FloatConstraint**: longueur du cube.

-    **Width|FloatConstraint**: largeur du cube.



### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Cylindre 



#### Données 


{{TitleProperty|Base}}

-    **Closed|Bool**: si à `False`, les extrémités planes du cylindre sont laissées ouvertes.

-    **Edge Length|FloatConstraint**: longueur des arêtes des faces du maillage.

-    **Length|FloatConstraint**: longueur du cylindre.

-    **Radius|FloatConstraint**: rayon du cylindre.

-    **Sampling|IntegerConstraint**: nombre de faces le long de la surface courbe.



### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Cône 



#### Données 


{{TitleProperty|Base}}

-    **Closed|Bool**: si la valeur `False` est attribuée, la ou les extrémités planes du cône sont laissées ouvertes.

-    **Edge Length|FloatConstraint**: longueur des arêtes des faces du maillage.

-    **Length|FloatConstraint**: longueur du cône.

-    **Radius 1|FloatConstraint**: premier rayon du cône. Peut être {{value|0}}.

-    **Radius 2|FloatConstraint**: deuxième rayon du cône. Peut être {{value|0}}.

-    **Sampling|IntegerConstraint**: nombre de faces le long de la surface courbe.



### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Sphère 



#### Données 


{{TitleProperty|Base}}

-    **Radius|FloatConstraint**: rayon de la sphère.

-    **Sampling|IntegerConstraint**: nombre de faces dans les deux directions de la surface courbe.



### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Ellipsoïde 



#### Données 


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: premier rayon de l\'ellipsoïde.

-    **Radius 2|FloatConstraint**: deuxième rayon de l\'ellipsoïde.

-    **Sampling|IntegerConstraint**: nombre de faces dans les deux directions de la surface courbe.



### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Tore 



#### Données 


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: premier rayon (principal) du tore.

-    **Radius 2|FloatConstraint**: deuxième rayon du tore.

-    **Sampling|IntegerConstraint**: nombre de faces dans les deux directions de la surface courbe.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh BuildRegularSolid/fr
