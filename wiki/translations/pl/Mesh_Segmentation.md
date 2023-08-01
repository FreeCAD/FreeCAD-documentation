---
- GuiCommand:
   Name:Mesh Segmentation
   Name/pl:Siatki Utwórz segmenty siatki
   MenuLocation:Siatki - Utwórz segmenty siatki ...
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Utwórz segmenty z najlepiej dopasowanych powierzchni](Mesh_SegmentationBestFit/pl.md)
---

# Mesh Segmentation/pl

## Opis

Polecenie **Utwórz segmenty siatki** tworzy oddzielne segmenty siatki dla określonych typów powierzchni obiektu siatkowego.

## Użycie

1.  Zaznacz pojedynczy obiekt siatki.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Mesh_Segmentation.svg" width=16px> [Utwórz segmenty siatki](Mesh_Segmentation/pl.md)**.
    -   Wybierz z menu polecenie **Siatki → <img src="images/Mesh_Segmentation.svg" width=16px> Utwórz segmenty siatki ...**.
3.  Otworzy się panel zadań **Segmentacja siatki**.
4.  Opcjonalnie zaznacz **Wygładź siatkę** i określ wartość gładkości siatki. Im wyższa wartość, tym gładsza będzie siatka. Podanie wartości {{Value|0}} ma taki sam efekt jak odznaczenie tej opcji. Nie zaznaczaj tej opcji, jeśli chcesz tworzyć segmenty planarne.
5.  Wybierz typ powierzchni, dla której chcesz utworzyć segmenty siatki. Możesz wybrać więcej niż jeden typ, ale może to prowadzić do gorszych rezultatów. Dostępne typy powierzchni to:
    -   
        **Płaszczyzna**
        

    -   
        **Walec**
        

    -   
        **Sfera**
        

    -   
        **Układ dowolny**
        
6.  Określ wymagane ustawienia. Upewnij się, że wartości **Tolerancji** nie są zbyt niskie, a wartości **Minimalna liczba płaszczyzn** nie są zbyt wysokie.
7.  Naciśnij przycisk **OK**.
8.  Polecenie utworzy [grupę](Std_Group/pl.md) zawierającą oddzielne obiekty siatkowe, każdy będący segmentem oryginalnego obiektu siatkowego.
9.  Jeśli utworzona grupa jest pusta spróbuj użyć polecenia ponownie ze zmienionymi ustawieniami.

## Uwagi

-   Obecna wersja polecenia ma problemy z rozpoznawaniem ścian na krawędziach typów powierzchni.
-   W niektórych przypadkach polecenie [Utwórz segmenty z najlepiej dopasowanych powierzchni](Mesh_SegmentationBestFit/pl.md) da lepsze rezultaty.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Segmentation/pl
