---
 GuiCommand:
   Name: FEM ConstraintCurrentDensity
   Name/pl: MES: Warunek brzegowy gęstości prądu
   MenuLocation: Model , Warunki brzegowe elektromagnetyczne , Warunek brzegowy gęstości prądu
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_EquationMagnetodynamic/pl, FEM_EquationMagnetodynamic2D/pl
---

# FEM ConstraintCurrentDensity/pl



## Opis

Tworzy warunek brzegowy MES gęstości prądu. Używane z równaniami [magnetodynamicznym](FEM_EquationMagnetodynamic/pl.md) i [magnetodynamicznym 2D](FEM_EquationMagnetodynamic2D/pl.md).



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintCurrentDensity.svg" width=16px> [Warunek brzegowy gęstości prądu](FEM_ConstraintCurrentDensity/pl.md)** lub wybierz opcję **Model → Warunki brzegowe elektromagnetyczne → <img src="images/FEM_ConstraintCurrentDensity.svg" width=16px> Warunek brzegowy gęstości prądu** z menu.
2.  W [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego chcesz przypisać warunek brzegowy.
3.  Wciśnij przycisk **Dodaj**.



## Opcje

-   **Gęstość prądu\_\*\_1**: Część rzeczywista/urojona gęstości prądu w kierunku x w A/m². Dla układów współrzędnych innych niż kartezjański 3D, będzie to pierwsza współrzędna układu zamiast x.
-   **Gęstość prądu\_\*\_2**: Część rzeczywista/urojona gęstości prądu w kierunku y w A/m². Dla układów współrzędnych innych niż kartezjański 3D, będzie to druga współrzędna układu zamiast y.
-   **Gęstość prądu\_\*\_3**: Część rzeczywista/urojona gęstości prądu w kierunku z w A/m². Dla układów współrzędnych innych niż kartezjański 3D, będzie to trzecia współrzędna układu zamiast z. Jeśli układ współrzędnych nie ma trzeciej współrzędnej, to ustawienie zostanie zignorowane.
-   **Gęstość prądu\_\*\_\*̠nieokreślona**: Czy dany parametr ma być wyłączony (traktowany jako niewiadoma przez solver).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintCurrentDensity/pl
