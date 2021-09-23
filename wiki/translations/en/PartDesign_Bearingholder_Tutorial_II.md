# PartDesign Bearingholder Tutorial II/en




{{TutorialInfo
|Topic=Modeling
|Level=Experienced User
|Author=NormandC
|Time=
|FCVersion=0.19.23300 or higher
|Files=
}}


**This tutorial was originally written for a now deprecated development version of FreeCAD. As of April 2016 these features have been integrated in the 0.17 pre-development release available [https://github.com/FreeCAD/FreeCAD/releases/tag/0.17_pre here].
<br />
Please note that this version of FreeCAD is still in an early stage of development. Moreover this tutorial may require updating. If you want to participate in its review and update, please post to the Wiki section of the [http://forum.freecadweb.org forum].**

![Bearing Holder Tutorial - Finished bearing holder (top)\|thumb\|right\|400px](images/HolderTop2-19.jpg )

~~As the warning at the top of the page already indicates, this **tutorial will NOT WORK unless you compile a special highly experimental branch from FreeCAD source code** and is an introductory tutorial to modeling with the PartDesign workbench in FreeCAD **using Datum planes which are a feature that does not yet exist in most FreeCAD versions**.~~

## Purpose in Brief 

The purpose of the tutorial is to introduce you to two different work flows for creating a cast part with drafts and fillets. Depending on what other CAD programs you have been using, one or the other might be familiar to you. As a working example we will be modeling a simple bearing holder.

This is the second part of the tutorial. It will use what might be called the \'multiple body\' workflow, using the (simpler) top part of the holder as an example.

Obviously, to follow through this tutorial you must activate the PartDesign workbench.

~~You can find my version of the part created in this tutorial [http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4 here](http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4_here.md)~~ *The file is no longer available, a new one will be provided at some later date*.

## Design data 

The holder should be able to hold a diameter 90mm bearing with a width of up to 33mm (e.g. DIN 630 type 2308 which has an inside diameter of 40mm). The bearing requires a shoulder height of at least 4.5mm in the holder (and on the shaft). The top part of the holder will be bolted to the bottom with two 12mm bolts. The head of such a bolt will require at least 20mm diameter free space. There should be a groove on both sides of the bearing able to hold a standard shaft sealing ring DIN 3760: 38x55x7 or 40x55x7 on one side, 50x68x8 on the other side.

The holder will be a sand cast with a minimum wall thickness of 5mm, a draft angle of 2 degrees, and a minimum fillet radius of 3mm.

## Setting up the skeleton geometry 

![Sketch of the skeleton geometry\|thumb\|right\|400px](images/HolderTop2-2.png ) Create a new part in the PartDesign workbench. Rename the Body that is created by default to Skeleton. This Body is probably activated already, which you can see by the blue background colour in the feature tree. Create a new sketch on the YZ plane containing the outline of the shaft, bearing and sealing rings. After finishing the sketch, make a revolution feature from it. This skeleton feature will later be used to reference the real geometry to it. This means that if you want to change any dimensions, all you need to do is adjust the skeleton feature\'s dimensions and the rest of the part will update accordingly. ![The skeleton geometry\|thumb\|right\|400px](images/HolderTop2-2-1.jpg )

## The main body 

![Sketch of the first Pad\|thumb\|right\|400px](images/HolderTop2-3.jpg ) Create a new body and make it active. The sketch for the first pad is shown on the right. It is placed on a datum plane with an offset of 5mm (wall thickness) from the skeleton face marking the side of one of the bearing sealing rings. Because all the important dimensions are taken from the skeleton, there are just three dimensions: The machining allowance (3mm) at the base as an offset to the XY-plane, the 5mm wall thickness from the outer diameter of the skeleton, and the two degrees draft angle. Two create the 5mm dimension, you first need to select the outer circle (radius 45mm) of the skeleton geometry as external geometry in the sketcher, and then put in a construction line constrained tangential to this circle and at an angle of two degrees.

You are probably wondering why there is this small straight segment at the bottom of each arc. This segment ensures that there will be a draft angle of 2 degrees on the arcs. This might look like a lot of work for a very small benefit, but many CAD programs (and maybe FreeCAD one day) have tools that highlight a solid model in different colours and immediately show you all faces where the draft angle is not correct. You don\'t want that to happen to your model, especially after putting on a lot of fillets!
![The first Pad\|thumb\|right\|400px](images/HolderTop2-4.jpg ) When you have done the sketch (which is a bit tricky because of the 2 degree tangential lines), create a Pad from it extending up to the other side of the skeleton geometry, again with a 5mm offset to the side face. You don\'t need to create a datum plane this time, the \"up to face\" mode of the Pad dialog offers to input an offset.
![Sketch for Pad cut-out\|thumb\|right\|400px](images/HolderTop2-5.jpg ) Next, we will cut away some material on both ends of the Pad because it is always ideal for cast parts to have as uniform a wall thickness as possible. Create a sketch on each of the end faces of the Pad and dimension it at 5mm offset from the circle representing the bearing sealing ring (radius 27.5mm on one side and 34mm on the other). For the bottom line segment of the sketch, create another external geometry from the Pad and constrain to this. Thus the sketch has only a single dimension, the 5mm wall thickness (the 150mm and 75mm dimensions are not important as long as they are large enough to ensure that everything is cut away).
![The Pad with cut-outs to achieve uniform wall thickness\|thumb\|right\|400px](images/HolderTop2-6.jpg ) Use the sketch you created to make a Pocket and extend it to the face of the skeleton geometry that represents the bearing, minus 5mm offset for the wall thickness. For the second Pocket, you can use the option \"Duplicate selected object\" from the Edit menu to duplicate the sketch you already made (choose not to duplicate dependend objects if the question pops up). Then, select the face you want to move this sketch to, and tell FreeCAD to map the sketch to this face (this is an item on the PartDesign menu). After creating the second Pocket, you can look at the result from the bottom to check that you have a uniform wall thickness of 5mm around the contour of the skeleton geometry.
![Neutral plane for applying draft\|thumb\|right\|400px](images/HolderTop2-7.jpg ) Now it\'s time to create draft and fillets. The draft feature requires a neutral plane, meaning that the geometry that is cut by this plane will remain in its place, while the rest of the face is tilted at the draft angle. Using the bottom of the Pad for this purpose for this is not a good idea, because the wall thickness in the top part of the holder would become less than 5mm. So we create a datum plane offset about 35mm from the XY for this purpose. Activate the Skeleton body and create the plane there, because we will need it for applying draft to other bodies, too.
![First body with draft and fillets\|thumb\|right\|400px](images/HolderTop2-8.jpg ) The picture on the right shows the finished first body with draft and fillets applied. Note that the outer (concave) edges have a larger fillet radius of 5mm, again with the purpose of creating a more uniform wall thickness (more than 5mm is not possible because then after machining the inside of the holder the wall thickness would become less than 5mm).

## Adding the bodies for the bolts 

![The sketch for the body for the bolts\|thumb\|right\|400px](images/HolderTop2-13.jpg ) The bolts need two cylindrical bodies on both sides of the main Body. It is best to include the 2 degree draft angle in the sketch. I tried revolving a cylinder and later applying a draft, but weird things happened after mirroring it and I couldn\'t put fillets on it because the surface was warped somehow.

The sketch is dimensioned so that the rotation axis is 12mm distance to the outer diameter of the skeleton Body, 7mm for the radius of the hole plus 5mm for the wall thickness. For the sake of having a fully parametric part, it is a good idea to add a plane to the Skeleton about 25mm above the XY-plane to mark the top of the cylinders. Since this will be machined, the sketch is dimensioned 3mm above it.

![The body for the bolts\|thumb\|right\|400px](images/HolderTop2-14.jpg ) Create a revolution from the sketch and apply a fillet of 4mm to the top. This means that after machining away 3mm, a slight radius will remain which helps to avoid a sharp edge where someone could cut their hand when tightening the bolt.
![The main body with the two bodies for the bolts\|thumb\|right\|400px](images/HolderTop2-16.jpg ) Create a boolean feature to fuse the main Body and the bolt body. Then create a new body for the other side. Duplicate the sketch of the revolution, move it to this body and create the second body for the bolts (mirroring a Body is not supported yet so you need to redo most of it). Then fuse this second body into the main Body as well. Finally, apply a large fillet on the edge created by the boolean fuse operation. The largest I could get was 4mm.

## Hollowing out the main body 

![The first Pad of the cut-out body inside the main body\|thumb\|right\|300px](images/HolderTop2-9.jpg ) We will now work on the inside of the holder and hollow it out to make space for the bearing and sealing rings. When doing this of course we need to keep in mind the 3mm machining allowance. Since this tutorial teaches the multi-body method, we will create the inside geometry as a separate body and then cut it out of the main body with a boolean operation.

Create a new body and make it active. First, we need a datum plane offset 3mm inside the skeleton face that shows the side of the bearing. Then, duplicate the sketch of the first Pad of the main body. It will be added to the main body, so right-click on it and choose to move it to the newly created body (this option is only available in the context menu if the PartDesign workbench is active). Map the sketch onto the datum plane (if the sketch turns upside-down after mapping, move the datum plane to the other side of the bearing, next to where the duplicated sketch is located). Now, modify the sketch so that the diameter is 3mm less than the outer diameter of the skeleton geometry that represents the bearing. All you need to do is remove the 5mm dimension, drag the sketch inside the reference circle, and create a new 3mm dimension.
![The cut-out body inside the skeleton body\|thumb\|right\|400px](images/HolderTop2-10.jpg ) Next we want two more Pads to hollow out the place for the sealing rings. Duplicate the sketch of the first pad of the cut-out Body and map it to the XZ-plane. Edit the sketch and replace the external reference with the outer diameter of the bearing sealing ring. Extrude this sketch to an offset of 3mm of the side of the sealing ring. Repeat the whole process for the sealing ring on the other side.

After this we want to create two more Pads like the last two to give the shaft a clearance (e.g. 3mm) inside the holder.
![The complete cut-out body (minus impossible fillets)\|thumb\|right\|400px](images/HolderTop2-11.jpg ) Now all that remains is to apply draft to the planar side faces, using the same neutral plane as for the main body, and filleting. Apply a general fillet of 3mm to all edges. You will notice that there are several edges that cannot be filleted\... this is a defect of the underlying geometric kernel which FreeCAD uses.
![The completed raw part of the holder (without machining)\|thumb\|right\|400px](images/HolderTop2-15.jpg ) We are ready to hollow out the main body. Select it and choose to create a new Boolean operation. Add the cut-out body to the list window and set the operation to \"Cut\". Put a 3mm fillet on the two edges resulting from the cut-out operation (again some edges remain that are \"unfilletable\"). The result should look like the picture on the right.

The raw part is now completed. This is what the holder will look like before machining. Note that since the mold will have a top and bottom half, the edge between these two cannot be filleted. Also, if you give away this model to a foundry make sure to point out that it has the dimensions after casting. The foundry will then have to apply a certain percentage of shrinkage to the model (making the digital model used to manufacture the mold larger so that when the metal cools down and shrinks after casting it will have the right size).

## Machining

![Sketch to \"drill\" the hole for the bolts\|thumb\|right\|400px](images/HolderTop2-17.jpg ) To take away the material for machining the inside of the holder, very conveniently we can use the Skeleton Body itself. If you don\'t want that because then the skeleton gets hidden somewhere deep in the tree, you can also duplicate the sketch of the skeleton Revolution feature and re-create the revolution in another body. This is not completely parametric, though, because the duplicated sketch is independent of the original, so you will have to work on both if you change a dimension. Dependent duplicated features might be supported in the future sometime.

For the rest of the machining, create a new Body. The bottom of the holder will be machined by a Pad sketched on the XY-plane extending downwards. Next, sketch a revolution to make a hole for the bolts. You will need to sketch on the XZ-plane and revolve it so that you can choose the outer diameter of the skeleton Body as an external reference. The top part of the sketch will serve to machine a flat place for the head of the bolt. It is dimensioned to leave at least 5mm wall thickness in the holder. If this does not give enough space for the bolt head then you can move the datum plane upwards. Of course, you could put this logic into the Skeleton, which is left as an exercise to the reader!
![The machining Body\|thumb\|right\|400px](images/HolderTop2-18.jpg ) You can mirror the revolution on the YZ-axis. The picture on the right shows the \"machining\" Body. Of course, most of the dimensions of the Pads and Revolutions are not important as long as there is plenty of overlap.
![The finished Holder with machining\|thumb\|right\|400px](images/HolderTop2-19.jpg ) Finally, create a boolean operation to cut the machining Body out of the main Body. If you want a nice visual effect, you can colour the machined surfaces differently from the rest of the part. This is also a useful optical feedback showing you whether you forgot to machine somewhere.

## Part One 

[PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I.md)



[Category:Tutorials](Category:Tutorials.md)
