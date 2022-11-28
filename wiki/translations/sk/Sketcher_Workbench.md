# <img alt="ikona pracovného stola Náčrtník" src=images/Workbench_Sketcher.svg  style="width   *64px;"> Sketcher Workbench/sk


{{TOCright}}

## Úvod

<img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Pracovný stôl Náčrtník](Sketcher_Workbench.md) sa vo FreeCADe používa na tvorbu 2D geometrie, ktorú následne využijete v <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [na pracovnom stole Dizajn dielca](PartDesign_Workbench.md), <img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> [pracovnom stole Arch](Arch_Workbench.md) a iných pracovných stoloch. Vo všeobecnosti sa za východiskový bod pre väčšinu CAD modelov považuje 2D náčrt, pretože ten dokážeme „vytiahnuť" a vytvoriť tak 3D tvar; navyše je možné 2D náčrty okrem predtým vytvorených 3D tvarov použiť aj na vytvorenie ďalších prvkov, ako sú kapsy, ryhy alebo výlisky. Spolu s booleanovskými operáciami definovanými na <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [pracovnom stole Diel](Part_Workbench.md) tvorí Náčrtník základ [konštruktívnej geometrie telies](constructive_solid_geometry.md) (CSG) - spôsobu tvorby telies. Okrem toho s operáciami <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [pracovného stola Dizajn dielu](PartDesign_Workbench.md) tvorí Náčrtník tiež základ metodológie [úpravy prvkov](feature_editing.md) pri tvorbe telies.

Pracovný stôl Náčrtník obsahuje \"väzby\", vďaka ktorým dokážete pomocou presných geometrických definícií ako dĺžky, uhla a vzťahov (vodorovnosť, zvislosť, kolmosť atď.) určiť umiestnenie 2d tvarov. Riešiteľ väzieb vypočíta rozsah väzieb 2D geometrie a poskytuje interaktívne prehliadanie stupňov voľnosti náčrtu.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width   *450px;"> 
*Plne zaväzbený náčrt*

## Základy používania väzieb náčrtu 

Pre lepšie pochopenie fungovania Náčrtníka môže pomôcť porovnanie s \"tradičným\" spôsobom rysovania.

#### Tradičné rysovanie 

