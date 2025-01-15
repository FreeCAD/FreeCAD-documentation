# O-X-Y Type Attachment Modes/fr
Nous fournissons ici des informations plus détaillées sur l\'utilisation des modes de type **Alignement O-X-Y** dans [Part Ancrage](Part_EditAttachment/fr.md).

Ces modes sont les suivants :

-   Alignement O-Z-X
-   Alignement O-Z-Y
-   Alignement O-X-Y
-   Alignement O-X-Z
-   Alignement O-Y-Z
-   Alignement O-Y-X

Ces modes sont utilisés pour ancrer à un sommet spécifié, avec une orientation déterminée par référence à d\'autres sommets ou arêtes.


**Reference1**

doit être un sommet. L\'origine est associée à ce point sélectionné.

Remarque : si un bord est sélectionné pour **Reference1**, les modes de type O-X-Y ne sont pas proposés.


**Reference2**

et **Reference3** doivent être des sommets ou des arêtes. Ils fournissent des informations sur la direction. Pour un sommet, la direction va de l\'origine au sommet sélectionné. Pour une arête, il s\'agit de la direction de l\'arête. **Reference3** est facultatif.

Prenons l\'exemple du mode O-X-Z :

-   Le **O** représente l\'origine, correspondant à **Reference1**.
-   Le **X** indique que l\'axe X de l\'objet ancré doit être aligné avec la direction du **Reference2**.
-   Le **Z** indique que l\'axe Z de l\'objet ancré doit être aligné sur la composante de la direction de **Reference3** à angle droit par rapport à l\'axe X.
-   L\'axe **Y** complète la triade des axes orthogonaux.

Pour les autres modes, les axes sont représentés de manière correspondante.

Si **Reference3** n\'est pas donné, FreeCAD le choisit par défaut.


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > O-X-Y Type Attachment Modes/fr
