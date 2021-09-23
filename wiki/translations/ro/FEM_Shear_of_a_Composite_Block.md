# FEM Shear of a Composite Block/ro



<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic= Finite Element Analysis
|Level= Beginner/Intermediate
|Time= 30 minutes
|Author=[http://www.freecadweb.org/wiki/index.php?title=User: HarryvL]
|FCVersion=0.17.12960 or above
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

### Introducere

În acest tutorial, analizăm deformarea de forfecare a unui bloc compozit constând dintr-un miez rigid încorporat într-o matrice flexibilă.Aceasta demonstrează utilizarea BooleanFragment și CompoundFilter pentru a crea solide pentru bloc și matrice din două cuburi concentrice. Acest flux de lucru asigură faptul că pot fi definite separat MeshRegions, Materiale și Condiții de limită pentru bloc și matricea înconjurătoare. Pentru a selecta regiuni interne, vom face uz de macrocomanda lui Markus Hovorka (https://github.com/drhooves/SelectionTools). Rezultatele CalculiX arată clar efectul nucleului rigid asupra răspunsului blocului de compozit.


</div>


<div class="mw-translate-fuzzy">

### Geometrie

Mai intai creeăm doua cuburi concentrice, unul cu latura având dimensiunea de 10mm și un altul cu dimensiunea de 5mm. Acest lucru se face în Atelierul \"Part\". Implicit, cubul este plasat la originea \[0, 0, 0\], astfel încât cubul mai mic trebuie redus și schimbat prin schimbarea setărilor din fila Date a panoului proprietăților. Pentru a face ca miezul să fie vizibil, Transparența blocului exterior este setată la 50 în fila Vizualizare a panoului de proprietăți. Rezultatul este prezentat mai jos.


</div>

<img alt="" src=images/Pic1.png  style="width:700px;">


<div class="mw-translate-fuzzy">

Apoi evidențiați cele două blocuri ale arborelui și creați un obiect BooleanFragments (Partea\> Split\> Fragmente Booleene). În fereastra \"Property Window - Data Tab\" schimbați modul la CompSolid. Acum, evidențiați Fragmentele Boolean din arborescența Obiect și creați un CompoundFilter (Component\> Compus\> Filtru Compus).


</div>

<img alt="" src=images/Pic2.png  style="width:700px;">


<div class="mw-translate-fuzzy">

### Regiunile de plasă și ochiurile de plasă 

De la masa de lucru FEM vom crea un container de analiză. Aceasta va conține toate definițiile necesare pentru analiza CalculiX și rezultatele acesteia. Rețineți că acest container de analiză trebuie activat (faceți clic dreapta și selectați \"Activare analiză\") ori de câte ori reîncărcați fișierul sau după trecerea de la alte analize. Pentru a porni procesul de întindere, evidențiați CompoundFilter în Arborele Obiect și activați dialogul de plasare \"Mesh\> FEM mesh from shape by Gmsh\". Lăsați dialogul făcând clic pe OK.


</div>


<div class="mw-translate-fuzzy">

Acum este creat un obiect Mesh în Arborele Obiect. Evidențiați acest obiect și creați un obiect din zona Mesh prin \"Mesh\> FEM mesh region\". Deschideți caseta de dialog pentru această regiune a rețelei, dând dublu clic pe și bifați butonul radio pentru Solid. Apoi faceți clic pe butonul \"Adăugați o referință\" și selectați obiectul CompoundFilter din fereastra grafică. Aceasta ar trebui să adauge o trimitere la \"CompoundFilter: Solid1\" în lista de obiecte a regiunii Mesh. În final, specificați dimensiunea maximă a elementului pentru această regiune (5mm în analiza curentă). Lăsați dialogul făcând clic pe OK.


</div>

<img alt="" src=images/Pic3.png  style="width:700px;">

Apoi, creați un obiect Mesh nou ca mai sus și utilizați macrocomanda de selecție (comanda rapidă S, E) pentru a selecta obiectul Cube\_Core din fereastra grafică. De această dată lista de referințe ar trebui să afișeze \"CompoundFilter: Solid2\", după cum urmează. Am ales o dimensiune maximă a elementului de 1mm.

Notă1: Selecția \"CompoundFilter: Solid2\" necesită selectarea uneia dintre fețele sale.

Notă2: Dacă aveți dificultăți la selectarea \"CompoundFilter: Solid2\", este posibil să fi uitat să setați modul BooleanFragments la CompSolid.

<img alt="" src=images/Pic4.png  style="width:700px;">


<div class="mw-translate-fuzzy">

### Material Assignment 


</div>

Materialul este alocat regiunilor Mesh printr-un obiect SolidMaterial. În acest tutorial le atribuim două materiale; unul pentru Matrix și unul pentru Core.


<div class="mw-translate-fuzzy">

Începeți prin selectarea CompoundFilter în arborescența obiect. Apoi creați un obiect SolidMaterial prin opțiunea de meniu \"Model\> Material FEM pentru solid\". Deschideți dialogul și bifați butonul radio pentru Solid, apăsați \"Add Reference\" și selectați obiectul CompoundFilter din fereastra grafică. Lista de referință ar trebui să afișeze acum \"CompoundFilter: Solid1\", ca mai înainte. Atribuiți materiale ABS pentru Matrix, cu modulele lui Young de aproximativ 1% din cele de oțel.


</div>

<img alt="" src=images/Pic5.png  style="width:700px;">

Repetați procedura de mai sus pentru Core (\"CompoundFilter: Solid2\") cu ajutorul macrocomenzii de selecție. De data aceasta atribuim CalciX-Steel, care este mult mai rigid decât materialul ABS pentru Matrix.


<div class="mw-translate-fuzzy">

### Sliding Support 


</div>


<div class="mw-translate-fuzzy">

Pentru a crea o condiție \"Shear Simple\" pentru blocul compozit, deformările la limite trebuie să fie neconstrânse. Pentru a realiza acest lucru, blocul este plasat pe un suport glisant. Acest lucru lasă trei grade de libertate în planul suportului (2 traduceri și o rotație) și acestea vor fi constrânse ulterior. (Notă: deoarece planul previne deformarea feței, aceasta induce încă o constrângere minoră, care ar putea fi eliminată de o altă alegere a condițiilor limită). Pentru a crea o condiție limită de alunecare, adăugați un obiect FemConstraintDisplacement (Model\> Constrângeri mecanice\> Deplasare constrângere). Cu caseta de dialog deschisă mai întâi selectați fața la care urmează să se aplice condițiile de graniță și apoi faceți clic pe butonul Adăugați. Pe măsură ce blocul este lăsat să alunece în planul x-y, este selectat numai butonul radio \"Fixed\" pentru \"Displacement z\", iar celelalte butoane radio sunt lăsate ca \"Free\".


</div>

<img alt="" src=images/Pic6.png  style="width:700px;">


<div class="mw-translate-fuzzy">

### Fixed Nodes 


</div>

Pentru a preveni mișcarea rigidă a corpului în planul de alunecare, trebuie eliminate trei grade independente de libertate. Pentru a realiza acest lucru, un vârf în planul de alunecare este constrâns în direcțiile x și y (eliminând 2 grade de libertate) și un vârf este fixat în direcția x (eliminând ultimul grad de libertate). În acest scop sunt create două obiecte suplimentare FemConstraintDisplacement și rezultatul este prezentat mai jos.

<img alt="" src=images/Pic7.png  style="width:700px;">


<div class="mw-translate-fuzzy">

### Forțe de forfecare 

Ultimul pas în definirea Analizei este aplicarea încărcărilor. Pentru a crea o condiție simplă de forfecare, se aplică un set de sarcini de forfecare, după cum se arată mai jos. Fiecare sarcină este aleasă de 1000 N și având în vedere direcțiile de aplicare, forța și momentul de echilibru sunt atinse pentru toate translațiile și gradele de libertate rotative. În FC acest lucru necesită adăugarea a patru obiecte FemConstraintForce (Model\> Constrângeri mecanice\> Forța de constrângere) - câte una pentru fiecare față. Cu prima casetă de dialog, apăsați butonul Adăugare referință și apoi selectați fața pe care se va aplica condiția de margine (Notă: aceasta este o secvență diferită față de cea cu FemConstraintDisplacement). Implicit, aceasta creează un set de forțe perpendiculare pe față (adică o forță normală). Pentru a schimba această forță la o forță de forfecare, apăsați butonul de direcție și selectați o margine cub care merge în direcția dorită. Dacă forța rezultată indică o direcție opusă a ceea ce este necesar, apoi selectați butonul radio pentru \"Direcția inversă\".


</div>

<img alt="" src=images/Pic8.png  style="width:700px;">


<div class="mw-translate-fuzzy">

### CalculiX Analysis 


</div>

Acum au fost definite toate regiuni ale ochiului de plasă, condițiile materiale și limita, fiind gata să analizăm deformarea blocului cu CalculiX. Activați analiza făcând clic dreapta pe \"Activare analiză\", deschideți dialogul CalculiX făcând dublu clic pe obiectul CalculiXccxTools și selectați un director pentru fișierele temporare create atât de FC cât și de CCX. Scrieți fișierul de intrare CCX și verificați mesajele de avertizare sau de eroare.  

<img alt="" src=images/PIC9.png  style="width:700px;">

După aceea, analiza poate fi pornită apăsând butonul RunCalculiX. Dacă totul merge bine, fereastra de ieșire CCX ar trebui să afișeze următoarele mesaje.

<img alt="" src=images/Pic10.png  style="width:700px;">


<div class="mw-translate-fuzzy">

### CalculiX Results 


</div>

După finalizarea analizei, dați dublu clic pe obiectul \"CalciX\_static\_results\" și selectați opțiunea \"Deplasare abs\". Deplasarea maximă de \~ 0,08 mm va apărea în caseta de ieșire relevantă. Deoarece deplasarea maximă este relativ mică în comparație cu dimensiunile blocului (\<1% din dimensiunea blocului), deplasările trebuie să fie scalate. Acest lucru se poate face sub titlul \"Deplasare\" prin bifarea butonului \"Afișare\" și deplasarea deplasării cu un factor de -șir. 20. Deplasarea maximă va fi acum exagerată la aproximativ 20% din dimensiunea cutiei. După închiderea ferestrei de dialog, rețeaua deformată poate fi din nou vizibilă prin evidențierea obiectului Result\_mesh și apăsarea barei de spațiu.

<img alt="" src=images/Figure_11_Deformed_Mesh.png  style="width:700px;">


<div class="mw-translate-fuzzy">

Pentru a investiga deformarea nucleului, trebuie să alunecăm blocul. Acest lucru se poate face prin crearea unui filtru de clipuri. Pentru a activa această funcție, trebuie mai întâi să creați o \"conductă de procesare post\" prin evidențierea obiectului \"CalciX\_static\_results\" și selectând \"Rezultate\> Postare conducte din Rezultat\" din meniu. Apoi, în cazul selectării conductei, creați un filtru Warp (Rezultate\> Filtru Warp), setați Vector = Displacement și Value = 20 pentru a scala deplasarea și Modul de afișare = \"Suprafață cu margini\", Field Coloring = \"Displacement\", Vector = \"Magnitude \"pentru a arăta contururile de deplasare colorate. Apăsați Aplicați și OK. Ca o ultimă etapă, adăugați un Filtru de Clipuri (Rezultate\> Filtru Clip) și creați un plan cu origine \[5.0,2,5,5,0\] și normal \[0,1,0\], adică la o față de bază cu normal în direcția y. Bifați butonul radio \"Cut Cells\" pentru a crea o suprafață plană. Așa cum a fost setat anterior Mod de afișare = \"Suprafață cu marginile\", câmpul Coloring = \"Displacement\", Vector = \"Magnitude\" pentru a afișa contururile de deplasare colorate. Apăsați Aplicați și OK. În cele din urmă, comutați filtrul de avertizare la invizibil pentru a afișa numai blocul tăiat.


</div>

<img alt="" src=images/Figure12_Deformed_Mesh_Clipped_View_(2).png  style="width:700px;">

Din rezultat este clar că miezul rămâne în mare parte nedeformat și ajută să reziste la deformarea matricei moi (comparați unghiul de forfecare a părții albastre cu cel al părții verzi). Ceea ce se evidențiază, de asemenea, este faptul că, în condiții de forfecare simplă, fețele blocului compozit se răsucesc, ceea ce implică faptul că starea limită alunecătoare de la baza cubului oferă o constrângere nejustificată.


<div class="mw-translate-fuzzy">

### Further work 


</div>

Următoarele provocări ar putea fi interesante ca un exercițiu suplimentar:

1\) Corect pentru constrângerea exagerată impusă de condiția limită de alunecare

2\) Încercați să creați condiții de contact între miez și matrice pentru a vedea dacă are loc separarea

Fișierul FC pentru acest tutorial este atașat mai jos ca un punct de pornire.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=26517&start=20>

Distracție Plăcută ! {{Tutorials navi}} {{FEM Tools navi}} 
