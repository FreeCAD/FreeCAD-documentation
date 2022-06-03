# Vector API/fr
{{VeryImportantMessage |(Octobre 2019) Ne modifiez pas cette page. L'information est incomplète et obsolète. Pour la dernière API, consultez la [https   *//www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Source documentation](Source_documentation/fr.md).}}

Les vecteurs sont utilisés partout dans FreeCAD.

Exemple   * 
```python
v=FreeCAD.Vector()
v=FreeCAD.Vector(1,0,0)
v=FreeCAD.Base.Vector()
v2 = FreeCAD.Vector(3,2,-5)
v3 = v.add(v2)
print v3.Length
```


{{APIProperty|Length|renvoie la longueur du vecteur.}}


{{APIFunction|add|Vector|ajoute un autre vecteur à celui-ci|. La somme de deux vecteurs.|vecteur}}


{{APIFunction |cross|Vector|le produit croisé entre ce vecteur et un autre.|vecteur}}


{{APIFunction|distanceToLine|Vector1, Vector2|la distance entre le vecteur et une ligne passant par Vecteur1 dans la direction Vecteur2.|float}}


{{APIFunction|distanceToLineSegment|Vector1,Vector2|un vecteur au point le plus proche sur un segment de ligne de Vector1 à Vector2.|vecteur}}


{{APIFunction|distanceToPlane|Vector1, Vector2|la distance entre le vecteur et un plan défini par un point et une normale.|float}}


{{APIFunction|dot|Vector||le produit scalaire entre deux vecteurs.|float}}


{{APIFunction|getAngle|Vector|l'angle en radians entre ce vecteur et un autre.|float}}


{{APIFunction|multiply|Float|multiplie (échelles) un vecteur par le facteur donné.|Rien.}}


{{APIFunction|normalize| |normalise un vecteur (fixe sa longueur à 1,0).|Rien}}


{{APIFunction|projectToLine|Vector1, Vector2 |projette le vecteur sur une ligne entre Vecteur1 et Vector2.|Rien}}


{{APIFunction|projectToPlan|Vector1, Vector2| projette le vecteur sur un plan défini par un point et un normal|Rien.}}


{{APIFunction|scale|Float,Float,Float|même que multipy, mais permet de spécifier des valeurs différentes pour les directions x, y et z. (non-uniform scale)|Rien.}}


{{APIFunction |sub|Vector | soustrait un autre vecteur du premier.|vector}}


{{APIProperty|x|la coordonnée x d'un vecteur.}}


{{APIProperty |y|la coordonnée y d'un vecteur.}}


{{APIProperty|z|la coordonnée z d'un vecteur.}}


 

[Category   *API](Category_API.md) [Category   *Poweruser Documentation](Category_Poweruser_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Vector API/fr
