---
 GuiCommand:
   Name: FEM PostCreateFunctionSphere
   Name/pl: Utwórz funkcję sfery
   MenuLocation: Wyniki , Funkcje filtrów , Sfera
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM PostCreateFunctionSphere/pl



## Opis

Narzędzie <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:24px;"> **Utwórz funkcję sfery** określa sposób geometrycznego cięcia siatki. Jest ono wykorzystywane przez narzędzia <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtr cięcia funkcją](FEM_PostFilterCutFunction/pl.md) oraz <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtr przycięcia obszaru](FEM_PostFilterClipRegion/pl.md).



## Użycie



### Utwórz funkcję sfery 

1.  Wciśnij przycisk **<img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> [Sfera](FEM_PostCreateFunctionSphere/pl.md)** lub wybierz opcję **Wyniki → Funkcje filtrów → <img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> Sfera** z menu.
2.  [Panel zadań](Task_panel/pl.md) funkcji niejawnej zostanie otwarty.
3.  Opcjonalnie, ustaw wartości dla początku i promienia sfery przekroju.
4.  Wciśnij przycisk **OK** aby zakończyć.



### Edytuj funkcję sfery 

Jeśli obiekt Sphere w [widoku drzewa](Tree_view/pl.md) jest ukryty, zaznacz <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:24px;"> obiekt Sphere w oknie [widoku 3D](3D_view/pl.md) i wciśnij klawisz **Spacja** aby uczynić go widocznym, jak w tym przykładzie:

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width:400px;">



#### Przesuń sferę 

-   Kliknij i przeciągnij sferyczną siatkę aby przesunąć sferę.



#### Przeskaluj sferę 

-   Kliknij i przeciągnij jedną z 8 małych kostek aby przeskalować sferę.



## Uwagi

-   Istniejące funkcje mogą być użyte do różnych filtrów a nawet do różnych <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [obiektów prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Jest jednak zalecane używanie osobnego zestawu funkcji dla każdego obiektu prezentacji graficznej wyników aby mieć pod kontrolą obiekty w [widoku drzewa](Tree_view/pl.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionSphere/pl
