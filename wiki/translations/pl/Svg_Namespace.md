# Svg Namespace/pl
**Rozwój Środowiska pracy [Kreślenie](Drawing_Workbench/pl.md) zatrzymał się w FreeCAD '''0.16''', a nowe Środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) mające na celu zastąpienie go zostało wprowadzone w wersji '''0.17'''. Oba Środowiska pracy są nadal dostępne w wersji '''0.17''', ale środowisko pracy Kreślenie może zostać usunięte w przyszłych wydaniach.**


{{TOCright}}

W dokumentach [SVG](http   *//en.wikipedia.org/wiki/Scalable_Vector_Graphics) eksportowanych przez środowisko [Kreślenie](Drawing_Workbench/pl.md) i używanych jako strony [szablonów](Drawing_templates.md), może zostac użytych kilka niestandardowych [atrybutów](http   *//www.w3schools.com/xml/xml_attributes.asp). Pierwotnie do użytku wewnętrznego programu FreeCAD, ale mogą być również używane przez inne aplikacje obsługujące FreeCAD w przyszłości. Wszystkie te atrybuty używają prefiksu **freecad   *** [przestrzeni nazw](http   *//www.w3schools.com/xml/xml_namespaces.asp). URL przestrzeni nazw zdefiniowany w tych dokumentach SVG odnosi się do tej strony.

## Użycie

Jeden piksel = jeden milimetr.

Musisz wstawić, gdzieś wewnątrz swojego kodu svg, gdzie chcesz, aby zawartość rysunku się pojawiła \'\'(na przykład na końcu pliku, tuż przed ostatnim znacznikiem \'\'\'


</svg>

*\')*, następującą linię   *

 {.xml}



 {.xml}
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    xmlns   *freecad="http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Aby umożliwić drukowanie w skali, rzeczywisty rozmiar słowa musi być podany w atrybutach szerokość i wysokość znacznika SVG. Wielkość dokumentu w jednostkach użytkownika *(px)* musi być podana w atrybucie **viewBox**.

Poniższe dane mają być sformatowane jak w podanym przykładzie, gdzie   *

-   xxx = szerokość piksela,
-   yyy = wysokość w pikselach.

 {.xml}
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


Dodatkowe informacje dotyczące przestrzeni roboczej i bloku tytułu mogą zostać dodane i są zdefiniowane na stronie [Szablony rysunków](Drawing_templates/pl.md).

## Atrybuty

### [freecad   *EditableText](#Przykład_kodu_freecad_EditableText.md)

Aby użyć któregokolwiek z atrybutów **freecad   *** w dokumentach SVG, musisz najpierw zdefiniować przestrzeń nazw freecad jako atrybut otwierany znacznikiem


<svg>

Definiuje tekst w szablonie, który może być edytowany przez FreeCAD.

Przykład   *

 {.xml}
<text freecad   *EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad   *basepoint1

Określa pierwszy punkt obiektu [Wymiarowanie](Draft_Dimension/pl.md) *(reprezentowanego jako grupa w dokumencie SVG)*. Atrybut ten jest używany podczas importu fragmentu SVG w programie FreeCAD, w celu odtworzenia obiektu wymiarowego. Grupa zawiera ścieżki i inne elementy graficzne do poprawnego renderowania obiektu wymiarowego w innych aplikacjach SVG.

Przykład   *

 {.xml}
<g freecad   *basepoint1="0.5 4.34" freecad   *basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>


### freecad   *basepoint2

Określa drugi punkt obiektu [Wymiarowanie](Draft_Dimension/pl.md) *(reprezentowanego jako grupa w dokumencie SVG)*. Atrybut ten jest używany podczas importu fragmentu SVG w programie FreeCAD, w celu odtworzenia obiektu wymiarowego. Grupa zawiera ścieżki i inne elementy graficzne do poprawnego renderowania obiektu wymiarowego w innych aplikacjach SVG.

Przykład   * zobacz [freecad   *basepoint1](#freecad_basepoint1.md)

### freecad   *dimpoint

Określa punkt obiektu [Wymiarowanie](Draft_Dimension/pl.md), przez który przechodzi linia wymiarowa. Ten atrybut jest używany podczas importowania fragmentu SVG w programie FreeCAD, w celu odtworzenia obiektu wymiarowego. Grupa zawiera ścieżki i inne elementy graficzne do poprawnego renderowania obiektu wymiarowego w innych aplikacjach SVG.

Przykład   * zobacz [freecad   *basepoint1](#freecad_basepoint1.md)

### Przykład kodu freecad   *EditableText 

Ten przykład został przeniesiony z tabeli na arkusz [A3 Poziomy](Misc_templates/pl#A3_Poziomy_tekst_US.2C_kompletny_z_konwencj.C4.85_US.md)

#### 1    * Tytuł bez pola textedit 

<img alt="" src=images/Svg_Namespace_01.png  style="width   *300px;">

 {.xml}
  <g
     id="g3587">
    <text
       sodipodi   *linespacing="119.00001%"
       id="text3482"
       y="229.10912"
       x="220.8476"
       style="font-size   *1.97555566px;font-style   *normal;font-weight   *normal;line-height   *119.00000572%;letter-spacing   *0.01975556px;word-spacing   *0.00846667px;writing-mode   *lr-tb;fill   *#000000;fill-opacity   *1;stroke   *none;font-family   *Sans;-inkscape-font-specification   *Sans"
       xml   *space="preserve"><tspan
         y="229.10912"
         x="220.8476"
         id="tspan3484"
         sodipodi   *role="line">AUTHOR NAME    *</tspan></text>


#### 2    * Tytuł z polem textedit 

<img alt="" src=images/Svg_Namespace_02.png  style="width   *300px;">

 {.xml}
  <g
     style="fill   *none;stroke   *#000000;stroke-width   *0.13;stroke-linecap   *butt;stroke-linejoin   *miter"
     id="g578-7"
     transform="translate(0,4)">
    <text
       xml   *space="preserve"
       style="font-size   *4px;font-style   *normal;font-variant   *normal;font-weight   *normal;font-stretch   *normal;line-height   *125%;letter-spacing   *0px;word-spacing   *0px;fill   *#000000;fill-opacity   *1;stroke   *none;font-family   *sans;-inkscape-font-specification   *sans"
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi   *linespacing="125%"
       freecad   *editable="AuthorName"><tspan
         sodipodi   *role="line"
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

 {.xml}
  <g


Początek struktury

 {.xml}
     style="fill   *none;stroke   *#000000;stroke-width   *0.13;stroke-linecap   *butt;stroke-linejoin   *miter"
     id="g578-7"
     transform="translate(0,4)">


Dane struktury

 {.xml}
    <text


Początek bloku tekstu

 {.xml}
       xml   *space="preserve"
       style="font-size   *4px;font-style   *normal;font-variant   *normal;font-weight   *normal;font-stretch   *normal;line-height   *125%;letter-spacing   *0px;word-spacing   *0px;fill   *#000000;fill-opacity   *1;stroke   *none;font-family   *sans;-inkscape-font-specification   *sans"


Wszystkie informacje o tekście, który będzie wyświetlany

 {.xml}
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi   *linespacing="125%"


Współrzędne i identyfikator gdzie pojawi się tekst

 {.xml}
       freecad   *editable="AuthorName"><tspan


Tutaj **AuthorName** jest zmienną zarządzaną przez **freecad   *editable**, zapisującą ciąg znaków do zmiany, który zostanie wyświetlony

 {.xml}
         sodipodi   *role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Współrzędne i identyfikator tekstu , który jest wyświetlany domyślnie, a **** oznacza koniec tekstu bloku

 {.xml}
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Inne bloki tekstowe i koniec **** struktury grupowania bloków tekstowych

Jest możliwe, że po pracy z plikiem SVG Inkscape\'a plik już nie działa, możliwe, że zaginęły informacje.

Następnie sprawdź, czy tekst edycji nie jest zmodyfikowany

Przykład   *

-   **editable** = \"AuthorName\"
-   zastąpiony przez **freecad   *editable** = \"AuthorName\"

## Inne dostępne atrybuty 

Zobacz [Szablony środowiska Kreślenie](Drawing_templates/pl.md)


{{Drawing Tools navi

}}

[Category   *Poweruser\_Documentation](Category_Poweruser_Documentation.md) [Category   *Developer](Category_Developer.md) [Category   *Python\_Code](Category_Python_Code.md) [Category   *Macros](Category_Macros.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/pl
