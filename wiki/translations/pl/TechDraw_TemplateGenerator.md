---
- TutorialInfo:/pl
   Topic:Generator szablonów - makrodefinicja Python
   Level:Podstawowa znajomość środowiska Python i struktur svg jest przydatna
   FCVersion:0.19.1 i nowszy
   Time:''(Jeszcze nie wiem)''
   Author:[FBXL5](User_FBXL5.md)
   SeeAlso:[Makro TemplateHelper](Macro_TemplateHelper/pl.md)
---

# TechDraw TemplateGenerator/pl







## Wprowadzenie

Ten poradnik opisuje jak z kilku linijek kodu Pythona wygenerować prosty szablon do wykorzystania w środowisku pracy Rysunek Techniczny.

Do kodowania można użyć dowolnego edytora tekstu. Mój wybór to Atom, ale wbudowany edytor FreeCAD też działa dobrze.

Poniższe przykłady kodu można skopiować i wkleić do pustego pliku tekstowego, a następnie zapisać pod wybraną nazwą jako plik typu ***.py** lub ***.FCMacro**.

Szablon stanowi tło dla zadań rysunkowych, a jego wymiary są wykorzystywane przez sterowniki drukarki do prawidłowego skalowania rysunku.

Szablony są plikami svg, więc makrodefinicja musi skomponować kilka linii kodu svg *(który jest podzbiorem kodu xml)*.



## Struktura zwykłej pustej strony 

Format SVG jest podzbiorem formatu XML. Dlatego plik SVG, jak każdy plik XML, składa się z dwóch części:

-   Nagłówka, czyli deklaracji formatu.
-   Zawartości, zawierającej informacje co pokazać i gdzie to umieścić

:   *(nie wiem po co ma być nagłówek, plik svg jest nadal poprawnym plikiem szablonu bez niego \...)*



### Nagłówek

Nagłówek to tylko jedna linia deklarująca, której wersji języka XML powinien użyć interpreter do obsługi instrukcji w treści.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
}}



### Zawartość

Struktura zaczyna się od znacznika otwierającego, który zawiera informacje o przestrzeniach nazw oraz o wielkości szablonu i miejscu jego umieszczenia. A kończy się znacznikiem zamykającym.


{{Code|lang=xml|code=
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


:   **xmlns=**<http://www.w3.org/2000/svg>\'\'\': Zewnętrzny link do przestrzeni nazw xml, aby wyszukać standardowe polecenia xml.
:   **version=**\"1.1\": Używana wersja xml to 1.1
:   **xmlns:freecad=**\"[Svg Namespace](https://wiki.freecad.org/index.php?title=Svg_Namespace)\": Zewnętrzny odnośnik do rozszerzenia przestrzeni nazw programu FreeCAD w celu wyszukania specjalnych poleceń, które są używane tylko wewnątrz środowiska FreeCAD np. dla tekstów edytowalnych.
:   \"freecad:\" będzie poprzedzone nazwami atrybutów, aby były one obsługiwane przez wspomniane specjalne polecenia.
:   **width=** \"420mm\": Szerokość obszaru rysowania.
:   **height=** \"297mm\": Wysokość obszaru rysowania.
:   **viewBox=** \"0 0 420 297\": Położenie lewego górnego rogu *(0;0)* i prawego dolnego rogu *(420;297)* w przestrzeni konstrukcyjnej svg *(w jednostkach svg)*.
:   Szerokość, wysokość i viewBox w tej kombinacji ustawiają 1 jednostkę svg na 1 mm dla całego dokumentu. Jednostka wymiarowa może być od tej pory pomijana.
:   W tym przypadku 420 i 297 dają stronę A3. Dostosuj te wartości, aby wygenerować inne rozmiary stron.

Dla pustej strony rozmiar DIN A3 w orientacji poziomej to wszystko.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}



## Kod Python \... 

Przed wygenerowaniem jakiegokolwiek kodu potrzebny jest folder do przechowywania nowego pliku szablonu.

Użytkownik powinien wybrać folder szablonu. Jego ścieżka jest następnie zapisywana w preferencjach środowiska pracy Rysunek Techniczny.  Nie jest konieczne, aby wiedzieć, gdzie przechowywane są preferencje, ponieważ FreeCAD posiada polecenia pozwalające na bezpośrednie adresowanie potrzebnych parametrów.


{{Code| |code=
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
template_file = os.path.join(template_path, template_name)
}}

**parameter_path** przyjmuje ścieżkę do \"folderu\" w ramach pliku konfiguracyjnego, w którym znajduje się parametr \"TemplateDir\".  **template_path** przyjmuje zawartość \"TemplateDir\", która jest ścieżką do katalogu z szablonem.  **template_name** przyjmuje nazwę szablonu, który ma zostać utworzony.

Teraz nazwa szablonu musi być połączona ze ścieżką szablonu w sposób, który jest kompatybilny z systemami operacyjnymi opartymi na Uniksie i Windows. Robi się to za pomocą polecenia \"os.path.join\" i przechowuje w **pliku szablonu**.



### \... aby stworzyć pustą stronę 


<div class="mw-collapsible mw-collapsed toccolours">

To makro pokazuje zasadę, jak można złożyć plik svg *(Format to A3)*.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- Get the path to the template folder that is set in the FreeCAD parameters
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
#- Link template_path and template_name for any OS
template_file = os.path.join(template_path, template_name)

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(file_path):
    t=open(file_path, "w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

# --- Main section ---

CreateSvgFile(template_file) # overwrites existing File

# Set sheet format (DIN A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(template_file)  # adds Start tag and namespaces
CreateSheet(template_file, formatWidth, formatHeight)
EndSvg(template_file)
# At this point a new SVG-file is generated and saved
}}


