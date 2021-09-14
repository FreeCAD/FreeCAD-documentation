# Fasteners Workbench/pl



<img alt="Ikonka FreeCAD dla środowiska Elementów złącznych" src=images/Fasteners_workbench_icon.svg  style="width:128px;">


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementów złącznych](Fasteners_Workbench.md) należy do [zewnętrznych środowisk pracy](External_workbenches/pl.md). Jest ono przeznaczone do łatwego, szybkiego i wygodnego dodawania / łączenia różnych elementów złącznych z częściami.

## Użycie

Użycie jest całkiem proste:

1.  Zainstaluj środowisko Elementów Złącznych poprzez [Menadżer dodatków](Std_AddonMgr/pl.md).
2.  Rozpocznij nowy dokument w programie FreeCAD.
3.  Wybierz środowisko <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementów Złącznych](Fasteners_Workbench/pl.md) z [listy menu rozwijanego](Std_Workbench/pl.md).
4.  Na pasku narzędzi pojawi się seria śrub *(patrz [Pasek narzędzi Elementów złącznych](#Pasek_narz.C4.99dzi_Element.C3.B3w_z.C5.82.C4.85cznych.md) poniżej)*.

Proste użycie: Kliknięcie na dowolną śrubę spowoduje utworzenie tej śruby w punkcie odniesienie położenia z domyślnymi właściwościami. Aby zmienić rozmiar / długość wybierz nowo utworzoną śrubę, następnie przejdź do zakładki **Dane** w [panelu właściwości](Property_editor/pl.md).

## Znane problemy 

-   Inne problemy / prośby o funkcje można znaleźć na stronie [Fastener Workbench GitHub issue queue](https://github.com/shaise/FreeCAD_FastenersWB/issues?utf8=✓&q=is%3Aissue)

## Bibliografia

-   Autor: [shaise](http://theseger.com/projects/author/shaise/)
    -   ScrewMaker: Ulrich Brammer
    -   Workbench wrapper: Shai Seger
-   Strona domowa: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Kod źródłowy na Github: <https://github.com/shaise/FreeCAD_FastenersWB>

## Instalacja

To środowisko pracy może być zainstalowane z <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;">. [Menadżera dodatków](Std_AddonMgr.md). Aby zainstalować go ręcznie zobacz stronę [Instalacja zewnętrznych środowisk pracy](Installing_more_workbenches/pl.md).

### Pasek narzędzi 

Środowisko pracy Elementy Złączne posiada dwa paski narzędzi. Pasek narzędzi **FS Screws** zawiera wiele narzędzi. W razie potrzeby można go rozwinąć, naciskając przycisk **&gt;&gt;**.

![](images/Fasteners_toolbars.png ) *Paski narzędzi środowiska Element złączne*

## Przybory

Szczegółowy opis znajduje się na stronie [domowej](http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/)

### Polecenia

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Odwróć](Fasteners_Flip.md): odwrócenie orientacji.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Przenieś](Fasteners_Move/pl.md): przeniesienie do nowej lokalizacji.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Kształt](Fasteners_Shape/pl.md): zmień obiekt na prosty kształt nieparametryczny.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Typ dopasowania Wewnętrzny](Fasteners_MatchTypeInner/pl.md): Dopasowanie śrub według wewnętrznej średnicy gwintu *(otworu gwintowanego)*.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Typ dopasowania Zewnętrzny](Fasteners_MatchTypeOuter/pl.md): dopasowanie śruby do średnicy gwintu zewnętrznego *(pasowanie otworu)*.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [BOM](Fasteners_BOM/pl.md): generuje zestawienie materiałowe.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Kalkulator śrub](Fasteners_ScrewCalculator/pl.md): pokaż kalkulator otworów pod śruby.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Fazka otworu](Fasteners_ChamferHole/pl.md): sfazowanie otworów pod wkręty z łbem stożkowym.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Zmiana parametrów](Fasteners_ChangeParameters/pl.md): umożliwia dokonanie zmian parametrów wybranych elementów złącznych.

### Samokontrujące elementy złączne i elementy złączne do PCB 

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Nakrętka metryczna samokontrująca.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Dystans metryczny samozaciskowy.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Samozaciskowy kołek metryczny.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> **PCB** Dystans metryczny męski/żeński.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> **PCB** Przekładka metryczna żeńska/żeńska.

