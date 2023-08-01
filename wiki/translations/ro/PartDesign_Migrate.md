---
- GuiCommand:/ro
   Name/ro:PartDesign Migrate
   Empty:1
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Migrate
   Version:0.17
---

# PartDesign Migrate/ro


</div>

## Descriere

Atelierul PartDesign în FreeCAD v0.17 introduce noi instrumente și elemente care și elemente care nu sunt recunoscute de versiunile mai vechi ale FreeCAD (0.16 and older). Documentele FreeCAD create în versiuni mai vechi pot fi deschise și editate. Pentru a beneficia de noile caracteristici, acestea trebuie migrate prin intermediul meniului PartDesign → Migrate.


<small>(v0.17)</small> 

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Deschide un document FreeCAD (≤ 0.16).
2.  Comutați pe atelierul PartDesign.
3.  Mergeți la meniu **Part Design** → **Migrate** .
4.  Dacă funcționează migrarea, a <img alt="" src=images/Std_Part.png  style="width:24px;"> [Part container](Std_Part.md) va fi creat care va deține unul sau mai multe <img alt="" src=images/PartDesign_Body.png  style="width:24px;"> [Bodies](PartDesign_Body.md), fiecare gazduind un lanț de caracteristici.


</div>

## Limite


<div class="mw-translate-fuzzy">

-   Înainte de a începe procesul de migrare, verificați dacă modelul a fost construit cu opțiunile de rafinare automată activate (in Edit → Preferences → Part design → General), și setați preferințele dvs. în consecință. Acest lucru poate fi ușor determinat prin trecerea succesivă a vizibilității entităților din arborescența modelului.Dacă nu mai există margini reziduale între funcții cum ar fi Pads and Pockets,opțiunile de rafinare automată au fost dezactivate.
-   Dacă un document de migrare conține numai schițe și funcții PartDesign, procesul de migrare poate avea succes. Unele caracteristici, cum ar fi șanfrenul și rotunjirile, pot necesita reconstruire.
-   În cazul în care documentul care urmează să fie migrat are un flux de lucru amestec de Part/Part Design/Draft work flow, conversia va eșua cel mai probabil sau, în cel mai bun caz, produce rezultate neașteptate și va trebui să migrați manual.


</div>





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate/ro
