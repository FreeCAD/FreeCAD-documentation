# WikiPages/pl
 {{TOCright}}

Ta strona jest rozszerzeniem strony [Pomoc: Edycja](Help:Editing.md) i podaje wspólne wytyczne dotyczące pisania i aktualizowania dokumentacji wiki FreeCAD. Podsumowuje kilka dyskusji i sesji burzy mózgów.

## Zanim rozpoczniesz pracę 

-   Ta dokumentacja wiki jest oparta na [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), tym samym oprogramowaniu, które zasila [Wikipedię](https://en.wikipedia.org/wiki/Main_Page). Jeśli już wcześniej brałeś udział w Wikipedii, edycja stron wiki FreeCAD powinna być łatwa.
-   W przeciwieństwie do Wikipedii, wiki FreeCAD jest zabezpieczona przed pisaniem, aby uniknąć spamu. Musisz poprosić o utworzenie konta na [forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   Jeśli nigdy wcześniej nie korzystałeś z oprogramowania wiki, przejdź do [Help:Editing](Help:Editing.md), aby zapoznać się z znacznikami stosowanymi do edycji stron.
-   Informacje na temat zaawansowanego korzystania z oprogramowania Wiki można znaleźć w [MediaWiki Help:Contents](https://www.mediawiki.org/wiki/Help:Contents). Nie wszystkie funkcje MediaWiki są dostępne w Wiki FreeCAD, ale wiele z nich jest dostępnych.
-   Chcemy, aby dokumentacja była przejrzysta i łatwa do odczytania, więc unikaj używania skomplikowanych funkcji. Utrzymuj ją w formie prostej.
-   Użyj piaskownicy do przetestowania swojego kodu, na przykład [FreeCADDocu:Sandbox](FreeCADDocu:Sandbox.md) lub konkretnej strony o nazwie [Sandbox:Yourname](Sandbox:Yourname.md).

Strony Piaskownicy muszą być umieszczone w kategorii Piaskownica. Robi się to poprzez dodanie składni [[Category:Sandbox]] na dole kodu wiki.

-   Proszę zwrócić uwagę na tłumaczenia. Wiki FreeCAD używa automatycznej obsługi tłumaczeń, aby dostarczać strony w wielu językach. Dla każdej strony może istnieć wiele wersji językowych. Na wielu stronach zobaczysz znaczniki takie jak <translate>...</translate> oraz wiele pojedynczych znaczników takich jak . Te ostatnie są tworzone przez system tłumaczeń, nigdy nie należy ich tworzyć ręcznie. Łączą one nagłówki i akapity z ich przetłumaczonymi wersjami. Nie powinieneś ich zmieniać, ponieważ zniszczyłoby to te linki. Można jednak przenosić akapity lub zmieniać ich brzmienie, o ile znaczniki pozostaną z nimi. Jeśli usuwasz nagłówek lub akapit, powinieneś również usunąć należący do niego znacznik. Należy pamiętać, że zmiany w istniejących nagłówkach i akapitach wpływają na aktualne tłumaczenia. Twoje zmiany powinny być tego warte. Nie musisz się martwić o dodawanie nowych materiałów, ponieważ system automatycznie doda nowe tagi po Twoich zmianach. Więcej informacji można znaleźć na stronie [Lokalizacja](Localisation/pl.md) oraz na oryginalnej stronie [Mediawiki:Extension:Translate](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example).

## Wytyczne ogólne 

### Dokładne opisy 

Opisując FreeCAD staraj się być zwięzły i konkretny oraz unikaj powtórzeń. Opisuj co FreeCAD *robi*, a nie czego FreeCAD *nie robi*. Unikaj również kolokwialnych wyrażeń takich jak *parę*. Używaj słowa *kilka*, gdy masz do czynienia z nieokreśloną liczbą, lub określ prawidłową ilość.

Opis niewłaściwy
:   [PartDesign](PartDesign_Workbench/pl.md): Środowisko pracy PartDesign jest stołem roboczym do projektowania części, którego celem jest dostarczenie narzędzi do modelowania złożonych brył części.





Opis dobry
:   [PartDesign](PartDesign_Workbench/pl.md): ma na celu dostarczenie narzędzi do modelowania złożonych brył części.

### Scentralizowane informacje 

Należy unikać powielania tych samych informacji w różnych miejscach. Umieść informacje na nowej stronie i łącze do tej strony z innych stron, które wymagają tych informacji.

Nie używaj funkcji przechodzenia stron *([Pomoc:Edycja\#Szablony i transkluzja stron](Help:Editing#Templates_and_transcluding_pages.md))*, ponieważ utrudnia to tłumaczenie wiki. Używaj tylko szablonów opisanych poniżej w sekcji [\#Szablony](#Szablony.md).

### Stylizacja

Szablony są używane do stylizacji stron pomocy. Nadają one dokumentacji spójny wygląd i sposób działania. Istnieje szablon dla poleceń menu, **Plik → Zapisz**, szablon dla klawiszy, które mają być wciśnięte, **Shift**, dla wyświetlania wartości logicznej, `True`, itd. Proszę zapoznać się z sekcją [\#Szablony](#Szablony.md) przed rozpoczęciem pisania stron pomocy.

### Flagi tymczasowe 

Jeśli pracujesz nad dużą stroną, zaleca się zaznaczenie jej albo jako praca w toku, albo jako niedokończona. Gwarantuje to, że administratorzy Wiki nie zaznaczą twojej strony jako gotowej do tłumaczenia, podczas gdy ty wciąż często ją zmieniasz.

Aby oznaczyć stronę, po prostu dodaj albo **** lub **** jako pierwszą linię do strony. Z **** zapraszasz wszystkich do przyłączenia się i ukończenia strony, podczas gdy z **** możesz wykonać pracę, a inni powinni dać ci trochę czasu.

Po zakończeniu pracy, proszę nie zapomnieć o usunięciu flag!

## Przykłady

Aby szybko zapoznać się ze strukturą i stylem Wiki dla FreeCAD zajrzyj na stronę modelu: [GuiCommand model](GuiCommand_model/pl.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Struktura


<div class="mw-collapsible-content">

[Centrum użytkownika](User_hub/pl.md) zapewnia [Spis treści](Online_Help_Toc/pl.md). Jest on używany jako główny punkt odniesienia do automatycznego budowania pomocy offline, do której można dotrzeć z programu FreeCAD, jak również dokumentacji offline PDF.

Szablon [Template:Docnav](Template:Docnav.md) jest używany do sekwencyjnego linkowania stron, zgodnie ze strukturą [Spisu treści pomocy online](Online_Help_Toc/pl.md). Lista wszystkich szablonów znajduje się w sekcji [Szablony](#Szablony.md).

### Nazwy stron 

Nazwy stron powinny być krótkie, a w odróżnieniu od \"opisu sprawy\" powinny zawierać \"tytuł sprawy\", wszystkie wyrazy poza pierwszym i nazwami własnymi piszemy małymi literami. Jest to styl [używany przez Wikipedię](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Capital_letters#Headings,_headers,_and_captions) dla ich artykułów.

Niewłaściwa nazwa strony:
:   Budowa Samolotów AeroCompany





Prawidłowa nazwa strony:
:   Budowa samolotów AeroCompany

Nazwy stron środowisk pracy o najwyższym poziomie muszą mieć taki format: XYZ Workbench, gdzie XYZ jest nazwą środowiska, na przykład [PartDesign Workbench](PartDesign_Workbench/pl.md). A nazwy stron opisujących polecenia *(lub narzędzia)* należące do danego środowiska muszą mieć taki format: XYZ Command, na przykład [PartDesign Pad](PartDesign_Pad/pl.md). Zwróć uwagę, że powinieneś używać nazwy polecenia tak, jak występuje ona w kodzie źródłowym.

Poprzednią konwencją było używanie dużej litery w tytule: każde słowo powinno zaczynać się wielką literą, chyba że są to artykuły, przyimki, spójniki lub inne cząstki gramatyczne (np. \'of\', \'on\', \'in\', \'a\', \'an\', \'and\'). Istnieje wiele istniejących stron używających tego stylu, ale jest on odradzany dla nowych stron. Zostało to przedyskutowane w wątku na forum [*(Linki z małych liter)* Używaj małych liter w tytułach stron wiki](https://forum.freecadweb.org/viewtopic.php?p=266029#p266029).

### Nagłówki

Podobnie jak nazwy stron, nagłówki akapitów powinny być krótkie i zawierać duże litery. Nie należy używać nagłówków H1 (= Nagłówek =) w znacznikach Wiki, ponieważ tytuł strony jest automatycznie dodawany jako główny nagłówek H1.

### Odnośniki internetowe 

Jeśli to możliwe, powinieneś używać oryginalnej nazwy linku dla linków. Dzięki temu w dokumentacji drukowanej lub offline łatwiej jest znaleźć stronę, do której zastosowano odniesienie. Proszę unikać nieistotnych słów dla linku.

Nieprawidłowy link
:   Aby uzyskać więcej informacji na temat rysowania obiektów 2D kliknij [tutaj](Draft_Workbench/pl.md).





Prawidłowy link
:   Więcej informacji na temat rysowania obiektów 2D można znaleźć w Środowisku pracy [Rysunek roboczy](Draft_Workbench/pl.md).

Preferowany format linku to:

[name of page](Name_of_page.md)

przetłumaczone:

[Nazwa Strony](Nazwa_Strony/pl.md)

Zauważ, że w przypadku części przed znakiem | istotny jest faktyczny link, wielkość liter. Jeśli nazwa Twojej strony to Name_of_page, link nie powiedzie się, jeśli wpiszesz Name_of_Page *(wielka litera P)*. Przed znakiem | wszystkie spacje należy zastąpić podkreśleniami (_). Ma to na celu pomoc tłumaczom korzystającym z oprogramowania tłumaczącego, bez podkreślników link zostałby przetłumaczony przez oprogramowanie, co jest niepożądane.

Aby połączyć się z konkretnym akapitem, dodaj do nazwy strony znak # i jego nagłówek. Przykład:

[WikiPages](WikiPages#Links.md)

przetłumaczone:

[Strona Wiki](WikiPages/pl#Odnośniki.md)

W obrębie tej samej strony możesz pominąć nazwę strony. Przykład:

[Links](#Links.md)

Aby przejść do górnej części strony możesz użyć:

</translate>{{Top}}<translate>

Szablon ten powinien automatycznie wyświetlać poprawny tekst w zależności od tego w jakim języku dana strona jest napisana. Link do góry strony jest szczególnie przydatny w przypadku długich stron, ponieważ pozwala użytkownikowi szybko przeskoczyć z powrotem do spisu treści. Możesz go umieścić na końcu każdego akapitu. Upewnij się, że przed i po szablonie znajduje się pusta linia.

Link do obrazu
:   <img alt="Opcjonalny tekst, który jest wyświetlany po najechaniu kursorem na obszar obrazka\|link=Draft\_Wire/pl" src=images/Draft_Wire.svg  style="width:24px;">.

Aby użyć obrazka jako odsyłacza:

![](images/)

Link do obrazu + link tekstowy
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Polilinia](Draft_Wire/pl.md)

Jeśli pominiesz opcjonalny tekst, sam link zostanie wyświetlony po najechaniu kursorem myszki na obraz, co jest lepszym rozwiązaniem, a także powinieneś dodać link tekstowy po linku do obrazka:

![](images/)_[Polilinia](Draft_Wire/pl.md)

### Strony Środowisk pracy 

Strona najwyższego poziomu powinna zaczynać się od:

-   Opisu do czego służy dane środowisko pracy.
-   Obrazka ilustrującego opis.

Zobacz sekcję [\#Zrzut ekranu](#Zrzut_ekranu.md) dla rozwiązań dotyczących dołączania obrazów.

### Strony poleceń 

Strony komend opisujące narzędzia środowiska pracy nie powinny być zbyt długie, powinny jedynie wyjaśniać, co dana komenda może zrobić, a czego nie, oraz jak jej użyć. Obrazki i przykłady należy ograniczyć do minimum. Poradniki mogą wyjaśniać jak używać danego narzędzia i podawać szczegóły krok po kroku.

Proszę odnieść się do strony [GuiCommand model](GuiCommand_model/pl.md) po więcej szczegółów.

### Poradniki

Dobrze napisany poradnik powinien uczyć, jak szybko osiągnąć pewne praktyczne rezultaty. Nie powinien być zbyt długi, ale powinien zawierać wystarczającą ilość instrukcji krok po kroku i obrazów, aby poprowadzić użytkownika. W miarę rozwoju programu FreeCAD, samouczki mogą stać się nieaktualne, dlatego ważne jest, aby wspomnieć o wersji FreeCAD użytej w poradniku lub wymaganej do jego napisania.

Przykłady można znaleźć na stronie [Poradniki](Tutorials/pl.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Szablony


<div class="mw-collapsible-content">

Stylizacja stron Wiki FreeCAD jest osiągana poprzez użycie ([szablonów i stron pośrednich](Help:Editing#Templates_and_transcluding_pages.md)). Zapewniają one standardowy wygląd i sposób działania wszystkich stron, a także umożliwiają zmianę stylu wiki. Możesz zobaczyć pełną listę zdefiniowanych szablonów wchodząc na stronę [Special:PrefixIndex/Template:](Special:PrefixIndex/Template:.md). Ale proszę używaj tylko szablonów wymienionych w tabelach poniżej. Tylko w bardzo szczególnych przypadkach powinieneś używać bezpośrednio znaczników HTML.

Kliknij na link do szablonu, aby zobaczyć instrukcje użycia szablonu oraz jego implementację. Szablony są potężną funkcją oprogramowania MediaWiki. Powinieneś być doświadczonym użytkownikiem wiki, jeśli chcesz proponować dodatki i modyfikacje do istniejących szablonów. Nieprawidłowo zaimplementowane szablony utrudniają tłumaczenie stron na inne języki, dlatego ich użycie powinno być ograniczone do formatowania tekstu, należy unikać dołączania stron. Zobacz [Pomoc MediaWiki:Szablony](https://www.mediawiki.org/wiki/Help:Templates/pl) aby dowiedzieć się więcej.

### Proste szablony 

Szablony te przyjmują prosty parametr tekstowy i formatują go za pomocą określonego stylu.

+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Szablon                                                                                                       | Wygląd                               | Opis                                                                                                                                                                                                                                                                                                         |
+===============================================================================================================+======================================+==============================================================================================================================================================================================================================================================================================================+
| [Top](Template:Top.md)                                                                                |                       | Użyj go, aby dodać link na początek strony.                                                                                                                                                                                                                                                                  |
|                                                                                                               | {{Top}}                              |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Emphasis](Template:Emphasis.md)                                                                      |                       | Użyj go do zaakcentowania fragmentu tekstu.                                                                                                                                                                                                                                                                  |
|                                                                                                               | **zaakcentowanie**          |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [KEY](Template:KEY.md)                                                                                |                       | Użyj go do wskazania klawisza klawiatury, który należy nacisnąć.                                                                                                                                                                                                                                             |
|                                                                                                               | **Alt**                          |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ASCII](Template:ASCII.md)                                                                            |                       | Użyj go do wskazania klawisza ascii w obrazie *(.svg)*, który musi zostać naciśnięty. Należy wprowadzić żądany znak lub numer kodu ascii tego znaku.                                                                                                                                                         |
|                                                                                                               | {{ASCII|A}}                          |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Button](Template:Button.md)                                                                          |                       | Użyj go do wskazania przycisku w graficznym interfejsie użytkownika, który należy nacisnąć.                                                                                                                                                                                                                  |
|                                                                                                               | **Anuluj**                    |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [RadioButton](Template:RadioButton.md)                                                                |                       | Użyj go, aby wskazać przycisk wyboru w graficznym interfejsie użytkownika, który należy {{RadioButton|TRUE|Zaznaczyć}} lub {{RadioButton|FALSE|Nie}}.                                                                                                                            |
|                                                                                                               | {{RadioButton|Opcja}}                |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [CheckBox](Template:CheckBox.md)                                                                      |                       | Użyj go, aby wskazać pole wyboru w graficznym interfejsie użytkownika, które należy {{CheckBox|TRUE|wybrać}} lub {{CheckBox|FALSE|Nie}}.                                                                                                                                         |
|                                                                                                               | {{CheckBox|Opcja}}                   |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SpinBox](Template:SpinBox.md)                                                                        |                       | Użyj go do wskazania pola wyboru w graficznym interfejsie użytkownika, które ma zostać zmodyfikowane.                                                                                                                                                                                                        |
|                                                                                                               | {{SpinBox|1.50}}                     |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ComboBox](Template:ComboBox.md)                                                                      |                       | Użyj go do wskazania pola listy wyboru w graficznym interfejsie użytkownika, które należy zmienić.                                                                                                                                                                                                           |
|                                                                                                               | {{ComboBox|Menu 1}}                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [FALSE](Template:FALSE.md), [False](Template:False.md)                                        |                       | Użyj go, aby wskazać wartość logiczną False, na przykład, jako właściwość w [Edytorze właściwości](Property_editor/pl.md). To jest skrót. Ponieważ jest to wartość, wywołanego szablonu [Value](Template:Value.md). {{Value|False}}                                            |
|                                                                                                               | {{FALSE/pl}}                         |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | , {{False/pl}}         |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [TRUE](Template:TRUE.md), [True](Template:True.md)                                            |                       | Użyj go, aby wskazać wartość logiczną True, na przykład, jako właściwość w [Edytorze właściwości](Property_editor/pl.md). To jest skrót. Ponieważ jest to wartość, wywołanego szablonu [Value](Template:Value.md). {{Value|true}}                                              |
|                                                                                                               | {{TRUE/pl}}                          |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | , {{true/pl}}          |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [MenuCommand](Template:MenuCommand.md)                                                                |                       | Użyj go do wskazania lokalizacji polecenia wewnątrz danego menu.                                                                                                                                                                                                                                             |
|                                                                                                               | **Plik → Zapisz**        |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [FileName](Template:FileName.md)                                                                      |                       | Użyj go do wskazania nazwy pliku lub katalogu.                                                                                                                                                                                                                                                               |
|                                                                                                               | {{FileName|File name}}               |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SystemInput](Template:SystemInput.md)                                                                |                       | Użyj go do wprowadzenia tekstu wejściowego, wprowadzonego przez użytkownika.                                                                                                                                                                                                                                 |
|                                                                                                               | {{SystemInput|Wprowadź ten tekst}}   |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SystemOutput](Template:SystemOutput.md)                                                              |                       | Użyj go do wskazania tekstu wychodzącego z systemu.                                                                                                                                                                                                                                                          |
|                                                                                                               | {{SystemOutput|Tekst wyjściowy}}     |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Incode](Template:Incode.md)                                                                          |                       | Użyj go, aby dołączyć kod źródłowy w wierszu z czcionką o stałej szerokości. Powinien zmieścić się w jednej linii.                                                                                                                                                                                           |
|                                                                                                               | `import FreeCAD`            |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [PropertyView](Template:PropertyView.md)                                                              |                       | Użyj go, aby wskazać właściwość widoku w [Edytorze właściwości](Property_editor/pl.md). Przykłady właściwości widoku to {{emphasis|Kolor linii}}, {{emphasis|Szerokość linii}}, {{emphasis|Kolor punktu}}, {{emphasis|Rozmiar punktu}}, itd. |
|                                                                                                               | {{PropertyView/pl|Kolor}}            |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [PropertyData](Template:PropertyData.md)                                                              |                       | Użyj go, aby wskazać właściwość Data w [Edytorze właściwości](Property_editor/pl.md). Właściwości danych są różne dla różnych typów obiektów.                                                                                                                                                        |
|                                                                                                               | {{PropertyData/pl|Pozycja}}          |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Properties Title](Template:Properties_Title.md) / [TitleProperty](Template:TitleProperty.md) |                       | Użyj go, aby wskazać nazwę grupy właściwości w [Edytorze właściwości](Property_editor/pl.md). Nazwa nie zostanie uwzględniona w automatycznym spisie treści.                                                                                                                                         |
|                                                                                                               | {{Properties_Title|Podstawowe}}      |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Obsolete](Template:Obsolete.md)                                                                      |                       | Użyj go, aby wskazać, że cecha stała się przestarzała w określonej wersji FreeCAD.                                                                                                                                                                                                                           |
|                                                                                                               | {{Obsolete/pl|0.19}}                 |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Version](Template:Version.md)                                                                        |                       | Użyj go, aby wskazać, że cecha została wprowadzona w określonej wersji FreeCAD.                                                                                                                                                                                                                              |
|                                                                                                               | {{Version/pl|0.18}}                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VersionMinus](Template:VersionMinus.md)                                                              |                       | Użyj go, aby wskazać, że cecha jest dostępna w określonej wersji FreeCAD i wcześniejszych wersjach.                                                                                                                                                                                                          |
|                                                                                                               | {{VersionMinus/pl|0.16}}             |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VersionPlus](Template:VersionPlus.md)                                                                |                       | Użyj go, aby wskazać, że cecha jest dostępna w określonej wersji FreeCAD i nowszych wersjach.                                                                                                                                                                                                                |
|                                                                                                               | {{VersionPlus/pl|0.17}}              |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ColoredText](Template:ColoredText.md)                                                                |                       | Użyj tego szablonu do pokolorowania tła, tekstu lub tła i tekstu. *([ColoredText](Template:ColoredText.md) - strona zawierająca więcej przykładów)*.                                                                                                                                                 |
|                                                                                                               | {{ColoredText|Kolorowy tekst}}       |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ColoredParagraph](Template:ColoredParagraph.md)                                                      |                       | Użyj tego szablonu do pokolorowania tła, tekstu lub tła i tekstu całego akapitu. *([ColoredParagraph](Template:ColoredParagraph.md) strona dla więcej przykładów)*                                                                                                                                   |
|                                                                                                               | {{ColoredParagraph|Kolorowy akapit}} |                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Złożone szablony 

Szablony te wymagają większej ilości parametrów wejściowych, lub generują blok tekstu o określonym formacie.

+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Szablon                                                                                          | Wygląd                                                                                                                   | Opis                                                                                                                                                                                                                                                                                                                                                |
+==================================================================================================+==========================================================================================================================+=====================================================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template:Prettytable.md)                                                   | Ta oto tabela                                                                                                            | Użyj go do formatowania tabel, takich jak ta. Można dodać dodatkowe właściwości tabeli.                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Caption](Template:Caption.md)                                                           |                                                                                                                | Użyj go, aby dodać wyjaśnienie pod obrazem. Możesz ustawić wyrównanie do lewej lub do środka.                                                                                                                                                                                                                                                       |
|                                                                                                  | <div style="width:400px;">                                                                                               |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                           |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  | *Jakiś podpis do obrazka*                                                                                      |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  | </div>                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Clear](Template:Clear.md)                                                               |                                                                                                                          | Użyj go do wyczyszczenia kolumn. Aby uzyskać szczegółowe wyjaśnienie, postępuj zgodnie z definicją szablonu. Jest on często używany do zatrzymania przepływu tekstu obok niepowiązanych obrazów.                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Code](Template:Code.md)                                                                 |                                                                                                           | Użyj go, aby dołączyć wielowierszowe przykłady kodu z czcionką monospace. Domyślnym językiem jest Python, ale można podać inne języki.                                                                                                                                                                                                              |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                             |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       | Użyty kod [Python](Python/pl.md) powinien stosować się do ogólnych zaleceń ustanowionych przez [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). W szczególności, nawiasy powinny następować bezpośrednio po nazwie funkcji, a spacja powinna następować po przecinku. Dzięki temu kod jest bardziej czytelny |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Fake heading](Template:Fake_heading.md)                                                 |                                                                                                           | Użyj go, aby utworzyć nagłówek, który nie będzie automatycznie umieszczany w spisie treści.                                                                                                                                                                                                                                                         |
|                                                                                                  | {{Fake heading|Nagłówek|2}}                                                                                              |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GuiCommand](Template:GuiCommand.md)                                                     | Zobacz [Model polecenia GUI](GuiCommand_model/pl.md)                                                             | Za jego pomocą można utworzyć pole z przydatnymi informacjami do dokumentowania poleceń *(narzędzi)* środowiska pracy.                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [TutorialInfo](Template:TutorialInfo.md)                                                 | Zobacz przykład [Poradnik: Podstawy modelowania](Basic_modeling_tutorial/pl.md)                                  | Użyj go do stworzenia ramki z przydatnymi informacjami, aby udokumentować [Poradniki](Tutoriale/pl.md).                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Macro](Template:Macro.md)                                                               | Zobacz przykład [Macro FlattenWire](Macro_FlattenWire.md)                                                        | Użyj go do stworzenia ramki z przydatnymi informacjami, aby udokumentować [makrodefinicje](macros/pl.md).                                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Docnav](Template:Docnav.md)                                                             |                                                                                                           | Za jego pomocą można utworzyć pasek ze słowami *następna*, *poprzednia* i *indeks* oraz odpowiednimi linkami, co jest przydatne do umieszczania stron w określonej kolejności.                                                                                                                                                                      |
|                                                                                                  |                                                                  |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VeryImportantMessage](Template:VeryImportantMessage.md)                                 |                                                                                                           | Użyj go, aby utworzyć wyróżnione pole z bardzo ważną wiadomością. Używaj rzadko, tylko do wskazania poważnych problemów w funkcjonalności oprogramowania, zaprzestania używania narzędzi itp.                                                                                                                                                       |
|                                                                                                  | **Ważny komunikat**                                                                                 |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Page in progress](Template:Page_in_progress.md)                                         |                                                                                                           | Użyj tego dla stron, które są w trakcie tworzenia lub które są obecnie przerabiane. Nie zapomnij usunąć tej opcji, gdy strona będzie gotowa.                                                                                                                                                                                                        |
|                                                                                                  | {{Page in progress|Strona w realizacji}}                                                                                 |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [UnfinishedDocu](Template:UnfinishedDocu.md)                                             |                                                                                                           | Użyj go, aby utworzyć podświetlone pole wskazujące niedokończoną stronę dokumentacji.                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                        |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Softredirect](Template:Softredirect.md)                                                 |                                                                                                                          | Użyj go zamiast normalnego przekierowania, gdy przekierowujesz na specjalną stronę *(taką jak Media: lub Kategoria:)*, w których to przypadkach normalne przekierowanie jest wyłączone.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Quote](Template:Quote.md)                                                               |                                                                                                           | Użyj go, aby utworzyć pole tekstu z dosłownym cytatem i odniesieniem.                                                                                                                                                                                                                                                                               |
|                                                                                                  | {{Quote|text=Krzyknij "Havoc" i wypuść psy wojny. |sign=William Shakespeare|source=''Juliusz Cezar'', akt III, scena I}} |                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Userdocnavi](Template:Userdocnavi.md), [Powerdocnavi](Template:Powerdocnavi.md) |                                                                                                                          | Użyj ich do stworzenia okien nawigacyjnych dla dokumentacji użytkownika, dokumentacji użytkownika zaawansowanych funkcji oraz dokumentacji programisty. Pozwala to na szybkie przeskakiwanie pomiędzy różnymi sekcjami dokumentacji. Umieszczają one również odpowiednią stronę we właściwej kategorii.                                             |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Grafika


