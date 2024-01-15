---
 GuiCommand:
   Name: FEM PostCreateFunctionBox
   Name/pl: Utwórz funkcję prostopadłościanu
   MenuLocation: Wyniki , Funkcje filtrów , Prostopadłościan
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_tutorial/pl
---

# FEM PostCreateFunctionBox/pl



## Opis

Narzędzie <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> **Utwórz funkcję prostopadłościanu** określa sposób geometrycznego cięcia siatki. Jest wykorzystywane przez narzędzia <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtr cięcia funkcją](FEM_PostFilterCutFunction/pl.md) oraz <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtr przycięcia obszaru](FEM_PostFilterClipRegion/pl.md).



## Użycie



### Utwórz funkcję prostopadłościanu 

1.  Wciśnij przycisk **<img src="images/FEM_PostCreateFunctionBox.svg" width=16px> [Prostopadłościan](FEM_PostCreateFunctionBox/pl.md)** lub wybierz opcję **Wyniki → Funkcje filtrów → <img src="images/FEM_PostCreateFunctionBox.svg" width=16px> Prostopadłościan** z menu.
2.  [Panel zadań](Task_panel/pl.md) funkcji niejawnej zostanie otwarty.
3.  Opcjonalnie, ustaw wartości dla środka i rozmiaru prostopadłościanu przekroju.
4.  Wciśnij przycisk **OK** aby zakończyć.



### Edytuj funkcję prostopadłościanu 

Jeśli obiekt Box w [widoku drzewa](Tree_view/pl.md) jest ukryty, zaznacz <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> obiekt Box w [widoku 3D](3D_view/pl.md) i wciśnij klawisz **Spacja** aby uczynić go widocznym, jak w tym przykładzie:

<img alt="" src=images/FEM_Box-Cut-Function-Example.png  style="width:400px;">



#### Przesuń prostopadłościan 

-   Kliknij i przeciągnij ścianę prostopadłościanu. Prostopadłościan jest definiowany przez niebieskie krawędzie.



#### Obróć i pochyl prostopadłościan 

-   Kliknij i przeciągnij jedną z 3 linii, które przechodzą przez prostopadłościan aby go obrócić i pochylić wokół jego środka.



#### Przeskaluj prostopadłościan 

-   Kliknij i przeciągnij jedną z 8 małych kostek w narożnikach prostopadłościanu aby go przeskalować.



#### Przekształć prostopadłościan 

-   Kliknij i przeciągnij jedną z 6 małych kostek wokół środka prostopadłościanu aby zmienić jego kształt.



## Uwagi

-   Istniejące funkcje mogą być użyte do różnych filtrów a nawet do różnych <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [obiektów prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Jest jednak zalecane używanie osobnego zestawu funkcji dla każdego obiektu prezentacji graficznej wyników aby mieć pod kontrolą obiekty w [widoku drzewa](Tree_view/pl.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionBox/pl
