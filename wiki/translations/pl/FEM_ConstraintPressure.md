---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintPressure
   Name/pl: MES Obciążenie ciśnieniem
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Obciążenie ciśnieniem
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintForce/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintPressure/pl



## Opis

Nakłada na ścianę obciążenie ciśnieniem.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintPressure.svg" width=16px> Obciążenie ciśnieniem** z menu.
2.  Wciśnij przycisk **Dodaj** i wybierz ściany w [widoku 3D](3D_view/pl.md). Opcjonalnie, wciśnij przycisk **Usuń** i kliknij na ścianach, które chcesz usunąć z zaznaczenia.
3.  Edytuj odpowiednie pole aby wprowadzić wartość ciśnienia w MPa.
4.  Zaznacz pole do odwrócenia kierunku działania ciśnienia, jeśli to konieczne.



## Uwagi

-   Rozkład ciśnienia na powierzchni jest zawsze jednorodny i prostopadły do niej.

-    {{VersionMinus/pl|0.21}}: Obciążenie ciśnieniem można zadawać na powłoki, ale tylko gdy siatka została utworzona przy pomocy generatora [Gmsh](FEM_MeshGmshFromShape/pl.md) a tworzenie grup siatki jest włączona. Opcja ta jest włączona na stałe, więc użytkownik nie musi się tym przejmować. Jednak, ze względu na błąd, obciążenie ciśnieniem może wymagać ponownego wygenerowania siatki żeby działało na powłokach.

-   To narzędzie korzysta ze [słowa kluczowego \*DLOAD w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure/pl
