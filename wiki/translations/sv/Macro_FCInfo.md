# Macro FCInfo/sv
<div class="mw-translate-fuzzy">


{{Macro/sv
|Name=Macro FCInfo
|Icon=FCInfo.png
|Translate=Macro FCInfo
|Description=Beskrivning = Ger en serie information på formuläret.
|Author=Mario52
|Version=1.22
|Date=2020/11/12
|FCVersion=All
|Download=Download the [https://forum.freecadweb.org/download/file.php?id=50755 Macro_FCInfo_Icon] package and paste it in the same directory of the macro
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey/sv.md)<br />[Macro SimpleProperties](Macro_SimpleProperties/sv.md)
}}


</div>


<div class="mw-translate-fuzzy">

## Beskrivning

Ger en serie information om den valda formen och kan visa en konvertering av längd, lutning (grader, radianer, grader, hällande) form, yta, volym och vikt av formuläret i densiteten vald i olika kvantiteter internationella och Anglo -Saxiska.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/4ff055ff5eb117f75beea5843efca4791990cf62/FCInfo_en_Ver_1-22-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Utnyttjande

Välj ett objekt eller starta programmet och välj ett objekt och en serie information visas. Hans beräkningar baserade på FreeCADs enhet, som är **mm** för varje nytt val, kommer längdsenheten alltid tillbaka på **mm** och vinkel på **decimalgrader**. <img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width:200px;">




**Sektor 1: Dokument**

-   Dokument namn
-   Etikett för objektet
-   Objektets interna namn
-   Subelementets namn på objektet
-   Typ av objektet

**Sektor 2: Koordinater klicka på musen**

-   Koordinater X, Y och Z klickar på musen
-   Knappen skapas på punkt, axel, plan, kopiera vektoraxelformat **FreeCAD.Vector (-24.0, 240.0, 7.0)**

**Sektor 2: Koordinater klicka på musen**

-   Koordinater X, Y och Z klickar på musen
-   Knappen skapas på punkt, axel, plan, kopiera vektoraxelformat **FreeCAD.Vector (-24.0, 240.0, 7.0)**

**Sektor 4: Vertexes och detaljer**

