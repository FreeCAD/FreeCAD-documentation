---
 GuiCommand:
   Name: CAM ToolBitLibraryOpen
   MenuLocation: CAM , Edytor biblioteki narzędzi
   Workbenches: CAM_Workbench/pl
   Version: 0.19
   SeeAlso: CAM_ToolBitDock/pl, CAM_Tools/pl, CAM_ToolBit/pl
---

# CAM ToolBitLibraryOpen/pl



## Opis

<img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:16px;"> [Edytor biblioteki narzędzi](CAM_ToolBitLibraryOpen/pl.md) to narzędzie do tworzenia, zarządzania i organizowania narzędzi. Uruchamianie menedżera biblioteki wyświetli menedżer jako okno modalne.

Stąd użytkownik może wykonywać wszystkie zadania związane z zarządzaniem końcówkami narzędzi:

-   Wybierz domyślną bibliotekę.
-   Twórz / edytuj / usuwaj końcówki narzędzi.
-   Twórz biblioteki.
-   Modyfikuj biblioteki dodając i usuwając końcówki narzędzi.
-   Zapisz bibliotekę pod nową nazwą.
-   Wyeksportuj bibliotekę do formatu biblioteki narzędzi LinuxCNC *(.tbl)*.

Tylko tworzenie nowych kształtów narzędzi nie może być wykonane z poziomu edytora biblioteki narzędzi. To złożony temat *(zobacz stronę o tworzeniu [kształtów narzędzi](CAM_ToolShape/pl.md))*.

![](images/Toolbitmanager.png )



*Edytor biblioteki narzędzi*

Panel po lewej stronie **(1)** pokazuje listę wszystkich bibliotek w bieżącym katalogu roboczym. Aktualna biblioteka jest podświetlona.

Ścieżka bieżącego katalogu roboczego jest pokazana w pasku tytułowym okna **(2)**. Narzędzie do wybierania plików **(3)** można wykorzystać do wskazania innego katalogu roboczego.

Panel po prawej stronie **(4)** pokazuje wszystkie końcówki narzędzi w obecnie wybranej bibliotece. Dwukrotne kliknięcie w lewej kolumnie pozwala zmienić domyślny numer dla tego narzędzia. Numer narzędzia będzie używany przy tworzeniu kontrolera narzędzia. Numer ten jest atrybutem biblioteki. Oznacza to, że to samo narzędzie może istnieć w wielu bibliotekach narzędzi i mieć różne domyślne numery w każdej.

Narzędzia na górze **(5)** są używane do tworzenia/dodawania/usuwania narzędzi z obecnej biblioteki.

Przycisk Zapisz jako **(6)** może być użyty do zapisania biblioteki do nowego pliku lub wyeksportowania jej do odpowiedniego formatu tabeli narzędzi. Obecnie wspierany jest tylko format LinuxCNC.

Edytor zapamięta ostatnią aktywną bibliotekę narzędzi i katalog roboczy pomiędzy użyciami.

Przycisk Zamknij **(7)** w dolnym prawym roku zamknie okno edytora biblioteki narzędzi. Wszelkie zmiany w obecnej bibliotece są zapisywane na dysku. Wciśnięcie klawisza Escape zamknie okno edytora, ale nie zostawi żadnych zmian w obecnej bibliotece. Biblioteka otwarta gdy edytor jest zamykany, stanie się nową domyślną biblioteką i będzie pokazana w tabeli narzędzi.



## Użycie

1.  Jest kilka sposobów otwarcia edytora biblioteki narzędzi:
    -   Wybierz opcję **CAM → <img src="images/CAM_ToolBitLibraryOpen.svg" width=16px> Edytor biblioteki narzędzi** z menu.
    -   Otwórz [Tabelę narzędzi](CAM_ToolBitDock/pl.md) jak opisano i wciśnij przycisk **<img src="images/Edit-edit.svg" width=16px> [Edytor biblioteki...](CAM_ToolBitLibraryOpen.md)**.
2.  Wybierz bibliotekę z listy.
3.  Twórz / dodawaj / usuwaj narzędzia z biblioteki.
4.  Kliknij wiersz dwukrotnie aby edytować narzędzie.
5.  Zamknij edytor.
6.  Wybrana biblioteka stanie się domyślną biblioteką dla tabeli narzędzi.



## Edycja narzędzi 

Jest kilka sposobów edytowania narzędzi i biblioteki:

A. Klikając nagłówki kolumn biblioteki możesz ją sortować. Biblioteka zachowa sortowanie i użyje go w tabeli narzędzi.

:   ![](images/Librarysort.png )

:   
    
*Sortuj bibliotekę narzędzi poprzez nagłówki kolumn*
    

B. Klikając dwukrotnie na pierwszej kolumnie możesz edytować numer narzędzia. Będzie to domyślny numer narzędzia używany przy tworzeniu nowego kontrolera narzędzia. Możliwe jest używanie tego samego numeru dla wielu narzędzi.

:   ![](images/Edittoolnumber.png )

:   
    
*Kliknij dwukrotnie pierwszą kolumnę aby edytować numer narzędzia*
    

C. Dwukrotne kliknięcie w dowolnym innym miejscu w rzędzie otworzy panel edycji narzędzia. Stąd możesz edytować inne właściwości narzędzia.

:   ![](images/Editingpanel.png )

:   
    
*Otwórz panel edycji narzędzia klikając w dowolnym innym miejscu w rzędzie.*
    



## Powiązane

-   [CAM: Narzędzia](CAM_Tools/pl.md)
-   [CAM: Końcówki narzędzi](CAM_ToolBit/pl.md)





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM ToolBitLibraryOpen/pl
