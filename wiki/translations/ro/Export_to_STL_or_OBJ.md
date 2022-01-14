# Export to STL or OBJ/ro
<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic= Export to STL or OBJ
|Level= Beginner
|Time= 20 minutes
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Introducere

În acest tutorial vom discuta cum să exportați fișiere STL / OBJ din FreeCAD. Din moment ce formatul STL / OBJ-ul este compus din ochiuri este adimensional, FreeCAD va presupune că unitățile utilizate în model sunt în mm. Dacă nu este cazul, trebuie să vă scalați modelul.


</div>

## Sample part 


<div class="mw-translate-fuzzy">

## Model de Piesă 

Puteți utiliza propriul fișier FreeCAD, dar puteți crea, de asemenea, un fișier de test rapid de către

-   Creați un nou document
-   Comutați pe Atelierul Part
-   Insert a cube by clicking on <img alt="" src=images/Part_Box.png  style="width:32px;">
-   Insert a cone by clicking on <img alt="" src=images/Part_Cone.png  style="width:32px;">
-   Select all two objects in the tree view
-   Apply a fusion by clicking on <img alt="" src=images/Part_Fuse.png  style="width:32px;">
-   Salvați fișierul


</div>

## Export Method 1: Using \"File → Export\" 


<div class="mw-translate-fuzzy">

## metoda 1 de Export: folosirea căii \"File \> Export\" 

-   Comutați pe Atelierul Mesh workbench sau workbench complet
-   Choose ** Edit** → ** Preferences** → ** Import-Export** → ** Mesh Formats** from the top menu
-   Here you can specify the maximum mesh deviation (0,1 mm is default) which controls how \"fine\" your mesh will get
-   Close dialogue with ** OK**
-   Select the solid to be exported in the tree view
-   Choose ** File** → ** Export...** and set file type to for example \"STL mesh (\*.stl \*.ast)\"
-   Introduceți numele fișierului dvs. și nu uitați extensia, alegeți** Save**


</div>

## Export Method 2: Using the Mesh Workbench in FreeCAD 


<div class="mw-translate-fuzzy">

## Metoda 2 de Export: folosirea atelierului Plase în FreeCAD 

-   Comutați pe Atelierul Mesh
-   Selectați în vederea arborescentă solidul care va fi transformat în plasă
-   Choose ** Meshes** → **<img src="images/Mesh_Mesh_from_Shape.svg" width=32px> Create Mesh from shape...** from the top menu
-   Select one of the three available meshers and specify the available options, for more info refer to [this page (Mesh from Shape)](Mesh_MeshFromShape.md)
-   Choose ** OK** and the mesh object will be created in the tree view (with green mesh icon)
-   Select the mesh object in the tree view and right click on mesh object in the tree view
-   Choose **<img src="images/Mesh_ExportMesh.png" width=32px> Export mesh** to export mesh
-   You will be prompted to choose file name (default is the name of the mesh object) and the file type (default is \"Binary STL (\*.stl)\")
-   Selectați ** Save** și ați terminat


</div>

## Which Method to choose ? 


<div class="mw-translate-fuzzy">

## Care metodă alegem? 

-   Se preferă metoda 2. Mai ales atunci când aveți mai multe corpuri pentru a converti de la Tools din Atelierul Mesh, cum ar fi fuzionarea Plaselor înainte de export.


</div>

## Links


<div class="mw-translate-fuzzy">

## Links 

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)


</div>




[<img src="images/Property.png" style="width:16px"> File\_Formats](Category_File_Formats.md)

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Export to STL or OBJ/ro
