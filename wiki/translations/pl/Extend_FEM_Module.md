---
 TutorialInfo:l
   Topic: MES
   Level: Średnio zaawansowany
   Time: 1 godzina
   Author: User:M42kus
   FCVersion: 0.17
---

# Extend FEM Module/pl





Środowisko pracy MES obsługuje już wiele różnych wiązań i kilka solwerów. Mimo to użytkownicy często potrzebują więzów, które nie są jeszcze obsługiwane przez FreeCAD. Ta strona jest punktem wyjścia do serii samouczków i innych zasobów opisujących, jak rozszerzyć środowisko pracy MES przy użyciu istniejącej struktury. Chociaż ta seria może okazać się pomocna również dla programistów, ideą jest umożliwienie użytkownikom MES, którzy interesują się kodowaniem w Pythonie, możliwości samodzielnego dodawania potrzebnych rzeczy.

Dodawanie nowych wiązań, równań lub solwerów to w większości rutynowa praca. Ale zrobienie tego po raz pierwszy nie będzie tak łatwe, jak mogłoby się wydawać. Zrozumienie poniższych tematów okaże się pomocne:

-   Tworzenie skryptów w języku Python we FreeCAD.
    -   [Poradnik: Tworzenie skryptów Python](Python_scripting_tutorial/pl.md)
    -   [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md)
-   Rozszerzanie FreeCAD za pomocą Python.
    -   [Obiekty tworzone skryptami](Scripted_objects/pl.md)
-   Ważne jest gruntowne zrozumienie solwera, dla którego będą dodawane nowe obiekty *(np. CalculiX lub Elmer)*.
-   Niewielka wiedza na temat systemów kompilacji, zwłaszcza `cmake` *(system kompilacji używany przez FreeCAD)*.



## System kompilacji *(cmake)* 

System kompilacji musi zostać zmodyfikowany niezależnie od tego, które obiekty zostaną dodane do środowiska pracy MES. Każdy moduł (plik) Python musi zostać zarejestrowany. Środowisko pracy FEM wymaga zarejestrowania każdego nowego modułu Python w `Mod/Fem/CMakeLists.txt`. Jest to niezależne od typu modułu Python *(GUI lub non-GUI)*. To, gdzie dokładnie moduł musi zostać wstawiony, zależy od jego roli. Solwer, równania i ograniczenia używają różnych list. Wyszukiwanie podobnych plików i wstawianie nowego pliku do tej samej listy działa przez większość czasu.

Jako *przykład* dodajmy nowe wiązanie o nazwie  dla tego wiązania. Nowe ograniczenie wymaga co najmniej następujących nowych modułów:

-    `constraint_<name>.py`
    

-    `view_constraint_<name>.py`
    

-    `CommandFemConstraint<name>.py`(może być niepotrzebny)

Te trzy pliki muszą zostać dodane do `Mod/Fem/CMakeLists.txt`, a także `Mod/Fem/App/CMakeLists.txt`. Wszystkie dodane linie kodu są oznaczone znakiem *+* na początku.


**Mod/Fem/CMakeLists.txt**


{{code|code=
SET(FemObjects_SRCS
    femobjects/__init__.py
    femobjects/base_fempythonobject.py
    femobjects/constraint_bodyheatsource.py
    femobjects/constraint_electrostaticpotential.py
    femobjects/constraint_flowvelocity.py
    femobjects/constraint_initialflowvelocity.py
+   femobjects/constraint_initialflowpressure.py
    femobjects/constraint_selfweight.py
...
    femobjects/solver_ccxtools.py
)
...
SET(FemGuiViewProvider_SRCS
    femviewprovider/__init__.py
    femviewprovider/view_base_femconstraint.py
    femviewprovider/view_base_femobject.py
    femviewprovider/view_constraint_bodyheatsource.py
    femviewprovider/view_constraint_electrostaticpotential.py
    femviewprovider/view_constraint_flowvelocity.py
+   femviewprovider/view_constraint_flowpressure.py
    femviewprovider/view_constraint_initialflowvelocity.py
    femviewprovider/view_constraint_selfweight.py
...
    femviewprovider/view_solver_ccxtools.py
)
}}



## Organizacja źródła 

Do organizacji kodu Python moduł MES wykorzystuje następujące podejście. Moduł jest podzielony na następujące pakiety:

-    `femobjects`, który zawiera wszystkie obiekty niezwiązane z GUI, takie jak proxy Python dla obiektów dokumentów, \* `femviewproviders`, który zawiera wszystkie obiekty związane z GUI, takie jak proxy Python dla obiektów dokumentów.

-    `femviewproviders`zawierający wszystko, co związane z GUI, takie jak pythonowe proxy dla dostawców widoków.

