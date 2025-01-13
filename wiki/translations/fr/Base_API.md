# Base API/fr
**(octobre 2019) Ne pas éditer cette page. L'information est incomplète et obsolète. Pour la dernière API, voir la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation du code source](Source_documentation/fr.md).**

Le module de Base est contenu à l\'intérieur du module FreeCAD et contient les constructeurs pour différents types d\'objets largement utilisés dans FreeCAD.


{{APIClass b|BoundBox|[Xmin,Ymin,Zmin,Xmax,Ymax,Zmax]}}


{{APIClass b|BoundBox|Tuple, Tuple}}


{{APIClass|BoundBox|Vector, Vector|créent une boîte de englobante.
Une boîte englobante est un cube orthographique qui permet de décrire les limites extérieures. De nombreux types d'objets 3D sont dotés d'une boîte englobante. Elle est souvent utilisée pour vérifier si une entité 3D se trouve dans le champ d'action d'un autre objet. Vérifier d'abord l'existence d'une interférence englobante peut faire gagner beaucoup de temps de calcul !}}


{{APIClass|Matrix| |Crée une [matrice](Matrix_API/fr.md) 4x4 qui peut être utilisée pour appliquer des transformations aux objets.}}


{{APIClass b|Vector| }}


{{APIClass|Vector|x, y, z|Crée un [vecteur](Vector_API/fr.md) 3D de FreeCAD, représentant un point 3D ou une direction.}}


{{APIClass|Placement| |crée un [positionnement](Placement_API/fr.md).}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Base API/fr