</div>


</div>


:   Główną zasadą jest:
    -   otworzyć plik do zapisu, a więc rozpocząć plik svg od zera, napisać linię nagłówka i zamknąć plik w pierwszym kroku.
    -   a następnie wielokrotne otwieranie pliku w celu dołączania kolejnych segmentów i ponowne zamykanie go po dołączeniu.
:   
:   Makro składa się z kilku funkcji, które są wywoływane z sekcji głównej.
:   Dodatkowe funkcje można by wstawić przed funkcją EndSvg, a potrzebne wywołania umieszczamy przed wywołaniem EndSvg().

Musimy mieć oko na liczbę spacji używanych przy operacjach zapisu, aby uzyskać poprawne wcięcie.



### \... aby stworzyć stronę w której jest trochę tuszu 

Aby stworzyć rysunek z pustej kartki potrzebujemy:

  - ramki czyli prostokąty utworzone za pomocą instrukcji **rect** bloku tytułowego i więcej linii utworzonych za pomocą instrukcji **path**,

  - proste teksty do indeksów i etykietowania komórek bloku tytułowego,

  - teksty edytowalne, takie jak numer lub nazwa części,

Zwykle te elementy graficzne są używane wielokrotnie, dlatego kod generujący jest umieszczany w funkcjach.



### funkcja svgrect 

Aby narysować prostokąt musimy tylko wywołać funkcję **svgrect** i przekazać wartości szerokości, wysokości i położenia lewego górnego rogu. Jest to lepiej czytelne niż zawartość svgline, która musiała być użyta zamiennie.


{{Code| |code=
#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine
}}



### funkcja svgpath 

Aby narysować linię wystarczy wywołać funkcję **svgpath** i przekazać współrzędne punktu początkowego i końcowego linii.

Zamiast współrzędnych punktu końcowego możemy przekazać znacznik do rysowania linii poziomej *(h)* lub pionowej *(v)*, a następnie długość linii lub znacznik do rysowania linii poziomej *(H)* lub pionowej *(V)*, a następnie rzędną x lub y punktu końcowego.

Każda ścieżka zaczyna się w punkcie początkowym i pierwszą czynnością jest ruch z \"podniesionym piórem\" *(bez rysowania)* do punktu początkowego. W tym przypadku ruch względny i ruch bezwzględny są takie same i dlatego nie ma znaczenia, czy znacznik m jest pisany wielką czy małą literą.


{{Code| |code=
#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine
}}



### funkcja svgtext 

Aby narysować fragment tekstu wystarczy wywołać funkcję **svgtext** i przekazać współrzędne punktu zakotwiczenia tekstu oraz sam ciąg tekstowy.

*(Wyrównanie tekstu jest kontrolowane przez otaczający znacznik grupy lub domyślnie wyrównane do lewej)*.


{{Code| |code=
#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine
}}



### funkcja FCeditext 

Aby narysować fragment edytowalnego tekstu wystarczy wywołać funkcję **FCeditext** i przekazać jej nazwę, współrzędne punktu zakotwiczenia tekstu oraz sam ciąg tekstowy.

FreeCAD tworzy obiekt słownika z każdym wstawionym szablonem, a każdy wpis ma nazwę *(klucz)* i wartość.

