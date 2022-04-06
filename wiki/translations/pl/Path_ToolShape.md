# Path ToolShape/pl
}





{{TOCright}}

## Opis

Profile narzędziowe są podstawową częścią systemu [narzędzi](Path_Tools/pl.md). Profile narzędzi są szablonami, na podstawie których tworzone są końcówki narzędzi *(ToolBits)*. Reprezentują one konkretny fizyczny kształt narzędzia. Kształt *(ToolShape)* nie opisuje w pełni końcówki - do tego potrzebne są dodatkowe parametry, które zostaną dodane, gdy rzeczywista końcówka zostanie określona parametrami na podstawie szablonu.

Początkowo Profile narzędzi są po prostu dokumentami FreeCAD z jednym korpusem utworzonym w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Tworzenie nowych profili narzędzi jest tematem zaawansowanym. Najczęściej potrzebne kształty już istnieją i są dostarczane wraz z instalacją programu FreeCAD:

-   W systemie Linux jest to zazwyczaj folder `/usr/lib64/FreeCAD/Mod/Path/Tools/Shape`.
-   W systemie Windows jest to zazwyczaj folder `C:\Program Files\FreeCAD\Mod\Path\Tools\Shape`.
-   Na macOS jest to zazwyczaj folder `/Applications/FreeCAD/Mod/Path/Tools/Shape`. {{ColoredText||Red|--> musi zostać poprawione}}

Są to:

:   
    {{FileName|ballend.fcstd}}
    

:   
    {{FileName|bullnose.fcstd}}
    

:   
    {{FileName|chamfer.fcstd}}
    

:   
    {{FileName|drill.fcstd}}
    

:   
    {{FileName|endmill.fcstd}}: {{FileName|endmill.fcstd}}

:   
    {{FileName|probe.fcstd}}
    

:   
    {{FileName|slittingsaw.fcstd}}
    

:   
    {{FileName|thread-mill.fcstd}}: {{FileName|thread-mill.fcstd}}

:   
    {{FileName|v-bit.fcstd}}
    

Można je znaleźć w podkatalogu {{FileName|/Mod/Path/Tools/Shape/}}, w którym został zainstalowany program FreeCAD.

## Użycie

1.  Utwórz nowy dokument FreeCAD.
2.  Otwórz środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Część](PartDesign_Workbench/pl.md).
3.  Utwórz zawartość i nadaj jej nazwę, która będzie wyświetlana przy wyborze końcówki.
4.  Utwórz szkic w płaszczyźnie XZ i narysuj połowę profilu końcówki narzędzia.
    -   Umieść górę środka końcówki w punkcie położenia odniesienia `(0,0)`.
5.  Dla każdego wiązania służącego jako parametr narzędzia *(np. długość całkowita)* utwórz wiązanie oznaczone nazwą.
    -   Nazwa będzie etykietą pola wprowadzania danych.
    -   Nazwy są dzielone na słowa w oknie dialogowym edycji na granicy CamelCase.
    -   Użyj `;` w nazwie, aby dodać komentarz, który będzie wyświetlany jako wskazówka pola wprowadzania danych.
    -   Jeśli narzędzie jest używane przez starsze operacje, to powinno mieć przynajmniej jedno wiązanie o nazwie Średnica *(Diameter)*.
    -   Do wiązań, które nie są bezpośrednio dostępne, takich jak Średnica i Kąt, należy używać linii konstrukcyjnych.
    -   Każde wiązanie bez nadanej nazwy nie będzie edytowalne dla danego narzędzia.
6.  Gdy szkic zostanie w pełni związany, zamknij go.
7.  Wykonaj wyciągnięcie szkicu przez obrót wokół osi z.
8.  Zapisz dokument jako nowy plik w katalogu `Shape`.

## Miniaturki narzędzi 

Końcówki narzędzi będą miały małą ikonę narzędzia w drzewie, jeśli obraz zostanie zapisany z aktywnymi miniaturami.

Ważne uwagi:

-   Przed zapisaniem dokumentu upewnij się, że w preferencjach programu FreeCAD zaznaczona jest opcja Zapisz miniaturę, a opcja Dodaj logo programu jest nieaktywna.
-   Upewnij się także, że przełączasz się na Widok z przodu i Dopasuj element do ekranu
-   Cokolwiek zobaczysz podczas zapisywania dokumentu, będzie to wizualna reprezentacja szablonu.

## Opcje





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolShape/pl
