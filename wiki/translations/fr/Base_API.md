# Base API/fr
{{VeryImportantMessage | (octobre 2019) Ne pas éditer cette page. L'information est incomplète et obsolète. Pour la dernière API, voir la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation source](Source_documentation/fr.md).}}

Le module de base est contenu à l\'intérieur du module FreeCAD et contient les constructeurs pour différents types d\'objets largement utilisés dans FreeCAD.


{{APIClass|BoundBox|[Xmin,Ymin,Zmin,Xmax,Ymax,Zmax] ) ou ( Tuple, Tuple ) ou ( Vector, Vector|créent un cadre enveloppant. Un cadre de délimitation est un cube orthographique qui est une façon de décrire les limites extérieures. Vous obtenez une boîte de sélection à partir d'un grand nombre de types 3D. Il est souvent utilisé pour vérifier si une entité 3D réside dans les limites d'un autre objet. La vérification des interférences des limites permet d'économiser beaucoup de temps de calcul!}}


{{APIClass | Matrix| | Crée une  [ Matrice](Matrix_API/fr.md) 4x4., Qui peut être utilisée pour appliquer des transformations aux objets}}

{{APIClass | Vector |) ou (x, y, z | Crée un  [ Vecteur](Vector_API/fr.md) FreeCAD 3D., Ce qui représente un point de 3D ou une direction}}


{{APIClass|Placement| |Creates a [Placement](Placement_API.md).}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Base API/fr
