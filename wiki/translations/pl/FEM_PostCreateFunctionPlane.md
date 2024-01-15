---
 GuiCommand:
   Name: FEM PostCreateFunctionPlane
   Name/pl: Utwórz funkcję płaszczyzny
   MenuLocation: Wyniki , Funkcje filtrów , Płaszczyzna
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM PostCreateFunctionPlane/pl



## Opis

Narzędzie <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> **Utwórz funkcję płaszczyzny** określa sposób geometrycznego cięcia siatki. Jest wykorzystywane przez narzędzia <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtr cięcia funkcją](FEM_PostFilterCutFunction/pl.md) oraz <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtr przycięcia obszaru](FEM_PostFilterClipRegion/pl.md).



## Użycie



### Utwórz funkcję płaszczyzny 

1.  Wciśnij przycisk **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> [Płaszczyzna](FEM_PostCreateFunctionPlane/pl.md)** lub wybierz opcję **Wyniki → Funkcje filtrów → <img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Płaszczyzna** z menu.
2.  [Panel zadań](Task_panel/pl.md) funkcji niejawnej zostanie otwarty.
3.  Opcjonalnie, ustaw wartości dla początku i kierunku płaszczyzny przekroju.
4.  Wciśnij przycisk **OK** aby zakończyć.



### Edytuj funkcję płaszczyzny 

Jeśli obiekt Plane w [widoku 3D](3D_view/pl.md) jest ukryty, zaznacz <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> obiekt Plane w [widoku drzewa](Tree_view/pl.md) i wciśnij klawisz **Spacja** aby uczynić go widocznym, jak w tym przykładzie:

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width:300px;">



#### Przesuń płaszczyznę 

-   Kliknij i przeciągnij duży biały prostopadłościan aby przesunąć płaszczyznę wzdłuż jej wektora normalnego.
-   Kliknij i przeciągnij białą siatkę .



#### Obróć i pochyl płaszczyznę 

-   Kliknij i przeciągnij linię, która łączy małe kostki z dużym białym prostopadłościanem aby obracać i pochylać płaszczyznę wokół jej początku.



#### Przeskaluj płaszczyznę 

-   Kliknij i przeciągnij jedną z 6 małych kostek aby przeskalować płaszczyznę. Jednak, ponieważ obiekt jest nieskończoną płaszczyzną, jego rozmiar nie ma znaczenia.



## Uwagi

-   Istniejące funkcje mogą być użyte do różnych filtrów a nawet do różnych <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [obiektów prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Jest jednak zalecane używanie osobnego zestawu funkcji dla każdego obiektu prezentacji graficznej wyników aby mieć pod kontrolą obiekty w [widoku drzewa](Tree_view/pl.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionPlane/pl
