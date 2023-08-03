# Basic modeling tutorial/pt
---
 TutorialInfo:t
   Topic :  Introdução à modelação
   Level :  Iniciante
   Time :  15 minutos
   Author : 
   FCVersion : 
   Files: 
}}

## Introduction


<div class="mw-translate-fuzzy">

Este Tutorial de Modelagem Básica mostrar-te-á como modelar um ângulo de ferro. Uma coisa que deverias saber é que FreeCAD é modular segundo o desenho, e como muitos outros programas de CAD, sempre há mais de um modo de fazer as coisas. Exploraremos dois métodos aqui.


</div>

This tutorial was written with version 0.15 of FreeCAD.

## Dantes de começar 

Recorda que FreeCAD ainda está num estado inicial de desenvolvimento, de modo que possivelmente não sejas tão produtivo como com outras aplicações de CAD, e encontrarás alguns erros, ou experimentes alguns pendures da aplicação. FreeCAD agora dispõe da opção de realizar cópias de respaldo. O numero de arquivos de respaldo pode-se especificar menu do diálogo de Preferências. Não duvides em permitir 2 ou 3 arquivos de respaldo até que conheças bem como trabalhar com FreeCAD.

Save your work often, from time to time save your work under a different name, so you have a \"safe\" copy to fall back to, and be prepared to the possibility that some commands might not give you the expected results.

## Modeling Techniques Intro 

The first  technique of solid modeling is Constructive Solid Geometry . There is also a detailed explanation  of Constructive_solid_geometry on the wiki. You work with primitive shapes like cubes, cylinders, spheres and cones to construct your geometry by combining them, subtracting one shape from the other, or intersecting them. These tools are part of the Part Workbench. You can also apply transformations on shapes, like applying rounds or chamfers on edges. These tools are also in the Part Workbench.

Then there are more advanced tools. You start by drawing a 2D profile which you\'ll either extrude or revolve.

So let\'s start by trying to do some iron feet for a table with these 2 methods.

## 1st Method - By Constructive Solid Geometry 

1.  Start with the Part Workbench !.
2.  If you haven\'t opened a new FreeCAD document , from the pull-down menu click **File , New** or click the !{width="32"} **Create a new empty document** icon.
3.  Click on the !{width="32"} Box button to create a box
4.  Change its dimensions by selecting it either in the 3D space, or by clicking it in the Project tab to the left, then
5.  Click on the Data tab at the bottom, and change values for Length, Width and Height to 50mm, 50 and 750 ** **Note**: *back when these captures were taken, the properties were ordered differently, with Height being first*.
6.  The box now fills most of the 3D view. Click on !{width="32"} Fit All to fit the view to the newly created box.
7.  Create a second box the same way, but with values L=40, W=40 and H=750mm. By default this box will be superimposed on the first one. **
8.  You\'ll now subtract the second box from the first. Select the first shape first , then the second one , the selection order is important!  to either CAD or Blender selection.)
9.  On the Part Workbench toolbar, click on the !{width="32"} Cut tool.

!Fig. 1.1 The first box

!Fig. 1.2 The second box on top of the first one, ready to be subtracted

!Fig. 1.3 After the subtraction

You now have your first iron angle **. You\'ll notice that, in the Project tab on the left, both boxes have been replaced by a \"Cut\" object. Actually, they\'re not disappeared, but rather grouped under the Cut object. Click on the **+** in front of it, and you\'ll see that both boxes are still there, but greyed out **. If you click on either of them and hit the **Space bar**, it will show up. The space bar toggles visibility of selected objects. **

Don\'t want the angle oriented that way? You just need to change the placement of the Box001 shape. Select it, unhide it, and in the Data tab, click on the **+** in front of Placement, then expand the Position parameter, and change its X and Y coordinates. Hit **Enter**, hide the Box001 shape again, and your angle orientation is now different. ** You can even change either of your shapes dimensions, and the Cut object will be updated.

!Fig. 1.4 The cut operation retains its original objects ")

