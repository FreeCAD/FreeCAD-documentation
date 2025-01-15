---
 GuiCommand:
   Name: Arch Schedule
   Name/pl: Architektura: Obmiar
   MenuLocation: Zarządzanie , Obmiar
   Workbenches: BIM_Workbench/pl
   SeeAlso: 
---

# Arch Schedule/pl



## Opis

Narzędzie **Obmiar** umożliwia tworzenie i automatyczne wypełnianie [arkusza kalkulacyjnego](Spreadsheet_Workbench/pl.md) zawartością zebraną z modelu.

Aby uzyskać bardziej ogólne rozwiązanie, zapoznaj się z środowiskiem pracy [Reporting Workbench](https://github.com/furti/FreeCAD-Reporting/tree/master) na liście [zewnętrznych środowisk pracy](External_workbenches/pl.md). To środowisko pracy używa składni SQL do wyodrębniania informacji z dokumentu.



## Użycie

1.  Otwórz lub utwórz dokument FreeCAD zawierający kilka obiektów.
2.  Naciśnij przycisk **<img src="images/Arch_Schedule.svg" width=16px> '''Obmiar'''**.
3.  Dostosuj żądane opcje. Włącz opcję **Skojarz arkusz** jeśli chcesz aby Obmiar generował [arkusz](Spreadsheet_Workbench/pl.md) programu FreeCAD. Lub, alternatywnie, kliknij prawym przyciskiem myszy na obmiarze w [widoku drzewa](Tree_view/pl.md) po utworzeniu i wybierz opcję **Dołącz arkusz** z menu kontekstowego.
4.  Naciśnij przycisk **OK**.



## Przepływ pracy 

Najpierw musisz mieć model. Na przykład tutaj jest dokument z kilkoma obiektami Architektury, ale inne obiekty są również obsługiwane.

![](images/Arch_schedule_example01.jpg )

Po wciśnięciu przycisku **<img src="images/Arch_Schedule.svg" width=16px> '''Obmiar'''** pojawi się następujący panel zadań:

![](images/ArchSchedule.png )

Teraz możesz wypełnić obmiar wiersz po wierszu. Każdy wiersz jest \"zapytaniem\" i wygeneruje jeden wiersz w arkuszu kalkulacyjnym. Naciśnij przycisk **<img src="images/List-add.svg" width=16px> Dodaj wiersz**, aby dodać nowy wiersz i kliknij dwukrotnie każdą komórkę z tego wiersza, aby wypełnić wartości. Przycisk **<img src="images/List-remove.svg" width=16px> Usuń wiersz** usunie wiersz zawierający aktualnie zaznaczoną komórkę, a **<img src="images/Delete.svg" width=16px> Wyczyść** usunie wszystkie wiersze. Możliwe wartości do wpisania w kolumnach to:

-   **Opis**: Opis dla tego zapytania. Kolumna Opis będzie pierwszą kolumną wynikowego arkusza kalkulacyjnego. Opis jest obowiązkowy do wykonania zapytania. Jeśli komórka opisu pozostanie pusta, cały wiersz zostanie pominięty i pozostawiony pusty w arkuszu kalkulacyjnym. Pozwala to na dodanie wierszy \"separatorów\".
-   **Właściwość**: Jest to rzeczywiste zapytanie, które ma zostać wykonane na wszystkich obiektach wybranych przez zapytanie. Mogą to być dwie rzeczy: słowo `count` lub właściwość obiektu:
    -   Jeśli wpiszesz `count` *(lub `Count` lub `COUNT`, wielkość liter nie ma znaczenia)* wybrane obiekty zostaną po prostu zliczone.
    -   Jeśli wprowadzi właściwość obiektu, wartość tej właściwości będzie odzyskana dla każdego z zaznaczonych obiektów i zsumowana. Obiekty, które nie mają danej właściwości będą pominięte. Ogólnie nazwa właściwości będzie tą pokazaną w [Edytorze właściwości](Property_editor/pl.md), bez spacji (np. typ `PerimeterLength` w kolumnie właściwości jeśli obiekt ma właściwość `Perimeter Length` w Edytorze właściwości). Użyj notacji kropkowej, aby pobrać właściwości właściwości: `PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. Jeśli właściwość przed pierwszą kropką zaczyna się od małej litery, zostanie ona uznana za odniesienie do samego obiektu i zignorowana. Wpisanie na przykład `object.Shape.Volume` jest tym samym, co wpisanie `Shape.Volume`.
-   **Jednostka**: Opcjonalna jednostka, w której wyrażone zostaną wyniki. Do użytkownika należy podanie jednostki, która pasuje do zapytania, które wykonuje, na przykład, jeśli pobierasz objętości, powinieneś użyć jednostki objętości, takiej jak `m^3` lub `m³`. Jeśli użyjesz niewłaściwej jednostki dla właściwości, np. `cm` dla objętości, otrzymasz błędne wyniki.
-   **Obiekty**: Można pozostawić to pole puste, wtedy wszystkie obiekty dokumentu będą brane pod uwagę przez to zapytanie, lub podać listę nazw obiektów oddzielonych średnikiem `;`. Jeśli którykolwiek z obiektów na tej liście jest grupą, jego dzieci również zostaną wybrane. Najprostszym sposobem na użycie tej funkcji jest pogrupowanie obiektów w dokumencie i podanie nazwy grupy w tym miejscu. Możesz także użyć przycisku **<img src="images/Edit-select-all.svg" width=16px> Dodaj wybrane**, aby dodać obiekty aktualnie zaznaczone w dokumencie. W tym przypadku należy użyć nazw wewnętrznych. Aby wybrać obiekty według ich etykiety, pozostaw tę kolumnę pustą i użyj zamiast niej kolumny Filtr.
-   **Filtr**: W tym miejscu można dodać listę filtrów oddzielonych średnikami`;`. Każdy filtr ma postać: `property:value`. Można używać tylko właściwości, które przechowują wartość łańcuchową. Zarówno właściwość, jak i wartość nie uwzględniają wielkości liter. Można pominąć `value`, ale nie `:`. Aby poprawnie obsługiwać harmonogramy utworzone w poprzednich wersjach Obmiaru, właściwość `type` zostanie przetłumaczona na właściwość `ifctype`. Zaleca się, aby nie używać `type` w nowych harmonogramach.

+++
| Zapytanie                              | Opis                                                                                                                                                                                                                                                                                                           |
+========================================+================================================================================================================================================================================================================================================================================================================+
|                         | Zachowa tylko obiekty, które mają \"floor1\" w ich **Label** i \"window\" w ich **IFC Type**. Okno z **Label** \"Floor1-AA\" i **IFC Type** \"Standardowym Przypadkiem Okna\" będzie uwzględnione. |
| `label:floor1;ifctype:window` |                                                                                                                                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                                                                                |
+++
|                         | Zachowa tylko obiekty, które mają \"door\" w ich **Label**                                                                                                                                                                                                                          |
| `label:door`                  |                                                                                                                                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                                                                                |
+++
|                         | Zachowa tylko obiekty, które nie mają \"door\" w ich **Label**                                                                                                                                                                                                                      |
| `!label:door`                 |                                                                                                                                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                                                                                |
+++
|                         | Zachowa tylko obiekty, które mają \"structural\" w ich **IFC Type**                                                                                                                                                                                                                 |
| `ifctype:structural`          |                                                                                                                                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                                                                                |
+++
|                         | Zachowa tylko obiekty, które nie mają \"structural\" w ich **IFC Type** lub te, które nie mają właściwości **IFC Type**                                                                                                                                  |
| `!ifctype:something`          |                                                                                                                                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                                                                                |
+++
|                         | Zachowa tylko obiekty, które nie mają właściwości **IFC Type**                                                                                                                                                                                                                      |
| `!ifctype:`                   |                                                                                                                                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                                                                                |
+++

: Example filter queries

Przycisk **<img src="images/Document-open.svg" width=16px> Import** umożliwia zaimportowanie listy utworzonej w innej aplikacji arkusza kalkulacyjnego, w postaci pliku csv.

Ukończony obmiar może wyglądać tak:

![](images/ArchScheduleExample.png )

Wreszcie, naciśnij **OK** i nowy obmiar zostanie dodany do dokumentu. Jeśli została wybrana powiązana opcja, obmiar będzie zawierał skojarzony arkusz:

![](images/Arch_schedule_example04.jpg )

Aby edytować istniejący obmiar, kliknij na nim dwukrotnie w widoku drzewa. Dwukrotne kliknięcie samego arkusza kalkulacyjnego powoduje wyświetlenie wyników w 3 kolumnach: Opis, Wartość, Jednostka *(jeśli dotyczy)*:

![](images/Arch_schedule_example05.jpg )

Arkusz kalkulacyjny można następnie normalnie wyeksportować do formatu csv z poziomu [środowiska pracy Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md).



## Własności dynamiczne 

Możliwe jest dodawanie własnych właściwości do obiektów. Są one nazywane [właściwościami dynamicznymi](Property_editor/pl#Działania.md). Jeśli zostały one dodane z zaznaczoną opcją **Prefiks dla nazwy grupy**, ich nazwy rzeczywiście zaczynają się od nazwy grupy, ale ten przedrostek nie jest wyświetlany w [Edytorze właściwości](Property_editor/pl.md). Ich nazwy mają następującą postać: `NameOfGroup_NameOfProperty`. Aby odwołać się do nich w harmonogramie, należy użyć tej pełnej nazwy.



---
⏵ [documentation index](../README.md) > Arch Schedule/pl
