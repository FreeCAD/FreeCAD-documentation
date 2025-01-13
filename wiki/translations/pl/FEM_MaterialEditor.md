---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MaterialEditor
   MenuLocation: Model , Materiały , Edytor materiału
   Workbenches: FEM_Workbench/pl, Arch_Workbench/pl
   Version: 0.18
   SeeAlso: Arch_SetMaterial/pl|Architektura: Wybór materiału
, FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: All
}}
---

# FEM MaterialEditor/pl



## Opis

**Edytor materiału** umożliwia edycję i zapis informacji zawartych w [materiale programu FreeCAD](Material/pl.md). Obecnie takie materiały są używane przez środowiska <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [MES](FEM_Workbench/pl.md) i <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/pl.md).

![](images/Material_editor.png )



## Użycie

Edytor materiału można obecnie uruchomić poprzezː

1.  <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Środowisko pracy BIM](BIM_Workbench/pl.md):
    -   Przycisk **<img src="images/BIM_Material.svg" width=16px> '''Wybór materiału'''**.
    -   Opcję **Architektura → Narzędzia materiałowe → <img src="images/BIM_Material.svg" width=16px> Materiał** w menu.
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [Środowisko pracy MES](FEM_Workbench/pl.md):
    -   Przycisk **<img src="images/FEM_MaterialEditor.svg" width=16px> '''Edytor materiału'''**.
    -   Opcję **Model → Materiały → <img src="images/FEM_MaterialEditor.svg" width=16px> Edytor materiału** w menu.



## Opcje

-   **Browser button**: Otwiera zawartość właściwości URL w przeglądarce.

-   **Material card**: Umożliwia wybranie predefiniowanego materiału z wypełnionymi polami.

-    **Open**: Otwiera plik .FCMat.

-    **Save as**: Zapisuje zawartość edytora jako nowy plik .FCMat

-   **Preview**: Niezaimplementowane.

-   **Properties editor**: Umożliwia edycję właściwości materiału.

-    **Add property**: Umożliwia dodanie nowej właściwości użytkownika.

-    **Delete property**: Usuwa wybraną właściwość. Tylko właściwości użytkownika mogą być usunięte.



## Uwagi

-   Przyciski **OK** i **Anuluj** mają ten sam efekt gdy Edytor materiału nie jest używany bezpośrednio do edycji właściwości materiału istniejącego obiektu.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/pl
