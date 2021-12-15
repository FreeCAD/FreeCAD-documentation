# Aeroplane/zh-tw
<div class="mw-translate-fuzzy">


{{TutorialInfo/zh-tw
|Topic=Part Workbench
|Level=Beginner
|Time=10 minutes
|Author=
|FCVersion=
|Files=
}}


</div>

## First Steps 


<div class="mw-translate-fuzzy">

## First Steps 

We will be working in the [Part Workbench](Part_Workbench.md) - select it from menus via View-\>Workbench-\>Part or from the Workbench selector.


</div>


<div class="mw-translate-fuzzy">

-   Create a new empty document.
-   Switch to Axonometric View.
-   Toggle axis cross ON (via View Menu).
-   Ensure you have the Combo View showing (via View-\>Views).


</div>


<div class="mw-translate-fuzzy">

-   Create a cylinder by clicking on the <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> [Cylinder](Part_Cylinder.md) button.
-   Select it by clicking on Cylinder in the Project viewer.
-   Click on the Data tab at the bottom of the Project viewer.


</div>

Change the Height to 20mm. Leave the Radius at 2mm.


<div class="mw-translate-fuzzy">

Click on [Placement](Tasks_Placement.md) (note the little \[+\]) and a button with three dots will appear. Click on it. (You can also select: Menu-\>Edit-\>Placement.) The Tasks viewer appears.


</div>

<img alt="" src=images/HTCaeroplane01.png  style="width:300px;">


<div class="mw-translate-fuzzy">

If you are unfamiliar with the XYZ axes then have a play with the numbers in the Translation box. When finished playing click on the Reset button.


</div>

## Second Steps 

<img alt="" src=images/HTCaeroplane02.png  style="width:400px;">


<div class="mw-translate-fuzzy">

We are now going to rotate the cylinder so that is lying along the X axis. To do this it needs to be rotated around the Y axis. The Rotation box should say \'Rotation axis with angle\' so change the Axis to Y and increment the Angle until it reaches 90. Click on OK.


</div>

I like to play with rotating the view at this point (and often!) so by all means do so. You should find the \'seam\' of the cylinder on the underside.

<img alt="" src=images/HTCaeroplane03.png  style="width:400px;">


<div class="mw-translate-fuzzy">

We are now going to add and modify a box so click on the <img alt="" src=images/Part_Box.png  style="width:32px;"> [Box](Part_Box.md) button. Select it by clicking on Box in the Project viewer. Change the Height to 1mm, the Length to 5mm and the Width to 20mm.


</div>


<div class="mw-translate-fuzzy">

Click on [Placement and the three dots](Tasks_Placement.md) to get the Tasks viewer. Using the Translation box enter Y: -10 and Z: -1. Click on OK


</div>


<div class="mw-translate-fuzzy">

We are now going to merge these two shapes together with a Boolean Operation. Click on the <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolean](Part_Boolean.md) button and the Tasks viewer will display the Boolean Operation selector.


</div>


<div class="mw-translate-fuzzy">

Make sure Union is selected, and that the Cylinder and the Box are each ticked once in the two shape lists. Click on Apply. Click on Close. You now have a single object called Fusion.


</div>


<div class="mw-translate-fuzzy">



</div>

Let\'s add one more box to finish off our model. Create a Box, Select it and change its Height to 5mm, Length to 3mm and Width to 1mm. Change its Placement by Y: -0.5.


<div class="mw-translate-fuzzy">

We now need to join our Fusion to Box001 so we\'ll do it the quick way. Click on Fusion in the Project viewer and CTRL-click on Box001. This selects both parts together. Now click on the <img alt="" src=images/Part_Fuse.png  style="width:32px;"> [Union](Part_Union.md) button to get Fusion001.


</div>


<div class="mw-translate-fuzzy">

You should now have a simple aeroplane model. Right-click on Fusion001 and Rename it \'Aeroplane\'.


</div>

<img alt="" src=images/HTCaeroplane04.png  style="width:500px;">

