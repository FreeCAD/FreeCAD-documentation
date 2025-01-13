# Gui Command/pl
Polecenia Gui to jedna z najważniejszych funkcji FreeCAD, stanowiąca główny punkt interakcji użytkownika. Za każdym razem, gdy użytkownik wybiera pozycję z menu lub naciska przycisk paska narzędziowego, aktywowane zostaje GuiCommand. Niektóre z atrybutów GuiCommand to:

-   Definiuje nazwę,
-   Zawiera ikonę,
-   Określa zakres operacji cofania/przywracania,
-   Posiada stronę pomocy,
-   Otwiera i kontroluje okna dialogowe,
-   Nagrywanie makr,
-   i inne.



## Nazwy

Polecenie Gui jest nazwane w standardowy sposób: *NazwaModułu_NazwaPolecenia*, na przykład \"[Base_Open](Base_Open.md)\" to polecenie otwierania w interfejsie graficznym w systemie Base. Nazwa polecenia Gui w określonym module zawiera nazwę modułu na początku, na przykład \"[Part_Cylinder](Part_Cylinder/pl.md)\".

Jeśli dokumentacja nie jest ukończona, użyj szablonu [Template:UnfinishedDocu](Template_UnfinishedDocu.md).



## Strona pomocy 

Każde polecenie Gui musi mieć stronę pomocy. Strona pomocy jest hostowana w serwisie Wiki dokumentacji programu FreeCAD. Artykuł ma taką samą nazwę jak polecenie Gui, na przykład [Draft ShapeString](Draft_ShapeString/pl.md).

Do tworzenia własnych stron pomocy można użyć szablonu [GuiCommand model](GuiCommand_model/pl.md).

Przykład:

-   [Draft ShapeString](Draft_ShapeString/pl.md)
-   [Draft Line](Draft_Line/pl.md)



## Ikony

<img alt="" src=images/Tango-Palette.png  style="width:400px;">

Każde polecenie Gui musi mieć ikonę. Używamy zestawu ikon [Tango](http://tango-project.org/Tango_Desktop_Project/) i jego wytycznych. Po prawej stronie widzisz paletę kolorów Tango.

Wszystkie ikony powinny być tworzone w formacie [SVG](SVG/pl.md) za pomocą aplikacji do tworzenia obrazów wektorowych, takiej jak [Inkscape](http://inkscape.org). Ułatwia to wprowadzanie zmian i tworzenie dodatkowych ikon w tej samej przestrzeni aplikacji.



### Tabela kodowania kolorami ikon 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Staramy się jak najbardziej przestrzegać tego schematu, więc kolor ikon ma bezpośrednie znaczenie.



---
⏵ [documentation index](../README.md) > Gui Command/pl
