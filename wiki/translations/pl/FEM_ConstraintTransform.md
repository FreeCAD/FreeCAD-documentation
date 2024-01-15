---
 GuiCommand:
   Name: FEM ConstraintTransform
   Name/pl: MES: Wiązanie MPC typu płaszczyzna
   MenuLocation: Model , Cechy geometryczne analizy , Lokalny układ współrzędnych
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintPlaneRotation/pl
---

# FEM ConstraintTransform/pl



## Opis

Przekształca układ współrzędnych powierzchni na określony układ współrzędnych --- prostokątny lub cylindryczny.



## Użycie

1.  Najpierw zdefiniuj [warunek brzegowy przemieszczenia](FEM_ConstraintDisplacement/pl.md) dla powierzchni.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_ConstraintTransform.svg" width=16px> '''Lokalny układ współrzędnych'''**.
    -   Wybierz opcję z menu **Model → Funkcje analizy geometrycznej → <img src="images/FEM_ConstraintTransform.svg" width=16px> Lokalny układ współrzędnych**.
3.  Wybierz przekształcenie prostokątne lub cylindryczne. Pierwsza opcja może być zastosowana do każdej powierzchni, druga jest dostępna tylko dla powierzchni cylindrycznych.
4.  Wybierz powierzchnię, do której wcześniej zastosowano warunek brzegowy przemieszczenia. Naciśnij przycisk **Dodaj**.
5.  W przypadku transformacji prostokątnej, należy określić obrót wokół każdej z trzech osi.



## Ograniczenia

-   Transformacja cylindryczna może być stosowana tylko do powierzchni cylindrycznych.



## Uwagi

-   To narzędzie może być stosowane do symulacji skręcania, ale tylko w przypadku prętów walcowych lub części zawierających takie pręty w celu przenoszenia momentu obrotowego.
-   To narzędzie wykorzystuje słowo kluczowe \*TRANSFORM w CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/pl
