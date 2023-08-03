---
 GuiCommand:
   Name: Mesh RemoveCompByHand
   Name/pl: Siatka: Usuń elementy Interaktywnie
   MenuLocation: Siatki , Usuń elementy ręcznie ...
   Workbenches: Mesh_Workbench/pl
   SeeAlso: Mesh_RemoveComponents/pl, Arch_SplitMesh/pl
---

# Mesh RemoveCompByHand/pl

## Opis

Polecenie **Usuń fragmenty ręcznie** usuwa wskazane elementy z obiektów siatkowych.

## Użycie

1.  Fragment odnosi się do kompletnej grupy połączonych powierzchni. Zazwyczaj obiekt siatki zawiera pojedynczy fragment. Ale, na przykład po użyciu polecenia [Scal](Mesh_Merge/pl.md), obiekt siatki może zawierać wiele fragmentów.
2.  Polecenie używa koloru czerwonego do zaznaczania wybranych fragmentów. Aby je prawidłowo zobaczyć:
    -   
        **Tryb wyświetlania**
        
        obiektów siatkowych powinien pokazywać ściany. W razie potrzeby użyj polecenia [Styl kreślenia](Std_DrawStyle/pl.md), aby nadpisać tę właściwość.

    -   
        **Kolor kształtu**
        
        obiektów siatki nie powinien być czerwony.
3.  Wybierz opcję z menu **Siatki → <img src="images/Mesh_RemoveCompByHand.svg" width=16px> Usuń fragmenty ręcznie ...**.
4.  Kursor zmienia się na ikonę dłoni.
5.  Wybierz komponenty, które chcesz usunąć w oknie [widoku 3D](3D_view/pl.md).
6.  Opcjonalnie wybierz opcję **Wyczyść zaznaczone powierzchnie** z menu podręcznego widoku 3D, aby odznaczyć wszystkie komponenty.
7.  Wybierz opcję **Usuń zaznaczone powierzchnie** z menu podręcznego widoku 3D, aby usunąć wybrane komponenty.
8.  Wybierz opcję **Opuść tryb usuwania** z menu podręcznego widoku 3D, aby zakończyć polecenie.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveCompByHand/pl