Tradičné rysovanie v CAD programoch používa podobné techniky, ako [technické výkresy](https   *//sk.wikipedia.org/wiki/Technick%C3%BD_v%C3%BDkres). Jednotlivé pohľady sú kreslené manuálne a sú určené na tvorbu technických výkresov (modrotlač). Objekty sú kreslené presne pre zvolenú veľkosť alebo rozmer. Ak chcete nakresliť vodorovnú čiaru s dĺžkou 100 mm začínajúcu na (0,0), aktivujete nástroj čiara. Kliknete na obrazovku alebo zadáte súradnice (0,0) pre prvý bod, potom kliknete znovu alebo zadáte súradnice druhého bodu na (100,0). Alebo čiaru nakreslíte bez ohľadu na umiestnenie a presuniete ju neskôr. Po dokončení kreslenia geometrie jej priradíte rozmery.

#### Používanie väzieb náčrtu 

\"Náčrtník\" sa od tohto postupu odlišuje. Objekty nemusia byť nakreslené úplne presne, pretože ich neskôr definujete priradenými väzbami. Môžete ich nakresliť voľne a pokiaľ sú bez väzieb, môžu byť upravované. V podstate \"plávajú\" na kresliacej ploche a môžete ich presúvať, naťahovať, otáčať, škálovať apod. To vám v procese návrhu poskytuje veľkú voľnosť.

#### Čo sú väzby? 

Namiesto rozmerov sú väzby používané na obmedzenie stupňov voľnosti objektu. Napríklad čiara bez väzieb má 4 stupne voľnosti (skrátene SV, angl. DOF)   * môže byť posúvaná vodorovne alebo zvislo, môže byť natiahnutá a môže byť otočená.

Použitie vodorovnej alebo zvislej väzby alebo väzby uhla čiary (vzhľadom na inú čiaru alebo jednu z osí) obmedzí jej schopnosť otáčania, takže jej zostanú 3 stupne voľnosti. Zamknutie jedného z jej dvoch bodov vzhľadom na začiatok súradníc odstráni ďalšie 2 stupne voľnosti. A nakoniec použitie väzby rozmeru odstráni posledný stupeň voľnosti. Po týchto úkonoch je čiara považovaná za \"plne zaväzbenú\".

Objekty môžu byť takisto zaväzbené medzi sebou. Dve čiary môžete spojiť pomocou jedného z ich bodov vďaka väzbe splynutia bodov. Môže takisto medzi nimi byť nastavený úhol, alebo môžu nastavené ako kolmé. Čiara môže byť dotyčnicou oblúka alebo kruhu apod. Komplexný náčrt s viacerými objektami bude mať viac možných riešení a jeho \"plné zaväzbenie\" znamená, že bolo dosiahnuté práve jedno z týchto možných riešení v závislosti od použitých väzieb.

Existujú dva typy väzieb   * geometrické a rozmerové. Sú opísané nižšie v časti [\'Nástroje\'](#Nástroje.md).

#### Na čo Náčrtník slúžiť nemá 

Náčrtník neslúži na tvorbu 2D výkresov. Akonáhle boli náčrty použité na vytvorenie prvku telesa, sú automaticky skryté. Väzby sú viditeľné iba v upravovacom režime náčrtu.


<div class="mw-translate-fuzzy">

Ak chcete vytvárať iba 2D pohľady pre tlač a nie 3D modely, skúste použiť radšej [pracovný stôl Návrh](Draft_Workbench.md). Na rozdiel od prvkov v Náčrtníku nepoužívajú objekty v Návrhu väzby; sú to jednoduché tvary definované v okamihu ich tvorby. Návrh aj Náčrtník je možné použiť na kreslenie 2D geometrie a vytváranie 3D telies, hoci zmysel ich použitia je iný; Náčrtník sa bežne používa spolu s pracovnými stolmi [Diel](Part_Workbench.md) a [Tvorba dielu](PartDesign_Workbench.md) na vytváranie telies; Návrh sa bežne používa pre jednoduché rovinné výkresy s mriežkou, ako pri kreslení architektonického pôdorysu; v týchto situáciách sa Návrh väčšinou používa spolu s [pracovným stolom Arch](Arch_Workbench.md). Nástroj pracovného stola Návrh - [Návrh do náčrtu](Draft_Draft2Sketch.md) prevedie objekt Návrhu na objekt Náčrtu a späť; mnoho nástrojov, ktoré ako vstup vyžadujú 2D tvar, dokážu pracovať s oboma typmi objektov, keďže sa pri tom vykoná automatická interná konverzia.


</div>

## Pracovný postup pri náčrte 


<div class="mw-translate-fuzzy">

Náčrt je vždy dvojrozmerný (2D). Na vytvorenie telesa treba najprv vytvoriť 2D náčrt jednej uzavretej oblasti a ten potom vytiahnuť alebo obtočiť a tým pridať 3. rozmer, teda z 2D náčrtu vytvoriť 3D teleso.


</div>


<div class="mw-translate-fuzzy">

Ak náčrt obsahuje segmenty, ktoré sa križujú, miesta, na ktorých sa bod nenachádza priamo na nejakom segmente, alebo miesta, na ktorých sú medzery medzi koncovými bodmi priľahlých segmentov, teleso sa vytiahnutím alebo obtočením nevytvorí. Niekedy bude s jednoduchými operáciami typu vytiahnutie fungovať aj náčrt, ktorý obsahuje križujúce sa čiary, ale neskoršie operácie, napr. lineárny vzor, zlyhajú. Preto odporúčame vyhnúť sa križovaniu čiar. Výnimkou z tohto pravidla je použitie konštrukčnej (modrej) geometrie.


</div>


<div class="mw-translate-fuzzy">

Vo vnútri uzavretej oblasti sa môžu nachádzať aj menšie neprekrývajúce sa oblasti. Tieto sa pri tvorbe 3D telesa stanú prázdnym priestorom.


</div>


<div class="mw-translate-fuzzy">

Akonáhle je náčrt plne zaväzbený, prvky náčrtu sa prefarbia na zeleno; konštrukčná geometria zostane modrá. V tomto okamihu je náčrt spravidla \"dokončený\" a pripravený na tvorbu 3D telesa. Po zavretí dialógového okna náčrtu ale môže byť užitočné prejsť na <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [pracovný stôl Diel](Part_Workbench.md) a spustiť príkaz **[<img src=images/Part_CheckGeometry.svg style="width   *16px"> [Skontrolovať geometriu](Part_CheckGeometry.md)** a odhaliť potenciálne prvky náčrtu, ktoré by mohli neskôr spôsobiť problémy.


</div>

## Nástroje

Nástroje pracovného stola Náčrtník sa nachádzajú v menu Náčrt, ktoré sa objaví po nahraní pracovného sola Náčrtník.

### Všeobecné


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> [Nový náčrt](Sketcher_NewSketch.md)   * Vytvorí nový náčrt na vybranej ploche alebo rovine. Ak nie je pri spustení tohto nástroja vybraná žiadna plocha, užívateľ je vyzvaný zvoliť si z vyskakovacieho okna želanú rovinu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width   *32px;"> [Upraviť náčrt](Sketcher_EditSketch.md)   * Úprava zvoleného náčrtu. Otvorí sa [dialógové okno Náčrtníka](Sketcher_Dialog.md).


</div>

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width   *32px;"> [Opustiť náčrt](Sketcher_LeaveSketch.md)   * Ukončí režim úprav náčrtu.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width   *32px;"> [Zobraziť náčrt](Sketcher_ViewSketch.md)   * Nastaví zobrazenie modelu kolmo na rovinu náčrtu.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width   *32px;"> [Zobraziť rez](Sketcher_ViewSection.md)   * Vytvorí reznú rovinu a dočasne skryje akýkoľvek materiál nachádzajúci sa pred reznou rovinou.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width   *32px;"> [Namapovať náčrt na plochu](Sketcher_MapSketch.md)   * Namapuje náčrt na predtým vybranú plochu alebo teleso.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width   *32px;"> [Preorientovať náčrt](Sketcher_ReorientSketch.md)   * Umožní vám naviazať náčrt na jednu z hlavných rovín.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width   *32px;"> [Skontrolovať náčrt](Sketcher_ValidateSketch.md)   * Skontroluje toleranciu jednotlivých bodov a upraví ich.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width   *32px;"> [Zlúčiť náčrty](Sketcher_MergeSketches.md)   * Zlúči dva alebo viac náčrtov.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width   *32px;"> [Zrkadliť náčrt](Sketcher_MirrorSketch.md)   * Zrkadlí náčrt podľa osy x, y alebo podľa začiatku súradníc.

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width   *32px;"> [Zastaviť operáciu](Sketcher_StopOperation.md)   * V režime úprav zastaví aktuálnu operáciu, napr. kreslenie, nastavovanie väzieb apod.

### Geometria v Náčrtníku 

Tu sú uvedené nástroje pre tvorbu objektov.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width   *32px;"> [Bod](Sketcher_CreatePoint.md)   * Nakreslí bod.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width   *32px;"> [Čiara](Sketcher_CreateLine.md)   * Nakreslí čiarový segment medzi 2 bodmi. Pre potreby niektorých väzieb sa čiary považujú za nekonečne dlhé.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width   *48px;"> [Vytvoriť oblúk](Sketcher_CompCreateArc.md)   * Toto rozbaľovacie menu v lište nástrojov Náčrtníka obsahuje nasledovné príkazy   *

   ** <img alt="" src=images/Sketcher_CreateArc.svg  style="width   *32px;"> [Oblúk](Sketcher_CreateArc.md)   * Nakreslí segment oblúka pomocou stredového bodu, polomeru a začiatočného a koncového uhla.

   ** <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width   *32px;"> [Oblúk podľa 3 bodov](Sketcher_Create3PointArc.md)   * Nakreslí segment oblúka pomocou dvoch koncových bodov a ďalšieho bodu na obvode.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width   *48px;"> [Vytvoriť kruh](Sketcher_CompCreateCircle.md)   * Toto rozbaľovacie menu v lište nástrojov Náčrtníka obsahuje nasledovné príkazy   *

   ** <img alt="" src=images/Sketcher_CreateCircle.svg  style="width   *32px;"> [Kruh](Sketcher_CreateCircle.md)   * Nakreslí kruh pomocou stredového bodu a polomeru.

   ** <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width   *32px;"> [Kruh podľa 3 bodov](Sketcher_Create3PointCircle.md)   * Nakreslí kruh pomocou troch bodov na jeho obvode.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width   *48px;"> [Vytvoriť kužeľosečku](Sketcher_CompCreateConic.md)   * Náčrtník poskytuje nasledovné kužeľosečky. Na rozdiel od B-spline kriviek môžu byť použité v rozličných väzbách, ako napríklad [Dotyčnica](Sketcher_ConstrainTangent.md), [Bod na objekt](Sketcher_ConstrainPointOnObject.md) alebo [Kolmá väzba](Sketcher_ConstrainPerpendicular.md).
    -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width   *32px;"> [Elipsa podľa stredu](Sketcher_CreateEllipseByCenter.md)   * Nakreslí elipsu pomocou stredového bodu, bodu hlavného polomeru a bodu vedľajšieho polomeru.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width   *32px;"> [Elipsa podľa 3 bodov](Sketcher_CreateEllipseBy3Points.md)   * Nakreslí elipsu pomocou hlavného polomeru (2 body) a bodu vedľajšieho polomeru.
    -   <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width   *32px;"> [Oblúk elipsy](Sketcher_CreateArcOfEllipse.md)   * Nakreslí oblúk elipsy pomocou stredového bodu, bodu hlavného polomeru, začiatočného a koncového bodu.
    -   <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width   *32px;"> [Oblúk hyperboly](Sketcher_CreateArcOfHyperbola.md)   * Nakreslí oblúk hyperboly.
    -   <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width   *32px;"> [Oblúk paraboly](Sketcher_CreateArcOfParabola.md)   * Nakreslí oblúk paraboly.


</div>

   ** <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width   *32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md)   * Draws an ellipse by center point, major radius point and minor radius point.

   ** <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width   *32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md)   * Draws an ellipse by major diameter (2 points) and minor radius point.

   ** <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width   *32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md)   * Draws an arc of ellipse by center point, major radius point, starting point and ending point.

   ** <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width   *32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md)   * Draws an arc of hyperbola.

   ** <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width   *32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md)   * Draws an arc of parabola.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width   *48px;"> [Vytvoriť B-spline krivku](Sketcher_CompCreateBSpline.md)   * Toto rozbaľovacie menu v lište nástrojov Náčrtníka obsahuje nasledovné príkazy   *
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width   *32px;"> [Vytvoriť B-spline krivku](Sketcher_CreateBSpline.md)   * Nakreslí B-spline krivku pomocou jej kontrolných bodov.
    -   <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width   *32px;"> [Vytvoriť periodickú B-spline krivku](Sketcher_CreatePeriodicBSpline.md)   * Nakreslí periodickú (uzavretú) B-spline krivku pomocou jej kontrolných bodov.


