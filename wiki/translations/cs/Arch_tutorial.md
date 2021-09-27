# Arch tutorial/cs
<div class="mw-translate-fuzzy">


{{TutorialInfo/cs
|Topic=Modeling
|Level=Intermediate
|Time=
|Author=_
|FCVersion=0.14
|Files=
}}


</div>

![](images/Arch_tutorial_00.jpg )

## Úvod


<div class="mw-translate-fuzzy">

Záměrem výukového program je představit základy práce v _. Jestliže nemáte žádné zkušenosti s FreeCADem, existuje stránka [Začínáme](Getting_started/cs.md), kterou byste si měli přečíst. Také si projděte naši stránku [Výukové programy](tutorials/cs.md) a na stránce [youtube](http://www.youtube.com/results?search_query=freecad) najdete také spoustu dalších výukových programů FreeCADu.


</div>


<div class="mw-translate-fuzzy">

Cílem _ významně využívá výhod ostatních disciplín, které FreeCAD poskytuje a nabízí některé vlastnosti, které jsou zřídka viděny u tradičních BIM aplikací.


</div>


<div class="mw-translate-fuzzy">

Zde je například několik zajímavých vlastností [Pracovní plochy Architektura ](Arch_Workbench/cs.md) ve FreeCADu, které byste obtížně hledali v jiných BIM aplikacích:


</div>

-   Architektonické objekty jsou vždy tělesa. Ze silných mechanických základů FreeCADu známe důležitost toho aby strukturální objekty byly vždy tělesy. To zajišťuje mnohem bezchybnější práci a velmi spolehlivé logické operace. Protože možnost dělat kapsy ve 3D objektech pomocí 2D plochy je také logická operace, hned vidíte důležitost v takovém případě.

-   Stavební objekty mohou mít kdykoliv jakýkoliv tvar. Nejsou žádná omezení. Zdi nemusejí být svislé, desky nemusejí vypadat jako desky. Jakékoliv těleso se může kdykoliv stát stavebním objektem. Velmi složité věci, obyčejně těžce definovatelné v jiných BIM aplikacích, jako jsou podlahové desky zatáčející se nahoru a přecházející v zeď (ano Zaho Hadide, to je to o čem jsi mluvil), nepředstavují žádný mimořádný problém ve FreeCADu.


<div class="mw-translate-fuzzy">

-   Celou sílu FreeCDAu máte na špičce prstu. Můžete vytvářet architektonické objekty pomocí jakéhokoliv nástroje FreeCADu, jako je [Pracovní plocha Návrh dílu](PartDesign_Workbench/cs.md) a když jsou připraveny, konvertujete je do architektonických objektů. Objekty si podrží celou svoji modelovací historii a jsou dále zcela editovatelné. [Pracovní plocha Atchitektura](Arch_Workbench/cs.md) také dědí mnoho z funkcionality [Pracovní plochy Kreslení](Draft_Workbench/cs.md) jako je třeba [zachycování](Draft_Snap/cs.md) a [pracovní roviny](Draft_SelectPlane/cs.md).


</div>


<div class="mw-translate-fuzzy">

-   /cs\|Pracovní plocha Architektura je velmi spřátelená s [modulem síť](Mesh_Workbench/cs.md). Snadno můžete vytvářet architektonické modely v aplikacích založených na sítích jako je [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) nebo [SketchUp](http://en.wikipedia.org/wiki/Sketchup) a importovat je do FreeCADu. Jestliže se staráte o kvalitu Vašeho modelu a jeho objekty jsou non-manifold (nejsou různorodá) tělesa, jejich převod do architektonických objektů vyžaduje pouze stisknutí tlačítka.


</div>


<div class="mw-translate-fuzzy">

V době, kdy je psán tento text, [Pracovní ploch Architektura](Arch_Workbench/cs.md), stejně jako zbytek FreeCADu trpí některými omezeními. Nicméně, na většině se pracuje a budou k dispozici později.


</div>


<div class="mw-translate-fuzzy">

-   FreeCAD není 2D aplikace. Je dělán pro 3D. Je v něm dostatečné množství nástrojů pro kreslení a úpravy 2D objektů v [Pracovní ploše Kreslení](Draft_Workbench/cs.md) a [Pracovní ploše Skicář](Sketcher_Workbench/cs.md), ate ty nejsou určeny pro práci s velkými a (někdy špatně nakreslenými) 2D CAD soubory. Běžně můžete uspěšně importovat 2D soubory, ale neočekávejte vysoký výkon, pokud na nich budte chtít pokračovat ve 2D. Byli jste varováni.


</div>


<div class="mw-translate-fuzzy">

-   Žádná podpora materiálů. FreeCAD bude mít kompletní [Materiálový](Material/cs.md) systém, který bude schopen definovat velmi komplexní materiály, se všemi výhodmai, které můžete očekávat (uživatelské vlastnosti, materiálové skupiny, vykreslování a vizuální vlastnosti, atd.) a [pracovní plocha Architektura](Arch_Workbench/cs.md) jej bude využívat hned jak bude připraven.


</div>

-   Je nainstalována velmi předběžbé podpora _, poskytované z [IfcOpenShell](http://ifcopenshell.org), ale exportování ještě není oficiálně podporováno. Vývojáři pracují na FreeCADu i na IfcOpenShellu a v budoucnu můžeme očekávay plnou podporu IFC.

-   Mnogo nástrojů Architektury je stále ještě ve vývoji. Znamená to, že automatické \"wizardy\", které jsou schopny vytvářet automaticky komplexní konstrukce, jako jsou [Střecha](Arch_Roof/cs.md) nebo [Schody](Arch_Stairs/cs.md) mohou zatím vytvářet jen určité typy těchto objektů a další nástroje, které mají předvolby jako jsou [Struktura](Arch_Structure/cs.md) nebo [Okno](Arch_Window/cs.md) mají jen několik základních předvoleb. To se samozřejmě časem zlepší.


<div class="mw-translate-fuzzy">

-   [Vztahy mezi objekty](Assembly_project/cs.md) ve FreeCADu stále ještě nejsou oficiálně dostupné. Tyto vztahy, např. vztah mezi oknem jaho hostující zdí, jsou v současné době implementovány do [pracovní plochy Architektura](Arch_Workbench/cs.md) pomocí dočasných (a proto poněkud omezených) metod. Přibude mnoho nových možností až bude tato vlastnost plně funkční.


</div>

-   Vlastnost [Jednotky](Units/cs.md) jsou právě implementovány ve FreeCADu, což umožňuje práci s jakýmikoliv jednotkami (dokonce i imperiálními jednotkami, vy hoši z USA můžete být trvale vděční Jürgenovi, patronovi a hlavnímu šéfoviFreeCADu). Ale v tomto okamžiku není implementace kompletní a pracovní plocha Architektura zatím tyto jednotky nepodporuje. Zatím musíte počítat s tím, že je \"bezjednotková\".


<div class="mw-translate-fuzzy">


{{Note|FreeCAD verze 0.14 je požadována|Tento výukový program byl psán za použití [FreeCAD verze 0.14](Release_notes_014/cs.md). Pokud budete zkoušet podle tohoto programu, budete potřebovat minimálně tuto verzi. Dřívější verze nemusejí obsahovat všechny potřebné nástroje nebo volby používané zde.}}


</div>

## Typický pracovní postup 


<div class="mw-translate-fuzzy">

[Pracovní plocha Architektura](Arch_Workbench/cs.md) je připravena hlavně pro dva druhy pracovních postupů:


</div>

-   Vytvoří se model v rychlejší, na sítích založené aplikaci jako je [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) nebo [SketchUp](http://en.wikipedia.org/wiki/Sketchup) a ten se importuje do FreeCADu za účelem extrakce plánů a řezů. FreeCAD je zařízen na přesné modelování na mnohem vyšší úrovni než je vyadováno v architektuře. Vytváření modelů přímo ve FreeCADu může být obtížné a pomalé. Z toho důvodu má tento pracovní postup velké výhody. Popsal jsem to v [tomto článku](http://yorik.uncreated.net/guestblog.php?2012=180) na mém blogu. Jestli máte zájem modelovat správně a přesně (clean, solid, non-manifold meshes), dává Vám tento pracovní postup stejnou úroveň výkonu a přesnosti jako jiné.


<div class="mw-translate-fuzzy">

-   Vytváření modelu přímo ve FreeCADu. To je to co Vám ukážu v tomto výukovém programu. Většinou budeme využívat tři pracovní plochy: [Architektura](Arch_Workbench/cs.md), samozřejmě, ale také [Kreslení](Draft_Workbench/cs.md), jehož všechny nástroje jsou včleněny do Architektury, takže není potřeba přepínat pracovní plochy a [Skicář](Sketcher_Workbench/cs.md). S výhodou to můžete udělat jak to běžně dělám já, že si vytvořím uživatelský nástrojový pruh v pracovní ploše Architektura, pomocí Nástroje → Uživatelské, a přidám ze Skicáře nástroje, které budu často používat. Toto je moje \"uživatelská\" pracovní plocha Architektura:


</div>

![](images/Arch_tutorial_01.jpg )

V tomto výukovém programu budeme modelovat dům ve 3D, založený na 3D výkresu, který stáhneme z netu a extrahujeme z 2D dokumentu plány, výšky a řezy.

## Příprava

Místo vytváření projektu od začátku, vezměme si pro modelování projekt z příkladu, ušetří nám to čas. Vybral jsem nádherný dům známého architekta [Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) (podívejte se na sérii [obrázků](http://www.leonardofinotti.com/projects/architects-second-house/image/40409-130405-010d) od Leonardo Finotti), protože je to blízko od mého bydliště, protože je to jednoduché a protože je to parádní příklad modernistické architektury v Sao Paulu a dwg výkresy jsou [snadno dostupné](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#).

Použijeme 2D DWG výkresy získané z odkazu nahoře (musíte se registrovat ke stažení, ale je to zdarma) jako základ pro tvorbu našeho modelu. Takže první věc je stažení souboru, jeho rozzipování a otevření DWG souboru v nějaké dwg aplikaci jeko je třeba _. Ale protože tyto soubory často mívají špatnou kvalitu a jsou velmi těžkopádné, je obyčejně lepší otevřít je ve 2D CAD aplikaci a pročistit je.

Zde jsem vyhodil všechny výkresy detailů, všechny rámečky s informacemi o výkrese, \"vyčistil\" jsem jej (v AutoCADu je to \"purge\") pro odstranění všech zbytečných entit, zreorganizoval jsem řezy do logického umístění v relaci s ohledem na plán a přesunul jsem všechno k počátku (0,0). Potom může být náš soubor otevřen ve FreeCADu efektivně. Zkontrolujte různé odlišné volby dostupné v menu Úpravy → Předvolby → Kreslení → Import/Export, které mohou ovlivnit jak (a jak rychle) jsou soubory DXF/DWG importovány.

Takto vypadá soubor po otevření ve FreeCADu. Změnil jsem taky tloušťku zdí (obsah skupiny \"muros\") a prohodil pár dveří, které byly importovány se špatným měřítkem v ose X, pomocí nástroje [Kreslení Měřítko](Draft_Scale/cs.md):

![](images/Arch_tutorial_02.jpg )

[DXF importer](Draft_DXF/cs.md) (který se také umí postarat o DWG soubory, protože při importu DWG souborů jsou nejdříve jednoduše zkonvertovány do DXF) seskupuje importované objekty podle vrstev. Ve FreeCADu nejsou vrstvy, ale [skupiny](Std_CreateGroup/cs.md). [Skupiny](Std_CreateGroup/cs.md) nabízejí jednoduchý způsob organizace objektů v souborech, ale nemají specifické vlastnosti jako vrstvy v AutoCADu, které se aplikují na jejich obsah. Ale mohou být umístěny uvnitř jiných skupin což je velmi šikovné. První věc, kterou zde budeme chtít udělat je vytvořit novou [skupinu](Std_CreateGroup/cs.md) (v [okně stromu](Document_structure/cs.md)), klikněte pravým tlačítkem myši na ikonu dokumentu, přidejte skupinu, klikněte na ni pravým tlačítkem myši a přejmenujte ji na \"base 2D plans\" a přetáhněte do ní všechny ostatní objekty .

## Výstavba zdí 


<div class="mw-translate-fuzzy">

Jako většina _, [dráty](Draft_Wire/cs.md) (lomené čáry), [náčrty](Sketcher_Workbench/cs.md), plochy nebo tělesa (nebo dokonce na ničem, když jsou definovány výškou, šířkou a délkou). Výsledná konstrukce zdi závisí na konstrukci základu a vlastnostech, které zadáte, jako jsou šířka a výška. Jak asi uhodnete, zeď založená na přímce ji využije jeko přímku, podle které se zeď zarovná, zatímco zeď založená na ploše využije plochu jako svůj základový obrys a zeď založená na tělese jednoduše převezme rozměry zadaného tělesa. To umožňuje jakémukoliv tvaru stát se zdí.


</div>


<div class="mw-translate-fuzzy">

Ve FreeCADu existuje několik možných strategií jak stavět zdi. Jedna umožňuje vystvět kompletní \"plán podlaží\" pomocí _ nad importovaným plánem, jeden pro každý typ zdi:


</div>

![](images/Arch_tutorial_03.jpg )

Jak vidíte nakreslil jsem červeně přímky, ze kterých budou betonové zdi ([vyhledání obrázků](http://www.google.com/search?tbm=isch&q=casa+artigas+brooklin) domu Vám může usnadnit rozlišení různých typů zdí), zelené přímky jsou vnější cihlové zdi a modré přímky se stanou vnitřními zdmi. Přímky procházejí i dveřmi, protože dveře budou vloženy do zdí později a vytvoří si otvory automaticky samostatně. Zdi mohou být k jejich základové přímce zarovnány zleva, zprava nebo centrálně, takže nezáleží na tom, po které straně základovou přímku nakreslíte. Také jsem si dával pozor abych se co nejvíce vyhnul protínáni, protože tak se model stane co nejčistším. Ale o protínání se postaráme později.

Když je to hotovo, můžete všechny tyto přímky umístit do nové [skupinu](Std_CreateGroup/cs.md). Postupně vybírejte přímky a stiskem tlačítka [Zeď](Arch_Wall/cs.md) z nich stavějte zdi. Můžete vybrat i několik přímek zároveň. Po dokončení a úpravě šířek (externí zdi jsou široké 25cm, vnitřní 15cm) a některých zarovnání. My už máme zdi připraveny:

![](images/Arch_tutorial_04.jpg )

Zeď můžeme budovat i z úplného začátku. Když stisknete tlačítko [Zeď](Arch_Wall/cs.md) bez vybraného objektu, můžete kliknout na dva body na obrazovce a nakreslit zeď. Ale na pozadí nástroj Zeď ve skutečnosti nakreslí přímku a na ní postaví zeď. Ale v tomto případě považuji za mnohem poučnější ukázat jak to funguje.

Všimli jste si, že jsem si hodně dával pozor abych nekřížil zdi? Později nám to ušetří hodně bolení hlavy, například když naši práci exportujeme do jiných aplikací, které to nemají rády. Já zde mám pouze jedno křížení, když jsem byl líný nakreslit dva krátké přímkové segmenty a nakreslil jsem jednu velkou lomenou čáru, která překřížila jinou. To musí být opraveno. Naštěstí mají všechny objekty Architektury skvělou vlastnost: můžete přidat jednu na druhou. Když to uděláme, sjednotí se jejich konstrukce, ale stále potom zůstanou editovatelné a nezávislé. Přidání jedné z našich překřížených zdí na druhou uděláme tak, že jednu z nich vybereme, potom CTRL+výběr druhé a stiskneme nástroj [Přidat](Arch_Add/cs.md):

![](images/Arch_tutorial_05.jpg )

Vlevo jsou dvě překřížené zdi, napravo výsledek po přidání jedné na druhou.


<div class="mw-translate-fuzzy">


{{Note|Důležitá poznámka k parametrickým objektům|Existuje něco důležitého s čím je již potřeba počítat. Jak víte, ve FreeCADu je všechno parametrické: Naše nová "sjednocená" zeď je vytvořena ze dvou zdí, z nichž každá je založena na základové přímce. Když je rozbalíte v [okně stromu](Document_structure/cs.md), uvidíte řetěz závislosí. Jak si můžete představit, taková hříčka se rychle může stát velmi složitou. Dále, když už víte jak se pracuje se [skicářem](Sketcher_Workbench/cs.md), mohli bychom chtít nakreslit základové přímky s vazbenými náčrty. Celá ta složitost něco stojí: exponenciálně narůstá množství výpočtů, které msuí FreeCAD provádět aby udržel konstrukci modelu aktuální. Tak, když se nad tím zamyslíte, nezvyšujte zbytečně složitost, pokud to není potřeba. Udržujte správnou rovnováhu mezi jednoduchými a složitými objekty a ty si nechte pro případy, kdy budete složitost skutečně potřebovat.}}


</div>

Například, já jsem mohl nakreslit základové přímky bez ohledu na jejich křížení a upravit to později pomocí nástroje [Přidat](Arch_Add/cs.md). Ale tím bych značně zvýšil složitost modelu bez jakéhokoliv přínosu. Lepší je to dělat správně od začátku a udržovat je jako velmi jednoduché části konstrukce.

Teď už jsou naše zdi v pořádku a potřebujeme zdvihnout jejich výšku až se protne se střechou. Potom, protože zeď nemůže být automaticky useknuta střechou (nicméně jednoho dne k tomu dojde), vytvoříme \"fiktivní\" objekt, který kopíruje tvar střechy, pro odebrání z naší zdi.

Nejprve, když se podíváme na 2D výkresy, vidíme, že nejvyšší bod střechy nad 5.6m nad podlahou. Proto nastavme výšku naší zdi na 6m a tím si zajistíme, že bude odebrána naším fiktivním objemem zdi. Můžete se ptát proč 6m a ne 5.6m? Dobrá, jestliže už jste někdy pracovali s logickými operacemi (přidání, odebrání, průniky), musíte už vědět, že tyto operace nemají moc rády \"face-on-face\" (povrch na povrch) situace. Mají rády čisté, opravdu se protínající objekty, Takže, když to uděláme takto, máme to pojištěné.

Pro zdvihnutí výšky naších zdí, jednoduše všechny vyberte (nezapomeňte tu, kterou jsme přidali na další) v okně stromu a změňte hodnotu jejich vlastnosti \"výška\".

Před vytvořením střechy a snížením zdí udělejme i ostatní objekty, které budou potřebovat snížení: Zdi horního studia a sloupy. Zdi studia jsou udělány stejným způsobem, jaký už jsme použili, na plánech horního patra, ale budou zvýšeny na úroveň 2.6m. Proto jim dáme požadovanou výšku, vrchol je ve výšce 6m, takže výška bude 3.4m. Když je to hotovo, zdvihněme zdi na úroveň 2.6m: Obě vybereme, přejdeme do pohledu zepředu (Pohled → Standardní pohledy → Zepředu), stiskněte tlačítko [Posun](Draft_Move/cs.md), vyberte první bod, potom zadejte 0, 2.6, 0 jako souřadnice a stiskněte ENTER. Objekty vyskočí do výšky 2.6m:

![](images/Arch_tutorial_06.jpg )


<div class="mw-translate-fuzzy">


{{Note|O souřadnicích|Objekty [Kreslení](Draft_Workbench/cs.md) a také většina objektů [Architektury](Arch_Workbench/cs.md) se řídí systémem Kreslení zvaným [pracovní roviny](Draft_SelectPlane/cs.md). Tento systém definuje 2D rovinu, na které se budou odehrávat následující operace. Jestliže nedefinujete žádnou rovinu, pak se pracovní rovina přizpůsobí do aktuálního pohledu. To je důvod proč přepínáme do pohledu zepředu a vidíte, že posun v X je 0 a Y je 2.6. Také můžeme určit, že pracovní rovina bude v přízemí, použitím nástroje [výběr roviny](Draft_SelectPlane/cs.md). Pak jsme zadali posun X rovno 0, Y rovno 0 a Z rovno 2.6. }}


</div>

Teď posuňme naše zdi vodorovně na jejich správnou pozici. Protože máme zachycovací body je to snadnější: Vybereme obě zdi, stiskneme nástroj [Posun](Draft_Move/cs.md) a posuneme je z jednoho bodu do druhého:

![](images/Arch_tutorial_07.jpg )

Nakonec jsem změnil barvu některých zdí na cihlovou (je to snadnější pro odlišení) a udělal malou korekci: Některé zdi nejdou až ke střeše, ale skončí na výšce 2.60m. Upravil jsem výšku těchto zdí.

## Zvednutí struktury 

Nyní, protože musíme snížit zdi odebráním objektu, mohli bychom se podívat jestli tam nejsou další objekty, které budou potřebovat tímto způsobem snížit. Jsou tam, některé ze sloupů. To je dobrá příležitost představit další z objektů architektury: [Strukturu](Arch_Structure/cs.md). Objekty struktury se víceméně chovají jako zdi, ale nejsou vytvořeny ze základové přímky. Spíše preferují práci z profilu, který se vysune (podél přímky profilu nebo ne) Jakýkoliv plochý objekt může sloužit jako profil pro strukturu, s jediným požadavkem: musí tvořit uzavřený tvar.

Pro naše sloupy použijeme jinou strategii než jsme použili pro zdi. Místo \"kreslení\" na 2D plánech, použijeme přímo objekty z nich: kružnice, které reprezentují sloupy v pohledu plánu. Teoreticky bychom mohli vybrat jeden z nich a stisknout tlačítko [Struktura](Arch_Structure/cs.md). Nicméně, pokud bychom to udělali takto, vytvoříme \"prázdný\" strukturální objekt. Je to kvůli tomu, že si nikdy nemůžete být jisti jak dobře byly objekty nakresleny v DWG souboru a tyto objekty často nejsou uzavřeny. Takže před jejich zformováním ve sloupy je změníme na plochy dvojnásobným použitím nástroje [Vylepšit](Draft_Upgrade/cs.md). Při prvním je zkonvertujeme do uzavřených drátů (lomených čár), při druhém zkonvertujeme dráty do ploch. Druhý krok není povinný, ale když máte plochy, můžete si být na 100% jisti, že jsou uzavřené (jinak nemůže být plocha vytvořena).

Když jsme zkonvertovali všechny sloupy do ploch, můžeme na ně použít nástroj [Struktura](Arch_Structure/cs.md) a nastavit výšku (některé mají 6m, další pouze 2.25m):

![](images/Arch_tutorial_08.jpg )

Na obrázku nahoře vidíte dva sloupy, které jsou tak jak byly v DWG souboru, dva byly vylepšeny na plochy a dva byly zformovány do strukturálních objektů a jejich výška nastavena na 6m a 2.25m.

Připomínám, že tyto různé architektonické objekty (zdi, struktury a další, které ještě objevíme) všechny sdílejí spoustu věci mezi sebou (například všechny mohou být přidány jedna na druhou, jako jsme to již udělali se zdmi, a kterákoliv z nich může být zkonverována do jiné). Je to více otázka vkusu, sloupy můžeme také udělat pomocí nástroje pro zeď a podle potřeby zkonvertovat. Ve skutečnosti některé z našich zdí jsou betonové zdi, později je můžeme zkonvertovat do struktur.

## Odebrání

Nyní je čas vytvořit náš odečítací objem. Nejjednodušším způsobem je nakreslit jeho profil nad řezem. Potom jej otočíme a umístíme jej do správné pozice. Podívejte se proč jsem umístil řez a sklon před začátkem? Bude to velmi šikovné pro nakreslení toho objemu zde, potom jeho posunutí do správné pozice na modelu.

Nakresleme tedy ten objem, větší než střecha, který bude odečten ze zdí. Udělám to tak, že nakreslím dvě přímky nad základnou střechy, potom jej trochu prodloužím pomocí nástroje [Oříznout](Draft_Trimex/cs.md). Potom nakreslím [drát](Draft_Wire/cs.md), zachycením k uvedeným přímkám a přechodem nahoru na našich 6 metrů. Také jsem nakreslil modrou přímku na úrovni přízemí (0.00), která bude naší osou rotace.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

A teď ta finta: Použijeme nástroj _ (je to v záložce \"úkoly\" v okně stromu) a nastavíme ji na YZ (což je \"boční\" rovina). Když nastavíte pracovní rovinu ručně, jako zde, nezmění to závislost na Vašem pohledu. Nyní můžete otočit pohled tak, abyste měli dobrý výhled na všechny věci, které musíte vybrat. Pro pozdější přepnutí pracovní roviny zpět \"automatického\" módu, stiskněte opět tlačítko [Vybrat rovinu](Draft_SelectPlane/cs.md) a nastavte ji na \"Žádná\".

Nyní bude snadné provést otočení: Vyberte profil, stiskněte tlačítko [Otočení](Draft_Rotate/cs.md), klikněte na bod v modré přímce, zadejte 0 jako počáteční úhel a 90 jako rotace:

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

A vše co musíme udělat teď je posunout profil trochu blíže k modelu (pokud je to potřeba, nastavte pracovní rovinu na XY) a vysunout jej. Můžete to udělat buď pomocí nástroje [Díl Vysunout](Part_Extrude/cs.md) nebo pomocí nástroje [Kreslení Oříznout](Draft_Trimex/cs.md), který má také speciální skrytou schopnost vysunovat plochy. Vždy se ujistěte, že vysunutí je delší než všechny zdi, které z něj budou odečteny abyste se vyhnuli problematické face-on-face situaci při odečítání:

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

A nyní příchází na řadu akce opačná k nástroji _. Tohle uvidíte po odebrání, objem pro odebrání zmizel ze 3D pohledu i z okna stromu. Je to proto, že byl označen jako dítě zdi a \"spolknut\" zdí. Vyberte zeď, rozbalte ji v okně stromu a máte tady Váš objem.

Nyní vyberte ten objem v okně stromu, CTRL + výběr další zdi a stiskněte [Odebrat](Arch_Remove/cs.md). Opakujte pro všechny zdi až budou všechny příslušně zkráceny:

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Pamatujte si, že pro oba nástroje [Přidat](Arch_Add/cs.md) i [Odebrat](Arch_Remove/cs.md), je důležité pořadí ve kterém se objekty vybírají. Hostující objekt je vždy jako poslední, jako \"Odebrat X z Y\" nebo \"Přidat X k Y\"


{{Note|Poznámka k přidávání a odebírání|Architektonické objekty které podporují takovéto přidávání a odebírání (všechny kromě pomocných "visual" objektů jako jsou osy) sledují takové objekty pomocí dvou vlastností , resp. "Přídavky" a "Odběry", které obsahují seznam odkazů na jiné objekty, které jsou odebrány nebo přidány.Nějaký objekt může být na seznamech některých jiných objektů, stejně jako náš odebíraný objem zde. Každý z "otců" jej bude chtít hodit do sebe v okně stromu, nicméně obyčejně zůstane v posledním objektu. Ale vždy můžete tento seznam pro každý objekt upravit, dvojklikem v okně stromu, což ve FreeCADu znamená, že se přechází do editačního módu. Editační mód ukončíte stisknutím klávesy ESC.}}

## Vytvoření střech 

Nyní co nám zbývá k dokompletování struktur je vytvoření střech a menších vnitřních desek. Opět nejjednodušší cestou je nakreslit jejich profil nad řezem pomocí nástroje [Drát](Draft_Wire/cs.md). Tady jsem nakreslil 3 profily jeden nad druhým (odsunul jsem je od sebe, v pohledu dole to můžeme vidět lépe). Zelený bude použit pro pozdější ohraničení desky střechy, potom modrý pro boční části a červený pro střední část, které je nad blokem koupelny:

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Pak musíme opakovat operaci otočení jako nahoře, otočit objekty ve svislé pozici, potom jejich posunutí na jejich správné umístění a zkopírování některých z nich, které budou vysunuty dvakrát pomocí nástroje [Posun](Draft_Move/cs.md), a to stisknutím klávesy ALT, což vytvoří kopie místo pouhého přesunutí aktuálního objektu. Také jsem přidal další dva profily pro boční zdi otvorů koupelny.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

Když je všechno na místě, je to už jen věcí použití nástroje [Oříznutí](Draft_Trimex/cs.md) na vysunutí a potom je zkonvertovat od objektů [Architektura Struktura](Arch_Structure/cs.md).

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

Pak vidíme, že vyvstaly další problémy: dva ze sloupů vpravo jsou příliš krátké (měly dosahovat až ke střeše) a taky je mezera mezi deskou a zdí studia vpravo vzadu (symbol úrovně 2.6 na řezu byl zřejmě špatně). Díky parametrickým objektům není problém to vyřešit: Pro sloupy jenom změníme jejich výšku 6m, vyberte objekt odebrání střech z okna stromu a odeberte jej ze sloupů. Pro zdi je to ještě jednodušší: posuňte je trochu dolu. Protože odebírací objem zůstává stále na svém místě, konstrukce zdi se přizpůsobí automaticky.

A ještě musí být opravena jedna věc, v koupelně je malá betonová deska, která protíná některé zdi. Opravme to vytvořením nového odebíracího objemu a odeberme jej z těchto zdí. Další vlastností nástroje [Oříznutí](Draft_Trimex/cs.md), který používáme k vysunutí hmoty, je to, že také může vysunout jednu plochu existujícího objektu. To vytvoří nový samostatný objekt, takže neriskujete \"poškození\" jiného objektu. Takže můžeme vybrat základovou plochu z malé betonové desky (podívejte se na ní zespodu modelu), potom stiskněte tlačítko [Oříznutí](Draft_Trimex/cs.md) a vysuňte ji až ke střeše. Pak ji odeberte z obou vnitřních zdí koupelny pomocí nástroje [Odebrat](Arch_Remove/cs.md):

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">

## Podlahy, schodiště a komín 

Teď je naše struktura kompletní a zbývá už jen dodělat pár měnších objektů.

### Komín

Pusťme se do komína. Nyní už víte jak to funguje? Nakreslete pár uzavřených [drátů](Draft_Wire/cs.md), posuňte je nahoru do jejich správné výšky nástrojem [Posun](Draft_Move/cs.md), vysuňte je nástrojem [Oříznout](Draft_Trimex/cs.md), změňte ten větší na [strukturu](Arch_Structure/cs.md), a odečtěte ten menší. Všimněte si, že komínový průduch nebyl na plánu zakreslen, ale našel jsem jeho pozici přetažením modrých čar z pohledu řezu.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">

### Podlahy

Podlahy nejsou v základním výkresu příliš dobře zobrazeny. Při pohledu na řezy nepoznáte kde a jak tlusté jsou podlahové desky. Tak budeme předpokládat, že zdi stojí na základech na úrovni 0.00 a že stejné je to s podlahami tlustými 15 cm, které leží přímo na základové desce. Takže podlahová deska nezasahuje pod zdi, ale je kolem nich. Můžeme je vytvořit z jedné velké obdélníkové desky a pak z ní odečíst zdi, ale víme, že odečítací operace je dost náročná na prostředky. Lepší je udělat podlahy z menších kusů, bude to \"levnější\" na výpočetní požadavky a uděláme to tedy rozumně pokoj po pokoji, bude se to později hodit při výpočtech podlahových ploch:

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Když jsou nakresleny dráty, jen je převedeme do [struktur](Arch_Structure/cs.md), a dáme jim výšku 0.15:

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">

### Schodiště

A teď schodiště. Seznamte se s dalším nástrojem Architektury [schodištěm](Arch_Stairs/cs.md). Tento nástroj je zatím ve velmi ranné fázi vývoje, takže od něho moc neočekávejte. Ale je už docela šikovný pro vytvoření jednoduchého, přímého schodiště. Je důležité znát jejich koncept, nástroj pro schodiště je zamýšlen pro vybudování schodiště z rovné podlahy na vršek zdi. Jinými slovy, při pohledu shora objekt schodiště zabírá přesně stejnou plochu jakou zabírá na půdorysu, takže poslední stupeň není zakreslen (ale samozřejmě je započten při výpočtu výšky).

V tomto příkladu jsem dal přednost vytvoření schodiště v řezu, protože budme potřebovat mnoho rozměrů, které se snadněji získají z tohoto pohledu. Nakreslil jsem pár červených vodicích přímek, potom dvě modré přímky, které budou základem dvou částí schodiště a dva zelené uzavřené dráty, které vytvoří chybějící části. Nyní vybereme první modrou přímku, stiskneme nástroj [Schodiště](Arch_Stairs/cs.md), zadáme počet stupňů na 5, výšku na 0.875,šířku na 1.30, typ struktury na \"massive\" a tloušťku struktury na 0.12. Opakujte pro další část.

Pak vysuňte oba zelené dráty o 1.30 a otočte je a posuňte do správné pozice:

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

Na bočním pohledu nakreslete (potom otočte) okraj:

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Potom všechno posuňte na místo:

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

Také nezapomeňte snížit sloup, který protíná schodiště, protože v BIM je vždy špatné, když se objekty protínají. Pamatujte, že stavíme stejně jako v reálném světě, kde se taky pevné objekty nemohou protínat. Tady jsem nechtěl odečíst sloup přímo od schodiště (protože jinak by objekt sloupu byl pohlcen objektem schodiště a to se mi nelíbí), proto jsem vzal plochu, na které byl sloup postaven a znovu jsem ji vysunul. Toto nové vysunutí pak bylo odečteno ze schodiště.

Výborně! Všechna těžká práce je nyní udělána a nyní se dejme do mnohem těžší práce!

## Dveře a okna 

Nástroj [Architektura Okno](Arch_Window/cs.md) je pěkně složitá záležitost. Používá se pro vytvoření všech druhů \"vložených\" objektů jako jsou okna nebo dveře. Ano, ve FreeCADu jsou dveře speciálním druhem okna. Ve skutečném životě taky, nemyslíte? Nástroj [Architektura Okno](Arch_Window/cs.md) může být stále ještě poněkud obtížnější na používání , ale to je za to, že byl sestaven pro maximální výkon. Může s ním být vytvořen téměř jakýkoliv druh okna podle vašich představ. Ale až tento nástroj bude mít v budoucnosti víc předvoleb, situace bude lepší.


<div class="mw-translate-fuzzy">

Objekt _, který obsahuje uzavřené dráty (lomené čáry)). Tyto dráty definují různé části okna: vnější rámečky, vnitřní rámečky, okenní panely, pevné panely, atd. Objekt okno má vlastnosti, které obsahují co dělat se kterým drátem: vysunout je, umístit je s určitým odsunutím, atd. Nakonec může být okno vloženo do hostitelského objektu jako je zeď nebo struktura, do které automaticky vytvoří otvor. Otvor bude vypočten podle největšího drátu nalezeného ve 2D plánu.


</div>

Ve FreeCADu jsou dva způsoby jak vytvořit takové objekty: Použitím předvoleb nebo nakreslením plánu okna od začátku. Zde se podíváme na oba způsoby. Ale pamatujte, že metoda s předvolbami nedělá nic jiného, než že vytvoří objekt plánu a definuje potřebná vysunutí.

### Použití předvoleb 

Při stisknutí nástroje [Architektura Okno](Arch_Window/cs.md) bez vybrání objektu, jste požádáni o zadání 2D plánu nebo zadání předvoleb. Použijme předvolbu \"Jednoduché dveře\" pro umístění hlavních vchodových dveří našeho modelu. Zadáme šířku 1m, výšku 2.45m a rozměr W1 0.15m, ostatní parametry ponechte na 0.05m. Když pak kliknete na levý spodní roh zdi, vytvoří se nové dveře:

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

Všimnete si, že ty Vaše nové dveře se nezobrazí v okně stromu. Je to kvůli tomu, že zachycením zdi jsme označili zeď jako hostitelský objekt. Následně byl \"pohlcen\" zdí. Ale kliknutím pravou myší na zeď → Jdi na výběr najdete dveře ve stromě.

V tomto případě, protože naše okno není vloženo do žádné zdi (otvor už tam byl), můžeme oddělit okno od hostující zdi. Udělá se to dvojklikem na hostující zeď v pohledu stromu pro přechod do editačního módu. Tam uvidíte okno v jeho \"Odečítací\" skupině. Jednoduše tam vyberte okno, stiskněte tlačítko \"odstranit prvek\" a potom OK. Naše okno bylo odstraněno z hostující zdi a leží na konci pohledu stromu.

Máme druhé dveře, přesně stejné jako ty první, trochu vlevo. Místo vytváření nových dveří od začátku, máme dva způsoby jak vytvořit kopii těch prvních: Použitím nástroje [Kreslení Posun](Draft_Move/cs.md) se současně stisknutou klávesou ALT, která jak jistě víte, objekt kopíruje místo přesunutí. Nebo, ještě lépe, můžeme použít nástroj [Kreslení Klon](Draft_Clone/cs.md). Nástroj Klon vytváří \"klon\" vybraného objektu, se kterým můžete pohybovat, ale drží si tvar původního objektu. Když se změní původní objekt, změní se zároveň i klon.

Takže všechno co musíme udělat je vybrat dveře, stisknout nástroj [Kreslení Klon](Draft_Clone/cs.md) a potom přesunot klon na jeho správnou pozici pomocí nástroje [Kreslení Posun](Draft_Move/cs.md).

### Organizace modelu 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Nyní je vhodný čas udělat malou očistu domu. Protože už máme dvě okna, je vhodný čas pro pročištění okna stromu: Vytvořte novou [skupinu](Std_CreateGroup/cs.md), přejmenujte ji na \"Windows\" a přesuňte do ní obě okna. Doporučuji Vám také další prvky oddělit tímto způsobem, jako jsou zdi a struktury. Protože můžete vytvořit i skupiny uvnitř [skupin](Std_CreateGroup/cs.md), můžete organizovat dále, například umístění všech prvků, které vytvářejí střechu do samostatné skupiny, takže bude snadné ji zapnout nebo vypnout (přepínání viditelnosti skupin platí i pro všechny objekty uvnitř nich).


<div class="mw-translate-fuzzy">

_, [Budova](Arch_Building/cs.md) a [Podlaží](Arch_Floor/cs.md). Tyto 3 objekty jsou založeny na standardních skupinách FreeCADu, takže se chovají přesně stejně jako skupiny, ale mají několik vlastností navíc. Například, [podlaží](Arch_Floor/cs.md) má schopnost nastavit a řídit výšku obsažených zdí a struktur, a když jsou přesunuty, celý jejich obsah je přesunut také.


</div>

Ale zde, protože máme pouze jednu budovu s pouze jedním (a půl) podlažím, není ve skutečnosti potřeba používat takové objekty, takže vystačíme jen s jednoduchými skupinami.




Vraťme se zpět k práci. Vypněte skupinu střechy, tak budme lépe vidět dovnitř a přepněte Zobrazovací mód objektů podlaží na Drátový model (nebo použijte nástroj [Kreslení Přepnout zobrazovací mód](Draft_ToggleDisplayMode/cs.md)) takže je můžeme zachycovat, ale můžeme vidět půdorys i zespodu. Ale můžeme také vypnout podlahy kompletně, potom umístit dveře na úroveň 0, potom je zvednout o 15cm pomocí nástroje [Kreslení Posun](Draft_Move/cs.md).


<div class="mw-translate-fuzzy">

Teď umístíme vnitřní dveře. Opět použijte předvolbu \"Jednoduché dveře\" a vytvořte dveře široké 1.00m a 0.70m a vysoké 2.1 s rozměrem W1 0.1m. Ujistěte se, že zachytíte správnou zeď až je budete umisťovat a ony vytvoří automaticky otvor v té zdi. Jestliže je obtížné umístit je správně, můžete je umístit na snadnější místo (například na roh zdi) a potom je posunout. Otvor se posune s nimi.


</div>

Pokud omylem vložíte okno do špatné zdi, je snadné to napravit: Odstraňte okno se skupiny \"Substraction (Odebrané)\" u hostující zdi v editačním módu, jak jsme viděli výše a potom je vložte do skupiny \"Substraction (Odebrané)\" u správné zdi stejnym způsobem nebo jednoduše použitím nástroje [Architektura Odebrat](Arch_Remove/cs.md).

O trochu práce později, všechny dveře jsou na místě:

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

Při bližším pohledu na bokorys, najdeme další chybu: Vrchol cihlové zdi není na 2.60m, ale o 17.5cm níže, tj. 2.425cm. Naštěstí okna založená na předvolbách mají výhodu: Můžete změnit jejich hlavní rozměry (šířku a výšku) v jejich vlastnostech. Takže změňme jejich výšku na 2.425-0.15, tj. na 2.275. Druhé okno, protože je to klon prvního okna, je převezme také. To je to zásadní v čem se projeví kouzlo parametrického návrhu.

A teď je podívejme na opravdu zajímavou věc: Jak navrhnout naše vlastní uživatelské okno.

### Vytváření uživatelských oken 


<div class="mw-translate-fuzzy">

Jak jsem vysvětlil výše, objekty _.


</div>

Začněme tedy s kreslením našeho prvního plánu okna. nakreslil jsem jej v nárysu, použitím několika [obdélníků](Draft_Rectangle/cs.md): Jeden z nich pro vnější linky, a 4 pro vnitřní linky. Zastavil jsem se přede dveřmi, protože, připomínám, naše dveře už rám mají:

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Potom vyberte všechny obdélníky a stiskněte tlačítko [Kreslení do Náčrtu](Draft_Draft2Sketch/cs.md) (a smažte obdélníky, protože tento nástroj nemaže původní objekty, pro případ, že něco nedopadlo dobře). Potom s vybranými novými náčrty, stiskněte nástroj [Architektura Okno](Arch_Window/cs.md).

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

Nástroj detekuje, že plán má jeden vnější drát a několik vnitřních drátů a automaticky navrhne deafultní konfiguraci: Jeden rám vytvořený odečtením vnitřních rámů od vnějšího, vysunutý o 1m. Změňme to přechodem do editačního módu okna dvojklikem na ně v okně stromu:

Uvidíte \"Defaultní\" komponentu, která byla vytvořena automaticky nástrojem Okno, které používá 5 drátů (vždy odečítá ostatní z největšího) a je vysunuto o 1. Zmněňme hodnotu vysunutí na 0.1 , aby odpovídalo tomu, jaké jsme použili u dveří.

Potom přidáme 4 nové skleněné panely, každý z nich využije jeden drát a dáme jim vysunutí 0.01 a odsun 0.05, takže jsou umístěny ve středu rámu. Takto bude Vaše okno vypadat, když dokončíte úpravy:

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

Předpokládám, že nyní už byste měli rozumět síle tohoto systému: Je možná jakákoliv kombinace rámů a panelů. Jestli je umíte kreslit ve 2D, pak mohou existovat jako zcela platné 3D objekty.

A teď nakresleme ostatní části, potom je přesuneme na jejich místo současně. Ale nejdříve musíme udělat nějaké úpravy v základním 2D výkresu, protože některé linky zřejmě úplně chybí - tam kde se okna dotýkají se chodištěm. Opravit to můžeme odsunutím přímky schodiště o 2.5cm pomocí nástroje [Kreslení Odsunout](Draft_Offset/cs.md) (samozřejmě se stisknutou klávesou ALT pro kopírování místo přesunutí). Nyní můžeme nakreslit náš plán pomocí [drátů](Draft_Wire/cs.md), potom je konvertovat do náčrtu a potom z nich vytvořit okno.

Až to několikrát zopakujeme (já jsem udělal 4 samostatné kousky, ale záleží na Vás jak se rozhodnete), máme fasádu kompletní:

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Nyní, stejně jako předtím, je to už jen věcí otočení částí a jejich posunutím na správnou pozici:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

Poslední chybějící část je segment zdi, který není vidět na půdorysu a který musíme přidat. Máme několik možností, jak to udělat, já jsem si vybral nakreslit přímku na plánu základů, potom ji přesunout na správnou výšku a pak z ní vytvořit zeď. Potom také musíme vytáhnout objem pro odečítání střechy (musí zůstat v posledním sloupci) a potom jej odečíst. Nyní je hotova tato strana budovy:

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Hotovo? Zatím ne. Podívejte se na obrázek nahoře, naše dveře jsme udělali s 5cm rámečkem, vzpomínáte (to bylo defaultní v předvolbě). Ale ostatní okna mají rámečky 2.5cm. To také musí být opraveno.

### Úpravy oken 

Už jsme si ukázali jak vytvářet a upravovat komponenty oken, pomocí editačního módu oken, ale můžeme i editovat podkladový náčrt. Předvolby oken se neliší od uživatelských oken, nástroj [Okno](Arch_Window/cs.md) pouze vytváří podkladový náčrt. Vyberte náš objekt dveří (původní, ne kopii, pamatujte, že je to klon) a rozbalte jej v okně stromu. Tam je náš náčrt. Dvojklikněte na něj a přejdete do editačního módu.


<div class="mw-translate-fuzzy">

[Pracovní plocha Skicář](Sketcher_Workbench/cs.md) je extrémě výkonný nástroj. Nemá některé z výhod [pracovní plochy Kreslení](Draft_Workbench/cs.md), jako jsou třeba zachycování a pracovní roviny, ale má zase mnoho jiných výhod. Ve FreeCADu budete často používat jednu nebo druhou podle potřeby. Nejdůležitější vlastností skicáře jsou vazby. Vazby umožňují automaticky vzájemně fixovat pozice některých elementů. Například můžete nastavit, že segment bude vždy svislý nebo bude vždy v dané vzdálenosti od jiného.


</div>

Když upravujeme náčrt našich dveří, vidíme, že je proveden na plně vazbeném náčrtu:

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Všechno co teď musíme udělat je upravit vzdálenost 5cm mezi vnější a vnitřní linkou dvojklikem na ně a změnou jejich hodnoty na 2.5cm (Pamatujte, že jednotky stále ještě nejsou plně funkční v době, kdy to píšu). Po kliknutí na tlačítko \"OK\", jsou dveře (a jejich klon) aktualizovány.

## Práce bez 2D podpory 

Naše práce byla až doteď relativně snadná, protože jsme měli podkladový 2D výkres jako základ, nad kterým jsme pracovali. Ale teď musíme udělat protější průčelí a skleněné atrium a věci se začínají komplikovat: Výkres protějšího průčelí má spoustu chyb, nepředstavuje atrium celé a jednoduše také nemáme výkres vnitřníh zdí atria. Proto si musíme pár věcí vymyslet sami. Určitě se podívejte na [odkazované obrázky](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/) pro představu jak je to uděláno. A nebo si to udělejte podle sebe!

Je jedna věc, kterou už můžeme udělat: zduplikovat komplikované okno na schodech nástrojem [Posun](Draft_Move/cs.md), protože to je stejné na obou stranách:

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Tady připomínám, že já dávám přednost duplikování pomocí nástroje [Posunpřed](Draft_Move/cs.md) použitím [klonování](Draft_Clone/cs.md), protože klon zatím nepodporuje různé barvy uvnitř objektu. Rozdíl je v tom, že klon je kopie konečného tvaru původního objektu, zatímco když objekt zkopírujete, vytvoříte nový objekt, který má stejné vlastnosti jako původní objekt (proto i základní náčrt a jeho definiční komponenty okna, které jsou uloženy jako vlastnosti).

A teď musíme zaútočit na části, které nejsou nakreslené nikde. Začněme se skleněnou zdí mezi obývacím pokojem a atriem. Snadnější bude kreslení z bočního pohledu, protože ten mám dá správnou výšku střechy. Když jste v půdorysu, můžete pohledem otáčet z menu Pohled -\> Standardní pohled -\> Otočit doleva nebo doprava až dostanete komfortní pohled na práci, jako třeba:

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Všimněte jak jsem na obrázku nahoře udělal přímku z modelu k levému řezu, abych získal přesnou šířku okna. Potom jsem tuto šířku zkopíroval do bokorysu a rozdělil jsem ji na 4 části. Pak jsem vytvořil jednu hlavní část okna, plus 4 další okna pro posuvné dveře. Skicář má občas potíže s překrývajícími se dráty, proto jsem dal přednost držet je odděleně, jak je zde:

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

Po nutném otočení všechno perfektně zapadne na místo:

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

Ještě tady potřebujeme nějakou rohovou část. Malý užitečný trik s nástrojem [Vybrat rovinu](Draft_SelectPlane/cs.md), když máte vybranou plochu a stisknete toto tlačítko, pracovní rovina se ztotožní s vybranou plochou (přinejmenším s její pozicí a pokud je plocha obdélníková, pokusí se ztotožnit i její osy). Je to užitečné při kreslení 2D objektů přímo na modelu, jako zde, můžeme nakreslit obdélník, který bude vysunut přímo do jeho správné pozice:

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

A teď se pusťme do dvou zbývajících částí. Jedna je snadná, je to kopie toho co je na druhé straně, takže snadno můžeme použít 2D výkres:

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Druhá část je trochu složitější. Při pohledu na obrázky vidíme, že má mnoho svislých sekcí, jako jsou okna na schodištích. Náhodou (nebo velice dobrým designem z Vilanova Artigas) šířka našich oken (4.50m) je přesně stejná jako šířka schodišťových oken, takže můžeme použít stejné sekce: 15 částí po 30cm. Zde jsem využil nástroj [Kreslení Pole](Draft_Array/cs.md) pro kopírování přes 2 přímky 15-krát a nad nimi jsem nakreslil obdélníky:


</div>

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Když je to uděláno, můžeme vytvořit okno stejnou metodou, kterou už známe. Další malá užitečná finta, pokud už jste si jí nevšimli dříve: Při úpravě okna, když změníte jméno komponenty, vytvoří se ve skutečnosti ji zduplikujete. Takže 15 vnitřních skleněných panelů vytvoříte místo 15 kliknutí na tlačítko \"add\" a 15-krát vyplnění jejich dat, pouze tak, že upravíte jeden a změníte jeho jméno a drát, což pokaždé vytvoří novou kopii.

Po tom co okno otočíme a posuneme na místo, je atrium kompletní:

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">

## Úpravy a opravy 

Když se nyní podíváme na zadní průčelí a porovnáme je s plánem , vidíme, že jsou tam nějaké rozdíly, které musejí být opraveny. A to, že ložnicová okna jsou menší než jsem si prvně myslel a budeme muset přidat nějaké další zdi. Aby to bylo uděláno správně, některá podlaží musejí být snížena:

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Samozřejmě to můžemeudělat několika způsoby. Snadný způsob by byl odečtení objemu, ale to by zase přineslo zbytečné zesložitění modelu. Lepší je úprava základového drátu každého podlaží. A teď přichází na řadu mód [Kreslení Úpravy](Draft_Edit/cs.md). Rozbalením těchto podlaží v okně stromu a potom zviditelněním základového drátu můžeme dvojklikem na něj přejít do editačního módu. Můžeme posunovat jeho body nebo [přidávat](Draft_AddPoint/cs.md) nebo [odebírat](Draft_DelPoint.md) body. Tak se snadno upraví podlahové desky.


</div>

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

Po nějaké další lopotě (osoba, která dělala ty výkresy, zřejmě pěkně zlenivěla, když dělala poslední bokorysy, mnoho jich je nakresleno špatně) máme nakonec dům kompletní:

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Všimněte si, že komínové trubice, která je vytvořena z kružnice, kterou jsem použil k vytvoření díry v komínovém bloku, který jsem vysunul a potom zkonvertoval do trubice pomocí nástroje [Díl odsunutí](Part_Offset/cs.md).


{{Note|Problémy v objektech|Někdy může mít Váš vytvořený objekt problémy. Například objekt, který byl vytvořen na základě, který byl smazán a objekt tak nemůže přepočítávat svůj tvar. Takové jsou obyčejně zobrazovány s malou červenou značkou na jejich ikoně a/nebo s varováním ve výstupním okně. Neexistuje obecný návod jak takové problémy opravit, protože mohou mít mnoho důvodů. Ale nejsnadnější způsob řešení je často jejich smazání a pokud jste nesmazali jejich základový objekt, znovu je vytvořit.}}

## Výstup

A teď, když jsme prošli tou těžkou prací při budování našeho modelu, přichází odměna: Co s tím můžeme dělat? V základě je to velká výhoda, pracovat s BIM, všechny naše tradiční architektonické požadavky, jako jsou 2D výkrasy (plány, řezy, atd.) vykreslování ve 3D a výpočty (výkaz výměr - seznam množství) mohou být získány z tohoto modelu. A ještě lépe, zregenerují se vždy, když je model upraven. Zde Vám ukážu jak získat tyto různé dokumenty.

## Příprava 

Před začátkem exportu je zajímavé udělat zajímavou úvahu: Jak jste viděli, náš model se stává čím dál tím víc složitý, se spoustou vztahů mezi objekty. To vyžaduje následné výpočtové operace, které jsou náročné, jako je prořezání skrz model. Jeden způsob jak kouzelně \"zjednodušit\" drasticky Váš model je vyjmutí celé této složitosti tak, že model exportujete do formátu [STEP](http://en.wikipedia.org/wiki/ISO_10303-21). Tento formát zachová celou Vaši konstrukci, ale vypustí všechny vztahy a parametrické konstrukce a podrží pouze konečný tvar. Když tento STEP soubor potom znovu naimportujete do FreeCADu, získáte model, který nemá žádné vztahy a má mnohem menší velikost souboru. Představte si ho jako \"výstupní\" soubor, který můžete kdykoliv regenerovat z \"hlavního\" souboru:

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">

### Exportování do IFC a dalších aplikací 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

Jedna ze základních věcí, které potřebujete při práci s BIM je schopnost importu a exportu souborů _ už je podporován a import IFC souborů do FreeCADu je už docela spolehlivý. Export je nicméně zatím ve stavu experimentování a aktuálně má mnoho omezení. Přesto, stav se zlepšuje a odpovídající exportní možnosti IFC bychom měli mít velmi brzy.

[IFC export](Arch_IFC/cs.md) požaduje jenom malé nastavení, když už jsou nainstalovány potřebné softwarové knihovny. Potřebujete pouze znovuvytvořit stavební struktury, které jsou potřebné ve všech IFC souborech, přidáním [Budovy](Arch_Building/cs.md) do souboru, potom [Podlaží](Arch_Floor/cs.md) a potom do něj přesunout všechny skupiny objektu, ze kterých se model skládá. Ujistěte se, že vypustíte konstrukční geometrii (všechny 2D věci, které jsme nakreslili), abychom se vyhnuli vytvoření zbytečně náročného IFC souboru.

IFC nemá žádný \"obecný\" strukturální prvek jako FreeCAD, musíme jim přiřadit role (sloup, nosník, atd.) aby exportér věděl jaký prvek vytvořit v IFC souboru.

V takovém případě potřebujeme celý nášarchitektonický systém, proto IFC exporter ví, jestli objekt musí být exportován jako zeď nebo jako sloup, takže používáme náš hlavní model a ne výstupní model.

Když je to uděláno, jednoduše vybereme stavební objekt a zvolíme formát \"Industry Foundation Classes\". Exportování do ne-BIM aplikace, jako je třeba _, STEP, IGES nebo OBJ.




### Rendering


<div class="mw-translate-fuzzy">

Ve FreeCADu je také renderovací modul [Pracovní plocha Raytracing](Raytracing_Workbench/cs.md). Tato pracovní plocha aktuálně podporuje dva renderovací enginy [PovRay](http://www.povray.org/) a [LuxRender](http://www.luxrender.net). Protože FreeCAD není určen pro renderování obrázků, je nabídka pracovní plochy Raytracing poněkud omezená. Pokud chcete odpovídající rendering je nejlepší postup exportovat model do formátu založeném na síti jako jsou OBJ nebo STL a otevřít jej v aplikaci vhodnější pro rendering, jako je [Blender](http://www.blender.org). Obrázek dole je renderován pomocí cyklovacího enginu Blenderu:


</div>

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

Ale pro rychlé renderování Vám pracovní plocha Raytracing poskytne už docela dobrý výsledek, s výhodou velmi snadného nastavení, díky jeho systému šablon. Toto je Váš model plně renderovaný ve FreeCADu pomocí enginu Luxrender při použití šablony \"indoor\".

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

Pracovní plocha Raytracing zatím nabízí velmi omezenou správu materiálů, ale osvětlení a prostředí jsou definovány v šablonách a proto mohou být plně uživatelsky upravovány.

### 2D výkresy 

Nejdůležitějším použití BIM je určitě automatická výroba 2D výkresů. Ve FreeCADu se to dělá nástrojem [Architektura Rovina řezu](Arch_SectionPlane/cs.md). Tento nástroj umožňuje umístit objekt roviny řezu ve 3D pohledu, kterým můžete orientovat výrobu plánů, řezů a nárysů. Roviny řezů musí znát objekty, které musí obsahovat, proto jakmile nějaký vytvoříte, musíte jej přidat nástrojem [Přidat](Arch_Add/cs.md). Můžete přidat jednotlivé objekty nebo ještě výhodněji skupinu, podlaží nebo celou budovu. To Vám umožní snadno později změnit rozsah určité roviny řezu přidáním nebo odebráním objektů z nebo do takové skupiny. Jakákoliv změna těchto objektů se odrazí v pohledech vytvořených rovinou řezu.

Rovina řezu automaticky vytváří průřezy objektů. Jinými slovy vytváří pohledy místo řezů, Vy pouze musíte umístit rovinu řezu mimo Váš objekt.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Roviny řezů mohou vytvářet dva různé výstupy: objekty [tvar](Part_Workbench/cs.md), které jsou ve stejném dokumentu jako Váš 3D model nebo [výkresy pohledů](Drawing_Workbench/cs.md), které jsou vytvořeny k použití na výkresech vytvářených pomocí [Pracovní plochy Kreslení](Drawing_Workbench/cs.md). Každý z nich se chová odlišně a má svoje výhody.


</div>

**Pohledy tvarů**


<div class="mw-translate-fuzzy">

Tento výstup vzniká použitím nástroje [Kreslení Tvar2DPohled](Draft_Shape2DView/cs.md) na vybrané rovině řezu. Vytvoříte 2D pohled modelu přímo ve 3D prostoru, jako je na obrázku nahoře. Zde je hlavní výhodou to, že na něm můžete pracovat s použitím nástrojů [Kreslení](Draft_Workbench/cs.md) (nebo jakýmkoliv standardním nástrojem FreeCADu), takže můžete přidat texty, kóty, symboly atd.:


</div>

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

Na obrázku nahoře byly vytvořeny dva [2DTvar pohledy](Draft_Shape2DView/cs.md) pro každý řez, jeden, který zobrazuje všechno, druhý, který zobrazuje pouze řezné čáry. To nám umožňuje dát odlišné tloušťky čar a zapnout šrafování. Potom byly přidány kóty, texty a symboly a bylo importováno několik DXF bloků představujících nábytek. Tyto pohledy jsou pak snadno exportovatelné do DXF nebo DWG a lze je otevřít ve Vaší oblíbené 2D CAD aplikaci, jako je [LibreCAD](http://www.librecad.org) nebo [DraftSight](http://www.3ds.com/products-services/draftsight/overview/), kde na nich můžete dál pracovat:

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Připomínám, že některé vlastnosti zatím stále ještě nejsou podporovány [DXF/DWG exporterem](Draft_DXF/cs.md), proto výsledek ve vaší 2D aplikaci se může trochu lišit. například u obrázku nahoře jsem musel vrátit šrafování a opravit pozice některých textů u kót. Jestliže umístíte objekty v různých skupinách ve FreeCADu, stanou se tyto skupiny vrstvami ve 2D CAD aplikaci.

**Výkresové pohledy**


<div class="mw-translate-fuzzy">

Další druh výstupu, který může být vytvořen pomocí [rovin řezů](Arch_SectionPlane/cs.md) je[pohled Výkresu](Drawing_Workbench/cs.md). Ty se vytvářejí nástrojem [Kreslení Výkres](Draft_Drawing/cs.md) na vybrané rovině řezu. Tato metoda má proti předešlé jedno velké omezení: máte omezené možnosti upravovat výsledky a v této době není nativně podporováno kótování ani šrafování.


</div>

Na druhou stranu může být finálný výstup snadněji manipulovatelný a grafické možnosti formátu SVG jsou obrovské. V budoucnosti bude toto nepochybně preferovaná metoda. Ale v současnosti dostanete lepší výsledky při použití první metody.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">

Na obrázku nahoře, konstrukce je přímý výstup z roviny řazu, ale byly přidány další objekty Kreslení jako jsou kóty a šrafované víceúhelníky. Další objekt pohledu se stejným měřítkem a hodnotami odsunutí byl vytvořen nástrojem [Výkres](Draft_Drawing/cs.md). V budoucnosti bude taková operace dělána přímo na výkresové stránce, ponechávajíc model zcela čistý.

### Zjišťování množství 


<div class="mw-translate-fuzzy">

To je také další velmi důležitá uloha prováděná modly BIM. Ve FreeCADu vypadají věci dobře už od začátku, protože OpenCasCade jádro FreeCADu už se stará o výpočty délek, ploch a objemů všech tvarů, které jsou vytvářeny. Protože všechny objekty [Modulu Architektura](Arch_Workbench/cs.md) jsou tělesa, máte vždy jistotu, že budete schopni zjistit jejich objem.


</div>

**Použití tabulkových kalkulátorů**

To populate a spreadsheet with values extracted from the model the Arch\_Schedule tool can be used.

![](images/Arch_schedule_example03.jpg )

**Přehledový mód**

Dalším způsobem jak prozkoumat model a vytáhnout z něj hodnoty, je použití módu [Architektura Přehled](Arch_Survey/cs.md). V tomto módu můžete kliknout na bod, hranu, plochu nebo dvojkliknout pro výběr celého objektu a získat hodnoty výšky, délky, plochy nebo objemu, zobrazené na modelu, vytištěné ve výstupním okně FreeCADu a zkopírované do schránky, takže hodnoty můžete vzít a vložit do jiné otevřené aplikace.

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">

## Závěr


<div class="mw-translate-fuzzy">

Doufám, že tento výukový program Vám dal dobrý přehled dostupných nástrojů. Určitě se pro další informace podívejte na dokumentaci [Pracovní plocha Architektura](Arch_Workbench/cs.md) a [Pracovní plocha Kreslení](Draft_Workbench/cs.md) (je tam mnoho dalších nástrojů, které jsem zde nezmínil) a ještě obecněji na zbývající [documentaci FreeCADu](Main_Page/cs.md). Navštivte také [fórum](http://forum.freecadweb.org), mnoho problémů zde může být obyčejně vyřešeno během chvíle a také se podívejte na můj [blog](http://yorik.uncreated.net/guestblog.php?tag=freecad), kde jsou novinky o vývoji pracovní plochy Architektura.


</div>


<div class="mw-translate-fuzzy">

Soubor vytvořený tímto výukovým programem najdete [zde](http://yorik.uncreated.net/archive/freecad/casa_artigas.fcstd).


</div>


{{Tutorials navi

}}

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch tutorial/cs
