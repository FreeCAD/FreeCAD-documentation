# Material/cs
 }


<div class="mw-translate-fuzzy">

Tato stránka je o materiálovém datovém systému FreeCADu.


</div>


{{TOCright}}

This page is about the Material data system in FreeCAD.


<div class="mw-translate-fuzzy">

## Koncept

Protože je obtížné až nemožné definovat daný nebo kompletní seznam materiálových vlastností, jdeme otevřenější cestou. Každý objekt ve FreeCADU, který má něco společného s materiálem bude mít vlastnost nazvanou \"Materiál\", což je seznam klíčů a hodnot, který může udržovat nekonečný počet materiálových vlastností. Vzhledem k tomu, že to je velmi otevřený a rozšiřitelný způsob práce s takovými daty, přináší také nebezpečí chaosu. Proto tato stránka definuje některá pravidla a základní vlastnosti pro práci s takovouto mapou materiálových vlastností.


</div>

## Pravidla

Každá sada vlastností má pouze jeden povinný údaj což je \"Name\" (Jméno). To je primární klíč materiálu. Zbytek materiálových vlastností už je volitelný nebo může být získaný z databáze materiálů.

Jména vlastností (klíče) jsou řazena podle textových řetězců oddělených podtržítkem. První podřetězec je pojmenován podle aplikace nebo standardu, následující mohou být použity pro další skupiny vlastností. Hodnoty také mohou být seskupovány podle podtržítek, např. k oddělení různých druhů oceli. Příklady:

-   Name=Steel\_Cast
-   SpecificWeight=7.85 (at 20° in kg/mm3)
-   EN10027\_name = S235JR+AR (steel standard EN 0027-1)
-   FEM\_YoungsModulus = xx (in mm−1·kg·s−2)
-   FEM\_YoungsModulus\_Z
-   FEM\_YoungsModulus\_X


<div class="mw-translate-fuzzy">

Každá vlastnost má běžně čitelný popis na této Materiálové stránce, s odkazem na další informace (např. Wikipedie).


</div>

Pro každou vlastnost musí být uvedena jednotka založená na interních jednotkách FreeCADu mm-kg-s! To umožňuje konzistentní použití a překlady.

Klíč (Jméno) a hodnota vlastnosti používá pouze ASCII znaky (7-bitů, nejsou povolena diakritická znaménka - háčky, čárky atd.). Klíče jsou zapisovány Camel-Case (slova spojena bez mezer, každé slovo začíná velkým písmenem), ale jsou interpretována bez rozlišení malých a velkých znaků.

Podtržíka později umožňují stromový pohled editoru nebo prohlížeči, kde mohou vytvářet složky.


<div class="mw-translate-fuzzy">

## Nástroje

Existují některé dobré zdroje, které umožňují snadnější práci s materiálem:

