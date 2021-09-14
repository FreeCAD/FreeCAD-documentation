# Matrix API/pl

 {{VeryImportantMessage|''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).}}

Macierze 4x4 są używane we wszystkich miejscach programu FreeCAD i mogą być tworzone w jeden z następujących sposobów: 
```python
m = FreeCAD.Matrix()          # m = the [http://en.wikipedia.org/wiki/Identity_matrix identity matrix]
m = FreeCAD.Base.Matrix()
print m.A21()               # print m[1][0]
```


{{APIFunction|A| | |wszystkie elementy macierzy.}}


{{APIFunction|A11| | |element macierzy.}}


{{APIFunction|A12| | |element macierzy.}}


{{APIFunction|A13| | |element macierzy.}}


{{APIFunction|A14| | |element macierzy.}}


{{APIFunction|A21| | |element macierzy.}}


{{APIFunction|A22| | |element macierzy.}}


{{APIFunction|A23| | |element macierzy.}}


{{APIFunction|A24| | |element macierzy.}}


{{APIFunction|A31| | |element macierzy.}}


{{APIFunction|A32| | |element macierzy.}}


{{APIFunction|A33| | |element macierzy.}}


{{APIFunction|A34| | |element macierzy.}}


{{APIFunction|A41| | |element macierzy.}}


{{APIFunction|A42| | |element macierzy.}}


{{APIFunction|A43| | |element macierzy.}}


{{APIFunction|A44| | |element macierzy.}}


{{APIFunction|determinant| |Oblicza [http://en.wikipedia.org/wiki/Determinant wyznacznik] macierzy|a number.}}


{{APIFunction|inverse| |[http://en.wikipedia.org/wiki/Inverse_matrix inwertuje] tę macierz, jeśli to możliwe|nothing.}}


{{APIFunction|invert| |Zwraca [http://en.wikipedia.org/wiki/Inverse_matrix odwrotność] tej macierzy, jeśli to możliwe|a Matrix}}


{{APIFunction|move|Vector|Sprawia, że ta macierz staje się macierzą [http://en.wikipedia.org/wiki/Translation_%28geometry%29 przesunięcia]|nothing.}}


{{APIFunction|multiply|Matrix or Vector|Zwraca [http://en.wikipedia.org/wiki/Cross_product iloczyn krzyżowy] macierzy lub wektora z tą macierzą|a Matrix}}


{{APIFunction|rotateX|Float(radians)|Sprawia, że ta macierz jest [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotacją] wokół transformacji X|nothing.}}


{{APIFunction|rotateY|Float(radians)|Sprawia, że ta macierz jest [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotacją] wokół transformacji Y|nothing.}}


{{APIFunction|rotateZ|Float(radians)|Sprawia, że ta macierz jest [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotacją] wokół transformacji Z|nothing.}}


{{APIFunction|scale|Vector|Tworzy z tej macierzy [http://en.wikipedia.org/wiki/Scaling_matrix transformatę skalującą]|nothing.}}


{{APIFunction|transform|Vector, Matrix|Tworzy z tej macierzy [http://en.wikipedia.org/wiki/Transformation_matrix macierz transformacji] opartą na wektorze i macierzy|nothing. }}


{{APIFunction|unity| |Sprawia, że ta macierz jest [http://en.wikipedia.org/wiki/Identity_matrix macierzą tożsamości]|nothing.}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
