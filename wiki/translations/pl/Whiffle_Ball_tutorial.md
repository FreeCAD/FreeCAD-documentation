# Whiffle Ball tutorial/pl
---
 TutorialInfo:l
   Topic: Projekt produktu
   Level: początkujący
   Time: 30 minut
   Author: r-frank oraz vocx
   FCVersion: 0.17 inowszy
   Files: https://github.com/FreeCAD/Examples/blob/master/Whiffle_Ball_Tutorial_ExampleFiles/WhiffleBall_Tutorial_FCWiki.FCStd?raw=true WhiffleBall_Tutorial_FCWiki.FCStd
}}



## Wprowadzenie

Ten poradnik został pierwotnie napisany przez Rolanda Franka **, a następnie przepisany i zilustrowany przez vocx.

W tym poradniku dowiesz się, jak korzystać ze środowiska Część.

Środowisko pracy Część było pierwszym opracowanym środowiskiem pracy. Zapewnia ono podstawowe elementy geometryczne, które mogą być używane jako bloki konstrukcyjne dla innych środowisk pracy. Środowisko pracy Część jest przeznaczone do stosowania w tradycyjnym przepływie pracy konstrukcyjna geometria bryłowa **. Aby uzyskać bardziej nowoczesny przepływ pracy z wykorzystaniem szkiców, wyciągnięć i cech, należy użyć środowiska pracy Projekt Części.

Będziesz ćwiczyć:

-   wstawianie elementów pierwotnych,
-   zmienianie parametrów tych obiektów pierwotnych,
-   modyfikowanie ich umiejscowienia,
-   wykonywanie operacji logicznych.

! 
*Ostateczny model kuli wiffle.*



## Konfiguracja

1\. Uruchom FreeCAD, utwórz nowy pusty dokument za pomocą **Plik , File:Std_New.svg   16px Std_New/pl**{: mediawiki} i przełącz się na środowisko Part Workbench.

:   1.1. Naciśnij przycisk **File:Std_ViewIsometric.svg   16px Std_ViewIsometric/pl**{: mediawiki} lub naciśnij **0** na klawiaturze numerycznej, aby zmienić widok na izometryczny w celu lepszej wizualizacji brył w widoku 3D.
:   1.2. Naciśnij przycisk **File:Std_ViewFitAll.svg   16px Std_ViewFitAll/pl**{: mediawiki} za każdym razem, gdy dodajesz obiekty, aby przesuwać i powiększać widok 3D tak, aby wszystkie elementy były widoczne w widoku.
:   1.3. Przytrzymaj **Ctrl** podczas klikania, aby zaznaczyć wiele elementów. Jeśli wybrałeś coś źle lub chcesz usunąć zaznaczenie, kliknij na puste miejsce w widok 3D.



## Wstaw sześcian pierwotny 

2\. Wstaw sześcian pierwotny, klikając w **Image:Part_Box.svg   16px Part_Box/pl**{: mediawiki}.

:   2.1. Wybierz {{incode   Sześcian}}{: mediawiki} w oknie widoku drzewa.
:   2.2. Zmień wymiary w zakładce **Dane** edytora właściwości.
:   2.3. Zmień **Długość** na {{Incode   90 mm}}{: mediawiki}.
:   2.4. Zmień **Szerokość** na {{incode   90 mm}}{: mediawiki}.
:   2.5. Zmień **Wysokość** na {{incode   90 mm}}{: mediawiki}.

3\. W zakładce **Dane** w edytorze właściwości kliknij na wartość **Umiejscowienie**, aby po prawej stronie pojawił się przycisk wielokropka **…**.

:   3.1. Naciśnij wielokropek, aby uruchomić okno dialogowe Umiejscowienie.
:   3.2. Zmień wartości **Przesunięcie**.
:   3.3. Zmień **X** na {{incode   -45 mm}}{: mediawiki}.
:   3.4. Zmień **Y** na {{incode   -45 mm}}{: mediawiki}.
:   3.5. Zmień **Z** na {{incode   -45 mm}}{: mediawiki}.
:   3.6. Naciśnij przycisk **OK**, aby zamknąć okno dialogowe.

