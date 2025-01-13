---
 GuiCommand:
   Name: Assembly CreateAssembly
   Name/pl: Złożenie Utwórz złożenie
   MenuLocation: Złożenie , Utwórz złożenie
   Workbenches: Assembly_Workbench/pl
   Shortcut: **A**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateAssembly/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Utwórz złożenie](Assembly_CreateAssembly/pl.md) tworzy bazowe złożenie (obiekt Assembly) w bieżącym dokumencie lub podzłożenie w istniejącym aktywnym złożeniu. Dokument może mieć tylko jedno bazowe złożenie.

Każdy obiekt Assembly jest domyślnie tworzony z obiektem [Origin](App_OriginGroupExtension.md) i pustym kontenerem Joints.



## Użycie

1.  Jeśli dokument ma już jedno lub więcej złożeń: aktywuj złożenie.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateAssembly.svg" width=16px> [Utwórz złożenie](Assembly_CreateAssembly/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateAssembly.svg" width=16px> Utwórz złożenie** z menu.
    -   Użyj skrótu: **A**.
3.  Zostanie utworzony nowy obiekt Assembly - w dokumencie lub w aktywowanym złożeniu.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Złożenie** lub formalnie {{Incode|Assembly::AssemblyObject}} ma następujące właściwości:



### Dane


{{TitleProperty|Base}}

-    **Type|String**:

-    **Material|Link**:

-    **Meta|Map|Hidden**:

-    **Id|String**:

-    **Uid|UUID|Hidden**:

-    **License|String**:

-    **License URL|String**:

-    **Color|Color**:

-    **Placement|Placement**:

-    **Label|String**:

-    **Label2|String|Hidden**:

-    **Expression Engine|ExpressionEngine|Hidden**:

-    **Visibility|Bool|Hidden**:

-    **Origin|Link|Hidden**:

-    **Group|LinkList**:

-    **_ Group Touched|Bool|Hidden**:



### Widok


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}} (jedyna opcja na razie).

-    **Show In Tree|Bool**: {{value|true}} domyślnie.

-    **Visibility|Bool**: {{value|true}} domyślnie.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**:

-    **Selection Style|Enumeration**:





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateAssembly/pl
