# CAM scripting/pl
## Wprowadzenie

Środowisko pracy CAM oferuje narzędzia do importowania, tworzenia, manipulowania i eksportowania [kodów G-code](https://pl.wikipedia.org/wiki/G-code) w FreeCAD. Dzięki niemu użytkownik ma możliwość importowania, wizualizacji i modyfikacji istniejących programów G-code, generowania ścieżek narzędzi na podstawie kształtów 3D i eksportowania tych ścieżek do G-code.

Środowisko pracy CAM jest obecnie we wczesnej fazie rozwoju i nie oferuje wszystkich zaawansowanych funkcji dostępnych w niektórych komercyjnych alternatywach. Jednak interfejs skryptów Pythona ułatwia modyfikację lub opracowywanie bardziej zaawansowanych narzędzi.



## Szybki start 

Obiekty Ścieżki we FreeCAD składają się z sekwencji poleceń ruchu. Typowe użycie wygląda następująco:


```python
>>> import Path
>>> c1 = Path.Command("g1x1")
>>> c2 = Path.Command("g1y4")
>>> c3 = Path.Command("g1 x2 y2") # spaces end newlines are ignored
>>> p = Path.Path([c1,c2,c3])
>>> o = App.ActiveDocument.addObject("Path::Feature","mypath")
>>> o.Path = p
>>> print (p.toGCode())
```



## Wewnętrzny format G-Code programu FreeCAD 

Ważne jest, aby zrozumieć wstępny koncept. Większość poniższej implementacji opiera się na poleceniach ruchu, które mają te same nazwy co polecenia G-code, ale nie są dostosowane do konkretnej implementacji kontrolera. Nazwy takie jak \'G0\' używane do reprezentowania ruchu \'szybkiego\' czy \'G1\' do reprezentowania ruchu \'posuwowego\' zostały wybrane ze względu na efektywność (oszczędność miejsca w pliku) i minimalizację pracy potrzebnej do tłumaczenia na/z innych formatów G-code. Ponieważ świat CNC posługuje się tysiącami dialektów G-code, wybrano bardzo uproszczony podzbiór. Można opisać format G-code FreeCAD jako \"niezależny od maszyny\" rodzaj G-code.

Wewnątrz plików .FCStd, dane Ścieżki są zapisywane bezpośrednio w tej formie G-code.

Wszystkie tłumaczenia między dialektami a G-code we FreeCAD są realizowane za pomocą skryptów przed i po. Oznacza to, że jeśli chcesz pracować z obrabiarką, która używa konkretnego kontrolera, takiego jak LinuxCNC, Fanuc, Mitsubishi czy HAAS, musisz użyć (lub napisać, jeśli nie istnieje) postprocesora dla tego konkretnego kontrolera (patrz sekcja „Importowanie i eksportowanie G-code" poniżej).



### Odniesienie do G-code 

Następujące zasady i wytyczne definiują podzbiór kodu G-code używanego wewnętrznie we FreeCAD:

-   Dane G-code, znajdujące się w obiektach Ścieżki we FreeCAD, są rozdzielone na \"Polecenia\". Polecenie jest definiowane przez nazwę polecenia, która musi zaczynać się od G lub M, oraz (opcjonalnie) argumenty, które mają formę litery plus liczby zmiennoprzecinkowej, na przykład X 0.02 lub Y 3.5 lub F 300. Oto przykłady typowych poleceń G-code w FreeCAD:




    G0 X2.5 Y0 (Nazwa polecenia to G0, argumentami są X=2.5 i Y=0)

    G1 X30 (Nazwa polecenia to G1, jedyny argument to X=30)

    G90 (Nazwa polecenia to G90, nie ma argumentów)

-   Dla numerycznej części polecnia G lub M, obsługiwane są zarówno formy \"G1\", jak i \"G01\".
-   Obecnie obsługiwane są tylko polecenia zaczynające się od G lub M.
-   Na razie akceptowane są tylko milimetry. G20/G21 są ignorowane.
-   Argumenty są zawsze sortowane alfabetycznie. Oznacza to, że jeśli utworzysz polecenie \"G1 X2 Y4 F300\", zostanie ono zapisane jako \"G1 F300 X2 Y4\".
-   Argumenty nie mogą być powtarzane w tym samym poleceniu. Na przykład, \"G1 X1 Y2 X2 Y3\" nie zadziała. Należy je podzielić na dwa polecenia, na przykład: \"G1 X1 Y2, G1 X2 Y3\".
-   Argumenty X, Y, Z, A, B, C są bezwzględne lub względne, w zależności od bieżącego trybu G90/G91. Domyślnie (jeśli nie określono) są bezwzględne.
-   I, J, K są zawsze względne względem ostatniego punktu. K można pominąć.
-   X, Y lub Z (oraz A, B, C) mogą być pominięte. W takim przypadku poprzednie współrzędne X, Y lub Z są zachowywane.
-   Polecenia G-code inne niż wymienione w tabeli poniżej są obsługiwane, tj. są zapisywane w danych ścieżki (o ile oczywiście spełniają powyższe zasady), ale po prostu nie będą miały żadnego widocznego efektu na ekranie. Na przykład, możesz dodać polecenie G81, zostanie ono zapisane, ale nie będzie wyświetlane.



### Lista obecnie wspieranych poleceń G-code 

  Polecenie       Opis                                           Wspierane argumenty   Wyświetlane
     
  G0              szybki ruch                                    X,Y,Z,A,B,C           Czerwony
  G1              normalny ruch                                  X,Y,Z,A,B,C           Zielony
  G2              łuk zgodny z ruchem wskazówek zegara           X,Y,Z,A,B,C,I,J,K     Zielony
  G3              łuk przeciwny do ruchu wskazówek zegara        X,Y,Z,A,B,C,I,J,K     Zielony
  G81, G82, G83   wiercenie                                      X,Y,Z,R,Q             Czerwony/Zielony
  G38.2           Prosty ruch sondy (używany w operacji sondy)   Z,F                   Żółty
  G90             bezwzględne współrzędne                                              
  G91             względne współrzędne                                                 
  (Wiadomość)     komentarz                                                            



## Obiekt Command 

Obiekt \*\*Command\*\* reprezentuje polecenie G-code. Ma trzy atrybuty: \*\*Name\*\*, \*\*Parameters\*\* i \*\*Placement\*\*, oraz dwie metody: \*\*toGCode()\*\* i \*\*setFromGCode()\*\*. Wewnątrz zawiera tylko nazwę i słownik parametrów. Pozostałe (placement i gcode) są obliczane na podstawie tych danych.


```python
>>> import Path
>>> c=Path.Command()
>>> c
Command  ( )
>>> c.Name = "G1"
>>> c
Command G1 ( )
>>> c.Parameters= {"X":1,"Y":0}
>>> c
Command G1 ( X:1 Y:0 )
>>> c.Parameters
{'Y': 0.0, 'X': 1.0}
>>> c.Parameters= {"X":1,"Y":0.5}
>>> c
Command G1 ( X:1 Y:0.5 )
>>> c.toGCode()
'G1X1Y0.5'
>>> c2=Path.Command("G2")
>>> c2
Command G2 ( )
>>> c3=Path.Command("G1",{"X":34,"Y":1.2})
>>> c3
Command G1 ( X:34 Y:1.2 )
>>> c3.Placement
Placement [Pos=(34,1.2,0), Yaw-Pitch-Roll=(0,0,0)]
>>> c3.toGCode()
'G1X34Y1.2'
>>> c3.setFromGCode("G1X1Y0")
>>> c3
Command G1 [ X:1 Y:0 ]
>>> c4 = Path.Command("G1X4Y5")
>>> c4
Command G1 [ X:4 Y:5 ]
>>> p1 = App.Placement()
>>> p1.Base = App.Vector(3,2,1)
>>> p1
Placement [Pos=(3,2,1), Yaw-Pitch-Roll=(0,0,0)]
>>> c5=Path.Command("g1",p1)
>>> c5
Command G1 [ X:3 Y:2 Z:1 ]
>>> p2=App.Placement()
>>> p2.Base = App.Vector(5,0,0)
>>> c5
Command G1 [ X:3 Y:2 Z:1 ]
>>> c5.Placement=p2
>>> c5
Command G1 [ X:5 ]
>>> c5.x
5.0
>>> c5.x=10
>>> c5
Command G1 [ X:10 ]
>>> c5.y=2
>>> c5
Command G1 [ X:10 Y:2 ]
```



## Obiekt Path 

Obiekt Path przechowuje listę poleceń


```python
>>> import Path
>>> c1=Path.Command("g1",{"x":1,"y":0})
>>> c2=Path.Command("g1",{"x":0,"y":2})
>>> p=Path.Path([c1,c2])
>>> p
Path [ size:2 length:3 ]
>>> p.Commands
[Command G1 [ X:1 Y:0 ], Command G1 [ X:0 Y:2 ]]
>>> p.Length
3.0
>>> p.addCommands(c1)
Path [ size:3 length:4 ]
>>> p.toGCode()
'G1X1G1Y2G1X1'

lines = """
G0X-0.5905Y-0.3937S3000M03
G0Z0.125
G1Z-0.004F3
G1X0.9842Y-0.3937F14.17
G1X0.9842Y0.433
G1X-0.5905Y0.433
G1X-0.5905Y-0.3937
G0Z0.5
"""

slines = lines.split('\n')
p = Path.Path()
for line in slines:
    p.addCommands(Path.Command(line))

o = App.ActiveDocument.addObject("Path::Feature","mypath")
o.Path = p

# but you can also create a path directly form a piece of G-code.
# The commands will be created automatically:

p = Path.Path()
p.setFromGCode(lines)
```

Jako skrót, obiekt Path można również utworzyć bezpośrednio z pełnej sekwencji G-code. Zostanie ona automatycznie podzielona na sekwencję poleceń.


```python
>>> p = Path.Path("G0 X2 Y2 G1 X0 Y2")
>>> p
Path [ size:2 length:2 ]
```



## Cecha Path 

Cecha Path jest obiektem dokumentu FreeCAD, który przechowuje ścieżkę i reprezentuje ją w widoku 3D.


```python
>>> pf = App.ActiveDocument.addObject("Path::Feature","mypath")
>>> pf
<Document object>
>>> pf.Path = p
>>> pf.Path
Path [ size:2 length:2 ]
```

Funkcja Path posiada również właściwość Placement. Zmiana wartości tej właściwości zmieni położenie funkcji w widoku 3D, choć sama informacja o ścieżce nie zostanie zmieniona. Transformacja jest czysto wizualna. Pozwala to, na przykład, stworzyć ścieżkę wokół powierzchni, która ma określoną orientację w modelu, różniącą się od orientacji materiału skrawającego na maszynie CNC.

Jednakże, Złożenia Ścieżki mogą korzystać z Umiejscowienia swoich elementów podrzędnych (zobacz poniżej).



## Obiekty Tool i Tooltable 

**UWAGA:** Ten typ użycia narzędzia jest przestarzały od oficjalnego wydania wersji 0.19. W wersji 0.19 wdrożono nowy system narzędzi, który zastąpił starszy system. W związku z tym kodowanie zmieniło się w porównaniu do przedstawionego poniżej. Proszę odwiedzić stronę [Narzędzia](CAM_Tools/pl.md) w celu uzyskania więcej informacji.

 ===Tworzenie skryptów \<= 0.18===

Obiekt Tool zawiera definicje narzędzia CNC. Obiekt Tooltable zawiera uporządkowaną listę narzędzi. Tabele narzędzi są przypisane jako właściwość do cech projektu ścieżki (Path Project) i mogą być również edytowane za pomocą GUI, klikając dwukrotnie projekt w widoku drzewa i klikając przycisk „Edytuj tabelę narzędzi" w otwieranych widokach zadań.

Z tego dialogu można importować tabele narzędzi z formatów .xml FreeCAD i .tooltable HeeksCad oraz eksportować do formatu .xml FreeCAD.


```python
>>> import Path
>>> t1=Path.Tool()
>>> t1
Tool Default tool
>>> t1.Name = "12.7mm Drill Bit"
>>> t1
Tool 12.7mm Drill Bit
>>> t1.ToolType
'Undefined'
>>> t1.ToolType = "Drill"
>>> t1.Diameter= 12.7
>>> t1.LengthOffset = 127
>>> t1.CuttingEdgeAngle = 59
>>> t1.CuttingEdgeHeight = 50.8
>>> t2 = Path.Tool("my other tool",tooltype="EndMill",diameter=10)
>>> t2
Tool my other tool
>>> t2.Diameter
10.0
>>> table = Path.Tooltable()
>>> table
Tooltable containing 0 tools
>>> table.addTools(t1)
Tooltable containing 1 tools
>>> table.addTools(t2)
Tooltable containing 2 tools
>>> table.Tools
{1: Tool 12.7mm Drill Bit, 2: Tool my other tool}
>>> 
```



## Funkcje



### Cecha Path Compound 

Celem tej funkcji jest zebranie jednej lub więcej ścieżek narzędziowych i powiązanie ich z tabelą narzędzi. Obiekt Compound zachowuje się również jak standardowa grupa FreeCAD, więc możesz dodawać lub usuwać obiekty z niej bezpośrednio z widoku drzewa. Możesz również zmieniać kolejność elementów, klikając dwukrotnie obiekt Compound w widoku drzewa i zmieniając kolejność jego elementów w otwierającym się widoku zadań.


```python
>>> import Path
>>> p1 = Path.Path("G1X1")
>>> o1 = App.ActiveDocument.addObject("Path::Feature","path1")
>>> o1.Path=p1
>>> p2 = Path.Path("G1Y1")
>>> o2 = App.ActiveDocument.addObject("Path::Feature","path2")
>>> o2.Path=p2
>>> o3 = App.ActiveDocument.addObject("Path::FeatureCompound","compound")
>>> o3.Group=[o1,o2]
```

Ważną funkcją obiektów Path Compound jest możliwość uwzględnienia Placement (położenia) ich podrzędnych ścieżek lub nie, poprzez ustawienie właściwości UsePlacements na True lub False. Jeśli jest ustawione na False, dane ścieżek podrzędnych będą po prostu dodawane sekwencyjnie. Jeśli jest ustawione na True, każde polecenie w ścieżkach podrzędnych, jeśli zawiera informacje o położeniu (G0, G1 itp.), będzie najpierw przekształcane przez Placement przed dodaniem.

Tworzenie obiektu Compound z tylko jedną podrzędną ścieżką pozwala zatem na \"realne\" zastosowanie Placement tej podrzędnej ścieżki (wpływa na dane ścieżki).



### Cecha Path Project 

Projekt Path to rozszerzona wersja obiektu Compound, która posiada dodatkowe właściwości związane z maszyną, takie jak tabela narzędzi. Jest głównie przeznaczony jako główny typ obiektu, który chcesz eksportować do G-code, gdy całe ustawienie ścieżek będzie gotowe. Obiekt Projektu jest teraz kodowany w Pythonie, więc jego mechanizm tworzenia jest nieco inny:


```python
>>> from PathScripts import PathProject
>>> o4 = App.ActiveDocument.addObject("Path::FeatureCompoundPython","prj")
>>> PathProject.ObjectPathProject(o4)
>>> o4.Group = [o3]
>>> o4.Tooltable
Tooltable containing 0 tools
```

Moduł Path zawiera również edytor tabeli narzędzi GUI, który można wywołać z Pythona, uzyskując obiekt z właściwością ToolTable:


```python
>>> from PathScripts import TooltableEditor
>>> TooltableEditor.edit(o4)
```



### Uzyskiwanie ścieżki z kształtu 

Przypisz kształt obiektu Część typu linia do zwykłego obiektu Path, używając funkcji skryptowej \Path.fromShape()\ (lub bardziej zaawansowanej \Path.fromShapes()\). Przekazując obiekt typu linia jako parametr, jego ścieżka zostanie automatycznie obliczona na podstawie kształtu. Należy pamiętać, że w tym przypadku umiejscowienie jest automatycznie ustawiane na pierwszy punkt linii, a obiekt nie może być już przesuwany poprzez zmianę jego umiejscowienia. Aby go przesunąć, należy przesunąć sam kształt.


```python
>>> import Part
>>> import Path
>>> v1 = FreeCAD.Vector(0,0,0)
>>> v2 = FreeCAD.Vector(0,2,0)
>>> v3 = FreeCAD.Vector(2,2,0)
>>> v4 = FreeCAD.Vector(3,3,0)
>>> wire = Part.makePolygon([v1,v2,v3,v4])
>>> o = FreeCAD.ActiveDocument.addObject("Path::Feature","myPath2")
>>> o.Path = Path.fromShape(wire)
>>> FreeCAD.ActiveDocument.recompute()
>>> p =  o.Path
>>> print(p.toGCode())
```



### Cechy Pythona 

Obie funkcje Path::Feature i Path::FeatureShape mają swoje wersje w Pythonie, odpowiednio nazywane Path::FeaturePython i Path::FeatureShapePython, które mogą być używane w kodzie Python do tworzenia bardziej zaawansowanych obiektów parametrycznych pochodzących od nich.



## Importowanie i eksportowanie kodu G-code 



### Format natywny 

Pliki G-code można bezpośrednio importować i eksportować za pomocą interfejsu graficznego, korzystając z opcji \"otwórz\", \"wstaw\" lub \"eksportuj\" w menu. Po podaniu nazwy pliku pojawia się okno dialogowe, w którym należy wybrać skrypt przetwarzający. Można to również zrobić z poziomu Pythona:

Informacje o ścieżkach są przechowywane w obiektach Path za pomocą podzbioru G-code opisanego w sekcji \"Wewnętrzny format G-code programu FreeCAD\". Ten podzbiór można importować lub eksportować \"tak jak jest\" lub konwertować do/od określonej wersji G-code dostosowanej do twojej maszyny.

Jeśli masz bardzo prosty i standardowy program G-code, który spełnia zasady opisane w sekcji \"Wewnętrzny format G-code programu FreeCAD\", na przykład boomerang z [cnccookbook](https://www.cnccookbook.com/g-code-examples-files/), można go bezpośrednio zaimportować do obiektu Path, bez potrzeby tłumaczenia (jest to równoważne używaniu opcji \"Brak\" w oknie dialogowym GUI).


```python
import Path
f = open("/path/to/boomerangv4.ncc")
s = f.read()
p = Path.Path(s)
o = App.ActiveDocument.addObject("Path::Feature","boomerang")
o.Path = p
```

W ten sam sposób możesz uzyskać informacje o ścieżce jako \"agnostyczny\" G-code i ręcznie zapisać je w pliku:


```python
text = o.Path.toGCode()
print text
myfile = open("/path/to/newfile.ngc")
myfile.write(text)
myfile.close()
```

Jeśli potrzebujesz innego formatu wyjściowego, będziesz musiał przetłumaczyć ten agnostyczny G-code na format odpowiedni dla twojej maszyny. To zadanie wykonują skrypty post-processora.



### Korzystanie ze skryptów przed i po 

Jeśli masz plik G-code napisany dla konkretnej maszyny, który nie jest zgodny z wewnętrznymi zasadami używanymi przez FreeCAD, opisanymi w sekcji \"Wewnętrzny format G-code programu FreeCAD\", może on nie zaimportować się i/lub nie renderować poprawnie w widoku 3D. Aby temu zaradzić, musisz użyć skryptu wstępnego przetwarzania, który przekonwertuje format specyficzny dla twojej maszyny na format FreeCAD.

Jeśli znasz nazwę skryptu wstępnego przetwarzania, którego chcesz użyć, możesz zaimportować swój plik przy jego użyciu z konsoli Pythona w ten sposób:


```python
import example_pre
example_pre.insert("/path/to/myfile.ncc","DocumentName")
```

Tak samo możesz wyeksportować obiekt Path do G-code, używając skryptu postprocesora w ten sposób:


```python
import example_post
example_post.export (myObjectName,"/path/to/outputFile.ncc")
```



### Pisanie skryptów przetwarzających 

Skrypty pre- i post-procesora działają jak inne powszechne importery/eksportery w FreeCAD. Wybierając skrypt pre/post-procesora z okna dialogowego, proces importu/eksportu zostanie przekierowany do wskazanego skryptu. Skrypty pre-procesora muszą zawierać przynajmniej następujące metody: \open(filename)\ i \insert(filename, docname)\. Skrypty post-procesora muszą implementować metodę \export(objectslist, filename)\.

Skrypty są umieszczane w folderze Mod/Path/Path/Post/scripts lub w katalogu makr użytkownika. Można nadać im dowolną nazwę, ale zgodnie z konwencją, aby były widoczne w oknie dialogowym GUI, nazwy skryptów pre-procesora muszą kończyć się na \"\_pre\", a skryptów post-procesora na \"\_post\" (upewnij się, że używasz podkreślenia, a nie myślnika, w przeciwnym razie Python nie będzie mógł ich zaimportować). Oto przykład bardzo, bardzo prostego pre-procesora. Bardziej złożone przykłady znajdują się w folderze Mod/Path/Path/Post/scripts:


```python
def open(filename):
    gfile = __builtins__.open(filename)
    inputstring = gfile.read()
    # the whole gcode program will come in as one string,
    # for example: "G0 X1 Y1\nG1 X2 Y2"
    output = ""
    # we add a comment
    output += "(This is my first parsed output!)\n"
    # we split the input string by lines
    lines = inputstring.split("\n")
    for line in lines:
        output += line
        # we must insert the "end of line" character again
        # because the split removed it
        output += "\n"
    # another comment
    output += "(End of program)"
    import Path
    p = Path.Path(output)
    myPath = FreeCAD.ActiveDocument.addObject("Path::Feature","Import")
    myPath.Path = p
    FreeCAD.ActiveDocument.recompute()
```

Pre- i post-procesory działają dokładnie w ten sam sposób. Różnią się tylko tym, że skrypty pre-procesora konwertują specyficzny G-code na \"agnostyczny\" G-code FreeCAD, podczas gdy skrypty post-procesora konwertują \"agnostyczny\" G-code FreeCAD na specyficzny G-code dla maszyny.



## Dodawanie wszystkich ścian obiektu Kształt z tekstu do listy BaseFeature\'s operacji ProfileFromFaces 

Ten przykład jest oparty na [dyskusji na niemieckim forum](https://forum.freecadweb.org/viewtopic.php?f=13&t=33310&p=279991#p279959).



### Wymagania wstępne 

-   Utwórz bryłę z Kształtem z tekstu jako wycięciem
-   Utwórz Zadanie używając tej bryły jako BaseObject
-   Utwórz operację ProfileFromFaces nazwaną \"Profile_Faces\" z pustym BaseGeometry.



### Kod

Następujący kod następnie doda wszystkie ściany z Kształtu z tekstu i utworzy ścieżki:


```python
doc = App.ActiveDocument
list_of_all_element_faces = []
for i, face in enumerate(doc.ShapeString.Shape.Faces):
    list_of_all_element_faces.append('Face' + str(i + 1))


doc.Profile_Faces.Base = [(doc.ShapeString, tuple(list_of_all_element_faces))]
doc.recompute()
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [CAM](CAM_Workbench.md) > CAM scripting/pl
