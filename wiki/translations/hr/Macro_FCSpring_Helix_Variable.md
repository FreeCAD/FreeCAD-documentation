# Macro FCSpring Helix Variable/hr
 {{Macro/hr
|Name=Macro FCSpring Helix Variable
|Translate=Makro FCSpring Helix Variable
|Icon=FCSpring Helix Variable.png
|Description=Stvara oprugu s varijablom heliksa.<br/>Otkriveni su: Površina (smjer lica), Cilindar (radijus), elipsa (MinorRadius), sfera (radijus), toroid (radijus1), ravnina (smjer), crta (slijedite smjer), točka (položaj vrha XYZ) <br / > Ako nije otkriven nijedan objekt (nije odabir), opruga se stvara u točki XYZ 0., 0., 0.<br / >See the [https://www.freecadweb.org/wiki/Macro_FCSpring_Helix_Variable/hr#Primjeri Primjeri]
|Author=Mario52
|Version=01.17
|Date=2020/11/12
|Download=Download the [https://forum.freecadweb.org/download/file.php?id=80844 the Icons] in .zip file 
|FCVersion=0.19
}}


<div class="mw-translate-fuzzy">

## Opis

Ova makronaredba stvara proljeće s prilagodljivim, svaki okret može promijeniti proljetnu konfiguraciju koja se može spremiti u datoteku s ekstenzijom **.FCSpring**
Otkriveni su: Površina (smjer lica), Cilindar (radijus), elipsa (MinorRadius), sfera (radijus), toroid (radijus1), ravnina (smjer), crta (slijedite smjer), točka (položaj vrha XYZ)
Ako nije otkriven nijedan objekt (nije odabir), opruga se stvara u točki XYZ 0., 0., 0.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/68c81c32a0727a693d3a/raw/5906d5d10c1d9c2b20dc34aa2a28a2634f2a49ba/Macro_FCSpring_Helix_Variable.FCMacro}}

<img alt="" src=images/TruncateSpring00.png  style="width:400px;"> 
*FCSpring Helix Variable*

## Upotreba

Ovaj odjeljak služi za konfiguraciju opruge

Shematski detalj konfiguracije opruga

![](images/Macro_TruncateSpring_01.png ) 

#### **GUI**

![](images/Macro_FCSpring_Helix_Variable_01.png ) 

#### **Prvi dio, konfiguracija opruge** 

-    {{SpinBox|10 coils}}**Number of coil** : Ukupno zavojnice na oprugu. Zadano = 10

-    {{SpinBox|20,000 mm}}**Radius of spring** : Radijus opruge. Zadano = 20.0

-    {{SpinBox|15,000 mm}}**Pitch of spring** : Smjer opće opruge. Zadano = 15.0

-    {{SpinBox|5 ( 72 points )}}**Precision of turn** : Preciznost okretanja preciznost odgovara broju točaka za 1 okretanje zavojnice i izračunava se: preciznost (broj točaka) = (pitch / (360 / preciznost)). Zadano = 5 (72 boda)

-    {{SpinBox|20,000 mm}}: A kúp nagy körének sugara (ellenőrizze a {{CheckBox|TRUE|Spring conical}} használatra)

-   **Spring conical** : Dajte velikom promjeru konusa što će dimenzija uvijek biti veća od radijusa

-    {{CheckBox|Angles}}: Odabir potvrdnog okvira za aktiviranje funkcije Početak i kraj kuta zavojnice prema početnim postavkama nije
    . Ako je funkcija označena, točnost se automatski postavlja na 1 (360 bodova po okretu 1 bod = 1 stupanj)

-    {{SpinBox|0 deg}}**Begin** : Započnite kut prve zavojnice opruge.

-    {{SpinBox|360 deg}}**End** : Završni kut posljednje zavojnice opruge.

![](images/Macro_FCSpring_Helix_Variable_02.png ) 

#### **Drugi odjeljak, upišite redak** 

