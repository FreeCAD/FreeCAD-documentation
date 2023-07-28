# Basic modeling tutorial/cs
---
- TutorialInfo:/cs
   Topic: Introduction to modelling
   Level: Beginner
   Time: 15 minutes
   Author:
   FCVersion:
   Files:
}}

## Introduction


<div class="mw-translate-fuzzy">

Tento Výukový program základního modelování Vám ukáže jak vymodelovat ocelový úhelník. Měli byste vědět že FreeCAD je modulární při konstruování a jako mnoho jiných CAD programů má vždy více než jednu možnost jak věci dělat. Zde si projdeme dvě metody.


</div>

This tutorial was written with version 0.15 of FreeCAD.

## Než začneme 

Mějte na mysli, že FreeCAD je stále v ranné fázi vývoje a proto nemůže být zatím tak produktivní jako jiné CAD aplikace a určitě se setkáte s chybami nebo si vyzkoušíte pády aplikace. FreeCAD už má možnost ukládat záložní soubory. Počet těchto záložních souborů může být specifikován v dialogovém okně předvoleb. Neváhejte použít 2 až 3 záložní soubory dokud nebudete umět s FreeCADem dobře pracovat.

Rozdělanou práci ukládejte často a občas ji uložte pod jiným jménem, získáte tak \"bezpečnou\" kopii, abyste se mohli vrátit k použitelné verzi Vašeho modelu a byli tak připraveni na možnost, že některé příkazy nevrátí očekávané výsledky.


<div class="mw-translate-fuzzy">

## Úvod do modelovacích technik 

