 Quantity è la combinazione di un numero in virgola mobile e di una unità di misura.

## Aspetti generali 

In un sistema CAD o CAE ​​è molto importante mantenere la traccia dell\'unità di misura di un valore. Quando si mescolano le unità o si calcolano i risultati in diverse unità di misura possono sorgere un sacco di problemi. Un famoso disastro, causato da un disguido sulle unità di misura, è il [crash of the Mars Climate Orbiter](http://en.wikipedia.org/wiki/Mars_Climate_Orbiter#Cause_of_failure). Anche all\'interno di uno stesso Sistema di misura le unità possono essere disponibili in diversi formati, secondo il settore di utilizzo. Ad esempio, la velocità in km/h per le automobili, in m/s in robotica o in mm/min per la fresatura. Un sistema CAD deve conservare una traccia affidabile delle unità. Inoltre deve utilizzarle per eseguire i calcoli e deve verificare che per i parametri speciali sia adottata la giusta unità.

Per questo motivo è stata creata la sezione Quantity di FreeCAD. Essa include tutto il codice e gli oggetti che servono per trattare le unità, i calcoli delle unità, i dati inseriti dall\'utente, la conversione tra i Sistemi e per fornire un corretto output delle unità e dei valori. In futuro, in FreeCAD, nessun parametro dovrebbe essere solo più un numero.

### Unità supportate 

Il parser dei dati in ingresso di FreeCAD supporta una serie di unità e di Sistemi di unità. FreeCAD supporta la lettera greca \'µ\' per micro ma accetta anche \'u\' in sostituzione. Un elenco completo di tutte le unità supportate [si trova quì](Expressions/it#Unità.md).

Le specifiche dettagliate si trovano nel codice:

