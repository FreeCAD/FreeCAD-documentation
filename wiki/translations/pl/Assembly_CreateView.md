---
 GuiCommand:
   Name: Assembly CreateView
   Name/pl: Złożenie Utwórz widok rozłożenia
   MenuLocation: Złożenie , Utwórz widok rozłożenia
   Workbenches: Assembly_Workbench/pl
   Shortcut: **V**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateView/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateView.svg  style="width:24px;"> [Utwórz widok rozłożenia](Assembly_CreateView/pl.md) tworzy kontener widoku rozłożonego (obiekt Exploded_Views) w aktywnym złożeniu, zawierający jeden (domyślnie) lub więcej widoków rozłożonych (obiekty Exploded_View). Złożenie może mieć tylko jeden kontener widoków rozłożonych.

Widok rozłożony zbiera ruchy (obiekty Move) używane do przemieszczenia części ze złożonych pozycji do rozłożonych pozycji. Zmienione pozycje złożonych części i reprezentacje ruchów są widoczne tylko gdy widok rozłożony jest edytowany i w widokach środowiska Rysunek Techniczny utworzonych z widoku rozłożonego.



## Użycie

1.  Upewnij się, że złożenie jest aktywne.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateView.svg" width=16px> [Utwórz widok rozłożenia](Assembly_CreateView/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateView.svg" width=16px> Utwórz widok rozłożenia** z menu.
    -   Użyj skrótu: **E**.
3.  Jeśli nie ma wcześniej utworzonych obiektów Exploded_Views: kontener Exploded_Views zostanie dodany do aktywnego złożenia.
4.  Obiekt Exploded_View zostanie dodany do kontenera Exploded_Views.
5.  Okno dialogowe **Utwórz widok rozłożenia** zostanie otwarte w [panelu zadań](Task_panel/pl.md).
6.  Opcjonalnie zaznacz opcję **Części jako pojedyncza bryła** aby\...
7.  Opcjonalnie wybierz jeden sposób dodania przemieszczenia:
    -   Rozłóż promieniowo:
        1.  Wciśnij przycisk **Rozłóż promieniowo**
        2.  Wszystkie części zostaną wybrane i pojawi się manipulator (zobacz [Uwagi](#Notes/pl.md)).
        3.  Opcjonalnie przesuń manipulator wybierając jedną z opcji z listy rozwijanej **Wyrównanie przeciągania do\...**.
            -   Wyrównanie przeciągania do\...
                1.  Wybierz krawędź lub ścianę dowolnej części aby wyrównać manipulator.
            -   Wyrównaj do środka części.
                1.  Manipulator zostanie wyrównany do środka zakotwionej części.
            -   Wyrównaj do początku układu współrzędnych części.
                1.  Manipulator zostanie wyrównany do początku układu współrzędnych części.
        4.  Przesuń manipulator jedną lub większą liczbą następujących opcji (tylko odsunięcie od punktu początkowego się liczy, każdy kierunek części jest liczony osobno):
            -   Wciśnij i przytrzymaj lewy przycisk myszy na strzałce osi i przeciągnij aby przesunąć obiekt wzdłuż tej osi.
            -   Wciśnij i przytrzymaj lewy przycisk myszy na płaszczyźnie i przeciągnij aby przesunąć obiekt wzdłuż płaszczyzny.
            -   Wciśnij i przytrzymaj lewy przycisk myszy na kuli i przeciągnij aby obrócić obiekt wokół danej osi.
        5.  Obiekt Move (zobacz [Uwagi](#Notes/pl.md)) zostanie dodany po puszczeniu lewego przycisku myszy.
    -   Rozłóż wzdłuż oddzielnych przemieszczeń:
        1.  Wybierz jedną lub więcej części.
        2.  Pojawi się manipulator.
        3.  Opcjonalnie wyrównaj manipulator (zobacz powyżej).
        4.  Przesuń manipulator jak opisano wyżej (kierunki zgodne z uchwytami manipulatora są brane pod uwagę).
        5.  Obiekt Move zostanie dodany po puszczeniu lewego przycisku myszy.
        6.  Opcjonalnie zaznacz/odznacz części i/lub potwórz przeciąganie aby dodać więcej przemieszczeń.
8.  Wykonaj jedną z poniższych czynności:
    -   Wciśnij przycisk **OK** aby zatwierdzić i zakończyć używanie narzędzia.
    -   Wciśnij przycisk **Anuluj** aby wycofać wszystkie zmiany i zakończyć używanie narzędzia.
9.  Wszystkie części zostanie przesunięte z powrotem do ich złożonych pozycji a linie łączące zostaną schowane.



## Uwagi

-   Manipulator jest narzędziem podobnym do (<img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std_TransformManip](Std_TransformManip/pl.md)), ale bez opcji **Przyrosty** w panelu zadań.
-   Obiekt Move w [widoku drzewa](Tree_view/pl.md) jest reprezentowany przez czerwoną linię przerywaną dla każdej części wchodzącej w skład danego przemieszczenia. Te linie łączące są widoczne tylko gdy narzędzie jest włączona lub w widoku środowiska Rysunek Techniczny utworzonym z obiektu Exploded_View.
-   Aby dodać widok rozłożony do strony Rysunku technicznego: przejdź do środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md), dodaj stronę, wybierz obiekt widoku rozłożonego w drzewie i kliknij [Wstaw widok](TechDraw_View/pl.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Kontenery Exploded_Views to obiekty {{Incode|Assembly::ViewGroup}}. Obiekty Exploded_View wywodzą się z klasy {{Incode|ExplodedView}}, zaś obiekty Move z klasy {{Incode|ExplodedViewStep}}.

### Assembly::ViewGroup



#### Dane


{{TitleProperty|Base}}

-    **Label|String**:

-    **Label2|String|Hidden**:

-    **Expression Engine|ExpressionEngine|Hidden**:

-    **Visibility|Bool|Hidden**:

-    **Group|LinkList**:

-    **_ Group Touched|Bool|Hidden**:



#### Widok


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**:

-    **Show In Tree|Bool**:

-    **Visibility|Bool**:


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**:

-    **Selection Style|Enumeration**:

### ExplodedView

Obiekt **ExplodedView** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Ma też następujące dodatkowe właściwości:



#### Dane 


{{TitleProperty|Exploded View}}

-    **Moves|LinkList**: Lista obiektów Move widoku rozłożenia.

### ExplodedViewStep

Obiekt **ExplodedViewStep** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Ma też następujące dodatkowe właściwości:



#### Dane 


{{TitleProperty|Exploded Move}}

-    **Move Type|Enumeration**: Typ przemieszczenia. ({{Value|Normal}}, {{Value|Radial}}).

-    **Movement Transform|Placement**: Wartość przemieszczenia.

    :   Końcowe położenie jest wynikiem początkowego położenia \* to położenie.

-    **Obj Names|StringList**: Przemieszczanie obiekty.

-    **Parts|LinkList**: Części zawierające przemieszczane obiekty.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateView/pl
