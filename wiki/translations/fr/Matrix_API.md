# Matrix API/fr
**(octobre 2019) Ne pas éditer cette page. L'information est incomplète et obsolète. Pour la dernière API, voir la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation du code source](Source_documentation/fr.md).**

Les Matrices 4x4 sont utilisées partout dans FreeCAD et peuvent être créées par l\'une des façons suivantes : 
```python
m = FreeCAD.Matrix()          # m = the [http://en.wikipedia.org/wiki/Identity_matrix identity matrix]
m = FreeCAD.Base.Matrix()
print m.A21()               # print m[1][0]
```


{{APIFunction | A | | | tous les éléments de la matrice}}

. {{APIFunction | A11 | | | un élément de matrice.}} {{APIFunction | A12 | | | un élément de matrice.}} {{APIFunction | A13 | | | un élément de matrice.}} {{APIFunction | A14 | | | un élément de matrice.}} {{APIFunction | A21 | | | un élément de matrice.}} {{APIFunction | A22 | | | un élément de matrice.}} {{APIFunction | A23 | | | un élément de matrice.}} {{APIFunction | A24 | | | un élément de matrice.}} {{APIFunction | A31 | | | un élément de matrice.}} {{APIFunction | A32 | | | un élément de matrice.}} {{APIFunction | A33 | | | un élément de matrice.}} {{APIFunction | A34 | | | un élément de matrice.}} {{APIFunction | A41 | | | un élément de matrice.}} {{APIFunction | A42 | | | un élément de matrice.}} {{APIFunction | A43 | | | un élément de matrice.}} {{APIFunction | A44 | | | un élément de matrice.}}{{APIFunction|determinant| |Calcule le [http://fr.wikipedia.org/wiki/D%C3%A9terminant_%28math%C3%A9matiques%29 déterminant] de la matrice|un nombre.}} {{APIFunction|inverse| |[http://fr.wikipedia.org/wiki/Matrice_inversible Matrice Inverse] cette matrice, si possible|rien.}} {{APIFunction|invert| |Returne l'[http://fr.wikipedia.org/wiki/Matrice_inversible inverse]de cette matrice, si possible|une Matrice}} {{APIFunction|move|Vector|fait faire à cette matrice une [http://fr.wikipedia.org/wiki/Translation_%28g%C3%A9om%C3%A9trie%29 translation] |rien.}} {{APIFunction|multiply|Matrix or Vector|Retourne le [http://http://fr.wikipedia.org/wiki/Produit_vectoriel produit croisé] d'une matrice ou d'un vecteur avec cette matrice|une Matrice}} {{APIFunction|rotateX|Float(radians)|fait faire une  [http://http://fr.wikipedia.org/wiki/Rotation_affine rotation] à cette matrice autour de X |rien.}} {{APIFunction|rotateY|Float(radians)|fait faire une  [http://http://fr.wikipedia.org/wiki/Rotation_affine rotation] à cette matrice autour de Y |rien.}} {{APIFunction|rotateZ|Float(radians)|fait faire une  [http://http://fr.wikipedia.org/wiki/Rotation_affine rotation] à cette matrice autour de Z|rien.}} {{APIFunction|scale|Vector|fait un changement  [http://en.wikipedia.org/wiki/Scaling_matrix d'échelle ]à cette matrice|rien.}} {{APIFunction|transform|Vector, Matrix|Fait à cette matrice une [http://fr.wikipedia.org/wiki/Matrice_d%27une_application_lin%C3%A9aire transformation ] basée sur Vecteur et Matrice |rien. }} {{APIFunction|unity| |Faire de cette matrice la [http://fr.wikipedia.org/wiki/Matrice_identit%C3%A9 matrice unité]|rien.}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Matrix API/fr
