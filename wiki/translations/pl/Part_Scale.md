---
 GuiCommand:
   Name: Part Scale
   Name/pl: Część: Skaluj
   MenuLocation: Część , Skaluj ...
   Workbenches: Part_Workbench/pl
   Version: 0.22
   SeeAlso: Draft_Clone/pl, Draft_Scale/pl
---

# Part Scale/pl



## Opis

Narzędzie **Skaluj** skaluje kształty o określony współczynnik we wszystkich kierunkach lub o różne współczynniki w każdym kierunku głównym. W przypadku różnych współczynników kształty mogą być zniekształcone.

![400px](images/Part_Scale_demo.png) 
*Przykłady skalowania*



## Użycie

1.  Wybierz jeden lub więcej kształtów w oknie [widoku 3D](3D_view/pl.md) lub w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Part_Scale.svg" width=16px> '''Skaluj ...'''**.
    -   Wybierz opcję z menu **Część → <img src="images/Part_Scale.svg" width=16px> Skaluj ...**.
3.  Otworzy się [panel zadań](#Panel_zadań.md).
4.  Wybierz **Skalowanie ujednolicone** lub **Skalowanie niejednolite**.
5.  Ustaw współczynnik skalowania.
6.  Kliknij **OK**.

Alternatywnie, wyboru można dokonać po uruchomieniu narzędzia, wybierając jeden lub więcej kształtów z listy w [Panelu zadań](#Panel_zadań.md).

W widoku drzewa zostanie wyświetlonych tyle obiektów Skalowania, ile wybrano kształtów. Każdy kształt wejściowy jest umieszczony pod indywidualnym obiektem Skala.



## Panel zadań 

![](images/Part_Scale_dialog.png )

-   Przycisk **OK** tworzy skalowany obiekt i zamyka panel zadań.
-   Przycisk **Zamknij** zamyka panel zadań bez wykonywania żadnych działań.
-   Przycisk **Zastosuj** tworzy skalowane obiekty, ale nie zamyka panelu zadań. Następnie można wybrać inny kształt z listy na dole i utworzyć więcej skalowanych obiektów.
-   Lista **Kształt**: tutaj można wybrać kształty do skalowania. W przypadku wybrania wielu kształtów tworzonych jest wiele obiektów operacji skalowania.



## Uwagi

-   Skalowanie nierównomierne zamieni wszystkie krawędzie w krzywe złożone, a wszystkie ściany w powierzchnie złożone. Są one cięższe obliczeniowo.
-   Punkty/wierzchołki nie mogą być skalowane, ponieważ są bezwymiarowe.
-   Obiekty [App: Łącznik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów i kontenery [App: Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz również mogą być skalowane.
-   Panel zadań nie oferuje jeszcze podglądu. Kliknięcie **Zastosuj** utworzy skalowany obiekt za każdym razem, gdy go klikniesz, co może być przydatne jako podgląd. Obiekty jednak pozostaną, a kolejny przeskalowany obiekt zostanie utworzony po kliknięciu przycisku **OK**. [Cofnij](Std_Undo/pl.md) może być przydatne do wyczyszczenia ich przed kliknięciem **OK**.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Skalowania wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Skala}}

-    **Baza|Link**: Kształt wejściowy *(kształt, do którego zastosowano Skalowanie części)*.

-    **Jednolity|Bool**: Kontroluje jednolite i niejednolite skalowanie

-    **Skala jednolita|Float**: Współczynnik skali dla jednolitego skalowania

-    **SkalaX|Float**: Współczynnik skali X dla skalowania nierównomiernego.

-    **SkalaY|Float**: Współczynnik skali Y, analogicznie.

-    **SkalaZ|Float**: Współczynnik skali Z, analogicznie.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Scale/pl