4\. Powtórz proces, wstawiając drugą, mniejszą kostkę, klikając **Image:Part_Box.svg   16px Part_Box/pl**{: mediawiki}.

:   4.1. Drugi sześcian zostanie utworzony z tą samą nazwą, ale z dodatkowym numerem, aby rozróżnić obiekt.
:   4.2. W oknie widoku drzewa wybierz {{incode   Cube001}}{: mediawiki}, a następnie zmień jego wymiary i położenie, tak jak w przypadku poprzedniego obiektu.
:   4.3. Zmień **Długość** na {{Incode   80 mm}}{: mediawiki}.
:   4.4. Zmień **Szerokość** na {{incode   80 mm}}{: mediawiki}.
:   4.5. Zmień **Wysokość** na {{incode   80 mm}}{: mediawiki}.
:   4.6. Otwórz okno dialogowe Umiejscowienie.
:   4.7. Zmień **X** na {{incode   -40 mm}}{: mediawiki}.
:   4.8. Zmień **Y** na {{incode   -40 mm}}{: mediawiki}.
:   4.9. Zmień **Z** na {{incode   -40 mm}}{: mediawiki}.
:   4.10. Naciśnij przycisk **OK**, aby zamknąć okno dialogowe.



## Zmiana właściwości wyglądu 

5\. Poprzednie operacje utworzyły mniejszy sześcian wewnątrz większego sześcianu. Aby to zwizualizować, możemy zmodyfikować właściwość **Widok** w edytorze właściwości.

:   5.1. Wybierz {{Incode   Cube001}}{: mediawiki}, mniejszą kostkę, w oknie widoku drzewa i zmień jej kolor. W zakładce **Widok** kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybierz kolor**, a następnie wybierz kolor zielony, zmień także wartość **Szerokość linii** na {{Incode   2.0}}{: mediawiki}.
:   5.2. Wybierz obiekt {{Incode   Sześcian}}{: mediawiki}, większy sześcian, w oknie widok drzewa. W zakładce **Widok** zmień wartość **Przezroczystość** na {{incode   70}}{: mediawiki}.5. Poprzednie operacje utworzyły mniejszy sześcian wewnątrz większego sześcianu. Aby to zwizualizować, możemy zmodyfikować właściwości **Widoku** w edytorze właściwości.

! 
*Bryła sześcianu wewnątrz innej bryły sześcianu.*



## Wstaw walec pierwotny 

6\. Wstaw cylinder pierwotny klikając na **Image:Part_Cylinder.svg   16px Part_Cylinder/pl**{: mediawiki}.

:   6.1. Wybierz {{incode   Walec}}{: mediawiki} w oknie widoku drzewa.
:   6.2. Zmień wymiary w zakładce **Dane** edytora właściwości.
:   6.3. Zmień **Promień** na {{incode   27.5 mm}}{: mediawiki}.
:   6.4. Zmień **Wysokość** na {{incode   120 mm}}{: mediawiki}.
:   6.5. Otwórz okno dialogowe Umiejscowienie.
:   6.6. Zmień **Z** na {{incode   -60 mm}}{: mediawiki}.
:   6.7. Naciśnij przycisk **OK**, aby zamknąć okno dialogowe.

7\. Powtórz proces, wstawiając drugi cylinder, klikając **Image:Part_Cylinder.svg   16px Part_Cylinder/pl**{: mediawiki}.

:   7.1. Drugi cylinder zostanie utworzony z tą samą nazwą, ale z dodatkowym numerem, aby rozróżnić obiekt.
:   7.2. Wybierz obiekt {{incode   Walec001}}{: mediawiki} w oknie widoku drzewa, a następnie zmień jego wymiary i położenie, tak jak w przypadku poprzedniego obiektu.
:   7.3. Zmień **Promień** na {{incode   27.5 mm}}{: mediawiki}.
:   7.4. Zmień **Wysokość** na {{incode   120 mm}}{: mediawiki}.
:   7.5. Otwórz okno dialogowe Umiejscowienie.
:   7.6. Zmień **Y** na {{incode   60 mm}}{: mediawiki}.
:   7.7. Zmień właściwość **Obrót** na {{incode   ROś obrotu z zadanym kątem}}{: mediawiki}; **Oś** na {{incode   X}}{: mediawiki} ** oraz **Kąt** na {{incode   90°}}{: mediawiki}.
:   7.8. Naciśnij przycisk **OK**, aby zamknąć okno dialogowe.

