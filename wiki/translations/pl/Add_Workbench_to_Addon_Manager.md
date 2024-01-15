# Add Workbench to Addon Manager/pl
## Wprowadzenie

Przedstawiono tutaj instrukcje krok po kroku, jak dodać środowisko pracy Python do [Menadżera dodatków](Std_AddonMgr/pl.md).

-   Lokalne repozytorium Git.
-   Zdalne repozytorium Git. Obsługiwane hosty git to [GitHub](https://github.com), [GitLab](https://about.gitlab.com/), [Framagit](https://framagit.org/public/projects) i [Debian Salsa](https://salsa.debian.org/public).
-   Git musi być zainstalowany.



## Włącz tryb deweloperski 

1.  Otwórz [Edytor preferencji](Preferences_Editor.md): wybierz z menu opcję **Edycja → <img src="images/Std_DlgPreferences.svg" width=16px> Preferencje ...**.
2.  Wybierz opcję **<img src="images/Std_AddonMgr.svg" width=16px> Menadżer dodatków** na lewym pasku.
3.  W zakładce **Opcje menedżera dodatków** zaznacz pole wyboru **Tryb dewelopera dodatków**. Spowoduje to włączenie przycisku **Narzędzia programisty ...** w menedżerze dodatków.
4.  Naciśnij przycisk **OK**, aby zamknąć Edytor preferencji.



## Utwórz plik package.xml 

1.  Otwórz [Menadżer dodatków](Std_AddonMgr.md): wybierz opcję **Narzędzia → <img src="images/Std_AddonMgr.svg" width=16px> Menadżer dodatków** z menu.
2.  Naciśnij przycisk **Narzędzia programisty ...**.
3.  Otworzy się okno dialogowe **Narzędzia dla twórców dodatków**.
    <img alt="" src=images/Addon_Manager_Addon_Developer_Tools_Dialog.png  style="width:350px;">
4.  Wprowadź następujące dane:
    -   
        **Ścieżka do dodatku**
        
        : Ścieżka do lokalnego repozytorium git.

    -   
        **Nazwa dodatku**
        
        : Ta nazwa pojawi się na liście w menedżerze dodatków.

    -   
        **Opis**
        
        : Analogicznie.

    -   
        **Wersja**
        
        : Analogicznie.

    -   
        **URL repozytorium**
        

    -   
        **Gałąź podstawowa**
        

    -   
        **URL README**
        
        : Rekomendowane.

    -   
        **Ikonka**
        
        : Ikonka musi być częścią repozytorium.
5.  Press the **<img src="images/List-add.svg" width=16px>** przycisk na dole okna dialogowego.
6.  The **Zawartość elementu** otwiera się okno dialogowe.

<img alt="" src=images/Addon_Manager_Content_Item_Dialog.png  style="width:350px;">

1.  
    **Typ treści**powinien być ustawiony na {{Value|Workbench}}.

2.  Zaznacz pole wyboru **To jest jedyny element w dodatku**.

3.  Wpisz **Nazwa klasy środowiska pracy**. Jest to nazwa klasy określona w pliku **InitGui.py**.

4.  Dla **Katalog podrzędny** wpisz {{Value|./}}.

5.  Naciśnij przycisk **OK**, aby zamknąć okno dialogowe.

6.  Naciśnij przycisk **Zapisz**, aby zamknąć okno dialogowe **Narzędzia dla twórców dodatków** i zapisać plik **package.xml**.

7.  Naciśnij przycisk **<img src="images/Process-stop.svg" width=16px> Close**, aby zamknąć Menedżer dodatków.

8.  Prześlij utworzony plik do zdalnego repozytorium.



## Dodaj środowisko pracy do pliku .gitmodules 

1.  Utwórz rozwidlenie <https://github.com/FreeCAD/FreeCAD-addons>.
2.  Utwórz nową gałąź.
3.  Edytuj plik **.gitmodules**, aby uwzględnić nowy dodatek, w kolejności alfabetycznej.
4.  Prześlij nową gałąź do GitHub.
5.  Prześlij Pull Request do repozytorium FreeCAD-Addons z nowym plikiem **.gitmodules**.



## Zobacz również 

-   [Tworzenie środowiska pracy](Workbench_creation/pl.md)
-   [Metadane pakietu](Package_Metadata/pl.md): Szczegółowe informacje o pliku **package.xml**.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [Developer Documentation](Category_Developer Documentation.md) > Add Workbench to Addon Manager/pl
