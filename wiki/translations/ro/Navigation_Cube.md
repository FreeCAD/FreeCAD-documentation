# Navigation Cube/ro
{{TOCright}}

## Introduction

The **Navigation Cube** gives visual information about the camera orientation in the current [3D view](3D_view.md) and can be used to change it. By default it is visible and resides in the upper right corner of the view.

The Navigation Cube was updated in FreeCAD version 0.20 and the rest of this page describes that version. In FreeCAD version 0.19 the main behavior is the same but some features are missing.

![](images/Navigation_Cube_Example.png )


<div class="mw-translate-fuzzy">

Cubul de navigarea este compus din următoarele piese:

-   Săgețile Direcționale
-   Cubul de Navigație principal
-   Meniul Mini-cubului


</div>

All parts, except the axis indicators, can be clicked.

## Usage

### Main cube 

The main cube has 26 faces: 6 square main faces, 12 rectangular edge faces (<small>(v0.20)</small> ), and 8 triangular corner faces. Clicking any of them will reorient the camera so that its direction is perpendicular to the selected face.


<div class="mw-translate-fuzzy">

## Săgețile Direcționale 


</div>


<div class="mw-translate-fuzzy">

Există șase săgeți direcționale: patru săgeți triunghiulare, unul în sus, în jos, la stânga și la dreapta; și două săgeți de rotație, una pe fiecare parte a săgeților de mai sus.


</div>

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube will rotate the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.


<div class="mw-translate-fuzzy">

## Meniul Mini-cub 


</div>


<div class="mw-translate-fuzzy">

În colțul din dreapta jos al cubului de navigație este un mic cub. Dacă faceți clic pe acest cub va apărea un meniu pe care îl puteți utiliza pentru a schimba tipul de vizualizare (Ortografic, Perspectivă, Isometric) și pentru a face o \"Zoom pentru a se potrivi\".


</div>

## Customization

### Move the Navigation Cube 


<div class="mw-translate-fuzzy">

## Deplasarea afișajului cubului de navigație 

Puteți mutați întreaga structură de control a cubului de navigație într-o altă locație din afișajul 3D, apăsând mouse-ul oriunde în cubul principal de navigare și trasând. De la această scriere (v 0.18), structura nu va începe să se miște până când indicatorul mouse-ului nu sa deplasat peste marginea cubului principal de navigație.


</div>

### Preferences

The Navigation Cube is controlled by several preferences: **Edit → Preferences... → Display → Navigation → Navigation cube**. See [Preferences Editor](Preferences_Editor#Navigation.md).

### Advanced options 

The [CubeMenu](Interface_Customization#CubeMenu.md) external workbench provides easier access to several more advanced customization options.


<div class="mw-translate-fuzzy">


{{docnav|Mouse Model|Document structure}}


</div>




[<img src="images/Property.png" style="width:16px"> User Documentation](Category_User_Documentation.md)

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/ro