<div class="mw-collapsible-content">

Obrazy i zrzuty ekranu są niezbędne do stworzenia kompletnej dokumentacji programu FreeCAD. Są one szczególnie przydatne do ilustrowania przykładów i samouczków. Obrazy powinny być wyświetlane w ich oryginalnym rozmiarze, tak aby prezentowały wystarczającą ilość szczegółów i były czytelne, jeśli zawierają tekst. Obrazy w formacie [Bitmap](bitmap/pl.md) nie powinny być zmieniane.

Unikaj animowanych obrazów *(GIF)* na ogólnych stronach pomocy. Animacje i filmy powinny być zarezerwowane dla samouczków, które nie są przeznaczone do użycia jako dokumentacja PDF offline.

Pliki graficzne mogą być załadowane poprzez stronę [Special:Upload](Special:Upload.md).

### Nazwa

Nadawaj obrazkom znaczące nazwy. Jeśli masz obrazek, który pokazuje charakterystykę konkretnego polecenia, powinieneś użyć nazwy tego polecenia z `_example` na końcu. Na przykład dla polecenia [Draft Offset](Draft_Offset/pl.md) obrazek powinien mieć nazwę `Draft_Offset_example.jpg`.

### Zrzut ekranu 

Zalecane rozmiary dla zrzutów ekranu to:

