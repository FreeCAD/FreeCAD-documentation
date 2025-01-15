---
 GuiCommand:
   Name: FEM CreateElementsSet
   Name/pl: Utwórz zestaw elementów
   MenuLocation: Siatka , Usuń elementy
   Workbenches: FEM_Workbench/pl
   Version: 1.0
   SeeAlso: FEM_tutorial/pl
---

# FEM CreateElementsSet/pl



## Opis

Ukrywa elementy zaznaczone wielokątem z siatki MES lub siatki wyników, umożliwiając usunięcie wybranych części siatki z widoku i zobaczenie elementów wewnątrz siatki.



## Użycie

1.  Zaznacz siatkę MES (utworzoną przy pomocy generatora Netgen/Gmsh lub zaimportowaną) lub siatkę wyników w drzewie.
2.  Wybierz opcję **Siatka → <img src="images/FEM_CreateElementsSet.svg" width=16px> Usuń elementy** z menu.
3.  Opcjonalnie, wprowadź nazwę obiektu narzędzia, który zostanie utworzony w drzewie.
4.  Wciśnij przycisk **Wielokąt** i kliknij w kilku dowolnych miejscach w widoku 3D aby zdefiniować wielokąt zaznaczania.
5.  Kliknij prawym przyciskiem myszy i wybierz *Inner* lub *Outer* (aby zdecydować czy usunięte zostaną elementy wewnątrz czy na zewnątrz wielokąta zaznaczania) bądź *Anuluj* jeśli chcesz opuścić narzędzie zaznaczania wielokątem.
6.  Wskazane elementy zostaną usunięte z siatki a liczba elementów usuniętych i zachowanych zostanie wyświetlona w oknie raportu.
7.  Wciśnij przycisk **OK**. Zauważysz nowe obiekty w drzewie - jeden o nazwie takiej jak podana (domyślnie *ElementSet*) i jeden o nazwie *NewFemMesh* lub *NewResultMesh* w zależności od typu siatki. W przypadku siatki wyników, pojawi się również kopia oryginalnej siatki nazwana *StartResultMesh*. Obiekt *ElementSet* może zostać użyty do ponownego skorzystania z narzędzia.
8.  Aby usunąć nowe obiekty z drzewa i zachować tylko oryginalną siatkę, kliknij dwukrotnie na obiekcie *ElementSet* i wciśnij przycisk **Przywróć**. Widoczność oryginalnej siatki nie zostanie przywrócona automatycznie.



## Uwagi

-   Aby ukryć więcej elementów z tej samej siatki MES po początkowym użyciu narzędzia, należy ręcznie wskazać nową (zmodyfikowaną) siatkę jako cel operacji. Nie ma takiej potrzeby w przypadku siatek wyników.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM CreateElementsSet/pl
