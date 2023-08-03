---
 TutorialInfo:l
   Topic: środowisko praczy Część
   Level: początkujący
   Time: 10 minut
   Author: Hughthecat
   FCVersion: wszystkie
   Files: brak
---

# Aeroplane/pl







## Pierwszy krok 

Będziemy pracować w środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) - wybierając go z menu **Widok → Środowiska pracy → Część** lub z [okienka wyboru środowiska pracy](Std_Workbench/pl.md).

-   Utwórz nowy pusty dokument.
-   Przełącz na <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [widok izometryczny](Std_ViewIsometric/pl.md).
-   Przełącz krzyż osi **ON** *(poprzez menu widoku)*.
-   Upewnij się, że [Widok połączony](Combo_view/pl.md) jest włączony *(poprzez menu **Widok → Panele**)*.

-   Utwórz walec, klikając przycisk <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Walec](Part_Cylinder/pl.md).
-   Wybierz go, klikając obiekt Walec w przeglądarce projektu.
-   Kliknij w zakładkę Dane w dolnej części przeglądarki projektu.

Zmień wysokość na {{Value|20 mm}}. Pozostaw promień na wartości {{Value|2 mm}}

Kliknij na [Umiejscowienie](Placement/pl.md) *(zwróć uwagę na mały **[+]**)*, a pojawi się przycisk z trzema kropkami **…**. Kliknij go *(Możesz także wybrać: **Menu → Edycja → Umiejscowienie**)*. Pojawi się panel zadań.

<img alt="" src=images/HTCaeroplane01.png  style="width:300px;">

Jeśli nie jesteś zaznajomiony z osiami XYZ, pobaw się liczbami w polu Przesunięcia. Po zakończeniu testów kliknij przycisk **Reset**.



## Drugi krok 

<img alt="" src=images/HTCaeroplane02.png  style="width:400px;">

Teraz obrócimy walec tak, aby leżał wzdłuż osi X. W tym celu należy go obrócić wokół osi Y. W polu Obrót powinien pojawić się napis **Oś obrotu z zadanym kątem**, więc zmień Oś na Y i zwiększaj Kąt, aż osiągnie 90°. Kliknij **OK**.

Lubię bawić się obracaniem widoku w tym momencie *(i to często!)*, więc jak najbardziej. Powinieneś znaleźć *szew* cylindra na spodzie.

<img alt="" src=images/HTCaeroplane03.png  style="width:400px;">

Teraz dodamy i zmodyfikujemy sześcian, więc kliknij przycisk <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Sześcian](Part_Box/pl.md). Wybierz go klikając na obiekt Sześcian w oknie [Widoku drzewa](Tree_view/pl.md) w przeglądarce projektów. Zmień wysokość na {{Value|1 mm}}, długość na {{Value|5}} mm i szerokość na {{Value|20 mm}}.

Kliknij [Umiejscowienie → **…**](Placement/pl.md), aby wyświetlić Panel zadań. W polu translacji wpisz Y: -10 i Z: -1. Kliknij **OK**.

Teraz połączymy te dwa kształty za pomocą operacji logicznej. Kliknij przycisk <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Operacja logiczna](Part_Boolean/pl.md), a Panel zadań wyświetli okno wyboru operacji logicznych.

Upewnij się, że opcja **Połączenie** jest zaznaczona, a Walec i Sześcian są zaznaczone na dwóch listach kształtów. Kliknij przycisk **Zastosuj**. Kliknij przycisk **Zamknij**. Masz teraz pojedynczy obiekt o nazwie **Połączenie**.




Dodajmy jeszcze jeden prostopadłościan, aby zakończyć nasz model. Utwórz Sześcian, wybierz go i zmień jego wysokość na {{Value|5 mm}}, długość na {{Value|3 mm}} i szerokość na {{Value|1 mm}}. Zmień jego położenie na Y: -0.5.

Musimy teraz dołączyć nasz obiekt Scalenie do Box001, więc zrobimy to w szybki sposób. Kliknij Scalenie w Widoku drzewa i **Ctrl** + kliknij Box001. Spowoduje to zaznaczenie obu części razem. Teraz kliknij na przycisk <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Scalenie](Part_Fuse/pl.md), aby uzyskać **Fusion001**.

Powinieneś teraz mieć prosty model samolotu. Kliknij prawym przyciskiem myszy na **Fusion001** i zmień jego nazwę na **Aeroplane**.

<img alt="" src=images/HTCaeroplane04.png  style="width:500px;">

Myślę, że skrzydła powinny być przesunięte nieco do przodu, ale jeśli wybiorę Aeroplane i spróbuję zmienić jego Umiejscowienie przesunięcia X, całość się przesunie. Chcę przesunąć tylko skrzydła, więc anuluję Umiejscowienie.

Rozwiń obiekt Samolot *(kliknij przycisk **[+]** obok niego)* i rozwiń obiekt Scalenie.