</div>

   ** <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width   *32px;"> [B-spline](Sketcher_CreateBSpline.md)   * Draws a B-spline curve by its control points.

   ** <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width   *32px;"> [Periodic B-spline](Sketcher_CreatePeriodicBSpline.md)   * Draws a periodic (closed) B-spline curve by its control points.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width   *32px;"> [Lomená čiara (čiara s viacerými bodmi)](Sketcher_CreatePolyline.md)   * Nakreslí čiaru zloženú z viacerých segmentov. Pri kreslení lomenej čiary a stláčaní klávesy **M** preskakujete medzi jednotlivými štýlmi lomených čiar.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width   *48px;"> [Vytvoriť obdĺžniky](Sketcher_CompCreateRectangles.md)   * Toto rozbaľovacie menu v lište nástrojov Náčrtníka obsahuje nasledovné príkazy   * <small>(v0.20)</small> 


</div>

   ** <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width   *32px;"> [Obdĺžnik](Sketcher_CreateRectangle.md)   * Nakreslí obdĺžnik pomocou 2 protiľahlých bodov.


<div class="mw-translate-fuzzy">

   ** <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width   *32px;"> [Vycentrovaný obdĺžnik](Sketcher_CreateRectangle_Center.md)   * Nakreslí obĺdžnik pomocou stredového bodu a rohového bodu. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

   ** <img alt="" src=images/Sketcher_CreateOblong.svg  style="width   *32px;"> [Zaoblený obĺdžnik](Sketcher_CreateOblong.md)   * Nakreslí zaoblený obĺdžnik z dvoch protiľahlých bodov. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width   *48px;"> [Vytvoriť pravidelný mnohouholník](Sketcher_CompCreateRegularPolygon.md)   * Toto rozbaľovacie menu v lište nástrojov Náčrtníka obsahuje nasledovné príkazy   *