-   Natywny 400x200 *(lub szerokość=400 i wysokość\<=200)*, dla stron [command reference](GuiCommand_model.md), aby obrazek zmieścił się w lewej części strony, oraz dla innych standardowych zrzutów.
-   Natywny 600x400 *(lub szerokość=600 i wysokość\<=400)*, dla stron [command reference](GuiCommand_model.md), kiedy naprawdę potrzebujesz większego obrazka, i nadal pozwalasz obrazkowi zmieścić się w lewej części strony, oraz dla innych standardowych zrzutów.
-   Natywny rozmiar 1024x768 *(lub szerokość=1024 i wysokość\<=768)*, tylko dla obrazów pełnoekranowych.
-   Mniejsze rozmiary są możliwe przy wyświetlaniu szczegółów.
-   Unikaj obrazów o większych rozdzielczościach, ponieważ nie będą one wystarczająco dopasowane do innych rodzajów wyświetlaczy lub drukowanej dokumentacji PDF.

Nie powinieneś polegać na niestandardowej konfiguracji pulpitu lub systemu operacyjnego podczas tworzenia zrzutów ekranu i powinieneś używać domyślnych ustawień wizualnych interfejsu FreeCAD, kiedy tylko jest to możliwe.

Aby utworzyć zrzuty ekranu, możesz użyć opcji dostarczonych przez system operacyjny lub jednej z tych makroinstrukcji: <img alt="" src=images/Snip.png  style="width:24px;"> [Macro Snip](Macro_Snip.md) lub <img alt="" src=images/Macro_Screen_Wiki.png  style="width:24px;"> [Macro Screen Wiki](Macro_Screen_Wiki.md).

