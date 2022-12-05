# Path ToolShape/pl
{{TOCright}}

## Opis

Profile narzędziowe są podstawową częścią systemu [narzędzi](Path_Tools/pl.md). Profile narzędzi są szablonami, na podstawie których tworzone są końcówki narzędzi *(ToolBits)*. Reprezentują one konkretny fizyczny kształt narzędzia. Kształt *(ToolShape)* nie opisuje w pełni końcówki - do tego potrzebne są dodatkowe parametry, które zostaną dodane, gdy rzeczywista końcówka zostanie określona parametrami na podstawie szablonu.

Początkowo Profile narzędzi są po prostu dokumentami FreeCAD z jednym korpusem utworzonym w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Tworzenie nowych profili narzędzi jest tematem zaawansowanym. Najczęściej potrzebne kształty już istnieją i są dostarczane wraz z instalacją programu FreeCAD:

-   W systemie Linux jest to zazwyczaj folder `/usr/lib64/FreeCAD/Mod/Path/Tools/Shape`.
-   Na macOS jest to zazwyczaj folder `/Applications/FreeCAD.app/Contents/Resources/Mod/Path/Tools/Shape`.
-   W systemie Windows jest to zazwyczaj folder `C:\Program Files\FreeCAD\Mod\Path\Tools\Shape`.

Są to:

:   
    **ballend.fcstd**
    

:   
    **bullnose.fcstd**
    

:   
    **chamfer.fcstd**
    

:   
    **drill.fcstd**
    

:   
    **endmill.fcstd**: **endmill.fcstd**

:   
    **probe.fcstd**
    

:   
    **slittingsaw.fcstd**
    

:   
    **thread-mill.fcstd**: **thread-mill.fcstd**

:   
    **v-bit.fcstd**
    

Można je znaleźć w podkatalogu **/Mod/Path/Tools/Shape/**, w którym został zainstalowany program FreeCAD.

## Użycie

1.  Utwórz nowy dokument FreeCAD.
2.  Otwórz środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Część](PartDesign_Workbench/pl.md).
3.  Utwórz zawartość i nadaj jej nazwę, która będzie wyświetlana przy wyborze końcówki.
4.  Utwórz szkic w płaszczyźnie XZ i narysuj połowę profilu końcówki narzędzia.
    -   Umieść górę środka końcówki w punkcie położenia odniesienia `(0,0)`. Będzie to środek osi, na której kod G będzie obracał końcówkę.
    -   Uwaga: W tym momencie nie należy dodawać żadnych więzów wymiarowych.
5.  Zamknij szkic.
6.  Wyciągnij szkic przez <img alt="" src=images/PartDesign_Revolution.svg  style="width:16px;"> [obrót](PartDesign_Revolution/pl.md) wokół pionowej osi szkicu.
7.  Otwórz środowisko pracy <img alt="" src=images/Workbench_Path.svg  style="width:16px;"> [Path](Path_Workbench/pl.md).
8.  Wybierz szkic w oknie [widoku drzewa](Tree_view/pl.md). Dzięki temu Koszyk właściwości narzędzia skrawającego utworzony w następnym kroku będzie zagnieżdżony w Zawartości.
9.  Wybierz z menu opcję **Ścieżka → Narzędzia → Koszyk własciwości narzędzia skrawającego**.
10. Zostanie utworzony Koszyk właściwości narzędzia skrawającego o nazwie {{Value|Atrybuty}}. Ten obiekt będzie używany do kontrolowania wymiarów w szkicu.
11. Kliknij dwukrotnie Koszyk właściwości narzędzia skrawającego w oknie [widoku drzewa](Tree_view/pl.md).
12. Zostanie otwarty panel zadań **Koszyk właściwości**.
13. Kliknij przycisk **Dodaj ...**.
14. Zostanie otwarte okno dialogowe **Utwórz właściwość**.
15. Utwórz właściwość o nazwie {{Value|Diameter}}. Ta właściwość jest obowiązkowa dla końcówek narzędzi. W nazwach właściwości rozróżniana jest wielkość liter i nie mogą one zawierać spacji.
16. Wybierz {{Value|Kształt}} z listy rozwijanej **Grupa**.
17. Wybierz odpowiednie polecenie **Typ**.
18. Opcjonalnie określ **Końcówkę narzędzia**.
19. Kliknij przycisk **OK**.
20. W panelu zadań **Koszyk właściwości** wprowadź wartość dla właściwości **Średnica**.
21. W podobny sposób dodaj wszystkie pozostałe wymagane właściwości.
22. Po zakończeniu kliknij przycisk **OK** w panelu zadań **Koszyk właściwości**.
23. Kliknij dwukrotnie szkic w oknie [Widoku drzewa](Tree_view.md).
24. Dodaj wiązania wymiarowe i zastosuj właściwości z utworzonego Koszyka właściwości. Na przykład, aby zastosować właściwość **Średnica**:
    1.  Kliknij dwukrotnie wymiar.
    2.  Kliknij ikonę <img alt="" src=images/Bound-expression.svg  style="width:16px;">.
    3.  Wpisz wartość {{Value|<<Attributes>>.Diameter}} w oknie **Edytora formuł**.
    4.  Kliknij dwukrotnie przycisk **OK**.
25. Powtarzaj tę czynność, aż szkic zostanie w pełni związany.
26. Zapisz plik **FCStd** w miejscu, w którym FreeCAD spodziewa się znaleźć pliki Końcówek narzędzi. Zobacz [opis](#Opis.md) powyżej.

-   Uwaga 1. Jeśli w systemie Windows odmówiono Ci dostępu do folderu, uruchom program FreeCAD w trybie ADMINISTRATOR.
-   Uwaga 2. Zawartość Zestawu narzędzi musi być pierwszym obiektem w oknie [widoku drzewa](Tree_view/pl.md). Te instrukcje zapewniają, że tak właśnie jest.

## Miniaturki narzędzi 

Końcówki narzędzi będą miały małą ikonę narzędzia w oknie [widoku drzewa](Tree_view/pl.md), jeśli obraz zostanie zapisany z aktywnymi miniaturami.

Ważne uwagi:

-   Przed zapisaniem dokumentu upewnij się, że w preferencjach programu FreeCAD zaznaczona jest opcja Zapisz miniaturę, a opcja Dodaj logo programu jest nieaktywna.
-   Upewnij się także, że przełączasz się na Widok z przodu i Dopasuj element do ekranu
-   Cokolwiek zobaczysz podczas zapisywania dokumentu, będzie to wizualna reprezentacja szablonu.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolShape/pl
