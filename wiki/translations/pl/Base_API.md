# Base API/pl
 **''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

Moduł Base jest zawarty wewnątrz modułu FreeCAD i zawiera konstruktory dla różnych typów obiektów często używanych w programie FreeCAD.


{{APIClass b|BoundBox|[Xmin,Ymin,Zmin,Xmax,Ymax,Zmax]}}


{{APIClass b|BoundBox|Tuple, Tuple}}


{{APIClass|BoundBox|Vector, Vector|
Tworzy ramkę okalającą.
Ramka ograniczająca to sześcian prostokątny, który jest sposobem na zdefiniowanie zewnętrznych granic. Otrzymujesz ramkę ograniczającą z wielu typów 3D. Jest on często używany do sprawdzenia, czy obiekt 3D leży w zasięgu innego obiektu. Sprawdzanie najpierw czy nie ma żadnych przeszkód może zaoszczędzić dużo czasu obliczeniowego!}}


{{APIClass|Matrix| |Tworzy [Macierz](Matrix_API/pl.md) 4x4, która może być użyta do zastosowania przekształceń do obiektów.}}


{{APIClass b|Vector| }}


{{APIClass|Vector|x, y, z|Tworzy [Wektor](Vector_API/pl.md) 3D FreeCAD, reprezentujący punkt 3D lub kierunek.}}


{{APIClass|Placement| |Tworzy [Umiejscowienie](Placement_API/pl.md).}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
