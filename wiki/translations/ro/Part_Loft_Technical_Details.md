# Part Loft Technical Details/ro
Această pagină explică în detalii cum este creată o suprafață [Loft](Part_Loft.md). Aceasta este un caz particular de suprafața baleiată [Part Sweep](Part_Sweep.md) dar creată de-a lungul unei traiectorii drepte, dar sunt și alte diferențe.

Informațiile furnizate sunt specifice implementării și se pot schimba. Starea actuală este relevantă pentru FreeCAD 0.15.4119, versiunea OCC   * 6.7.0.

## Etapele creării suprafeței riglate Loft 

Pentru a explica procesul de mansardare, este convenabil să-l împărțim în etape   *

1.  faceți ca numărul de segmente din profiluri să fie egal (dacă acestea nu sunt deja)
2.  stabiliți corespondența între segmente
3.  face suprafața mansardei

### pasul 1. Faceți ca numărul de segment din profiluri să se potrivească 

Instrumentul Loft-ul are nevoie de numărul de segmente să se potrivească pentru a crea suprafețe între segmentele corespunzătoare. Dacă numărul de segmente se potrivește în toate profilurile, acest pas poate fi/este omis.

Dacă cel puțin unul dintre profile are un număr diferit de segmente, se aplică următoarea procedură. Procedura este explicată aici pentru cazul a numai două profiluri pentru simplitate.

1.  profilurile sunt aliniate temporar, astfel încât acestea să fie coplanare și să se potrivească centrele lor de masă.
2.  (vezi imaginea) pentru fiecare vârf dintr-un profil, al doilea profil este tăiat la același unghi polar (centrul polar este centrul masei). Dacă există mai mult de o felie posibilă sau nicio felie deloc posibilă (se poate întâmpla pe profile foarte convexe), Loft-ul eșuează în mod obișnuit.
3.  același lucru se face în sens opus.

Operația este extinsă la toate profilurile, pentru a obține un număr egal de segmente. Numărul total de segmente din fiecare profil ar fi egal cu suma tuturor numerelor de segmente ale tuturor profilurilor (cu condiția ca nici unul dintre vârfuri să nu aibă același unghi polar).

   
  <img alt="The process of slicing profile2 (white crescent-like shape) to create joints corresponding to vertices of profile1 (purple pentagon). The inserted joints are marked by yellow arrows." src=images/Loft-vertex-insertion.png  style="width   *300px;">   <img alt="The result of loft relevant to the picture on the left." src=images/Loft_crescent_pentagon.png  style="width   *300px;">
   

### Pasul 2. Establishing correspondence between segments 

<img alt="Demonstration of Loft keeping the number of segments in profiles when they match. Note how 3 edges of the top square \"collapse\" into a small polygonal piece of the bottom profile." src=images/Loft_Number_of_verts_match.png  style="width   *300px;"> În cazul în care numărul de segmente din toate profilurile nu este egal, felierea a fost făcută în pasul 1, iar corespondența este trivială. În cazul în care numerele de segmente din toate profilurile au fost egale, segmentele existente sunt utilizate (vezi imaginea), iar acesta este momentul în care trebuie stabilită corespondența.

Algoritmul exact de a găsi segmente corespunzătoare este complex, dar, în general, tinde să minimizeze răsucirea Loft-ului rezultat. Aceasta înseamnă că, dacă se face o mansardă/loft între două pătrate, este posibilă o răsturnare maximă de \<45 °. Rotirea ulterioară a unuia dintre pătrate va face Loft-ul să sară la alte noduri.

Corespondența dintre profilurile învecinate se face independent. Aceasta înseamnă că răsucirea suplimentară poate fi obținută prin adăugarea de mai multe profiluri.

Un alt lucru care trebuie remarcat este că atunci când numărul de segmente în profiluri este egal, loftul rezultat este substanțial mai robust în ceea ce privește profilurile complexe, în special pentru cele ne-convexe. 

### Pasul 3. Making the loft surface. 

<img alt="A spline interpolation curve (red) that follows the loft surface. The points to interpolate through are shown as red squares." src=images/Loft_B-spline.png  style="width   *400px;"> Dacă există doar două profiluri, suprafețele create sunt suprafețe riglate între segmentele corespunzătoare ale profilurilor. Muchiile/marginile drepte sunt create pentru a conecta vârfurile corespunzătoare ale profilurilor.

Dacă există mai mult de două profile, suprafețele sunt realizate din curbe spline în același mod în care liniile drepte formează suprafețe riglate. Curbele Spline imaginare pe care suprafața este \"realizată\" sunt desenate prin punctele corespunzătoare ale segmentelor corespunzătoare ale profilurilor.

Curebele sunt interpolare B-spline.

-   Dacă numărul de profile este mai mic de 10, interpolarea se face cu o funcție B-spline cu un grad maxim posibil (adică grad = number\_of\_profiles - 1).
-   În cazul în care numărul de profile depășește 10, interpolarea este trecută la funcții B-splinele de gradul 3.

Metoda de îmbinare utilizată este \"lungimea aproximativă a coardei\". Aproximarea constă în faptul că vectorul nodului este exact același pentru fiecare curbă spline dintr-o mansardă/loft. Pentru mai multe informații despre ceea ce este interpolarea B-spline, vectorul nodului, metoda lungimii coardei, a se vedea, de exemplu,[cs.mtu.edu Curve Global Interpolation](http   *//www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/INT-APP/CURVE-INT-global.html).

Rețineți că Loft are o proprietate \"Riglat\". Dacă este setat la adevărat, suprafețele riglate sunt realizate între profilurile învecinate chiar și atunci când există mai multe profiluri. Asta este, interpolarea funcției B-spline este înlocuită cu o interpolare liniară pe bucăți/părți. 

## Esența instrumentului 

-   Instrumentul Loft efectuează o interpolare B-spline între profilurile furnizate. Interpolarea este comutată în liniară pe bucăți/părți atunci când proprietatea \"Ruled\" este setată la true.
-   Când numărul de profile depășește 9, gradul de interpolare este de 3. Această comutare poate reduce semnificativ agitarea/termurul.
-   Dacă se potrivește numărul de segmente (sau numărul de noduri) din profiluri aceasta oferă Loft-ului o răsucire ușoară și, în general, vă permite să utilizați profiluri mai complexe.
-   Când numărul de segmente nu se potrivește, este mai bine să păstrați profilurile astfel încât să poată fi reprezentate de o funcție corespunzătoare (phi) în coordonate polare.

## Observații suplimentare 

-   Nu este necesar ca profilurile să fie paralele (a se vedea imaginea de mai jos).
-   Pentru Loft, nu este necesar ca profilurile să fie separate (a se vedea o imagine de mai jos). Ele pot fi coplanare, dar nu ar trebui să se intersecteze.
-   Când proprietatea \"închisă\" a Loft-ului este \"adevărată\", există o îmbinare la vârf între toate curbele spline care formează Loft-ul (vezi imaginea de mai jos). Nu există nici o modalitate sigură de a închide Loft-ul fără asperități/probleme.

    
  <img alt="It is not required that the profiles are parallel." src=images/Loft_nonparallel.png  style="width   *300px;">   <img alt="In Loft, the profiles can be coplanar. In this example, two of three profiles are coplanar." src=images/Loft_Coplanar.png  style="width   *300px;">   <img alt="An example of a closed loft between three pentagonal profiles (white). Note the non-smooth joint at the outermost profile. This is the first profile in the closed loft." src=images/Loft-closed.png  style="width   *300px;">
    


 

[Category   *Tutorials](Category_Tutorials.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Part_Workbench.md) > Part Loft Technical Details/ro
