---
 TutorialInfo:l
   Topic: Tworzenie szablonu Rysunku Technicznego - makrodefinicja Python
   Level: Podstawowa znajomość środowiska Python i struktur svg jest przydatna
   FCVersion: 0.21 i nowszy
   Time: ''''
   Author: User:FBXL5
   SeeAlso: Macro_TemplateHelper/pl
---

# TechDraw TemplateGenerator/pl







## Wprowadzenie

Ten poradnik opisuje jak z kilku linijek kodu Pythona wygenerować prosty szablon do wykorzystania w środowisku pracy Rysunek Techniczny.

Do kodowania można użyć dowolnego edytora tekstu. Mój wybór to Atom, ale wbudowany edytor FreeCAD też działa dobrze.

Poniższe przykłady kodu można skopiować i wkleić do pustego pliku tekstowego, a następnie zapisać pod wybraną nazwą jako plik typu ***.py** lub ***.FCMacro**.

Szablon stanowi tło dla zadań rysunkowych, a jego wymiary są wykorzystywane przez sterowniki drukarki do prawidłowego skalowania rysunku.

Szablony są plikami svg, więc makrodefinicja musi skomponować kilka linii kodu svg *(który jest podzbiorem kodu xml)*.

**Uwaga:** Kiedy FreeCAD został przeniesiony z **freecadweb.org** do **freecad.org**, ta strona została odpowiednio zaktualizowana, a wynikowy kod SVG nie jest już kompatybilny z wersjami FreeCAD starszymi niż v0.21. W przypadku tych wersji należy ręcznie zmienić {{Incode|freecad.org}} na {{Incode|freecadweb.org}} w wierszu deklaracji przestrzeni nazw w wynikowym kodzie SVG, w przeciwnym razie edytowalne teksty nie zostaną rozpoznane.



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
:   **xmlns:freecad=**\...=Svg_Namespace\": Zewnętrzny link do strony Wiki FreeCAD [Svg Namespace](Svg_Namespace/pl.md). Link nie jest używany do pobierania informacji lub wartości w czasie wykonywania, ale jest kluczem do aktywacji niestandardowych atrybutów, np. tych dla edytowalnych tekstów.
:   \"freecad:\" zostaną poprzedzone nazwami atrybutów niestandardowych.
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
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}



## Kod Python \... 

Kodowanie rozpoczyna się od frameworka zawierającego oddzielną funkcję główną:


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2024 Your name LGPL


def main():
    """Here is where the magic happens"""
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}



### \... aby stworzyć pustą stronę 

Proces tworzenia szablonu składa się z następujących etapów

-   Zlokalizowanie folderu szablonów.
-   Otwarcie pliku do zapisu w celu utworzenia pliku svg od podstaw, napisanie linii nagłówka i zamknięcie pliku w pierwszym kroku.
-   A następnie wielokrotne otwieranie pliku w celu dodania kolejnych segmentów, zamykając go ponownie za każdym razem.

Makrodefinicja składa się z kilku funkcji, które są wywoływane z sekcji głównej.
Dodatkowe funkcje można wstawić przed funkcją EndSvg, a potrzebne wywołania przed wywołaniem EndSvg().
Aby wcięcie było prawidłowe, musimy zwracać uwagę na liczbę spacji używanych podczas operacji zapisu.



#### pathToTemplate()

Przed wygenerowaniem jakiegokolwiek kodu potrzebny jest folder do przechowywania nowego pliku szablonu i należy ustawić nazwę pliku.

Użytkownik powinien wybrać folder szablonu. Jego ścieżka jest następnie zapisywana w preferencjach środowiska pracy Rysunek Techniczny.  Nie jest konieczne, aby wiedzieć, gdzie przechowywane są preferencje, ponieważ FreeCAD posiada polecenia pozwalające na bezpośrednie adresowanie potrzebnych parametrów.


{{Code| |code=
def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file
}}

**parameter_path** przyjmuje ścieżkę do \"folderu\" w ramach pliku konfiguracyjnego, w którym znajduje się parametr \"TemplateDir\".  **template_path** przyjmuje zawartość \"TemplateDir\", która jest ścieżką do katalogu z szablonem.
**template_name** przyjmuje nazwę szablonu, który ma zostać utworzony.

Teraz nazwa szablonu musi być połączona ze ścieżką szablonu w sposób, który jest kompatybilny z systemami operacyjnymi opartymi na Uniksie i Windows. Robi się to za pomocą polecenia \"os.path.join\" i przechowuje w **pliku szablonu**. Aby włączyć to polecenie, wymagana jest instrukcja \"import os\".



#### createSvgFile()

Spowoduje to utworzenie nowego pliku szablonu i zapisanie nagłówka xml.


{{Code| |code=
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close
}}



#### startSvg()

Powoduje to dołączenie pliku szablonu i utworzenie znacznika otwierającego svg wraz z jego atrybutami.
Każda instrukcja zapisu zawiera jedną linię kodu svg zakończoną \"\\n\", znacznikiem CR/LF.


{{Code| |code=
def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close
}}



#### endSvg()

To dalej dołącza plik szablonu i tworzy znacznik zamykający svg; To ostatecznie kończy kod szablonu.


{{Code| |code=
def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close
}}



#### main()

Funkcja main() wywołuje funkcje i przekazuje pewne parametry.


{{Code| |code=
def main():
    """This one creates an empty A3 template"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return
}}

W tym przykładzie {{Incode|format_width}} i {{Incode|format_height}} są twardo zakodowanymi wymiarami, obie niepotrzebne linie oznaczają punkty, w których inne sposoby pobierania danych formatu mogłyby umieścić swoją zawartość.


<div class="mw-collapsible mw-collapsed toccolours">

#### Kompletna makrodefinicja pustej strony 

To makro składa się z powyższych segmentów kodu, gotowych do uruchomienia.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2024 Your name LGPL

import os  # to enable the use of os.path.join()


# - SVG creation -
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close

def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file

def main():
    """This one creates an empty A3 template"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>



### \... aby stworzyć stronę w której jest trochę tuszu 

Aby stworzyć rysunek z pustej kartki potrzebujemy:

-   ramki czyli prostokąty utworzone za pomocą instrukcji **rect**,

bloku tytułowego i więcej linii utworzonych za pomocą instrukcji **path**,

-   proste teksty do indeksów i etykietowania komórek bloku tytułowego,
-   teksty edytowalne, takie jak numer lub nazwa części,

Zwykle te elementy graficzne są używane wielokrotnie, więc kod generujący jest umieszczony w czterech funkcjach:

-   svgRect() dla prostokątnych elementów ramki.
-   svgPath() dla elementów prostych.
-   svgText() dla tekstów statycznych.
-   ediText() dla tekstów edytowalnych.

Wszystkie funkcje są umieszczane wewnątrz powyższej makrodefinicji przed funkcją main(), a powiązane z nimi wywołania funkcji są wstawiane do funkcji main() między {{Incode|startSvg(...)}} i {{Incode|endSvg(...)}}.



#### funkcja svgRect() 

Aby narysować prostokąt musimy tylko wywołać funkcję **svgRect** i przekazać wartości szerokości, wysokości i położenia lewego górnego rogu. Jest to lepiej czytelne w tym miejscu, niż gdyby svg_line zawierał całą linię kodu svg.


{{Code| |code=
def svgRect(width, height, x, y):
    # Generates an svg-instruction to draw a rectangle with the given values
    svg_line = (
        "<rect width=\"" + width + "\" height=\"" + height + "\" x=\"" + x
        + "\" y=\"" + y + "\" />"
        )
    return svg_line
}}

Instrukcja svg jest podzielona, aby pozostać w zalecanej długości linii Pythona, mimo to spowoduje to utworzenie pojedynczej linii svg.



#### funkcja svgPath() 

Aby narysować linię wystarczy wywołać funkcję **svgPath** i przekazać współrzędne punktu początkowego i końcowego linii.

Zamiast współrzędnych punktu końcowego możemy przekazać znacznik do rysowania linii poziomej *(h)* lub pionowej *(v)*, a następnie długość linii lub znacznik do rysowania linii poziomej *(H)* lub pionowej *(V)*, a następnie rzędną x lub y punktu końcowego.

Każda ścieżka zaczyna się w punkcie początkowym i pierwszą czynnością jest ruch z \"podniesionym piórem\" *(bez rysowania)* do punktu początkowego. W tym przypadku ruch względny i ruch bezwzględny są takie same i dlatego nie ma znaczenia, czy znacznik m jest pisany wielką czy małą literą.


{{Code| |code=
def svgPath(x1, y1, x2, y2):
    # Generates an svg-instruction to draw a path element (line) with the given values
    if x2 == "v" or x2 == "V" or x2 == "h" or x2 == "H":
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " " + x2 + " " + y2 + "\" />")
    else:
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " l " + x2 + "," + y2 + "\" />")
    return svg_line
}}



#### funkcja svgText() 

Aby narysować fragment tekstu wystarczy wywołać funkcję **svgText** i przekazać współrzędne punktu zakotwiczenia tekstu oraz sam ciąg tekstowy i opcjonalnie kąt dla obracanego tekstu. Aby obrócić tekst, instrukcja transformacji musi zostać wstawiona do każdego znacznika tekstowego osobno. Środki obrotu są ustawione na te same współrzędne, co powiązane punkty zakotwiczenia tekstu.

*(Wyrównanie tekstu jest kontrolowane przez otaczający znacznik grupy lub domyślnie wyrównane do lewej)*.


{{Code| |code=
def svgText(x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place a text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated texts
    """
    if str_angle == "0":
        svg_line = ("<text x=\"" + x + "\" y=\"" + y + "\">" + str_value + "</text>")
    else:
        svg_line = (
            "<text x=\"" + x + "\" y=\"" + y + "\" transform=\"rotate(" + str_angle
            + "," + x + "," + y + ")\">" + str_value + "</text>"
            )
    return svg_line
}}



#### funkcja ediText() 

Aby narysować fragment edytowalnego tekstu wystarczy wywołać funkcję **ediText** i przekazać jej nazwę, współrzędne punktu zakotwiczenia tekstu oraz sam ciąg tekstowy i opcjonalnie kąt dla obracanego tekstu. Aby obrócić tekst, instrukcja transformacji musi zostać wstawiona do każdego znacznika tekstowego osobno. Środki obrotu są ustawione na te same współrzędne, co powiązane punkty zakotwiczenia tekstu.

FreeCAD tworzy obiekt słownika z każdym wstawionym szablonem, a każdy wpis ma nazwę *(klucz)* i wartość.

*(Wyrównanie tekstu jest kontrolowane przez otaczający znacznik grupy lub domyślnie wyrównane do lewej)*.


{{Code| |code=
def ediText(entry_name, x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place an editable text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated editable texts
    """
    if str_angle == "0":
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\">  <tspan>" + str_value + "</tspan>  </text>"
            )
    else:
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\" transform=\"rotate(" + str_angle + "," + x + "," + y + ")\">  <tspan>"
            + str_value + "</tspan>  </text>"
            )
    return svg_line
}}



### Funkcja createXxxx 

Funkcje te rozpoczynają się od kodu otwierającego plik w trybie dołączania i zapisującego znacznik otwierający grupę.

Następnie widzimy sekcję do ustawiania i obliczania wartości oraz z instrukcjami zapisu, które wywołują powyższe funkcje w celu wygenerowania kodu svg.

I wreszcie znacznik zamykający grupę, po którym następuje instrukcja zamknięcia pliku.


{{Code| |code=
def createFrame(file_path, sheet_width, sheet_height):
    # Creates rectangles for sheet frame and drawing area
    t = open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round\">\n")
    #- upper left corner of inner Frame, drawing area
    frame_x = str(20)
    frame_y = str(10)
    #- frame dimensions
    frame_width = str(int(sheet_width) - 20 - 10)
    frame_height = str(int(sheet_height) - 10 - 10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    #- upper left corner outer frame, sheet frame
    frame_x = str(15)
    frame_y = str(5)
    #- frame dimensions
    frame_width = str(int(sheet_width)-20)
    frame_height = str(int(sheet_height)-10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
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
# (c) 2024 Your name LGPL

import os  # to enable the use of os.path.join()


# - SVG creation -
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close

def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

def svgRect(width, height, x, y):
    # Ggenerates an svg-instruction to draw a rectangle with the given values
    svg_line = (
        "<rect width=\"" + width + "\" height=\"" + height + "\" x=\"" + x
        + "\" y=\"" + y + "\" />"
        )
    return svg_line

def svgPath(x1, y1, x2, y2):
    # Generates an svg-instruction to draw a path element (line) with the given values
    if x2 == "v" or x2 == "V" or x2 == "h" or x2 == "H":
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " " + x2 + " " + y2 + "\" />")
    else:
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " l " + x2 + "," + y2 + "\" />")
    return svg_line

def svgText(x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place a text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated texts
    """
    if str_angle == "0":
        svg_line = ("<text x=\"" + x + "\" y=\"" + y + "\">" + str_value + "</text>")
    else:
        svg_line = (
            "<text x=\"" + x + "\" y=\"" + y + "\" transform=\"rotate(" + str_angle
            + "," + x + "," + y + ")\">" + str_value + "</text>"
            )
    return svg_line

def ediText(entry_name, x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place an editable text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated editable texts
    """
    if str_angle == "0":
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\">  <tspan>" + str_value + "</tspan>  </text>"
            )
    else:
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\" transform=\"rotate(" + str_angle + "," + x + "," + y + ")\">  <tspan>"
            + str_value + "</tspan>  </text>"
            )
    return svg_line

def createFrame(file_path, sheet_width, sheet_height):
    # Creates rectangles for sheet frame and drawing area
    t = open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round\">\n")
    #- calculate upper left corner of inner Frame, drawing area
    frame_x = str(20)
    frame_y = str(10)
    #- frame dimensions
    frame_width = str(int(sheet_width) - 20 - 10)
    frame_height = str(int(sheet_height) - 10 - 10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    #- calculate upper left corner outer frame, sheet frame
    frame_x = str(15)
    frame_y = str(5)
    #- frame dimensions
    frame_width = str(int(sheet_width)-20)
    frame_height = str(int(sheet_height)-10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    t.write("    </g>\n\n")
    t.close

def createTitleBlock(file_path, sheet_width, sheet_height):
    """Creates a title block and transfers it to the position according to the sheet dimensions"""
    #- calculate title block origin (lower left corner), offset from page origin
    tbX = str(int(sheet_width) - 10 - 180)  # 180 according to DIN EN ISO 7200
    tbY = str(int(sheet_height) - 10)
    t = open(file_path, "a", encoding="utf-8")
    #- group to transfer all included title block elements at once
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate(" + tbX + "," + tbY + ")\">\n")
    #- sub-group of title block line framework
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        " + svgPath("  0","  0","  0","-63") + "\n")
    t.write("        " + svgPath("  0","-63","180","  0") + "\n")
    t.write("        " + svgPath("  0","-30","h","155") + "\n")
    t.write("        " + svgPath("155","  0","v","-63") + "\n")
    t.write("      </g>\n")
    #- sub-group of title block static texts (left-aligned by default)
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        " + svgText("  4.5","-43.5 ","Some static text") + "\n")
    t.write("        " + svgText("  4.5","-13.5 ","More static text") + "\n")
    t.write("        " + svgText("162.5","-3.5 ","Vertical static text","-90") + "\n")
    t.write("      </g>\n")
    t.write("    </g>\n\n")
    t.close

def createEditableText(file_path, sheet_width, sheet_height):
    """Creates editable texts positioned according to the page origin"""
    #- calculate offset to titleblock origin
    edX = int(sheet_width) - 10 - 180 # 180 according to DIN EN ISO 7200
    edY = int(sheet_height) - 10
    t = open(file_path, "a", encoding="utf-8")
    #- group editable texts using the same attributes
    t.write("    <g id=\"titleblock-editable-texts\"\n")
    t.write("      style=\"font-size:7.0;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write(
        "      " + ediText("EdiText-1",str(edX + 60),str(edY - 43.5),"Some editable text") + "\n"
        )
    t.write(
        "      " + ediText("EdiText-2",str(edX + 60),str(edY - 13.5),"More editable text") + "\n"
        )
    t.write(
        "      " + ediText("EdiText-3",str(edX + 173),str(edY - 4.5),"90° editable text","-90")
        + "\n"
        )
    t.write("    </g>\n\n")
    t.close

def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file

def main():
    """This one creates an A3 template with simple frame and title block"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    createFrame(template_file, format_width, format_height)
    createTitleBlock(template_file, format_width, format_height)
    createEditableText(template_file, format_width, format_height)
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
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
        <text x="162.5" y="-3.5 " transform="rotate(-90,162.5,-3.5 )">Vertical static text</text>
      </g>
    </g>

    <g id="titleblock-editable-texts"
      style="font-size:7.0;text-anchor:start;fill:#0000d0;font-family:osifont">
      <text freecad:editable="EdiText-1" x="290" y="243.5">  <tspan>Some editable text</tspan>  </text>
      <text freecad:editable="EdiText-2" x="290" y="273.5">  <tspan>More editable text</tspan>  </text>
      <text freecad:editable="EdiText-3" x="403" y="282.5" transform="rotate(-90,403,282.5)">  <tspan>90° editable text</tspan>  </text>
    </g>

</svg>
}}


</div>


</div>

I jak to powinno wyglądać po wstawieniu *(plus powiększony blok tytułowy)*:

<img alt="" src=images/TechDraw_TemplateGenerator.png  style="width:600px;">

Kolorowanie edytowalnych tekstów na niebiesko jest tylko osobistym wyborem, aby łatwiej odróżnić statyczne i edytowalne teksty na gotowym rysunku.



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator/pl
