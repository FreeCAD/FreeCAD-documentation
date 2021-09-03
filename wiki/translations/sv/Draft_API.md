


<div class="mw-translate-fuzzy">

Dessa funktioner är en del av Skissmodulen och kan användas i skript och makron eller från pythontolken, när Skissmodulen har importerats.


</div>

These functions are part of the [Draft Workbench](Draft_Workbench.md) and can be used in [macros](macros.md) and from the [Python](Python.md) console once the `Draft` module has been imported.

Exempel: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction|cut|FreeCAD.Object, FreeCAD.Object|Returnerar ett klippt objekt som gjorts från skillnaden mellan 2 givna objekt. Originalobjekten göms.|Det nyligen skapade objektet}}


{{APIFunction|extrude|FreeCAD.Object, Vector|Extruderar det givna objektet i den riktning som ges av vektorn. Originalobjektet göms.|Det nyligen skapade objektet}}


{{APIFunction|formatObject|FreeCAD.Object, [FreeCAD.Object]|Denna funktion tillämpar de nuvarande egenskaperna som ställts in i Skiss verktygslådan på det givna objektet (linjefärg och linjebredd), eller om ett andra objekt är specificerat så kopieras egenskaperna från det. Det placerar också objektet i konstruktionsgruppen om konstrktion knappen trycks ned.|Ingenting}}


{{APIFunction|fuse|FreeCAD.Object, FreeCAD.Object|Returnerar ett objekt som gjorts från föreningen av de 2 givna objekten. Om objekten är koplanära, så används en speciell Skisstråd, annars så är det slutliga objektet an standard Del förening.|Det nyligen skapade objektet}}


{{APIFunction|getDraftPath|[string]|Returnerar användaren eller systemsökvägen varifrån Skissmodulen körs. Om en delsökväg eller filnamn anges, så returneras den fulla sökvägen till delsökvägen inuti Skiismodulen.|En filsökväg}}


{{APIFunction|getGroupContents|list|Skannar den givna listan rekursivet efter grupper. Om grupper hittas, så adderas dess innehåll till llistan.|En lista med FreeCAD Objekt}}


{{APIFunction|getRealName|string|Tar bort efterföljande nummer fårn ett objektnamn.|Det nedkortade objektnamnet}}


{{APIFunction|getSelection| |Returnerar det nuvarande FreeCAD valet.|Det nuvarande FreeCAD valet.}}


{{APIFunction|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|Skapar ett cirkelobjekt med given radie. Om en placering ges, så används den. Om facemode är falskt, så visas cirkeln som en trådram, annars som en yta. Om startangle OCH endangle är givna (i grader), så används de och objektet visas som en cirkelbåge.|Det nyligen skapade objektet.}}


{{APIFunction|makeDimension|Vector, Vector, [Vector] or FreeCAD.Object, int, int, [Vector]|Skapar ett Dimensioneringsobjekt som mäter distansen mellan den första och den andra vektorn, med dimensionslinjen passerande genom den tredje vektorn. Nuvarande linjebredd och färg från Skissverktygslådan kommer att användas. Istället för 2 vektorer, så kan du även använda ett FreeCAD objekt, och två heltal (och valfritt, en vektor där dimensionlinjen måste passera). I det fallet, så kommer dimensionen att associeras med objektet, och mäta två av dess hörn, som indikeras av de två givna indexnumren.|Det nyligen skapade objektet.}}


{{APIFunction|makeLine|Vector, Vector|Skapar en linje mellan de två givna vektorerna. Nuvarande linjebredd och färg från Skissverktygslådan kommer att användas.|Det nyligen skapade objektet.}}


{{APIFunction|makeRectangle|length, width, [placement], [facemode]|Skapar ett Rektangelobjekt med längden i X riktningen och höjden i Y riktningen. Om en placering ges, så navänds den. Om facemode är falskt, så visas rektangeln som en trådram, annars som en yta. Nuvarande linjebredd och färg från Skissverktygslådan kommer att användas.|Det nyligen skapade objektet.}}


{{APIFunction|makeText|string or list, [Vector], [screenmode]|Skapar ett Textobjekt vid den givna punkten om en vektor finns, som innehåller strängen eller de strängar som ges i listan, en sträng per rad. Nuvarande färg från Skissverktygslådan och texthöjd samt typsnitt som specificerats i alternativ, används. Om screenmode är sant, så kommer texten alltid att visas mot vyriktningen, annars så läggs den på XY planet.|Det nyligen skapade objektet.}}


{{APIFunction|makeWire|list or Part.Wire, [closed], [placement], [facemode]|Skapar ett trådobjekt från den givna listan med vektorer eller från den givna Tråden. Om closed är sant eller om den första och den sista punkten är identisk, så är tråden sluten. Om facemode är Sant (och tråden är sluten), så kommer tråden att visas fylld. Nuvarande linjebredd och färg från Skissverktygslådan kommer att användas.|Det nyligen skapade objektet.}}


{{APIFunction|move|FreeCAD.Object or list, Vector, [copymode]|Flyttar det givna objektet eller objekten som finns i den givna listan, i den riktning och distans som indikeras av den givna vektorn. Om copymode är Sant, så flyttas inte de aktuella objekten, utan kopior skapas istället.|Objekt(en) (eller dess kopior om copymode var Sant).}}


{{APIFunction|precision| |Returnerar precisionsvärdet från användarinställningarna i Skiss.|Ett heltal.}}


{{APIFunction|rotate|FreeCAD.Object or list, angle, [center], [axis] ,[copymode]|Roterar det givna objektet eller objekten som finns i den givna listan, med given vinkel runt ett givet centrum, och använder axis som rotationsaxel. Om axis är ospecificerat, så kommer rotationen at ske runt den vertikala Z axeln. Om copymode är Sant, så flyttas inte de aktuella objekten, utan kopior skapas istället.|Objekt(en) (eller dess kopior om copymode var Sant).}}


{{APIFunction|scale|FreeCAD.Object or list, vector, [center], [copymode]|Skalar det givna objektet eller objekten som finns i den givna listan  med en skalfaktor don definieras av den givna vektorn (i X, Y och Z riktningarna) runt ett givet centrum. Om copymode är Sant, så flyttas inte de aktuella objekten, utan kopior skapas istället.|Objekt(en) (eller dess kopior om copymode var Sant).}}


{{APIFunction|select|FreeCAD.Object|Avmarkerar allting och markerar bara det givna objektet|Ingenting.}}


{{APIFunction|shapify|FreeCAD.Object|Omvandlar ett parametriskt formobjekt till icke-parametriskt.|Det nya objektet.}}


{{APIFunction|draftify|FreeCAD.Object or list|Omvandlar det givna objektet eller varje objekt i den givna listan till Skiss parametriska trådar.|Ingenting.}}


{{APIFunction|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|Skapar en SVG representation av det givna objektet. linemodifier attributet är en skalfaktor (i procent) för linjebredd, och textmodifier för textstorlek. Du kan alternativt också ange en tupel med vektorer för att definiera ett projektionsplan, annars så kommer geometrin att projiceras på XY planet.|en sträng som innehåller en SVG representation av det givna objektet.}}


 




[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)
