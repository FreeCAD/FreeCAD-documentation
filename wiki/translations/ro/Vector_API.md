# Vector API/ro



<div class="mw-translate-fuzzy">

Vectorii sunt utilizați peste tot în FreeCAD.


</div>

Vectors are used everywhere in FreeCAD.

Exempluː 
```python
v=FreeCAD.Vector()
v=FreeCAD.Vector(1,0,0)
v=FreeCAD.Base.Vector()
v2 = FreeCAD.Vector(3,2,-5)
v3 = v.add(v2)
print v3.Length
```


{{APIProperty|Length|returnează lungimea vectorului.}}


{{APIFunction|add|Vector|adaugă un alt vector la acesta.|vector}}


{{APIFunction|cross|Vector|produsul vectorial între acest vector și un altul.|vector}}


{{APIFunction|distanceToLine|Vector1,Vector2| distanța dintre vector și o linie prin Vector1 în direcția Vector2.|float}}


{{APIFunction | distanceToLineSegment | Vector1, Vector2 | vector la cel mai apropiat punct pe un segment de linie de la Vector1 la Vector2 | vector}}


{{APIFunction | distanceToPlane | Vector1, Vector2 | distanța dintre vector și un plan definit de un punct și o normală. | Float}}


{{APIFunction | dot | Vector | produsul scalar între 2 vectori | float}}


{{APIFunction | getAngle | Vector | unghiul în radiani între acest vector și un altul. | float}}


{{APIFunction | multiplica | Float | multiplica (scara uniforma) un vector cu factorul dat. | Nimic}}


{{APIFunction | normaliza | | normalizează un vector (stabilește lungimea lui la 1.0). | nothing}}


{{APIFunction | projectToLine | Vector1, Vector2 | proiectează vectorul pe o linie prin Vector1 în direcția Vector2. | Nothing}}


{{APIFunction | projectToPlane | Vector1, Vector2 | proiectează vectorul pe un plan definit de un punct (Vector1) și un vector o normală (vector2). | nothing}}


{{APIFunction | scale | Float, Float, Float | Același lucru ca și multiplicare, dar permite să specificați diferite valori pentru direcțiile x, y și z. (scară neuniformă) | nimic}}


{{APIFunction|sub|Vector|scăderea altui vector din acesta.|vector}}


{{APIProperty|x|coordonata x a vectorului.}}


{{APIProperty|y|coordonata y a vectorului.}}


{{APIProperty|z|coordonata z a vectorului}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
