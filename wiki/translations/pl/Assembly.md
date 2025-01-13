# Assembly/pl
## Wprowadzenie




W FreeCAD słowo **Złożenie** jest zwykle używane w odniesieniu do modelu [3D](Model/pl.md), który składa się z kilku rozróżnialnych części, które są połączone ze sobą w jakiś sposób, aby stworzyć funkcjonalny obiekt, tak jak powstają prawdziwe produkty.

Na przykład śruba, podkładka i nakrętka to trzy oddzielne elementy, które po połączeniu tworzą złożenie.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">



*Z lewej: trzy pojedyncze przylegające bryły, każda z nich modelowana przez [Zawartość](PartDesign_Body/pl.md) środowiska Projekt Części. Z prawej: poszczególne bryły zestawione razem w [Część](Std_Part/pl.md), aby stworzyć złożenie.*



## Użycie



### Montaż manualny 

Ogólnie rzecz biorąc, nie potrzebujesz specjalnych narzędzi do tworzenia złożeń, wystarczy, że będziesz miał wiele różnych [Zawartości](Body/pl.md) poukładanych w określony sposób.

Aby ustawić ciała tam, gdzie chcesz, możesz

-   użyć narzędzia [Przemieszczenie](Std_TransformManip/pl.md),
-   użyć narzędzia <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Umiejscowienie](Std_Placement/pl.md) okna dialogowego, lub.
-   zmodyfikować właściwość [Umiejscowienie](Placement/pl.md) bezpośrednio w [edytorze właściwości](Property_editor/pl.md).

Możesz użyć jednego z pseudo-montaży [środowisk zewnętrznych](External_workbenches/pl.md), takich jak Lattice2, Manipulator, Part-o-magic lub WorkFeature, aby pomóc Ci znaleźć przecięcia, zmierzyć odległości i rozmieścić obiekty w pożądany sposób.

Ogólnie rzecz biorąc, obiekt **[<img src=images/Std_Part.svg style="width:16px"> [Część](Std_Part/pl.md)** został zaprojektowany tak, aby służył jako podstawowy budulec do tworzenia złożeń. Obiekt ten służy do grupowania kilku [Zawartości](Body/pl.md) i przenoszenia ich razem jako jednostki, czyli jako podzespołu. Następnie ten podzespół może być umieszczony obok lub użyty wewnątrz innych podzespołów, aby stworzyć ostateczne złożenie.



### Złożenie z więzami 

Można też użyć wbudowanego [środowiska pracy Złożenie](Assembly_Workbench/pl.md) lub jego zewnętrznych odpowiedników, jak <img alt="" src=images/A2p_workbench.svg  style="width:24px;"> [A2plus](A2plus_Workbench/pl.md), <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Złożenie 3](Assembly3_Workbench/pl.md), czy <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Złożenie 4](Assembly4_Workbench/pl.md). Należy pamiętać, że [Złożenie 2](Assembly2_Workbench/pl.md) nie jest utrzymywany, więc nie jest zalecany dla nowych modeli.

Środowiska pracy złożeń wykorzystują wiązania i wyrażenia do tworzenia relacji między obiektami w modelu, aby matematycznie powiązać obiekty w miejscu, na przykład: \"ta ściana powinna przylegać do tej drugiej ściany\", \"ten walec powinien być współśrodkowy z tym okręgiem\", \"ten punkt powinien podążać za tą krawędzią\" itp.

Jest to zaawansowane wykorzystanie oprogramowania, które jest zwykle używane w złożonych systemach mechanicznych. Jeśli twój [model](Model/pl.md) nie jest bardzo skomplikowany, to użycie środowiska do złożeń może nie być konieczne.



## Uwagi

-   Od wersji FreeCAD 1.0, dostępne jest oficjalne [środowisko pracy Złożenie](Assembly_Workbench/pl.md) uwzględnione w domyślnej instalacji.

-   Zauważ, że środowiska złożeń są z reguły niekompatybilne między sobą. Jeśli stworzysz złożenie w jednym z nich, powinieneś trzymać się oryginalnego środowiska i nie używać innego w tym samym dokumencie.


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Assembly/pl
