# Draft annotation scale widget/pl
## Opis

**Widżet skalowania adnotacji** może być użyty do określenia skali adnotacji wersji roboczej. Skala ta określa mnożnik **Mnożnik skali** nowego obiektu [Adnotacja wieloliniowa](Draft_Text/pl.md), [Wymiar](Draft_Dimension/pl.md) i [Etykieta](Draft_Label/pl.md). Widżet jest dostępny tylko w środowiska <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md). Jest to [opcjonalny](##Ustawienia.md) element GUI, który znajduje się w [pasku statusu](Status_bar/pl.md).

![](images/Draft_annotation_scale_widget_button.png ) 
*Widżet skali adnotacji środowiska Rysunek Roboczy.*



## Użycie

1.  Naciśnij przycisk **x:x** na [pasku statusu](Status_bar/pl.md). Przycisk wyświetla bieżącą skalę adnotacji.
2.  Otworzy się menu skali.
3.  Wykonaj jedną z następujących czynności:
    -   Wybierz jedną ze standardowych skal.
    -   Wybierz opcję **Użytkownika**:
        -   W otwartym oknie dialogowym wprowadź skalę niestandardową, używając formatu {{Value|x:x}} lub {{Value|x<nowiki>=</nowiki>x}}.
        -   Naciśnij **Enter** lub przycisk **OK**.

![](images/Draft_annotation_scale_widget_menu.png ) 
*Menu widżetu.*



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Widżet skali adnotacji Rysunku Roboczego jest opcjonalny: **Edycja → Preferencje ... → Rysunek Roboczy → Interfejs → Pokaż widżet skali adnotacji środowiska Rysunek Roboczy**.
-   Aby zmienić skalę adnotacji bez widżetu: **Przybory → Edycja parametrów ... → BaseApp → Preferencje → Mod → Draft → DraftAnnotationScale**. Skala jest definiowana przez pojedynczą liczbę. Dla skali {{Value|1:50}} wpisz {{Value|0.02}}.



## Uwagi

-   Zobacz także: [Ustaw style](Draft_SetStyle/pl.md) i [Zastosuj bieżący styl](Draft_ApplyStyle/pl.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft annotation scale widget/pl
