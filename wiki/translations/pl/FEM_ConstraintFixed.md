---
 GuiCommand:
   Name: FEM ConstraintFixed
   Name/pl: MES Warunek brzegowy utwierdzenia
   MenuLocation:  Model , Warunki brzegowe i obciążenia mechaniczne , Warunek brzegowy utwierdzenia
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintContact/pl
---

# FEM ConstraintFixed/pl



## Opis

Tworzy warunek brzegowy MES dla utwierdzonego obiektu geometrycznego poprzez zablokowanie wszystkich dostępnych stopni swobody węzłów leżących u podstaw wybranego obiektu geometrycznego *(6 stopni swobody dla elementów belkowych i powłokowych, 3 dla elementów bryłowych)*.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintFixed.svg" width=16px> Warunek brzegowy utwierdzenia** z menu.
2.  W [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego ma być przypisany warunek brzegowy. Może to być wierzchołek, krawędź lub ściana.



## Ograniczenia

Nie możesz mieszać typów obiektów geometrycznych w obrębie tego samego warunku brzegowego. Użyj osobnego warunku utwierdzenia do każdego typu obiektu.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFixed/pl
