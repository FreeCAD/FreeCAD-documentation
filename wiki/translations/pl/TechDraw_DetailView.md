---
 GuiCommand:
   Name: TechDraw DetailView
   Name/pl: Rysunek Techniczny: Wstaw widok szczegółu
   MenuLocation: Rysunek Techniczny , Widoki  , Wstaw widok szczegółu
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_View/pl
---

# TechDraw DetailView/pl



## Opis

Narzędzie **Wstaw widok szczegółu** tworzy widok małego obszaru istniejącego widoku.

![](images/ViewDetail.png ) 
*Widok szczegółu z okrągłym obrysem.*



## Użycie

1.  Wybierz widok podstawowy dla widoku szczegółu.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_DetailView.svg" width=16px> '''Wstaw widok szczegółu'''**, aby utworzyć widok szczegółu.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki Rysunku Technicznego → <img src="images/TechDraw_DetailView.svg" width=16px> Wstaw widok szczegółu**.
3.  Do widoku podstawowego dodawany jest kontur podświetlenia, do strony dodawany jest widok szczegółu i otwierany jest panel zadań.
4.  Dla przejrzystości najlepiej jest przesunąć widok szczegółu tak, aby nie nakładał się już na widok podstawowy: przytrzymaj lewy przycisk myszy na jego ramce lub etykiecie i przeciągnij go do nowej pozycji.
5.  Aby zmienić położenie konturu zaznaczenia, wykonaj jedną z poniższych czynności:
    -   Przesuń kontur, przeciągając go:
        1.  Naciśnij przycisk **Podświetlenie szczegółu**.
        2.  Kontur zostanie zaznaczony na stronie i dodana zostanie tymczasowa etykieta \"przeciągnij\".
        3.  Przytrzymaj lewy przycisk myszy na samym obrysie lub na tej etykiecie i przeciągnij obrys do nowej pozycji.
    -   Przesuwanie obrysu za pomocą współrzędnych:
        1.  Zmień współrzędne X i Y w panelu zadań. Współrzędne są względne w stosunku do środka widoku podstawowego.
6.  Opcjonalnie zmień *Promień* widoku szczegółu.
7.  Opcjonalnie zmień *Typ skali* i *Współczynnik skali* widoku szczegółu. Więcej informacji można znaleźć w na stronie [Wstaw widok](TechDraw_View/pl#Właściwości.md).
8.  Określ etykietę **Odniesienie**. Etykieta ta będzie wyświetlana w pobliżu konturu zaznaczenia.
9.  Naciśnij przycisk **OK**.



## Uwagi

-   Aby edytować widok szczegółu, kliknij go dwukrotnie w oknie [Widok drzewa](Tree_view/pl.md).
-   Kontury widoków szczegółu mogą być okrągłe lub kwadratowe. Jest to kontrolowane przez [ustawienia](TechDraw_Preferences/pl#Adnotacje.md) **Kształt konturu widoku szczegółu** .
-   [Temat na forum z dobrą dyskusją na temat ustawiania kotwicy](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281).



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

We właściwościach **Widok podstawowy** możesz zmienić wygląd zarysu szczegółu.

Widok szczegółu, formalnie obiekt {{Incode|TechDraw::DrawViewDetail}}, wywodzi się z [Widoku części](TechDraw_View/pl#Właściwości_-_Widok_części.md), formalnie obiektu {{Incode|TechDraw::DrawViewPart}} i dziedziczy wszystkie jego właściwości. Ma również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Wygląd}}

-    **Pokaż matowanie|Bool**: Pokaż lub ukryj matowanie wokół widoku szczegółu. {{Version/pl|1.0}}

-    **Pokaż podświetlenie|Bool**: Pokaż lub ukryj podświetlenie w widoku źródłowym. {{Version/pl|1.0}}


{{TitleProperty|Szczegół}}

-    **Widok podstawowy|Link**: Widok, na którym opiera się ten widok szczegółu.

-    **Punkt kotwiczenia|Vector**: Środek widoku szczegółowego w obrębie **Widoku podstawowego**.

-    **Promień|Float**: Rozmiar obszaru w **Widoku podstawowym**, który jest wyświetlany w widoku szczegółów.

-    **Odniesienie|String**: Identyfikator widoku szczegółowego w **Widoku podstawowym**.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/pl
