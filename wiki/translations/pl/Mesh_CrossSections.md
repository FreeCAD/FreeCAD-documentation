---
- GuiCommand:
   Name:Mesh CrossSections
   Name/pl:Siatka: Wiele przekrojów
   MenuLocation:Siatki → Cięcie → Przekrój poprzeczny ...
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Przekrój płaszczyzną](Mesh_SectionByPlane/pl.md)
---

# Mesh CrossSections/pl



## Opis

Polecenie **Wiele przekrojów** tworzy wiele przekrojów przez obiekty siatki. Przekroje są wykonywane równolegle do jednej z głównych płaszczyzn globalnych *(XY, XZ lub YZ)*. Dla każdego zestawu przekrojów tworzona jest pojedyncza [Cecha](Part_Feature/pl.md).



## Użycie

1.  Wybierz jeden lub więcej obiektów siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_CrossSections.svg" width=16px> [Przekrój poprzeczny ...](Mesh_CrossSections/pl.md)**.
    -   Wybierz z menu opcję **Siatki → Cięcie → <img src="images/Mesh_CrossSections.svg" width=16px> Przekrój poprzeczny ...**.
3.  Otwiera się panel zadań **Przekrój poprzeczny**.
4.  Płaszczyzny, które zostaną użyte do utworzenia przekrojów są wskazane w oknie [widoku 3D](3D_view/pl.md) i będą aktualizowane na podstawie danych z panelu zadań.
5.  Wybierz **Płaszczyznę prowadzenia**:
    -   
        **XY**
        

    -   
        **XZ**
        

    -   
        **YZ**
        
6.  Określa **Pozycję** płaszczyzny prowadzącej od początku. Domyślna pozycja jest oparta na środku ramki otaczjącej wybranych obiektów siatkowych. Wybranie innej **Płaszczyzny prowadzenia** lub przełączenie pola wyboru **Przekroje** spowoduje przywrócenie wartości domyślnej **Pozycji**.
7.  Opcjonalnie zaznacz pole wyboru **Przekroje**, aby utworzyć wiele przekrojów:
    -   
        **Po obu stronach**
        
        : jeśli zaznaczone, przekroje są tworzone po obu stronach płaszczyzny prowadzącej.

    -   
        **Licznik**
        
        : liczba przekrojów.

    -   
        **Odległość**
        
        : odległość między przekrojami. Wartość domyślna jest oparta na wymiarach ramki otaczjącej, opcji **Po obu stronach** oraz wartości **Licznik**. Zmiana wartości **Licznik** spowoduje zresetowanie opcji **Odległość** do tej wartości domyślnej. Zmiana opcji **Po obu stronach** spowoduje ponowne obliczenie wartości **Odległość** *({{value|*2.0}} lub {{value|*0.5}})*. Zauważ, że pole wejściowe może być nieaktywne, ale wartość może być w rzeczywistości zmieniona.

    -   Opcjonalnie zaznacz pole wyboru **Połącz krawędzie jeśli odległość jest mniejsza niż** i określ wartość.
8.  Naciśnij przycisk {{button|Zastosuj}}, aby utworzyć zestaw przekrojów.
9.  Opcjonalnie zmień jedno lub więcej ustawień i utwórz dodatkowe zestawy przekrojów.
10. Naciśnij przycisk {{button|OK}} lub przycisk {{button|Anuluj}}, aby zamknąć panel zadań i zakończyć polecenie.



## Właściwości

Zapoznaj się z informacjami na stronie: [cecha](Part_Feature/pl.md) środowiska Część.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh CrossSections/pl
