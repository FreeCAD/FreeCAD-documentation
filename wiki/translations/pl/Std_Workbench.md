---
 GuiCommand:
   Name: Std Workbench
   Name/pl: Std: Środowiska pracy
   Empty: 1
   MenuLocation: Widok , Środowiska pracy
   Workbenches: wszystkie
---

# Std Workbench/pl



## Opis

Polecenie **Środowiska pracy** aktywuje wybrane [Środowisko pracy](Workbenches/pl.md).

![](images/Std_Workbench_ComboBox_Icons_And_Text.png ) 
*Domyślny typ rozwijanej listy selektora środowisk pracy.*

![](images/Std_Workbench_TabBar_Icons_Only.png ) 
*Opcjonalny typ Paska zakładek selektora środowisk pracy (tutaj wyświetlany tylko z ikonami) {{Version/pl|1.0*}}



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz środowisko pracy z listy rozwijanej lub paska zakładek ({{Version/pl|1.0}}) na pasku narzędzi Środowisko.
    -   Wciśnij przycisk **<img src="images/List-add.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** na pasku zakładek aby z wyświetlonego menu wybrać środowisko pracy, które zostało wyłączone w [preferencjach](Preferences_Editor/pl#Dostępne_środowiska_pracy.md).
    -   Wybierz środowisko pracy z menu podrzędnego **Widok → Środowiska pracy**.



## Uwagi

-   Dodatkowe [zewnętrzne środowiska pracy](External_workbenches/pl.md) mogą być pobrane za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).



## Ustawienia

Zapoznaj się z informacjami na stronie: [Edytor preferencji](Preferences_Editor/pl.md).

-   [strona z powiązanymi preferencjami](Preferences_Editor/pl#Dostępne_środowiska_pracy.md) jest dostępna: **Edycja → Preferencje... → Środowiska pracy→ Dostępne środowiska pracy**. Możesz zmienić **Startowe środowisko pracy**,**Typ selektora środowisk pracy** i więcej. Przycisk **<img src="images/List-add.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** na pasku zakładek TabBar daje dostęp do tej strony przez menu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić środowisko pracy należy użyć metody `activateWorkbench` modułu FreeCADGui.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
⏵ [documentation index](../README.md) > Std Workbench/pl
