# Manual:Traditional 2D drafting/ro
{{Manual   *TOC/ro}}


<div class="mw-translate-fuzzy">

S-ar putea să fiți interesat de FreeCAD deoarece aveți deja o experiență tehnică de desen, de exemplu cu software-ul de genul [AutoCAD](https   *//en.wikipedia.org/wiki/AutoCAD). Sau știți deja ceva despre design sau preferați să desenați lucruri înainte de a le construi. În oricare dintre aceste cazuri, FreeCAD dispune de un atelier de lucru mai tradițional, cu instrumente găsite în majoritatea aplicațiilor CAD 2D   * The [Draft Workbench](Draft_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

Proiectul Workbench, deși adoptă metode de lucru moștenite de la lumea tradițională 2D CAD, nu este limitat deloc la domeniul 2D. Toate instrumentele funcționează în întreg spațiul 3D și multe dintre instrumentele de proiectare, de exemplu <img alt="" src=images/Draft_Move.png  style="width   *16px;"> [Move](Draft_Move.md) or <img alt="" src=images/Draft_Rotate.png  style="width   *16px;"> [Rotate](Draft_Rotate.md),sunt utilizate frecvent peste tot în FreeCAD, deoarece sunt adesea mai intuitive decât schimbarea manuală a parametrilor de plasare.


</div>


<div class="mw-translate-fuzzy">

sunt utilizate frecvent peste tot în FreeCAD, deoarece sunt adesea mai intuitive decât schimbarea manuală a parametrilor de plasare.<img alt="" src=images/Draft_Line.png  style="width   *16px;"> [Line](Draft_Line.md), <img alt="" src=images/Draft_Circle.png  style="width   *16px;"> [Circle](Draft_Circle.md), or <img alt="" src=images/Draft_Wire.png  style="width   *16px;"> [Wire](Draft_Wire.md) (polyline), modification tools like <img alt="" src=images/Draft_Move.png  style="width   *16px;"> [Move](Draft_Move.md), <img alt="" src=images/Draft_Rotate.png  style="width   *16px;"> [Rotate](Draft_Rotate.md) or <img alt="" src=images/Draft_Offset.png  style="width   *16px;"> [Offset](Draft_Offset.md), a [working plane/grid system](Draft_SelectPlane.md) care vă permite să definiți exact în ce avion lucrați și un plan complet [snapping system](Draft_Snap.md) care face foarte ușor să desenezi și să poziționezi elementele exact în raport unul cu celălalt.


</div>

Pentru a arăta fluxul de lucru și posibilitățile Atelierului, vom trece printr-un exercițiu simplu, rezultatul căruia va fi acest desen mic, arătând planul unei case mici care conține doar o chicinetă (Un plan destul de absurd, dar putem face ceea ce dorim aici, nu-i așa?)   *

![](images/Exercise_cabin_01.jpg )


<div class="mw-translate-fuzzy">

-   comuntă pe **Draft Workbench**
-   Ca în orice aplicație de desen , este înțelept să setăm corect mediul, asta ne va salva foarte mult timp. Configurează [grid and working plane](Draft_SelectPlane.md), [Text](Draft_Text.md) and [Dimension](Draft_Dimension.md) settings to your liking in menu **Edit -\> Preferences -\> Draft**. În acest exercițiu, totuși, vom acționa ca și cum aceste setări ar fi rămas la valorile lor implicite.


</div>

![](images/Freecad_draft_options_01.jpg )


<div class="mw-translate-fuzzy">

-   O opțiune ar putea avea nevoie de atenția ta, dură   *"**Fill objects with faces whenever possible**\" . Dacă aceasta este marcată, obiectele închise cum ar fi dreptunghiurile sau cercurile vor fi umplute cu o fațetă în mod implicit. Puteți opri această opțiune acum sau mai târziu, dezactivați proprietatea \"**Make Face**\" pentru fiecare obiect individual, pentru a preveni creare de fațete.


</div>

-   Atelierul Draft are de asemenea două bare de instrumente speciale   * unul cu **visual settings**, unde puteți schimba planul de lucru curent, activați/dezactivați modul de construție [construction mode](Draft_ToggleConstructionMode.md) , setați culoarea liniei, culoarea fațetei, grosimea liniei și mărimea textului pentru a fi utilizate pentru obiecte noi și o altă **snap location**. Acolo, puteți activa / dezactiva grila și seta / dezactiva loca\'iile individuale [Snap locations](Draft_Snap.md)   *

![](images/Draft_toolbars.jpg )

-   Pornirea tuturor butoanelor de blocare este convenabilă, dar, de asemenea, face desenarea mai lentă, deoarece trebuie făcut mai mult calcul atunci când mutați cursorul mouse-ului. Este adesea mai bine să lr păstrați numai pe cele pe care le veți folosi efectiv.


<div class="mw-translate-fuzzy">

-   Să începem prin transformarea \"modului de construcție\", ceea ce ne va permite să trasăm câteva linii directoare pe care vom desena geometria finală.
-   If you wish, set the **working plane** to **XY**. Dacă faceți acest lucru, planul de lucru nu se va schimba, indiferent de punctul de vedere curent. Dacă nu, planul de lucru se va adapta automat la vizualizarea curentă și ar trebui să aveți grijă să rămâneți în vederea de sus ori de câte ori doriți să desenați planul XY (la sol).
-   Apoi selctați instrumentul <img alt="" src=images/Draft_Rectangle.png  style="width   *16px;"> [Rectangle](Draft_Rectangle.md) și trageți un dreptunghi, începând de la punctul (0,0,0), de 2 metri pe 2 metri (lăsați Z la zero). Rețineți că majoritatea comenzilor Draft pot fi executate pe deplin de la tastatură, fără a atinge mouse-ul, utilizând comandă lor scurtă de două litere. Primul nostru dreptunghi 2x2m se poate face astfel   * re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**.
-   Duplicați acel dreptunghi cu 15 cm înăuntru, folosind <img alt="" src=images/Draft_Offset.png  style="width   *16px;"> [Offset](Draft_Offset.md) tool, turning its Copy mode on, and giving it a distance of 15cm   *


</div>

![](images/Exercise_cabin_02.jpg )


<div class="mw-translate-fuzzy">

-   Putem apoi trage o pereche de linii verticale pentru a defini unde vor fi plasate ușile și ferestrele noastre, folosind instrumentul <img alt="" src=images/Draft_Line.png  style="width   *16px;"> [Line](Draft_Line.md) . Traversarea acestor linii cu cele două dreptunghiuri ne va da intersecții utile pentru a ne fixa pereții. Desenați primul rând din punct(15cm, 1m, 0) la punctul (15cm, 3m, 0).
-   Multiplicați acea linie de 5 ori, utilizând<img alt="" src=images/Draft_Move.png  style="width   *16px;"> [Move](Draft_Move.md) instrument cu modul de copiere activat. Întoarceți și modul Relativ, care ne va permite să definim mișcări în distanțe relative, ceea ce este mai ușor decât calcularea poziției exacte a fiecărei linii. Dați fiecărei copii noi un punct de pornire, puteți lăsa la (0,0,0) De exemplu, și următoarele puncte relative de capăt    *
    -   line001   * x   * 10cm
    -   line002   * x   * 120cm
    -   line003   * x   * -55cm, y   * -2m
    -   line004   * x   * 80cm
    -   line005   * x   * 15cm


</div>

![](images/Exercise_cabin_03.jpg )


<div class="mw-translate-fuzzy">

-   Asta e tot ce avem nevoie acum, ca să putem schimba modul de construcție. Verificați dacă întreaga geometrie a construcției a fost plasată într-un grup \"Construcție\", ceea ce îl face ușor să o ascundeți dintr-o dată sau chiar să o ștergeți complet ulterior.
-   Acum, să ne desenați cele două piese de perete folosind instrumentul <img alt="" src=images/Draft_Wire.svg  style="width   *16px;"> [Wire](Draft_Wire.md). Fiți siguri că este pornit <img alt="" src=images/Draft_Snap_Intersection.svg  style="width   *16px;"> [intersection snap](Draft_Snap.md), deoarece va trebui să ajungem la intersecțiile liniilor și dreptunghiurilor noastre. Desenați două polilinii după cum urmează, făcând clic pe toate punctele conturului lor. Pentru a le închide, fie faceți clic din nou pe primul punct, fie apăsați butonul **Close**   *


</div>

![](images/Exercise_cabin_04.jpg )

-   Putem schimba culoarea lor gri implicită într-un model frumos de hașură, prin selectarea ambilor pereți, apoi stabilirea lor**Pattern** property to **Simple**, and their **Pattern size** to your liking, for example **0.005**.

![](images/Exercise_cabin_05.jpg )


<div class="mw-translate-fuzzy">

-   Acum putem ascunde geometria construcției făcând clic cu butonul din dreapta pe grupul Construcții și alegeți **Hide Selection**.
-   Acum, trageți ferestrele și ușile. Asigurați-vă că <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width   *16px;"> [midpoint snap](Draft_Snap.md) is turned on, and draw six lines as follow   *


</div>

![](images/Exercise_cabin_06.jpg )


<div class="mw-translate-fuzzy">

-   Vom schimba acum linia de ușă pentru a crea un simbol pentru ușă deschisă. Începeți prin rotirea liniei folosind <img alt="" src=images/Draft_Rotate.png  style="width   *16px;"> [Rotate](Draft_Rotate.md) tool. Click the endpoint of the line as rotation center, give it a start angle of **0**, și un unghi final de **-90**.
-   Apoi creăm arcul care descrie deschiderea ușii <img alt="" src=images/Draft_Arc.png  style="width   *16px;"> [Arc](Draft_Arc.md) tool. Alegeți același punct ca și centrul de rotație pe care l-am folosit la pasul anterior ca centru, faceți clic pe celălalt punct al liniei pentru a da raza, apoi punctul de început și sfârșit după cum urmează   *


</div>

![](images/Exercise_cabin_07.jpg )


<div class="mw-translate-fuzzy">

-   Acum putem începe să punem niște mobilier. Pentru a începe, să punem o masă prin desenarea unui dreptunghi din colțul interior din stânga sus și dându-i o lățime de 170 cm și o înălțime de -60 cm. În imaginea de mai jos,**Transparency** property of the rectangle is set to 80%, to give it a nice furniture look.
-   Adica să adaugăm o chiuvetă si un aragaz. Desenarea acestor tipuri de simboluri de mână poate fi foarte obositoare și de obicei sunt ușor de găsit pe internet, de exemplu pe <http   *//www.cad-blocks.net> . In the **Downloads** pentru secțiunea de mai jos, pentru separare, am separat o chiuvetă și un aragaz de acest proiect și le-am salvat ca fișiere DXF. Puteți descărca aceste două fișiere vizitând linkurile de mai jos și făcând clic dreapta pe **Raw** button, then choosing **save as**.
-   Inserarea unui fișier DXF într-un documente deschis FreeCAD poate fi realizată fie prin alegerea **File -\> Import** opțiunea de meniu sau prin glisarea și plasarea fișierului DXF din fișierul de explorare în fereastra FreeCAD. Este posibil ca conținutul fișierelor DXF să nu apară chiar în centrul vizualizării curente, în funcție de locul în care se află în fișierul DXF. Puteți utiliza meniul**View -\> Standard views -\> Fit all** pentru a micșora și a găsi obiectele importate. Introduceți cele două fișiere DXF și deplasați-le într-o locație potrivită pe tăblia mesei   *


</div>

![](images/Exercise_cabin_08.jpg )


<div class="mw-translate-fuzzy">

-   Acum putem plasa câteva cote/dimensiuni folosind <img alt="" src=images/Draft_Dimension.png  style="width   *16px;"> [Dimension](Draft_Dimension.md) tool.Cotele sunt extrase făcând clic pe 3 puncte   * punctul de început, un punct final și un al treilea punct pentru a plasa linia de cotă. Pentru a face cote orizontale sau verticale, chiar dacă cele două prime puncte nu sunt aliniate, apăsați **Shift** while clicking the second point.
-   Puteți modifica poziția unui text de cotă făcând dublu clic pe cota din afișarea arborescentă. Un punct de control vă va permite să mutați grafic textul. În exercițiul nostru, \"0.15\" texts have been moved away for better clarity.
-   Puteți schimba conținutul textului de dimensiune modificând-o **Override** proprietate. În exemplul nostru, textele cotelor ușii și ferestrelor au fost editate pentru a indica înălțimea lor   *


</div>

![](images/Exercise_cabin_09.jpg )


<div class="mw-translate-fuzzy">

-   Să adăugăm câteva texte de descriere folosind <img alt="" src=images/Draft_Text.png  style="width   *16px;"> [Text](Draft_Text.md) tool. Faceți clic pe un punct pentru a poziționa textul, apoi introduceți liniile de text, apăsând Enter după fiecare linie. Pentru a termina, apăsați pe Enter de două ori.
-   Liniile de indicație (numite și \"lideri\") care leagă textele de elementele pe care le descriu sunt pur și simplu făcute cu instrumentul Wire. Desenați poliliniile, pornind de la poziția textului, până la locul descris. Odată ce acest lucru este făcut, puteți adăuga un glonț sau o săgeată la sfârșitul poliliniilro prin setarea lor **End Arrow** property to **True**


</div>

![](images/Exercise_cabin_10.jpg )

-   Desenul nostru este acum complet! Deoarece există destul de multe obiecte acolo, ar fi înțelept să faceți ceva curățenie și să restructurați totul în grupuri frumoase, pentru a face fișierul mai ușor de înțeles pentru alte persoane   *

![](images/Exercise_cabin_11.jpg )


<div class="mw-translate-fuzzy">

-   Putem imprima acum lucrarea noastră plasând-o pe o foaie de desen, pe care o vom arăta mai târziu în acest manual sau vom exporta direct desenul nostru la alte aplicații CAD, exportându-l într-un fișier DXF. Pur și simplu selectați-ne\"Floor plan\" group, select menu **File -\> Export**, și selectați formatul Autodesk DXF. Fișierul poate fi apoi deschis în orice altă aplicație CAD 2D cum ar fi [LibreCAD](http   *//www.librecad.org). Ați putea observa unele diferențe, în funcție de configurațiile fiecărei aplicații.


</div>

![](images/Exercise_cabin_12.jpg )


<div class="mw-translate-fuzzy">

-   Cel mai important lucru despre Workbench Draft este însă faptul că geometria pe care o creați cu ea poate fi folosită ca bază sau ușor extrudată în obiecte 3D, pur și simplu prin utilizarea <img alt="" src=images/Part_Extrude.png  style="width   *16px;"> [Part_Extrude](Part_Extrude.md) tool from the [Part Workbench](Part_Workbench.md), or, to stay in Draft, the <img alt="" src=images/Draft_Trimex.png  style="width   *16px;"> [Trimex](Draft_Trimex.md) (Trim/Extend/Extrude) care, sub capotă, efectuează o Extruziune de Piesă, dar o face \"modul Draft\", adică vă permite să indicați și să fixați grafic lungimea de extrudare. Experimentați extrudarea pereților noștri, după cum se arată mai jos.
-   Apăsând <img alt="" src=images/Draft_SelectPlane.png  style="width   *16px;"> [working plane](Draft_SelectPlane.md) după selectarea unei fețe a unui obiect, puteți, de asemenea, plasa planul de lucru oriunde și, prin urmare, desenați obiecte Draft în diferite planuri, de exemplu, deasupra pereților. Acestea pot fi apoi extrudate pentru a forma alte solide 3D. Experimentați setarea planului de lucru pe una dintre fețele superioare ale pereților, apoi trageți niște dreptunghiuri acolo.


</div>

![](images/Exercise_cabin_13.jpg )

-   Tot felul de deschideri se poate realiza la fel de ușor prin desenarea obiectelor de Draft pe fețele pereților, apoi prin extrudare, apoi prin folosirea uneltelor booleene de la Atelierul Piese pentru a le extrage dintr-un alt solid, după cum am văzut în capitolul precedent.


<div class="mw-translate-fuzzy">

În mod fundamental, ceea ce face Atelierul Draft este de a oferi metode grafice pentru a crea operațiuni Part. În timp ce sunteți în Part, veți poziționa obiectele în mod obișnuit prin setarea parametrului lor de plasare, în Draft puteți face acest lucru pe ecran. Există momente când una este mai bună, alteori când celălaltă este preferabilă. Nu uitați, puteți crea [custom toolbars](Interface_Customization.md) într-unul din aceste Ateliere de lucru, adăugați instrumentele de la celălalt și obțineți cele mai bune rezultate din ambele lumi.


</div>


<div class="mw-translate-fuzzy">

**Fişiere de descărcat**


</div>

-   Fișierul creat în timpul acestui exercițiu   * <https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   Fișierul DXF chivetei    * <https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   Fișier DXF al aragazului   * <https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   Fișierul final DXF produs în timpul acestui exercițiu   * <https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>


<div class="mw-translate-fuzzy">

**De citit în plus**


</div>


<div class="mw-translate-fuzzy">

-   [The Draft Workbench](Draft_Workbench.md)
-   [Snapping](Draft_Snap.md)
-   [The Draft working plane](Draft_SelectPlane.md)


</div>


<div class="mw-translate-fuzzy">


</div>

[Category   *Tutorials/ro](Category   *Tutorials/ro.md) [Category   *Tutorials](Category_Tutorials.md) [Category   *Draft](Category_Draft.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/ro