</div>

   ** <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width   *32px;"> [Trojuholník](Sketcher_CreateTriangle.md)   * Nakreslí pravidelný trojuholník vpísaný do kružnice v konštrukčnej geometrii.

   ** <img alt="" src=images/Sketcher_CreateSquare.svg  style="width   *32px;"> [Štvorec](Sketcher_CreateSquare.md)   * Nakreslí pravidelný štvorec vpísaný do kružnice v konštrukčnej geometrii.

   ** <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width   *32px;"> [Päťuholník](Sketcher_CreatePentagon.md)   * Nakreslí pravidelný päťuholník vpísaný do kružnice v konštrukčnej geometrii.

   ** <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width   *32px;"> [Šesťuholník](Sketcher_CreateHexagon.md)   * Nakreslí pravidelný šesťuholník vpísaný do kružnice v konštrukčnej geometrii.

   ** <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width   *32px;"> [Sedemuholník](Sketcher_CreateHeptagon.md)   * Nakreslí pravidelný sedemuholník vpísaný do kružnice v konštrukčnej geometrii.

   ** <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width   *32px;"> [Osemuholník](Sketcher_CreateOctagon.md)   * Nakreslí pravidelný osemuholník vpísaný do kružnice v konštrukčnej geometrii.


<div class="mw-translate-fuzzy">

   ** <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width   *32px;"> [Vytvoriť pravidelný mnohouholník](Sketcher_CreateRegularPolygon.md)   * Nakreslí pravidelný mnohouholník pomocou voľby počtu strán a výberom dvoch bodov   * stredu a jedného rohu.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width   *32px;"> [Drážka](Sketcher_CreateSlot.md)   * Nakreslí ovál pomocou stredu jedného polkruhu a koncového bodu druhého polkruhu.

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width   *48px;"> [Create a fillet](Sketcher_CompCreateFillets.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   *


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width   *32px;"> [Zaoblenie](Sketcher_CreateFillet.md)   * Medzi dvomi čiarami spojenými bodom vytvorí zaoblenie. Vyberte obe čiary alebo rohový bod a potom aktivujte nástroj.