První (a základní) technika modelování těles je [Constructive Solid Geometry (CSG)](http://en.wikipedia.org/wiki/Constructive_solid_geometry). Pracujete se základními tvary jako jsou kostky, válce, koule a kužely a konstruujete z nich požadované tvary jejich kombinací, odečítáním jednoho tvaru od druhého nebo jejich protínáním. Tyto nástroje jsou součástí [Pracovní plochy Díl](Part_Workbench/cs.md). Můžete také uplatnit transformace tvarů, jako jsou zaoblení nebo úkosy hran. Tyto nástroje jsou také v [Pracovní ploše Díl](Part_Workbench/cs.md).


</div>

Potom jsou zde také další pokročilé nástroje. Začnete kreslením 2D profilů, které potom vysunete nebo obtočíte.

Takže začněme tak, že si vyzkoušíme udělat nějaké železné nohy ke stolu pomocí těchto dvou metod.


<div class="mw-translate-fuzzy">

## 1.metoda - Konstrukční geometrie těles 

-   Začněte na [pracovní ploše Díl](Part_Workbench/cs.md) (menu **Pohled \> Pracovní plocha \> Díl**)
-   Klikněte na tlačítko <img alt="" src=images/Part_Box.png  style="width:32px;"> [Box](Part_Box/cs.md) pro vytvoření boxu (kostky)
-   Změnte jho rozměry tak, že jej vyberete buď ve 3D prostoru nebo kliknutím na něj v záložce Projektu vlevo, potom
-   klikněte na záložku Data dole v okně Projektu a změňte hodnoty výšky, délky a šířky na 750mm, 50 a 50 *(viz. Obr. 1.1)*
-   Stejným způsobem vytvořte druhý box, ale s hodnotami 750, 40 a 40mm. Ve výchozím postavení bude tento box překrývat ten první. *(viz. Obr. 1.2)*
-   Teď odečtete druhý box od prvního. Vyberte ten první (nazvaný Box), potom druhý (nazvaný Box001), pozor, pořadí výběru je důležitét! (ujistěte se, že oba tvary jsou vybrány v okně stromu projektu. Pamatujte si jednu věc: v navigačním módu Invertor - Vynálezce, nefunguje kombinace Ctrl + klik pro vícenásobný výběr. [Switch](Mouse_Model.md) to either CAD or Blender selection.)
-   On the Part Workbench toolbar, click on the <img alt="" src=images/Part_Cut.png  style="width:32px;"> [Cut](Part_Cut.md) tool.


</div>

![Obr. 1.1 První box](images/Tutorial-normand01.jpg )

![Obr. 1.2 Druhý box na prvním, připraven k odečtení](images/Tutorial-normand02.jpg )

![Obr. 1.3 Po odečtení](images/Tutorial-normand03.jpg )


<div class="mw-translate-fuzzy">

Nyní máte Váš první železný úhelník *(Obr. 1.3)*. všimněte si, že v okně stromu projektu vlevo byly oba boxy přepsány objektem \"Cut\". Ve skutečnosti nezmizely, ale jsou seskupeny pod objektem Cut. Klikněte na + před nimi a uvidíte, že oba boxy jsou stále zde, ale zbarveny šedě *(Obr. 1.4)*. Když kliknete na některý z nich a stisknete klávesu mezerník, tak se ukáže. Mezerník přepíná viditelnost vybraných objektů. *(Obr. 1.5)*


</div>


<div class="mw-translate-fuzzy">

Nechcete úhelník orientovaný takto? Potřebujete pouze změnit umístění boxu Box001. Vyberte jej, mezerníkem zviditelněte a v záložce Data klikněte na + před Umístěním a potom rozbalte parametr Pozice a změňte jeho souřadnice X a Y. Stiskněte ENTER, opět skryjte Box001 a orientace Vašeho úhelníku je nyní jiná. *(Obr. 1.5)* Můžete změnit i rozměry tvaru a objekt Cut bude aktualizován.


</div>

![Obr. 1.4 Operace odečtení ponechá její původní objekty (boxy)](images/Tutorial-normand04.jpg )

![Obr. 1.5 Stále ještě můžete objekty zviditelnit](images/Tutorial-normand05.jpg )


<div class="mw-translate-fuzzy">

Mimochodem, můžeme přidat zaoblení, tak bude úhelník více realistický. Použijeme nástroj <img alt="" src=images/Part_Fillet.png  style="width:32px;"> [Zaoblení](Part_Fillet/cs.md). 
*(Obr. 1.6)*


</div>

![Obr. 1.6 Zaoblené hrany](images/Tutorial-normand06.jpg )


<div class="mw-translate-fuzzy">

## 2.metoda - Vysunutí profilu 

Tato metoda vyžaduje začít kreslení 2D profilu. Musíte aktivovat [pracovní plocha 2D Kreslení](Draft_Workbench/cs.md) (menu **Pohled \> Pracovní plocha \> 2D Kreslení**).


</div>


<div class="mw-translate-fuzzy">

Dále potřebujeme nastavit [pracovní rovinu](Draft_SelectPlane/cs.md). Podle verze FreeCADu máte přímo pod nástrojovým pruhem vpravo tlačítko \"None\". Klikněte na ně a vlevo se objeví hned za \"aktivní příkaz\": Vyberte rovinu Odstup, potom textové pole a několik dalších tlačítek. Předpokládejme, že chcete začít profil v půdorysu, stiskněte XY. Tlačítko \"None\" nyní bude ukazovat \"Top\" jako aktivní rovinu. [Podívejte se na poznámku.](#DraftPlaneButton.md)

Vyberte nástroj ![](images/Draft_Wire.png ) [Drát (lomená čára)](Draft_Wire/cs.md), potom začněte kreslit tvar použitím textových polí pro pozice X a Y. Mělo by být zakliknuto políčko \"Relativně\" i políčko \"Vyplněno\".


</div>


<div class="mw-translate-fuzzy">

-   1\. bod: 0,0
-   2\. bod: 50,0
-   3\. bod: 0,10
-   4\. bod: -40,0
-   5\. bod: 0,40
-   6\. bod: -10,0
-   7\. bod nebudeme zadávat, lepší je kliknout na tlačítko \"Uzavřít\" pro uzavření profilu. Teď bychom měli mít profil, označený \"Drát\" v záložce okna stromu projektu:


</div>


<div class="mw-translate-fuzzy">

![Obr. 1.7 Základní drát](images/Tutorial-normand07.jpg )


</div>


<div class="mw-translate-fuzzy">

Na numerické klávesnici stiskněte nulu a nasatvíte axonometrický pohled.


</div>


<div class="mw-translate-fuzzy">

Aktivujte [pracovní plochu Díl](Part_Workbench/cs.md).


</div>


<div class="mw-translate-fuzzy">

Klikněte na nástroj <img alt="" src=images/Part_Extrude.png  style="width:32px;"> [Vysunout](Part_Extrude/cs.md).


</div>


<div class="mw-translate-fuzzy">

Na záložce Úkoly vlevo vyberte objekt **Drát**. Potom zadejte požadovanou délku, třeba 750mm. Směr ponechte na Z. Klikněte na Použít. Nyní bychom měli mít **Vysunutý** objekt v záložce stromu projektu *(Obr. 1.8)*


</div>

![Obr. 1.8 Vysunutý objekt](images/Tutorial-normand08.jpg )

U této metody mám drobné varování ve srovnání s první: pro úpravu tvaru musíte upravit Drát a to není tak jednoduché jako u předešlé metody.


<div class="mw-translate-fuzzy">

A je ještě několik dalších způsobů jak to udělat! Doufám, že tyto dva příklady Vám pomohou začít. Určitě cestou narazíte na pár zádrhelů (I já jsem narazil, když jsem se učil FreeCAD a to mám zkušenosti s 3D CAD aplikacemi), ale neváhejte se zeptat na [FreeCAD fóru](http://forum.freecadweb.org)!


</div>


<div id="DraftPlaneButton">

Poznámka k tlačítku Pracovní rovina Kreslení:


</div>

Označení na tlačítku Vašeho FreeCADu může být jiné v závislosti na verzi a také na tom co jste dělali předtím. Označení tlačítka může být: \"top\", \"front\", \"side\", \"None\" nebo Vektor reprezentovaný jako d(0.0,0.0,1.0). Také může být prázdný, Například:

![Výběr roviny None](images/DraftPlaneNone.png )

![Výběr roviny Top](images/DraftPlaneTop.png )


<div class="mw-translate-fuzzy">

![Výběr roviny View](images/DraftPlaneView.png ) 


</div>

Instrukce uvedené výše budou fungovat bez ohledu na to co je tlačítku.


 {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Basic modeling tutorial/cs
