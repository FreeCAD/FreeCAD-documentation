---
- GuiCommand:
   Name: Part Compound
‏‎   MenuLocation: Part - Make compound
   Workbenches: [Part](Part_Workbench.md)
   SeeAlso: 
---

# Part Compound/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Introducere

Aceată comandă creează un compus/compound din orice forme toplogice. Acestea por fi de tip solid sau plasă cu ochiuri de discretizare sau orice fel de forme topologice.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

Marcați formele toplogice care trebuie adăugate la compound în vizualizarea arborecentă și alegeți **Part → Compound → Make Compound**


</div>

## Notes


<div class="mw-translate-fuzzy">

## Notă

**Warning**
Un compus/compound care conține piese care se intersectează sau atinge este **invalid** pentru operațiile booleene. Din cauza problemelor legate de performanță, nu se face verificarea dacă se intersectează piesele . Verificarea geometriei automate (disponibilă pentru operațiile Boolean) este dezactivată și pentru compusul pieselor.


</div>

To turn this check on go to **Tools → Edit Parameters → Preferences... → Mod → Part → CheckGeometry → RunBOPCheck** and set the parameter to `true`.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/ro
