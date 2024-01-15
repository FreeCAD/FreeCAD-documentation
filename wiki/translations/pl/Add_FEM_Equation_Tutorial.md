---
 TutorialInfo:l
   Topic: Dodawanie równań MES
   Level: Zaawansowany
   Time: 1 dzień
   Author: User:JohnWang
   FCVersion: 0.19
---

# Add FEM Equation Tutorial/pl







## Wprowadzenie

W tym poradniku dodamy równanie **Flow** (przepływu) do FreeCAD i zaimplementujemy wsparcie dla solvera Elmer. Upewnij się, że przeczytałeś i zrozumiałeś stronę [Rozszerzenie modułu MES](Extend_FEM_Module/pl.md) przed przejściem do tego poradnika.

Zadanie można podzielić na pięć części:

-   **Nowy typ równania**. Ten krok musi być wykonany tylko jeśli równanie nie istnieje jeszcze we FreeCAD (w przeciwieństwie do równania, które jest już we FreeCAD, ale nie jest wspierane przez docelowy solver).
-   **Nowy obiekt równania**. Dodawanie konkretnego obiektu dokumentu reprezentującego konkretne równanie solvera Elmer.
-   **Rozszerz obiekt solvera**. Dodawanie wsparcia dla nowego równania do obiektu solvera Elmer.
-   **Rozszerz obiekt zapisujący równania**. Rozszerzenie eksportu do solvera Elmer o wsparcie dla nowego typu równania.
-   **Narzędzie w GUI do tworzenia równania**. Dostęp do funkcji nowego równania z poziomu GUI środowiska pracy MES.



## Nowy typ równania 

W tym kroku zmodyfikujemy następujący plik:

-    **src/Mod/Fem/femsolver/equationbase.py**
    

