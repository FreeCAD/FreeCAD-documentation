# <img alt="Ikonka FreeCAD dla Środowiska pracy Arkusz Kalkulacyjny" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/pl

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> **Arkusz Kalkulacyjny** pozwala tworzyć i edytować arkusze kalkulacyjne, używać danych z arkusza kalkulacyjnego jako parametrów w modelu, wypełniać arkusz kalkulacyjny danymi pobranymi z modelu, wykonywać obliczenia i eksportować dane do innych aplikacji arkuszy kalkulacyjnych, takich jak LibreOffice czy Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Arkusz kalkulacyjny z komórkami wypełnionymi tekstem i ilościami*

## Przybory

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Utwórz arkusz](Spreadsheet_CreateSheet/pl.md): tworzy nowy arkusz kalkulacyjny.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Importuj arkusz](Spreadsheet_Import/pl.md): wczytuje plik CSV do arkusza kalkulacyjnego.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Eksportuj arkusz](Spreadsheet_Export/pl.md): zapisuje pliku CSV na podstawie arkusza kalkulacyjnego.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Scal komórki](Spreadsheet_MergeCells/pl.md): łączy wybrane komórki.

-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Podziel komórkę](Spreadsheet_SplitCell/pl.md): rozdziela poprzednio scalone komórki.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Wyrównaj do lewej](Spreadsheet_AlignLeft/pl.md): wyrównuje treść wybranych komórek do lewej.

-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Wyśrodkuj w poziomie](Spreadsheet_AlignCenter/pl.md): wyrównuje treść wybranych komórek do środka w poziomie.

-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Wyrównaj do prawej](Spreadsheet_AlignRight/pl.md): wyrównuje treść wybranych komórek do prawej.

-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Wyrównaj do góry](Spreadsheet_AlignTop/pl.md): wyrównanie zawartości wybranych komórek w górę.

-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Wyśrodkuj w pionie](Spreadsheet_AlignVCenter/pl.md): wyrównuje treść wybranych komórek do środka w pionie.

-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Wyrównaj w dół](Spreadsheet_AlignBottom/pl.md): wyrównuje treść wybranych komórek do dołu.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Pogrubienie](Spreadsheet_StyleBold/pl.md): ustawia pogrubienie treści wybranych komórek.

-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Kursywa](Spreadsheet_StyleItalic/pl.md): ustawia treść wybranych komórek na kursywę.

-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Podkreślenia](Spreadsheet_StyleUnderline/pl.md): ustawia treść wybranych komórek jako podkreśloną.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Ustaw alias](Spreadsheet_SetAlias/pl.md): ustawia alias dla wybranej komórki.

-   Przyciski **Czarny** oraz **Biały** ustawia kolory czcionki i tła dla wybranych komórek.

## Ustawienia

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width:32px;"> [Ustawienia](Spreadsheet_Preferences/pl.md): preferencje dla środowiska pracy Arkusz Kalkulacyjny. {{Version/pl|0.20}}

## Wstawianie i usuwanie wierszy i kolumn 

Wiersze i kolumny można wstawiać i usuwać, klikając prawym przyciskiem myszy nagłówek wiersza lub kolumny i wybierając odpowiednią opcję z menu podręcznego. Możliwe jest zaznaczenie najpierw wielu wierszy lub kolumn. Można to zrobić, przytrzymując klawisz **Ctrl** podczas zaznaczania nagłówków lub przytrzymując lewy przycisk myszy i przeciągając.

W programie FreeCAD w wersji 0.19 i wcześniejszych wiersze są wstawiane nad zaznaczonymi wierszami, a kolumny po lewej stronie zaznaczonych kolumn. W programie FreeCAD w wersji 0.20 można określić kierunek wstawiania.

Należy pamiętać, że usunięcie wierszy lub kolumn z danymi może spowodować zepsucie arkusza kalkulacyjnego i Twojego modelu, jeśli opiera się on na arkuszu. W takim przypadku użytkownik nie jest ostrzegany.

## Wycinanie i kopiowanie-wklejanie komórek 

W komórkach arkuszy kalkulacyjnych programu FreeCAD można wykonywać operacje wycinania i kopiowania-wklejania. Do tych operacji można używać standardowych skrótów klawiszowych: **Ctrl** + **X**, **Ctrl** + **C** i **Ctrl** + **V**. Aby zaznaczyć wiele komórek, przytrzymaj klawisz **Ctrl** podczas zaznaczania lub przytrzymaj lewy przycisk myszy i przeciągnij, aby zaznaczyć prostokątny zakres komórek.