-   [Quantity lexer](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/QuantityLexer.c)
-   [Quantity definitions](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/Quantity.cpp#l167)

## Rappresentazione interna 

Tutte le unità fisiche possono essere espresse come combinazione delle sette [Unità SI](http://en.wikipedia.org/wiki/International_System_of_Units) di base:

<img alt="" src=images/SI-Derived-Units.jpg  style="width:750px;">

Un modo semplice per esprimere una Unità è quello di utilizzare un gruppo di 7 interi, il numero delle unità di base, che definisce di quale unità si tratta. Le firme delle 7 unità di base sono:

-   LUNGHEZZA: \[1,0,0,0,0,0,0\]
-   MASSA: \[0,1,0,0,0,0,0\]
-   TEMPO: \[0,0,1,0,0,0,0\]
-   CORRENTE ELETTRICA: \[0,0,0,1,0,0,0\]
-   TEMPERATURA TERMODINAMICA: \[0,0,0,0,1,0,0\]
-   QUANTITÀ DI SOSTANZA: \[0,0,0,0,0,1,0\]
-   INTENSITÀ LUMINOSA: \[0,0,0,0,0,0,1\]

Usando queste 7 unità, siamo poi in grado di esprimere tutte le unità derivate definite nella [Guida per l\'utilizzo del Sistema Internazionale di Unità (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) e di crearne di nuove, secondo le esigenze, come ad esempio:

-   MASS DENSITY: \[-3,1,0,0,0,0,0\]
-   AREA: \[0,2,0,0,0,0,0\]

Dato che l\'angolo è fisicamente adimensionale, ma in un sistema CAD non è meno importante, si è aggiunta una unità virtuale in più per Angle. Questo crea un vettore di 8 dati nella firma delle unità di FreeCAD.

## Il convertitore delle unità 

Sovente è necessario convertire le unità da un sistema a un altro. Per esempio, quando i parametri sono contenuti in vecchie tabelle e espressi in determinate unità. In questi casi FreeCAD offre uno strumento di conversione denominato Units-Calculator che aiuta a tradurre le unità.

La sua desrizione si trova nella pagina: [Std\_UnitsCalculator](Std_UnitsCalculator/it.md)

## InputField

Inputfield è un oggetto QLineEdit derivato da un widget Qt e serve per gestire tutti i tipi di interazioni dell\'utente con le quantità e con i parametri. Offre le seguenti proprietà:

-   analisi dei valori e delle unità arbitrarie inserite
-   verifica della corrispondenza dell\'unità (se fornita) e restituzione di un riscontro
-   speciale menu contestuale per le operazioni sulle Quantità e sui Valori
-   gestione della cronologia (salva gli ultimi valori usati)
-   salvataggio dei valori usati frequentemente nella scorciatoia del menu contestuale
-   selezione dei valori con la rotellina del mouse e con i tasti freccia (tbd)
-   selezione con il tasto centrale più il movimento del mouse (tbd)
-   integrazione Python per l\'utilizzo nella console Python (tbd)

Lo strumento UnitsCalculator usa già InputField.

Documentazione di riferimento: [InputField](InputField/it.md)

Codice:

-   [InputField.h](https://github.com/FreeCAD/FreeCAD/blob/master/src/Gui/InputField.h)
-   [InputField.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Gui/InputField.cpp) <http://sourceforge.net/p/free-cad/code/ci/master/tree/src/Gui/InputField.cpp>

## Script Python 

Come quasi tutto in FreeCAD, anche i sistemi Unit e Quantity sono totalmente accessibili tramite Python.

### Unit

La classe Unit rappresenta la firma digitale di qualsiasi unità fisica. Come descritto nella sezione di base, per rappresentare questa firma digitale viene usato un vettore di otto numeri. La classe Unit permette di gestire tutte queste informazioni e di usarle per i calcoli.


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

Unit è utilizzata principalmente per descrivere un parametro in un determinato tipo di unità. In FreeCAD si può quindi importare una particolare proprietà Type abbinata a una Unit per controllare e garantire che sia utilizzata l\'unità corretta. Una Unit più un valore in virgola mobile sono definiti una quantità.

### Quantity


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

### I valori nell\'interfaccia utente 

Normalmente negli script si può utilizzare Quantity per ogni tipo di calcolo e di verifica, ma può capitare che si debba attendere un po\' per ottenere l\'uscita dei risultati. Si può utilizzare getValueAs() per forzare una certa unità, ma di solito si definisce il proprio sistema di unità nelle preferenze. Il sistema di unità converte tutta la rappresentazione nel sistema impostato. Al momento sono implementati questi 3 sistemi di unità:

-   1: Internal (mm/kg/s)
-   2: MKS (m/kg/s)
-   3: US customary (in/lb)

In futuro potranno essere facilmente implementati altri sistemi \...

Attualmente, ci sono due modi di utilizzare la classe Quantity per realizzare la conversione del sistema:


```python
from FreeCAD import Units

# Use the translated string:
Units.Quantity('1m').UserString           # '1000 mm' in 1; '1 m' in 2; and '1.09361 yr' in 3
```

Questo metodo va bene quando serve solo una stringa. A volte però, si ha bisogno di un controllo maggiore, ad esempio quando si vuole avere una finestra di dialogo con un pulsante su e giù. In questo caso servono ulteriori informazioni sull\'uscita della conversione, allora viene usato il metodo getUserPreferred() di quantity:


```python
Units.Quantity('22 m').getUserPreferred() # gets a tuple:('22 m', 1000.0, 'm')
Units.Quantity('2  m').getUserPreferred() # Tuple: ('2000 mm', 1.0, 'mm')
```

Qui si ottengono due informazioni in più sotto forma di una tupla di 3 elementi. Si ottiene, come prima, la stringa, inoltre il fattore numero viene tradotto e la stringa cruda con solo l\'unità scelta dal sistema di conversione. Con queste informazioni è possibile implementare una interazione con l\'utente molto più ricca.


<div class="mw-translate-fuzzy">

Il codice di definizione del sistema di conversione è visibile in:

-   [Internal](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaInternal.cpp)
-   [MKS](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaMKS.cpp)
-   [Imperial](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaImperial.cpp)


</div>

### Precisione

La precisione delle quantità è il numero di decimali specificato nelle finestre di dialogo di FreeCAD [nelle preferenze](Preferences_Editor/it#Unità.md). Per utilizzare queste impostazioni negli script (ad esempio nelle finestre di dialogo), si può usare questo codice: 
```python
import FreeCAD

params = App.ParamGet("User parameter:BaseApp/Preferences/Units")
params.GetInt('Decimals') # returns an int
```

## Appendice

### Unità supportate dal Parser 

Anche se tutte le unità fisiche possono essere descritte con le sette unità SI, la maggior parte delle unità utilizzate nelle aree tecniche sono delle combinazioni di unità comuni (come Pa = N/m\^2 Pascal ). Pertanto il parser delle unità di FreeCAD supporta molte combinazioni del SI e del Sistema Imperiale. Queste unità sono definite nel file src/Base/QuantityParser.l e in futuro potranno essere incrementate.


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


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
