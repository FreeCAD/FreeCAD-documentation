---
 GuiCommand:
   Name: FEM PostApplyChanges
   Name/pl: Zastosuj zmiany
   MenuLocation: Wyniki , Zastosuj zmiany
   Workbenches: FEM_Workbench/pl
   SeeAlso: Std_Refresh/pl, FEM_PostCreateFunctions/pl
---

# FEM PostApplyChanges/pl



## Opis

Umożliwia przełączanie, czy zmiany w obiektach prezentacji graficzne wyników i filtrach są stosowane natychmiast czy nie.

Jeśli ta opcja jest aktywna, zmiany w [funkcjach filtrujących](FEM_PostCreateFunctions/pl.md) i filtrach mają natychmiastowy efekt. Jednak przy dużych siatkach wynikowych może to znacznie spowolnić pracę komputera.

Jeżeli funkcja nie jest aktywna, to zmiana rozmiaru i pozycji funkcji najpierw wywoła efekt po ponownym obliczeniu obiektu funkcji *(patrz [Odśwież](Std_Refresh/pl.md))*. W przypadku zmian w filtrach, zmiana będzie miała najpierw efekt po naciśnięciu w oknie dialogowym filtra przycisku **Zastosuj** lub po ponownym przeliczeniu filtrowanego obiektu.



## Użycie

Kliknij przycisk na pasku narzędzi **<img src="images/FEM_PostApplyChanges.svg" width=16px> '''Zastosuj zmiany'''** lub użyj menu **Wyniki → <img src="images/FEM_PostApplyChanges.svg" width=16px> Zastosuj zmiany**.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostApplyChanges/pl