Operacje wycinania i kopiowania zapisują zawartość i właściwości komórek w Schowku. Operacja wklejania powoduje zapisanie danych w taki sposób, że zawartość lewej górnej komórki zapisanych danych jest umieszczana w aktywnej komórce. Pozostała przechowywana zawartość jest umieszczana względem tej komórki. Formuły są odpowiednio aktualizowane.

Należy pamiętać, że usunięcie komurek z danymi może spowodować zepsucie arkusza kalkulacyjnego i Twojego modelu, jeśli opiera się on na arkuszu. W takim przypadku użytkownik nie jest ostrzegany.

W programie FreeCAD w wersji 0.19 i wcześniejszych występuje błąd, który może powodować zawieszanie się programu FreeCAD, jeśli wklejany jest zakres komórek inny niż prostokątny. Zaleca się zapisanie pracy przed wykonaniem jakichkolwiek operacji wklejania.

## Właściwości komórek 

Właściwości komórki arkusza kalkulacyjnego można edytować, klikając komórkę prawym przyciskiem myszy i wybierając z menu podręcznego polecenie **Właściwości ...**. Zostanie wyświetlone następujące okno dialogowe:

![](images/SpreadsheetCellPropDialog.png )

Zgodnie z informacjami na kartach można zmieniać następujące właściwości:

