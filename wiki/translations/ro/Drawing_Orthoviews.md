# Drawing Orthoviews/ro
---
- GuiCommand:   Name:Drawing Orthoviews   Workbenches:[MenuLocation:Drawing → Insert orthographic views   Shortcut:none   SeeAlso:[[Drawing Landscape A3|Drawing Landscape A3](Drawing_Workbench___Drawing]],_Complete.md)---

Instrumentul Orthoviews introduce un set de proiecții ortogonale ale obiectului selectat în foaia de desen activă. Rețineți că nu creează un singur obiect de vizualizare pe pagină. În schimb, va fi creată o proiecție ortogonală separată pentru fiecare dintre vizualizările selectate în opțiuni.

Instrumentul Orthoviews creează toate proiecțiile ortogonale reprezintă locația potrivită pentru vizualizarea principală dată.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

1.  Selectați o funcție în arborescența modelului.
2.  Dacă există mai mult de o pagină, multi-selectați pagina dorită (păstrând în același timp caracteristica selectată).
3.  Apăsați butonul **<img src="images/Drawing_Orthoviews.png" width=16px> [Insert orthographic views](Drawing_Orthoviews.md)**.
4.  Definiți opțiunile de creare a vizualizării dorite. Consultați [ Opțiuni](#Opțiuni.md).
5.  Faceți clic pe OK pentru a crea vizualizările funcțiilor selectate pe pagina selectată.

## Opţiuni

În funcție de selecțiile efectuate, este posibil ca unele opțiuni să nu fie disponibile.

![](images/Drawing_Orthoviews_Options.png )

-   **Proiecție**: Selectați dacă doriți un al treilea unghi (implicit) sau proiecție în primul unghi
-   **Vedere din**: Alegeți axa care se va afla din foaia de desen spre utilizator.
-   **Axa aliniată dreapta**: Alegeți axa care se îndreptă spre dreapta pe foaia de desen. Axa rămasă va fi verticală pe pagină.
-   **Vederi secundare**: Alegeți vizualizările pe care doriți să le creați. Vederea principală se află în centrul casetelor de selectare și este orientată de vizualizările{{Variable|View from}} și {{Variable|Axis aligned right}}. Vizualizările secundare vor fi create pentru fiecare casetă care este bifată.

### General


<div class="mw-translate-fuzzy">

-   **Scala / poziția automată**: Dacă este bifată această casetă, va fi aleasă scara de vizualizare, locația și spațiul pentru a utiliza cel mai bine spațiul disponibil pe pagină. Dacă această casetă nu este bifată, utilizatorul specifică scala, locația și spațierea.
-   **Scale**: Scara pentru vizualizare, exprimată ca numitor al unei fracțiuni de scară. Astfel, {{SystemInput | 2 |}} va crea un set de vizualizări scalate la 1: 2.
-   **Sus la stânga x / y**: Locația setului de vizualizări din partea stângă sus a paginii. Incorporarea valorii x (prima coloană) mișcă vizualizările spre dreapta. Creșterea valorii y (a doua coloană) mută vizualizările în jos pe pagină.
-   **Spacing dx / dy**: Distanțele x (prima coloană) și y (a doua coloană) între vizualizările adiacente. Distanțele sunt spațiul dintre sistemul de coordonate al părții; în majoritatea cazurilor va exista un spațiu mai mic între vizualizările că valoarea de spațiu (deoarece vizualizările au dimensiuni x și y).
-   **Afișați linii ascunse**: Dacă selectați, liniile ascunse vor fi vizibile în vizualizările create.
-   **Arătați liniile netede**: Dacă este selectată, arătați linii în care curbura este discontinuă (de exemplu, unde o racordare se conectează la o parte plată).


</div>

## Proprietăți

Nu există proprietăți pentru această comandă; comanda creează proprietăți pentru fiecare vizualizare individuală.

## Scrip-Programare 

Drawing Orthoviews nu este numit în scripting. Vizualizările individuale create de comanda Drawing Orthoviews pot fi create în scripturi.

## Limite

De completat

## Tutoriale

-   [Drawing tutorial](Drawing_tutorial.md), Introducere pentru crearea de planuri cu Atelierul Drawing workbench
-   [Manual:Generating 2D drawings](Manual_Generating_2D_drawings.md) cu Atelierul Drawing și cu addon-ul Drawing Dimensioning .


{{docnav|[Open Browser](Drawing_Openbrowser.md)|[Symbol](Drawing_Symbol.md)|[Drawing Workbench](Drawing_Workbench.md)|IconL=Drawing_Openbrowser.png|IconC=Workbench_Drawing.svg|IconR=Drawing_Symbol.png}}


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing Orthoviews/ro
