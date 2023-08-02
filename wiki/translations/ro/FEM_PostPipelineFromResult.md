# FEM PostPipelineFromResult/ro
---
- GuiCommand:   Name: FEM PostPipelineFromResult   MenuLocation:  Results -> post pipeline from result   ---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Conducta este un obiect rezultat, care creează o nouă reprezentare grafică a rezultatelor analizei FEM pe partea analizată. Acesta adaugă scara de culori și mai multe opțiuni de afișare.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

-   Aveți nevoie de un obiect rezultat valid în {{KEY | [ <img src=images/_FEM_Analysis.svg  style="width:24px"> [ Container de analiză](FEM_Analysis_.md)}}, cum ar fi {{KEY | CalculiX_static_results}}.
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

If you see no model in the graphical area, go to and enable **Edit → Preferences → Display → 3D View → Rendering → Backlight color**.

If you use a [SI](https://en.wikipedia.org/wiki/International_System_of_Units)-derived FreeCAD [unit system](Preferences_Editor#Units.md), the values in the output scale are based on SI units as well. This means the displacement is in meter, the stress is in Pascal and the temperature is in Kelvin.

## Properties

### Dialog box 

This pipeline dialog box has the following settings:

-   **Mode**: How to draw the results. The possible modes are
    -   **Outline**: The outline of the result mesh. In fact is displays no results but only the borders of the mesh.
    -   **Nodes**: The result mesh nodes.
    -   **Surface**: This is the default and displays the surface of the result mesh.
    -   **Surface with Edges**: Like **Surface** but with the mesh outline edges and the surface mesh node connection lines.
-   **Field**: Which result property to draw.
-   **Vector**: Is only active if the **Field** is a vector. You can select whether to display the vector *Magnitude* or its X, Y, Z components.

### Scale

If you double-click on the scale, you get this settings dialog box:

![](images/SIMTUT_05.PNG )

and you can modify these properties:

-   **Gradient**: You can select reversed order of the default color gradient, *Red-White-Blue*, *Black-White* or *White-Black*.
-   **Style**: The default option *Flow* uses the full color gradient range. The option *Zero* uses only the color gradient range starting form the color that would display the mean value to the maximum.
-   **Visibility**: The option *Out grayed* will color all mesh nodes whose values are outside the set minimum/maximum range in gray. The option *Out transparent* will make these mesh nodes transparent.
-   **Parameter range**: Minimum and maximum values are filled-in automatically. You can modify them, however make sure you know what you are doing. You can also change the number of displayed decimal places and the number of labels distributed over the parameter range.

### Property Editor 

In the [property editor](Property_editor.md) you can set in the *View* tab the settings from the dialog box. In the *Data* tab you can additionally set this:

-    **Mode**: How the filters used in the pipeline will be treated. These modes are possible:

    -   **Serial**: In this mode every filter takes the previous filter as input. The order is hereby the order of creation. The first created filter takes the pipeline as input. Its **Input** property is therefore empty.
    -   **Parallel**: In this mode all filters take the pipeline as input.
    -   **Custom**: <small>(v0.20)</small>  This is the default and keeps the input of the filters as they are. Therefore it allows to have e.g. two filters that take the pipeline as input, and a third filter that takes one of the two filters as input.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/ro
