---
- GuiCommand:
   Name: Mesh_RemoveComponents
   Name/pl: Siatka: Usuń fragmenty
   MenuLocation: Siatki - Usuń fragmenty ...
   Workbenches: [Siatka](Mesh_Workbench/pl.md)
   SeeAlso: [Usuń elementy interaktywnie](Mesh_RemoveCompByHand/pl.md), [Podziel siatkę](Arch_SplitMesh/pl.md)
---

# Mesh RemoveComponents/pl

## Opis

Polecenie **Usuń fragmenty** usuwa ściany z obiektów siatkowych.

![](images/Meshes_RemoveComponents.jpg ) 
*Panel zadań Usuń fragmenty*

## Użycie

1.  Polecenie używa koloru czerwonego do zaznaczenia wybranych ścian. Aby zobaczyć je poprawnie:
    -   
        **Tryb wyświetlania**
        
        obiektów siatki powinien być ustawiony na {{Value|Linie płaskie}}, ale powinien przynajmniej pokazywać ściany. W razie potrzeby użyj polecenia [Styl kreślenia](Std_DrawStyle/pl.md), aby nadpisać tę właściwość.

    -   
        **Kolor kształtu**
        
        obiektów siatki nie powinien być czerwony.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_RemoveComponents.svg" width=16px> [Usuń fragmenty ...](Mesh_RemoveComponents/pl.md)**.
    -   Wybierz z menu opcję **Siatki → <img src="images/Mesh_RemoveComponents.svg" width=16px> Usuń fragmenty ...**.
3.  Otwiera się panel zadań **Usuń fragmenty**.
4.  Użyj jednej lub więcej opcji **Wybierz**, aby wybrać ściany:
    -   Naciśnij przycisk **Obszar** i trzymając wciśnięty lewy przycisk myszki narysuj zakres, zamkniętą łamaną w oknie [widoku 3D](3D_view/pl.md). Zostaną wybrane ściany, które pasują do opcji **Obszar** i *(częściowo)* mieszczą się wewnątrz regionu.
    -   Naciśnij przycisk **Wszystkie**, aby wybrać wszystkie ściany.
    -   Naciśnij przycisk **Fragmenty**, aby wybrać wszystkie fragmenty z mniejszą niż określona maksymalną liczbą powierzchni. W tym miejscu fragment odnosi się do kompletnej grupy połączonych powierzchni. Zazwyczaj obiekt siatki zawiera pojedynczy fragment. Ale, na przykład po użyciu polecenia [Scal](Mesh_Merge/pl.md), obiekt siatki może zawierać wiele fragmentów.
    -   Naciśnij przycisk **Wybierz trójkąt**, aby wybrać pojedynczą ściankę w widoku 3D. Jeśli opcja **Akceptuj tylko widoczne trójkąty** jest zaznaczona, wybranie ścian spowoduje wybranie całego fragmentu, do którego należy ściana.
5.  Opcjonalnie użyj jednej lub więcej opcji **Odznacz** aby odznaczyć ściany. Opcje te są identyczne jak opcje **Zaznacz**, z wyjątkiem tego, że liczba ścian dla przycisku **Fragmenty** jest liczbą minimalną.
6.  Opcjonalnie naciśnij przycisk **Odwróć wybór**, aby odwrócić wybór.
7.  Naciśnij przycisk **Usuń**, aby usunąć wybrane ściany.
8.  Naciśnij przycisk **Zamknij**, aby zamknąć panel zadań i zakończyć wykonywanie polecenia.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveComponents/pl