Typ równania jest dzielony przez wszystkie obiekty równań różnych solverów. Każdy typ ma ciąg określający (np. \"Heat\" - ciepło) i dedykowane polecenie dodające równanie do wybranego solvera. To upraszcza GUI, ponieważ mamy tylko jeden przycisk dla równania ciepła, z którego korzystają wszystkie wspierane solvery.

Najpierw dodaj nowe równanie do modułu {{Incode|equationbase.py}}. Każde równanie wymaga dwóch klas. Proxy dokumentu i proxy widoku. Te dwie klasy będą później używane jako klasy bazowe dla konkretnych klas równania Elmer. Po prostu skopiuj i wklej je z istniejącego typu równania i dostosuj ścieżkę ikony w {{Incode|getIcon(self)}} proxy widoku.


```python
class FlowProxy(BaseProxy):
    pass

class FlowViewProxy(BaseViewProxy):
    def getIcon(self):
        return ":/icons/FEM_EquationFlow.svg"
```



## Nowy obiekt równania solvera Elmer 

W tym kroku zaimplementujemy obiekt dokumentu. Musimy dodać nowy plik {{Incode|flow.py}} w:

-    **src/Mod/Fem/femsolver/elmer/equations/flow.py**
    

i zmodyfikować następujące pliki:

-    **src/Mod/Fem/ObjectsFem.py**
    

-    **src/Mod/Fem/CMakeLists.txt**
    

Zacznijmy od dodania nowego pliku {{Incode|flow.py}}. Ten plik można skopiować z istniejącego równania.



### Słowa kluczowe 

-   Jeśli nowe równanie wspiera tylko słowa kluczowe dla układów liniowych (**linear**) to skopiuj moduł {{Incode|femsolver/elmer/equations/elasticity.py}}.
-   Jeśli nowe równanie wspiera słowa kluczowe dla układów liniowych (**linear**) i nieliniowych (**non-linear**) to skopiuj {{Incode|femsolver/elmer/equations/heat.py}}.

Równanie przepływu w Elmer jest potencjalnie nieliniowym równanie. Oznacza to, że oprzemy naszą pracę na {{Incode|heat.py}}.



### Edycja plików 

Po skopiowaniu {{Incode|heat.py}} do {{Incode|flow.py}}, dostosuj {{Incode|flow.py}} w tych lokalizacjach:

-   argument name (nazwa) funkcji modułu {{Incode|create}},
-   klasy bazowe klasy {{Incode|Proxy}},
-   cechę {{Incode|Type}} klasy {{Incode|Proxy}},
-   klasy {{Incode|ViewProxy}}.


```python
def create(doc, name="'''Flow'''"):
    return femutils.createObject(
        doc, name, Proxy, ViewProxy)

class Proxy(nonlinear.Proxy, equationbase.'''Flow'''Proxy):

    Type = "Fem::EquationElmer'''Flow'''"

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.Priority = 10

class ViewProxy(nonlinear.ViewProxy, equationbase.'''Flow'''ViewProxy):
    pass
```

Następnie musisz zmienić właściwości dodane przez funkcję {{Incode|obj.addProperty(..)}} na te wymagane przez równanie.

W momencie pisania tego poradnika równanie przepływu solvera Elmer nie miało żadnych specjalnych właściwości. Zobacz równanie elastyczności solvera Elmer jeśli potrzebujesz przykładu z właściwościami.

Wreszcie, należy zarejestrować definicję **makeEquationFlow** w {{Incode|src/Mod/Fem/ObjectsFem.py}} poprzez zduplikowanie dostępnego wpisu.

FreeCAD korzysta z **make** do budowania programu. Więc musimy zarejestrować plik nowego modułu ({{Incode|flow.py}}) w {{Incode|src/Mod/Fem/CMakeLists.txt}} w sposób opisany na stronie [Rozszerzenie modułu MES](https://www.freecadweb.org/wiki/Extend_FEM_Module/pl). Odpowiednie listy można łatwo znaleźć szukając plików modułów istniejących równań solvera Elmer.



## Rozszerz obiekt solvera 

W tym kroku zmodyfikujemy następujący plik:

-    **src/Mod/Fem/femsolver/elmer/solver.py**
    

Teraz sprawiliśmy, że FreeCAD rozpoznaje nowy typ równania a nawet dodaliśmy polecenie, które wstawia to równanie do obiektu wybranego solvera. Zaimplementowaliśmy też konkretny obiekt równania dla solvera Elmer. Pozostało utworzenie połączenia między solverem Elmer i równaniem przepływu. Należy to zrobić bezpośrednio w obiekcie solvera Elmer.

Zarejestruj moduł, w którym właśnie zaimplementowaliśmy obiekt naszego nowego równania ({{Incode|flow.py}}) z określnikiem równania z kroku 1 (\"Flow\") na liście {{Incode|_EQUATIONS}} w {{Incode|elmer/solver.py}}.


```python
from .equations import electrostatic
+from .equations import flow

...

_EQUATIONS = {
    "Heat": heat,
    "Elasticity": elasticity,
+    "Flow": flow,
}
```



## Rozszerz obiekt zapisujący równania 

W tym kroku zmodyfikujemy następujący plik:

-    **src/Mod/Fem/femsolver/elmer/writer.py**
    

Ten plik zawiera klasę {{Incode|Writer}}, która eksportuje analizę do formatu SIF solvera Elmer.

Dla każdego wspieranego równania są dwie główne metody eksportu. Po prostu skopiuj je wszystkie z istniejącego równania i dostosuj je do swoich potrzeb.

-    {{Incode|_getFlowSolver}}
    

-    {{Incode|_handleFlow}}
    

Musisz zarejestrować metodę {{Incode|_handleFlow}} w klasie {{Incode|Writer}}:


```python
class Writer(object):
...
    def write(self):
...
        self._handleFlow()

...

```


{{Incode|_handleFlow}}

może kontrolować serię innych złożonych metod. Nasze równanie przepływu korzysta z następujących złożonych metod:

-    {{Incode|_handleFlowConstants}}
    

-    {{Incode|_handleFlowMaterial}}
    

-    {{Incode|_handleFlowInitialVelocity}}
    

-    {{Incode|_handleFlowBndConditions}}
    

-    {{Incode|_handleFlowEquation}}
    

Zakończyliśmy teraz część funkcji nowego równania. Następnie połączymy nowe równanie poprzez GUI.



## Narzędzie w GUI do tworzenia równania 

Właśnie utworzyliśmy klasę nowego równania. Aby mieć do niej dostęp z GUI środowiska pracy MES, musimy utworzyć przycisk i podłączyć go do klasy nowego równania. Tu znajduje się poradnik: [Poradnik: Dodaj przycisk do paska narzędzi MES](Add_Button_to_FEM_Toolbar_Tutorial/pl.md).



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add FEM Equation Tutorial/pl
