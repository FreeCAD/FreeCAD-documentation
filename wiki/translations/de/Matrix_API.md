# Matrix API/de

 {{VeryImportantMessage|(Oktober 2019) Diese Seite nicht ändern. Diese Information ist unvollständig und veraltet. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation] oder generiere die Dokumentation selbst, siehe [Quellendokumentation](Source_documentation/de.md).}}

4x4-Matrizen werden überall in FreeCAD verwendet und können auf eine der folgenden Weisen erstellt werden: 
```python
m = FreeCAD.Matrix()          # m = the [http://en.wikipedia.org/wiki/Identity_matrix identity matrix]
m = FreeCAD.Base.Matrix()
print m.A21()               # print m[1][0]
```


{{APIFunction|A| | |all the matrix elements.}}


{{APIFunction|A11| | |a matrix element.}}


{{APIFunction|A12| | |a matrix element.}}


{{APIFunction|A13| | |a matrix element.}}


{{APIFunction|A14| | |a matrix element.}}


{{APIFunction|A21| | |a matrix element.}}


{{APIFunction|A22| | |a matrix element.}}


{{APIFunction|A23| | |a matrix element.}}


{{APIFunction|A24| | |a matrix element.}}


{{APIFunction|A31| | |a matrix element.}}


{{APIFunction|A32| | |a matrix element.}}


{{APIFunction|A33| | |a matrix element.}}


{{APIFunction|A34| | |a matrix element.}}


{{APIFunction|A41| | |a matrix element.}}


{{APIFunction|A42| | |a matrix element.}}


{{APIFunction|A43| | |a matrix element.}}


{{APIFunction|A44| | |a matrix element.}}


{{APIFunction|determinant| |Computes the [http://en.wikipedia.org/wiki/Determinant determinant] of the matrix|a number.}}


{{APIFunction|inverse| |[http://en.wikipedia.org/wiki/Inverse_matrix Inverts] this matrix, if possible|nothing.}}


{{APIFunction|invert| |Returns the [http://en.wikipedia.org/wiki/Inverse_matrix inverse] of this matrix, if possible|a Matrix}}


{{APIFunction|move|Vector|Makes this matrix a [http://en.wikipedia.org/wiki/Translation_%28geometry%29 translation] matrix|nothing.}}


{{APIFunction|multiply|Matrix or Vector|Returns the [http://en.wikipedia.org/wiki/Cross_product cross product] of a matrix or vector with this matrix|a Matrix}}


{{APIFunction|rotateX|Float(radians)|Makes this matrix a [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotation] about X transform|nothing.}}


{{APIFunction|rotateY|Float(radians)|Makes this matrix a [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotation] about Y transform|nothing.}}


{{APIFunction|rotateZ|Float(radians)|Makes this matrix a [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotation] about Z transform|nothing.}}


{{APIFunction|scale|Vector|Makes this matrix a [http://en.wikipedia.org/wiki/Scaling_matrix scaling transform]|nothing.}}


{{APIFunction|transform|Vector, Matrix|Makes this matrix a [http://en.wikipedia.org/wiki/Transformation_matrix transformation matrix] based on Vector and Matrix|nothing. }}


{{APIFunction|unity| |Makes this matrix the [http://en.wikipedia.org/wiki/Identity_matrix identity matrix]|nothing.}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
