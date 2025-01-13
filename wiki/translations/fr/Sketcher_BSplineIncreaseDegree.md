---
 GuiCommand:
   Name: Sketcher BSplineIncreaseDegree
   Name/fr: Sketcher Augmenter le degré d'une B-spline
   MenuLocation: Esquisse , Outils d'esquisse des B-splines , Augmenter le degré d'une B-spline
   Workbenches: Sketcher_Workbench/fr
   Version: 0.17
   SeeAlso: Sketcher_BSplineDecreaseDegree/fr
---

# Sketcher BSplineIncreaseDegree/fr

## Description

L\'outil <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:24px;"> [Sketcher Augmenter le degré d\'une B-spline](Sketcher_BSplineIncreaseDegree/fr.md) augmente le degré (l\'ordre) des [B-splines](B-Splines/fr.md).



## Utilisation

1.  Sélectionnez une ou plusieurs B-splines.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> [Augmenter le degré de la B-spline](Sketcher_BSplineIncreaseDegree/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse des B-splines → <img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Augmenter le degré de la B-spline** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Augmenter le degré de la B-spline** du menu contextuel.



## Exemple

Les B-splines sont essentiellement une combinaison de [courbes de Bézier](https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier) (bien expliqué ces vidéos [ici](https://www.youtube.com/watch?v=bE1MrrqBAl8) et [ici](https://www.youtube.com/watch?v=xXJylM2S72s)).

Dans cette spline cubique (degré 3) il y a 3 segments, ce qui signifie que 3 courbes sont reliées à 2 nœuds.

Le degré est indiqué par le chiffre au centre. Voir <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:16px;"> [Afficher/masquer le degré des B-splines](Sketcher_BSplineDegree/fr.md).

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*Une B-spline de degrés 3 et avec 2 nœuds qui ont chacun une multiplicité de 1.*

Les segments extérieurs ont chacun 2 points de contrôle, le segment intérieur n\'en a aucun pour s\'assurer que les nœuds ont une multiplicité de 1. Voir [cette page](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) pour une explication de la multiplicité.

En augmentant le degré à 4, on ajoute des points de contrôle sans modifier la forme de la B-spline :

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Même B-spline où le degré a été changé de 3 à 4. Notez que la multiplicité des nœuds a également été augmentée.*

À partir de ce résultat, il n\'est pas possible de revenir à l\'état initial de la B-spline en diminuant le degré. Certaines informations sont perdues lorsque le degré d\'une B-spline est modifié. Diminuer le degré à 3 conduit à ce résultat :

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Même B-spline où le degré a été ramené de 4 à 3. Notez que la multiplicité des nœuds a de nouveau augmenté. En fonction de la B-spline, l'algorithme de réduction du degré peut ajouter un grand nombre de nœuds pour préserver la forme, comme c'est le cas ici.*

Chaque segment a maintenant 2 points de contrôle et chaque nœud coïncide avec un point de contrôle supplémentaire. Les nœuds ont une continuité *C^0^* telle que la B-spline obtiendra des \"coins\" si vous déplacez un point de contrôle. L\'information d\'une continuité plus élevée est donc perdue. Voir [cette page](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) pour une explication sur la continuité.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/fr