8\. Wstaw kolejny walec. Tym razem utwórz duplikat, aby nie trzeba było zmieniać promienia i wysokości, a jedynie jego położenie.

:   8.1. Zaznacz {{incode   Cylinder001}}{: mediawiki} w oknie widok drzewa i przejdź do menu **Edycja , Std_DuplicateSelection/pl   Duplicate selection**{: mediawiki}. Spowoduje to utworzenie obiektu {{Incode   Cylinder002}}{: mediawiki}.
:   8.2. Otwórz okno dialogowe Umiejscowienie.
:   8.3. Zmień **X** na {{incode   -60 mm}}{: mediawiki} i zmień **Y** z powrotem na {{incode   0 mm}}{: mediawiki}.
:   8.4. Zmień **Obrót** na {{incode   Oś obrotu z zadanym kątem}}{: mediawiki}; **Oś** na {{incode   Y}}{: mediawiki} i **Kąt** na {{incode   90°}}{: mediawiki}.
:   8.5. Naciśnij przycisk **OK**, aby zamknąć okno dialogowe.



## Zmiana właściwości wyglądu 

9\. Poprzednie operacje tworzą trzy cylindry, które przecinają się ze sobą, a także przecinają sześciany. Aby lepiej to zobrazować, możemy zmodyfikować właściwości **Widok** w edytorze właściwości.

:   9.1. Wybierz {{Incode   Sześcian001}}{: mediawiki}, mniejszą kostkę, w widoku drzewa i zmień przezroczystość. W zakładce **Widok** zmień wartość **Przezroczystość** na {{incode   70}}{: mediawiki}.
:   9.2. Wybierz obiekt {{Incode   Walec}}{: mediawiki}, w zakładce **Widok** kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor czerwony.
:   9.3. Wybierz obiekt {{Incode   Walec001}}{: mediawiki}, w zakładce **Widok** kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor niebieski.
:   9.4. Wybierz {{Incode   Walec002}}{: mediawiki}, w zakładce **Widok** kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor różowy.
:   9.5. Zaznacz trzy cylindry, w zakładce **Widok** zmień także wartość **Szerokość linii** na {{Incode   2.0}}{: mediawiki}.

! 
*Przecinające się bryły walców i bryły sześcianów.*



## Połączenie i wycięcie 

10\. W oknie widok drzewa wybierz obiekt {{incode   Sześcian001}}{: mediawiki}  i drzewo walców, a następnie naciśnij **File:Part_Fuse.svg   16px Part_Fuse/pl**{: mediawiki}. Spowoduje to utworzenie obiektu {{incode   Scalenie}}{: mediawiki}.

1\. Następnie wykonaj cięcie logiczne obiektu {{Incode   Sześcian}}{: mediawiki} ** i nowego obiektu {{Incode   Scalenie}}{: mediawiki}.

:   11.1. W oknie widoku drzewa wybierz najpierw {{Incode   Sześcian}}{: mediawiki}, a następnie {{Incode   Scalenie}}{: mediawiki}.
:   11.2. Następnie wciśnij **File:Part_Cut.svg   16px Part_Cut/pl**{: mediawiki}. Spowoduje to utworzenie obiektu {{Incode   Wycięcie}}{: mediawiki}.

Kolejność zaznaczania obiektów jest ważna dla operacji cięcia. Obiekt bazowy jest zaznaczany jako pierwszy, a obiekt odejmowany na końcu.

:   11.3. Jeśli kolory wyglądają dziwnie, wybierz nowy obiekt {{Incode   Wycięcie}}{: mediawiki}, przejdź do zakładki **Widok**, kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor szary; zmień także wartość **Szerokość linii** na {{Incode   2.0}}{: mediawiki}.

! 
*Wydrążony kształt powstały z wycięcia sześcianu i trzech walców z większego sześcianu.*



## Wstaw kostki pierwotne, aby wyciąć narożniki częściowej bryły 

