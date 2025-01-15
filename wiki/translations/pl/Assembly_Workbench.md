# <img alt="Ikonka FreCAD dla środowiska pracy Złożenie" src=images/Workbench_Assembly.svg  style="width:64px;"> Assembly Workbench/pl






## Wprowadzenie


{{Version/pl|1.0}}

Środowisko pracy <img alt="" src=images/Workbench_Assembly.svg  style="width:24px;"> [Złożenie](Assembly_Workbench/pl.md) to nowe wbudowane środowisko pracy FreeCAD do modelowania złożeń. Korzysta z otwartoźródłowego [solvera Ondsel](https://github.com/Ondsel-Development/OndselSolver).

<img alt="" src=images/Assembly_Workbench_Example.png  style="width:400px;">



## Narzędzia



### Złożenie

-   <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:32px;"> [Utwórz złożenie](Assembly_CreateAssembly/pl.md): tworzy bazowe złożenie w bieżącym dokumencie lub podzłożenie w istniejącym aktywnym złożeniu.

-   <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Insert objects:

  - <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"> [Wstaw komponent](Assembly_InsertLink/pl.md): wstawia komponent do aktywnego złożenia.

  - <img alt="" src=images/Assembly_InsertNewPart.svg  style="width:32px;"> [Wstaw nową część](Assembly_InsertNewPart/pl.md): wstawia nową Część.

-   <img alt="" src=images/Assembly_SolveAssembly.svg  style="width:32px;"> [Rozwiąż złożenie](Assembly_SolveAssembly/pl.md): rozwiązuje aktualnie aktywne złożenie.

-   <img alt="" src=images/Assembly_CreateView.svg  style="width:32px;"> [Utwórz widok rozłożenia](Assembly_CreateView/pl.md): tworzy kontener widoków rozłożenia w aktywnym złożeniu, zawierający jeden lub więcej widoków rozłożenia.

-   <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:32px;"> [Utwórz symulację](Assembly_CreateSimulation/pl.md): tworzy symulację bieżącego złożenia. {{Version/pl|1.1}}

-   <img alt="" src=images/Assembly_CreateBom.svg  style="width:32px;"> [Utwórz zestawienie](Assembly_CreateBom/pl.md): tworzy zestawienie materiałów (BOM) ze wskazanego złożenia lub z dokumentu.

-   <img alt="" src=images/Assembly_ExportASMT.svg  style="width:32px;"> [Eksportuj do pliku ASMT](Assembly_ExportASMT/pl.md): eksportuje aktualnie aktywne złożenie do pliku ASMT.



### Połączenia

-   <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:32px;"> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md): blokuje położenie i orientację kształtu względem układu współrzędnych złożenia, do którego ten kształt należy.

-   <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:32px;"> [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl.md): tworzy połączenie blokujące dwie części złożenia razem, zapobiegając wszelkim przesunięciem lub obrotom, ale może być również wykorzystane do zdefiniowania innych typów połączeń.

-   <img alt="" src=images/Assembly_CreateJointRevolute.svg  style="width:32px;"> [Utwórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md): tworzy zawias pozwalający na obrót wokół jednej osi między dwiema wskazanymi częściami.

-   <img alt="" src=images/Assembly_CreateJointCylindrical.svg  style="width:32px;"> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md): tworzy połączenie cylindryczne między dwiema wskazanymi częściami, pozwalając na obrót wokół jednej osi i przesunięcie wzdłuż tej samej osi.

-   <img alt="" src=images/Assembly_CreateJointSlider.svg  style="width:32px;"> [Utwórz połączenie przesuwne](Assembly_CreateJointSlider/pl.md): tworzy połączenie suwliwe (pryzmatyczne) między dwiema wskazanymi częściami, pozwalając na przesunięcie wzdłuż jednej osi i blokując obrót.

-   <img alt="" src=images/Assembly_CreateJointBall.svg  style="width:32px;"> [Utwórz przegub kulowy](Assembly_CreateJointBall/pl.md): tworzy przegub kulowy między dwiema wskazanymi częściami w jednym punkcie, pozwalając na obrót wokół tego punktu i utrzymując obie części połączone w nim.

-   <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:32px;"> [Utwórz połączenie dystansowe](Assembly_CreateJointDistance/pl.md): tworzy połączenie dystansowe między wskazanymi częściami, blokując odległość między nimi.

-   <img alt="" src=images/Assembly_CreateJointParallel.svg  style="width:32px;"> [Utwórz połączenie równoległe](Assembly_CreateJointParallel/pl.md): tworzy połączenie równoległe między dwiema wskazanymi częściami, ustawiając osie Z wybranych układów współrzędnych równolegle.

-   <img alt="" src=images/Assembly_CreateJointPerpendicular.svg  style="width:32px;"> [Utwórz połączenie prostopadłe](Assembly_CreateJointPerpendicular/pl.md): tworzy połączenie prostopadłe między dwiema wybranymi częściami, ustawiając osie Z wybranych układów współrzędnych prostopadle.

