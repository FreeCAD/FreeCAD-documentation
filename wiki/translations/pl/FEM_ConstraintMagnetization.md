---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintMagnetization
   Name/pl: MES: Warunek brzegowy magnetyzacji
   MenuLocation: Model , Warunki brzegowe elektromagnetyczne , Warunek brzegowy magnetyzacji
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_EquationMagnetodynamic/pl, FEM_EquationMagnetodynamic2D/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Elmer
}}
---

# FEM ConstraintMagnetization/pl



## Opis

Tworzy warunek brzegowy MES magnetyzacji. Używane z równaniem [magnetodynamicznym](FEM_EquationMagnetodynamic/pl.md) i [magnetodynamicznym 2D](FEM_EquationMagnetodynamic2D/pl.md).



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintMagnetization.svg" width=16px> [Warunek brzegowy magnetyzacji](FEM_ConstraintMagnetization/pl.md)** lub użyj opcji **Model → Warunki brzegowe elektromagnetyczne → <img src="images/FEM_ConstraintMagnetization.svg" width=16px> Warunek brzegowy magnetyzacji** z menu.
2.  Wciśnij przycisk **Dodaj**.
3.  W [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego ma być przypisany warunek brzegowy.



## Opcje

-   **Magnetyzacja\*\_1**: Część rzeczywista/urojona magnetyzacji w kierunku x w A/m. Dla układów współrzędnych innych niż kartezjański 3D, będzie to pierwsza współrzędna układu zamiast x.
-   **Magnetyzacja\*\_2**: Część rzeczywista/urojona magnetyzacji w kierunku y w A/m. Dla układów współrzędnych innych niż kartezjański 3D, będzie to druga współrzędna układu zamiast y.
-   **Magnetyzacja\*\_3**: Część rzeczywista/urojona magnetyzacji w kierunku z w A/m. Dla układów współrzędnych innych niż kartezjański 3D, będzie to trzecia współrzędna układu zamiast z. Jeśli układ współrzędnych nie ma trzeciej współrzędnej, to ustawienie zostanie zignorowane.
-   **Magnetyzacja\*\_\*\_nieokreślona**: Czy dany parametr ma być wyłączony (traktowany jako niewiadoma przez solver).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintMagnetization/pl
