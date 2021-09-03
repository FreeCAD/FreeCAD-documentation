 {{TutorialInfo/ro
|Topic= Importaţi text şi forme geometrice create cu InkScape
|Nivel= Începător
|Timp= 30 minute
|Autor=r-frank
|FCVersion=0.16.6704
|Fişiere=
}}

## Introducere

Acest îndrumător a fost destinat să vă arate cum să importaţi text sau obiecte geometrice create cu InkScape în FreeCAD, prin intermediul formatului SVG.
În acest scop, s-au utilizat Inkscape 0.91 şi FreeCAD 0.16.6704 sub Windows.

## Sugestii pentru importul din InkScape {#sugestii_pentru_importul_din_inkscape}

-   the svg-import in FreeCAD cannot handle a svg file with a resolution of more than 45 dpi, so check the settings in inkscape
-   when importing path objects which show up in the 3D view in FreeCAD not very smooth it may be a matter of the FreeCAD-settings for the shape view.
    -   in FreeCAD choose ** Edit** → ** Preferences** → ** Part Design** → ** Shape View**
    -   as for \"Tesselation\", the \"Maximum deviation depending on the model bounding box\" the default value is \"0,5 %\"
    -   setting this to a lower value will increase smoothness of the model in the 3D view (and use more PC performance)
    -   don\'t use values lower than \"0,01 %\", this will most likely crash FreeCAD
    -   in that case deleting \"system.cfg\" and \"user.cfg\" in your FreeCAD-user-directory will solve this problem


<div class="mw-translate-fuzzy">

## Importul unul text din InkScape {#importul_unul_text_din_inkscape}

-   după inserarea unui text in InkScape (şi, poate, aplicarea unor efecte precum mlădierea sau de alt tip) asiguraţi-vă căː
    -   select your text and choose ** Path** → ** Object to path**
    -   ungroup your objects
    -   save as \"Plain SVG (\*.svg)\" file format
-   open the file in FreeCAD, choosing the option \"SVG as geometry (importSVG)\"
-   a path object for each letter/number/sign will be created in the tree view
-   use [draft upgrade](Draft_Upgrade.md) on each path object to create faces
-   use pad or extrude on the faces to get solids
-   you can fuse your objects or use compound on them depending on your intended further work


</div>

## Importul de forme geometrice din InkScape {#importul_de_forme_geometrice_din_inkscape}

Since inkscape and FreeCAD seem to have different approaches on how to apply dimensions on svg-object, the recommended workflow seems to be:

-   ungroup all objects in inkscape
-   select all objects in inkscape
-   apply a stroke style with a width of 0 mm (yes, that is zero millimeter) to all objects
-   save as \"Inkscape SVG (\*.svg)\" or \"Plain SVG (\*.svg)\" file format
-   open the file in FreeCAD, choosing the option \"SVG as geometry (importSVG)\"
-   the dimensions of the objects in inkscape and in FreeCAD should now be identical

## Credite

Le mulţumesc utilizatorilor \"freecad-heini-1\" şi \"herbk\" pentru testare şi pentru furnizarea unor impresii şi informaţii de un real folos.




