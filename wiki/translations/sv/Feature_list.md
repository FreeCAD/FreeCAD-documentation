 


<div class="mw-translate-fuzzy">

Detta är en extensiv, fast inte komplett, lista på de funktioner som FreeCAD har. Om du vill se in i framtiden, se [utvecklingskartan](Development_roadmap/sv.md) för en snabb överblick så är [Skärmdumpar](Screenshots/sv.md) en bra plats att gå till.


</div>


{{TOCright}}

## Release notes 

-   [Release 0.11](Release_notes_0.11.md) - March 2011
-   [Release 0.12](Release_notes_0.12.md) - December 2011
-   [Release 0.13](Release_notes_0.13.md) - January 2013
-   [Release 0.14](Release_notes_0.14.md) - March 2014
-   [Release 0.15](Release_notes_0.15.md) - March 2015
-   [Release 0.16](Release_notes_0.16.md) - April 2016
-   [Release 0.17](Release_notes_0.17.md) - April 2018
-   [Release 0.18](Release_notes_0.18.md) - March 2019
-   [Release 0.19](Release_notes_0.19.md) - March 2021
-   [Release 0.20](Release_notes_0.20.md) - TBD

## Allmäna funktioner 


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) En komplett [OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE)-baserad **geometrikärna** som tillåter komplexa 3D operationer på komplexa formtyper, och stöder nativt koncept som brep, nurbs, booleska operationer eller fasningar 
-   ![](images/Feature3.jpg ) En full **parametrisk modell** som tillåter valfri typ av parameter-drivna anpassade objekt, som även [helt kan programmeras i python](Scripted_objects/sv.md) 
-   ![](images/Feature4.jpg ) Komplett åtkomst från den inbyggda **python** tolken, makron eller externa skript till nästan alla delar i FreeCAD, so till exempel [skapande och omvandling av geometri](Topological_data_scripting/sv.md), 2D eller 3D representationen av den geometrin ([Scengrafen](scenegraph/sv.md)) eller även [FreeCAD gränssnittet](PySide/sv.md) 
-   ![](images/Feature5.jpg ) Import/export till **standard format** som [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://sv.wikipedia.org/wiki/Obj), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://sv.wikipedia.org/wiki/Svg) [U3D](http://en.wikipedia.org/wiki/Universal_3D) eller [STL](http://en.wikipedia.org/wiki/STL_(file_format))
-   ![](images/Feature7.jpg ) En [Skissare](Sketcher_Workbench/sv.md) med begränsningslösare, som låter dig skissa geometri-begränsade 2D former. Skissare tillåter dig för tillfället att bygga flera typer av begränsad geometri, och sedan använda dem som en bas att bygga andra objekt i FreeCAD.
-   ![](images/Feature9.jpg ) En [Robot simulerings](Robot_Workbench/sv.md) modul som tillåter dig att studera robotrörelser. Robotmodulen har redan ett utökat grafiskt gränssnitt, vilket kan användas för ett smidigt arbetsflöde. 
-   ![](images/Feature8.jpg ) En [Ritningsark](Drawing_Workbench/sv.md) modul som låter dig skapa 2D vyer på dina 3D modeler på ett ritningsark. Denna modul producerar sedan färdiga SVG eller PDF dokument. Modulen är ännu funktionsfattig, men har redan en kraftfull python-funktionalitet.
-   ![](images/Feature-raytracing.jpg ) En [Renderingsmodul](Raytracing_Workbench/sv.md) som kan exportera 3D objekt för rendering med externa rendererare. Stödjer för närvarande endast [povray](http://sv.wikipedia.org/wiki/POV-Ray), men förväntas stödja andra renderare i framtiden.
-   ![](images/Feature-arch.jpg ) En [Arkitektur](Arch_Workbench/sv.md) modul som tillåter [BIM](http://sv.wikipedia.org/wiki/Building_Information_Modeling)-likt arbetsflöde, med [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) kompatibilitet. Skapandet av arkitekturmodulen diskuteras mycket av communityn [här](http://forum.freecadweb.org/viewtopic.php?f=10&t=821).

[BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)-like workflow, with [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) compatibility. The making of the Arch Workbench is heavily discussed by the community [here](http://forum.freecadweb.org/viewtopic.php?f=10&t=821).


</div>


<div class="mw-translate-fuzzy">

## Allmänna funktioner 


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD är multi-plattform**. Det kan köras och beter sig på exakt samma sätt på Windows Linux och Mac OSX plattformarna.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD är en helgrafisk applikation**. FreeCAD har ett komplett grafiskt användargränssnitt baserat på det berömda [Qt](http://www.qtsoftware.com/) strukturen, med en 3D visare baserad på [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor), vilket tillåter snabb rendering av 3D scener och en mycket lättåtkomlig scenrepresentation.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD kan också köras som en kommandolinje applikation**, med litet minnesbehov. I kommandolinje läge, så körs FreeCAD utan ett gränssnitt, men med alla geometriverktyg. Det kan till exempel användas som en server för att producera data för andra applikationer.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD kan importeras som en [Python modul](Embedding_FreeCAD/sv.md)**, inuti andra applikationer som kan köra python skript, eller i en python konsol. Som i konsol läge, så är FreeCAD\'s gränssnitt otillgängligt, men alla geometriverktyg finns tillgängliga.


</div>


<div class="mw-translate-fuzzy">

-   **Arbetsbänk koncept**: I FreeCAD gränssnittet, så är verktygen grupperade i [arbetsbänkar](Workbenches/sv.md). Detta innebär att endast de verktyg som behövs för att utföra en viss uppgift visas, vilket håller arbetsytan ren och responsiv, och snabb laddning av applikationen.


</div>


<div class="mw-translate-fuzzy">

-   **Plugin/Modul struktur för sen laddnig av funktioner/data-typer**. FreeCAD är uppdelat i en kärnapplikation och moduler, som endast laddas när de behövs. Nästan alla verktyg och geometrityper är lagrade i moduler. Moduler beter sig som plugins, och kan adderas eller tas bort från en existerande installation av FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   **Parametriska associativa dokumentobjekt**: Alla objekt i ett FreeCAD dokument kan definierass av parametrar. Dessa parametrar kan ändras direkt, och omberäknas när som helst. Förhållandet mellan objekt lagras också, så om ett objekt ändras, så ändras även de objekt som är beroende av det.


</div>


<div class="mw-translate-fuzzy">

-   **Parametriska primitiver** som låda, sfär, cylinder, kon eller torus.


</div>


<div class="mw-translate-fuzzy">

-   Grafiska **ändringsoperationer** som förflyttning, rotation, skalning, spegling, offset (trivial or after \[<http://www.ann.jussieu.fr/~frey/papers/meshing/Jung%20W>.,%20Self-intersection%20removal%20in%20triangular%20mesh%20offsetting.pdf Jung/Shin/Choi\]) eller formförändring, i valfritt plan i 3D rymden


</div>


<div class="mw-translate-fuzzy">

-   **[Booleska operationer](http://en.wikipedia.org/wiki/Constructive_solid_geometry)** som **förening**, **skillnad** och **skärning**.


</div>


<div class="mw-translate-fuzzy">

-   Grafiskt skapande av**enkel plangeometri** som linjer, trådar, rektanglar, cirkelbågar eller cirklar i valfritt plan i 3D rymden


</div>


<div class="mw-translate-fuzzy">

-   Modellering med raka eller rotering **extrusioner**, **sektioneringar** och **avrundningar**.


</div>


<div class="mw-translate-fuzzy">

-   Topologiska komponenter som **hörn, kanter, trådar** och **plan** (via pythonskript).


</div>


<div class="mw-translate-fuzzy">

-   **Testing and repairing** tools for meshes: solid test, non-two-manifolds test, self-intersection test, hole filling and uniform orientation.


</div>


<div class="mw-translate-fuzzy">

-   **Anteckningar** som texter eller dimensioner


</div>


<div class="mw-translate-fuzzy">

-   **Ångra/Gör om struktur**: Allt kan ångras eller göras om, med åtkomst till ångra minnet, så multipla steg kan ångras åt gången.


</div>


<div class="mw-translate-fuzzy">

-   **Transaktionshantering**: Ångra/Gör om minnet lagrar dokumenttransaktioner och inte enstaka aktioner, vilket tillåter varje verktyg att exakt definiera vad som ska ångras eller göras om.


</div>


<div class="mw-translate-fuzzy">

-   **Inbyggd [skript](Scripting/sv.md) struktur**: FreeCAD tillhandahåller en inbyggd [Python](http://www.python.org/) tolk, och ett API som täcker nästan alla delar av applikationen, gränssnittet, geometrin och representationen av denna geometri i 3D visaren. Tolken kan köra från enstaka kommandon upp till komplexa skript, faktum är att hela moduler kan programmeras helt och hållet i Python.


</div>


<div class="mw-translate-fuzzy">

-   **Inbyggd Python konsol** med syntaxmarkering, autokomplettering och klassvisare: Python kommandon kan utföras direk i FreeCAD och ge resultat omedelbart, vilket tillåter skriptskrivare att testa funktionaliteten direkt, utforska modulernas innehåll och lätt lära sig FreeCAD\'s innanmäte.


</div>


<div class="mw-translate-fuzzy">

-   **Användarinteraktion speglas i konsolen**: Allt som användaren gör i FreeCAD\'s gränssnitt, kör pythonkod, vilken kan skrivas ut i konsolen och spelas in i makron.


</div>


<div class="mw-translate-fuzzy">

-   **Full makro inspelning & redigering**: De pythonkommandon som körs när användaren manipulerar gränssnittet kan spelas in, om nödvändigt redigeras, och sparas för att reproduceras senare.


</div>


<div class="mw-translate-fuzzy">

-   **Sammansatt (ZIP baserat) dokumentformat**: FreeCAD dokument som är sparade med filtypen .fcstd kan innehålla många olika informationstyper, som geometri, skript eller tumnagelikoner.


</div>


<div class="mw-translate-fuzzy">

-   **Fullt anpassningsbart/skriptbart grafiskt användargränssnitt**. Det [Qt](http://www.qtsoftware.com)-baserade gränssnittet i FreeCAD är helt åtkomligt via python tolken. Förutom de enkla funktioner som FreeCAD själv ger till arbetsbänkarna, så är hela Qt strukturen också tillgänglig, vilket tillåter vilken operation som helst på gränssnittet, som till exempel skapa, lägga till, docka, ändra eller ta bort widgets och verktygslådor.


</div>


<div class="mw-translate-fuzzy">

-   **Tumnaglare** (endast Linux system för närvarande): FreeCAD\'s dokumentikoner visar filens innehåll i de flesta filhanterarapplikationer som till exempel gnome\'s nautilus.


</div>


<div class="mw-translate-fuzzy">

-   **en modulär MSI installerare** tillåter flexibel installation på Windowssystem. Paket för Ubuntusystem är också underhållna.


</div>

## I utveckling 


<div class="mw-translate-fuzzy">

-   ![](images/Feature-assembly.jpg ) An [Församling](Assembly_project/sv.md) modul som gör det möjligt för att arbeta med flera projekt, flera former, flera dokument, flera filer, flera relationer\...
-   ![](images/Feature-CAM.jpg ) [CAM modulen](Cam_Module/sv.md) är tillägnad mekanisk bearbetning som till exempel fräsning. Denna modul har just påbörjats och är för tillfället mest tillägnad [Inkrementell plåtformning](http://en.wikipedia.org/wiki/Incremental_sheet_forming). Fastän det finns en del algoritmer för verktygsväg planering, så är de inte användbara för slutanvändaren för tillfället.


</div>

## Extra Workbenches 

Power users have created various custom [external workbenches](external_workbenches.md).


<div class="mw-translate-fuzzy">


{{docnav/sv|About_FreeCAD/sv|Install on Windows/sv}}


</div>




[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
