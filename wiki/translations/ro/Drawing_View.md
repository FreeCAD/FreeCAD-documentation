---
- GuiCommand:/ro   Name:Drawing View   Name/ro:Drawing View   Workbenches:[MenuLocation:Drawing → Insert view in drawing   Shortcut:none   SeeAlso:[[Drawing Landscape A3/ro|Drawing Landscape A3](Drawing_Workbench/ro___Drawing]],_Complete.md)---


</div>

Acest instrument creează o nouă vedere a obiectului selectat în foaia activă de desen.

<img alt="A drawing sheet with three views: front, top and isometric." src=images/Drawing_Views.png  style="width:500px;">


<div class="mw-translate-fuzzy">

### Cum se utilizează {#cum_se_utilizează}

Selectați un obiect în vizualizarea 3D sau în arborescența Proiect, apoi faceți clic pe instrumentul Vizualizare desene. În mod prestabilit, în partea stângă sus a paginii va fi afișată o vedere de sus scara la 1: 1 (scară reală). Este posibil să nu fie vizibil dacă este prea mic sau prea mare pentru pagină.


</div>

Un obiect \'\'\' View *\' se adaugă la obiectul*\' Page \'\'\' din arborescența Project. Pentru afișările ulterioare, se va adăuga un număr de trei cifre la nume. Faceți clic pe săgeata din fața obiectului Pagină pentru a o deschide și afișați vizualizările pe care le conține.

Dacă numai obiectul este selectat în Arborescența proiectului, vizualizarea este adăugată la prima pagină a proiectului. Dacă aveți mai multe pagini în proiect, selectați obiectul și pagina la care ar trebui adăugată. Apoi faceți clic pe pictograma pentru a adăuga vizualizarea la pagina selectată.

### Modificați o vizualizare existentă {#modificați_o_vizualizare_existentă}

Deschideți obiectul Page din arborele Project și selectați View. Parametrii săi pot fi editați în fila Vizualizare proprietăți.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Isometric view with smooth lines visibility off](images/Drawing_View_Iso.png‎  style="width:150px;"> <img alt="Isometric view with smooth lines visibility on" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width:150px;">

-   **Label**: modifică eticheta vizualizării în arborescența proiectului. De asemenea, puteți să dați clic pe Afișați din arborescență și să faceți clic dreapta pe → Redenumire sau să apăsați pe **F2**.
-   **Rotation**: rotește vederea. De exemplu, o vizualizare izometrică va necesita o rotație de 60 de grade (vezi și parametrul Direction below)
-   **Scale**: stabilește scala de vizualizare.
-   **X**: setează poziția orizontală a vederii pe pagină în milimetri.
-   **Y**: stabilește poziția verticală a vederii pe pagină în milimetri. Rețineți că coordonatele (0,0) sunt localizate în partea din stânga sus a paginii, deci cu cât este mai mare numărul, cu atât mai mic va fi vizualizarea pe pagină.
-   **Direction**: schimbă direcția de vizualizare. Acesta este setat de valorile xyz care definesc un vector normal pentru pagină. Vederea de sus va fi (0,0,1), iar izometria va fi (1,1,1). Valorile pot fi negative.
-   **Afișează liniile ascunse**: comută sau dezactivează vizibilitatea liniilor ascunse selectând \'\' Adevărat \'\' sau \'\' Fals \'\'.
-   **Afișează liniile netede**: comută sau dezactivează vizibilitatea liniilor netede prin selectarea*True*sau*False*. Liniile netede sunt de asemenea numite margini de tangență. Aceste margini indică schimbări de suprafață între suprafețele tangente.

### Expertul vizualizării desenului {#expertul_vizualizării_desenului}

Pentru a genera automat o foaie de desen cu vizualizări standard, utilizați [Automatic drawing Macro](Macro_Automatic_drawing.md). 

### Other

If you are looking for persective-orthographic toggling in 3D view check [Std PerspectiveCamera](Std_PerspectiveCamera.md) and [Std OrthographicCamera](Std_OrthographicCamera.md)


{{docnav
|[New A3 landscape drawing](Drawing_Landscape_A3.md)
|[Annotation](Drawing_Annotation.md)
|[Drawing Workbench](Drawing_Workbench.md)
|IconL=Drawing_Landscape_A3.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Annotation.png
}}


{{Drawing Tools navi

}} 
