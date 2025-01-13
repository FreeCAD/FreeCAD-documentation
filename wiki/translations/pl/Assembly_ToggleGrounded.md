---
 GuiCommand:
   Name: Assembly ToggleGrounded
   Name/pl: Złożenie Włącz / wyłącz zakotwienie
   MenuLocation: Złożenie , Włącz / wyłącz zakotwienie
   Workbenches: Assembly_Workbench/pl
   Shortcut: **G**
   Version: 1.0
   SeeAlso: 
---

# Assembly ToggleGrounded/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:16px;"> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md) blokuje położenie i orientację kształtu względem układu współrzędnych złożenia, do którego ten kształt należy.



## Użycie

1.  Wybierz jedną lub więcej części.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_ToggleGrounded.svg" width=16px> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_ToggleGrounded.svg" width=16px> Włącz / wyłącz zakotwienie** z menu.
    -   Użyj skrótu: **G**.
3.  Obiekt GroundedJoint zostaje dodany dla każdej wybrane części.



## Uwagi

-   Zakotwienie połączenia spowoduje wyświetlenie czerwonej ikony blokady w widoku 3D, wokół środka masy zakotwiczonego elementu. Aby ukryć blokadę, należy wyłączyć własciwość **Widoczność** połączenia.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **GroundedJoint** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Ma też następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Ground}}

-    **Object To Ground|Link**: Obiekt do zablokowania.

-    **Placement|Placement**: Tu część jest zakotwiona. Zobacz [Umiejscowienie](Placement/pl.md).





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly ToggleGrounded/pl