-   Kolor: kolor tekstu i kolor tła
-   Wyrównanie: wyrównanie tekstu w poziomie i w pionie
-   Styl: styl tekstu: pogrubienie, kursywa, podkreślenie
-   Jednostki: Wyświetl jednostki dla tej komórki. Proszę przeczytać sekcję [Jednostki](#Jednostki.md) poniżej.
-   Alias: Definiuje [alias](Spreadsheet_SetAlias/pl.md) dla tej komórki. Można go używać w formułach komórek, a także w ogólnych [wyrażeniach](Expressions/pl.md). Więcej informacji na ten temat znajduje się w sekcji [Dane arkusza kalkulacyjnego w wyrażeniach](#Dane_arkusza_kalkulacyjnego_w_wyra.C5.BCeniach.md).

## Wyrażenia w komórkach 

Komórka arkusza kalkulacyjnego może zawierać dowolny tekst lub wyrażenie. Technicznie rzecz biorąc, wyrażenia muszą zaczynać się od znaku równości \"=\". Jednak arkusz kalkulacyjny stara się być inteligentny. Jeśli wpiszesz coś, co wygląda jak wyrażenie bez znaku \"=\", zostanie on dodany automatycznie.

Wyrażenia komórek mogą zawierać liczby, funkcje, odwołania do innych komórek i odwołania do właściwości modelu *(ale przeczytaj akapit [Obecne ograniczenia](#Obecne_ograniczenia.md) poniżej)*. Do komórek odwołujemy się za pomocą ich adresu utworzonego z indeksu kolumny *(wielka litera)* i wiersza *(liczba)*. Do komórki można się też odwoływać za pomocą jej [nazwy alias](#alias_name.md). Przykład: B4 + A6

**Uwaga:** Wyrażenia komórek są traktowane przez FreeCAD jak kod programowania. Dlatego podczas edycji zawartości komórki można zauważyć, że nie jest ona zgodna z ustawieniami wyświetlania:

-   separatorem miejsc dziesiętnych jest zawsze kropka
-   liczba wyświetlanych miejsc po przecinku może się różnić od Twoich [ustawień w preferencjach](Preferences_Editor#Jednostki.md).

Odwołania do obiektów w modelu wyjaśniono w sekcji [Odniesienia do danych CAD](#Odniesienia_do_danych_CAD.md) poniżej. Używanie wartości komórek arkusza kalkulacyjnego do definiowania właściwości modelu wyjaśniono w sekcji [Dane arkusza kalkulacyjnego w wyrażeniach](#Dane_arkusza_kalkulacyjnego_w_wyra.C5.BCeniach.md) poniżej. Więcej informacji na temat wyrażeń i dostępnych funkcji można znaleźć na stronie [Wyrażenia](Expressions/pl.md).

## Interakcja między arkuszami kalkulacyjnymi a modelem CAD 

Dane znajdujące się w komórkach arkusza kalkulacyjnego mogą być wykorzystywane w wyrażeniach parametrów modelu CAD. W ten sposób arkusz kalkulacyjny może być używany jako źródło wartości parametrów używanych w całym modelu, efektywnie gromadząc wartości w jednym miejscu. Gdy wartości są zmieniane w arkuszu kalkulacyjnym, zostają one przekazane do całego modelu.

Podobnie, właściwości obiektów modelu CAD mogą być używane w wyrażeniach w komórkach arkusza kalkulacyjnego. Pozwala to na wykorzystanie w arkuszu kalkulacyjnym właściwości obiektu, takich jak objętość czy powierzchnia. Jeśli nazwa obiektu w modelu CAD zostanie zmieniona, zmiana ta zostanie automatycznie przeniesiona do wszystkich odwołań w wyrażeniach arkusza kalkulacyjnego używających zmienionej nazwy.

W dokumencie może być używany więcej niż jeden arkusz kalkulacyjny. Arkusz kalkulacyjny można zidentyfikować, używając jego nazwy lub etykiety.

FreeCAD automatycznie przypisuje unikalną nazwę do arkusza kalkulacyjnego podczas jego tworzenia. Nazwy te są zgodne z wzorcem `Arkusz kalkulacyjny`, `Arkusz kalkulacyjny001`, `Arkusz kalkulacyjny002` i tak dalej. Nazwy tej nie można zmienić ręcznie i nie jest ona widoczna we właściwościach arkusza kalkulacyjnego. Można jej użyć do odwołania się do arkusza kalkulacyjnego w [wyrażeniach](Expressions/pl.md) *(zobacz sekcję [Dane arkusza kalkulacyjnego w wyrażeniach](#Dane_arkusza_kalkulacyjnego_w_wyra.C5.BCeniach.md) poniżej)*.

Etykieta arkusza kalkulacyjnego jest automatycznie ustawiana na nazwę arkusza podczas jego tworzenia. W przeciwieństwie do nazwy, etykietę można zmienić, np. w panelu właściwości lub za pomocą polecenia **Zmień nazwę** w menu podręcznym. Należy pamiętać, że etykieta arkusza kalkulacyjnego w dokumencie musi być unikalna. Jeśli spróbujesz zmienić etykietę na etykietę używaną już przez inny arkusz kalkulacyjny, FreeCAD nie zaakceptuje nowej etykiety.

FreeCAD sprawdza, czy nie występują zależności cykliczne. Zobacz sekcję [obecne ograniczenia](#Obecne_ograniczenia.md).

### Odniesienia do danych CAD 

Jak wskazano powyżej, w wyrażeniach arkusza kalkulacyjnego można odwoływać się do danych z modelu CAD.

Wyrażenia obliczeniowe w komórkach arkusza kalkulacyjnego zaczynają się od znaku równości {{ASCII|61|24}}. Jednak mechanizm wprowadzania danych w arkuszu kalkulacyjnym stara się być inteligentny. Wyrażenie może być wpisane bez znaku {{ASCII|61|24}}. Jeśli wpisany ciąg znaków jest poprawnym wyrażeniem, znak {{ASCII|61|24}} jest automatycznie dodawany po ostatnim naciśnięciu klawisza **Enter**. Jeśli wpisany ciąg nie jest poprawnym wyrażeniem *(często jest to wynik wpisania czegoś z niewłaściwą literą, np. \"MyCube.length\" zamiast \"MyCube.Length\")*, nie jest dodawany znak {{ASCII|61|24}} i jest on traktowany jako zwykły ciąg tekstowy.

**Uwaga:** Powyższe zachowanie *(automatyczne wstawianie {{ASCII|61|24}})* ma kilka nieprzyjemnych konsekwencji:

-   Jeśli chcesz zachować kolumnę nazw odpowiadającą [nazwie alias](#alias_name.md) w sąsiedniej kolumnie wartości, musisz wprowadzić nazwę w kolumnie etykiety \"przed\" podaniem komórki w wartości kolumna jego alias-name. W przeciwnym razie, gdy wprowadzisz nazwę aliasu w kolumnie etykiety, arkusz kalkulacyjny przyjmie, że jest to wyrażenie i zmieni go na „=". Wyświetlany tekst będzie wtedy wartością z komórki .
-   Jeśli popełnisz błąd podczas wpisywania nazwy w kolumnie etykiety i chcesz go poprawić, nie możesz po prostu zmienić go na nazwę aliasu. Zamiast tego musisz najpierw zmienić nazwę aliasu na inną, następnie poprawić nazwę tekstową w kolumnie etykiety, a kolejnie zmienić nazwę aliasu w kolumnie wartości z powrotem na oryginalną.

One way to side-step these issues is to prefix text labels corresponding to alias-names with a fixed string, thereby making them different. Note that \"\_\" will not work, as it is converted to \"=\". However, a blank, while invisible, will work.

The following table shows some examples assuming the model has a feature named \"MyCube\":

  CAD-Data                                     Cell in Spreadsheet            Result
    
  Parametric Length of a Part-Workbench Cube   =MyCube.Length                 Length with units mm
  Volume of the Cube                           =MyCube.Shape.Volume           Volume in mm³ without units
  Type of the Cube-shape                       =MyCube.Shape.ShapeType        String: Solid
  Label of the Cube                            =MyCube.Label                  String: MyCube
  x-coordinate of center of mass of the Cube   =MyCube.Shape.CenterOfMass.x   x-coordinate in mm without units

### Dane arkusza kalkulacyjnego w wyrażeniach 

In order to use spreadsheet data in other parts of FreeCAD, you will usually create an [Expression](Expressions.md) that refers to the spreadsheet and the cell that contains the data you want to use. You can identify spreadsheets by name or by label, and you can identify the cells by address or by alias. Autocompletion is available for all forms of referencing.

++++
|                 | Spreadsheet by Name                                 | Spreadsheet by Label                                   |
+=================+=====================================================+========================================================+
| Cell by Address |                                      |                                         |
|                 | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                 |                                                  |                                                     |
++++
| Cell by Alias   |                                      |                                         |
|                 | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                 |                                                  |                                                     |
++++


<div class="mw-collapsible mw-collapsed">

The recommended way to refer to spreadsheet data is to use the spreadsheet label and cell alias name. For a more in-depth explanation of the pros and cons of the addressing modes, see the expanded section below.


<div class="mw-collapsible-content">

Using the spreadsheet label has the advantage that it can be freely changed to describe the contents of the spreadsheet. It is also easier to identify the spreadsheet that is being used since the text in the expression matches the label shown in the model and property views. If you decide to change the label of a spreadsheet, existing references to the contents of the spreadsheet will be updated, so you won\'t break your expressions by renaming the spreadsheet. The internal name of the spreadsheet is not readily available anywhere except within the expression editor, so if you use the internal name and later decide to rename the spreadsheets, you might have a hard time tracing your expression data back to its source.

Be aware that when you create a new spreadsheet, the name and the label are the same, so it is easy to accidentally use the spreadsheet name instead of the label. A simple way to avoid this is to give the spreadsheet a meaningful name before starting to use it in expressions.

While you may use the row and column number in an expression to reference a cell, best practice is to give the cell an alias name and use that. See [Cell Properties](#Cell_Properties.md) above on how to set the alias. For example, if the data in cell B1 contained the length parameter for an object, an alias name of `MyObject_Length` would allow the value to be referred to as `<<MyParams>>.MyObject_Length` instead of `Spreadsheet.B1`. Besides being much easier to read and understand, alias names are also much easier to change if you decide to adjust the structure of your spreadsheet. Using an alias also has the advantage that it is reasier to see which cells are used to control other parts of the document. Note that FreeCAD will automatically adjust the positional references in expressions if you insert or remove rows and columns in the spreadsheet, so even if you use row and column numbers in an expression, you can insert rows and columns without breaking the references to the surrounding cells.


</div>


</div>

### Complex models and recomputes 

Editing a spreadsheet will trigger a recompute of the 3D model, even if the changes do not affect the model. For a complex model a recompute can take a long time, and having to wait after every single edit is of course quite annoying.

There are three solutions to deal with this:

1.  Temporarily skip recomputes:
    -   In the [Tree view](Tree_view.md) right-click the <img alt="" src=images/Document.svg  style="width:24px;"> document that contains the spreadsheet.
    -   Select the **Skip recomputes** option from the context menu.
    -   There is a big disadvantage to this solution. New values entered in the spreadsheet will not be displayed until the document is recomputed. Instead `#PENDING` is shown.
    -   You can either recompute manually, using the [Std Refresh](Std_Refresh.md) command, or disable **Skip recomputes** when you are done editing.
2.  Use a macro to automatically skip recomputes while editing a spreadsheet:
    -   Download and run [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   This solution saves a few steps compared to the first solution, but also has the mentioned disadvantage.
3.  Put the spreadsheet in a separate [FreeCAD file](File_Format_FCStd.md):
    -   You can reference spreadsheet data from an external {{FileName|.FCStd}} file with this syntax: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   The advantage of having the spreadsheet in another file over switching off recomputes is that the spreadsheet itself does get recomputed.
    -   The disadvantage is that the model won\'t automatically recompute after changes to the spreadsheet.
    -   In the scenario where you first open the \'spreadsheet\' file, change one or more values and then open the \'model\' file, there won\'t be any indication that the model needs to be recomputed. But if both files are open the [Std Refresh](Std_Refresh.md) icon will update correctly for the \'model\' file after changes to the \'spreadsheet\' file.

## Jednostki

The Spreadsheet has a notion of dimension (units) associated with cell values. A number entered without an associated unit has no dimension. The unit should be entered immediately following the number value, with no intervening space. If a number has an associated unit, that unit will be used in all calculations. For example, the multiplication of two lengths with the unit mm gives an area with the unit mm².

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)

You can change the units displayed for a cell value using the properties dialog [units tab](#units_tab.md) (above). This does not change the value contained in the cell; it only converts the existing value for display. The value used for calculations does not change, and the results of formulas using the value do not change. For example, a cell containing the value \"5.08cm\" can be displayed as \"2in\" by changing the units tab value to \"in\".

A dimensionless number cannot be changed to a number with a unit by the cell properties dialog. One can put in a unit string, and that string will be displayed; but the cell still contains a dimensionless number. In order to change a dimensionless value to a value with a dimension, the value itself must be re-entered with its associated unit.

Occasionally it may be desirable to get rid of a dimension in an expression. This can be done by multiplying by 1 with a reciprocal unit.

## Importowanie i eksportowanie 

### Format CSV 

Arkusze kalkulacyjne FreeCAD mogą być importowane i eksportowane do formatu [CSV](https://en.wikipedia.org/wiki/Comma-separated_values), który może być również odczytywany i zapisywany przez większość innych aplikacji arkuszy kalkulacyjnych, takich jak Microsoft Excel czy LibreOffice Calc. Więcej informacji na ten temat można znaleźć na stronach [Import](Spreadsheet_Import/pl.md) i [Eksport](Spreadsheet_Export/pl.md).

### Format XLSX 

Arkusze kalkulacyjne w formacie Excel XLSX można importować za pomocą polecenia [Importuj](Std_Import/pl.md) lub polecenia [Otwórz](Std_Open/pl.md). Obsługiwane są następujące funkcje:

-   Wszystkie funkcje, które są dostępne także w arkuszu kalkulacyjnym FreeCAD. Inne funkcje powodują wystąpienie błędu w odpowiedniej komórce po zaimportowaniu.
-   Nazwy aliasów dla komórek.
-   Więcej niż jeden arkusz w arkuszu kalkulacyjnym Excel. W takim przypadku dla każdego arkusza Excela tworzony jest jeden arkusz kalkulacyjny FreeCAD.

Inne funkcje nie są importowane do arkusza kalkulacyjnego FreeCAD.

## Wydruki

Aby zachować ustawienia strony niezbędne do drukowania, arkusze kalkulacyjne FreeCAD można drukować, wstawiając je do obiektu [widok Arkusza Kalkulacyjnego](TechDraw_SpreadsheetView/pl.md).

## Obecne ograniczenia 

FreeCAD sprawdza, czy istnieją zależności cykliczne. Z założenia sprawdzanie to zatrzymuje się na poziomie obiektu arkusza kalkulacyjnego. W konsekwencji nie powinieneś mieć arkusza kalkulacyjnego zawierającego zarówno komórki, których wartości są używane do określania parametrów modelu, jak i komórki, których wartości wykorzystują dane wyjściowe z modelu. Na przykład nie można mieć komórek określających długość, szerokość i wysokość obiektu, a inna komórka odwołuje się do całkowitej objętości wynikowego kształtu. Ograniczenie to można obejść, mając dwa arkusze kalkulacyjne: jeden używany jako źródło danych dla parametrów wejściowych do modelu, a drugi używany do obliczeń opartych na danych wynikowych geometrii.

## Podstawy pisania skryptów 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/pl