-    {{RadioButton|TRUE|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}**BSpline**: Upišite liniju BSpline.

-    {{RadioButton|<img src="images/Draft_Wire.svg" width=24px> Wire}}**Wire**: Upišite line Wire.

-    {{CheckBox|<img src="images/Draft_Point.svg" width=24px> Points}}**Points**: Označite potvrdni okvir ako je potvrdni okvir aktiviran.

-    {{CheckBox|Reverse}}**Reverse**: Oznaka obrnuto ako je potvrdni okvir aktiviran, smjer proljeća mijenja

![](images/Macro_FCSpring_Helix_Variable_03.png ) 

#### **Treći odjeljak, odabir** 

Ovaj je odjeljak prikazan ako je odabran objekt. Objekt tipa je prikazan u uređivaču teksta

Objekt može biti linija, 2 boda, krug, žica \... jedna osa se automatski stvara duljina opruge

Otkrivanje: cilindar (radijus), sfera (radijus), toroid (radijus), konus (mali radijus), krug (radijus), luk (radijus), elipsa (mali radijus)

-    **Normal****Norm.**: Ako je odabran jedan krug **Norm** ne mijenja radijus kruga (zadano)

    -   
        **Adapt Rad.**
        
        : Ha megnyomja a **Normal** \'gombot, akkor a gomb {{Button | Adapt Rad.}} Értékre vált. A rugót az érzékelt sugarahoz igazítják (Ha egy sugarat érzékelnek)

-    **Point Mouse**: Ako je miš na jednom licu, proljeće je na ovoj točki (zadano)

    -   
        **Center Face**
        
        : Ha megnyomja a **Point Mouse** gombot, akkor a gomb **Center Face** értékre változik, és a rugó a kiválasztott középső felületre jön létre.

-    {{CheckBox|Position}}**Položaj**: Ako se odaberu dva objekta (prva os, drugo proljeće), ovaj checkBox je omogućen i možete izmijeniti objekt 2 položaja (opruga) duž objekta 1 (os)

-    **Circle**: Ako su tri točke kliknute mišem, gumb **Circle** je omogućen i moguće je stvoriti krug koji može poslužiti kao baza za proljeće

![](images/Macro_FCSpring_Helix_Variable_02_1.png ) 

#### Position (0)(xx)\'\' 

(0)(xx) : Odabir broja, duljina u mm stvorene osi x 10, tj. Broj točaka za pomicanje opruge osi

-    **Begin/End**: Postavite oprugu na početnu, srednju i krajnju os

-    **Reverse Spr.**: Okrenite oprugu osi

-    {{SpinBox|0,1 mm}}: Pomicanje opruge s preciznošću (0,1 mm) duž svoje osi

-    **Reverse Count.**: Obrnuti brojač ex: Početak 0 do 10 .. ili Kraj 0 do 10 ..

-   **Slider**: Postavite oprugu na njegovu os

![](images/Macro_FCSpring_Helix_Variable_02_2.png ) 

#### Četiri dijela, zavojnica posebne duljine 

-    {{SpinBox|Num: 2}}**Numbering of coil** : Numeriranje zavojnice za izmjenu. (Zadano : none)

-    {{CheckBox|Smoothing}}**Smoothing** Ovaj checkBox otkriva jedan spinBox za određivanje stupnja izglađivanja maksimalna vrijednost je vrijednost preciznosti -1 (ova opcija je još uvijek u fazi prototipa i rezultat može biti zadovoljavajući ili potpuno pogrešan)

-    {{SpinBox|0,000 mm}}**Pitch of coil** : Smjestite zavojnicu za izmjenu. (Defaut: nitko)

-    **15.0 mm**: Ako se pritisne tipka, na vrijednost \"Pitch of string\" utječe \"Pitch of coil\" (ova vrijednost se automatski poravnava s vrijednošću Pitch stringa)

-    {{SpinBox|0,000 mm}}**Radius of coil** : Radijus izmjenjivača zavojnice. (Zadano : none)

-    **20.0 mm**: Ako se pritisne tipka, na \"Radius of coil\" utječe vrijednost \"Radius string\" (ova vrijednost se automatski poravnava s vrijednošću Radius stringa)

-    **<img src="images/FCSpring_Helix_Variable_Icon_01.png" width=16px> Accept the value modified**: Gumb za prihvaćanje modifikacije nakon odabira numeracije svitka i izmjena visine zavojnice.

-   **Text edit** : Ovaj prozor prikazuje sve izmijenjene zavojnice.

-    **Clear**: Očistite uređivač teksta

-    **Zoom**: Gumb \"Zoom\" povećava tekstualni prozor

![](images/Macro_FCSpring_Helix_Variable_04.png ) 

#### Naredbe

-    **<img src="images/FCSpring_Helix_Variable_Icon_02.png" width=16px> Load**: Gumb Čitanje otvara dijaloški okvir za čitanje datoteke **.FCSpring**.

-    **<img src="images/FCSpring_Helix_Variable_Icon_03.png" width=16px> Save**: Gumb Spremi otvara dijaloški okvir za spremanje datoteke **.FCSpring** s modificiranom proljetnom konfiguracijom ili ne.

-    **<img src="images/FCSpring_Helix_Variable_Icon_02b.png" width=16px> Load Coordinates**: Otvorite dijaloški okvir da biste pročitali datoteku **.FCSpringCoor** (sve koordinate točaka proljeća).

-    **<img src="images/FCSpring_Helix_Variable_Icon_02b.png" width=16px> Load Coordinates**: Otvorite dijaloški okvir da biste spremili datoteku **.FCSpringCoor** (sve koordinate točaka proljeća).

-    **<img src="images/FCSpring_Helix_Variable_Icon_04.png" width=16px> Quit**: Zatvorite makronaredbu.

-    **<img src="images/FCSpring_Helix_Variable_Icon_05.png" width=16px> Reset**: Ponovno postavite makronaredbu na zadanu konfiguraciju.

-    **<img src="images/FCSpring_Helix_Variable_Icon_06.png" width=16px> Launch**: Pokrenite makronaredbu i stvorite konfigurirano proljeće.

-    **Help**: Ez a gomb megjeleníti a wiki oldalt a FreeCAD böngészőben.

![](images/Macro_FCSpring_Helix_Variable_05.png ) 

## Prikaz izvješća 

Prikaz izvješća prozora prikazao je svu izmijenjenu vrijednost.

![](images/Macro_FCSpring_Helix_Variable_06.png ) 

## Primjer proljeće 

Primjer za modificirano proljeće

![](images/Macro_FCSpring_Helix_Variable_07.png ) 

## Primjer prikaza izvješća 

Kada se makro pokrene, u tabličnom se obliku prikazuje cijeli popis skretanja.

Ovdje su podaci o izvoru iznad i prikazani u prikazu izvješća ![](images/Macro_FCSpring_Helix_Variable_08.png ) 

## Ikona

Preuzmite sliku i kopirajte datoteku u svoj makro repertoar.

Kliknite sliku, u novom prozoru postavite pokazivač miša iznad slike, kliknite desnu tipku miša i učinite \"Spremi cilj kao \...\"

Gumb alatne trake ![Button](images/FCSpring_Helix_Variable.png )  Ikone makronaredbi

![](images/FCSpring_Helix_Variable_Icon_01.png ) ![](images/FCSpring_Helix_Variable_Icon_02.png ) ![](images/FCSpring_Helix_Variable_Icon_02b.png ) ![](images/FCSpring_Helix_Variable_Icon_03.png ) ![](images/FCSpring_Helix_Variable_Icon_03b.png ) ![](images/FCSpring_Helix_Variable_Icon_04.png ) ![](images/FCSpring_Helix_Variable_Icon_05.png ) ![](images/FCSpring_Helix_Variable_Icon_06.png ) 

## Skripta

**Macro\_FCSpring\_Helix\_Variable.FCMacro**

Preuzmite makronaredbu u Gist [Macro\_FCSpring\_Helix\_Variable](https://gist.github.com/mario52a/68c81c32a0727a693d3a)

## Installation

A fenti fájl egy makró GitHub kód formájában. Töltse le a Zip fájlt a GitHub-on, majd kövesse a próbabábut makrók telepítésére vonatkozó útmutatásait, amely a következő webhelyen látható: [installing FreeCAD macros in Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).

## Primjeri


<center>

<File:Valves> Assembly IN EX.png\| Valves Assembly IN EX with permit and created by r.tec see [Inlet & Exhaust Valves Assembly](http://forum.freecadweb.org/viewtopic.php?f=24&t=14183) and [Spiralfeder](http://forum.freecadweb.org/viewtopic.php?f=13&t=14143) thanks r.tec


</center>



<center>

<File:Macro> FCSpring Helix Variable 12.png\| <File:Macro> FCSpring Helix Variable 13.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 14.png\| <File:Macro> FCSpring Helix Variable 15.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 16.png\| <File:Macro> FCSpring Helix Variable 17.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 18.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 19.png\|Difference between Smooth (here 71 with precision 5 (72 points)) and normal


</center>



<center>

<File:Macro> FCSpring Helix Variable.gif\|Example


</center>



<center>

<File:Macro> FCSpringHelixVariable Example 02.gif\|Example create conical spring


</center>



<center>

<File:Macro_FCSpringHelixVariable_Spring_On_Circle.gif%7CPrimjer> stvaranja opruge na krugu <File:Macro_FCSpringHelixVarable_Spring_Along_Axis.gif%7CPomaknite> se duž osi


</center>


## Linkovi

Rasprava na forumu [Try to do a Spring](http://forum.freecadweb.org/viewtopic.php?f=3&t=8313&p=68161#p68161)

## Projekt

opružna opruga

omekšati priključke :done

promijenite promjer na bilo koju zavojnicu :done

## Verzija

2020/11/12 Version=01.17 : suppress the timer chrono !!

2020/10/18 Ver 00.16b : i suppress the test on FC 18 line 56, i suppress the timer chrono and i wait one little

2020/05/01 Ver 00.16: correction error file (save and load) cause \"label\_11\_Name\" suppressed\...

2020/04/11 Ver 01.15: layout and little presentation

2019/05/03 Ver 01.14: compatible FreeCAD 0.19.16523 (Git)

03/04/2017: ver 01.12: correction bug line 2314 add \"global ui\"

03/04/2017: ver 01.12: correction bug line 2314 add \"global ui\"

11/12/2016: ver 01.11: Adding Position of the spring on a selected object

10/09/2016: ver 01.10: Adding Button \"Zoom\" enlarge the textedit window

04/09/2016: ver 01.09: add smoothing

16/03/2016: ver 01.08 : correct and add \"int()\" to debutAngle and finAngle (read file)

02/03/2016: ver 01.07 : add option reverse spring

08/02/2016: ver 01.06 : correct bug angle cause \"modifyAngle = int(file.readline().rstrip(\'\\n\\r\')) \# 9\" modifyAngle is int() not char

07/01/2015: ver 01.05 : adding \"Try \...Except\" (data cone) for compatibility with old version

07/01/2015: ver 01.04 : adding spring conical and modify the path to \"UserAppData\" and adding the icone.

07/12/2014: ver 01.03 : new version with radius coil adjustable

17/11/2014: ver 1.02 : new version with GUI and modification any coil and save or load the data to disk.

10/11/2014: (23h20) correction of the modification 
```python
ligne.Placement = App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` 10/11/2014: modify line 44 : 
```python
        a = FreeCAD.ActiveDocument.Line.Placement=App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` to 
```python
        ligne = FreeCAD.ActiveDocument.Line.Placement=App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` 6/11/2014 : adding \"makeBSpline\" and configuration

## Ograničenja

Za vrijeme testova su ovdje greške koje sam dobio!


<center>

<File:Macro> FCSpring Helix Variable 20.png\|For the moment the macro is not adapted for the square, rectangle\...
Only circle work well


</center>



<center>

<File:Macro> FCSpring Helix Variable 09.png\|ACCESS VIOLATION <File:Macro> FCSpring Helix Variable 10.png\|TCollection\_IndexedDataMap


</center>



<center>

<File:Macro> FCSpring Helix Variable 11.png\|Wrong usage of punctual sections


</center>


