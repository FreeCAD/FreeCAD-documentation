---
 GuiCommand:
   Name: SheetMetal AddFoldWall
   Name/pl: Arkusz Blachy: Składanie ścianek
   MenuLocation: SheetMetal , Składanie ścianek
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **C** **F**
---

# SheetMetal AddFoldWall/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> **Składanie ścianek** składa blachę *(pustą)* na wybranej linii.

Może być używany z wstępnie wyciętym półfabrykatem do

-   utworzenia perforowanej strefy gięcia
-   pozostawienia płaskich sekcji w obszarze gięcia i poza nim, np. zakładek. *(wymaga przerw w linii gięcia)*.

<img alt="" src=images/SheetMetal_AddFoldWall-13.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*Wstępnie wycięty półfabrykat i linia gięcia z dwiema szczelinami → perforowana strefa gięcia o wciąż płaskiej geometrii.*



## Użycie

1.  Wybierz ścianę, która ma zostać wygięta.
2.  Przytrzymaj klawisz **Ctrl** *(lub **Command** na macOS)*.
3.  Wybierz współpłaszczyznowy <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">. [szkic](Sketcher_Workbench/pl.md) *(tj. leżący na tej samej płaszczyźnie)* zawierający **linię *(segmenty)* zgięcia** (najlepiej z [Widoku drzewa](Tree_view/pl.md)).
4.  Puść klawisz **Ctrl** (lub **Command**).
5.  To polecenie można aktywować na kilka sposobów:
    -   Wciśnij przycisk **<img src="images/SheetMetal_AddFoldWall.svg" width=16px> [Składanie ścianek](SheetMetal_AddFoldWall/pl.md)**.
    -   Wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddFoldWall.svg" width=16px> Składanie ścianek** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **Sheet Metal → <img src="images/SheetMetal_AddFoldWall.svg" width=16px> Składanie ścianek** z menu kontekstowego.
    -   Użyj skrótu klawiszowego: **C** a następnie **F**.
6.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Generate Sheet Metal base shape** (wprowadzony w wersji 0.5.00).
7.  Opcjonalnie wciśnij przycisk **Base Object** i wybierz inną ścianę.
8.  Opcjonalnie wciśnij przycisk **Bend Line** i wybierz inny szkic.
9.  Opcjonalnie dostosuj parametry w panelu zadań.
10. Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
11. Utworzony zostanie obiekt **Fold**.
12. Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).

<img alt="" src=images/SheetMetal_AddFoldWall-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*Linia zgięcia ''(linie zgięcia)'' leżąca w środku perforacji → aby zgięcie było wyśrodkowane w ten sam sposób, właściwość **Pozycja* musi być ustawiona na {{value|środek**.}}



## Uwagi

-   Szkic linii zgięcia musi być **współpłaszczyznowy** do wybranej ściany.

-   Segmenty linii zgięcia muszą być **współliniowe** względem siebie.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Składania ścianki środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Parametry}}

-    **Linia gięcia|Link**: *Lista linii referencyjnych zgięć*. Łącza do obiektów linii zagięcia.

-    **Pozycja|Enumeration**: *Pozycja linii gięcia*.

    :   
        {{value|Przecięcie płaszczyzn}}
        
        *(wprowadzone w wersji 0.4.12)*,


{{value|w przód}}

*(domyślnie)*, {{value|środek}}, {{value|wstecz}}.

-    **Kąt|Angle**: *Kąt zgięcia*. Domyślna wartość kąta: {{value|90,00°}}.

-    **Obiekt bazowy|LinkSub**: *Obiekt bazowy*. Łącze do płaskiej powierzchni, która ma zostać wygięta.

-    **Odwróć|Bool**: *Odwróć kierunek zgięcia*. Wartość domyślna: {{FALSE/pl}}.

-    **OderóćZgięcie|Bool**: *Odwróć kierunek zgięcia bryły*. Wartość domyślna: {{FALSE/pl}}.

    :   Wartość {{TRUE/pl}} zamienia stronę linii, która ma zostać wygięta.

-    **WspółczynnikK|FloatConstraint**: *Pozycja osi neutralnej*. Wartość domyślna: {{value|0,50}}.

-    **Promień|Length**: *Promień zgięcia*. Wartość domyślna: {{value|1,00 mm}}.

