# Tasks Placement/pl
## Opis

Polecenie modyfikujące **Umiejscowienie**. Opcje te odnoszą się tylko do położenia i orientacji obiektu w przestrzeni, nie wpływają na inne atrybuty kształtu. Umiejscowienie jest przechowywane wewnętrznie jako pozycja i obrót *(oś obrotu i kąt przekształcone w [kwaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation))*. Chociaż istnieje kilka metod określania obrotu, na przykład za pomocą środka obrotu, jest on używany tylko do wpływania na obliczenia obrotu i nie jest przechowywany do późniejszych operacji. Podobnie, jeśli określono oś obrotu *(1,1,1)*, może ona zostać znormalizowana po zapisaniu w kwaternionie i pojawić się jako *(0,58, 0,58, 0,58)* podczas późniejszego przeglądania parametrów obiektu.



## Użycie

Dostęp do funkcji **Umiejscowienie** można uzyskać na kilka sposobów:

-   poprzez [skrypty](Python_scripting_tutorial#Vecteurs_et_Positions.md) Python w konsoli i jego [API](Placement_API.md).

:   ![Tworzenie skryptów Umiejscowienie jako y/p/r i macierz](images/PlacePyConv10.png )

-   lub w oknie **Widoku połączonego → Właściwości → Dane → Umiejscowienie → **...****,

:   ![Task_Placement/pl](images/Tache_Placement_fr_01.png )

-   lub przez menu **Edycja → Umiejscowienie ...**.



### Włączenie umiejscowienia w Widoku połączonym 

-   Kliknij kształt, aby go zaznaczyć.
-   Kliknij Umiejscowienie*\'*(tytuł, nie małą strzałkę)\'\', a pojawi się przycisk z wielokropkiem **…**: <img alt="Rozmieszczenie detali" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">
-   Kliknięcie wielokropka spowoduje wyświetlenie okna dialogowego **Umiejscowienie**:

:   ![](images/Tache_Placement_en_02.png )



### Opcje


{{TitleProperty|Przesunięcie}}

-    {{TasksTag|X}}<img alt="Przemieszczenie w kierunku X *(kliknij, aby powiększyć)*" src=images/Tache_Placement_Translation_X_fr.gif  style="width:150px;"> Przesuwa układ współrzędnych obiektu w kierunku **X** w odniesieniu do współrzędnych początku osi 0, 0, 0.

-    {{TasksTag|Y}}<img alt="Przemieszczenie w kierunku Y *(kliknij, aby powiększyć)*" src=images/Tache_Placement_Translation_Y_fr.gif  style="width:150px;"> Przesuwa układ współrzędnych obiektu w kierunku **Y** w odniesieniu do współrzędnych początku osi 0, 0, 0.

-    {{TasksTag|Z}}<img alt="Przemieszczenie w kierunku Z *(kliknij, aby powiększyć)*" src=images/Tache_Placement_Translation_Z_fr.gif  style="width:150px;"> Przesuwa układ współrzędnych obiektu w kierunku **Z** w odniesieniu do współrzędnych początku osi 0, 0, 0.


{{TitleProperty|Środek}}

-    {{TasksTag|X}}: Przesuwa środek obrotu w kierunku **X**, od współrzędnych wybranego obiektu. *(domyślnie: 0,0,0)*

-    {{TasksTag|Y}}: Przesuwa środek obrotu w kierunku **Y**, od współrzędnych wybranego obiektu. *(domyślnie: 0,0,0)*

-    {{TasksTag|Z}}: Przesuwa środek obrotu w kierunku **Z**, od współrzędnych wybranego obiektu. *(domyślnie: 0,0,0)*

-    {{TasksTag|User Defined...}}: Umożliwia modyfikację wartości współrzędnych trzech osi *(**X, Y, Z**)* w jednej operacji <img alt="Określony przez użytkownika" src=images/Part_Revolve_fr_06.png  style="width:96px;">.


{{TitleProperty|Obrót}}

Aby dostosować nasze **parametry obrotu**, mamy do dyspozycji dwie metody.

-   Pierwsza opcja. Wybierz **Oś obrotu z zadanym kątem**<img alt="Detale umiejscowienia. Opcja osi obrotu i kąta" src=images/Tache_Placement_fr_05.png  style="width:256px;"> *(Domyślnie)*.
    -   
        {{TasksTag|Oś: X}}
        
        : Obrót nastąpi na osi **X**.

    -   
        {{TasksTag|Oś: Y}}
        
        : Obrót będzie na osi *Y*.

    -   
        {{TasksTag|Oś: Z}}
        
        : Obrót nastąpi na osi *Z*. (Oś domyślna).

    -   
        {{TasksTag|Oś:}}
        
        . Kąt obrotu w stopniach od **-360.00°** do **360.00°** *(Domyślnie: **0.00°**)*.

-   Druga opcja. Wybierz **Kąty Eulera** <img alt="Detale umiejscowienia. Opcja kątów Eulera" src=images/Tache_Placement_fr_04.png  style="width:256px;">.

Ta opcja może być łatwiejsza w użyciu, jednak nawet w tym trybie należy pamiętać o ważnych rzeczach: Dodatnie obroty są w kierunku zgodnym z **ruchem wskazówek zegara**, patrząc **na zewnątrz** od początku wzdłuż dodatniej osi. Mówiąc inaczej, obroty są dodatnie w kierunku **przeciwnym do ruchu wskazówek zegara**, patrząc **do środka** do początku wzdłuż dodatniej osi.

  -


<div id="Yaw">


</div>

**[Yaw](https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft))** : to poziomy obrót Zawartości wokół osi pionowej. *(Symbol **ψ**\' jest często używany dla odchylenia)*.

  -


<div id="Pitch">


</div>

**[Pitch](https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft))** : definiuje się jako oscylacyjny ruch statku do przodu i do tyłu.

  -


