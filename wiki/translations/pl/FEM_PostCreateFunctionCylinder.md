---
 GuiCommand:
   Name: FEM PostCreateFunctionCylinder
   Name/pl: Utwórz funkcję walca
   MenuLocation: Wyniki , Funkcje filtrów , Walec
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_tutorial/pl
---

# FEM PostCreateFunctionCylinder/pl



## Opis

Narzędzie <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> **Utwórz funkcję walca** określa sposób geometrycznego cięcia siatki. Jest wykorzystywane przez narzędzia <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtr cięcia funkcją](FEM_PostFilterCutFunction/pl.md) oraz <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtr przycięcia obszaru](FEM_PostFilterClipRegion/pl.md).



## Użycie



### Utwórz funkcję walca 

1.  Wciśnij przycisk **<img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> [Walec](FEM_PostCreateFunctionCylinder/pl.md)** lub wybierz opcję **Wyniki → Funkcje filtrów → <img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> Walec** z menu.
2.  [Panel zadań](Task_panel/pl.md) funkcji niejawnej zostanie otwarty.
3.  Opcjonalnie, ustaw wartości dla środka i promienia walca przekroju.
4.  Wciśnij przycisk **OK** aby zakończyć.



### Edytuj funkcję walca 

Jeśli obiekt Cylinder w [widoku drzewa](Tree_view/pl.md) jest ukryty, zaznacz <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> obiekt Cylinder w [widoku 3D](3D_view/pl.md) i wciśnij klawisz **Spacja** aby uczynić go widocznym, jak w tym przykładzie:

<img alt="" src=images/FEM_Cylinder-Cut-Function-Example.png  style="width:400px;">



#### Przesuń walec 

-   Kliknij i przeciągnij duży biały prostopadłościan aby przesunąć walec wzdłuż jego wektora normalnego.
-   Kliknij i przeciągnij białą siatkę.



#### Obróć i pochyl walec 

-   Kliknij i przeciągnij linię, która łączy małe kostki z dużym białym prostopadłościanem aby obracać i pochylać walec wokół jego początku.



#### Przeskaluj walec 

-   Kliknij i przeciągnij jedną z 6 małych kostek aby przeskalować walec.



## Uwagi

-   Istniejące funkcje mogą być użyte do różnych filtrów a nawet do różnych <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [obiektów prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Jest jednak zalecane używanie osobnego zestawu funkcji dla każdego obiektu prezentacji graficznej wyników aby mieć pod kontrolą obiekty w [widoku drzewa](Tree_view/pl.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionCylinder/pl
