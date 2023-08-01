---
- GuiCommand:
   Name: Part BooleanFragments
   MenuLocation: Part - Split - Boolean Fragments
   Workbenches: [Part](Part_Workbench.md)
   Version: 0.17
   SeeAlso: [Part Slice](Part_Slice.md), [Part XOR](Part_XOR.md), [Part Join features](Part_CompJoinFeatures.md), [Part Boolean](Part_Boolean.md)
---

# Part BooleanFragments/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Tool to compute all fragments that can result from applying Boolean operations between input shapes. For example, for two intersecting spheres, three non-overlapping but touching solids are generated.


</div>

![600px](images/Part_BooleanFragments_Demo.png)


<div class="mw-translate-fuzzy">

(pe imaginea de mai sus, piesele au fost mutate separat manual după aceea, pentru a dezvălui felierea)


</div>


<div class="mw-translate-fuzzy">

Forma de ieșire este întotdeauna un compus. Conținutul compusului depinde de tipurile de intrare și de modul de operare. Asta înseamnă că nu primești imediat accesul la piesele individuale ale rezultatului - piesele rămân grupate împreună. Piesele individuale pot fi extrase prin explodarea compusului ([Draft Downgrade](Draft_Downgrade.md)).


</div>

Instrumentul are trei moduri: \"Standard\", \"Split\" și \"CompSolid\".

\"Standard\" și \"Split\" diferă de acțiunea instrumentului pe fire/polilinii, shells și compsolids: dacă este \"Split\", acestea sunt separate; dacă este \"Standard\", acestea sunt păstrate împreună (obțineți segmente suplimentare).

Structura de comprimare în modurile \"Standard\" și \"Split\" urmează structura de compunere a intrărilor. Adică, dacă se alimentează cu doi compuși, fiecare conținând o sferă ca în exemplul de mai sus, rezultatul va conține de asemenea doi compuși, fiecare conținând bucățile sferei conținute inițial. Aceasta înseamnă că piesa comună va fi repetată de două ori în rezultat. Numai în cazul în care shperes de intrare ambele nu sunt în compuși, rezultatul va conține piesa comună o singură dată.

În modul \"CompSolid\", solidele sunt unite într-un compsolid (compsolid este un set de solide conectate prin fețe, ele sunt legate de solide, cum ar fi firele sunt legate de margini, și shell-urile sunt legate de fețe, numele fiind probabil o scurtă expresie \"solid compozit\"). Rezultatul este un compus non-imbricat de compsolids

## Usage


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Selectați obiectele care urmează să fie intersectate.
    Ordinea de selecție nu este importantă, deoarece acțiunea instrumentului este simetrică. Este suficient să selectați o sub-formă a fiecărui obiect (de exemplu, fețele). De asemenea, puteți selecta un compus care conține toate formele de conectat, de ex. [Array Draft](Draft_Array.md).
2.  Invoca comanda BooleanFragments parte.


</div>


<div class="mw-translate-fuzzy">

Se creează un obiect parametru Boolean Fragments. Obiectele originale sunt ascunse, iar rezultatul intersecției este afișat în vizualizarea 3D.


</div>

## Properties


<div class="mw-translate-fuzzy">

## Proprietăți


{{TitleProperty|Boolean Fragments}}

-    **Objects**:Lista obiectelor care urmează să fie intersectate. În general, sunt necesare cel puțin două obiecte, dar un singur compus care conține formele care se intersectează va face și el. (din FreeCAD v0.17.8053, această proprietate nu este afișată în editorul de proprietăți și poate fi accesată numai prin Python).

-    {{PropertyData | Mod}}: \"Standard\", \"Split\" sau \"CompSolid\". \"Standard\" este implicit. Standard și Split diferă prin acțiunea instrumentului pe formele de tip agregate: dacă sunt separate, acestea sunt separate; altfel ele sunt păstrate împreună (obțineți segmente suplimentare).

-    {{PropertyData | Tolerance}}: valoarea \"fuzziness\". Aceasta este o toleranță suplimentară aplicabilă în cazul căutării intersecțiilor, pe lângă toleranțele stocate în formele de intrare.


</div>

## Implementation details 


<div class="mw-translate-fuzzy">

## Implementarea detaliilor 

Funcția Boolean Fragments (\"Fragmente booleene\") în modul \"Standard\" este operatorul general al siguranței OpenCascade (GFA). Acceptă o combinație de probabil toate tipurile de forme, iar logica ieșirii este destul de complicată. Vedeți [OpenCascade user guide: Boolean operations](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__boolean_operations.html).


</div>

Pentru modurile \"Split\" și \"CompSolid\", post-procesarea suplimentară este efectuată de FreeCAD.



## Script


<div class="mw-translate-fuzzy">

Instrumentul poate fi utilizat în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>

**BOPTools.SplitFeatures.makeBooleanFragments(name)**

-   Creează o funcție()onalitate BooleanFragments vidă. Proprietatea \"Obiecte\" trebuie să fie atribuită în mod explicit, după aceea.
-   Returnează obiectul nou creat.

BooleanFragments poate fi aplicată și în forme simple, fără a avea nevoie de un obiect de document, prin:


{{code|code=
import BOPTools.SplitAPI
BOPTools.SplitAPI.booleanFragments(list_of_shapes, mode, tolerance = 0.0)

# OR, for Standard mode:

list_of_shapes = [App.ActiveDocument.Sphere.Shape, App.ActiveDocument.Sphere001.Shape]
pieces, map = list_of_shapes[0].generalFuse(list_of_shapes[1:], tolerance)
# pieces receives a compound of shapes; map receives a list of lists of shapes, defining list_of_shapes <--> pieces correspondence 
}}

Acest lucru poate fi util pentru crearea de caracteristici scripturi personalizate Python.

Exempluː {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeBooleanFragments(name= 'BooleanFragments')
j.Objects = FreeCADGui.Selection.getSelection() 
}}

Instrumentul propriu-zis este implementat în Python, vezi /Mod/Part/BOPTools/SplitFeatures.py unde este instalat FreeCAD.

## Notes


<div class="mw-translate-fuzzy">

## Versiune

Acest instrument a fost introdus în FreeCAD v0.17.8053. FreeCAD și necesită compilarea cu OCC 6.9.0 sau mai recent; altfel instrumentul este inutilizabil.


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part BooleanFragments/ro
