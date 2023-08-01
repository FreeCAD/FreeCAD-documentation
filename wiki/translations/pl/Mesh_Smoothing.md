---
- GuiCommand:
   Name: Mesh Smoothing
   Name/pl: Siatka: Wygładź
   MenuLocation: Siatki - Wygładź ...
   Workbenches: [Siatka](Mesh_Workbench/pl.md)
---

# Mesh Smoothing/pl

## Opis

Polecenie **Wygładź** wygładza obiekty siatkowe poprzez zmianę położenia ich wierzchołków.

![](images/Meshes_Smooth.jpg ) 
*Panel zadań wygładzania po wybraniu opcji Tylko wybór.*

## Użycie

1.  Jeśli planujesz określić parametry typu powierzchni, zwróć uwagę, że polecenie używa koloru czerwonego do oznaczenia ścian wybranych dla tej opcji. Aby je prawidłowo zobaczyć:
    -   
        {{PropertyView/pl|Tryb wyświetlania}}
        
        obiektu siatki idealnie powinien być ustawiony na {{Value|Cieniowany z krawędziami}}, ale powinien przynajmniej pokazywać ściany. W razie potrzeby użyj polecenia [Styl kreślenia](Std_DrawStyle/pl.md), aby nadpisać tę właściwość.

    -   
        {{PropertyView/pl|Kolor kształtu}}
        
        obiektu siatkowego nie powinien być czerwony.
2.  Wybierz jeden lub więcej obiektów siatki.
3.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_Smoothing.svg" width=16px> '''Wygładź'''
**
    -   Wybierz **Siatki → <img src="images/Mesh_Smoothing.svg" width=16px> Wygładź ...** opcję z menu.
4.  Otworzy się panel zadań **Wygładzanie**.
5.  Jeśli chcesz wygładzić tylko wybrane obszary: wybierz opcję **Tylko wybór**:
    -   Do panelu zadań zostanie dodany panel **Zaznaczanie**.
    -   Określ opcje regionu:
        -   
            **Akceptuj tylko widoczne trójkąty**
            

        -   
            **Akceptuj tylko trójkąty o normalnych ścian zwrócone w stronę ekranu**
            
    -   Naciśnij przycisk **Dodaj** i trzymając wciśnięty lewy przycisk myszy narysuj obszar, zamkniętą krzywą łamaną, w oknie [widoku 3D](3D_view/pl.md). Zostaną wybrane ściany, które odpowiadają opcjom obszaru i *(częściowo)* mieszczą się w tym obszarze.
    -   Opcjonalnie naciśnij przycisk **Wyczyść**, aby wyczyścić zaznaczenie.
6.  Wybierz **Metodę** wygładzania:
    -   
        **Taubin**
        

    -   
        **Laplace**
        
7.  Podaj **Parametry**:
    -   
        **Powtórzenia**
        
        : im wyższa ta liczba, tym gładszy efekt końcowy. Wartość ta ma również wpływ na całkowity czas przetwarzania polecenia. Unikaj wysokich wartości, jeśli obiekty siatki mają wiele punktów.

    -   
        **λ**
        
        : wartość musi być z przedziału {{Value|0}} - {{Value|1}}.

    -   
        **μ**
        
        : wartość musi być z przedziału {{Value|0}} - {{Value|1}}.
8.  Naciśnij przycisk **OK**, aby zakończyć polecenie.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Smoothing/pl