<div id="Roll">


</div>

**[Roll](https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft))** : jest to ruch obrotowy ciała wokół jego osi wzdłużnej *(osi obrotu)*.

Odchylenie *(yaw)*, wychylenie *(pitch)* i przechylenie *(roll)* odnoszą się do \"położenia\" obiektu w przestrzeni 3D. Terminy te są powszechnie używane w lotnictwie. Kąty te są **kątami Taita-Bryana**. Więcej informacji można znaleźć na stronie [Kąty Eulera](https://en.wikipedia.org/wiki/Euler_angles).

![None\|Opcja Kąty Eulera](images/Tache_Placement_en_03.png )

![None\|Yaw](images/Tache_Placement_Lacet_fr_Mini.gif )

-    {{TasksTag|oś yaw}}**Yaw to obrót wokół osi Z**, czyli obrót od lewej do prawej. *(Kąt odchylenia to*Psi ψ*)*. Wartość **-360,00°** do **360, 00°** *(domyślnie, **0,00°**)*.

![None\|Pitch](images/Tache_Placement_Tangage_fr_Mini.gif )

-    {{TasksTag|oś pitch}}**Pitch to obrót wokół osi Y**, czyli nos w górę i nos w dół. *(Kąt nachylenia to **Phi φ**)*. Wartość **-360,00°** do **360, 00°** *(domyślnie **0,00°**)*.

![None\|Obrót](images/Tache_Placement_Roulis_fr_Mini.gif )

-    {{TasksTag|oś roll}}**Roll oznacza obrót wokół osi X**, czyli inaczej mówiąc skrzydło w górę i w dół. *(Kąt obrotu to **Thêta θ**)*. Przyjmuje wartość **-360.00°** do **360, 00°** *(domyślnie, **0.00°**)*.

-    {{TasksTag|Zastosuj zmiany przyrostowe}}do umieszczenia obiektu: Po wybraniu, ta opcja **wirtualnie** ustawia wszystkie parametry na zero, aby umożliwić wprowadzenie wartości bez konieczności obliczania z oryginalnymi parametrami formularza. Po potwierdzeniu przyciskiem **OK**, wprowadzone wartości zostaną dodane do wartości w formularzu.

-   Przycisk **Reset** przywraca wszystkie wartości do **0,0,0**.



## Odnośniki internetowe i przykłady 

Praktyczny przykład użycia tego polecenia znajduje się w poradniku [Samolot](Aeroplane/pl.md).

Inne wyjaśnienie dotyczące [Umiejscowienie](Placement/pl.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Command_Reference](Category_Command_Reference.md) > Tasks Placement/pl
