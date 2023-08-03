---
 GuiCommand:
   Name: FEM ConstraintTransform
   Name/pl: MES: Zdefiniuj odkształcenie
   MenuLocation: Model , Wiązania Geometryczne , Zdefiniuj odkształcenie
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintPlaneRotation/pl
---

# FEM ConstraintTransform/pl



## Opis

Przekształca układ współrzędnych powierzchni na określony układ współrzędnych --- prostokątny lub cylindryczny.



## Użycie

1.  Najpierw [zdefiniuj przemieszczenie](FEM_ConstraintDisplacement/pl.md) do powierzchni.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_ConstraintTransform.svg" width=16px> [Zdefiniuj odkształcenie](FEM_ConstraintTransform/pl.md)**.
    -   Wybierz opcję z menu **Model → Wiązania geometryczne → <img src="images/FEM_ConstraintTransform.svg" width=16px> Wiązanie przekształcenia**.
3.  Wybierz przekształcenie prostokątne lub cylindryczne. Pierwsza opcja może być zastosowana do każdej powierzchni, druga jest dostępna tylko dla powierzchni cylindrycznych.
4.  Wybierz powierzchnię, do której wcześniej zastosowano wiązanie przekształcenia. Naciśnij przycisk **Dodaj**.
5.  W przypadku transformacji prostokątnej należy określić obrót wokół każdej z trzech osi.



## Ograniczenia

-   Transformacja cylindryczna może być stosowana tylko do powierzchni cylindrycznych.



## Uwagi

-   To wiązanie może być stosowane do symulacji skręcania, ale tylko w przypadku prętów walcowych lub części zawierających takie pręty, używanych do przenoszenia momentu obrotowego.
-   To wiązanie wykorzystuje kartę \*TRANSFORM w programie CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/pl