Teraz utworzymy więcej kostek, które będą używane jako narzędzia tnące do przycinania narożników wcześniej uzyskanego obiektu {{Incode   Wycięcie}}{: mediawiki}.

12\. Kliknij **Image:Part_Box.svg   16px Part_Box/pl**{: mediawiki}.

:   12.1. Wybierz {{Incode   Sześcian002}}{: mediawiki} w oknie widok drzewa, a następnie zmień jego wymiary i położenie.
:   12.2. Zmień **Długość** na {{Incode   140 mm}}{: mediawiki}.
:   12.3. Zmień **Szerokość** na {{Incode   112 mm}}{: mediawiki}.
:   12.4. Zmień **Wysokość** na {{Incode   112 mm}}{: mediawiki}.
:   12.5. Otwórz okno dialogowe Umiejscowienie.
:   12.6. Zmień **X** na {{Incode   -70 mm}}{: mediawiki}.
:   12.7. Zmień **Y** na {{Incode   -56 mm}}{: mediawiki}.
:   12.8. Zmień **Z** na {{Incode   -56 mm}}{: mediawiki}.
:   12.9. Naciśnij **OK**.

13\. Kliknij **Image:Part_Box.svg   16px Part_Box/pl**{: mediawiki}.

:   13.1. Wybierz {{incode   Sześcian003}}{: mediawiki} w widok drzewa i zmień wymiary i położenie.
:   13.2. Zmień **Długość** na {{incode   180 mm}}{: mediawiki}.
:   13.3. Zmień **Szerokość** na {{incode   180 mm}}{: mediawiki}.
:   13.4. Zmień **Wysokość** na {{incode   180 mm}}{: mediawiki}.
:   13.5. Otwórz okno dialogowe Umiejscowienie.
:   13.6. Zmień **X** na {{incode   -90 mm}}{: mediawiki}.
:   13.7. Zmień **Y** na {{incode   -90 mm}}{: mediawiki}.
:   13.8. Zmień **Z** na {{incode   -90 mm}}{: mediawiki}.
:   13.9. Naciśnij **OK**.

Powielimy ponownie dwa poprzednie obiekty, aby użyć ich ponownie jako obiektów tnących.

14\. Wybierz tylko {{Incode   Sześcian002}}{: mediawiki} w oknie widok drzewa i przejdź do **Edycja , Std_DuplicateSelection/pl   Powiel zaznaczone**{: mediawiki}. Spowoduje to utworzenie obiektu {{incode   Sześcian004}}{: mediawiki}.

15\. Wybierz tylko {{Incode   Sześcian003}}{: mediawiki} w oknie widok drzewa i przejdź do **Edycja , Std_DuplicateSelection/pl   Powiel zaznaczone**{: mediawiki}. Spowoduje to utworzenie obiektu {{incode   Sześcian005}}{: mediawiki}.

16\. Aby lepiej to zobrazować, możemy zmodyfikować właściwości **Widok** w oknie edytora właściwości.

:   16.1. Zaznacz obiekt {{Incode   Wycięcie}}{: mediawiki}, w zakładce **Widok** kliknij na wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor niebieski.
:   16.2. Zaznacz wszystkie nowe sześciany {{Incode   Sześcian002}}{: mediawiki}, {{Incode   Sześcian003}}{: mediawiki}, {{Incode   Sześcian004}}{: mediawiki} i {{Incode   Sześcian005}}{: mediawiki}, w zakładce **Widok** zmień wartość **Przeźroczystość** na {{Incode   80}}{: mediawiki}.

! 
*Dodatkowe kostki zewnętrzne, które będą używane jako obiekty tnące dla bryły wewnętrznej.*



## Ścinanie narożników 1 

17\. W oknie widok drzewa wybierz {{incode   Sześcian002}}{: mediawiki} i {{incode   Sześcian003}}{: mediawiki}.

