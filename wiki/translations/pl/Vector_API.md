 {{VeryImportantMessage|''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).}}

Wektory są używane dosłownie wszędzie w programie FreeCAD.

Przykład: 
```python
v=FreeCAD.Vector()
v=FreeCAD.Vector(1,0,0)
v=FreeCAD.Base.Vector()
v2 = FreeCAD.Vector(3,2,-5)
v3 = v.add(v2)
print v3.Length
```


{{APIProperty|Length|zwraca długość wektora.}}


{{APIFunction|add|Vector|dodaje kolejny wektor do obecnego.|vector}}


{{APIFunction|cross|Vector|iloczyn krzyżowy pomiędzy obecnym wektorem a kolejnym.|vector}}


{{APIFunction|distanceToLine|Vector1,Vector2|odległość między wektorem a prostą przechodzącą przez wektor1 w kierunku wektora2.|float}}


{{APIFunction|distanceToLineSegment|Vector1,Vector2|wektor do najbliższego punktu na odcinku od wektora1 do wektora2.|vector}}


{{APIFunction|distanceToPlane|Vector1,Vector2|odległość między wektorem a płaszczyzną zdefiniowaną przez punkt i normalną.|float}}


{{APIFunction|dot|Vector|iloczyn punktowy między 2 wektorami.|float}}


{{APIFunction|getAngle|Vector|kąt w radianach pomiędzy obecnym wektorem a kolejnym.|float}}


{{APIFunction|multiply|Float|mnoży ''(skala jednostajna)'' wektor przez podany współczynnik.|nothing}}


{{APIFunction|normalize| |normalizuje wektor ''(ustawia jego długość na wartość 1.0)''.|nothing}}


{{APIFunction|projectToLine|Vector1,Vector2|rzutuje wektor na prostą przechodzącą przez wektor1 w kierunku wektora2.|nothing}}


{{APIFunction|projectToPlane|Vector1,Vector2|rzutuje wektor na płaszczyznę zdefiniowaną przez punkt ''(wektor1)'' i normalną ''(wektor2)''.|nothing}}


{{APIFunction|scale|Float,Float,Float|To samo co mnożenie, ale pozwala określić różne wartości dla kierunków x, y i z. ''(niejednolita skala)''|nothing}}


{{APIFunction|sub|Vector|odejmuje wektor od obecnego.|vector}}


{{APIProperty|x|współrzędna x wektora.}}


{{APIProperty|y|współrzędna y wektora.}}


{{APIProperty|z|współrzędna z wektora.}}


 

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)
