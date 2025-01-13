---
 GuiCommand:
   Name: Part Defeaturing
   Name/pl: Część: Usuwanie cech
   MenuLocation: Część , Usuwanie cech
   Workbenches: Part_Workbench/pl
   Version: 0.18
   SeeAlso: Defeaturing_Workbench/pl, Macro_Parametric_Defeaturing/pl
---

# Part Defeaturing/pl



## Opis

Narzędzie **Usuwanie cech** jest przeznaczone do usuwania wybranych cech z modelu. W tym kontekście przez cechy rozumie się otwory, występy, szczeliny, fazy, zaokrąglenia itp. znajdujące się w modelu.

Narzędzie Usuwanie cech może być bardzo przydatne w różnych kontekstach:

-   Edycja zaimportowanej bryły, w przypadku której nie jest dostępna historia operacji.
-   Usuwanie defektów w modelu, np. wypełnianie szczelin, otworów itp.
-   Uproszczenie modelu na potrzeby analizy numerycznej, wyświetlania na urządzeniach mobilnych itp.

Usunięte elementy są wypełniane przez przedłużenie sąsiednich ścian, więc w wyniku nie powinny pojawić się żadne nieoczekiwane części. Należy pamiętać, że wynikiem jest nowy kształt, który nie jest powiązany z oryginałem; dlatego jest nieparametryczny.

Aby to narzędzie było dostępne, FreeCAD musi być oparty na Open Cascade **7.3.0** lub nowszym. Jeśli nie jest ono dostępne w twojej wersji FreeCAD, możesz rzucić okiem na zewnętrzne środowisko pracy [Upraszczanie](Defeaturing_Workbench/pl.md), który proponuje podobną funkcjonalność nawet w starszych wersjach OCC lub FreeCAD.

![](images/Part_Defeaturing_example.png )



## Użycie

1.  Wybierz ściany na modelu do usunięcia.
2.  Naciśnij przycisk **<img src="images/Part_Defeaturing.svg" width=16px> '''Usuwanie cech'''**.
3.  Zostanie utworzony nowy obiekt oznaczony jako *Uproszczony* w [widoku drzewa](Tree_view/pl.md) modelu, a oryginalny obiekt zostanie ukryty.



## Odnośniki internetowe 

-   [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211), oficjalne ogłoszenie na wspólnym portalu deweloperskim Open Cascade.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/pl
