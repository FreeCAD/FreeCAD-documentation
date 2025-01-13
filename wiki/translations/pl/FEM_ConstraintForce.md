---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintForce
   Name/pl: MES Obciążenie siłą
   MenuLocation:  Model , Warunki brzegowe i obciążenia mechaniczne , Obciążenie siłą
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintPressure/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Wszystkie
}}
---

# FEM ConstraintForce/pl



## Opis

Przykłada siłę o określonej wartości \[N\] do wskazanej geometrii.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintForce.svg" width=16px> [Obciążenie siłą](FEM_ConstraintForce/pl.md)
**
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintForce.svg" width=16px> Obciążenie siłą** z menu.
2.  Obiekt siatki zostanie automatycznie ukryty, pokazując geometrię modelu. Jeśli obiekt siatki jest nadal widoczny, wykonaj jeden z poniższych kroków aby go ukryćː
    -   Wybierz obiekt siatki z [widoku drzewa](Tree_view/pl.md) i wciśnij klawisz **spacja**.
    -   Kliknij prawym przyciskiem myszy na obiekcie siatki w [widoku drzewa](Tree_view/pl.md) i wybierz **Ukryj zaznaczone** z menu kontekstowego.
3.  Okno dialogowe **Parametry cech analizy** w [panelu zadań](Task_panel/pl.md) również zostało otwarte.
4.  Wciśnij przycisk **Dodaj** i wybierz jeden lub więcej obiektów typu *ściany*, *krawędzie* lub *wierzchołki* w [widoku 3D](3D_view/pl.md) aby przypisać do nich siłę. Wybrane obiektu pojawią się na liście.
5.  Opcjonalnie, wciśnij przycisk **Usuń** i odznacz jeden lub więcej obiektów w [widoku 3D](3D_view/pl.md). Odznaczone obiekty zostaną usunięte z listy.
6.  Wprowadź wartość **Siła** w \[N\].
7.  Opcjonalnie, wybierz ścianę lub krawędź i wciśnij przycisk **Kierunek** aby zmienić kierunek działania siły. Często pole to zostaje puste aby siła działała w kierunku normalnym.
8.  Opcjonalnie, zaznacz pole **Odwróć kierunek** aby zmienić wektor siły.
9.  Wciśnij przycisk **OK** aby zakończyć.

![](images/FEM_ConstraintForce_example.JPG )



## Uwagi

-   Zdefiniowana siła jest rozkładana równomiernie na wskazanych obiektach. Przykładowo, zdefiniowanie jednego obciążenia siłą o wartości 200 N przyłożonego do dwóch ścian o tej samej powierzchni sprawi, że każda ze ścian będzie obciążona siłą 100 N.
-   To narzędzie korzysta ze [słowa kluczowego \*CLOAD w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node172.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintForce/pl
