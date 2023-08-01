---
- GuiCommand:
   Name:Mesh Difference
   Name/pl:Siatka Różnica
   MenuLocation:Siatki → Operacje logiczne → Różnica
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Połączenie](Mesh_Union/pl.md), [Przecięcie](Mesh_Intersection/pl.md)
---

# Mesh Difference/pl

## Opis

Polecenie **Różnica**\' tworzy nowy nieparametryczny obiekt siatkowy [cecha siatki](Mesh_Feature/pl.md), który jest różnicą dwóch obiektów siatkowych: jeden obiekt siatkowy jest wycięty z drugiego.

[OpenSCAD](http://www.openscad.org/) musi być zainstalowany, aby użyć tego polecenia, a ścieżka do jego pliku wykonywalnego musi być ustawiona w [ustawieniach OpenSCAD](OpenSCAD_Preferences/pl.md).

![](images/Mesh_Difference_example.png ) 
*Po lewej dwa obiekty siatkowe, po prawej obiekt siatkowy, który jest różnicą tych obiektów, jeśli sześcian jest wybrany jako obiekt główny.*

## Użycie

1.  Wybierz główny obiekt siatki.
2.  Dodaj do zaznaczenia obiekt siatkowy, który chcesz wyciąć z głównego obiektu. Obiekty siatkowe muszą się pokrywać.
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_Difference.svg" width=16px> '''Różnica'''**.
    -   Wybierz z menu opcję **Siatki → Operacje logiczne → <img src="images/Mesh_Difference.svg" width=16px> Różnica**.

## Właściwości

Zapoznaj się z informacjami na stronie: [cecha siatki](Mesh_Feature/pl.md).





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Difference/pl