:   17.1. Otwórz okno dialogowe Umiejscowienie.
:   17.2. Zaznacz opcję **Zastosuj zmiany przyrostowe**; zauważ, że wszystkie wartości **Przesunięcia** są wyzerowane.
:   17.3. Zmień **Obrót** na {{incode   Oś obrotu z zadanym kątem}}{: mediawiki}; **Oś** na {{incode   X}}{: mediawiki} i **Kat** na {{incode   45°}}{: mediawiki}, a następnie kliknij **Zaqstosuj**. Spowoduje to zastosowanie obrotu wokół osi X i wyzerowanie pola **Kat**.
:   17.4. Zmień **Obrót** ponownie, teraz **Oś** na {{incode   Z}}{: mediawiki} i **Kat** na {{incode   45°}}{: mediawiki}, a następnie kliknij **Zastosuj**. Spowoduje to zastosowanie obrotu wokół lokalnej osi Z i wyzerowanie pola **Kąt**.
:   17.5. Kliknij **OK**, aby zamknąć okno dialogowe.

18\. W oknie widoku drzewa usuń zaznaczenie obiektów; następnie wybierz {{incode   Sześcian003}}{: mediawiki}, większy sześcian, a następnie {{incode   Sześcian002}}{: mediawiki}, mniejszy sześcian.

:   18.1. Następnie naciśnij **File:Part_Cut.svg   16px Part_Cut/pl**{: mediawiki}. Spowoduje to utworzenie obiektu {{incode   Wycięcie001}}{: mediawiki}. Jest to wydrążona bryła, która przecina początkowy obiekt {{incode   Wytcięcie}}{: mediawiki} tylko w niektórych rogach.

19\. Aby lepiej to zobrazować, możemy zmodyfikować właściwości **Widok** w edytorze właściwości.

:   19.1. Zaznacz {{Incode   Sześcian004}}{: mediawiki} i {{Incode   Sześcian005}}{: mediawiki}, w zakładce **Widok**, a następnie zmień wartość **Widoczność** na {{false/pl}}, lub naciśnij klawisz **Spacja** na klawiaturze.
:   19.2. Wybierz {{Incode   Wycięcie001}}{: mediawiki}, kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor czerwony; zmień także wartość **Przezroczystość** na {{Incode   90}}{: mediawiki}.

! 
*Obrócona, wydrążona bryła, która będzie używana jako obiekt tnący dla niektórych narożników bryły wewnętrznej.*



## Ścinanie narożników 2 

20\. W oknie widoku drzewa wybierz obiekt {{incode   Wycięcie001}}{: mediawiki}, w zakładce **Widok** zmień wartość **Widoczność** na {{false/pl}} lub naciśnij klawisz **Spacja** na klawiaturze.

21\. W oknie widoku drzewa wybierz {{incode   Sześcian004}}{: mediawiki} i {{incode   Sześcian005}}{: mediawiki}, w zakładce **Widok** zmień wartość **Widoczność** na {{incode   true}}{: mediawiki} lub naciśnij klawisz **Spacja** na klawiaturze.

:   21.1. Otwórz okno dialogowe Umiejscowienie.
:   21.2. Zaznacz opcję **Zastosuj zmiany przyrostowe**; zauważ, że wszystkie wartości **Przesunięcie** są wyzerowane.
:   21.3. Zmień **Obrót** na {{incode   Oś obrotu z zadanym kątem}}{: mediawiki}; **Oś** na {{incode   X}}{: mediawiki} i **Kąt** na {{incode   45°}}{: mediawiki}, a następnie kliknij **Zastosuj**. Spowoduje to zastosowanie obrotu wokół osi X i wyzerowanie pola {{Incode   Kąt}}{: mediawiki}.
:   21.4. Zmień **Obrót** ponownie, teraz **Oś** na {{incode   Z}}{: mediawiki} i **Kąt** na {{incode   -45°}}{: mediawiki}, a następnie kliknij **Zastosuj**. Spowoduje to zastosowanie obrotu wokół lokalnej osi Z i wyzerowanie pola **Kąt**.
:   21.5. Kliknij **OK**, aby zamknąć okno dialogowe.

22\. W oknie widoku drzewa usuń zaznaczenie obiektów, następnie wybierz {{incode   Sześcian005}}{: mediawiki}, większy sześcian, a następnie {{incode   Sześcian004}}{: mediawiki}, mniejszy sześcian.

