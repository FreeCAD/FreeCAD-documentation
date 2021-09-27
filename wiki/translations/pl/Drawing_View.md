---
- GuiCommand:/pl
   Name:Drawing View
   Name/pl:Kreślenie: Widok
   Workbenches:[Kreślenie](Drawing_Workbench/pl.md), [Complete](Complete_Workbench/pl.md)
   MenuLocation:Kreślenie → Wstaw widok w rysunku
   Shortcut:brak
   SeeAlso:[Rysunek w formacie poziomym A3](Drawing_Landscape_A3/pl.md)
---

# Drawing View/pl

To narzędzie tworzy nowy widok wybranego obiektu w aktywnym arkuszu rysunkowym.

<img alt="Arkusz rysunkowy z trzema widokami: z przodu, z góry oraz izometryczny." src=images/Drawing_Views.png  style="width:500px;">

### Użycie

Zaznacz obiekt w oknie [widoku 3D](3D_view/pl.md) lub w drzewie projektu, a następnie kliknij narzędzie Widok rysunku. Domyślnie zostanie umieszczony widok z góry przeskalowany w skali 1:1 *(skala rzeczywista)* w lewym górnym rogu strony. Może on nie być widoczny, jeśli jest zbyt mały lub zbyt duży dla strony.

Obiekt **Widok** jest dodawany do obiektu **Strona** w drzewie projektu. Dla kolejnych widoków do nazwy zostanie dołączony trzycyfrowy numer. Kliknij na strzałkę przed obiektem Strona, aby go rozwinąć i wyświetlić widoki, które zawiera.

Jeśli tylko obiekt jest wybrany w drzewie projektu, widok jest dodawany do pierwszej strony projektu. Jeśli masz wiele stron w projekcie zaznacz obiekt oraz stronę, do której ma zostać dodany. Następnie kliknij na ikonę, aby dodać widok do wybranej strony.

### Modyfikacja istniejącego widoku 

Rozwiń obiekt Strona w drzewie projektu i wybierz widok. Jego parametry można edytować w zakładce *Dane* Widoku właściwości.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Widok izometryczny z liniami wygładzonymi widoczność wyłączona](images/Drawing_View_Iso.png‎  style="width:150px;"> <img alt="IWidok izometryczny z liniami wygładzonymi widoczność włączona" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width:150px;">


{{Properties Title|Podstawowe}}

-    {{PropertyData/pl|Etykieta}}: zmienia tekst etykiety widoku w drzewie projektu. Możesz również kliknąć na widok w drzewie i kliknąć prawym przyciskiem myszy → Zmień nazwę, lub nacisnąć **F2**.


{{Properties Title|Widok rysunku}}

-    {{PropertyData/pl|Obrót}}: obraca widok. Na przykład, widok izometryczny wymaga obrotu o 60 stopni *(patrz również parametr Kierunek poniżej)*.

-    {{PropertyData/pl|Scala}}: ustawia skalę widoku.

-    {{PropertyData/pl|X}}: ustawia poziomą pozycję widoku na stronie w milimetrach.

-    {{PropertyData/pl|Y}}: ustawia pionową pozycję widoku na stronie w milimetrach. Należy pamiętać, że współrzędna *(0,0)* znajduje się w lewym górnym rogu strony, więc im wyższa liczba, tym niżej na stronie będzie znajdował się widok.


{{Properties Title|Widok kształtu}}

-    {{PropertyData/pl|Kierunek}}: zmienia kierunek widoku. Jest on ustawiany przez wartości xyz, które definiują wektor normalny dla stron. Widok górny będzie miał wartość *(0,0,1)*, a izometryczny *(1,1,1)*. Wartości mogą być ujemne.

-    {{PropertyData/pl|Pokaż niewidoczne linie}}: włącza lub wyłącza widoczność niewidocznych linii poprzez wybranie wartości `True` lub {{False}}.

-    {{PropertyData/pl|Pokaż linie gładkie}}: włącza lub wyłącza widoczność linii gładkich wybierając `True` lub {{False}}. Gładkie linie są również nazywane krawędziami styczności. Krawędzie te wskazują zmiany powierzchni pomiędzy powierzchniami stycznymi.

### Kreator widoków rysunków 

Aby automatycznie wygenerować arkusz rysunkowy z widokami standardowymi, użyj [Makrodefinicja: Automatyczne rysowanie](Macro_Automatic_drawing/pl.md). 

### Inne

Jeśli szukasz przełączania persektywnego i ortogonalnego w widoku 3D, sprawdź strony _





{{Drawing Tools navi

}}

---
[documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing View/pl