</div>

   ** <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width   *32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md)   * Creates a fillet between two non-parallel lines while preserving their (virtual) intersection.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width   *32px;"> [Orezanie](Sketcher_Trimming.md)   * Oreže čiaru, kruh alebo oblúk podľa zvoleného bodu.


</div>

-   <img alt="" src=images/Sketcher_Extend.svg  style="width   *32px;"> [Predĺženie](Sketcher_Extend.md)   * Predĺži čiaru alebo oblúk až po hraničnú čiaru, oblúk, elipsu, oblúk elipsy alebo bod v priestore.

-   <img alt="" src=images/Sketcher_Split.svg  style="width   *32px;"> [Rozdelenie](Sketcher_Split.md)   * Rozdelí čiaru alebo oblúk na dve časti, premení kruh na oblúk pri zachovaní väčšiny väzieb. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width   *32px;"> [Vonkajšia geometria](Sketcher_External.md)   * Vytvorí hranu spojenú s vonjakšou geometriou.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width   *32px;"> [Presná kópia](Sketcher_CarbonCopy.md)   * Skopíruje geometriu iného náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width   *32px;"> [Konštrukčný režim](Sketcher_ToggleConstruction.md)   * Prepne geometriu náčrtu z/do konštrukčného režimu. Konštrukčná geometria je sfarbená na modro a mimo režim úprav náčrtu je neviditeľná.


</div>

### Väzby v Náčrtníku 

Väzby sa používajú na definovanie dĺžok, nastavenie pravidiel medzi súčasťami náčrtu a na ukotvenie náčrtu vzhľadom na vodorovnú a zvislú os. Niektoré väzby vyžadujú [Pomocné väzby](Sketcher_helper_constraint.md).

#### Geometrické väzby 

Tieto väzby nie sú spojené s číselnými dátami.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *32px;"> [Splynutie](Sketcher_ConstrainCoincident.md)   * Pripojí bod na jeden alebo viacero iných bodov.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *32px;"> [Bod na objekt](Sketcher_ConstrainPointOnObject.md)   * Pripojí bod na iný objekt typu čiara, oblúk alebo os.