-   <img alt="" src=images/Assembly_CreateJointAngle.svg  style="width:32px;"> [Utwórz połączenie kątowe](Assembly_CreateJointAngle/pl.md): tworzy połączenie kątowe między dwiema wybranymi częściami, ustalając kąt między osiami Z wybranych układów współrzędnych.

-   <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:32px;"> [Utwórz połączenie zębatki i koła zębatego](Assembly_CreateJointRackPinion/pl.md): tworzy połączenie zębatki i koła zębatego, które wiąże przesunięcie części połączenia typu Przesuwne i obrót części połączenia typu Obrotowe.

-   <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:32px;"> [Utwórz połączenie śrubowe](Assembly_CreateJointScrew/pl.md): tworzy połączenie śrubowe (spiralne), które wiąże przesunięcie części z połączeniem typu Przesuwne i obrót części z połączeniem typu Obrotowe.

-   <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz połączenie koła zębatego / pasa:

  - <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:32px;"> [Utwórz połączenie kół zębatych](Assembly_CreateJointGears/pl.md): tworzy połączenie kół zębatych wiążące obrót dwóch części z dwoma różnymi połączeniami typu Obrotowe.

  - <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:32px;"> [Utwórz połączenie pasowe](Assembly_CreateJointBelt/pl.md): tworzy połączenie przekładni pasowej, które wiąże obrót dwóch części z dwoma różnymi połączeniami typu Obrotowe.



## Ustawienia

-   <img alt="" src=images/Preferences-assembly.svg  style="width:32px;"> [Ustawienia](Assembly_Preferences/pl.md): preferencje dla środowiska pracy Złożenie.



## Przykład - korba i suwak 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:80px;"> Ten przykład jest tymczasowy i może zostać usunięty gdy pojawią się odpowiednie opisy/przykłady.


<div class="mw-collapsible-content">



### Złożenie - korba i suwak 

Złożenie, które ma zostać utworzone, składa się z czterech części: podstawy, suwaka, korby i korbowodu. Są one połączone czterema przegubami.

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:300px;">



*Złożone części: Podstawa ''(bursztynowy)'', Suwak ''(jasnoniebieski)'', Korba ''(czerwony)'', Korbowód ''(zielony)''*



### Przygotowanie części 

W tym przykładzie wszystkie części i zespół są tworzone w jednym dokumencie.

Geometrie cylindryczne obiektów są równoległe lub prostopadłe, pozostałe kształty nie są istotne dla tego przykładu, chyba że występują kolizje. Mając to na uwadze, możesz zamodelować własne obiekty lub utworzyć je przy pomocy poniższego kodu Pythona. Ten kod utworzy nowy dokument z czterema obiektami (prostszymi niż na rysunkach). Po prostu skopiuj i wklej następujące linie do [konsoli Pythona](Python_console/pl.md):


