---
 GuiCommand:Addon/pl
   Name: BIM Library
   Name/pl: BIM: Biblioteka
   MenuLocation: Modelowanie 3D , Biblioteka
   Workbenches: Image:IFC.svg BIM Workbench/pl
   Addon: BIM
   SeeAlso: Arch Equipment/pl
---

# BIM Library/pl



## Opis

Narzędzie Biblioteka pozwala na umieszczenie w bieżącym modelu obiektu z [FreeCAD Parts Library](Biblioteka_części/pl.md), który musi być zainstalowany poprzez <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menedżera dodatków](Std_AddonMgr/pl.md), aby to narzędzie było dostępne.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;"> 
*Powyżej: Okno dialogowe '''Przeglądarka bibliotek''' w [Panel zadań](Task_panel/pl.md) po lewej stronie*



## Użycie

1.  Naciśnij przycisk **<img src="images/BIM_Library.png" width=16px> '''Biblioteka BIM'''**.
2.  Wynik: W [widoku połączonym](Combo_view/pl.md) → [Panel zadań](Task_panel/pl.md) zostanie wyświetlone okno dialogowe zatytułowane **Przeglądarka biblioteki**.
3.  Kliknij plik w przeglądarce biblioteki.
4.  Kliknij go dwukrotnie lub naciśnij przycisk **Wstaw**.
5.  Kliknij punkt w [Widoku 3D](3D_view/pl.md) lub wprowadź współrzędne ręcznie, aby umieścić obiekt.



## Opcje

-   Obsługiwane są pliki [FCStd](FCStd/pl.md), [STEP](STEP/pl.md) i [BREP](BREP/pl.md). Tylko pliki STEP i BREP można umieszczać. Pliki FCStd nie pozwalają na wybór miejsca umieszczenia, ponieważ mogą składać się ze złożonej serii obiektów o znaczących pozycjach. Po wybraniu pliku FCStd jego zawartość zostanie wstawiona w miejscu określonym w pliku.
-   Obiekty STEP i BREP są wstawiane jako <img alt="Arch_Equipment/pl" src=images/Arch_Equipment.svg  style="width:24px;"> [wyposażenie](Arch_Equipment/pl.md) bez oddzielnego kształtu bazowego. Późniejsze dodanie kształtu bazowego do tych obiektów zniszczy ich obecny kształt.
-   Podczas umieszczania obiektu można wybrać jego punkt wstawienia pomiędzy oryginalnym *(`0,0,0`)* punktem zdefiniowanym w pliku, górnym, środkowym, dolnym i lewym, środkowym i prawym.
-   Biblioteka może działać w trybie offline, w którym polega na zainstalowanym *(i aktualizowanym przez użytkownika)* dodatku Parts Library, lub online, w którym przegląda bezpośrednio z repozytorium [Parts Library Git](https://github.com/FreeCAD/FreeCAD-library) i umożliwia pobieranie bezpośrednio stamtąd.



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > BIM Library/pl
