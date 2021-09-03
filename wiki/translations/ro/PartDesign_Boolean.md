---
- GuiCommand:/ro
   Name:PartDesign Boolean
   Name/ro:PartDesign Operație booleană
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Operație booleană
   Version:0.17
---


</div>

## Descriere


<div class="mw-translate-fuzzy">

**PartDesign Boolean** importă una sau mai multe [PartDesign Bodies](PartDesign_Body.md) or [PartDesign Clones](PartDesign_Clone.md) (designated as \"tool bodies\") în Corpul PartDesign și aplică o operație booleană (fuse, cut or common).


</div>

![](images/PartDesign_Boolean_example.png )


<div class="mw-translate-fuzzy">

*În stânga: corpul activ (A) cu insrumentele corpurilor (B) și (C); rezultă în dreapta după Boolean Cut.*


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}


</div>


<div class="mw-translate-fuzzy">

1.  Activați corpul care primește funcționalitatea Booleană. \'**\'Note**:este important să vă asigurați că nu este selectată nici corpul activ și nici una dintre funcțiile pe care le conține acesta înainte de a trece la pasul 2. \"
2.  apăsați buton **<img src="images/PartDesign_Boolean.png" width=24px> '''Boolean'''**.
3.  În **Boolean Parameters**, click pe butonul **Add body**. Corpul activ dispare temporar din vizualizarea 3D pentru a facilita selecțiile.
4.  În vizualizarea 3D, selectați Body care se va utiliza în funcția Booleană. Repetați pentru a adăuga mai multe corpuri.
5.  Selectați tipul operațiunii Booleene în meniul derulant (Fuziune, Substracție ori Intersecție)
6.  Click **OK**.

De asemenea, puteți selecta unul sau mai multe corpuri înainte de a apăsa butonul Boolean. acestea vor fi adăugate automat.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   **Fuse:** unește corpul sau corpurile de corpul activ.
-   **Cut:** scade corpul sau corpurile din corpul activ.
-   **Common:** extrage intersecția dintre corpul sau corpurile selectate cu corpul activ
-   Apăsați butonul **Remove body** pentru a extrage corpul,prin selectarea acestuia în vizualizarea 3D.


</div>

## Proprietăți

-    **Type**: setează operația Boolean (Fuse, Cut, Common)

-    **Label**: nume dat operațiunii, acest nume poate fi schimbat dacă vă convine.

-    **Group**: listează corpurile implicate.

-    **Display**: setează afișarea între 2 moduri:

    -   Result (default): afișează rezultatul funcțiilor Booleene. În acest mod, corpurile implicate nu pot fi afișate în starea inițială, chiar și atunci când vizibilitatea acestora este activată.
    -   Tools: afișează corpurile instrumentate în starea inițială. Acest mod este util atunci când este necesară editarea lor.

-    **Selectable**: true or false. Dacă este setat la falsă, funcția nu poate fi selectată în vizualizarea 3D.

-    **Visibility**: true or false. Comută vizibilitatea funcției în vizualizarea 3D.

## Limite

-   Pentru ca Intersecția să lucreze cu mai mult de un corp, altul decât corpul activ, fiecare trebuie să aibă o parte comună cu corpul activ.
-   Corpurile folosite adoptă originea locală a corpului activ. Dacă corpul activ nu este localizat la coordonatele (0,0,0) în sistemul global de coordonate, plasarea corpurilor utilizate trebuie să fie relativă față de corpul activ. Poate fi mai ușor să transpuneți plasarea corpului activ la origine înainte de a aplica funcția Boolean și apoi să o readuceți la locația inițială.





{{PartDesign Tools navi

}} 
