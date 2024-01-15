---
 GuiCommand:
   Name: SheetMetal Extrude
   Name/pl: Arkusz blachy: Wydłuż ściankę
   MenuLocation: SheetMetal , Wydłuż ściankę
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **E**
---

# SheetMetal Extrude/pl



## Opis

Narzędzie <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Wydłuż ściankę** rozciąga blachę na wybranej krawędzi.

Tworzy **proste przedłużenie** wzdłuż wektora normalnego wybranej krawędzi:

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

Dodanie szkicu konturu powoduje utworzenie **geometrii zazębienia** w celu zamknięcia profilu:

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Trzy profile ze szkicami do dodania → trzy wyniki*



## Użycie



### Prosty Wydłużenie 

1.  Wybierz jedną lub więcej krawędzi, które mają zostać wyciągnięte.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **Wydłuż ściankę** używając jednego z poniższych:
    -   Przycisk **<img src="images/SheetMetal_Extrude.svg" width=16px> '''Wydłuż ściankę'''**.
    -   Opcja menu **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Wydłuż ściankę**.
    -   Skrót klawiaturowy: **E**.
3.  Zmień wartość właściwości **Długość**, aby dostosować długość wydłużenia.



### Przedłużenie z blokadą 

1.  Wybierz jedną krawędź do przedłużenia.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **Wydłuż ściankę** *(patrz wyżej)*.
3.  Dodaj współpłaszczyznowy szkic konturu do właściwości **Szkic**.
4.  Ustaw wartość właściwości **Użyj odejmowania** na {{TRUE/pl}}, aby utworzyć wycięcia na przedłużenia.
5.  Ustaw właściwość **Odsunięcie**, aby dostosować prześwit wokół rozszerzenia.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Trzy profile → położenie szkiców → wyniki bez wycięć → wyniki końcowe.*



## Uwagi

-   Szkic może zawierać więcej niż jeden kontur.

Po wstawieniu szkicu co najmniej jeden z jego konturów musi dotykać co najmniej jednej przeciwległej ściany, w przeciwnym razie narzędzie nie utworzy żadnego przedłużenia lub wycięcia.

Wystarczy jeden kontur dotykający przeciwległej ściany, aby utworzyć geometrię rozszerzenia ze wszystkich konturów szkicu.

-   Każde wycięcie będzie miało kształt prostopadłościanu, niezależnie od kształtu odpowiadającego mu szkicu konturu.

-   Kształty inne niż prostokąty mogą zachowywać się nieco dziwnie i nawet jeśli obiekt można rozłożyć, wynik nie będzie zgodny z oczekiwaniami.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Trzy szkice i wynikające z nich rozszerzenia: oddzielna trójkątna płyta z prostokątnym wycięciem, okrąg bez prześwitu → rozłożona bryła jest podzielona w nieoczekiwanym miejscu.*

-   W operacji rozszerzenia zaleca się pozostawienie właściwości **Ulepsz** ustawionej na {{TRUE/pl}} *(domyślnie)*.

-   Operacja rozszerzenia z połączonym szkicem może się nie powieść z powodu problemów z współpłaszczyznowością, jeśli powierzchnia po stronie szkicu i powierzchnia po przeciwnej stronie są współpłaszczyznowe, ale mają przeciwne orientacje. Niewielkie przesunięcie może pomóc w takim przypadku.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt wydłużenia ścianki środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|Extend}} *(+ kolejny numer dla drugiej i następnych pozycji)*. Edytowalna przez użytkownika nazwa tego obiektu, może to być dowolny ciąg znaków UTF8.

-    **Cecha podstawowa|Link|ukryte**: Cecha bazowa. Link do cechy nadrzędnej.

-    **_Body|LinkHidden|ukryte**: Link ukryty do zawartości nadrzędnej.


{{Properties_Title|Parametry}}

-    **Obiekt bazowy|LinkSub**: Obiekt bazowy. Łącze do powierzchni planarnej, która ma zostać rozszerzona.

-    **Szczelina1|Distance**: Szczelina z prawej strony. Wartość domyślna: {{value|0,00 mm}}.

-    **Szczelina2|Distance**: Szczelina z lewej strony. Wartość domyślna: {{value|0,00 mm}}.

-    **Długość|Length**: Długość ściany. Wartość domyślna: {{value|10,00 mm}}.


{{Properties_Title|Parametry Ext}}

-    **Odsunięcie|Distance**: Odsunięcie dla odejmowania. Wartość domyślna: {{value|20,00 µm}}.

-    **Ulepsz|Bool**: Użyj ulepszania. Wartość domyślna: {{TRUE/pl}}.

-    **Szkic|Link**: Szkic ściany.

-    **Użyj odejmowania|Bool**: Użyj odejmowania. Wartość domyślna: {{FALSE/pl}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Extrude/pl