*(Wyrównanie tekstu jest kontrolowane przez otaczający znacznik grupy lub domyślnie wyrównane do lewej)*.


{{Code| |code=
#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine
}}



### Funkcja CreateXxxx 

Funkcje te rozpoczynają się od kodu otwierającego plik w trybie dołączania i zapisującego znacznik otwierający grupę.

Następnie widzimy sekcję do ustawiania i obliczania wartości oraz z instrukcjami zapisu, które wywołują powyższe funkcje w celu wygenerowania kodu svg.

I wreszcie znacznik zamykający grupę, po którym następuje instrukcja zamknięcia pliku.


{{Code| |code=
#- Frame creation
def CreateFrame(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(20)
    drawingY=str(10)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20-10)
    drawingHeight=str(int(shHeight)-10-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(15)
    drawingY=str(5)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20)
    drawingHeight=str(int(shHeight)-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close
}}



### Rezultat


<div class="mw-collapsible mw-collapsed toccolours">

Makro to dodaje kilka podstawowych elementów graficznych potrzebnych do prawidłowego działania szablonów tj. elementy linii, etykiety oraz teksty do edycji.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- Get the path to the template folder that is set in the FreeCAD parameters
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
#- Link template_path and template_name for any OS
template_file = os.path.join(template_path, template_name)

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(file_path):
    t=open(file_path, "w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine

#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine

#- Frame creation
def CreateFrame(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(20)
    drawingY=str(10)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20-10)
    drawingHeight=str(int(shHeight)-10-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(15)
    drawingY=str(5)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20)
    drawingHeight=str(int(shHeight)-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Title block movable
def CreateTitleBlock(file_path, shWidth, shHeight):

    #- lower left corner
    tbX=str(int(shWidth)-10-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-10)
    #- group to transform all elements at once
    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("  4.5","-43.5 ","Some static text")+"\n")
    t.write("        "+svgtext("  4.5","-13.5 ","More static text")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def CreateEditableText(file_path, shWidth, shHeight):

    #- offsets for editable texts
    edX=int(shWidth)-10-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-10

    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"titleblock-editable-texts\"\n")
    t.write("      style=\"font-size:7.0;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("EdiText-1",str(edX+60),str(edY-43.5),"Some editable text")+"\n")
    t.write("      "+FCeditext("EdiText-2",str(edX+60),str(edY-13.5),"More editable text")+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateSvgFile(template_file) # overwrites existing File

# Set sheet format (A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(template_file)  # adds Start tag and namespaces
CreateSheet(template_file, formatWidth, formatHeight)
CreateFrame(template_file, formatWidth, formatHeight)
CreateTitleBlock(template_file, formatWidth, formatHeight)
CreateEditableText(template_file, formatWidth, formatHeight)
EndSvg(template_file)
# At this point a new SVG-file is generated and saved
}}

A to jest kod svg pochodzący z tej makrodefinicji:


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width ="420mm"
  height="297mm"
  viewBox="0 0 420 297">
    <g id="drawing-frame"
      style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round">
      <rect width="390" height="277" x="20" y="10" />
      <rect width="400" height="287" x="15" y="5" />
    </g>

    <g id="titleblock"
      transform="translate(230,287)">
      <g id="titleblock-frame"
        style="fill:none;stroke:#000000;stroke-width:0.35;stroke-linecap:miter;stroke-miterlimit:4">
        <path d="m   0,  0 l   0,-63" />
        <path d="m   0,-63 l 180,  0" />
        <path d="m   0,-30 h 155" />
        <path d="m 155,  0 v -63" />
      </g>
      <g id="titleblock-text-non-editable"
        style="font-size:5.0;text-anchor:start;fill:#000000;font-family:osifont">
        <text x="  4.5" y="-43.5 ">Some static text</text>
        <text x="  4.5" y="-13.5 ">More static text</text>
      </g>
    </g>

    <g id="titleblock-editable-texts"
      style="font-size:7.0;text-anchor:start;fill:#0000d0;font-family:osifont">
      <text freecad:editable="EdiText-1" x="290" y="243.5">  <tspan>Some editable text</tspan>  </text>
      <text freecad:editable="EdiText-2" x="290" y="273.5">  <tspan>More editable text</tspan>  </text>
    </g>

</svg>
}}


</div>


</div>

I jak to powinno wyglądać po wstawieniu *(plus powiększony blok tytułowy)*:

<img alt="" src=images/TechDraw_TemplateGenerator.png  style="width:600px;">



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator/pl