I think the wings need to be moved forward a bit but if I select Aeroplane and try changing its Placement X Translation the whole thing moves. I only want to move the wings so cancel the Placement.

Expand Aeroplane (click on the **[+]** beside it) and expand Fusion.

Click on Box and get its [Placement into Tasks](Placement.md). Notice it already has Y: -10 and Z: -1 in the Translation. Change the X translation to 3 and click on **Apply**. That\'s better. Click **OK**.




## Rotations

Click on Aeroplane and get its [Placement into Tasks](Placement.md). In the Rotation section change where it says \'Rotation axis with angle\' to \'Euler angles\' because they\'re a lot easier to work with.

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Yaw** is the rotation about the **Z axis**, that is to say a rotation from left to right. (The yaw angle is the **Psi ψ**).  ![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pitch** is rotation about the **Y axis**, that is to say nose-up and nose-down. (The Pitch angle is the **Phi φ**).  ![](images/Tache_Placement_Roulis_fr_Mini.gif )**Roll** is rotation about the **X axis**, that is to say wing up and down. (The Roll angle is the **Thêta θ**). 

However, even here there are some important things to remember:

-   Positive Rotations are clockwise when viewed from the Origin outwards along a positive axis. Or to put it another way: Positive Rotations are anticlockwise when viewed from a positive axis towards the Origin.

-   Although the three labels are Yaw, Pitch and Roll that\'s not really what they are. Yaw, Pitch and Roll are references to the *body coordinates* of an object in 3D space. The labels should be Heading, Elevation and Bank or even Azimuth, Inclination and Bank because they actually refer to the *space coordinates* of the 3D system. These are the **Tait-Bryan angles**. If you want more information then try [Euler Angles](http://en.wikipedia.org/wiki/Euler_angles#Tait-Bryan_angles).

-   With the Aeroplane in its present position simple rules apply. Yaw is rotation around the Z axis, ie left and right. Pitch is rotation around the Y axis, ie nose up and down. Roll is rotation around the X axis, ie wings up and down. That\'s fine to start with but it\'s not going to be true later!

Have a play with the three YPR numbers. You only need to change things by a few degrees to get the idea. Reset when you finished.

Now we\'re going to see why the Yaw-Pitch-Roll labels are not really suitable. Change the Roll number to 90°. Yaw should move the nose of the aeroplane up and down and Pitch should move it side to side *as viewed from outside the aeroplane* which is where we are. Do they? No they don\'t! Pitch changes the yaw and Yaw changes the pitch. OK, Reset.

So, a better way of thinking about rotations is that Yaw changes your Longitude, Pitch changes your Latitude and Roll changes the direction (NSEW) that you\'re facing. Or you could check out [Axes conventions](http://en.wikipedia.org/wiki/Axes_conventions) for other descriptions.

Right, back to work. Change Yaw to 45° and Pitch to -30°. Click on OK to show that the operation has been completed. Now get back the [Placement Task](Placement.md) and look at the Rotation box. It has reverted to \'Rotation axis with angle\' and has some wierd numbers Axis and Angle boxes. Mine had Axis: (0.219493,-0.529904,0.819161) and Angle: 53.65°. The three numbers in brackets are the XYZ components of a unit vector in the 3D space. It is the axis about which our original Aeroplane was rotated to get our final Aeroplane. The angle is how much it was rotated. Clever, huh, but not very friendly! It was Euler who showed that you could combine a series of XYZ rotations into one rotation about one axis.

Here\'s some more suggestions for playing with the Aeroplane:

-   Change the Z Location (and Apply) then change the YPR numbers and see what the effect is. Then try changing the X and Y Locations and rotating.
-   Change the X Centre (and Apply) then change the YPR numbers and see what the effect is. Then try changing the Y and Z Centres and rotating.

I hope this little tutorial has helped you to get a feel for rotations.


{{Tutorials navi

}}

---
[documentation index](../README.md) > Aeroplane/zh-tw
