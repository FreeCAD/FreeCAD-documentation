# Vector API/fr
**(Octobre 2019) Ne modifiez pas cette page. L'information est incomplète et obsolète. Pour la dernière API, consultez la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation du code source](Source_documentation/fr.md).**

Les vecteurs sont utilisés partout dans FreeCAD.

Exemple : 
```python
v=FreeCAD.Vector()
v=FreeCAD.Vector(1,0,0)
v=FreeCAD.Base.Vector()
v2 = FreeCAD.Vector(3,2,-5)
v3 = v.add(v2)
print v3.Length
```


{{APIProperty|Length|renvoie la longueur du vecteur.}}


{{APIFunction|add|Vector|ajoute un autre vecteur à celui-ci|vecteur}}


{{APIFunction|distanceToPoint|Vector|la distance entre ce vecteur et un autre.|virgule flottante}}


{{APIFunction |cross|Vector|le produit croisé entre ce vecteur et un autre.|vecteur}}


{{APIFunction|distanceToLine|Vector1, Vector2|la distance entre le vecteur et une ligne passant par Vecteur1 dans la direction Vecteur2.|virgule flottante}}


{{APIFunction|distanceToLineSegment|Vector1,Vector2|un vecteur au point le plus proche sur un segment de ligne de Vector1 à Vector2.|vecteur}}


{{APIFunction|distanceToPlane|Vector1, Vector2|la distance entre le vecteur et un plan défini par un point et une normale.|virgule flottante}}


{{APIFunction|dot|Vector|le produit scalaire entre deux vecteurs.|virgule flottante}}


{{APIFunction|getAngle|Vector|l'angle en radians entre ce vecteur et un autre.|virgule flottante}}


{{APIFunction|isEqual|Vector2,tolerance|vérifie si la distance entre les points représentés par ce Vector et Vector2 est inférieure ou égale à la tolérance donnée.|vrai/faux}}


{{APIFunction|isNormal|Vector2,tolerance|vérifie si ce vecteur est normal à Vector2 dans les limites de la tolérance.|vrai/faux}}


{{APIFunction|isOnLineSegment|Vector1,Vector2|vérifie si ce vecteur est sur le segment de ligne généré par Vector1 et Vector2.|vecteur}}


{{APIFunction|isParallel|Vector2,tolerance|vérifie si ce vecteur est parallèle à Vector2 dans la limite de la tolérance.|vrai/faux}}


{{APIFunction|multiply|Float|multiplie (échelles) un vecteur par le facteur donné.|rien}}


{{APIFunction|negative|Vector|renvoie le négatif (opposé) de ce vecteur.|vecteur}}


{{APIFunction|normalize| |normalise un vecteur (fixe sa longueur à 1,0).|rien}}


{{APIFunction|projectToLine|Vector1, Vector2 |projette le vecteur sur une ligne entre Vecteur1 et Vector2.|rien}}


{{APIFunction|projectToPlan|Vector1, Vector2| projette le vecteur sur un plan défini par un point et un normal|rien}}


{{APIFunction|scale|Float,Float,Float|comme multiply, mais permet de spécifier des valeurs différentes pour les directions x, y et z. (échelle non uniforme)|rien}}


{{APIFunction |sub|Vector|soustrait un autre vecteur du premier.|vecteur}}


{{APIProperty|x|la coordonnée x d'un vecteur.}}


{{APIProperty |y|la coordonnée y d'un vecteur.}}


{{APIProperty|z|la coordonnée z d'un vecteur.}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Vector API/fr
