---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintTransform
   Name/pl: MES: Wiązanie MPC typu płaszczyzna
   MenuLocation: Model , Cechy geometryczne analizy , Lokalny układ współrzędnych
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintPlaneRotation/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ConstraintTransform/pl



## Opis

Przekształca układ współrzędnych powierzchni na układ współrzędnych użytkownika --- prostokątny lub cylindryczny. Ten układ współrzędnych wpływa na definicje warunków brzegowych i obciążeń. Przykładowo, możesz z niego skorzystać by zablokować przemieszczenia w kierunku normalnym do pochylonej powierzchni. Wybierz tylko odpowiednią składową w [warunku brzegowym przemieszczenia](FEM_ConstraintDisplacement/pl.md).



## Użycie

1.  Najpierw zdefiniuj [warunek brzegowy przemieszczenia](FEM_ConstraintDisplacement/pl.md) dla powierzchni.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_ConstraintTransform.svg" width=16px> '''Lokalny układ współrzędnych'''**.
    -   Wybierz opcję z menu **Model → Funkcje analizy geometrycznej → <img src="images/FEM_ConstraintTransform.svg" width=16px> Lokalny układ współrzędnych**.
3.  Wybierz przekształcenie prostokątne lub cylindryczne. Pierwsza opcja może być zastosowana do każdej powierzchni, druga jest dostępna tylko dla powierzchni cylindrycznych.
4.  Wybierz powierzchnię, do której wcześniej zastosowano warunek brzegowy przemieszczenia. Naciśnij przycisk **Dodaj**.
5.  W przypadku transformacji prostokątnej, należy określić obrót wokół każdej z trzech osi. Strzałki wyświetlane na ścianie wskazują nowe kierunku (X - czerwona, Y - zielona, Z - niebieska).



## Ograniczenia

-   Transformacja cylindryczna może być stosowana tylko do powierzchni cylindrycznych.



## Uwagi

-   To narzędzie może być stosowane do symulacji skręcania, ale tylko w przypadku prętów walcowych lub części zawierających takie pręty w celu przenoszenia momentu obrotowego.
-   To narzędzie wykorzystuje [słowo kluczowe \*TRANSFORM w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node253.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/pl
