# Placement API/pl
**''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

W FreeCAD, umiejscowienie definiuje pozycję i obrót obiektu. Koncepcja umiejscowienia jest szczegółowo wyjaśniona na tej stronie: [Umiejscowienie](Placement/pl.md).

Przykład ustawienia Umiejscowienia obiektu dokumentu: 
```python
myObj = FreeCAD.ActiveDocument.ActiveObject
pl = FreeCAD.Placement()
pl.move(FreeCAD.Vector(2,0,0))
myObj.Placement = pl
```


{{APIClass|Placement| ) lub (Placement) lub (Matrix) lub (Base, Rotation) lub (Base,Rotation,Center) lub (Base,Axis,Angle|Konstruuje umiejscowienie, puste lub z podanymi argumentami, lub jako kopię podanego umiejscowienia.}}


{{APIProperty|Base|wektor reprezentujący położenie umiejscowienia.}}


{{APIProperty|Rotation|czworościan reprezentujący obrót umiejscowienia.}}


{{APIFunction|inverse| |oblicza odwrotność umiejscowienia|umiejscowienie}}


{{APIFunction|move|Vector|przesuwa umiejscowienie wzdłuż podanego wektora|}}


{{APIFunction|multVec|Vector|stosuje umiejscowienie do podanego wektora|wektor wynikowy}}


{{APIFunction|multiply|Placement|zwielokrotnia to umiejscowienie|wynikające umiejscowienie}}


{{APIFunction|toMatrix| | |macierz reprezentująca transformację umiejscowienia}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Placement API/pl