-   Panele zadań oparte na C++ są przechowywane w \'`Gui`\',

-   ikony można znaleźć w \'`Gui/Resources/icons/`\',

-   pliki .ui są przechowywane w poleceniach \'`Gui/Resources/ui/`\'.

Jeden pakiet nie jest zgodny z tym wzorcem: `femsolver`. Ma on swoje miejsce na tym samym poziomie co `femobjects` i `femguiobjects` (`src/Mod/Fem/femsolver`). Pakiet zawiera pakiety i moduły związane z solwerem i równaniami i jest zorganizowany w następujący sposób:

    .femsolver
    .femsolver.elmer
    .femsolver.elmer.equations
    .femsolver.calculix
    .femsolver.calculix.equations
    .femsolver.z88
    .femsolver.z88.equations



## Solwer

W FreeCAD solwer można podzielić na dwie części:

-   Jedna to obiekt dokumentu używany przez użytkownika do interakcji z solwerem. Można poprzez niego ustawić parametry solwera i jest on również używany do kontrolowania procesu rozwiązywania.
-   Druga część to tak zwane zadania solwera. Proces rozwiązywania jest podzielony na te zadania, a mianowicie: *sprawdź, przygotuj, rozwiąż i wyniki*. Zadania te wykonują rzeczywistą pracę polegającą na wyeksportowaniu analizy do formatu rozumianego przez plik wykonywalny solwera, uruchomieniu pliku wykonywalnego i załadowaniu wyników z powrotem do FreeCAD.

Większość plików związanych z solwerem znajduje się w pakiecie podrzędnym pakietu `femsolver` *(np. dla Elmera w `femsolver/elmer`)*. Poniższa lista wylicza wszystkie pliki związane z implementacją solwera. Są to pliki, które należy skopiować i zmodyfikować, aby dodać obsługę nowego solwera do FreeCAD. Podany przykład pochodzi z implementacji solwera Elmer.

-   **femsolver/elmer/solver.py:** Obiekt dokumentu widoczny w widoku drzewa. Zaimplementowane w Pythonie poprzez proxy dokumentu i proxy widoku.
-   **femsolver/elmer/tasks.py:** Moduł zawierający jedną klasę zadań dla każdego zadania wymaganego dla implementacji solwera. Zadania te dzielą proces rozwiązywania analizy na następujące kroki: sprawdzenie, przygotowanie, rozwiązanie, wyniki.
-   **femcommands/commands.py:** Dodaje obiekt dokumentu solwera do aktywnego dokumentu. Wymagane, aby uzyskać dostęp do obiektu solwera z GUI.



## Równania

Równanie reprezentuje określoną fizykę, która powinna być brana pod uwagę podczas rozwiązywania analizy *(np. Przepływ, Ciepło)*. Nie wszystkie solwery w FreeCAD obsługują *(wszystkie)* równania. Równania są reprezentowane przez obiekty podrzędne odpowiedniego obiektu solwera. W widoku drzewa wygląda to następująco:

-   elmer-solver
    -   elastyczność
    -   ciepło
    -   przepływ
    -   elektrostatyka

Większość opcji specyficznych dla solwera *(np. maksymalna liczba iteracji, metoda rozwiązywania itp.)* jest ustawiana za pomocą obiektów równań. Jedną z konsekwencji tego jest to, że każdy solwer musi mieć własną implementację \"tego samego\" równania. CalculiX miałby inny obiekt Heat niż Elmer. Aby uniknąć posiadania wielu przycisków dla tej samej fizyki w GUI, każdy obiekt solwera sam dodaje swoje równania.

Rzeczywistą implementację można podzielić na część ogólną i część specyficzną dla solwera. Część ogólna znajduje się w module `femsolver.equationbase`. Część specyficzna dla solwera znajduje się w poszczególnych pakietach Equations pakietów solwera *(np. `femsolver/elmer/equations`)*.

Dodanie nowych równań do Elmera powinno być bardzo proste. Dla początkujących istnieje poradnik, który pokazuje, jak dodać nowe równanie do Elmera poprzez dodanie istniejącego solwera sprężystości do FreeCAD: [Poradnik: Dodawanie równań w środowisku MES](Add_FEM_Equation_Tutorial/pl.md).



## Wiązania

Wiązania definiują warunki brzegowe dla problemu, który ma zostać rozwiązany. W FreeCAD wiązania nie są specyficzne dla konkretnego solwera. Konfiguracja problemu może być rozwiązana przez wszystkie solwery, które obsługują wszystkie warunki w analizie.

Dodawanie nowych wiązań jest dość proste. Dla początkujących dostępny jest poradnik: [Poradnik: Dodawanie wiązań w środowisku MES](Add_FEM_Constraint_Tutorial/pl.md)



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Extend FEM Module/pl
