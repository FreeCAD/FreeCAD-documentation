





{{TOCright}}


<div class="mw-translate-fuzzy">

### Använda licenser 

Här är de tre licenserna under vilka FreeCAD är publicerad:


</div>

FreeCAD uses two different licenses, one for the application itself, and one for the documentation:


<div class="mw-translate-fuzzy">


[GPL](http://sv.wikipedia.org/wiki/GNU_General_Public_License): För Python sripten för att bygga binärfilerna som uttalat i .py filerna i src/Tools





[LGPL](http://sv.wikipedia.org/wiki/GNU_Lesser_General_Public_License): För kärnbiblioteken som uttalat i .h och .cpp filerna i src/App src/Gui src/Base och de flesta [modulerna](Workbenches/sv.md) i src/Mod och för de körbara som uttalat i .h och .cpp filerna i src/main





[Open Publication Licence](wikipedia:Open_Publication_License.md): För dokumentationen på <http://free-cad.sourceforge.net/> om inget annat markerats av författaren


</div>

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** For the documentation on <https://www.freecadweb.org>


<div class="mw-translate-fuzzy">

Se FreeCAD\'s [debian copyright file](http://free-cad.git.sourceforge.net/git/gitweb.cgi?p=free-cad/free-cad;a=blob;f=package/debian/copyright;h=a97cf019d020edba596f2d0f614c9b09ce546b0f;hb=HEAD) för mer detaljer om de licenser som används i FreeCAD


</div>


<div class="mw-translate-fuzzy">

### Licensernas inverkan 


</div>

Below is a friendlier explanation of what the LGPL license means for you:


<div class="mw-translate-fuzzy">

#### Privata användare 

Privata användare kan använda FreeCAD utan avgift och kan göra ungefär vad de vill med den\....


</div>


<div class="mw-translate-fuzzy">

#### Professionella användare 

Kan använda FreeCAD fritt, för alla sorters privata eller professionella arbeten. De kan anpassa applikationen som de önskar. De kan skriva öppen eller sluten källkodsextensioner till FreeCAD. De är alltid herrar över deras data, de är inte tvingade att uppdatera FreeCAD, ändra deras bruk av FreeCAD. Att använda FreeCAD binder dem inte till några kontrakt eller krav.


</div>


<div class="mw-translate-fuzzy">

#### Öppen källkodsutvecklare 

Kan använda FreeCAD som grundplattform för egna extensionsmoduler för speciella ändamål. De kan välja antingen GPL eller LGPL för att tillåta bruk av deras arbete i proprietär mjukvara, eller inte.


</div>


<div class="mw-translate-fuzzy">

#### Professionella utvecklare 

Professionella utvecklare Kan använda FreeCAD som grundplattform för egna extensionsmoduler för speciella ändamål och är inte tvingade att göra sina moduler till öppen källkod. De kan använda alla moduler som använder LGPL. De är tillåtna att distribuera FreeCAD tillsammans med deras proprietära mjukvara. De kommer få support av författarna så länge som den inte är enkelriktad. Om du vill sälja din modul så behöver du en Coin3D licens, annars är du tvingad av detta bibliotek att göra den till öppen källkod.


</div>

#### Files

The models and other files produced with FreeCAD are not subject to any license stated above, nor bound to any kind of restriction or ownership. Your files are truly yours. You can set the owner of the file and specify your own license terms for the files you produce inside FreeCAD, via menu File → Project Information.


<div class="mw-translate-fuzzy">

### Uttalande från underhållaren 

Jag vet att diskussionen om *\"rätt\"* licens för öppen källkod tar upp en signifikant del av internetbandbredden, så här är skälen till varför, enligt min åsikt, FreeCAD ska ha denna.


</div>


<div class="mw-translate-fuzzy">

Jag valde [LGPL](http://sv.wikipedia.org/wiki/GNU_Lesser_General_Public_License) och [GPL](http://sv.wikipedia.org/wiki/GNU_General_Public_License) för projektet och jag vet för- och nackdelarna med LGPL och vill ge dig några skäl till det beslutet.


</div>

FreeCAD är en blandning av bibliotek och en applikation, så GPL skulle vara lite för starkt för det. Det skulle förhindra skapande av kommersiella moduler för FreeCAD därför att det skulle förhindra länkning med FreeCAD\'s basbibliotek. Du kanske frågar dig: varför kommersiella moduler överhuvudtaget? Därför är Linux ett bra exempel. Skulle Linux vara så framgångsrikt om GNU C Biblioteket skulle vara GPL och därför förhindra länkning mot icke-GPL applikationer? Och fastän jag älskar friheten i Linux, så vill jag också kunna använda den mycket bra NVIDIA 3D grafikdrivrutinen. Jag förstår och accepterar anledningen till att NVIDIA inte vill ge bort drivrutinskod. Vi jobbar alla för företag och behöver lön eller åtninstone mat. Så för mig är en samexistens av öppen källkod och sluten källkodsmjukvara inte något dåligt, när det följer reglerna i LGPL. Jag skulle vilja se någon som skriver en Catia import/export processor för FreeCAD och distribuerar den gratis eller för lite pengar. Jag tycker inte om att tvinga honom att ge bort mer än han vill. Det skulle inte vara bra varken för honom eller FreeCAD.

Detta beslut är ändå bara gjort för FreeCAD\'s kärnsystem. Var och en som skriver en applikationsmodul kan ta sina egna beslut.


{{Quote|Jürgen Riegel|15 October 2006}}


<div class="mw-translate-fuzzy">


{{docnav/sv|Dialog creation/sv|Tracker/sv}}


</div>


 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
