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
2.  To polecenie można wywołać na kilka sposobów:
    -   Wciśnij przycisk **<img src="images/SheetMetal_Extrude.svg" width=16px> [Wydłuż ściankę](SheetMetal_Extrude/pl.md)**.
    -   Wybierz opcję **Sheet Metal → <img src="images/SheetMetal_Extrude.svg" width=16px> Wydłuż ściankę** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **Sheet Metal → <img src="images/SheetMetal_Extrude.svg" width=16px> Wydłuż ściankę** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **E**.
3.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Extend Parameters** opens (wprowadzony w wersji 0.5.00).
4.  Opcjonalnie wciśnij przycisk **Wybierz** aby dodać więcej ścianek.
    -   Wciśnij przycisk **Pogdląd** aby zakończyć wybór i wyświetlić zmiany.
5.  Opcjonalnie dostosuj parametry w panelu zadań.
6.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
7.  Utworzony zostanie obiekt **Extend** składający się z jednego nowego przedłużenia ściany dla każdej wskazanej ściany.
8.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).



### Przedłużenie z blokadą 

:   (Przygotuj a <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [szkic](Sketcher_Workbench/pl.md) dla blokujących się zakładek)

1.  Wybierz krawędź ściany do przedłużenia.
2.  Wywołaj polecenie zgodnie z powyższym opisem.
3.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
4.  W [Edytorze właściwości](Property_editor/pl.md) wciśnij przycisk **...** właściwości **Sketch**.
5.  Otwarte zostanie okno dialogowe Link.
    -   Wybierz przygotowany szkic z listy.
    -   Wciśnij przycisk **OK** aby zamknąć okno dialogowe.
6.  Ustaw wartość właściwości **Użyj odejmowania** na {{TRUE/pl}}, aby utworzyć wycięcia na przedłużenia.
7.  Ustaw właściwość **Odsunięcie**, aby dostosować prześwit wokół rozszerzenia.

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

Obiekt wydłużenia ścianki środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


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
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Extrude/pl
