# Quantity/cs
<div class="mw-translate-fuzzy">

Veličina je kombinace čísla a jednotky. Je využívána všude ve FreeCADu k práci s parametry a všemi dalšími druhy vstupů a výstupů.


</div>

### Základní


<div class="mw-translate-fuzzy">

V CAD a CAE systémech je velmi důležité sledovat jednotky hodnot. Mnoho problémů může nastat když se míchají různé jednotky nebo vypočítané výsledky v různých jednotkových systémech. Jeden známý případ je [havárie Mars Climate Orbiteru](http://en.wikipedia.org/wiki/Mars_Climate_Orbiter#Cause_of_failure) kvůli pomíchání jednotek. I ve stejném jednotkovém systému přicházejí jednotky se spoustou variant šitých vždy na dané použití. Jednoduché příklady jsou např. rychlost v km/h (auta), m/s (roboti) nebo mm/min (frézování). CAD systém musí spolehlivě sledovat jednotky. Také s nimi dělat výpočty a kontrolovat správné jednoty u speciálních parametrů.


</div>


<div class="mw-translate-fuzzy">

Z těchto důvodů byl vytvořen Framework veličin FreeCADu. Zahrnuje všechny kódy a objekty, které pracují s jednotkami, výpočty jednotek, uživatelské vstupy, konverze do jiných jednotkových systémů a pěkný výstup jednotek a hodnot. V dlouhodobém horizontu by žádný paramater ve FreeCADu neměl být pouze jen číslo.


</div>

### Podporované jednotky 


<div class="mw-translate-fuzzy">

Vstupní parser FreeCADu podporuje balík jednotek a jednotkových systémů. Používáme řecké písmeno pro mikro, ale jako náhrada je akceptováno i \'u\'.


</div>


<div class="mw-translate-fuzzy">

Detailní informace najdete v kódu:

-   Slovník veličin: <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Base/QuantityParser.l>
-   Definice veličin: <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Base/Quantity.cpp#l167>


</div>

## Interní reprezentace 

Všechny fyzické jednotky mohou být vyjádřeny jako kombinace sedmi [SI-jednotek](http://en.wikipedia.org/wiki/International_System_of_Units):

<img alt="" src=images/SI-Derived-Units.jpg  style="width:750px;">


<div class="mw-translate-fuzzy">

Jednoduchým způsobem jak vyjádřit jednotku je celočíselné pole 7 čísel (počet základních jednotek), které definuje o jakou jednotku se jedná. Signatury 7 základních jednotek jsou:

-   DĚLKA: \[1,0,0,0,0,0,0\]
-   HMOTNOST: \[0,1,0,0,0,0,0\]
-   ČAS: \[0,0,1,0,0,0,0\]
-   ELEKTRICKÝ PROUD: \[0,0,0,1,0,0,0\]
-   TERMODYNAMICKÁ TEPLOTA: \[0,0,0,0,1,0,0\]
-   LÁTKOVÉ MNOŽSTVÍ: \[0,0,0,0,0,1,0\]
-   SVĚTELNÁ INTENZITA: \[0,0,0,0,0,0,1\]


</div>


<div class="mw-translate-fuzzy">

Těmito 7 jednotkami můžeme vyjádřit všechny odvozené jednotky definované v [Průvodci pro použití Mezinárodního jednotkového systému (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) a vytvářet nové jednotky podle potřeby jako například:

-   MĚRNÁ HMOTNOST: \[-3,1,0,0,0,0,0\]
-   PLOCHA: \[0,2,0,0,0,0,0\]


</div>


<div class="mw-translate-fuzzy">

Protože úhly jsou fyzikálně bezrozměrné, ale ne méně důležité v CAD systému, přidali jsme jednu další virtuální jednotku pro úhel. To dotváří 8-mi místný vektor v jednotkové signatuře FreeCADu.


</div>


<div class="mw-translate-fuzzy">

## Kalkulátor jednotek 

Často potřebujete přepočítávat jednotky z jednoho systému do druhého. Například máte starou tabulku parametrů s drátovými jednotkami. Pro takový případ FreeCAD nabízí konverzní nástroj nazývaný Kalkulátor jednotek, který pomáhá s přepočtem jednotek.


</div>


<div class="mw-translate-fuzzy">

Detailní popis je zde: [Std_UnitsCalculator](Std_UnitsCalculator.md)


</div>


<div class="mw-translate-fuzzy">

## VstupníPole

VstupníPole je QLineEdit odvozený z Qt widgetu k práci se všemi druhy uživatelských vstupů veličin a parametrů. Má následující vlastnosti:

-   zpracovává libovolné hodnoty/jednotky na vstupu
-   kontrola na správnou jednotku (je-li zadána) a dává uživatelskou odezvu
-   speciální kontextové menu pro operace s veličinami/jednotkami
-   správa historie (ukládá poslední použitou hodnotu)
-   ukládá často používané hodnoty jako klávesové zkratky v kontextovém menu
-   vytáčené hodnoty pomocí kolečka myši a klávesových šipek (tbd)
-   vytáčené hodnoty pomocí středního tlačítka myši a posunů myši (tbd)
-   integrace do Pythonu pro použití v dialogových oknech Pythonu (tbd)


</div>

Kalkulátor jednotek již VstupníPole používá.


<div class="mw-translate-fuzzy">

Hlavní dokument: [InputField/cs](InputField/cs.md)


</div>


<div class="mw-translate-fuzzy">

Kód:

-   <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Gui/InputField.h>
-   <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Gui/InputField.cpp>


</div>

## Skriptování v Pythonu 

Systém veličin a jednotek ve FreeCADu je (jako téměř všechno) plně přístupný v Pythonu.


<div class="mw-translate-fuzzy">

### Jednotka

Třída Unit (jednotka) reprezentuje identifikaci fyzické jednotky. Jek je popsáno v základní části je pro reprezentaci jednotky použít vektor 8 čísel. Třída Unit umožňuje práci a výpočty s těmito informacemi.


</div>


```python

from FreeCAD import Units

# creating a unit with certain signature
Units.Unit(0,1)      # Mass     (kg)
Units.Unit(1)        # Length   (mm)
Units.Unit(-1,1,-2)  # Pressure (kg/mm*s^2)

# using predefined constants
Units.Unit(Units.Length)
Units.Unit(Units.Mass)
Units.Unit(Units.Pressure)

# parsing unit out of a string
Units.Unit('kg/(m*s^2)')    # Pressure
Units.Unit('Pa')            # the same as combined unit Pascale
Units.Unit('J')             # Joule (work,energy) mm^2*kg/(s^2)

# you can use units from all supported systems of units
Units.Unit('psi')           # imperial pressure
Units.Unit('lb')            # imperial  mass
Units.Unit('ft^2')          # imperial area

# comparing units
Units.Unit(0,1) == Unit(Units.Mass)

# getting type of unit
Units.Unit('kg/(m*s^2)').Type == 'Pressure'

# calculating
Units.Unit('kg') * Units.Unit('m^-1*s^-2') == Units.Unit('kg/(m*s^2)')

```


<div class="mw-translate-fuzzy">

Jednotka je používaná hlavně k popisu typu jednotky parametru. Proto speciální typ vlastnosti ve FreeCADu může předávat jednotky pro jejich kontrolu a zaručuje správnou jednotku. Hodnota jednotky a čísla je nazývána Veličina.


</div>

### Veličina


```python

from FreeCAD import Units

# to create a quantity you need a value (float) and a unit
Units.Quantity(1.0,Units.Unit(0,1))     # Mass       1.0 kg
Units.Quantity(1.0,Units.Unit(1))       # Length    1.0 mm
Units.Quantity(1.0,Units.Unit(-1,1,-2)) # Pressure  1.0 kg/mm*s^2
Units.Quantity(1.0,Units.Pressure)      # Pressure  1.0 kg/mm*s^2

# you can directly give a signature
Units.Quantity(1.0,0,1)     # Mass       1.0 kg
Units.Quantity(1.0,1)       # Length    1.0 mm
Units.Quantity(1.0,-1,1,-2) # Pressure  1.0 kg/mm*s^2

# parsing quantities out of a string
Units.Quantity('1.0 kg/(m*s^2)') # Pressure
Units.Quantity('1.0 Pa')         # the same as combined Unit Pascale
Units.Quantity('1.0 J')          # Joule (Work,Energy) mm^2*kg/(s^2)

# You can use a point or comma as float delimiter
Units.Quantity('1,0 m')
Units.Quantity('1.0 m')

# you can use units from all supported systems of units
Units.Quantity('1.0 psi')  # imperial pressure
Units.Quantity('1.0 lb')   # imperial mass
Units.Quantity('1.0 ft^2') # imperial area

# the quantity parser can do calculations too
Units.Quantity('360/5 deg')        # splitting circle 
Units.Quantity('1/16 in')          # fractions
Units.Quantity('5.3*6.3 m^2')      # calculating an area
Units.Quantity('1/(log(2.3)/sin(pi)*3.4)+1.8e-3 m')
Units.Quantity('1ft 3in')          # imperial style

# and for sure calculation and comparison
Units.Quantity('1 Pa') * Units.Quantity(2.0) == Units.Quantity('2 Pa')
Units.Quantity('1 m') * Units.Quantity('2 m') == Units.Quantity('2 m^2')
Units.Quantity('1 m') * Units.Quantity('2 ft') + Units.Quantity('2 mm^2')
Units.Quantity('1 m') > Units.Quantity('2 ft')

# accessing the components
Units.Quantity('1 m').Value # get the number (always internal system (mm/kg/s))
Units.Quantity('1 m').Unit  # get the unit
Units.Quantity('1 m') == Units.Quantity( Units.Quantity('1 m').Value , Units.Quantity('1 m').Unit)

# translating the value into other units than the internal system (mm/kg/s)
Units.Quantity('1 km/h').getValueAs('m/s')                  # translate value
Units.Quantity('1 m').getValueAs(2.45,1)                    # translation value and unit signature
Units.Quantity('1 kPa').getValueAs(Units.Pascal)            # predefined standard units 
Units.Quantity('1 MPa').getValueAs(Units.Quantity('N/m^2')) # a quantity
          
```


<div class="mw-translate-fuzzy">

### Hodnoty pro uživatele 

Ve skriptech můžete používat veličiny pro všechny druhy výpočtů a kontrol, přijde čas, kdy budete muset vytvořit výstupní informaci pro uživatele. Můžete použít getValueAs() pro vynucení určité jednotky, ale normálně uživatel nastaví svoje preferované jednotkové schéma v předvolbách. Toto jednotkové schema dělá všechny převody do reprezentace, kterou chce uživatel vidět. V této době jsou implementována 3 schemata:

-   1: Vnitřní (mm/kg/s)
-   2: MKS (m/kg/s)
-   3: US customary (in/lb)

Přidální dalších schemat bude v budoucnosti snadné \...


</div>


<div class="mw-translate-fuzzy">

Třída pro veličinu má dvě možnosti použití aktuálních převodového schematu:


</div>


```python
from FreeCAD import Units

# Use the translated string:
Units.Quantity('1m').UserString           # '1000 mm' in 1; '1 m' in 2; and '1.09361 yr' in 3
```


<div class="mw-translate-fuzzy">

To funguje jenom když potřebujete řetězce (texty). Ale někdy potřebujete větší řízení, např. když máte dialogové tlačítko a možností posunu nahoru a dolu. Pak potřebujete mnohe víc informací o převodu do výstupu. Proto je pro veličiny používána metoda getUserPrefered():


</div>


```python
Units.Quantity('22 m').getUserPreferred() # gets a tuple:('22 m', 1000.0, 'm')
Units.Quantity('2  m').getUserPreferred() # Tuple: ('2000 mm', 1.0, 'mm')
```


<div class="mw-translate-fuzzy">

Zde získáte dvě další informace jako pole o velikosti 3. Dostanete řetězec jako předtím, plus faktor, kterým je číslo převedeno a neupravený řetězec pouze s jednotkou vybranou převodovým schematem. S takovou informací můžete implementovat mnohem bohatší odezvu.


</div>


<div class="mw-translate-fuzzy">

Kódy pro převodní schema můžete najít zde:

-   <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Base/UnitsSchemaInternal.cpp>
-   <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Base/UnitsSchemaMKS.cpp>
-   <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Base/UnitsSchemaImperial1.cpp>


</div>

### Precision

The precision of quantities is within FreeCAD dialogs the number of decimals specified [in the preferences](Preferences_Editor#Units.md). To use this settings for your script (for example in dialogs), you can get it with this code: 
```python
import FreeCAD

params = App.ParamGet("User parameter:BaseApp/Preferences/Units")
params.GetInt('Decimals') # returns an int
```

## Dodatek


<div class="mw-translate-fuzzy">

### Jednotky podporované parserem 

Ačkoliv všechny fyzické jednotky mohou být popsány 7 jednotkami SI, většina jednotek používaných v technické oblasti jsou obecné kombinované jednotky (jako Pa = N/m\^2 Pascal ). Proto parser jednotek ve FreeCADu podporuje spoustu SI a Imperiálních jednotek. Tyto jednotky jsou jsou definovány v souboru src/Base/QuantityParser.l a mohou být v budoucnosti dále rozšiřovány.


</div>


```python

from FreeCAD import Units

 "nm"  = Units.Quantity(1.0e-6    ,Units.Unit(1));         // nano meter
 "µm"  = Units.Quantity(1.0e-3    ,Units.Unit(1));         // micro meter
 "mm"  = Units.Quantity(1.0       ,Units.Unit(1));         // milli meter
 "cm"  = Units.Quantity(10.0      ,Units.Unit(1));         // centi meter
 "dm"  = Units.Quantity(100.0     ,Units.Unit(1));         // deci meter
 "m"   = Units.Quantity(1.0e3     ,Units.Unit(1));         // meter
 "km"  = Units.Quantity(1.0e6     ,Units.Unit(1));         // kilo meter
 "l"   = Units.Quantity(1000000.0 ,Units.Unit(3));         // liter dm^3
                                                  
 "µg"  = Units.Quantity(1.0e-9    ,Units.Unit(0,1));       // micro gram
 "mg"  = Units.Quantity(1.0e-6    ,Units.Unit(0,1));       // milli gram
 "g"   = Units.Quantity(1.0e-3    ,Units.Unit(0,1));       // gram
 "kg"  = Units.Quantity(1.0       ,Units.Unit(0,1));       // kilo gram
 "t"   = Units.Quantity(1000.0    ,Units.Unit(0,1));       // ton
                                                  
 "s"   = Units.Quantity(1.0       ,Units.Unit(0,0,1));     // second (internal standard time)
 "min" = Units.Quantity(60.0      ,Units.Unit(0,0,1));     // minute
 "h"   = Units.Quantity(3600.0    ,Units.Unit(0,0,1));     // hour  
                                                  
 "A"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,1));   // Ampere (internal standard electric current)
 "mA"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,1));   // milli Ampere         
 "kA"  = Units.Quantity(1000.0    ,Units.Unit(0,0,0,1));   // kilo Ampere         
 "MA"  = Units.Quantity(1.0e6     ,Units.Unit(0,0,0,1));   // Mega Ampere         
                                                  
 "K"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,1)); // Kelvin (internal standard thermodynamic temperature)
 "mK"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,0,1)); // Kelvin         
 "µK"  = Units.Quantity(0.000001  ,Units.Unit(0,0,0,0,1)); // Kelvin         

 "mol" = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,1)); // Mole (internal standard amount of substance)        

 "cd"  = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,0,1)); // Candela (internal standard luminous intensity)        

 "deg" = Units.Quantity(1.0         ,Units.Unit(0,0,0,0,0,0,0,1)); // degree (internal standard angle)
 "rad" = Units.Quantity(180/M_PI    ,Units.Unit(0,0,0,0,0,0,0,1)); // radian         
 "gon" = Units.Quantity(360.0/400.0 ,Units.Unit(0,0,0,0,0,0,0,1)); // gon         

 "in"  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
 "\""  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
 "fo"  = Units.Quantity(304.8       ,Units.Unit(1));       // foot
 "'"   = Units.Quantity(304.8       ,Units.Unit(1));       // foot
 "th"  = Units.Quantity(0.0254      ,Units.Unit(1));       // thou
 "yd"  = Units.Quantity(914.4       ,Units.Unit(1));       // yard

 "lb"  = Units.Quantity(0.45359237   ,Units.Unit(0,1));    // pound
 "oz"  = Units.Quantity(0.0283495231 ,Units.Unit(0,1));    // ounce
 "st"  = Units.Quantity(6.35029318   ,Units.Unit(0,1));    // Stone
 "cwt" = Units.Quantity(50.80234544  ,Units.Unit(0,1));    // hundredweights
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Quantity/cs