```python
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(140, 40, 7, App.Vector(0, -20, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(120, 0, 7))
box2 = Part.makeBox(20, 12, 10, App.Vector(5, -6, 7))
cyl2 = Part.makeCylinder(6, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(4, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
shape = box1.fuse([cyl1, box2, cyl2]).removeSplitter().cut(cyl3)
base = doc.addObject("Part::Feature", "Base")
base.Shape = shape

box1 = Part.makeBox(4, 12, 12, App.Vector(-12, -6, 0))
box2 = Part.makeBox(14, 12, 4, App.Vector(-8, -6, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(0, 0, 4))
cyl2 = Part.makeCylinder(4, 88, App.Vector(-12, 0, 6),App.Vector(-1, 0, 0))
shape = box1.fuse([box2, cyl1, cyl2]).removeSplitter()
slider_rod = doc.addObject("Part::Feature", "SliderRod")
slider_rod.Shape = shape
slider_rod.Placement.Base = App.Vector(100, -40, 0)

cyl1 = Part.makeCylinder(7.5, 4)
box1 = Part.makeBox(15, 30, 4, App.Vector(-7.5, 0, 0))
cyl2 = Part.makeCylinder(7.5, 4, App.Vector(0, 30, 0))
cyl3 = Part.makeCylinder(4, 6, App.Vector(0, 30, 4))
cyl4 = Part.makeCylinder(4, 4)
shape = cyl1.fuse([box1, cyl2]).removeSplitter().fuse(cyl3).cut(cyl4)
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = shape
crank.Placement.Base = App.Vector(125, -70, 0)

cyl1 = Part.makeCylinder(6, 4)
box1 = Part.makeBox(50, 12, 4, App.Vector(0, -6, 0))
cyl2 = Part.makeCylinder(6, 4, App.Vector(50, 0, 0))
cyl3 = Part.makeCylinder(4, 4)
cyl4 = Part.makeCylinder(4, 4, App.Vector(50, 0, 0))
shape = cyl1.fuse([box1, cyl2]).removeSplitter().cut(cyl3.fuse(cyl4))
connecting_rod = doc.addObject("Part::Feature", "ConnectingRod")
connecting_rod.Shape = shape
connecting_rod.Placement.Base = App.Vector(25, -70, 0)

mat = base.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
base.ViewObject.ShapeAppearance = (mat,)

mat = slider_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
slider_rod.ViewObject.ShapeAppearance = (mat,)

mat = crank.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
crank.ViewObject.ShapeAppearance = (mat,)

mat = connecting_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.0, 0.0)
connecting_rod.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



#### Dodawanie złożenia 

Przy pomocy polecenia <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:16px;"> [Utwórz złożenie](Assembly_CreateAssembly/pl.md) dodaj do dokumentu złożenie.

<img alt="" src=images/Assembly_KinematicExample-01.png  style="width:200px;">



*Widok drzewa części i złożenia.*



### Przenieś części do złożenia 

W [Widoku drzewa](Tree_view/pl.md) przeciągnij i upuść części na obiekt Złożenia. Teraz mogą być one obsługiwane przez solver złożeń.

<img alt="" src=images/Assembly_KinematicExample-02.png  style="width:200px;">



*Części są teraz w kontenerze złożeń.*



### Kotwienie części 

Aby utrzymać złożenie w pożądanej pozycji, część bazowa powinna zostać zablokowana lub zakotwiona, jak to się tutaj nazywa. Wybierz bazę w [widoku drzewa](Tree_view/pl.md) lub w [widoku 3D](3D_view/pl.md) i użyj polecenia <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md). Spowoduje to ustalenie pozycji Bazy w odniesieniu do lokalnego układu współrzędnych (LCS) kontenera złożenia. Obiekt GroundedJoint zostanie dodany do kontenera Joints.

<img alt="" src=images/Assembly_KinematicExample-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-04.png  style="width:240px;">



*Rozwiń kontener Połączeń, aby znaleźć obiekt Zakotwienia połaczeń.*



### Alternatywa: Wstaw łącze 

Zamiast dwóch kroków opisanych wyżej, można również użyć polecenia <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Wstaw łącze](Assembly_InsertLink/pl.md) aby umieścić obiekty w złożeniu. Pierwszy obiekt automatycznie zostaje zakotwiony. Musisz więc zacząć od obiektu podstawy. To polecenie tworzy łącza i oryginalne obiekty pozostają poza złożeniem. Aby uniknąć wątpliwości, zalecane jest wyłączanie ich widoczności.



### Zastosuj połączenia 

Połączenie łączy dokładnie dwa elementy różnych części. Można je opcjonalnie wybrać przed wywołaniem żądanego polecenia połączenia *(dowolna liczba wybranych elementów innych niż dwa powoduje pusty wybór)*. Elementy definiują położenie i orientację LCS reprezentowanego przez wypełniony okrąg na lokalnej płaszczyźnie XY i trzy linie wzdłuż lokalnych osi X *(czerwony)*, Y *(zielony)* i Z *(niebieski)*.

-   Połączenie obrotowe między podstawą a korbą.

<img alt="" src=images/Assembly_KinematicExample-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-06.png  style="width:200px;">



*Zaznaczone elementy + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Utwórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md) → przestawiona korba.*

Przesuń **Korbę** używając lewego przycisku myszy. Tylko obrót wokół osi powinien być możliwy.

-   Połączenie przesuwne między podstawą a suwakiem.

<img alt="" src=images/Assembly_KinematicExample-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-08.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Utwórz połączenie przesuwne](Assembly_CreateJointSlider/pl.md) → przestawiony suwak*

Przesuń **Suwak** używając lewego przycisku myszy. Tylko przemieszczenie wzdłuż jego osi powinno być możliwe.

-   Połączenie obrotowe między korbą a korbowodem.

<img alt="" src=images/Assembly_KinematicExample-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-10.png  style="width:200px;">



*Zaznaczone elementy + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Utwórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md) → przestawiony korbowód*

Przesuń **Korbowód** używając lewego przycisku myszy. Tylko obrót wokół osi powinien być możliwy.

<img alt="" src=images/Assembly_KinematicExample-11.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-12.png  style="width:200px;">



*Jeśli jest kilka połączeń w linii, musimy pomóc solverowi w znalezieniu sensownego rozwiązania.
Jeśli to konieczne, kliknij i przeciągnij części do łatwiejszej do obliczenia pozycji.*

-   Połączenie cylindryczne między korbowodem a suwakiem.

<img alt="" src=images/Assembly_KinematicExample-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-14.png  style="width:200px;">



*Zaznaczone elementy +<img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md) → zakończone złożenie*

W gotowym złożeniu użyj kursora myszki, aby przeciągnąć części zgodnie z użytymi połączeniami.



#### Uwaga

Sworzeń pręta suwaka jest nadmiarowo zorientowany. Jego oś jest równoległa do sworznia podstawy poprzez łańcuch kinematyczny z podstawy przez korbę i korbowód, t.j. jego lokalna oś Z nie może się obracać wokół żadnej osi X lub Y. Połączenie przesuwne również zapobiega obrotowi jego osi Z wokół dwóch lokalnych osi a więc skutkuje dwoma nadmiarowo związanymi stopniami swobody. Połączenie cylindryczne zamiast przesuwnego zablokowałoby tylko jeden obrót skutkując pojedynczym nadmiernie związanym stopniem swobody.



### Napęd korby 

Aby kontrolować układ złożenia za pomocą kąta między podstawą a korbą, musimy zmienić połączenie obrotowe na stałe. Aby to zrobić, kliknij dwukrotnie obiekt Obrotowy w widoku drzewa. W oknie dialogowym zmień Obrotowy na Stały i zmień wartość obrotu zgodnie z potrzebą *(ruch powinien podążać za ruchem kółka myszki)*.

Zauważ, że zmiana typu połączenia zmieni jego etykietę, ale nie nazwę. W tym przypadku etykiety zostaje zmieniona na \"Stałe\".

Aby dokonać animacji złożenia, możemy zmienić obrót (Offset1.Angle) połączenia stałego używając kodu Pythona. Po prostu skopiuj i wklej następujące linie do konsoli Pythona:


```python
import math
import FreeCAD as App
import FreeCADGui as Gui

