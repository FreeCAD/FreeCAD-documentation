---
 GuiCommand:
   Name: Std Workbench
   Name/pl: Std: Środowiska pracy
   Empty: 1
   MenuLocation: Widok , Środowiska pracy
   Workbenches: Workbenches/pl
---

# Std Workbench/pl



## Opis

Polecenie **Środowiska pracy** aktywuje wybrane [Środowisko pracy](Workbenches/pl.md) wraz z jego graficznym interfejsem użytkownika *(GUI)*.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*Menu rozwijane dla środowisk pracy oznaczone numerem '''10''' w standardowym [interfejsie](interface/pl.md).*



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz środowisko pracy z **rozwijanej listy środowisk pracy** na pasku narzędziowym środowiska. Opcja ta nie jest dostępna, jeśli bieżącym środowiskiem roboczym jest `<none>`. (brak środowiska pracy).
    -   Wybierz środowisko pracy z menu podrzędnego **Widok → Środowiska pracy**.



## Uwagi

-   Dodatkowe [zewnętrzne środowiska pracy](External_workbenches/pl.md) mogą być pobrane za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).



## Ustawienia

-   Rozruchowy warsztat pracy można zmienić w preferencjach: **Edycja → Preferenceje → Ogólne → Ogólne → Uruchamianie**. Zobacz też [Edytor ustawień](Preferences_Editor/pl#Informacje_og.C3.B3lne.md).



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić środowisko pracy należy użyć metody `activateWorkbench` modułu FreeCADGui. Metoda ta nie jest dostępna, jeśli FreeCAD jest uruchomiony w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
⏵ [documentation index](../README.md) > Std Workbench/pl