-    **Rozwiń|Bool**: *Rozwiń zagięcie*. Wartość domyślna: {{FALSE/pl}}.



## Przykład

<img alt="" src=images/SheetMetal_AddFoldWall-01.png  style="width:300px;"> 
*Prosty klips*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">



### Przygotowania

Ten klips jest wykonany z półfabrykatu, który otrzymuje trzy zagięcia, więc potrzebujemy czterech szkiców przygotowanych wcześniej:

:   \- jeden dla obrysu plus szczelina *(półfabrykat)*,
:   \- jeden dla zagięcia na końcu,
:   \- jeden dla zagięcia w górę ,
:   \- jeden dla zagięcia w dół.

Najprostszym sposobem zagwarantowania, że jedna powierzchnia półfabrykatu i wszystkie linie zagięcia są współpłaszczyznowe, jest utworzenie wszystkich szkiców na tej samej płaszczyźnie - w tym przypadku **Płaszczyzna_XY**.

Linie zagięcia można stworzyć za pomocą innych narzędzi, ale hej, mamy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench.md)!

<img alt="" src=images/SheetMetal_AddFoldWall-21.png  style="width:280px;"> <img alt="" src=images/SheetMetal_AddFoldWall-20.png  style="width:200px;"> 
*Szkice na wspólnej płaszczyźnie i ich reprezentacja w drzewie projektu.*



### Przepływ pracy 

1.  Utwórz półfabrykat
    1.  Wybierz szkic konturu
    2.  Naciśnij przycisk **<img src="images/SheetMetal_AddBase.svg" width=16px>'''Wykonaj składanie ścianek'''
**

 lub użyj skrótu klawiaturowego:  <img alt="" src=images/SheetMetal_AddFoldWall-02.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-03.png  style="width:280px;"> 

1.  Złóż końcówkę
    1.  Wybierz **dolną powierzchnię** półfabrykatu
    2.  Wybierz **szkic** o nazwie ***Tip Fold line*** *(najlepiej z widoku drzewa)*  *(i nie zapomnij o klawiszu **Ctr** / **Command**)*
    3.  Naciśnij przycisk  lub użyj skrótu klawiaturowego: <img alt="" src=images/SheetMetal_AddFoldWall-10.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-04.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-05.png  style="width:280px;">
    4.  Zagięcie powinno być skierowane w dół pod kątem 90°, dlatego należy ustawić niektóre wartości w oknie właściwości, np.:  - wartość **kąta** na 60°  - **odwróć** na {{true/pl}} dla zagięcia w górę

 

1.  Utwórz zagięcie w dół
    1.  Wybierz **dolną powierzchnię** półfabrykatu.
    2.  Następnie *szkic* o nazwie ***Down-Fold line***.
    3.  Naciśnij przycisk  lub użyj skrótu klawiaturowego: <img alt="" src=images/SheetMetal_AddFoldWall-11.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-06.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-07.png  style="width:280px;">
    4.  Ustaw wartość **kąta** na {{Value|92°}}.
    5.  Jeśli przesunęła się niewłaściwa sekcja części, ustaw wartość **OdwróćGięcie** na  
2.  Aby utworzyć zagięcie w górę:
    1.  Wybierz **dolną powierzchnię** półfabrykatu.
    2.  I następnie **szkic** o nazwie ***Up-Fold line***
    3.  Naciśnij przycisk  lub użyj skrótu klawiaturowego: <img alt="" src=images/SheetMetal_AddFoldWall-12.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-08.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-09.png  style="width:280px;">
    4.  Ustaw wartość **kąta** na {{Value|80°}}.
    5.  Jeśli zagięcie zostało wykonane w dół, ustaw wartość *Odwróć* na {{true/pl}}
    6.  Jeśli to konieczne, ustaw wartość **OdwróćGięcie** na true  

Gotowe!

Uwaga!: W rzeczywistości zagięcie w górę musi być wykonane przed zagięciem w dół. Jedynie wirtualny świat CAD pozwala nam na zginanie przez stały materiał. Dzięki temu orientacja sekcji statycznej nie ulega zmianie.  Wszystkie szkice leżą na tej samej płaszczyźnie, aby uniknąć szkiców dołączonych do ruchomych powierzchni.


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddFoldWall/pl
