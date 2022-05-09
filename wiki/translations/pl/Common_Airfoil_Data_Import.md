# Common Airfoil Data Import/pl
## Importowanie danych profili lotniczych 

FreeCAD może importować dane o profilach lotniczych, takie jak te znajdujące się w bazie danych profili lotniczych [UIUC Airfoil Coordinates Database](http   *//m-selig.ae.illinois.edu/ads/coord_database.html) lub pliki tworzone przez oprogramowanie do tworzenia i analizy profili lotniczych, takie jak [XFLR5](http   *//www.xflr5.com/xflr5.htm).

## Użycie

Z menu Plik wybierz polecenie **Otwórz** dla nowego dokumentu lub **Importuj** dla istniejącego dokumentu. W oknie dialogowym Otwórz lub Importuj wybierz z menu rozwijanego typ pliku   * **Wspólne dane o profilach lotniczych (\*.dat)**, kolejnie wybierz plik i kliknij w przycisk **Otwórz**.

Podczas otwierania plików danych profilu lotniczego program FreeCAD wczytuje plik i importuje go w jednostkach programu FreeCAD. Pliki danych o profilach podają współrzędne XY w liczbach z zakresu od 0 do 1. W rezultacie importowany profil będzie miał domyślnie długość cięciwy 1 mm. Poniżej przedstawiono przykładowy plik .dat typowego profilu lotniczego. Zauważ, że wszystkie punkty danych mieszczą się w przedziale od 0 do 1. 
```python
AG35
     0.999998    0.002490
     0.994759    0.003346
     0.985091    0.004927
     0.973580    0.006810
     0.961032    0.008862
     0.948054    0.010984
     0.934900    0.013135

~ ~ ~ ~ ~ ~ ~ ~

     0.947640   -0.000001
     0.960660   -0.000001
     0.973282    0.000000
     0.984898    0.000000
     0.994724   -0.000001
     1.000001    0.000000
```

## Import rozszerzony 

Dostępna jest makrodefinicja, dzięki której można zaimportować profil lotniczy o długości cięciwy zdefiniowanej przez użytkownika. Makro to najpierw pozwala użytkownikowi wybrać plik danych profilu lotniczego do zaimportowania, a następnie wprowadza długość cięciwy. Następnie odpowiednio przeskaluje profil do użycia. Można je znaleźć na stronie Wiki [Przepisy na makropolecenia](Macros_recipes/pl.md) pod nazwą [Import profili lotniczych i skala](Macro_Airfoil_Import_%26_Scale/pl.md).




[Category   *User Documentation](Category_User_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Common Airfoil Data Import/pl
