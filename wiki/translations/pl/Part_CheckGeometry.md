---
 GuiCommand:
   Name: Part CheckGeometry‏‎
   Name/pl: Część: Sprawdź geometrię
   MenuLocation: Część , Sprawdź geometrię
   Workbenches: Part_Workbench/pl
---

# Part CheckGeometry/pl



## Opis

Narzędzie <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> **Sprawdź geometrię** uruchamia weryfikację i zgłasza, czy geometria jest prawidłową bryłą. Narzędzie sprawdza, czy [Odwzorowanie linii granicznych](https://en.wikipedia.org/wiki/Boundary_representation) *(BRep lub [B-rep](Glossary/pl#B.md))* modelu jest prawidłowe.



## Użycie

1.  Wybierz część (pamiętaj, aby wybrać całą część, a nie tylko ścianę, aby sprawdzić poprawność bryły).
2.  Wywołaj narzędzie poprzez
    -   Kliknięcie przycisku **<img src="images/Part_CheckGeometry.svg" width=16px> '''Sprawdź geometrię'''** dostępny na pasku narzędzi części.
    -   Używając polecenia z menu **Część → <img src="images/Part_CheckGeometry.svg" width=16px> Sprawdź geometrię**.
3.  Otworzy się panel zadań **Ustawienia**, chyba że włączona jest opcja **Pomiń ustawienia**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md). Kliknij przycisk **Uruchom sprawdzanie**.

Wyniki zostaną wyświetlone w [Panelu zadań](Task_panel/pl.md). Jeśli kontrola wykazała błędy: kliknij w raporcie na konkretny komunikat o błędzie, a odpowiadający mu obiekt geometryczny *(krawędź, ściana itp.)* zostanie podświetlony w oknie [widoku 3D](3D_view/pl.md).



## Opcje



### Pomiń ustawienia 

Jeśli opcja ta jest zaznaczona, kolejne wywołania narzędzia pomijają wyświetlanie panelu zadań **Ustawienia**.



### Kontrola operacji logicznych 

Jeśli opcja ta jest zaznaczona, dodatkowo wykonywana jest kontrola operacji logicznych *(**B**oolean **OP**erations BOP)*.



### Zapisywanie błędów 

Jeśli opcja ta jest zaznaczona, wszelkie znalezione błędy są również rejestrowane w oknie [widoku raportów](Report_view/pl.md).



## Zawartość kształtu 

Oprócz wykrywania potencjalnych błędów geometrii, narzędzie to wyświetla szereg właściwości dotyczących wybranego obiektu:

-   Sprawdzony obiekt
-   Typ kształtu
-   Liczba elementów geometrycznych: wierzchołki, krawędzie, polilinie, ściany, powłoki, bryły, bryły złożone, złożenia, suma kształtów.
-   Właściwości geometryczne i właściwości masy:
    -   Powierzchnia,
    -   Objętość,
    -   Masa,
    -   Długość,
    -   Środek masy,
    -   Orientacja,
    -   Oś symetrii,
    -   Punkt symetrii,
    -   Momenty,
    -   Pierwsza oś bezwładności,
    -   Druga oś bezwładności,
    -   Trzecia oś bezwładności,
    -   Promień bezwładności,
    -   Globalne umiejscowienie.



## Uwagi

-   Obiekty [połączone](App_Link/pl.md) z odpowiednimi typami obiektów i kontenery środowiska [Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również sprawdzane za pomocą tego narzędzia. W przypadku [powiązań](App_Link/pl.md) sprawdzany jest kształt połączonego obiektu. W przypadku kontenerów środowiska [Część](App_Part/pl.md) widoczne obiekty wewnątrz są sprawdzane jako złożenia. {{Version/pl|0.20}}
-   FreeCAD nie posiada metod automatycznej naprawy geometrii. Jeśli wykryte zostaną błędy, kroki związane z tworzeniem modelu muszą zostać sprawdzone i naprawione przez użytkownika.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/pl
