# <img alt="Ikonka FreeCAD dla środowiska pracy Manipulator" src=images/Manipulator_workbench_icon.svg  style="width:64px;"> Manipulator Workbench/pl



## Wprowadzenie


{{TOCright}}

Środowisko pracy [Manipulator](Manipulator_Workbench/pl.md) to [zewnętrzne środowisko pracy](External_workbenches/pl.md) mające na celu pomoc użytkownikom FreeCAD w wyrównywaniu, przesuwaniu, obracaniu i mierzeniu obiektów 3D poprzez przyjazny GUI. Ta seria narzędzi pomaga Przemieszczać umiejscowienie i dokonywać Pomiarów obiektów i modeli STEP w programie FreeCAD.



## Funkcjonalność

![](images/Aligner-ico.png ) **Wyrównywacz:** zestaw narzędzi do przesuwania i wyrównywania części 3D. Może również wyrównać obiekt *(ścianę, krawędź, punkt)* do punktu odniesienia położenia w programie FreeCAD.

![](images/Manipulator_Mover.svg ) **Przesuwacz**: zestaw narzędzi do przesuwania i obracania części 3D na różnych osiach.

![](images/Manipulator_Caliper.svg ) **Suwmiarka:** zestaw narzędzi do pomiaru części 3D, z niektórymi funkcjami przyciągania i pomiarami promienia, długości, kąta.

Pomocnicy ci pracują z obiektami **Część, App::Part i Zawartość**.

Narzędzia te mogą być **pływające** lub **zadokowane w lewą lub prawą stronę**.

Każde narzędzie ma ![](images/Help-btn.png ) **Przycisk pomocy**, aby można było uzyskać kilka przydatnych wskazówek.



## Bibliografia

-   Autor w serwisie Github: [\@easyw](https://github.com/easyw)
-   Forum FreeCAD: [easyw-fc](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=6387)
-   Kod źródłowy w serwisie Github: <https://github.com/easyw/Manipulator>
-   Ogłoszenia / dyskusje na forum: <https://forum.freecadweb.org/viewtopic.php?t=24742>



## Poradnik

<img alt="środowisko Manipulator w pracy" src=images/Manipulator-WB-@Work.png  style="width:1024px;">



*Poradnik w serwisie YouTube [https://youtu.be/owGzsd1fyZc środowisko Manipulator w pracy]*



## Przybory

![](images/Manipulator-WB-Tools.png ) 
*Powyżej: Okienko dialogowe środowiska pracy Manipulator. Bardziej szczegółowy opis znajduje się w pliku [https://github.com/easyw/Manipulator/blob/master/README.md README.md] w serwisie Github.*



### Wyrównywacz

![](images/Manipulator-WB-Aligner.gif ) 
*Wyrównywacz: zestaw narzędzi do przesuwania i wyrównywania części 3D. Może również wyrównać obiekt ''(ścianę, krawędź, punkt)'' do punktu odniesienia położenia w programie FreeCAD.*



### Przesuwacz

![](images/Manipulator-WB-Mover.gif ) 
*Przesuwacz: zestaw narzędzi do przesuwania i obracania części 3D na różnych osiach.*

![](images/Manipulator-WB-Mover-with-App_Part&Body.gif ) 
*Przesuwacz: Wykorzystanie App:Part oraz Zawartości.*

![](images/Manipulator-WB-Mover-with-External-Reference.gif ) 
*Przesuwacz: z odniesieniem zewnętrznym.*



### Suwmiarka

![](images/Manipulator-WB-Measure-Radius.gif ) 
*Suwmiarka: pomiar promienia.*

![](images/Manipulator-WB-Measure-Angles.gif ) 
*Suwmiarka: pomiar kąta.*

![](images/Manipulator-WB-Dimension.gif ) 
*Suwmiarka: pomiar rozmiaru.*

![](images/Manipulator-WB-Dimension-2.gif ) 
*Suwmiarka: pomiar rozmiaru ''(kontynuacja)''.*

![](images/Manipulator-WB-Parallel-Planes-Distance.gif ) 
*Suwmiarka: odległość płaszczyzn równoległych.*



### Manipulator

![](images/Manipulator-WB-Assembly-Parts.gif )



## Instalacja



### Instalacja automatyczna 

Zalecanym sposobem na zainstalowanie środowiska pracy Manipulator jest instalacja poprzez <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md) z menu **Przybory → Menadżer dodatków**.


<div class="mw-collapsible mw-collapsed toccolours" style="width:600px">



### Instalacja samodzielna 

Jeśli konieczna jest instalacja samodzielna, należy postępować zgodnie z poniższymi instrukcjami:


<div class="mw-collapsible-content">

-   Skopiuj źródło Manipulatora do podkatalogu **Mod** aplikacji FreeCAD.


```python
cd ~/.FreeCAD/Mod 
git clone https://github.com/easyw/Manipulator Manipulator
```

-   Uruchom ponownie program FreeCAD.


</div>


</div>



### Wsparcie

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 11707
-   FreeCAD v0.18+
-   FreeCAD v0.19+



## Historia

Środowisko pracy wyewoluowało z makrodefinicji [Wyrównaj obiekty do ścian lub krawędzi](Macro_Center_Align_Objects_with_Faces_or_Edges/pl.md).



## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Manipulator Workbench/pl
