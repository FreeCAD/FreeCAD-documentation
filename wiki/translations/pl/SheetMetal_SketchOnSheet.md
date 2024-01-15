---
 GuiCommand:
   Name: SheetMetal SketchOnSheet
   Name/pl: Arkusz Blachy: Szkic na arkuszu blachy
   MenuLocation: SheetMetal , Szkic na arkuszu blachy
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **M** **S**
---

# SheetMetal SketchOnSheet/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Szkic na arkuszu blachy](SheetMetal_SketchOnSheet/pl.md) wycina otwory wzdłuż zagiętych ścian obiektu z blachy. Do rozmieszczenia otworów wykorzystuje się <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [szkic](Sketcher_Workbench/pl.md).

W przeciwieństwie do polecenia <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Kieszeń](PartDesign_Pocket/pl.md) środowiska pracy Projekt Części, gdzie otwory są po prostu wycinane wzdłuż normalnej szkicu *(lokalnej osi Z)*, to narzędzie działa tak, jakby rozkładało obiekt z blachy, wycinało otwory i ponownie składało obiekt.



## Użycie

1.  Wybierz **płaską powierzchnię**.
2.  Utwórz współpłaszczyznowy <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [szkic](Sketcher_Workbench/pl.md) *(tj. leżący na tej samej płaszczyźnie)* dla **układu otworów** *(najlepiej w [Widoku drzewa](Tree_view/pl.md))*.
    -   *Uwaga:*\' Nie zapomnij o klawiszu **Control**/**Command**!
3.  Aktywuj polecenie <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> Szkic na arkuszu blachy używając:
    -   Przycisku **<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> '''Szkic na arkuszu blachy'''**.
    -   Polecenia z menu **SheetMetal → <img src="images/SheetMetal_SketchOnSheet.svg" width=16px> Szkic na arkuszu blachy**.
    -   Skrótu klawiaturowego: **M** następnie **S**



## Uwagi

-   Szkic może zawierać więcej niż jeden kontur.
-   Każdy kontur musi przynajmniej dotykać powierzchni planarnej, w przeciwnym razie nie zostanie wycięty żaden otwór.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Szkic na arkuszu blachy** wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|SketchOnSheet}} *(+ kolejny numer dla drugiej i następnych pozycji)*. Edytowalna przez użytkownika nazwa tego obiektu, może to być dowolny ciąg znaków UTF8.

-    **Cecha podstawowa|Link|ukryte**: Cecha bazowa. Link do cechy nadrzędnej.

-    **_Body|LinkHidden|ukryte**: Link ukryty do zawartości nadrzędnej.


{{Properties_Title|Parametry}}

-    **Szkic|Link**: \"Szkic na blasze\". Łącze do układu otworów/szkicu wycięcia.

-    **Obiekt bazowy|LinkSub**: \"Obiekt bazowy\". Łącze do płaskiej powierzchni, od której rozpoczyna się wycięcie.

-    **Współczynnik K|FloatConstraint**: \"Szczelina z lewej strony\". Wartość domyślna: {{value|0,50}}.



## Przykład

<img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:300px;"> 
*Prosta rzecz do zrobienia*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Przygotowanie

Ten przedmiot jest wykonany ze złożonej blachy z dodanymi otworami.
Dlatego należy wcześniej przygotować jeden otwarty szkic konturu blachy i jeden szkic układu otworów.
Pierwsza linia prosta pierwszego szkicu musi być współpłaszczyznowa względem drugiej płaszczyzny szkicu, co spowoduje, że szkic i powierzchnia będą współpłaszczyznowe w następnych krokach.

<img alt="" src=images/SheetMetal_SketchOnSheet-01.png  style="width:200px;"> 
*Tylko kontur i układ otworów*



### Przepływ pracy 

1.  Utwórz zagięty obiekt z blachy
    1.  Wybierz szkic **konturu**  <img alt="" src=images/SheetMetal_SketchOnSheet-02.png  style="width:240px;">.
    2.  Naciśnij przycisk **<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)** button
        lub użyj skrutu:  <img alt="" src=images/SheetMetal_SketchOnSheet-03.png  style="width:240px;">
2.  Wytnij kilka otworów
    1.  Wybierz **płaską powierzchnię**
    2.  Wybierz szkic układu otworów
        <img alt="" src=images/SheetMetal_SketchOnSheet-04.png  style="width:240px;">
    3.  Naciśnij przycisk **<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Sketch On Sheet metal](SheetMetal_SketchOnSheet.md)** button
        lub użyj skrutu: **M** + **S**
        <img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:240px;">
        Done!  
3.  Kilka wskazówek
    1.  Sprawdź, czy grubość zagiętego obiektu jest budowana po prawej stronie.
        <img alt="" src=images/SheetMetal_SketchOnSheet-06.png  style="width:240px;">
        Żółty kontur powinien leżeć na górnej powierzchni dolnego zagięcia *(jak pokazano)*.
        Aby odwrócić kierunek, ustaw wartość właściwości **Strona gięcia** *(Zewnętrzna \<-\> Wewnętrzna)*.
    2.  **Kształty otworów** nie dotykające używanej płaskiej powierzchni nie będą wycinać otworów w złożonym obiekcie.
        <img alt="" src=images/SheetMetal_SketchOnSheet-07.png  style="width:240px;">
        Dolny prostokąt, który prawie nie dotyka wspomnianej powierzchni, wycina otwór, podczas gdy górny kształt szczeliny nie.


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal SketchOnSheet/pl
