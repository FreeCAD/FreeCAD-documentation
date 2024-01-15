---
 GuiCommand:
   Name: FEM ConstraintElectrostaticPotential
   Name/pl: MES: Warunek brzegowy potencjału elektrostatycznego
   MenuLocation: Model , Warunki brzegowe elektromagnetyczne , Warunek brzegowy potencjału elektrostatycznego
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_Example_Capacitance_Two_Balls/pl, FEM_tutorial/pl
---

# FEM ConstraintElectrostaticPotential/pl



## Opis

Tworzy warunek brzegowy MES dla potencjału elektrostatycznego. Używane z równaniem [elektrostatycznym](FEM_EquationElectrostatic/pl.md) lub [siły elektrostatycznej](FEM_EquationElectricforce/pl.md).



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> '''Warunek brzegowy potencjału elektrostatycznego'''** lub użyj opcji **Model → Warunki brzegowe elektromagnetyczne → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Warunek brzegowy potencjału elektrostatycznego** z menu.
2.  W oknie [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego chcesz przypisać warunek brzegowy.
3.  Wciśnij przycisk **Dodaj**.



## Opcje

To okno dialogowe zawiera następujące ustawienia:

![](images/FEM_ElectrostaticPotential_dialog.png )

-   **Potencjał**: Potencjał elektryczny w V.
-   *nieokreślony*\': Aby zadeklarować potencjał jako niewiadomą dla solvera.
-   **Pole wektorowe**: Aby aktywować wprowadzanie składowych pola wektorowego potencjału.
-   **x**: Rzeczywista / urojona część potencjału w kierunku x w V.
    Dla innych układów współrzędnych niż kartezjański 3D, to będzie pierwsza współrzędna układu zamiast x.
-   **y**: Rzeczywista/urojona część potencjału w kierunku y w V.
    Dla innych układów współrzędnych niż kartezjański 3D, to będzie druga współrzędna układu zamiast y.
-   **z**: Rzeczywista / urojona część potencjału w kierunku z w V.
    Dla innych układów współrzędnych niż kartezjański 3D, to będzie trzecia współrzędna układu zamiast z. Jeśli układ nie ma trzeciej współrzędnej, to ustawienie zostanie zignorowane.
-   **pola wyboru obok x, y, z**: Aby zadeklarować potencjał w danym kierunku jako niewiadomą dla solvera.
-   **Definicja potencjału elektrostatycznego**: Opcja ustawienia stałego potencjału.
-   **Dalekie pole / nieskończoność elektryczna**: Opcja założenia, że sferyczna objętość wokół powierzchni rozciąga się w nieskończoność.
-   **Oblicz siłę elektrostatyczną**: Opcja włączenia obliczeń siły elektrycznej przy użyciu [równania siły elektrostatycznej](FEM_EquationElectricforce/pl.md).
-   **Jednostka przepustowa:**: Licznik ciała *(lub powierzchni)* z pojemnością.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/pl
