 {{VeryImportantMessage|(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).}}

In FreeCAD le matrici 4x4 sono utilizzate ovunque e possono essere create con una delle seguenti modalità: 
```python
m = FreeCAD.Matrix()          # m = the [http://en.wikipedia.org/wiki/Identity_matrix identity matrix]
m = FreeCAD.Base.Matrix()
print m.A21()               # print m[1][0]
```


{{APIFunction|A| | |tutti gli elementi della matrice.}}


{{APIFunction|A11| | |un elemento della matrice.}}


{{APIFunction|A12| | |un elemento della matrice.}}


{{APIFunction|A13| | |un elemento della matrice.}}


{{APIFunction|A14| | |un elemento della matrice.}}


{{APIFunction|A21| | |un elemento della matrice.}}


{{APIFunction|A22| | |un elemento della matrice.}}


{{APIFunction|A23| | |un elemento della matrice.}}


{{APIFunction|A24| | |un elemento della matrice.}}


{{APIFunction|A31| | |un elemento della matrice.}}


{{APIFunction|A32| | |un elemento della matrice.}}


{{APIFunction|A33| | |un elemento della matrice.}}


{{APIFunction|A34| | |un elemento della matrice.}}


{{APIFunction|A41| | |un elemento della matrice.}}


{{APIFunction|A42| | |un elemento della matrice.}}


{{APIFunction|A43| | |un elemento della matrice.}}


{{APIFunction|A44| | |un elemento della matrice.}}


{{APIFunction|determinant| |Calcola il [http://en.wikipedia.org/wiki/Determinant determinante] della matrice|un numero.}}


{{APIFunction|inverse| |[http://en.wikipedia.org/wiki/Inverse_matrix Inverte] questa matrice, se è possibile|nulla.}}


{{APIFunction|invert| |Restituisce [http://en.wikipedia.org/wiki/Inverse_matrix la matrice inversa] di questa matrice, se possibile|una Matrice}}


{{APIFunction|move|Vector|Makes this matrix a [http://en.wikipedia.org/wiki/Translation_%28geometry%29 translation] matrix|nothing.}}


{{APIFunction|multiply|Matrix or Vector|Returns the [http://en.wikipedia.org/wiki/Cross_product cross product] of a matrix or vector with this matrix|a Matrix}}


{{APIFunction|rotateX|Float(radians)|Makes this matrix a [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotation] about X transform|nothing.}}


{{APIFunction|rotateY|Float(radians)|Makes this matrix a [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotation] about Y transform|nothing.}}


{{APIFunction|rotateZ|Float(radians)|Makes this matrix a [http://en.wikipedia.org/wiki/Rotation_%28mathematics%29 rotation] about Z transform|nothing.}}


{{APIFunction|scale|Vector|Makes this matrix a [http://en.wikipedia.org/wiki/Scaling_matrix scaling transform]|nothing.}}


{{APIFunction|transform|Vector, Matrix|Makes this matrix a [http://en.wikipedia.org/wiki/Transformation_matrix transformation matrix] based on Vector and Matrix|nothing. }}


{{APIFunction|unity| |Makes this matrix the [http://en.wikipedia.org/wiki/Identity_matrix identity matrix]|nothing.}}


 

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)