:   22.1. Następnie naciśnij **File:Part_Cut.svg   16px Part_Cut/pl**{: mediawiki}. Spowoduje to utworzenie obiektu {{incode   Wycięcie002}}{: mediawiki}. Jest to wydrążona bryła, która przecina początkowy obiekt {{incode   Wytcięcie}}{: mediawiki} tylko w niektórych rogach.

23\. Aby lepiej to zobrazować, możemy zmodyfikować właściwości **Widok** w edytorze właściwości.

:   23.1. Wybierz {{Incode   Wycięcie002}}{: mediawiki}, kliknij na wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz różowy kolor. Zmień także wartość **Przezroczystość** na {{Incode   90}}{: mediawiki}.

! 
*Obrócona, wydrążona bryła, która będzie używana jako obiekt tnący dla niektórych narożników bryły wewnętrznej.*



## Wykończenie modelu 

24\. Upewnij się że wszystkie obiekty są widoczne. W oknie widoku drzewa zaznacz wszystkie obiekty, w zakładce **Widok** zmień wartość **Widoczność** na {{true/pl}} lub naciśnij klawisz **Spacja** na klawiaturze.

! 
*Wewnętrznie wydrążona bryła wraz z zewnętrznymi przedmiotami, które zostaną użyte do jej przecięcia.*

25\. W oknie widoku drzewa usuń zaznaczenie obiektów, a następnie wybierz najpierw obiekt {{incode   Wycięcie}}{: mediawiki}, a następnie {{incode   Wycięcie001}}{: mediawiki}.

:   25.1. Następnie naciśnij **File:Part_Cut.svg   16px Part_Cut/pl**{: mediawiki}. Spowoduje to utworzenie obiektu {{Incode   Wycięcie003}}{: mediawiki}.

! 
*Wewnętrznie wydrążona bryła, wycięta przez obiekt {{Incode   Wycięcie001*.}}{: mediawiki}

26\. W oknie widoku drzewa usuń zaznaczenie, a następnie wybierz najpierw obiektów {{incode   Wycięcie003}}{: mediawiki}, a następnie {{incode   Wycięcie002}}{: mediawiki}.

:   26.1. Następnie naciśnij **File:Part_Cut.svg   16px Part_Cut/pl**{: mediawiki}. Spowoduje to utworzenie {{incode   Wycięcie004}}{: mediawiki}. To jest ostateczny obiekt.
:   26.2. Wybierz {{Incode   Wycięcie004}}{: mediawiki}, kliknij wartość **Kolor kształtu**, aby otworzyć okno dialogowe **Wybór koloru**, a następnie wybierz kolor zielony. Zmień także wartość **Szerokość linii** na {{Incode   2.0}}{: mediawiki}.

! 
*Wewnętrznie wydrążona bryła, wycięta przez obiekt {{incode   Wycięcie001* i `Wycięcie002`. Model końcowy.}}{: mediawiki}

27\. Rzeczywiste obiekty nie mają idealnie ostrych krawędzi lub narożników, więc zastosowanie zaokrąglenia na krawędziach może być wykonane w celu udoskonalenia modelu.

:   27.1. W widoku drzewa wybierz obiekt {{Incode   Wycięcie004}}{: mediawiki}, a następnie naciśnij przycisk **File:Part_Fillet.svg   16px Part_Fillet/pl**{: mediawiki}.
:   27.2. W oknie **Zaokrąglenie krawędzi** panelu zadań przejdź do sekcji **Wybór**, wybierz **Wybór krawędzi**, a następnie wciśnij **Wszystkie**. Jako **Typ zaokrąglenia** wybierz {{Incode   Promień stały}}{: mediawiki}, a następnie ustaw **Promień** na {{Incode   1 mm}}{: mediawiki}.
:   24.3. Naciśnij **OK**. Spowoduje to utworzenie obiektu {{incode   Zaokrąglenie}}{: mediawiki}.
:   27.4. W zakładce **Widok** zmień wartość **Szerokość linii** na {{incode   2.0}}{: mediawiki}.

! 
*Końcowy model kuli Whiffle z zaokrągleniami na krawędziach.*


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Whiffle Ball tutorial/pl
