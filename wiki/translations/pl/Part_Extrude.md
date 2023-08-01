---
- GuiCommand:
   Name:Part Extrude
   Name/pl:Część: Wyciągnięcie
   MenuLocation:Część → Wyciągnięcie
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Przytnij](Draft_Trimex/pl.md), [Wyciągnij](PartDesign_Pad/pl.md)
---

# Part Extrude/pl



## Opis

**Wyciągnięcie części** powoduje wydłużenie kształtu o określoną odległość i w określonym kierunku. Typ kształtu wyjściowego zależy od typu kształtu wejściowego i wybranych opcji.

W najczęstszych scenariuszach poniższa lista zawiera oczekiwany typ kształtu wyjściowego z danego typu kształtu wejściowego,

-   Wyciągnięcie wierzchołka *(punktu)* spowoduje utworzenie krawędzi liniowej *(linii)*.
-   Wyciągnięcie otwartej krawędzi *(np. linii, łuku)*, spowoduje utworzenie otwartej ściany *(np. płaszczyzny)*
-   Wyciągnięcie zamkniętej krawędzi *(np. okręgu)*, opcjonalnie utworzy zamkniętą ścianę *(np. otwarty walec)* lub, jeśli parametr *bryła* ma wartość {{true/pl}}, utworzy bryłę *(np. zamknięty, pełny walec)*.
-   Wyciągnięcie otwartej krzywej *(np. krzywa środowiska Rysunek Roboczy)*, spowoduje utworzenie otwartej powłoki *(kilka połączonych ścian)*.
-   wyciągnięcie zamkniętej krzywej *(np. krzywa środowiska Rysunek Roboczy)*, opcjonalnie utworzy powłokę *(kilka połączonych ścian)* lub, jeśli parametr *bryła* ma wartość {{true/pl}}, utworzy bryłę
-   Wyciągnięcie ściany *(np. płaszczyzny)*, spowoduje utworzenie bryły *(np. prostopadłościanu)*.
-   Wyciągnięcie **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Kształt z tekstu](Draft_ShapeString/pl.md)**, utworzy złożenie brył *(ciąg jest złożeniem liter, z których każda jest bryłą)*
-   Wyciągnięcie powłoki ze ścian, {{true/pl}} utworzy bryłę Złożoną.

![600px](images/Part_Extrude_demo.png)



*Przykłady wytłaczania*



## Użycie

