# Embedding FreeCAD/sv
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

FreeCAD har den fantastiska förmågan att kunna importeras som en python modul i andra program eller i en python konsol, tilsammans med alla dess moduler och komponenter. Det är även möjligt att importera FreeCAD\'s gränssnitt som en python modul \-- emellertid med några begränsningar.


</div>


<div class="mw-translate-fuzzy">

### Använda FreeCAD utan gränssnitt 


</div>


<div class="mw-translate-fuzzy">

En första, direkt, lätt och användbar sak du kan göra med detta är att importera FreeCAD dokument in till ditt program. I det följande exemplet, så kommer vi att importera Del geometrin i ett FreeCAD dokument till [blender](http://www.blender.org). Här är det kompletta skriptet. Jag hoppas att du kommer att bli imponerad av dess enkelhet:


</div>


{{Code|lang=python|code=
<nowiki>
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

Den första, viktiga delen är att försäkra sig om att python kan hitta vårt FreeCAD bibliotek. När den väl har hittats, så kommer alla FreeCAD moduler som Del, som vi kommer använda, automatiskat att vara tillgängliga. Så vi tar bara sys.path variabeln, vilket är var python söker efter moduler, och lägger till sökvägen till FreeCAD\'s bibliotek. Denna ändring är endast temporär, och kommer att förloras när vi stänger vår python tolk. Ett annat sätt kan vara att göra en länk till ditt FreeCAD bibliotek i en av python\'s sökvägar. Jag behöll sökvägen i en konstant (FREECADPATH) så att det blir lättare för en annan användare av skriptet att konfigurera den till sitt eget system.


</div>


{{Code|lang=python|code=
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
}}


<div class="mw-translate-fuzzy">

När vi är säkra på att biblioteket är laddat(try/except sekvensen), så kan vi nu arbeta med FreeCAD, på samma sätt som vi skulle inuti FreeCAD\'s egen python tolk. Vi öppnar FreeCAD dokumentet som skickats till oss genom main() funktionen, och vi gör en lista på dess objekt. Sedan då vi valde att endast bry oss om Del geometri, så kontrollerar vi om varje objekts Typegenskap innehåller \"Part\", sedan tesselerar vi den.


</div>


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

Tesseleringen producerar en lista på hörn och en lista på ytor som definierats av hörnindexen. Detta är perfekt, eftersom det är på exakt samma sätt som blender definierar nät. Så vår uppgift är löjligt enkel, vi adderar bara båda listinnehållen till verts och faces av ett blender nät. När allting är gjort, så ritar vi bara om skärmen, och det är klart!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}


<div class="mw-translate-fuzzy">

Detta skript är förstås mycket enkelt (det finns ett mer avancerat [här](http://yorik.orgfree.com/scripts/import_freecad.py)), du kanske vill bygga ut det, för att till exempel importera nätobjekt också, eller importera Del geometri som inte har några ytor, eller importera andra filformat som FreeCAD kan läsa. Du kanske också vill exportera geometri till ett FreeCAD dokument, vilket kan göras på samma sätt. Du kanske också vill bygga en dialog, så att användaren kan välja vad som ska importeras, etc\... Skönheten i allt detta ligger i det faktum att du låter FreeCAD göra grundarbetet medan du presenterar dess resultat i ett program som du väljer.


</div>


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.


<div class="mw-translate-fuzzy">

### Använda FreeCAD med gränssnitt 


</div>

Från och med version 4.2 så har Qt den fängslande förmågan att inbädda Qt-gränssnitt-beroende plugins till icke-Qt värdapplikationer och dela värdens händelseslinga.

Speciellt för FreeCAD så betyder detta att den kan importeras från en annan applikation med hela gränssnittet där värdapplikationen har full kontroll över FreeCAD.

Hela python koden för att uppnå detta har bara två rader


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Om värdapplikationen är baserad på Qt så ska denna lösningen fungera på alla plattformar som Qt stöder. emellertid så ska värden länka samma Qt version som FreeCAD, annars såkan du få oväntade fel.

Men för icke-Qt applikationer så finns det en del begränsningar som du måste vara uppmärksam på. Denna lösning fungerar troligen inte tillsammans med alla andra verktygskiten.

I Windows så fungerar det så länge som värdapplikationen är direkt baserad på Win32 eller något annat verktygskit som internt använder Win32 API som wxWidgets, MFC eller WinForms. för att få det att fungera under X11 så måste värdapplikationen länka till \"glib\" biblioteket.

Notera att för konsolapplikationer fungerar inte denna lösning eftersom det inte finns någon händelseslinga som körs.

## Caveats

Although it is possible to import FreeCAD to an external Python interpreter, this is not a common usage scenario and requires some care. Generally, it is better to use the Python included with FreeCAD, run FreeCAD via command line, or as a subprocess. See [Start up and Configuration](Start_up_and_Configuration.md) for more on the last two options.

Since the FreeCAD Python module is compiled from C++ (rather than being a pure Python module), it can only be imported from a compatible Python interpreter. Generally this means that the Python interpreter must be compiled with the same C compiler as was used to build FreeCAD. Information about the compiler used to build a Python interpreter (including the one built with FreeCAD) can be found as follows: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Embedding FreeCAD/sv