-   Checkbox för att söka eller inte alla detaljer om objektet om det inte är markerat visas endast huvudvärdet.
-   Vertexes och detaljer om formen (compt\_Edge), (compt\_Faces), (compt\_Vector of the Face)
    Max 200 linjer i tabellen, om det finns mer än 200 linjer visas det (! + 200) och antalet rader
    (fullständiga detaljer kan spara **Save** -knappen i en fil i CSV-format och kan ses i filen i kalkylbladet med **Read** eller av ett externt kalkylblad som[LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other)

**Sektor 5: Höjning**

-   Höjningar av objektet kan visas i:
-   **decimalgrad**, ex: 174.831872611 °
-   **gradminne sekund**, ex: 174° 49\' 54.741401\'\'
-   **radian**, ex: 3.05139181449 rad
-   **betyg**, ex: 194.257636235 gon
-   **pourcent** ex: 30° = 57,74%
-   Höjningar i plan XY, YZ, ZX och deras koordinater
-   **Riktningsobjekt**, ge objektets riktning beräkningen är: coord\_1 - coord\_2 = riktning (eller omvänd)
    -   
        **Line**
        
        den här knappen skapar en rad i riktning mot objektet
-   *\' ValueAt*\' returnerar 3D-vektorn som motsvarar ett parametervärde.

**Sektor 6: Yta och volym**

-   Ytan på formuläret visat enhetsstorlek kan väljas
-   Ytan på ansiktets visade enhetsstorlek kan väljas
-   Volymen av formuläret visat enhetsstorlek kan väljas
-   Täthet av materialet i \'\'\'kg av dm3 \'\'\'
    (\"spinBox\" är inställt på **7,5** kg, medeltäthet av stål. Om du vill ha ett annat standardvärde , ändra värdet på densiteten, linje 204)
-   Massfältet **gram** buttom kan väljas:
    ton, kvintal, kg, hg, dag, gramm, dg, cg, mg, μg, ng, pg, fg, gr (korn), dr (drachm), oz (en gång), oz t (en gång troj),
    lb t (livre troy), lb (livre av) , cwt (hundra vikt), tonneau fr, ct
-   Vikten av formuläret som visas enhetens massa kan väljas

**Sektor 7: BoundBox**

-   BoundBox extrema dimensioner av formen

**Sektor 8: Centrum för:**

-   Centrum för formen och dessa koordinater XYZ
-   Masscentrum och dessa koordinater XYZ
-   Knappen skapas på punkt, axel, plan, kopiera vektoraxelformat **FreeCAD.Vector (-24.0, 240.0, 7.0)**

**Sektor 9: Tröghet**

-   Moment av tröghet och dessa koordinater längd och vikt
-   Knappen skapas på punkt, axel, plan, kopiera vektoraxelformat **FreeCAD.Vector (-24.0, 240.0, 7.0)**
    -   åtgärdslinje 1: x1, y1, z1
    -   åtgärdslinje 2: x2, y2, z2
    -   åtgärdslinje 3: x3, y3, z3
    -   åtgärd 4 diagonal: x1, y2, z3

samma för längd och vikt

-   Bestämmer 1: beräknar determinanten av matrisens vetenskapliga värde
-   Bestämmer 2: beräknar determinanten av matris decimalvärdet

**Avsnitt 10: SpreadSheet**

-    **Read**: läs data i ett kalkylblad sparat **.FCInfo** eller txt, asc, csv

-    **Save**: spara data på disk i formuläret nedan **.FCInfo** eller txt, asc, csv

-    **Tabulation**: separatorn är tabulering

-    **Comma**: separatorn är Comma

-    **semicolon**: separatorn är semikolon

-    **Space**: separatorn är Space

Alternativ för att spara eller läsa spreadSheet med olika separator, Tabulation, Comma, Semicolon, Space
Tabellen är separatorn för FreeCAD spreadSheet-modulen
Numret på den här fyra separatorn beräknas för hjälp om det är okänt
Kommunen är den gamla (01.16 och tidigare) separatorn av FCInfo makro
Nu för kompatibilitet med FreeCAD spreadSheet och sedan 01.17 versionen är tabellen separator som standard
Om du vill konvertera ditt gamla FCInfo-kalkylblad: Öppna det i FCInfo och spara det med Tabuleringsalternativet markerat

**Avsnitt 11: Huvud**

-    **CheckBox Klippkort**: om markerad sparas koordinaterna i clipboardform: \'\' \'FreeCAD.Vector (-24.0, 240.0, 7.0)\'\'\'

-    **CheckBox Point**: om kryssad en punkt skapas i den visade koordinaten: \'\' \'FreeCAD.Vector (-24.0, 240.0, 7.0)\'\'\'

-    **CheckBox Axis**: om den markerade enaxeln skapas i den visade koordinaten: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **CheckBox Plane**: om det markerade ettaxelplanet skapas i den koordinat som visas: \'\' \'FreeCAD.Vector (-24.0, 240.0, 7.0)\'\'\'

-    **Ref**: Uppdatera visning av data i rapportvy

-    **Exit**: Avsluta makroet (du måste starta om från verktygsfältet knappen eller menyn \"Visa → Paneler → FCInfo\"

-    **CheckBox****1**: Om denna kryssrutan är markerad visas informationen i rapportvynsfönstret

-    **CheckBox****2**: Om den här kryssrutan inte är markerad visas fönstret makro till höger (standard). Om den är markerad visas fönstret makro till vänster

När makroen är lanserad, förblir makroen aktiv och fönstret är synligt. För att lämna makroet genom att trycka på **Exit**. Om du lämnar vid korset kvarstår makrot i minnet och data visas i \"Rapportvy\" av FreeCAD.


<center>

Image:Macro\_FCInfo\_04.png\|Dockad till höger, Image:Macro FCInfo 05.png\|eller vänster med kombinationsvy och nås med en flik, eller inte dockad till valet.


</center>




## Alternativ

### Den enhet som används 

#### Längd enhet: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Vinkelgrader :

1.  **decimal degree**, ex: 174.831872611°
2.  degree minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon
5.  pourcent ex: 30° = 57.74%

Förståelse av vinklar i FCInfo-displayen.


<center>

Image:Macro FCInfo 02.png\|Förståelse av vinklar i FCInfo-displayen Image:Macro FCInfo 03.gif\|Förståelse av vinklar i poucent i FCInfo-skärm
klicka två gånger för att se animationen (bilden måste vara i helskärm)


</center>




#### Viktenhet :

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
\"spinboxen\" är inställd på **7,5** kg, medeltäthet av stål. Om du vill ha ett annat standardvärde, ändra värdet på densiteten, linje 208


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```

En fil kan skapas med knappen **Save**. Filen är skriven som en fil [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) på så sätt kan data studeras i ett kalkylblad i FreeCAD eller Openoffice, LibreOffice\...

## Script

Kopiera innehållet i makroet i en fil med namnet \"FCInfo.FCMacro\"

-   Windows: formen är vanligtvis **\" drive:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: formen är vanligtvis **\" /home/your\_user\_name/.FreeCAD \"**.

Eller direkt i gränssnittet till FreeCAD
Ikonen måste vara i samma katalog som makroen.
Ladda ner bildpositionering på ikonen <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> och dra sedan musen med högerklicka \"spara som\" (ändra inte namnet)
**PS: för länge att finnas på wikisidan (för tillfället wiki sidorna accepterar endast 64 KB) makrokoden har placerats i forumet**


<div class="toccolours mw-collapsible mw-collapsed">

Det finns också FCInfo\_Alternate\_Linux för endast för FreeCAD-versionen 0.13\... and PyQt4


<div class="mw-collapsible-content">

Det finns även en [Macro\_FCInfo\_Alternate\_Linux](http://www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux) här ändras koden (på grund av teckenfönstret : **² ³ ° μ** ordinal not in range (128)\") vilket innebar problem i vissa konfigurationer funktionerna är desamma
Example : 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` remplacés par 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
``` **Filer som sparas med den här versionen är inkompatibla med den andra versionen (dockad eller ej)**


</div>


</div>

Ladda ner ikonfilen [Macro\_FCInfo\_Icon](https://forum.freecadweb.org/download/file.php?id=50755) Unzip och kopiera ikonen i samma katalog i makroet

Hämta makrofilen på **docked to right**


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|senaste versionen Macro_FCInfo och ikonerna i slutet av sidan}}

(Eller **[On the forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS:** detta makro använder **getSelection ()** och listan över objekt börjar till 1 ex: för en ruta **Edge1 till Edge12** och koden i konsolen börjar vid 0 ex: for a box **Edge\[0\] to Edge\[11\]**
Detta är normalt att räkna på arrayer / listor i OpenCascade börjar alltid på **1 och inte på 0**

### Begränsningar

Lämna alltid knappen **Exit**. Om man lämnar programmet utan att gå igenom knappen **Exit**, förblir programmet i minnet och fortsätter att springa och displayen kommer att vara kvar i \"visningsrapporten\". Du måste lämna FreeCAD för att radera det från minnet.
Endast de första 200 elementen i objektet är synliga i tabellen om det finns mer än 200 objekt i objektet kommer en signal att visas med **(! +200)**. Den fullständiga listan med data är synlig i filen som sparas med knappen **Save**.
Om fönstret makro är osynligt efter körningen, se nedre fönstret:

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

projekt:
~~läs filen direkt i en tabell.~~ gjort
~~matchar \"Edges\" och deras koordinater~~ gjort
Sammansättning av ett ämne för dens densitet
~~lutning på elementet snarare än det globala objektet~~ gjort
~~inlägg direkt i gränssnittet till FreeCAD~~ gjort

## Version

-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` and i adding the possibility display or not the \"Error Message\" window \"False\" by default, if you wand activate the warning window go to : 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" replace character micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"
-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu replace all characters over 127 in ex: \"°\" in chr(176)) \#degree
-   ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"
-   Ver 1.20, 29/01/2018 optimering
-   ver 1.19, 20/01/2018 skapa checkbox för att upptäcka alla element i objektet om det är önskat eller inte, makroet är snabbare. Optimering
-   ver 1.18, 19/12/2017 \...
-   ver 1.17c, 14/12/2017 skapa plan med koordinat ge i ett projekt i annat projekt och ersätt \"FCInfo\" med \"\_\_title\_\_\"
-   Ver 1.17b, 13/12/2017 liten korrigering ersätter FCTreeView till FCInfo
-   ver 1.17, 12/12/2017 lägg till uppgradering Moment of inertia mm och kg av pinq [FCMacro och tröghetsmoment](https://forum.freecadweb.org/viewtopic.php?t=23888) och skapa plan, axel, punkt och lägg till alternativ separator för kalkylblad
-   ver 1.16, 21/06/2017 lägg till kontrollhöjds polis (här PointSize 8) och kryssrutan för att placera fönstret åt höger eller vänster
-   ver 1.15, 19/12/2015 suppression PyQt4 alternativ [se](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541), lägg till checkbox för att redigera infos i rapportvy
-   ver 1.14, 04/08/2014 ersätt PyQt4 och PySide och korrigera verktygstips inte visad orsak på PySide och lägg till fg
-   ver 1.13, 27/07/2014 ersätt FCInfo\_en\_Ver\_1-12\_Docked.FCMacro till FCInfo\_en\_Ver\_1-13\_Docked.FCMacro acceptera PyQt4 och PySide
-   ver 1.12, 10/03/2014 lägger till verktygstips
-   ver 1.11, 04/03/2014 Lägga till μm, nm, pm, fm, μg, ng, pg, hällande, fast av storhet karat ~~\"cd\"~~ i \'\' \'\"ct\" , visning av etiketten och internt namn, fast beräkning av vinklar XY YZ ZX kan ge ett fel på en sammansatt form, fönstret dockbart i FreeCAD
-   Ver 1.10.b, 19/11/2013 knappar utanför rullningsfältet och dimensionerna i fönstret blockerar

(ver 1.10, 18/11/2013 skapa rullningsfältet)
\* ver 1.08.b, 10/11/2013 översättningsenheter på engelska, felkorrigering för att visa området för ansikten som anges i tabellen och ersättning av **print** **App.Console .PrintMessage**
~~ver 1.09, 04/11/2013 fungerar perfekt på Windows och Linux (orsak till fel på Linux karaktärerna: ² ³ ° ordinal inte inom intervallet (128) \")~~
I en Linux-distribution och i händelse av ett fel på \'\' \'\' ordinär inte inom intervallet (128) finns det en alternativ version på den här sidan [Macro\_FCInfo\_Alternate\_Linux](Macro_FCInfo_Alternate_Linux/sv.md)
\* Ver 1.08, 24/10/2013 korrigering av högsta \"Faces\" och \"Edges\" som visar 100 objekt (i den sparade filen)
\* ver 1.07, 11/10/2013 matchar \"Faces\" och deras koordinater.
\* ver 1.06, 22/09/2013 matchar \"Edges\" och deras koordinater, lutning på elementet snarare än det globala objektet
\* ver 1.05, 17/09/2013 lade till en ikon för kalkylbladet, konverteringskärlet fr, affichage des dimensions overall istället för koordinater.
\* ver 1.04, 11/09/2013: läs filen direkt i en tabell.
\* ver 1.03, 09/09/2013: tydligare visning i rapport och ersättning med \"typeObject = sel \[0\] .Shape.ShapeType\"
\* ver 1.02, 7/09/2013: små uppdateringar
\* ver 1.00, 6/09/2013


<div class="mw-translate-fuzzy">

## Länkar

Se även [Arch Survey](Arch_Survey/sv.md) <img alt="Arch Survey" src=images/Arch_Survey.png  style="width:36px;">


</div>

Du kan dela dina kommentarer på forumet [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Här ett annat inlägg av [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)

---
[documentation index](../README.md) > Macro FCInfo/sv