1.  Wybierz kształt*(y)* w oknie [widoku 3D](3D_view/pl.md) lub [Widoku drzewa](Tree_view/pl.md).
2.  Kliknij przycisk **<img src="images/Part_Extrude.svg" width=16px> [Wyciągnięcie ...](Part_Extrude/pl.md)
** na pasku narzędzi lub przejdź do menu **Część → Wyciągnięcie ...**
3.  Ustaw kierunek i długość oraz opcjonalnie inne parametry (więcej szczegółów znajduje się w sekcji [Parametry](#Parametry.md)).
4.  Kliknij **OK**.

Alternatywnie, wyboru można dokonać po uruchomieniu narzędzia, wybierając jeden lub więcej kształtów z listy w [Panelu zadań](Task_panel/pl.md).

Drzewo modelu wyświetli tyle obiektów Wyciągnięcia, ile wybrano kształtów. Każdy kształt wejściowy jest umieszczony pod swoim obiektem Wyciągnięcie.



## Parametry

Kształt Wyciągnięcia jest definiowany przez następujące parametry, które mogą być edytowane po jego utworzeniu w [Edytorze właściwości](Property_editor/pl.md).

-   **Podstawa**: kształt wejściowy *(kształt, na którym zastosowano wyciągnięcie)*.

-   **Kierunek**: kierunek rozszerzenia kształtu. Jeśli \"Tryb kierunku\" ma wartość \"Użytkownika\", można edytować \"Kierunek\". W przeciwnym razie **Kierunek** jest tylko do odczytu i jest obliczany na podstawie połączonego kształtu.

-   **Kierunek połączenia**: parametryczne połączenie z krawędzią *(linią)*, które określa kierunek wytłaczania.

-   **Kierunek**: kierunek wydłużenia kształtu. Jeśli **Tryb Kierunku** ma wartość *Użytkownika*, można edytować **Kierunek**. W przeciwnym razie **Kierunek** jest tylko do odczytu i jest obliczany na podstawie połączonego kształtu.

-   **Długość wzdłuż**: Odległość do wyciągnięcia. Jeśli zarówno **Długość wzdłuż**, jak i **Długość przeciwnie** wynoszą zero, używana jest długość wektora **Kierunek**.

-   **Długość przeciwnie**: Dodatkowa długość do wyciągnięcia względem **Długość**.

-   **Utwórz bryłę**: jeśli wartość wynosi {{True/pl}}, wyciągnięcie zamkniętej krawędzi lub zamkniętego krzywej spowoduje utworzenie bryły. Jeśli wartość ta wynosi {{False/pl}}, wynikiem będzie powłoka.

-   **Odwrócony**: odwraca wyciskanie w kierunku przeciwnym do parametry **Kierunek**.

-   **Symetrycznie**: jeśli wartość ta jest równa True, wytłaczanie jest wyśrodkowane na kształcie wejściowym, a całkowita długość jest równa *Długość wzdłuż*. **Długość przeciwnie** jest ignorowana.

-   **Kąt ścięcia** oraz **Kąt ścięcia przeciwnie**: stosuje kąt do wyciągnięcia, dzięki czemu boki wyciągnięcia są wyciągnięte pod określonym kątem. Dodatni kąt oznacza rozszerzenie przekroju. **Kąt ścięcia przeciwnie** ustawia odwrotne zwężenie dla części wytłoczenia *(część z **Długość przeciwnie**)*.
    -   
        {{Version/pl|0.20}}
        
        Wewnętrzne struktury otrzymują przeciwny kąt stożka. Ma to na celu ułatwienie projektowania form i wyprasek.

    -   
        {{VersionMinus/pl|0.19}}
        
        Stożkowe wytłaczanie jest obsługiwane tylko w przypadku kształtów bez struktur wewnętrznych. Wytłaczanie stożkowe nie działa dobrze, jeśli kształt zawiera krzywe złożone.

-   **Klasa kreatora ścian**: ustawia nazwę klasy C++ kodu tworzącego ściany, który jest używany podczas tworzenia brył z krzywych. Ta właściwość służy głównie do zachowania kompatybilności wstecznej. Nie używaj jej, chyba że wiesz co robisz.

-   **Umiejscowienie**: standardowe parametry [Umiejscowienia](Placement/pl.md).

-   **Etykieta**: etykieta wyświetlana w oknie [widoku drzewa](Tree_view/pl.md) *(niedostępna w trakcie tworzenia Wyciągnięcia)*.



## Okno dialogowe zadania 

![](images/Part_Extrude_dialog.png )

-   Przycisk **OK** tworzy wytłoczenie i zamyka okno dialogowe.

-   Przycisk **Zamknij** zamyka okno dialogowe, nie robiąc nic.

-   Przycisk **Zastosuj** tworzy wyciągnięcie, ale nie zamyka okna dialogowego. Następnie można wybrać inny kształt z listy na dole i utworzyć więcej wyciągnięć. Kliknięcie przycisku **Zastosuj** może spowodować utworzenie wielu wyciągnięć.

-   Przyciski wyboru **Kierunek**: ustawiają sposób obliczania kierunku wyciągnięcia.

-   Przycisk **Wybierz**: kliknij go, a następnie wybierz krawędź w oknie [Widoku 3D](3D_view/pl.md). Krawędź ta pojawi się w polu tekstowym obok przycisku, w formacie \"ObjectName:EdgeN\". Możesz również wpisać link ręcznie. Wartości X,Y,Z zostaną wypełnione zgodnie z kierunkiem krawędzi.

-   Przyciski **X**, **Y**, **Z**: Kliknij przycisk **X**, aby ustawić kierunek wyciągnięcia na oś **+X**. Kliknij go ponownie, aby ustawić oś **-X**.

-   Pola wejściowe **X**, **Y**, **Z**: ustawiają lub wyświetlają wektor kierunku wyciągnięcia. Jeśli obie długości wynoszą zero, długość tego wektora ustawia długość wyciągnięcia, a wartości są zawsze w mm, niezależnie od preferencji dotyczących jednostek.

-   Pola długości: ustawiają długość wyciągnięcia. Te pola wejściowe obsługują jednostki.

-   Symetrycznie: rozkłada wyciągnięcie w obu kierunkach, dzięki czemu profil pozostaje ustawiony środkowo.

-   Kąt ścięcia wzdłuż: dodatni kąt oznacza, że profil jest rozszerzany na drugim końcu wytłoczenia.

-   Pole wyboru Utwórz bryłę: jeśli pole jest zaznaczone, wyciągnięcie zamkniętej krawędzi lub krzywej spowoduje utworzenie bryły. Jest domyślnie zaznaczone, jeśli zamknięta krawędź została wstępnie wybrana przed wywołaniem funkcji Wyciągnięcia.

-   Lista kształtów: tutaj można wybrać kształty do wyciągnięcia. W przypadku wybrania wielu obiektów tworzonych jest wiele obiektów wyciągnięcia.



## Uwagi

-   Obiekty typu [odnośnik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów i kontenery [App: Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako profile i do określania kierunku. {{Version/pl|0.20}}

-   Okno dialogowe zadania nie oferuje jeszcze podglądu. Przycisk **Zastosuj** utworzy obiekt wyciągnięcia za każdym razem, gdy go klikniesz, co może być przydatne jako podgląd. Jednak pozostaną one i kolejne zostaną utworzone po kliknięciu przycisku **OK**. [Cofnij](Std_Undo/pl.md) może być przydatne do wyczyszczenia ich przed kliknięciem **OK**.



## Porównanie z wyciągnięciem Projekt Części 

[Wyciągnięcie](PartDesign_Pad/pl.md) środowiska Projekt Części jest również funkcją wyciągnięcia, ale istnieją między nimi istotne różnice:

-   Wyciągnięcie środowiska Część zawsze tworzy samodzielny kształt. Wyciągnięcie środowiska Projekt Części łączy wynik wyciągnięcia z resztą Zawartości.
-   Wyciągnięcie środowiska Część nie dba o to, gdzie znajduje się w drzewie modelu. Wyciągnięcie środowiska Projekt Części może znajdować się tylko wewnątrz [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części.
-   Wyciągnięcie części może wytłaczać dowolny obiekt, który ma geometrię części *(kształt [OpenCASCADE](OpenCASCADE/pl.md))*, z wyjątkiem brył i brył złożonych.
-   Wyciągnięcie środowiska Część może wytłaczać pojedyncze ściany innych obiektów. Wyciągnięcie środowiska Projekt Części będzie akceptować jako profil tylko szkic lub ściany obiektów środowiska Projekt Części.





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Extrude/pl
