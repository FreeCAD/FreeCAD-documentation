# Scenegraph/pl
## Wprowadzenie

Geometria, która pojawia się w oknie [widoku 3D](3D_view/pl.md) programu FreeCAD jest renderowana przez bibliotekę [Coin3D](https://en.wikipedia.org/wiki/Coin3D). Coin3D jest implementacją standardu [Open Inventor](https://en.wikipedia.org/wiki/Open_Inventor). Oprogramowanie [OpenCASCADE](https://en.wikipedia.org/wiki/Open_Cascade_Technology) również zapewnia tę samą funkcjonalność, ale na bardzo wczesnym etapie rozwoju programu FreeCAD zdecydowano, aby nie używać wbudowanej przeglądarki OpenCASCADE, lecz przejść na bardziej wydajne oprogramowanie Coin3D. Dobrym sposobem na zapoznanie się z tą biblioteką jest książka [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).

## Opis

[Open Inventor](https://en.wikipedia.org/wiki/Open_Inventor) to język opisu sceny 3D. Scena opisana w Open Inventor jest następnie renderowana w OpenGL na ekranie użytkownika. Coin3D zajmuje się tym, więc programiści nie muszą zajmować się skomplikowanymi wywołaniami OpenGL, a mogą jedynie dostarczyć poprawny kod Open Inventora. Dużą zaletą jest to, że Open Inventor jest bardzo dobrze znanym i dobrze udokumentowanym standardem.

Jednym z najważniejszych zadań, które FreeCAD wykonuje za Ciebie, jest tłumaczenie informacji o geometrii OpenCASCADE na język Open Inventor.

Open Inventor opisuje scenę 3D w postaci [scenogramu](https://en.wikipedia.org/wiki/Scene_graph), takiego jak poniżej:

![](images/Scenegraph.gif ) 
*Grafika pobrana z [https://web.archive.org/web/20190807185912/http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/ Inventor mentor]*

Sceneria open Inventor opisuje wszystko, co jest częścią sceny 3D, np. geometrię, kolory, materiały, światła itp., i organizuje wszystkie te dane w wygodną i przejrzystą strukturę. Wszystko może być pogrupowane w podstruktury, co pozwala organizować zawartość sceny w dowolny sposób. Oto przykład pliku programu Open Inventor:


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}

Jak widać, struktura jest bardzo prosta. Separatory służą do organizowania danych w bloki, podobnie jak pliki w folderach. Na przykład pierwsze dwa elementy naszego głównego separatora to rotacja i przesunięcie, które wpływają na następny element, będący separatorem. W separatorze definiuje się materiał i kolejną transformację. Na nasz walec będą więc miały wpływ obie transformacje - ta zastosowana bezpośrednio do niego oraz ta, która została zastosowana do jego nadrzędnego separatora.

Do dyspozycji mamy także wiele innych typów elementów organizujących naszą scenę, takich jak grupy, przełączniki czy adnotacje. Możemy definiować bardzo złożone materiały dla naszych obiektów, w tym kolory, tekstury, tryby cieniowania i przezroczystość. Można także definiować światła, kamery, a nawet ruch. W plikach programu Open Inventor można nawet osadzać fragmenty skryptów w celu zdefiniowania bardziej złożonych zachowań.

Jeśli chcesz dowiedzieć się więcej o Open Inventor, przejdź bezpośrednio do jego najbardziej znanego źródła: [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/).

W programie FreeCAD nie ma potrzeby bezpośredniej interakcji ze scenografią Open Inventor. Każdy obiekt w dokumencie FreeCAD, będący siatką, kształtem części lub czymkolwiek innym, jest automatycznie konwertowany do kodu Open Inventor i wstawiany do głównego scenogramu, który jest widoczny w oknie [widoku 3D](3D_view/pl.md). Ten schemat scenograficzny jest stale aktualizowany, gdy modyfikujesz, dodajesz lub usuwasz obiekty. W rzeczywistości każdy obiekt *(w przestrzeni aplikacji)* ma dostawcę widoku *(odpowiadający mu obiekt w przestrzeni GUI)* odpowiedzialnego za wydawanie kodu Open Inventora.

Jednak możliwość bezpośredniego dostępu do scenogramu ma wiele zalet. Na przykład możemy tymczasowo zmienić wygląd obiektu lub dodać do sceny obiekty, które nie mają rzeczywistego odpowiednika w dokumencie FreeCAD, takie jak geometria konstrukcyjna, elementy pomocnicze, graficzne podpowiedzi lub narzędzia, takie jak manipulatory lub informacje wyświetlane na ekranie.

Sam program FreeCAD posiada kilka narzędzi do przeglądania i modyfikowania kodu Open Inventor. Na przykład poniższy kod Pythona wyświetli reprezentację Open Inventor dla wybranego obiektu:


```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```

Ale mamy też moduł środowiska Python, który umożliwia pełny dostęp do wszystkiego, co jest zarządzane przez Coin3D, np. do scenogramu FreeCAD. Tak więc, zapoznaj się z [Pivy](Pivy/pl.md).

## Przykłady kodu 

Zobacz stronę [wycinki Coin3d](Coin3d_snippets/pl.md) dzięki uprzejmości MariwanJ w ramach badań dla środowiska pracy [Design456](Design456_Workbench.md). Repozytorium kodu można znaleźć pod adresem <https://github.com/MariwanJ/COIN3D_Snippet>. {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Scenegraph/pl
