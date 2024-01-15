# Svg Namespace/pl
**Rozwój Środowiska pracy [Kreślenie](Drawing_Workbench/pl.md) zatrzymał się w FreeCAD '''0.16''', a nowe środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) mające na celu zastąpienie go zostało wprowadzone w wersji '''0.17'''. Oba Środowiska pracy są nadal dostępne w wersji '''0.17''' do '''0.21''', ale środowisko pracy Kreślenie nie jest już dołączane od wersji '''0.21'''.**


{{Message|Obecnie środowisko pracy Rysunek Techniczny nadal wykorzystuje atrybut '''freecad:EditableText''' i związaną z nim deklarację przestrzeni nazw w swoich aktualnych szablonach.}}






## Wprowadzenie

FreeCAD może importować i eksportować dokumenty [SVG](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) zawierające kod należący do określonej \"przestrzeni nazw\", która jest podzbiorem instrukcji XML.

Jak każdy dokument XML, dokument SVG składa się z dwóch sekcji:

-   Nagłówka: to zaledwie jeden wiersz deklarujący, która wersja języka XML jest używana dla instrukcji w treści tego dokumentu.
-   Treść: lista instrukcji. Dokumenty SVG zawierają wszystkie instrukcje w znacznikach<svg>.

:   Znacznik otwierający zawiera informacje o rozmiarze i używanych przestrzeniach nazw SVG.



## Domyślna przestrzeń nazw 

Domyślna przestrzeń nazw SVG używana przez FreeCAD jest zadeklarowana w tym wierszu:


{{Code|lang=xml|code=
xmlns="http://www.w3.org/2000/svg" version="1.1"
}}

Zewnętrzny link prowadzi do strony internetowej zawierającej informacje o przestrzeni nazw i jej zestawie instrukcji. Atrybuty tej przestrzeni nazw są używane bez przedrostka.



## Rozszerzenie przestrzeni nazw 

Atrybuty brakujące w przestrzeni nazw SVG mogą być dodawane przez rozszerzenia przestrzeni nazw. FreeCAD używa takiego rozszerzenia dla szablonów rysunkowych. Szablony dla Drawing workbench używają czterech niestandardowych atrybutów, które są oznaczone prefiksem \"freecad:\":

