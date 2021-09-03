---
- GuiCommand:   Name:FEM PostPipelineFromResult   MenuLocation: Results → post pipeline from result   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial|FEM tutorial](FEM_Workbench___FEM]].md)---


</div>

**\* You need a valid result object in the **<img src="images/FEM_Analysis.svg" width=24px> [Analysis container](FEM_Analysis.md)
**, such as **CalculiX static results**.**

## Description


<div class="mw-translate-fuzzy">

## Descriere

Conducta este un obiect rezultat, care creează o nouă reprezentare grafică a rezultatelor analizei FEM pe partea analizată. Acesta adaugă scara de culori și mai multe opțiuni de afișare.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

-   Aveți nevoie de un obiect rezultat valid în {{KEY | [ 24px](FEM_Analysis.png .md) [ Container de analiză](FEM_Analysis_.md)}}, cum ar fi {{KEY | CalculiX_static_results}}.
-   Selectați obiectul rezultat
-   Faceți clic pe butonul ![ 24px](images/_FEM_PostPipelineFromResult.png ) sau faceți clic pe meniul {{KEY | Results}} și pe elementul {{KEY | Post Pipeline from results}}. Un nou obiect numit \"Pipeline\" va fi adăugat la documentul dvs.; notați dacă vor apărea în afara containerului Analiză.
-   Faceți dublu clic pe noul obiect Pipeline din arborele Model și selectați tipul de proprietăți de afișat. Setările tipice sunt: ​​Mod: Selectați {{KEY | Surface}}, Câmp: De ex. {{KEY | Von Mises stres}} ![](images/_Pipeline.PNG )
    -   Mod: Cum să desenezi rezultatele
    -   Câmp: Care proprietate rezultă să desenezi
    -   Vector: Dacă o proprietate este un vector, puteți restrânge datele pe o axă (X, Y, Z) sau selectați Magnitude pentru a utiliza valoarea vectorului.
-   Dacă nu vedeți niciun model în zona grafică, mergeți la {{KEY | Edit}} {{KEY | Preferences}}, selectați categoria {{KEY | Display}} și bifați o casetă de selectare **Enable backlight color**
-   Dacă faceți dublu clic pe scală, puteți modifica proprietățile afișajului.

![](images/_SIMTUT_05.PNG )

-   -   Gradient: Puteți selecta ordinea inversă a gradientului de culoare implicit sau alb-negru sau alb-negru.
    -   Intervalul parametrilor: Valorile minime și maxime sunt completate automat atunci când selectați o proprietate pentru a evalua pe obiectul {{KEY | Pipeline}}; le puteți modifica, însă asigurați-vă că știți ce faceți. De asemenea, puteți modifica numărul de etichete afișate și numărul de zecimale afișate.


</div>

## Limite

Încă o dată, rețineți că reprezentarea conductelor rezultate (denumită VTK) pe partea afișată este diferită de rezultatele gradientului de culoare care sunt vizibile când terminați soluția. Valorile din scara de gradient nu pot fi aplicate obiectului rezultat al soluției. Detalii găsiți la <https://www.vtk.org/Wiki/VTK/Tutorials/New_Pipeline>





{{FEM Tools navi

}}  