actuator = App.ActiveDocument.getObjectsByLabel("Fixed")[0]

for angle in range(0, 361, 10):
    # A full rotation of the Crank in steps of 10°
    actuator.Offset1.Rotation.Angle = math.radians(angle)
    App.ActiveDocument.recompute()
    Gui.updateGui()
```

Koniec zakresu musi być większy niż 360, aby uwzględnić ten kąt jako prawidłowy wynik.


</div>


</div>



## Przykład - przegub Cardana 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:80px;"> Ten przykład jest tymczasowy i może zostać usunięty gdy pojawią się odpowiednie opisy/przykłady.


<div class="mw-collapsible-content">



### Złożenie przegubu Cardana 

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:300px;">

W tym przykładzie tworzony jest [przegub Cardana](https://pl.wikipedia.org/wiki/Przegub_Cardana).

Złożenie składa się z trzech części bryłowych: dwóch identycznych widelców i krzyżowego łącznika. Potrzebne są też dwa dodatkowe elementy niebryłowe, oś 1 i oś 2 reprezentujące osie pod kątem. Osie i części bryłowe są połączone kilkoma połączeniami.



### Przygotowanie części 

W tym przykładzie wszystkie części i złożenie są tworzone w jednym dokumencie.

Poniższy kod Pythona utworzy nowy dokument z czterema obiektami (tylko 1 widelec). Po prostu skopiuj i wklej następujące linie do [konsoli Pythona](Python_console/pl.md):


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = -80
axle1.Y2 = 0
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 80
axle2.Y2 = 0
axle2.Z2 = 0
axle2.Placement.Rotation.Angle = math.radians(20)

sph1 = Part.makeSphere(50, App.Vector(0, 0, 0), App.Vector(-1, 0, 0), 0, 90, 360)
box1 = Part.makeBox(50, 40, 80, App.Vector(-50, -20, -40))
cyl1 = Part.makeCylinder(20, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(20, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(30, 60, App.Vector(0, -30, 0), App.Vector(0, 1, 0))
box2 = Part.makeBox(30, 60, 60, App.Vector(0, -30, -30))
cyl4 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl5 = Part.makeCylinder(15, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
shape = sph1.common(box1).fuse([cyl1, cyl2]).cut(cyl3.fuse([box2, cyl4, cyl5]))
fork = doc.addObject("Part::Feature", "Fork")
fork.Shape = shape.removeSplitter()
fork.Placement.Base = App.Vector(0, 100, 0)

cyl1 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(15, 80, App.Vector(0, -40, 0), App.Vector(0, 1, 0))
shape = cyl1.fuse([cyl2])
cross = doc.addObject("Part::Feature", "Cross")
cross.Shape = shape.removeSplitter()
cross.Placement.Base = App.Vector(70, 100, 0)

mat = fork.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fork.ViewObject.ShapeAppearance = (mat,)

mat = cross.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cross.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Zmień kąt osi 

Kąt między osiami jest ustawiony na 20 stopni. Jeśli chcesz zmienić tą wartość, wybierz oś 2 i ustaw właściwość Umiejscowienie.Kąt. Ta właściwość musi być zmieniona przed przesunięciem osi 2 do złożenia.

Ostrzeżenie: części mogą ze sobą kolidować jeśli kąt jest zbyt duży.



#### Dodawanie złożenia 

Dodaj złożenie do dokumentu korzystając z narzędzia <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Utwórz złożenie](Assembly_CreateAssembly/pl.md).



### Przenieś osie do złożenia 

W [widoku drzewa](Tree_view/pl.md) przeciągnij i upuść osie do obiektu Złożenie.



### Zakotwienie osi 

Wybierz dwie osie w widoku drzewa i użyj narzędzia <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md).



### Przenieś części bryłowe do złożenia 

Dla innych obiektów użyjemy narzędzia <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Wstaw komponent](Assembly_InsertLink/pl.md):

1.  Wywołaj to narzędzie.
2.  W oknie dialogowym, które zostanie otwarte kliknij raz na obiekcie łącznika krzyżowego i dwa razy na obiekcie widelca.
3.  Wciśnij przycisk **OK**.
4.  Schowaj obiekty poza złożeniem.
5.  Jeśli obiekty w złożeniu za bardzo na siebie nachodzą, możesz je przeciągnąć do nowej pozycji.



### Zastosuj połączenia 

-   Połączenie obrotowe między osią 1 i łącznikiem krzyżowym

<img alt="" src=images/Assembly_UniversalJointExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-03.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Utweórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md) + Odsunięcie +40mm lub -40mm → przestawiony widelec 1*

Jeśli najpierw wywołujesz narzędzie a następnie wskazujesz elementy, możesz kliknąć w pobliżu prawidłowego punktu końcowego osi 1 aby uniknąć konieczności wprowadzania odsunięcia.

-   Połączenie cylindryczne między widelcem 1 i łącznikiem krzyżowym

<img alt="" src=images/Assembly_UniversalJointExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-05.png  style="width:200px;">



*Zaznaczone elementy +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md) → przestawiony łącznik krzyżowy*

-   Połączenie cylindryczne między osią 1 i widelcem 2

<img alt="" src=images/Assembly_UniversalJointExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-07.png  style="width:200px;">



*Zaznaczone elementy +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md) → przestawiony widelec 2*

Jeśli to konieczne, odwróć kierunek połączenia używając przycisku **<img src="images/Button_sort.svg" width=16px>** w panelu zadań.

-   Połączenie cylindryczne między łącznikiem krzyżowym i widelcem 2

<img alt="" src=images/Assembly_UniversalJointExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-09.png  style="width:200px;">



*Zaznaczone elementy +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md) → przestawiony łącznik krzyżowy i widelec 2*



### Sterowanie przegubem Cardana 

Przegubem Cardana można sterować ruszając widelec 1 lewym przyciskiem myszy.

Jeśli chcesz sprawdzić sytuację dla osobnych kątów obrotu:

1.  Zmień połączenie cylindryczne między osią 1 i widelcem 1 na połączenie stałe.
2.  Wybierz właściwość Odsunięcie1.Kąt połączenia stałego i przesuń kółko myszy.
3.  Przegub Cardana może być ustawiony dla dowolnego kąta.


</div>


</div>



## Przykład - imadło 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:80px;"> Ten przykład jest tymczasowy i może zostać usunięty gdy pojawią się odpowiednie opisy/przykłady.


<div class="mw-collapsible-content">



### Złożenie imadła 

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:300px;">

W tym przykładzie modelowane jest [imadło](https://pl.wikipedia.org/wiki/Imad%C5%82o).

Złożenie składa się z trzech części bryłowych: stałej i ruchomej szczęki oraz śruby z dźwignią. Potrzebny jest też jeden dodatkowy element niebryłowy - korba. Między korbą a częściami bryłowymi jest kilka połączeń.

Połączenie śrubowe wiąże przesunięcie części z połączeniem przesuwnym z rotacją części z połączeniem obrotowym. Śruba powinna wykonywać ruch translacyjny i rotacyjny, więc musi być częścią z połączeniem cylindrycznym. W tym złożeniu śruba będzie sprzężona z ruchomą szczęką połączeniem dystansowym, z niebryłową korbą połączeniem równoległym a z nieruchomą szczęką połączeniem cylindrycznym.



### Przygotowanie części 

W tym przykładzie wszystkie części i złożenie są tworzone w jednym dokumencie.

Poniższy kod Pythona utworzy nowy dokument z czterema obiektami. Po prostu skopiuj i wklej następujące linie do [konsoli Pythona](Python_console/pl.md):


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(95, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box4 = Part.makeBox(35, 24, 24, App.Vector(0, -12, -12))
box5 = Part.makeBox(60, 34, 69, App.Vector(35, -17, -19))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
box7 = Part.makeBox(95, 90, 10, App.Vector(0, -45, -32))
shape = box1.fuse([cyl1, box2, box6, box7]).cut(cyl2.fuse([box3, cyl3, cyl4, cyl5, box4, box5]))
fixedJaw = doc.addObject("Part::Feature", "FixedJaw")
fixedJaw.Shape = shape.removeSplitter()
fixedJaw.Placement.Rotation.Axis = App.Vector(0, 0, 1)
fixedJaw.Placement.Rotation.Angle = math.radians(180)

box1 = Part.makeBox(35, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(160, 24, 24, App.Vector(-160, -12, -12))
box4 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box5 = Part.makeBox(160, 18, 18, App.Vector(-160, -9, -9))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
shape = box1.fuse([cyl1, box2, box3, box6]).cut(cyl2.fuse([box4, cyl3, cyl4, box5, cyl5]))
movableJaw = doc.addObject("Part::Feature", "MovableJaw")
movableJaw.Shape = shape.removeSplitter()
movableJaw.Placement.Base = App.Vector(150, 100, 0)

cyl1 = Part.makeCylinder(5, 190, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cyl2 = Part.makeCylinder(10, 20, App.Vector(190, 0, 0), App.Vector(1, 0, 0))
cyl3 = Part.makeCylinder(4, 100, App.Vector(200, 0, -50), App.Vector(0, 0, 1))
shape = cyl1.fuse([cyl2, cyl3])
leverScrew = doc.addObject("Part::Feature", "LeverScrew")
leverScrew.Shape = shape.removeSplitter()
leverScrew.Placement.Base = App.Vector(150, -100, 0)

wire1 = Part.makePolygon([App.Vector(0, 0, 100), App.Vector(0, 0, 0), App.Vector(100, 0, 0)])
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = wire1
crank.Placement.Base = App.Vector(0, -100, 0)

mat = fixedJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fixedJaw.ViewObject.ShapeAppearance = (mat,)

mat = movableJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
movableJaw.ViewObject.ShapeAppearance = (mat,)

mat = leverScrew.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
leverScrew.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



#### Dodawanie złożenia 

Dodaj złożenie do dokumentu korzystając z narzędzia <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Utwórz złożenie](Assembly_CreateAssembly/pl.md).



#### Przenieś części do kontenera złożeń 

W [widoku drzewa](Tree_view/pl.md) przeciągnij i upuść części na obiekt Złożenia. Teraz mogą być one obsługiwane przez solver złożeń.



### Kotwienie części 

Aby utrzymać złożenie w żądanej pozycji, stała szczęka powinna być zablokowana (zakotwiona, jak się to określa w tym przypadku). Wybierz ją w [widoku drzewa](Tree_view/pl.md) lub w [widoku 3D](3D_view/pl.md) i użyj narzędzia <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md). Obiekt GroundedJoint zostanie dodany do kontenera połączeń.



### Zastosuj połączenia 

-   Połączenie obrotowe między stałą szczęką a korbą.

<img alt="" src=images/Assembly_ViseExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-03.png  style="width:200px;">



*Zaznaczone elementy + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Utwórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md) → przestawiona korba.*

-   Połączenie przesuwne między stałą a ruchomą szczęką

<img alt="" src=images/Assembly_ViseExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-05.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Utwórz połączenie przesuwne](Assembly_CreateJointSlider/pl.md) → przestawiona ruchoma szczęka*

Ustaw minimalną długość na -77 mm i maksymalną długość na -7 mm. To ogranicza rozwarcie imadła do 70 mm.

Następne trzy połączenia są konieczne do zmuszenia śruby do: przesuwania jak ruchoma szczęka, obrotu jak korba i obrotu wokół głównej osi.

-   Połączenie dystansowe między śrubą a ruchomą szczęką

<img alt="" src=images/Assembly_ViseExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-07.png  style="width:200px;">



*Zaznaczone elementy + <img src="images/Assembly_CreateJointDistance.svg" width=24px> [Utwórz połączenie dystansowe](Assembly_CreateJointDistance/pl.md) → przestawiona śruba*

Wybierz dwie ściany. Ustaw odległość na 20 mm.

-   Połączenie równoległe między śrubą a korbą

<img alt="" src=images/Assembly_ViseExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-09.png  style="width:200px;">



*Zaznaczone elementy + <img src="images/Assembly_CreateJointParallel.svg" width=24px> [Utwórz połączenie równoległe](Assembly_CreateJointParallel/pl.md) → przestawiona śruba*

-   Połączenie cylindryczne między śrubą a stałą szczęką

<img alt="" src=images/Assembly_ViseExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-11.png  style="width:200px;">



*Zaznaczone elementy +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md) → przestawiona śruba*

-   Połączenie śrubowe między ruchomą szczęką a korbą

<img alt="" src=images/Assembly_ViseExample-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-13.png  style="width:200px;">



*Zaznaczone elementy (śruba niewidoczna) + <img src="images/Assembly_CreateJointScrew.svg" width=24px> [Utwórz połączenie śrubowe](Assembly_CreateJointScrew/pl.md) → cały mechanizm imadła (śruba widoczna)*

Jeśli to konieczne, schowaj śrubę podczas wskazywania.

Ustaw promień skoku na 5 mm



### Napęd imadła 

Imadło może być napędzane poprzez poruszanie korbą i ruchomą szczęką przy pomocy lewego przycisku myszy.


</div>


</div>



## Przykład - amortyzator 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ShockAbsorberExample-01.png  style="width:80px;"> Ten przykład jest tymczasowy i może zostać usunięty gdy pojawią się odpowiednie opisy/przykłady.


<div class="mw-collapsible-content">



### Złożenie amortyzatora 

<img alt="" src=images/Assembly_ShockAbsorberExample.gif  style="width:300px;">

W tym przykładzie tworzony jest [amortyzator](https://pl.wikipedia.org/wiki/Amortyzator).

Złożenie składa się z trzech części bryłowych: tłoka, cylindra i sprężyny. Potrzebne są również trzy dodatkowe elementy niebryłowe - dwie osie i pręt. Wszystkie części są połączone kilkoma połączeniami.

Zawias tłoka obraca się wokół osi 2, podczas gdy zawias cylindra przesuwa się na łuku okręgu wyśrodkowanego na osi 1. Niebryłowy pręt jest wykorzystywany do tego ruchu. Długość pręta jest promieniem łuku.



### Przygotowanie części 

Poniższy kod Pythona utworzy nowy dokument z 6 obiektami. Utwórz nowe [makro](Macros/pl.md) i wklej poniższy kod do edytora Pythona (nie do konsoli Pythona). Następnie [uruchom to makro](Std_DlgMacroExecuteDirect/pl.md).

Poniższy kod nie może zostać uruchomiony z konsoli Pythona, ponieważ sprężyna musi być obiektem [Part::FeaturePython](App_FeaturePython/pl.md) definiowanym przez klasę z funkcjami zwrotnymi {{Incode|execute()}} i {{Incode|onChanged()}}. Tylko wtedy można zmienić jej wysokość poprzez właściwość.


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

class Spring():
    def __init__(self, spring):
        spring.addProperty("App::PropertyLength", "Height", "Spring", "Height of the helix").Height = 200.0
        spring.Proxy = self
        spring.ViewObject.Proxy = 0
        
    def execute(self, spring):
        helix = Part.makeHelix(spring.Height/8.5, spring.Height, 35)
        startPnt = helix.Edges[0].Curve.value(0)
        section = Part.Wire([Part.Circle(startPnt, App.Vector(0, 1, 0), 5).toShape()])
        hel1 = helix.makePipeShell([section], True, True)
        box1 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, -10))
        box2 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, spring.Height))
        shape = hel1.cut(box1).cut(box2)
        spring.Shape = shape
        
    def onChanged(self, spring, prop):
        if prop == "Height":
            self.execute(spring) 
            
spring = doc.addObject("Part::FeaturePython", "Spring")
Spring(spring)
spring.Placement.Base = App.Vector(0, 100, 0)

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = 0
axle1.Y2 = 80
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 0
axle2.Y2 = 80
axle2.Z2 = 0
axle2.Placement.Base = App.Vector(120, 0, -250)

rod = doc.addObject("Part::Line", "Rod")
rod.X2 = 100
rod.Y2 = 0
rod.Z2 = 0
rod.Placement.Base = App.Vector(0, -50, 0)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10, App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(5, 130)
cyl7 = Part.makeCylinder(20, 5,App.Vector(0, 0, 130))
shape = cyl1.fuse([tor1,cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, cyl7])
piston = doc.addObject("Part::Feature", "Piston")
piston.Shape = shape.removeSplitter()
piston.Placement.Base = App.Vector(200, 100, -200)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(25, 130)
tor2 = Part.makeTorus(20, 5,App.Vector(0, 0, 130))
cyl7 = Part.makeCylinder(20, 135)
cyl8 = Part.makeCylinder(20, 130)
cyl9 = Part.makeCylinder(5, 135)
shape = cyl1.fuse([tor1, cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, tor2, cyl7]).cut(cyl8.fuse([cyl9]))
cylinder = doc.addObject("Part::Feature", "Cylinder")
cylinder.Shape = shape.removeSplitter()
cylinder.Placement.Rotation.Axis = App.Vector(0, 1, 0)
cylinder.Placement.Rotation.Angle = math.pi
cylinder.Placement.Base = App.Vector(100, 100, 0)

mat = piston.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
piston.ViewObject.ShapeAppearance = (mat,)

mat = cylinder.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cylinder.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



#### Dodawanie złożenia 

Dodaj złożenie do dokumentu korzystając z narzędzia <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Utwórz złożenie](Assembly_CreateAssembly/pl.md).



#### Przenieś części do kontenera złożeń 

W [Widoku drzewa](Tree_view/pl.md) przeciągnij i upuść części na obiekt Złożenia. Teraz mogą być one obsługiwane przez solver złożeń.



### Zakotwienie dwóch osi 

Aby utrzymać złożenie w żądanej pozycji, dwie osie powinny być zablokowane (zakotwione, jak się to określa w tym przypadku). Wybierz je w [widoku drzewa](Tree_view/pl.md) lub w [widoku 3D](3D_view/pl.md) i użyj narzędzia <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Włącz / wyłącz zakotwienie](Assembly_ToggleGrounded/pl.md). Dwa obiekty GroundedJoint zostaną dodane do kontenera połączeń.



### Zastosuj połączenia 

-   Połączenie obrotowe między osią 1 i tłokiem

<img alt="" src=images/Assembly_ShockAbsorberExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-03.png  style="width:200px;">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Utwórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md) + Wybrane elementy → przestawiony tłok*

-   Połączenie przesuwne między tłokiem a cylindrem

<img alt="" src=images/Assembly_ShockAbsorberExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-05.png  style="width:200px;">



*<img src="images/Assembly_CreateJointSlider.svg" width=24px> [Utwórz połączenie przesuwne](Assembly_CreateJointSlider/pl.md) + Wybrane elementy → przestawiony i przesunięty cylinder*

Uważaj na lokalizację układu położenia przed wskazaniem ściany. Powinien on być na środku każdej ściany.

Przeciągnij cylinder aby utworzyć przerwę między nim i tłokiem. Ściany stanowiące podstawy dla sprężyny powinny być widoczne.

-   Połączenie dystansowe między tłokiem a cylindrem

<img alt="" src=images/Assembly_ShockAbsorberExample-06A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-06B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-07.png  style="width:200px;">



*<img src="images/Assembly_CreateJointDistance.svg" width=24px> [Utwórz połączenie dystansowe](Assembly_CreateJointDistance/pl.md) + Wybrane ściany → przestawiony cylinder z odległością ustawioną na 200 mm*

Ustaw wartość odległości na 200 mm.

Następne dwa połączenia są konieczne aby zmusić zawias cylindra do ruchu po łuku okręgu.

-   Połączenie cylindryczne między osią 1 a prętem

<img alt="" src=images/Assembly_ShockAbsorberExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-09.png  style="width:200px;">



*<img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Utwórz połączenie cylindryczne](Assembly_CreateJointCylindrical/pl.md) + Wybrane elementy → przestawiony pręt*

Upewnij się, że oś Z układu współrzędnych (niebieska) jest prostopadła do pręta wybierając punk końcowy.

-   Połączenie obrotowe między prętem a cylindrem

<img alt="" src=images/Assembly_ShockAbsorberExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-11.png  style="width:200px;">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Utwórz połączenie obrotowe](Assembly_CreateJointRevolute/pl.md) + Wybrane elementy → przestawiony cylinder*

Ponownie upewnij się, że oś Z układu współrzędnych (niebieska) jest prostopadła do pręta.

Możesz napotkać problemy z tym połączeniem. Jeśli tak jest, spróbuj:

1.  Usunąć połączenie.
2.  Przełączyć się na [widok z przodu](Std_ViewFront/pl.md).
3.  Obrócić złożenie (przeciągając tłok) i pręt, tak że środek otworu zawiasu cylindra leży na pręcie.
4.  Utworzyć połączenie ponownie.

Następne dwa połączenia są konieczne aby zamocować sprężynę do ściany podstawy.

-   Połączenie równoległe między sprężyną a tłokiem

<img alt="" src=images/Assembly_ShockAbsorberExample-12A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-12B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-13.png  style="width:200px;">



*<img src="images/Assembly_CreateJointParallel.svg" width=24px> [Utwórz połączenie równoległe](Assembly_CreateJointParallel/pl.md) + Wybrane ściany → przestawiona sprężyna*

Wybierz środek ściany podstawy tłoka i środek dolnej ściany sprężyny. Zachowaj wartość odległości 0.

-   Połączenie stałe między sprężyną a tłokiem

<img alt="" src=images/Assembly_ShockAbsorberExample-14A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-14B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-15.png  style="width:200px;">



*<img src="images/Assembly_CreateJointFixed.svg" width=24px> [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl.md) + Wybrane elementy → przestawiona sprężyna*

Wybierz dolny wierzchołek szwu cylindra tłoka i narożnikowy wierzchołek sprężyny.

-   Połącz właściwość odległości połączenia **Distance** z właściwością **Height** sprężyny używając [wyrażenia](Expressions/pl.md):

1.  Wybierz sprężynę w [widoku drzewa](Tree_view/pl.md).
2.  Wybierz niebiską ikonę <img alt="" src=images/Bound-expression.svg  style="width:16px;"> w polu właściwości Height.
3.  Wprowadź w edytorze wyrażeń: {{Incode|<<Distance>>.Distance}}



### Napęd amortyzatora 

Aby ruszać amortyzatorem, kliknij dwukrotnie na obiekcie Distance w widoku drzewa i zmień jego właściwość Distance. Przelicz dokument. Sprężyna zmieni swoją długość.


</div>


</div>





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Assembly](Category_Assembly.md) > Assembly Workbench/pl
