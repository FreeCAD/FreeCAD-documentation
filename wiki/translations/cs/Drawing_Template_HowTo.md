


{{VeryImportantMessage|The [Drawing Workbench](Drawing_Workbench.md) became obsolete in v0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.}}


<div class="mw-translate-fuzzy">


{{TutorialInfo/cs|Topic=2D Drafting|Level=Intermediate|Author=Mark Stephen ([Quick61](User:Quick61.md))|Time=An hour or less|FCVersion=0.14.3700 or greater}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

Tato lekce Vám ukáže jak od základu vytvořit a upravovat grafický SVG soubor pro použití jako šablonu výkresu pomocí pracovní plochy Výkres. Od verze 0.14 revize 2995 FreeCADu, pracovní plocha Výkres bude promítat výbraný díl do výkresové šablony podle pravidel nastavených v SVG dokumentu. Tato pravidla definují pracovní prostor v souřadnicích X,Y, ve kterém může FreeCAD promítat díl a automaticky se vyhnout nežádoucímu pronikání do popisového pole.


</div>

Každý kdo navrhuje šablony, které mají být sdíleny, by měl dodržovat základní pokyny uvedené v tomto výúkovém programu. Použití značek pro Pracovní prostor ("Working space") a Popisové pole ("Title block") v šabloně nevylučuje šablonu z použití ve starších verzich FreeCADu. Zatímco vložení těchto značek učiní Vaši šablonu plně funkční v současných verzích.

Tento výukový program začne nastavením stránky v programu Inkscape a vytvořením základní výkresové šablony. Následně bude přidán artwork, který dá Vaší práci osobní nebo profesionální styl. Dále uvidíte jak lze upravovat Vaši novou šablonu a jaké informace musí obsahovat pro použití ve FreeCADu.

Tento výukový program předpokládá, že čtenář má základní znalosti programu Inkscape a textového editoru.

## Základy

### Nastavení stránky 

Začneme s novým dokumentum v Inkscapu. Podle odkazu ve Wiki stránce FreeCADu na výkresové šablony, jeden pixel = jeden milimetr. To znamená, že jestliže chcete vytvořit výkresovou šablonu pro stránky rozměru ANSI A (rozměr letter), která je 216mm x 279mm, měla by naše šablona mít rozměr 216px x 279px. Chcete-li aby stránka byla orientována na šířku, měly by být tyto hodnoty prohozeny. Pro použití v tomto výukovém programu bude použita orientace na šířku. Stránka je tedy definována na šířku 279px a na výšku 216px.

V Inkscapu rozbalte menu File a vyberte Document Properties, Nyní byste měli vidět okno Document Properties. Upravte šířku a výšku jak bylo zmíněno a ujistěte se, že jednotky jsou nastaveny na pixely.

<img alt="" src=images/Inkscape_Template_tut_1.png  style="width:780px;">

Nyní byste měli mít dokument Inkscapu který je široký 279px a vysoký 216px. Pokračujeme přidáním rámečku.

### Rámeček

Dále vytvoření rámečku. Ačkoli není pro potřeby tohoto výukového progarmu nutné, bude na něj odkazováno později.

Použitím nástroje "Draw Bezier curves and straight lines" a výběrem módu "Create a sequence of paraxial line segments" vytvoříte obdélník rámečku dokumentu. Jakmile je obdélník uzavřen, kliknete na nástroj \"Select and transform objects\" (klávesová zkratka F1). Obdélník by se nyní měl zobrazovat jako vybraný. Pokud ne, použijte nástroj a vyberte jej.

Použitím vodorovných a svislých souřadnic u nastavení výběru, podle nastavení šířky a výšky výběru, umístíme rámeček o 10 jednotek (pixelů) dovnitř dokumentu od jeho okrajů. Zadejte následovně X=10, Y=10, W=259 a H=196. Vidíte, že levý dolní rok obdélníku pro rámeček je 10 pixelů nad a 10 pixelů vlevo od levého dolního rohu stránky. Zadáním rozměrů obdélníka jsme jej umístili rovnoměrně v hranicích dokumentu.

![](images/Inkscape_Template_tut_2.png )

### Popisové pole (Title Block) 

Nyní vytvoříme popisové pole (Title Block). To je editovatelné pole kam se zapisují informace o výkresu z FreeCADu. Tento výukový program použije jednoduchý příklad. Popisové pole může být jednoduché nebo složité jak si budete přát.

Popisové pole (Title Block) v příkladu bude obsahovat následující údaje: Název projektu, Datum, Měřítko a Autora. Potom bude umístěno do pravého dolního rohu rámečku.

Začnete vytvořením obdélníka někde uvnitř rámečku dokumentu. Uděláte to stejným způsobem jako jste udělali rámeček. Potom jej rozdělíte do 4 sekcí jak je vidíte. Když je to provedeno, vyberte obdélník i dělicí čáry a udělejte z nich skupinu a tu potom umístěte na X=169, Y=10 a rozměry W=100 a H=50 stejným způsobem jako rámeček.

![](images/Inkscape_Template_tut_3.png )

### Pevný text 

A teď přidáte textové bloky, které budou pevně umístěny v popisovém poli (Title Block). Bude to Název projektu, Datum, Měřítko a Autor. Uděláte to tak, že vyberete textový nástroj a kliknete někam do dokumentu. Potom jednoduše napíšete text, zvlášť pro každý název - kikněte na textový nástroj v dokumentu a po výběru odpovídající velikosti fontu (velikost 6 je pro tento dokument) zapište Název projektu. Potom přejeďte ukazatelem na další místo, opět klikněte a začněte nový textový blok, text bude Datum. Stejntě pak pro Měřítko a Autor. Nyní mohou být výběrovým nástrojem vybrány jednotlivé textové bloky a tažením nebo pomocí šipe přesunuty na příslušné místo v popisovém poli.

Po přesunutí všech textových bloků na jejich místo by měly být všechny vybrány společně s popisovým polem a vytvořena z nich skupina. Od té chvíle budou popisové pole a pevné texty spojeny jako jeden celek.

![](images/Inkscape_Template_tut_4.png )

### Editovatelný text 

A nyní přidáte textové bloky u kterých budete chtít aby byly editovatelné z FreeCADu. Stejným způsobem jako byly vytvořeny pevné texty budou vytvořeny i editovatelné texty a budou uloženy na odpovídající pozice. Texty zadáte následovně - NAME, DATE, SCALE, AUTHOR a přiřadíte jim velikost fontu 8. Jakmile budou texty umístěny, vyberte 4 textová pole, která chcete mít editovatelná a udělejte z nich samostatnou skupinu. Nevčleňujte je do stejných skupin jako jsou rámeček nebo popisové pole. Pro tuto chvíli jste s editovatelnými poli hotovi. Až bude hotová grafická část šablony, dokončíte proces vytvoření polí editovatelných z FreeCADu. Nyní ještě doděláme tuto část doplněním malé kresby do šablony.

![](images/Inkscape_Template_tut_5.png )

## Další

### Přidání Artworku 

Nyní když je hotova základní šablona, můžete do ní přidat malý artwork. Může to být cokoliv budete chtít. Vaše osobní nebo firemní logo, obrázek nebo vyobrazení Vašeho projetku, atd. Pro tento výukový program bude použito logo FreeCADu, které se nalézá v sekci [Artwork](Artwork.md) FreeCAD Wiki. Můžete na ně jednoduše kliknout a vybrat uložení obrázku. Až bude uloženo, naimportujte jej do Inkscapu. Po naimportování obrázku do vaší šablony může být obrázku změněna velikost a uložena podle Vašich představ. Až tak je snadné přidání artworku do vaší šablony.


<div class="mw-translate-fuzzy">

V této chvíli můžete z menu vybrat File a potom Save. V tomto výukovém programu je soubor pojmenován jednoduše example.svg, ale Vy si samozřejmě můžete pojmenovat soubor jak chcete.


</div>

![](images/Inkscape_Template_tut_6.png )

## Když je šablona vytvořena 

### Otevření souboru textovým editorem 

Po uložení šablony ji otevřete Vašim oblíbeným textovým editorem (ne textovým procesorem jako je třeba Word, apod.). Může to být něco jako Windows Notepad nebo dokonalejší Kate. V tomto výukovém programu bude použit editor Kate a všechny screenshoty budou z tohoto editoru.

Po otevření SVG souboru Vašim textovým editorem uvidíte následující.

![](images/Kate1.png )

### Značka "xmlns:freecad" 

První věci bude vložení následující řádky do dokumentu. Tento řádek je deklarace jmenného prostoru SVG a musí být zadána aby všechny SVG prvky byly identifikovány jako součást jmenného prostoru SVG.

 {.XML}
xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"



<div class="mw-translate-fuzzy">

Tento řádek je zadán ihned za první \<svg značku a se stejným odsazením jako ostatní xmlns údaje.


</div>

![](images/Kate2.png )

### Page Size 

In order to allow a final drawing to be printed in the right scale, the template must contain it\'s dimensions in real world units. Otherwise the whole drawing page would be printed scaled down by a factor of 3.54 (90(px/in)/25.4(in/mm)). Inside the the \<SVG\>-Tag the unit \"mm\" is added to the width and height fields. And a viewBox Attribute has to be added. The viewBox ranges from 0 0 to the width and height of the template. This way the SVG user unit (px) is redefined to be 1mm long. In consequence programs like Inkscape will be able to print a resulting drawing up to scale. Current versions of Inkscape handle this information very badly. Inkscape effectively rescales the whole document to 90dpi. This is not much of a problem for a final drawing, but imposes difficulties for editing drawing templates. After editing a template in Inkscape, it would have the same real word size on its own but elements of the drawing would be scaled down by a factor of 3.54. (Because the template would be in 90dpi but FreeCAD assumes 1px/mm.) Therefore it\'s recommended to remove the \"mm\" from the width and height attributes before opening an existing template in inkscape and recreate the units and viewBox attribute afterwards.

 {.html}
width="279mm"
height="216mm"
viewBox="0 0 279 216"


![](images/Kate2a.png )

### Značky Pracovního prostoru (Working space) a Popisového pole (Title Block) 

Další řádky, které přidáte budou značky pro Pracovní prostory (Working space) a Popisové pole (Title block). Tyto značky a jejich použití je definováno ve stránce Kreslení Šablony. Zatím nejsou tyto značky požadovány, ale novější verze pracovní plochy Výkres ve FreeCADu z nich bude mít prospěch a na starší verze FreeCADu nebudou mít vliv.

Značka Working space pro pracovní prostor je použita pro definici prostoru do kterého může FreeCAD zobrazovat. To umožní FreeCADu vytvářet automatické zobrazení na výkresové šabloně tak aby zůstalo uvnitř nakresleného rámečku nebo uvnitř definovaného prostoru na stránce.

Značka Title block pro popisové pole je použita pro definování místa v Pracovním prostoru, kde toto pole leží. Tato informace je FreeCADem využita k tomu, aby se vyhnul místu s popisovým polem. Může to být označeno jako vyhnutí se popisovému poli.

Jsou-li použity obě tyto značky, musí se značka Working space objevit jako první a musí být ihned následována značkou title block. Obě tyto značky se také musí objevit před první značkou \<metadata. Tyto značky mohou být umístěny buď hned na začátku po značce \<? xml nebo právě před značkou \<metadata. V tomto výukovém programu jsme je umístili na začátek.

#### Značka Working space 

První značka je Working space a je utvořena následovně.

 {.html}



Kde X1, Y1, X2, Y2 jsou definovány jako:

-   X1 je vzdálenost od levého okraje stránky k levé straně rámečku v ose X.
-   Y1 je vzdálenost od horního okraje stránky k horní straně rámečku v ose Y.
-   X2 je vzdálenost od levého okraje stránky k pravé straně rámečku v ose X.
-   Y2 je vzdálenost od horního okraje stránky ke spodní straně rámečku v ose Y.

Takže pro tento výukový program šablony bude značka Working space.

 {.html}



#### Značka Title block 


<div class="mw-translate-fuzzy">

Další značka bude značka Title block a bude utvořena následovně:


</div>

 {.html}



Kde X1a, Y1a, X2a, Y2a jsou definovány jako:

-   X1a je vzdálenost od levého okraje stránky k levé straně popisového pole v ose X.
-   Y1a je vzdálenost od horního okraje stránky k horní straně popisového pole v ose Y.
-   X2a je vzdálenost od levého okraje stránky k pravé straně popisového pole v ose X.
-   Y2a je vzdálenost od horního okraje stránky ke spodní straně popisového pole v ose Y.

Ještě jednou, s odkazem na šablonu vytvořenou v tomto výukovém programu, bude značka Title block vypadat takto:

 {.html}



Umístění těchto dvou značek v požadovaném pořadí na začátku dokumentu vypadá takto:

![](images/Kate3.png )

### Značka freecad:editable 

Přidáním značky freecad:editable do SVG dokumentu umožníme FreeCADu editační přístup k definovaným textovým blokům. U bloků textu, které chcete mít editovatelné z FreeCADu udělejte následující.

Prohledejte odshora dolu SVG dokument až najdete sekci, která obsahuje text, který chcete editovat. Když jste vytvářeli šablonu, umístili jste tyto texty do skupiny, výsledkem je pak to, že i v dokumentu se objeví jako skupina. Když skupinu textových prvků najdete, přidáte řádek freecad:editable=" " ke každému textovému bloku, kde text, který chcete udělat editovatelným je obsažen v uvozovkách. Umístěte jej tak jak je zobrazeno pro všechny čtyři řádky editovatelného textu.

![](images/Kate4.png )

### Značka DrawingContent 

Poslední značka, která je potřebná v šabloně je značka DrawingContent. Bez ní by FreeCAD neměl přístup k výkresové šabloně. Tato značka informuje FreeCAD kde uvnitř dokumentu může uložit zobrazení a další atributy. Je to jedna značka, která musí být v SVG dokumentu výkresové šablony aby spolupracovala s FreeCADem.

Značka je utvořena následovně a je vložena právě před poslední značku


</svg>

.

 {.html}



![](images/Kate5.png )

A je to. SVG dokument nyní může být uložen a používán s FreeCADem.

## Dokončení příkladu šablony 

Dále je doončená SVG šablona. Když víte, že je v SVG formátu, můžete ji otevírat a ukládat ve Vašem textovém editoru jako názorný příklad pro vytváření Vašich vlastních šablon.

![](images/TemplateExample.svg )

## Nástroje

Dva použité nástroje v tomto výukovém programu byly Inkscape a Kate. Oba můžete nalézt na odkazech uvedených níže.

-   [Inkscape](http://www.inkscape.org/)
-   [Kate](http://kate-editor.org/)


{{Drawing Tools navi

}} 
