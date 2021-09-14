# Scenegraph/sv




{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Den geometri som syns i FreeCAD\'s \#D vyer är renderade av Coin3D biblioteket. Coin3D är en implementering av [OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor) standarden. openCascade mjukvaran erbjuder också samma funktionalitet, men det beslöts när FreeCAD påbörjades att inte använda openCascade\'s inbyggda visare utan istället använda sig av den snabbare coin3D mjukvaran.


</div>

## Description


<div class="mw-translate-fuzzy">

[OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor) är egentligen ett 3D scen beskrivningsspråk. Den scen som beskrivs i renderas sedan av OpenGL på din skärm. Coin3D gör arbetet med detta, så programmeraren inte behöver bry sig om komplexa openGL anrop, programmeraren behöver bara förse den med giltig OpenInventor kod. Den stora fördelen är att openInventor är en mycket välkänd och väldokumenterad standard.


</div>


<div class="mw-translate-fuzzy">

Ett av de stora jobben som FreeCAD gör för dig är att översätta openCascade geometriinformation till openInventor språket.


</div>


<div class="mw-translate-fuzzy">

OpenInventor beskriver en 3D scen i formen av en [scenegraph](http://en.wikipedia.org/wiki/Scene_graph), som den nedan:


</div>

![](images/Scenegraph.gif )


<div class="mw-translate-fuzzy">

![](images/Scenegraph.gif ) image from [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html)


</div>


<div class="mw-translate-fuzzy">

En openInventor scengraf beskriver allt som utgör en 3D scen, som geometri, färger, material, ljus, etc, och organiserar all den data i smidig och klar struktur. Allting kan grupperas till sub-strukturer, vilket tillåter dig att organisera ditt sceninnehåll så som du vill. Här är ett exempel på en openInventor fil:


</div>


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}


<div class="mw-translate-fuzzy">

Som du kan se, så är strukturen mycket simpel. Du använder separatorer för att organisera din data till block, lite som du skulle organisera dina filer i mappar. Varje uttryck påverkar vad som kommer härnäst, till exempel de första två punkterna i vår rot separator är en rotation och en förflyttning, båda kommer att påverka nästa punkt, vilken är en separator. I den separatorn, så är ett material definierat, och en annan förflyttning. Vår cylinder kommer därför att påverkas av båda förändringarna, den som vi lade direkt på den och den som vi lade på dess förälderseparator.


</div>


<div class="mw-translate-fuzzy">

Vi har också många andra elementtyper för att organisera vår scen, som grupper, växlar eller annoteringar. Vi kan definiera mycket komplexa material för våra objekt, med färg, texturer, skugglägen och transparens. Vi kan också definiera ljus, kameror, och även rörelser. Det är även möjligt att bädda in skriptbitar i openInventor filer, för att definiera mer komplext beteende.


</div>


<div class="mw-translate-fuzzy">

Om du är intresserad av att lära dig mer om openInventor, hoppa direkt till dess berömdaste referens, [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html).


</div>


<div class="mw-translate-fuzzy">

I FreeCAD behöver vi normalt inte interagera direkt med scengrafen openInventor. Varje objekt i ett FreeCAD dokument, ett nät, en delform eller något annat, blir automatiskt konverterat till openInventor kod och insatt i huvudscengrafen som du ser i en 3D vy. Den scengrafen uppdateras kontinuerligt när du gör förändringar, lägger till eller tar bort objekt i dokumentet. Alla objekt (i App rymden) har en visare(ett motsvarande objekt i Gui rymden), som anvarar för att ge openInventor kod.


</div>


<div class="mw-translate-fuzzy">

Men det finns många fördelar med att kunna komma åt scengrafen direkt. Vi kan till exempel temporärt ändra utseendet på ett objekt, eller vi kan lägga till objekt som inte har en reell existens i FreeCAD dokumentet, som till exempel konstruktionsgeometri, hjälpare, grafiska tips eller verktyg som manipulatorer eller information på skärmen.


</div>

Själva FreeCAD har flera verktyg för att se eller ändra openInventor kod. Till exempel, följande pythonkod kommer att visa openInventor representationen av ett valt objekt: 
```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```


<div class="mw-translate-fuzzy">

Men vi har också en python modul som tillåter komplett åtkomst till allt som hanterar av Coin3D, som vår FreeCAD scengraf. Så, läs vidare på [Pivy](Pivy/sv.md).


</div>

## Coding examples 

See [Coin3d snippets](Coin3d_snippets.md) courtesy of MariwanJ\'s research for the [Design456 Workbench](Design456_Workbench.md). The code repository of said examples can be found at <https://github.com/MariwanJ/COIN3D_Examples>.

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md)
