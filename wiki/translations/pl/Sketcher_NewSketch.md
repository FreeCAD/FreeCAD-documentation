---
 GuiCommand:
   Name: Sketcher NewSketch
   Name/pl: Szkicownik: Utwórz szkic
   MenuLocation: Szkic , Utwórz szkic
   Workbenches: Sketcher_Workbench/pl
   SeeAlso: PartDesign_NewSketch/pl, Sketcher_ReorientSketch/pl
---

# Sketcher NewSketch/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> **Utwórz szkic** tworzy nowy szkic i otwiera [okno dialogowe](Sketcher_Dialog/pl.md) edycji.

Należy pamiętać, że środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md) ma własne polecenie [utwórz szkic](PartDesign_NewSketch/pl.md), podczas pracy z obiektem [Projekt Części: Zawartość](PartDesign_Body/pl.md) zaleca się używanie tego narzędzia.



## Użycie

1.  Jeśli szkic powinien być [dołączony](Part_EditAttachment/pl.md) do istniejącej geometrii: wybierz obiekt z kształtem, lub jeden lub więcej wierzchołków, krawędzi, i / lub ścian, oraz / lub płaszczyznę.
2.  Istnieje kilka sposobów, aby uruchomić narzędzie:
    -   Kliknij przycisk **<img src="images/Sketcher_NewSketch.svg" width=16px> [Utwórz szkic](Sketcher_NewSketch/pl.md)**.
    -   Wybierz opcję z menu **Szkic → <img src="images/Sketcher_NewSketch.svg" width=16px> Utwórz szkic**.
3.  Jeśli została wybrana geometria:
    1.  Otwiera się okno dialogowe **Dołączanie szkicu**.
    2.  Wybierz [metodę dołączania](Part_EditAttachment/pl#Tryby_dołączenia.md) z listy rozwijanej. Lub wybierz **Nie dołączaj**, aby zignorować wybór.
    3.  Naciśnij przycisk **OK**.
4.  Jeśli nie dokonano wyboru, lub w poprzednim kroku została wybrana opcja **Nie dołączaj**:
    1.  Otwiera się okno dialogowe **Wybierz orientację**.
    2.  Określ płaszczyznę dla orientacji. Płaszczyzna jest względem lokalnego układu współrzędnych, w którym znajduje się szkic:
        -   Jeśli pole wyboru **Odwróć kierunek** nie jest zaznaczone:
            -   Góra: **Płaszczyzna XY**
            -   Przód: **Płaszczyzna XZ**
            -   Prawo: **Płaszczyzna YZ**
        -   Jeśli pole wyboru **Odwróć kierunek** jest zaznaczone:
            -   Dół: **Płaszczyzna XY**
            -   Tył: **Płaszczyzna XZ**
            -   Lewo: **Płaszczyzna YZ**
    3.  Opcjonalnie zmień **Odsunięcie**. Odsunięcie jest mierzone wzdłuż osi Z, Y lub X lokalnego układu współrzędnych.
    4.  Naciśnij przycisk **OK**.
5.  Tworzony jest szkic.
6.  Szkic jest ustawiany w trybie edycji i otwiera się [okno dialogowe](Sketcher_Dialog/pl.md) szkicownika.
7.  Aby zakończyć tryb edycji, zobacz informacje na stronie <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Zamknij szkic](Sketcher_LeaveSketch/pl.md).



## Uwagi

-   Istniejące szkice mogą być dołączane do *(różnych)* obiektów za pomocą narzędzia [Mapuj szkic na powierzchnię](Sketcher_MapSketch/pl.md) lub odłączane i reorientowane za pomocą narzędzia [Zmień orientacje szkicu](Sketcher_ReorientSketch/pl.md).





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/pl