Kliknij na obiekt Sześcian i uzyskaj jego [Umiejscowienie](Placement/pl.md) w Panelu zadań. Zauważ, że ma już wartości Y: -10 i Z: -1 w przesunięciu. Zmień tłumaczenie X na 3 i kliknij **Zastosuj**. Tak jest lepiej. Kliknij **OK**.






## Obrót

Kliknij na Aeroplane i przejdź do [Umiejscowienie](Placement/pl.md) w Panelu zadań. W sekcji Obrót zmień **Oś obrotu z zadanym kątem** na **Kąty Eulera (ZY\'X\')**, ponieważ łatwiej się z nimi pracuje.

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Yaw** to obrót wokół osi *Z*, czyli obrót od lewej do prawej. *(Kąt odchylenia to **Psi ψ**)*.  ![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pitch** to obrót wokół osi Y, czyli nosem w górę i nosem w dół. *(Kąt nachylenia to **Phi φ**)*.  ![](images/Tache_Placement_Roulis_fr_Mini.gif )**Roll** to obrót wokół osi **X**, czyli skrzydło w górę i w dół. *(Kąt obrotu to **Thêta θ**)*. 

Jednak nawet w tym przypadku należy pamiętać o kilku ważnych rzeczach:

-   Pozytywne obroty są zgodne z ruchem wskazówek zegara, gdy patrzy się od początku na zewnątrz wzdłuż dodatniej osi. Lub mówiąc inaczej: Obroty dodatnie są przeciwne do ruchu wskazówek zegara, gdy patrzy się na nie od osi dodatniej w kierunku początku.

-   Chociaż te trzy etykiety to Yaw, Pitch i Roll, tak naprawdę nie są tym, czym są. Odchylenie, pochylenie i przechylenie są odniesieniami do \"współrzędnych Zawartości\" obiektu w przestrzeni 3D. Etykiety powinny brzmieć Nagłówek, Wysokość i Brzeg lub nawet Azymut, Nachylenie i Brzeg, ponieważ w rzeczywistości odnoszą się do **współrzędnych przestrzennych** systemu 3D. Są to **kąty Taita-Bryana**. Więcej informacji można znaleźć na stronie [Kąty Eulera](http://en.wikipedia.org/wiki/Euler_angles#Tait-Bryan_angles).

-   Gdy samolot znajduje się w obecnej pozycji, obowiązują proste zasady. Odchylenie to obrót wokół osi Z, tj. w lewo i w prawo. Pitch to obrót wokół osi Y, czyli nos w górę i w dół. Roll to obrót wokół osi X, czyli skrzydła w górę i w dół. Jest to dobre na początek, ale nie będzie prawdziwe później!

Pobaw się trzema liczbami YPR. Wystarczy zmienić je o kilka stopni, aby zrozumieć ideę. Zresetuj po zakończeniu.

Teraz zobaczymy, dlaczego etykiety Yaw-Pitch-Roll nie są odpowiednie. Zmień wartość Roll na 90°. Odchylenie powinno przesuwać nos samolotu w górę i w dół, a pochylenie powinno przesuwać go na boki \"patrząc z zewnątrz samolotu\", czyli tam, gdzie jesteśmy. Czy tak? Nie, nie zmieniają! Pitch zmienia przechylenie, a Yaw zmienia pochylenie. OK, reset.

Tak więc lepszym sposobem myślenia o rotacjach jest to, że odchylenie zmienia długość geograficzną, pochylenie zmienia szerokość geograficzną, a przechylenie zmienia kierunek *(NSEW)*, w którym stoisz. Lub możesz sprawdzić [Konwencje osi](http://en.wikipedia.org/wiki/Axes_conventions) dla innych opisów.

W porządku, wracamy do pracy. Zmień Yaw na 45° i Pitch na -30°. Kliknij OK, aby pokazać, że operacja została zakończona. Teraz wróć do [Umiejscowienie](Placement/pl.md) w Panelu zadań i spójrz na pole Obrót. Wartość została zmieniona na *Oś obrotu z zadanym kątem* i zawiera dziwne liczby w polach Oś i Kąt. Mój miał Oś: *(0.219493,-0.529904,0.819161)* i Kąt: 53.65°. Trzy liczby w nawiasach to składowe XYZ wektora jednostkowego w przestrzeni 3D. Jest to oś, wokół której nasz oryginalny samolot został obrócony, aby uzyskać nasz ostateczny samolot. Kąt określa, o ile został obrócony. Sprytne, ale niezbyt przyjazne! To Euler pokazał, że można połączyć serię obrotów XYZ w jeden obrót wokół jednej osi.

Oto kilka innych sugestii dotyczących zabawy z samolotem:

-   Zmień lokalizację Z *(i zastosuj)*, a następnie zmień wartości YPR i zobacz, jaki będzie efekt. Następnie spróbuj zmienić lokalizacje X i Y i obrócić.
-   Zmień środek X *(i zastosuj)*, a następnie zmień wartości YPR i zobacz, jaki będzie efekt. Następnie spróbuj zmienić centra Y i Z i obrócić.

Mam nadzieję, że ten mały poradnik pomógł Ci zrozumieć rotacje.



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Aeroplane/pl