</div>

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width   *32px;"> [Zvislá väzba](Sketcher_ConstrainVertical.md)   * Zaväzbí vybrané čiary alebo elementy lomených čiar do presne zvislej polohy. Pred aplikovaním tejto väzby môžete vybrať jeden alebo viac objektov.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width   *32px;"> [Vodorovná väzba](Sketcher_ConstrainHorizontal.md)   * Zaväzbí vybrané čiary alebo elementy lomených čiar do presne vodorovnej polohy. Pred aplikovaním tejto väzby môžete vybrať jeden alebo viac objektov.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width   *32px;"> [Rovnobežná väzba](Sketcher_ConstrainParallel.md)   * Zaväzbí dve alebo viac číar tak, aby boli rovnobežné.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width   *32px;"> [Kolmá väzba](Sketcher_ConstrainPerpendicular.md)   * Zaväzbí dve čiary tak, aby boli na seba kolmé, alebo zaväzbí čiaru kolmo na koncový bod oblúka.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width   *32px;"> [Väzba dotyčnice](Sketcher_ConstrainTangent.md)   * Medzi dvomi vybranými objektami vytvorí väzbu dotyčnice, alebo kolineárnu väzbu medzi dvomi čiarovými segmentami. Čiarový segment nemusí nutne ležať priamo na oblúku alebo kruhu, aby mohol s týmto oblúkom alebo kruhom vytvárať väzbu dotyčnice.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width   *32px;"> [Väzba zhodnosti](Sketcher_ConstrainEqual.md)   * Zaväzbí dva vybrané objekty tak, aby boli zhodné. Ak ju použijete na kruhy alebo oblúky, ich polomery sa budú zhodovať.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *32px;"> [Väzba symetrie](Sketcher_ConstrainSymmetric.md)   * Zaväzbí dva body symetricky k čiare, alebo zaväzbí prvé dva vybrané body symetricky k tretiemu vybranému bodu.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width   *32px;"> [Blokovacia väzba](Sketcher_ConstrainBlock.md)   * Zablokuje hranu a znemožní jej posun, to znamená, že neumožní jej vrcholom zmeniť umiestnenie. Hodí sa napríklad na ukotvenie pozície B-Spline kriviek. Viď [príspevok na fóre o blokovacej väzbe](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Väzby rozmerov 

Tieto väzby sú spojené s číselnými dátami a môžete v nich použiť [matematické výrazy](Expressions.md). Dáta môžu pochádzať aj z [tabuľky](Spreadsheet_Workbench.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width   *32px;"> [Zámok](Sketcher_ConstrainLock.md)   * Zaväzbí vybraný objekt nastavením jeho zvislej a vodorovnej vzdialenosti od začiatku súradníc, čím v podstate uzamkne umiestnenie objektu. Tieto väzobné vzdialenosti je možné následne upraviť.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width   *32px;"> [Vodorovná vzdialenosť](Sketcher_ConstrainDistanceX.md)   * Nastaví vodorovnú vzdialenosť medzi dvomi bodmi alebo koncovými bodmi čiary. Ak je vybraný len jeden objekt, je vzdialenosť nastavená voči začiatku súradníc.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width   *32px;"> [Zvislá vzdialenosť](Sketcher_ConstrainDistanceY.md)   * Nastaví zvislú vzdialenosť medzi dvomi bodmi alebo koncovými bodmi čiary. Ak je vybraný len jeden objekt, je vzdialenosť nastavená voči začiatku súradníc.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width   *32px;"> [Vzdialenosť](Sketcher_ConstrainDistance.md)   * Definuje vzdialenosť vybranej čiary zaväzbením jej dĺžky, alebo definuje vzdialenosť medzi dvomi bodmi zaväzbením ich vzájomnej vzdialenosti.

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width   *48px;"> [Arc or circle](Sketcher_CompConstrainRadDia.md)   * This is an icon menu in the Sketcher constraints toolbar that holds the following commands   *


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width   *32px;"> [Polomer](Sketcher_ConstrainRadius.md)   * Zaväzbí polomer vybraného oblúka alebo kruhu určením jeho konkrétnej hodnoty.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width   *32px;"> [Priemer](Sketcher_ConstrainDiameter.md)   * Zaväzbí priemer vybraného oblúka alebo kruhu určením jeho konkrétnej hodnoty.
-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width   *32px;"> [ Automatické zaväzbenie polomeru/priemeru](Sketcher_ConstrainRadiam.md)   * Automaticky definuje polomer/priemer vybraného oblúka alebo kruhu (váhu riadiaceho bodu B-spline krivky, priemer kompletného kruhu, polomer oblúka) <small>(v0.20)</small> 
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width   *32px;"> [Uhol](Sketcher_ConstrainAngle.md)   * Definuje interný uhol medzi dvomi vybranými čiarami.


</div>

   ** <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width   *32px;"> [Diameter](Sketcher_ConstrainDiameter.md)   * Defines the diameter of a selected arc or circle by constraining the diameter.

   ** <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width   *32px;"> [Radiam](Sketcher_ConstrainRadiam.md)   * Automatically defines radius/diameter of a selected arc or circle (weight for a B-spline pole, diameter for a complete circle, radius for an arc). <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width   *32px;"> [Angle](Sketcher_ConstrainAngle.md)   * Defines the internal angle between two selected lines.

#### Špeciálne väzby 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width   *32px;"> [Snellov zákon](Sketcher_ConstrainSnellsLaw.md)   * Zaväzbí dve čiary tak, aby dodržiavali zákon lomu a simulovali prechod svetla cez optické rozhranie.


</div>

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width   *32px;"> [Vnútorné zarovnanie](Sketcher_ConstrainInternalAlignment.md)   * Zarovná vybrané elementy k zvolenému tvaru (napr. čiara sa stane hlavnou osou elipsy).

#### Nástroje väzieb 

Efekty väzieb je možné meniť nasledovnými nástrojmi   *

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width   *32px;"> [Prepnúť riadiacu/referenčnú väzbu](Sketcher_ToggleDrivingConstraint.md)   * Prepne lištu nástrojov alebo zvolenú väzbu do/z referenčného stavu.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width   *32px;"> [Aktivovať/dekativovať väzbu](Sketcher_ToggleActiveConstraint.md)   * Zapne alebo vypne už umiestnenú väzbu. <small>(v0.19)</small> 


</div>

### Nástroje Náčrtníka 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width   *32px;"> [Select solver DOFs](Sketcher_SelectElementsWithDoFs.md)   * Zelenou farbou označí geometrické elementy, pri ktorých riešiteľ stále ukazuje nezaväzbené stupne voľnosti.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width   *32px;"> [Uzavrieť tvar](Sketcher_CloseShape.md)   * Vytvorí uzavretý tvar aplikovaním väzieb splynutia na koncové body.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width   *32px;"> [Spojiť hrany](Sketcher_ConnectLines.md)   * Spojí elementy náčrtu aplikovaním väzieb splynutia na koncové body.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width   *32px;"> [Vybrať väzby](Sketcher_SelectConstraints.md)   * Vyberie väzby elementu náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width   *32px;"> [Vybrať elementy spojené s väzbami](Sketcher_SelectElementsAssociatedWithConstraints.md)   * Vyberie elementy náčrtu spojené s väzbami.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width   *32px;"> [Vybrať nadbytočné väzby](Sketcher_SelectRedundantConstraints.md)   * Vyberie nadbytočné väzby náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width   *32px;"> [Vybrať konfliktné väzby](Sketcher_SelectConflictingConstraints.md)   * Vyberie konfliktné väzby náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width   *32px;"> [Zobraziť/skryť vnútornú geometriu](Sketcher_RestoreInternalAlignmentGeometry.md)   * Znovu vytvorí chýbajúcu/zmaže nepotrebnú vnútornú geometriu vybraného kruhu, oblúka elipsy/hyperboly/paraboly alebo B-spline krivky.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width   *32px;"> [Vybrať začiatok súradníc](Sketcher_SelectOrigin.md)   * Vyberie začiatok súradníc náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width   *32px;"> [Vybrať zvislú os](Sketcher_SelectVerticalAxis.md)   * Vyberie zvislú os náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width   *32px;"> [Vybrať vodorovnú os](Sketcher_SelectHorizontalAxis.md)   * Vyberie vodorovnú os náčrtu.


</div>

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width   *32px;"> [Symetria](Sketcher_Symmetry.md)   * Skopíruje element náčrtu symetricky ku zvolenej čiare.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width   *32px;"> [Klon](Sketcher_Clone.md)   * Vytvorí klon elementu náčrtu s prepojením na originál.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width   *32px;"> [Kópia](Sketcher_Copy.md)   * Vytvorí kópiu elementu náčrtu bez prepojenia na originál.

-   <img alt="" src=images/Sketcher_Move.svg  style="width   *32px;"> [Presun](Sketcher_Move.md)   * Presunie vybranú geometriu podľa posledného vybraného bodu.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width   *32px;"> [Obdĺžnikové pole](Sketcher_RectangularArray.md)   * Vytvorí pole z vybraných elementov náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width   *32px;"> [Odstrániť zarovnanie k osám](Sketcher_RemoveAxesAlignment.md)   * Odstráni zarovnanie k osám a zároveň sa pokúsi zachovať vzťah väzieb výberu. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width   *32px;"> [Zmazať všetku geometriu](Sketcher_DeleteAllGeometry.md)   * Zmaže všetku geometriu v náčrte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width   *32px;"> [Zmazať všetky väzby](Sketcher_DeleteAllConstraints.md)   * Zmaže všetky väzby z náčrtu.


</div>

### Nástroje B-spline kriviek Náčrtníka 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width   *32px;"> [Zobraziť/skryť stupeň B-spline krivky](Sketcher_BSplineDegree.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width   *32px;"> [Zobraziť/skryť kontrolný polygón B-spline krivky](Sketcher_BSplinePolygon.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width   *32px;"> [Zobraziť/skryť hrebeň zakrivenia B-spline krivky](Sketcher_BSplineComb.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width   *32px;"> [Zobraziť/skryť násobnosť uzla B-spline krivky](Sketcher_BSplineKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width   *32px;"> [Zobraziť/skryť váhu kontrolných bodov B-spline krivky](Sketcher_BSplinePoleWeight.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width   *32px;"> [Konvertovať geometriu na B-spline krivku](Sketcher_BSplineApproximate.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width   *32px;"> [Zvýšiť stupeň B-spline krivky](Sketcher_BSplineIncreaseDegree.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width   *32px;"> [Znížiť stupeň B-spline krivky](Sketcher_BSplineDecreaseDegree.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width   *32px;"> [Zvýšiť násobnosť uzla](Sketcher_BSplineIncreaseKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width   *32px;"> [Znížiť násobnosť uzla](Sketcher_BSplineDecreaseKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width   *32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md), <small>(v0.20)</small> 

### Virtuálny priestor Náčrtníka 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width   *32px;"> [Prepnúť virtuálny priestor](Sketcher_SwitchVirtualSpace.md)   * Umožní vám skryť všetky väzby náčrtu a potom ich znovu zobraziť.


</div>

## Predvoľby

-   <img alt="" src=images/Preferences-general.svg  style="width   *32px;"> [Predvoľby](Sketcher_Preferences.md)   * Predvoľby pracovného stola \"Náčrtník\".

## Osvedčené postupy 

Každý CAD používateľ si priebežne vytvára vlastný pracovný postup, ale existujú určité osvedčené postupy, ktoré je dobré zachovávať.


<div class="mw-translate-fuzzy">

-   Séria jednoduchých náčrtov sa spravuje ľahšie, ako jeden komplexný náčrt. Napríklad prvý náčrt môžete vytvoriť pre základný 3D prvok (napríklad pomocou vytiahnutia alebo obtočenia), zatiaľ čo druhý môžete použiť na vytvorenie dier alebo výrezov (kapies). Niektoré detaily môžete vynechať a vytvoriť ich neskôr ako 3D prvky. Môžete v náčrte takisto vynechať zaoblenia, ak ich obsahuje príliš veľa, pričom ich neskôr pridáte ako 3D prvky.
-   Vždy vytvárajte uzavretý profil, inak z vášho náčrtu nebudete môcť vytvoriť teleso, ale iba súbor otvorených plôch. Ak nechcete, aby boli niektoré objekty zahrnuté do tvorby telesa, zmeňte ich pomocou nástroja Konštrukčný režim na konštrukčné elementy.
-   Aby ste nemuseli všetky väzby vytvárať manuálne, môžete na niektoré elementy použiť ich automatické vytváranie.
-   Vo všeobecnosti platí, že najprv by ste mali aplikovať geometrické väzby, potom väzby rozmerov a na koniec celý náčrt uzamknúť. Ale zapamätajte si   * pravidlá sú často na to, aby sa porušovali. Ak máte problém manipulovať s náčrtom, môže byť vhodné niektoré objekty zaväzbiť, než celý náčrt dokončíte.
-   Ak sa dá, vycentrujte náčrt k začiatku súradníc (0,0) pomocou väzby Zámok. Ak náčrt nie je symetrický, zaväzbite jeden z jeho bodov k začiatku súradníc, alebo si pre väzby vzdialeností zvoľte okrúhle čísla. Vo verzii 0.12 nie sú externé väzby (umožňujúce zaväzbiť náčrt k existujúcej 3D geometrii, ako napríklad hranám či iným náčrtom) ešte implementované. To znamená, že naviazanie geometrie náčrtu k predchádzajúcemu náčrtu musíte vykonať manuálne nastavením vzdialeností od predchádzajúceho náčrtu. Väzba zámku (25,75) od začiatku súradníc sa určite pamätá lepšie, než (23.47,73.02).
-   Ak máte možnosť výberu medzi väzbou dĺžky a väzbami vodorovnej/zvislej vzdialenosti, použite radšej tie druhé. Väzby vodorodnej a zvislej vzdialenosti sä výpočetne jednoduchšie.
-   Vo všeobecnosti sú najlepšie väzby tieto   * vodorovná a zvislá vzdialenosť, vodorovná a zvislá dĺžka, dotyčnica bod-na-bod. Ak je to možné, obmedzte použitie týchto väzieb   * všeobecná väzba dĺžky; dotyčnica hrana-na-hranu; väzba bodu na čiaru; väzba symetrie.
-   Ak máte pochybnosti o platnosti náčrtu po jeho ukončení (prvky sú vysvietené nazeleno), zavrite dialógové okno Náčrtníka, prepnite sa na <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [pracovný stôl Dielec](Part_Workbench.md) a spustite príkaz **[<img src=images/Part_CheckGeometry.svg style="width   *16px"> [Skontrolovať geomegriu](Part_CheckGeometry.md)**.


</div>

## Návody


<div class="mw-translate-fuzzy">

-   [Sketcher tutorial](https   *//forum.freecadweb.org/viewtopic.php) od autora chrisb. Toto je 70-stranový PDF dokument, ktorý slúži ako detailný návod na použitie Náčrtníka. Vysvetľuje základy použitia Náčrtníka a poskytuje veľa detailov o tvorbe geometrických tvarov a všetkých druhov väzieb.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) pre začiatočníkov
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimálne požiadavky na náčrt a úplné určenie náčrtu.


</div>

## Skriptovanie

Stránka [Skriptovanie v Náčrtníku](Sketcher_scripting.md) obsahuje príklady vytvárania väzieb pomocou skriptov v jazyku Python.





{{Sketcher_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/sk