-   [freecad:EditableText](#freecad_EditableText.md), jest on nadal używany z szablonami dla środowiska pracy TechDraw.
-   [freecad:basepoint1](#freecad_basepoint1.md).
-   [freecad:basepoint2](#freecad_basepoint2.md)
-   [freecad:dimpoint](#freecad_dimpoint.md)

Deklaracja przestrzeni nazw jest używana do wprowadzenia prefiksu i linku do powiązanej strony internetowej, **tej strony**:


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
}}

Link nie jest używany do pobierania informacji lub wartości w czasie wykonywania, ale jest kluczem do aktywacji niestandardowych atrybutów.



### Szablony rysunków 

W dokumentach [SVG](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) eksportowanych przez środowisko pracy [Kreślenie](Drawing_Workbench/pl.md) programu FreeCAD i używanych jako *(rysunkowe)* [szablony](Drawing_templates/pl.md) stron, mogą być używane niestandardowe [atrybuty](http://www.w3schools.com/xml/xml_attributes.asp), pierwotnie do użytku wewnętrznego FreeCAD, ale mogą być również używane przez inne aplikacje obsługujące FreeCAD w przyszłości. Wszystkie te atrybuty używają prefiksu **freecad:** [przestrzeni nazw](http://www.w3schools.com/xml/xml_namespaces.asp). Adres URL przestrzeni nazw zdefiniowany w tych dokumentach SVG odnosi się do tej strony.

:   środowisko pracy Kreślenie nie jest już zawarte w podstawowym pakiecie FreeCAD {{VersionPlus/pl|0.21}}, więc te szablony Rysunku są już nieaktualne.



### Szablony Rysunku Technicznego 

Środowisko pracy Rysunek Techniczny również używa szablonów SVG, ale nie może tworzyć i eksportować szablonów. Opiera się na [freecad:EditableText](#freecad_EditableText.md) dla wpisów w blokach tytułowych.



### Migracja do freecad.org 

Ponieważ wiki FreeCAD, w tym **ta strona**, została przeniesiona z **freecadweb.org** do **freecad.org** w wersji 0.21, link musi zostać odpowiednio zaktualizowany:


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
}}

Zaktualizowane szablony Rysunku Technicznego zawierają teraz klucz, który nie może aktywować niestandardowych atrybutów, gdy są używane z FreeCAD {{VersionMinus/pl|0.20}}, w wyniku czego edytowalne teksty ostatnich szablonów nie są rozpoznawane i są traktowane jako zwykły tekst.

:   W takich przypadkach \"web\" musi zostać ręcznie ponownie wstawiony do deklaracji przestrzeni nazw szablonu.

Wygląda na to, że {{VersionPlus/pl|0.21}} może obsługiwać oba adresy linków.



## Użycie

Jeden piksel = jeden milimetr.

Musisz wstawić, gdzieś wewnątrz swojego kodu svg, gdzie chcesz, aby zawartość rysunku się pojawiła *(na przykład na końcu pliku, tuż przed ostatnim znacznikiem*\'


</svg>

*\')*, następującą linię:

 xml



 xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Aby umożliwić drukowanie w skali, rzeczywisty rozmiar słowa musi być podany w atrybutach szerokość i wysokość znacznika SVG. Wielkość dokumentu w jednostkach użytkownika *(px)* musi być podana w atrybucie **viewBox**.

Poniższe dane mają być sformatowane jak w podanym przykładzie, gdzie:

-   xxx = szerokość piksela,
-   yyy = wysokość w pikselach.

 xml
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


Dodatkowe informacje dotyczące przestrzeni roboczej i bloku tytułu mogą zostać dodane i są zdefiniowane na stronie [Szablony rysunków](Drawing_templates/pl.md).



## Atrybuty



### [freecad:EditableText](#Przykład_kodu_freecad_EditableText.md)

Aby użyć któregokolwiek z atrybutów **freecad:** w dokumentach SVG, musisz najpierw zdefiniować przestrzeń nazw freecad jako atrybut otwierany znacznikiem


<svg>

Definiuje tekst w szablonie, który może być edytowany przez FreeCAD.

Przykład:

 xml
<text freecad:EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad:basepoint1

Określa pierwszy punkt obiektu [Wymiarowanie](Draft_Dimension/pl.md) *(reprezentowanego jako grupa w dokumencie SVG)*. Atrybut ten jest używany podczas importu fragmentu SVG w programie FreeCAD, w celu odtworzenia obiektu wymiarowego. Grupa zawiera ścieżki i inne elementy graficzne do poprawnego renderowania obiektu wymiarowego w innych aplikacjach SVG.

Przykład:

 xml
<g freecad:basepoint1="0.5 4.34" freecad:basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>


### freecad:basepoint2

Określa drugi punkt obiektu [Wymiarowanie](Draft_Dimension/pl.md) *(reprezentowanego jako grupa w dokumencie SVG)*. Atrybut ten jest używany podczas importu fragmentu SVG w programie FreeCAD, w celu odtworzenia obiektu wymiarowego. Grupa zawiera ścieżki i inne elementy graficzne do poprawnego renderowania obiektu wymiarowego w innych aplikacjach SVG.

Przykład: zobacz [freecad:basepoint1](#freecad_basepoint1.md)

### freecad:dimpoint

Określa punkt obiektu [Wymiarowanie](Draft_Dimension/pl.md), przez który przechodzi linia wymiarowa. Ten atrybut jest używany podczas importowania fragmentu SVG w programie FreeCAD, w celu odtworzenia obiektu wymiarowego. Grupa zawiera ścieżki i inne elementy graficzne do poprawnego renderowania obiektu wymiarowego w innych aplikacjach SVG.

Przykład: zobacz [freecad:basepoint1](#freecad_basepoint1.md)



### Przykład kodu freecad:EditableText 

Ten przykład został przeniesiony z tabeli na arkusz [A3 Poziomy](Misc_templates/pl#A3_Poziomy_tekst_US.2C_kompletny_z_konwencj.C4.85_US.md)



#### 1 : Tytuł bez pola textedit 

<img alt="" src=images/Svg_Namespace_01.png  style="width:300px;">

 xml
  <g
     id="g3587">
    <text
       sodipodi:linespacing="119.00001%"
       id="text3482"
       y="229.10912"
       x="220.8476"
       style="font-size:1.97555566px;font-style:normal;font-weight:normal;line-height:119.00000572%;letter-spacing:0.01975556px;word-spacing:0.00846667px;writing-mode:lr-tb;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"
       xml:space="preserve"><tspan
         y="229.10912"
         x="220.8476"
         id="tspan3484"
         sodipodi:role="line">AUTHOR NAME :</tspan></text>




#### 2 : Tytuł z polem textedit 

<img alt="" src=images/Svg_Namespace_02.png  style="width:300px;">

 xml
  <g
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">
    <text
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"
       freecad:editable="AuthorName"><tspan
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>
    <text
    ...
    ...
    ...
    ... </text>
  
  </g>




#### Objaśnienia

 xml
  <g


Początek struktury

 xml
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">


Dane struktury

 xml
    <text


Początek bloku tekstu

 xml
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"


Wszystkie informacje o tekście, który będzie wyświetlany

 xml
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"


Współrzędne i identyfikator gdzie pojawi się tekst

 xml
       freecad:editable="AuthorName"><tspan


Tutaj **AuthorName** jest zmienną zarządzaną przez **freecad:editable**, zapisującą ciąg znaków do zmiany, który zostanie wyświetlony

 xml
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Współrzędne i identyfikator tekstu , który jest wyświetlany domyślnie, a **** oznacza koniec tekstu bloku

 xml
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Inne bloki tekstowe i koniec **** struktury grupowania bloków tekstowych

Jest możliwe, że po pracy z plikiem SVG Inkscape\'a plik już nie działa, możliwe, że zaginęły informacje.

Następnie sprawdź, czy tekst edycji nie jest zmodyfikowany

Przykład:

-   **editable** = \"AuthorName\"
-   zastąpiony przez **freecad:editable** = \"AuthorName\"



## Inne dostępne atrybuty 

Zobacz [Szablony środowiska Kreślenie](Drawing_templates/pl.md)


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/pl