### Treść

Aby ułatwić tłumaczenie dokumentacji, staraj się unikać zrzutów ekranu, które zawierają teksty. Jeśli nie możesz tego uniknąć, rozważ zrobienie osobnych zrzutów ekranu interfejsu i okna [widoku 3D](3D_view/pl.md). Obraz widoku 3D może być ponownie użyty w każdym tłumaczeniu, podczas gdy tłumacz może w razie potrzeby wykonać zrzut ekranu zlokalizowanego interfejsu.

### Ikonki i grafika 

Odnieś się do strony [Artykuły](Dzieło_sztuki.md), aby zobaczyć wszystkie grafiki i ikony, które zostały stworzone dla FreeCAD, a które mogą być również użyte na stronach dokumentacji. Jeśli chciałbyś dodać ikony, proszę przeczytaj [Artwork Guidelines](Artwork_Guidelines.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Tłumaczenia


<div class="mw-collapsible-content">

Zgodnie z ogólnym konsensusem, strona referencyjna w Wiki jest stroną angielską, która powinna być utworzona jako pierwsza. Jeśli chcesz zmienić lub dodać treść do strony, powinieneś zrobić to najpierw na angielskiej stronie, a dopiero po zakończeniu aktualizacji przenieść modyfikację na przetłumaczoną stronę.

FreeCAD Wiki wspiera rozszerzenie tłumaczenia, które pozwala na łatwiejsze zarządzanie tłumaczeniami między stronami; szczegóły w [Tłumaczenie dokumentacji Wiki dla FreeCAD](Localisation/pl#T.C5.82umaczenie_dokumentacji_Wiki_dla_FreeCAD.md).

Inne przydatne zasoby to:

-   [Kody ISO języków](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) aby określić dwuliterowy kod dla danego języka, na który chcesz tłumaczyć.
-   [Google Translate](http://translate.google.com/) do pomocy przy tłumaczeniach.
-   [tłumacz Deepl](https://www.deepl.com/translator) do pomocy przy tłumaczeniach.

## Kilka wskazówek dla tłumaczy 

### Tłumaczenie komend Gui 

    {{GuiCommand
    |Name=FEM EquationFluxsolver
    |MenuLocation=Solve → Equation fluxsolver
    |Workbenches=[FEM](Fem_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

przetłumaczone:

    {{GuiCommand/fr
    |Name=FEM EquationFluxsolver
    |Name/fr=FEM EquationFluxsolver
    |MenuLocation=Solveur → Equation fluxsolver
    |Workbenches=[Atelier FEM](Fem_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutoriel](FEM_tutorial/fr.md)
    }}

### Ustawienia szablonu 

    {{FEM_Tools_navi}}

przetłumaczone:

    {{FEM_Tools_navi/fr}}

### Tłumaczenie odnośnika 

    [Part Module](Part_Module.md)

przetłumaczone:

    [Atelier Pièces](Part_Module/fr.md)

### Tłumaczenie Docnav 

    

przetłumaczone:

    

Przykład z ikonami:

    

przetłumaczone:

    


</div>


</div>

## Tworzenie, zmiana nazwy i usuwanie strony 

### Tworzenie stron 

Przed utworzeniem nowej strony powinieneś najpierw sprawdzić, czy podobna strona już istnieje. Jeśli tak, to zazwyczaj lepiej jest edytować istniejącą stronę. W razie wątpliwości najpierw otwórz temat na forum w dziale [Wiki forum](https://forum.freecadweb.org/viewforum.php?f=21).

Aby utworzyć nową stronę wykonaj jedną z poniższych czynności:

-   Odwiedź adres URL z żądaną nazwą strony, na przykład: https://wiki.freecadweb.org/Moja_nowa_strona, i kliknij na przycisk *utwórz tą stronę*.
-   Wyszukaj w Wiki nazwę strony i kliknij na czerwony tekst w \'\'Utwórz stronę **Moja nowa strona** w tej Wiki!\'.

### Zmiana nazwy stron 

Ponieważ FreeCAD jest projektem w ciągłym rozwoju, czasami jest konieczne zrewidowanie zawartości Wiki. Jeśli nazwy poleceń są zmieniane w kodzie źródłowym, strony wiki je dokumentujące również muszą być zmieniane. To może być zrobione tylko przez administratorów Wiki. Aby ich o tym poinformować, otwórz temat na forum [forum Wiki](https://forum.freecadweb.org/viewforum.php?f=21) i w tym formularzu opisz konieczną operację zmiany nazwy:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...

### Usuwanie plików i stron 

W przypadku, gdy chcesz usunąć plik, przejdź na jego stronę (https://www.freecadweb.org/wiki/File:***.***) i edytuj ją. Nie ważne czy strona jest pusta czy nie, dodaj to jako pierwszy element: {{Delete}} i bezpośrednio pod nim opisać, dlaczego strona powinna zostać usunięta. Dodatkowo, otwórz temat w dziale [forum Wiki](https://forum.freecadweb.org/viewforum.php?f=21).

Dla stron procedura jest taka sama.

## Dyskusja

Subforum [Development/Wiki](http://forum.freecadweb.org/viewforum.php?f=21) w [FreeCAD forum](https://forum.freecadweb.org) zapewnia dedykowaną przestrzeń do dyskusji na tematy Wiki, wygląd i wszystko inne związane z Wiki. Kieruj tam swoje pytania i sugestie.

## Terminologia - Zasady nazewnictwa 

### Angielski

Zobacz [Słownik](Glossary.md)

### Inne języki 

-   [włoski](Italian_Translation.md)
-   [francuski](French_Translation.md)
-   [niemiecki](German_Translation.md)
-   [polski](Polish_translation.md)

[Category:Documentation](Category:Documentation.md) [Category:Wiki](Category:Wiki.md) [Category:Wiki Documentation](Category:Wiki_Documentation.md) [Category:Administration](Category:Administration.md)