!Fig. 1.5 You can still make the original boxes visible

By the way, we can add rounds to the angle so it is more realistic, using the !{width="32"} Fillet tool. **

!Fig. 1.6 The filleted edges

## 2nd Method - By extruding a profile 

This method requires that you start by drawing a 2D profile. You need to activate the Draft workbench !.

-   If you haven\'t opened a new FreeCAD document , from the pull-down menu click File , New or click the !{width="32"} **Create a new empty document** icon.

### Setting the working plane 

First we need to define on which working plane to draft our profile.

1.  Locate the toolbar displayed below. Depending on your Draft preferences, it may be below the main toolbar, to the left or to the right.

    :   !
2.  Press the **Auto** button .
3.  Depending on your Draft preferences, this expands a **Select Plane** dialog in the Tasks side panel, or a horizontal toolbar labeled \"active command: **Select Plane**\". See the Note on Draft Working Plane Button for screen captures showing the two expanded modes.
4.  We will leave the *Offset* field at a value of zero.
5.  Press the **XY** button to set the working plane to XY. This closes the Tasks panel or the expanded buttons. The \"Auto\" button will now be relabeled as \"Top\" to show it is the active plane.

### Drafting the profile 

1.  Select the !{width="32"} DWire  tool.
2.  Check the \"Relative\" and \"Filled\" boxes.
3.  Rather than drawing the shape in the 3D view, we\'ll enter coordinates in the *Global X*, *Global Y* and *Global Z* input fields. The process is the following:
    1.  Click in the *Global X* input field;
    2.  Enter a value as listed in the bullet list below and press **TAB** to go to the *Global Y* input field;
    3.  Enter the *Global Y* value and press **TAB** to go to the *Global Z* input field;
    4.  In the *Global Z* field, leave the zero value and press **ENTER** to validate the coordinates for the point;
    5.  Repeat for the next 5 points.
        -   **Coordinates** 
        -   1st point: 0, 0, 0
        -   2nd point: 50, 0, 0
        -   3rd point: 0,10, 0
        -   4th point: -40, 0, 0 **Note:** *in FreeCAD 0.16, there is a bug that removes the previous point when entering the minus sign in the input field. A workaround is to enter a positive value, then place the cursor before the number and add the minus sign. *
        -   5th point: 0, 40, 0
        -   6th point: -10, 0, 0
4.  Press the **Close** button to close the profile. You should now have this profile, titled **DWire** in the Model tab:

!Fig. 1.7 The base DWire

Hit the **0**  key on the numerical keypad to set the view to axonometric.

### Extruding the profile 

Activate the !{width="32"} Part Workbench either from the workbench selector, or from the **Std View Menu   View , Workbench , Part**{: mediawiki} menu.

Click on the **Image:Part_Extrude.svg   32px Part_Extrude**{: mediawiki} tool.

On the Tasks tab on the left, select the **Wire** object. Then enter the desired length, say 750mm. Leave the direction at Z = 1. Press **OK**. You should now have an **Extrude** object in the Model tab **

!Fig. 1.8 The extruded object

This method has a minor caveat compared to the other one: to edit the shape, you need to edit the Wire, it\'s not as easy to do as the previous method.

And there are a few other ways to do it too! I hope these two examples get you started. You\'ll sure hit some snags along the way , but don\'t hesitate to ask questions on the FreeCAD forum!

### Note on Draft Working Plane Button 

The label on your button may be different, depending on your version and also on what you were doing beforehand. The button label could read: \"Top\", \"Front\", \"Side\", \"None\" or a Vector representation such as d. It can also be blank. For example:

!Select Plane None

!Select Plane Top

!Select Plane View  After pressing the button, the options will be expanded into either of the following configurations.

!**Select Plane** parameters as shown in Tasks panel mode.

!**Select Plane** parameters as shown in Toolbar mode. 

The above instructions will work, no matter what label your button has.


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Basic modeling tutorial/pt
