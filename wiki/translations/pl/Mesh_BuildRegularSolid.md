---
- GuiCommand:
   Name:Mesh BuildRegularSolid
   Name/pl:Siatka Utwórz bryłę pierwotną
   MenuLocation:Siatki → Utwórz bryłę pierwotną ...
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
---

# Mesh BuildRegularSolid/pl



## Opis

Polecenie **Utwórz bryłę pierwotną** tworzy regularną parametryczną bryłę obiektu siatkowego.



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_BuildRegularSolid.svg" width=16px> '''Utwórz bryłę pierwotną'''**.
    -   Wybierz z menu opcję **Siatki → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Utwórz bryłę pierwotną ...**.
2.  Otworzy się okno dialogowe **Bryła pierwotna**.
3.  Najpierw wybierz typ obiektu siatkowego z listy rozwijanej:
4.  First select a mesh object type from the dropdown list:
    -   
        **<img src="images/Mesh_Cube.svg" width=16px> Sześcian
**
        

    -   
        **<img src="images/Mesh_Cylinder.svg" width=16px> Walec
**
        

    -   
        **<img src="images/Mesh_Cone.svg" width=16px> Stośek
**
        

    -   
        **<img src="images/Mesh_Sphere.svg" width=16px> Sfera
**
        

    -   
        **<img src="images/Mesh_Ellipsoid.svg" width=16px> Ellipsoida
**
        

    -   
        **<img src="images/Mesh_Torus.svg" width=16px> Torus
**
        
5.  Określ wymagane ustawienia. Dostępne ustawienia zależą od typu obiektu siatkowego. Zobacz [Właściwości](#W.C5.82a.C5.9Bciwo.C5.9Bci.md).
6.  Dla siatek z zakrzywionymi powierzchniami: wyższa wartość **Próbkowania** skutkuje drobniejszą siatką.
7.  Naciśnij przycisk {{button|Utwórz}}, aby utworzyć obiekt siatki.
8.  Opcjonalnie utwórz więcej obiektów siatki.
9.  Naciśnij przycisk {{button|Zamknij}}, aby zamknąć okno dialogowe i zakończyć polecenie.



## Uwagi

-   Obiekty siatkowe utworzone za pomocą tego polecenia są parametryczne. Kiedykolwiek są one ponownie obliczane, na przykład po zmianie jednego z ich parametrów, ich siatka jest rekonstruowana. Oznacza to, że manipulowanie nimi za pomocą poleceń takich jak [Ulepsz przez Gmsh](Mesh_RemeshGmsh/pl.md), [Skaluj](Mesh_Scale/pl.md) itp. zwykle nie ma sensu.



## Właściwości

Obiekty siatkowe utworzone za pomocą tego polecenia dziedziczą wszystkie właściwości typu [Cecha siatki](Mesh_Feature/pl.md). Dodatkowo każdy typ obiektu siatkowego posiada szereg właściwości pozwalających kontrolować jego parametryczne zachowanie:



### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Sześcian 



#### Dane


{{TitleProperty|Sześcian}}

-    **Wysokość|FloatConstraint**: wysokość sześcianu.

-    **Długość|FloatConstraint**: długość sześcianu.

-    **Szerokość|FloatConstraint**: szerokość sześcianu.



### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Walec 



#### Dane 


{{TitleProperty|Podstawa}}

-    **Zamknięty|Bool**: jeśli ustawiono na wartość `False`, planarne końce walca pozostają otwarte.

-    **Długość krawędzi|FloatConstraint**: długość krawędzi ścian w siatce.

-    **Długość|FloatConstraint**: długość walca.

-    **Promień|FloatConstraint**: promień walca.

-    **Próbkowanie|IntegerConstraint**: liczba ścian wzdłuż zakrzywionej powierzchni.



### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Stożek 



#### Dane 


{{TitleProperty|Podstawa}}

-    **Zamknięty|Bool**: jeśli ustawiono na wartość `False`, planarny koniec *(końce)* stożka pozostają otwarte.

-    **Długość krawędzi|FloatConstraint**: długość krawędzi ścian w siatce.

-    **Długość|FloatConstraint**: długość stożka.

-    **Promień 1|FloatConstraint**: pierwszy promień stożka. Może przyjmować wartość {{value|0}}.

-    **Promień 2|FloatConstraint**: drugi promień stożka. Może przyjmować wartość {{value|0}}.

-    **Próbkowanie|IntegerConstraint**: liczba ścian wzdłuż zakrzywionej powierzchni.



### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Sfera 



#### Dane 


{{TitleProperty|Podstawa}}

-    **Promień|FloatConstraint**: promień kuli.

-    **Próbkowanie|IntegerConstraint**: liczba ścian wzdłuż obu kierunków zakrzywionej powierzchni.



### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Ellipsoida 



#### Dane 


{{TitleProperty|Podstawa}}

-    **Promień 1|FloatConstraint**: pierwszy promień elipsy.

-    **Promień 2|FloatConstraint**: drugi promień elipsy.

-    **Próbkowanie|IntegerConstraint**: liczba ścian wzdłuż obu kierunków zakrzywionej powierzchni.

### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Torus 



#### Dane 


{{TitleProperty|Podstawa}}

-    **Promień 1|FloatConstraint**: pierwszy *(główny)* promień torusa.

-    **Promień 2|FloatConstraint**: drugi promień torusa.

-    **Próbkowanie|IntegerConstraint**: liczba ścian wzdłuż obu kierunków zakrzywionej powierzchni.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh BuildRegularSolid/pl