-   [Kalkulátor jednotek](http://www.dimensionengine.com/) k získání informací o materiálu v jednotkách potřebných ve FreeCADu
-   [<http://www.matweb.com/>](http://www.matweb.com/) bezplatná databáze materiálů s tisícovkami materiálových hodnot


</div>

## Materiálová databáze 

Máme-li implementován výše uvedný standard, bylo by nesmyslné ukládat všechny vlastnosti znovu a znovu do objektů. V zásadě můžeme vybudovat materiálovou databázi se jménem materiálu jako primárním klíčem. Takže pokud nemáte nějaké specální požadavky pro Váš materiál, jednoduše definujte např. Name=Steel a FreeCAD může načíst všechny vlastnosti z databáze. Všechny další vlastnosti, které přidáte nebo změníte, přepíší ty případně načtené z databáze se stejným jménem.

V budoucnosti bychom mohli takovou databázi hostovat někde na webu a vytvořit univerzální OpenSource materiálovou databázi.

Aktuálně přemýšlím o kompilaci malé kolekce dat (datasetu) se sadou \"základních\" materiálů a jejich základních vlastností a o plné verzi založené na SQLite.


<div class="mw-translate-fuzzy">

## Material.py

Protože správa materiálových vlastností je otravná práce, měli bychom implementovat Modul Pythonu nazvaný Material.py. Bude to místo pro provádění všech druhů pomocných metod pro práci s materiálem.

-   Výpočet hmotnosti z objemu a měrné hmotnosti
-   Převody v různých systémech měrných jednotek
-   Výpočty potřebné ve speciálních aplikacích (např. FEM)
-   a cokoliv dalšího o čem ještě nevíme


</div>

Modul by měl být implementován tak, aby mohl běžet ve FreeCADu nebo samostatně z příkazové řádky (mapa materiálových vlastností se bude dodávat jako mapa v Pythonu).


<div class="mw-translate-fuzzy">

## Souborový formát materiálové karty ve FreeCADu 

Práce s materiáelm znamená často import/export materiálových definicí. Proto je potřebný souborový formát. Protože máme pouze tvar klíč/hodnota, můžeme snadno a jednoduče číst a zpracovávat souborový formát. Proto je vybrán formát [ini-file](http://en.wikipedia.org/wiki/INI_file). Je standardizován a jsou k dispozici parsery (čtou a zpracovávají data v souboru). Např. [Modul konfiguračního parseru v Pythonu](http://docs.python.org/2/library/configparser.html).


</div>


<div class="mw-translate-fuzzy">

Každá materiálová definice je uložena v souboru s příponou .FCMat. Některé z těchto souborů jsou součástí zdrojáků FreeCADu a jsou zkompilovány do binárního tvaru. Jsou přiloženy k distribuci a přístupné. Ale soubory mohou být umístěny a prohlíženy i na různých místech, aby bylo umožněno přidávání dalších nestandardních materiálových definic.


</div>


<div class="mw-translate-fuzzy">

### Příklady

; last modified 1 April 2001 by John Doe
Name=Steel_Cast
Father=Steel
Source=Some material book everyone knows (or not) ;Some comment
 
[EN10027]
; steel standard EN 10027-1
Name=S235JR+AR      
[Graphic]
Color_Emissiv = 255,255,255


</div>

## Materiálové vlastnosti 

Zde je popis dohodnutých materiálových vlastností. Můžete přidat podsekci pro materiálové vlastnosti je-li to obor kde jste experti.

### Základní


<div class="mw-translate-fuzzy">

  Název vlastnosti                  Popis                                                                                                                                                                                                                    Jednotka/Datový typ
  --------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------
  Name                              Jedinečné jméno vlastnosti, podle pravidel uvedených výše                                                                                                                                                                ASCII znaky 7-bit
  Father (otec)                     Název materiálové skupiny kam daný materiál patří. Je-li tato vlastnost definována, materiál dědí všechny vlastnosti svého otce. To znamená, že když dále není nic definováno, budou použity všechny vlastnosti otce..   ASCII znaky 7-bit
  Description (popis)               Místo pro delší popis materiálu                                                                                                                                                                                          ASCII znaky 7-bit
  SpecificWeight (měrná hmotnost)   Měrná hmotnost je váha daného množství (jednotka) materiálu. Podívejte se na: [Měrné hmotnosti](http://en.wikipedia.org/wiki/Specific_weight)                                                                            kg/mm\^3
  Vendor (prodávající)              Specifikuje značku nebo prodávajícího daný materiál                                                                                                                                                                      ASCII znaky 7-bit
  ProductURL                        Internetová adresa (URL) kde lze nalézt více informací o materiálu                                                                                                                                                       ASCII string 7-bit
  SpecificPrice (jednotková cena)   Cena za jednotku materiálu. Jednotky se mohou značně lišit (USD/m³, EUR/kusy, atd\...)                                                                                                                                   ASCII znaky 7-bit

  : Základní vlastnosti materiálu


</div>

**Dodělat:** přidat některé vlastnosti s uspořádacím systémem pro materály (kov, slitina, minerál, dřevo, \....)

### Mechanické


<div class="mw-translate-fuzzy">

  Název vlastnosti                  Popis                                                                                                                                                                                                                                              Jednotka/Datový typ
  --------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------
  YoungsModulus(modul elasticity)   Young\'s modul, známý také jako modul tažnosti nebo modul elasticity, je míra tuhosti elastického materiálu a je to veličina, které charakterizuje materiál. Podívejte se na: [Young\'s modulus](http://en.wikipedia.org/wiki/Young%27s_modulus)   kg\*mm\^-1\*s\^-2 (kPa)
  UltimateTensileStrength           Mez pevnosti v tahu                                                                                                                                                                                                                                N\'\*mm\^-2 (MPa)
  Hardness                          Tvrdost                                                                                                                                                                                                                                            
  EN-10027-1                        V případě ocelových materiálů jsou [třídy oceli](http://en.wikipedia.org/wiki/Steel_grades) jak je difinováno v [Evropském standardu](http://en.wikipedia.org/wiki/European_Committee_for_Standardization) č. 10027-1.                             ASCII znaky 7-bit

  : Mechaické vlastnosti používané ve strojním inžanýrství


</div>

**Dodělat:** přidat další vlastnosti potřebné pro strojařské návrhy.

### Grafické

Tento odstavec definuje materiálové vlastnosti, které se vztahují k vizuálnímu zobrazení materiálu.


<div class="mw-translate-fuzzy">

  Název vlastnosti   popis                                                                                                Jednotka/Datový typ
  ------------------ ---------------------------------------------------------------------------------------------------- -----------------------------------------------
  AmbientColor       Ambient color in the Coin3D color model                                                              desetinné,desetinné,desetinné rozsah: 0.0-1.0
  DiffuseColor       Diffuse color in the Coin3D color model                                                              desetinné,desetinné,desetinné rozsah: 0.0-1.0
  SpecularColor      Specular color in the Coin3D color model                                                             desetinné,desetinné,desetinné rozsah: 0.0-1.0
  EmissiveColor      Emissive color in the Coin3D color model                                                             desetinné,desetinné,desetinné rozsah: 0.0-1.0
  Shininess          Ambient color in the Coin3D color model                                                              desetinné rozsah: 0.0-1.0
  Transparency       Ambient color in the Coin3D color model                                                              desetinné rozsah: 0.0-1.0
  VertxShader        Vertex shader program as defined in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)     Víceřádkový ASCII řetězec 7-bit
  FragmentShader     Fragment shader program as defined in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)   Víceřádkový ASCII řetězec 7-bit

  : Vizuální vzhled


</div>


<div class="mw-translate-fuzzy">

### Metoda konečných prvků (FEM) 

**Dodělat:** Vytvořit kolekci materiálových vlastností FEM.


</div>

  property name                 Description                                                                                                                                                          Unit/Data-Type
  ----------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------
  ThermalConductivity           The [thermal conductivity (R or lambda coefficient)](http://en.wikipedia.org/wiki/Thermal_conductivity) that indicates the capacity to transfer heat of a material   W/m²K
  ThermalExpansionCoefficient                                                                                                                                                                        
  SpecificHeat                                                                                                                                                                                       

  : Thermal properties

### Architktura a BIM 


<div class="mw-translate-fuzzy">

  Název vlastnosti      Popis                                                                                                                                                         Jednotka/Datová typ
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------
  StandardFormat        Specifikační systém standardu používaný u daného materiálu (ASTM, MasterFormat, CSI, OmniClass, etc\...)                                                      ASCII znaky 7-bit
  StandardCode          Specifický kód materiálu podle výše uvedeného formátu standardu                                                                                               ASCII znaky 7-bit
  FireStandard          Standard odolnosti proti ohni u daného materiálu                                                                                                              ASCII znaky 7-bit
  FireClass             [Třída odolnosti proti ohni](http://en.wikipedia.org/wiki/Fire-resistance_rating) materiálu podle výše uvedeného standardu                                    ASCII znaky 7-bit
  ThermalConductivity   [Měrná tepelná vodivost (R nebo lambda koeficient)](http://en.wikipedia.org/wiki/Thermal_conductivity), který u materiálu indikuje schopnost přenášet teplo   W/m²K
  SoundTransmission     Koeficient přenosu zvuku u materiálu                                                                                                                          W/m²K
  Finish                Typ povrchové úpravy materiálu                                                                                                                                ASCII znaky 7-bit
  Color                 Barva materiálu                                                                                                                                               ASCII znaky 7-bit
  UnitsArea             Počet jednotek materiálu potřebný k zaplnění určité plochy                                                                                                    ASCII znaky 7-bit

  : Materiálové vlastnosti využívané ve stavebnictví

**Dodělat:** přídat vlastnosti pro životnost & LEED


</div>

## TODO

-   add sustainability & LEED properties

 {{FEM Tools navi}} 

[Category:Developer](Category:Developer.md) [Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Roadmap](Category:Roadmap.md) [Category:BIM](Category:BIM.md) [Category:File\_Formats](Category:File_Formats.md)
