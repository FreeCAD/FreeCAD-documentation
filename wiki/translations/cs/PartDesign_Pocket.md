---
- GuiCommand:/cs   Name:PartDesign_Pocket   Name/cs:Návrh dílu Kapsa   Workbenches:[[PartDesign Workbench/cs   Návrh dílu]], Kompletace|MenuLocation:Návrh dílu -> Kapsa---


</div>


<div class="mw-translate-fuzzy">

## Úvod

\'Vytvoří kapsu podle vybraného náčrtu\' - Tento nástroj vezme vybraný náčrt a vytvoří s ním kapsu. Pojem kapsa je používán pro vysunutí náčtru tak, že odebírá objem z konstrukce do které proniká. Například, je-li náčrt tvořen jednoduše kružnicí na jedné ploše kostky, pak nástroj kapsa vytvoří díru \'vyvrtanou\' do kostky:


</div>

![](images/PartDesign_Pocket_example.svg ) \'\'Sketch profile (A) was mapped to the top face of base solid (B); result after pocketing through on the right. \'\'

## Usage

1.  Select the sketch to be pocketed.

    :   The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear. {{VersionMinus|0.16}}
2.  Press the **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''** button.
3.  Set the Pocket parameters (see next section).
4.  Click OK.

## Volby

![](images/Pocket_options_cs.png )


<div class="mw-translate-fuzzy">

Při vytváření kapsy nabízí dialogové okno \'parametrů kapsy\' čtyři různé způsoby pro zadání hloubky do jaké bude kapsa vysunuta

### Rozměr

Zadání číselné hodnoty pro hloubku kapsy. Defaultní směr pro vysunutí je do podkladu. Vysunutí je ve směru [kolmém](http://en.wikipedia.org/wiki/Surface_normal) k definované rovině náčrtu. Záporné hodnoty nejsou možné.

### Do první {#do_první}

Kapsa bude vysunuta až do první plochy podkladu ve směru vysunutí. Jinými slovy odebírá všechen materiál až dokud nenarazí na prázdný prostor.

### Skrz celý {#skrz_celý}

Kapsa vyseká všechen materiál ve směru vysunutí. S volbou **Symetricky k rovině** bude kapsa vysekána celým materiálem v obou směrech.

### Až k ploše {#až_k_ploše}

Kapsa bude vysunuta až k ploše podkladu, která může být vybrána kliknutím na ni.


</div>

### Up to face {#up_to_face}

The pocket will extrude up to a face in the support that can be chosen by clicking on it.

### Two dimensions {#two_dimensions}

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option. <small>(v0.17)</small> 

## Omezení

-   Použijte **Rozměr** nebo **Skrz vše** kdykoliv je to možné, protože s ostatními typy jsou někdy problémy, když jsou vzorkovány
-   Jinak objekt kapsa má stejná [omezení](PartDesign_Pad/cs#Limitations.md) jako objekt Deska.

## Užitečné odkazy {#užitečné_odkazy}

[Příklad](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) na fóru.





{{PartDesign Tools navi

}} 
