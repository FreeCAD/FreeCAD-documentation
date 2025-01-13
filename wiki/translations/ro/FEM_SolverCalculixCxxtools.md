---
 GuiCommand:
   Name: FEM SolverCalculixCxxtools
   MenuLocation: Solve , Solver CalculiX Standard
   Workbenches: FEM Workbench
   Shortcut: 
   SeeAlso: FEM_tutorial
---

# FEM SolverCalculixCxxtools/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

CalculiXccxTools permit utilizarea calculatorului [CalculiX](http://dhondt.de/). Puteți să-l utilizați

1.  setați parametrii de analiză
2.  selectați directorul de lucru
3.  executați Solverul CalculiX.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

Acest obiect este creat automat cu crearea cotainerului **<img src="images/_FEM_Analysis.svg_" width= 24px> [Container de analiză](FEM_Analysis.md)
**. Altfel utilizați **Solve** → **Solver CalculiX Standard** sau apăsați **S** apoi tastele **X**

1.  Opțional setați proprietățile de date ale obiectului **<img src="images/_FEM_SolverCalculixCxxtools.svg_" width= 24px> CalculiXccxTools** obiect
2.  Faceți dublu clic pe **<img src="images/_FEM_SolverCalculixCxxtools.svg" width=24px> CalculiXccxTools** obiect
3.  Selectați tipul analizei
4.  Faceți clic pe **Write .inp file**
5.  Faceți clic pe **Run CalculiX**


</div>



## Opţiuni


<div class="mw-translate-fuzzy">

Folosind {{KEY | Edit .inp file}}, puteți afișa și edita manual fișierul de intrare CalculiX înainte de a rula analiza. În acest caz ar putea fi util să utilizați parametrul \"Split Input Writer = true\".


</div>



## Proprietăți


<div class="mw-translate-fuzzy">

Default values can be set in the menu **Edit** → **Preferences** → **FEM** → **CalculiX**


</div>


<div class="mw-translate-fuzzy">

-    **Analysis Type**:

    -   static
    -   frecvent
    -   termomech - pentru sarcini mecanice și termice


</div>

-    **Beam Reduced Integration**\- <small>(v1.0)</small> :

    -   true - uses beam elements with reduced integration (B31R or B32R), required when pipe beam section is used, can also make it possible to obtain [accurate results with plasticity](https://forum.freecad.org/viewtopic.php?t=61233)
    -   false - uses regular (fully-integrated) beam elements


<div class="mw-translate-fuzzy">

-    **Beam Shell Result Output 3D**: rețineți că CalculiX extinde intern elementele 1D și 2D în elemente 3D pentru a realiza analiza FE

    -   false - rezultatele elementelor 1D și 2D vor fi medii la nodurile rețelei originale 1D sau 2D (adică fascicolul curbat curbat va arăta 0 solicitări nodale datorită mediei)
    -   true - rețeaua rezultată va conține elemente 1D și 2D extins la elementele 3D


</div>

-    **Buckling Accuracy**\- <small>(v1.1)</small> : defines the accuracy of buckling eigenvalue evaluation. In most cases it can be left with the default value (0.01) but sometimes it might be necessary to lower it (e.g. to 0.0001) to capture the first eigenvalue.


<div class="mw-translate-fuzzy">

-    **Eigenmode High Limit**: Valorile proprii deasupra acestei limite nu vor fi calculate


</div>

-    **Eigenmode Low Limit**: Valorile proprii mai jos de aceste limite nu vor fi calculate

-    **Eigenmodes Count**: numărul de moduri proprii minime care urmează a fi calculate


<div class="mw-translate-fuzzy">

-    **Geometric Nonlinearity**:

    -   linear - o analiză liniară va fi efectuată dacă modelul nu conține material neliniar
    -   neliniare - se va efectua o analiză neliniară


</div>


<div class="mw-translate-fuzzy">

-    **Iterations Control parameter Cutb**: definește a doua linie de parametri avansați de iterație sub cartela \* CONTROLS, utilizată atunci când \"Iterations Control Parameter Time Use\" este adevărată


</div>


<div class="mw-translate-fuzzy">

-    **Iterations Control Parameter Iter**: definește prima linie de parametri avansați de iterație sub cartela \* CONTROLS, folosită când \"Iterations Control Time Parameter Use\" este adevărată


</div>


<div class="mw-translate-fuzzy">

-    **Iterations Control Parameter Time Use**-   true - activează \"Iterations Control Parameter Cutb\" și \"Iterations Control Parameter Iter\"


</div>


<div class="mw-translate-fuzzy">

-    **Iterations Thermo Mech Maximum**: numărul maxim de creșteri în analizele termomecanice după care lucrarea va fi oprită.


</div>

-    **Iterations User Defined Incrementations**:

    -   true - controlul incrementării automate va fi oprit prin parametrul DIRECT
    -   false - controlul incrementării va fi automat


<div class="mw-translate-fuzzy">

-    **Iterations User Defined Time Step Length**:

    -   true - activează parametrii \"Time End\" și \"Time Initial Step\"


</div>


<div class="mw-translate-fuzzy">

-    **Material Nonlinearity**:

    -   în analiză vor fi incluse proprietăți liniare numai liniare
    -   vor fi utilizate proprietăți neliniare - materiale neliniare **<img src="images/FEM_MaterialMechanicalNonlinear.png" width=24px> '''[Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md)'''** object


</div>


<div class="mw-translate-fuzzy">


{{PropertyData | Matrix Solver Type}}

: tipul rezolverului pentru rezolvarea sistemului de ecuații în analiza FE. Este posibil să afecteze semnificativ viteza de calcul și cerințele de memorie. Capacitatea depinde de modelul dvs. FE și de hardware-ul disponibil

-   -   implicit - selectează automat rezolvatorul de matrice în funcție de solverii disponibili (probabil vor fi Spooles)
    -   spooles - Solver direct cu suportul mai multor CPU-uri. Numărul de procesoare trebuie să fie setat în {{KEY | Edit}} → {{KEY | Preferences}} → {{KEY | FEM}} → {{KEY | CalculiX}} Solver implicit → Numărul CPU-urilor de utilizat)
    -   iterativescaling - solver iterativ cu cele mai mici cerințe de memorie, potrivit dacă modelul conține mai mult elemente 3D
    -   iterativecholesky - iterativ solver cu precondiționare cu și cu cerințe de memorie redusă, potrivite dacă modelul conține mai mult elemente 3D


</div>

-    **Model Space**\- <small>(v1.0)</small> : switches between 3D and 2D analyses, the latter require surface geometry on the XY plane (on the right of the Y axis in the axisymmetric case) with [thickness definition](FEM_ElementGeometry2D.md) (value ignored in the axisymmetric case) and proper boundary conditions ([displacement boundary condition](FEM_ConstraintDisplacement.md) with degrees of freedom X and Y has to be used instead of [fixed boundary condition](FEM_ConstraintFixed.md)) and in-plane loads applied to edges

    -   3D - three-dimensional solid/shell/beam elements are used
    -   plane stress - plane stress 2D solid elements are used
    -   plane strain - plane strain 2D solid elements are used
    -   axisymmetric - axisymmetric 2D solid elements are used

-    **Output Frequency**\- <small>(v1.0)</small> : defines the frequency of results writing in increments (the default setting of 1 means that the results are written every increment, setting 2 would save the results every 2 increments and so on), particularly useful for nonlinear and transient simulations, helps reduce the clutter in the tree since currently a pair of results objects (CCX_Results and Pipeline_CCX_Results) is created for each results frame

-    **Split Input Writer**:

    -   false - scrie intrări întregi într-un fișier \* .inp pentru a fi utilizat de CalculiX solver
    -   adevărat - split solver intrări în mai multe fișiere \* .inp, care pot clarifica editare manuală


<div class="mw-translate-fuzzy">

-    **Thermo Mechanical Steady State**:

    -   adevărată - analiză termo-mecanică la starea de echilibru
    -   fals - analiză termo-mecanică tranzitorie


</div>

-    **Thermo Mech Type**\- <small>(v1.0)</small> :

    -   coupled - coupled thermo-mechanical analysis
    -   uncoupled - uncoupled thermo-mechanical analysis
    -   pure heat transfer - purely thermal analysis (*\*HEAT TRANSFER*)


<div class="mw-translate-fuzzy">

-    **Time End**: perioada de timp a pasului, folosită atunci când parametrul \"Iterații creșteri definite de utilizator\" sau \"Iterații definit de utilizator\" este adevărat


</div>


<div class="mw-translate-fuzzy">

-    **Time Initial Step**: incrementarea timpului inițial a pasului, folosită atunci când parametrul \"Iterații creșteri definite de utilizator\" sau \"Iterații de lungime a pasului definit de utilizator\" este adevărat


</div>

-    **Time Maximum Step**\- <small>(v1.0)</small> : maximum time increment of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Time Minimum Step**\- <small>(v1.0)</small> : minimum time increment of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Working Dir**: calea către directorul de lucru care va fi folosit pentru fișierele de analiză CalculiX.



## Limite

When running a CalculiX, you might end up with **error 4294977295**. This means you don\'t have enough RAM space. You have then 2 options:

1.  reduce the number of mesh nodes, preferably by omitting geometry that is not absolutely necessary for your analysis
2.  buy more RAM for your PC



## Notă

Documentația originală CalculiX poate fi găsită la <http://dhondt.de/> in the \"ccx\" paragraph.



## Scrip-Programare 





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/ro