### Elementy złączne DIN, EN oraz ISO 

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> **ISO 4017** Śruba z łbem sześciokątnym. Klasy produktów A i B.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> **ISO 4014** Śruba z łbem sześciokątnym. Klasy produktów A i B.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Śruba z łbem sześciokątnym z kołnierzem, seria mała.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Śruba sześciokątna z kołnierzem, seria gruba.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Śruba z gniazdem sześciokątnym z niskim łbem.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Śruba z łbem o gnieździe sześciokątnym z niskim łbem i środkiem.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Śruba z łbem kulistym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Śruba z łbem kulistym z gniazdem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Śruba z łbem stożkowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> **ISO 2009** Śruba z łbem płaskim z rowkiem stożkowym. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> **ISO 2010** Śruba z łbem wpuszczanym z podwyższonym rowkiem. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> **ISO 1580** Śruba z łbem walcowym z rowkiem. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> **ISO 1207** Śruba z łbem serowym z rowkiem. Produkt klasy A.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Śruba z łbem wpuszczanym krzyżowym z kołnierzem.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> **ISO 7045** Śruba z łbem walcowym typu H z wgłębieniem krzyżowym. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> **ISO 7046** Śruba z łbem stożkowym płaskim H z wgłębieniem krzyżowym. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> **ISO 7047** Śruba z łbem stożkowym podniesionym H z wgłębieniem krzyżowym. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Śruba z łbem serowym z wgłębieniem krzyżowym typu H.

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Śruba z łbem stożkowym z gniazdem sześciokątnym, wysoki łeb.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Śruba z łbem stożkowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Podkładka ślizgowa, seria normalna. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> **ISO 7090** Podkładka ślizgowa fazowana, seria normalna. Gatunek produktu A.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Podkładka zwykła, seria mała.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Podkładka ślizgowa, seria duża. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Podkładka zwykła, seria ekstra duża.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Śruba z gniazdem sześciokątnym z płaskim czubkiem.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Śruba z gniazdem sześciokątnym z czopem stożkowym.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> **ISO 4032** Nakrętka sześciokątna, styl 1. *Klasy produktów A i B.*.

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> **ISO 4033** Nakrętka sześciokątna, styl 2. *Klasy produktów A i B.*.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> **ISO 4035** Nakrętka sześciokątna cienka, fazowana. Gatunek produktu A i B.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Nakrętka sześciokątna z kołnierzem.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Nakrętka czworokątna.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Nakrętka czworokątna.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Nakrętka Nyloc.

### Elementy złączne ASME 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Śruba z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Śruba z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Nakrętka do śruby maszynowej.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Nakrętka sześciokątna.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Nakrętka sześciokątna cienka.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Śruba z łbem stożkowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Śruba z łbem kulistym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Śruba z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Śruba z gniazdem sześciokątnym z płaskim czubkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Śruba z gniazdem sześciokątnym z czopem stożkowym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC śruba z łbem płaskim z rowkiem stożkowym.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN podkładka, seria wąska.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN podkładka, seria regularna.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN podkładka, seria szeroka.

### Elementy złączne różne 

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Pręt gwintowany o dowolnej długości do gwintowania otworów *(metryczny)*.

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Pręt gwintowany o dowolnej długości do gwintowania otworów *(calowy)*.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Rura gwintowana o dowolnej długości do nacinania gwintów zewnętrznych *(metrycznych)*.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Rura gwintowana o dowolnej długości do nacinania gwintów zewnętrznych *(calowych)*.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Pręt gwintowany **DIN 975** o dowolnej długości *(metryczny)*.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Pręt gwintowany **DIN 975** o dowolnej długości *(calowy)*.

## Pozostałe

-   <img alt="" src=images/preferences-fasteners.svg  style="width:32px;"> 
**Preferencje środowiska Elementy złączne**
-   <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:32px;"> 
**ikonka środowiska Elementy złączne**

## Odnośniki internetowe dla środowiska 

-   Wiki na temat tego środowiska pracy: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Wiki dla FreeCAD: <https://www.freecadweb.org/wiki/Fasteners_Workbench>
-   Forum FreeCAD: <https://forum.freecadweb.org/viewtopic.php?t=11429>
-   Poradniki - jak używać: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Wideo:
-   Pliki:
-   Zgłaszanie błędów: Proszę zgłaszać błędy na <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Instalacja: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>

## Inne użyteczne odnośniki 

-   [Generowanie otworów pod wkręty z łbem stożkowym z użyciem programu FreeCAD.](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [ŚRUBY](https://github.com/jreinhardt/BOLTS): Otwarta biblioteka dla specyfikacji technicznych
-   [Środowiska zewnętrzne](External_workbenches/pl.md)
-   [Przepisy na makropolecenia](Macros_recipes/pl.md)



[Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md) [Category:External Workbenches](Category:External_Workbenches.md) [Category:Fasteners](Category:Fasteners.md)
