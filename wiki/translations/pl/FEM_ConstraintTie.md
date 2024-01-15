---
 GuiCommand:
   Name: FEM ConstraintTie
|Name/pɬMES Wiązanie tie
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Wiązanie tie
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure/pl
---

# FEM ConstraintTie/pl



## Opis

Definiuje wiązanie tie łączące dwie wybrane powierzchnie w taki sposób, że (w przeciwieństwie do tego jak działa kontakt) nie mogą się rozdzielić ani ślizgać po sobie podczas analizy. Są więc trwale połączone.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintTie.svg" width=16px> [Wiązanie tie](FEM_ConstraintTie/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintTie.svg" width=16px> Wiązanie tie** z menu.
2.  Wciśnij przycisk **Dodaj** w panelu zadań a następnie kliknij na ścianie, którą chcesz dodać do definicji wiązania tie. Dokładnie dwie powierzchnie muszą być dodane, jedna po drugiej.
3.  Opcjonalnie, zdefiniuj Tolerancję - wiązanie tie będzie zadane tylko na węzły oddalone od przeciwległej powierzchni o odległość nie większą niż ta podana jako tolerancja.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTie/pl
