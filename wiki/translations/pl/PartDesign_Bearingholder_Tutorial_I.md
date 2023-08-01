---
- TutorialInfo:/pl
   Topic:Modelowanie
   Level:Użytkownik zaawansowany
   Author:NormandC
   Time: nieokreślony
   FCVersion:0.19.23300 lub nowszy
   Files:brak
---

# PartDesign Bearingholder Tutorial I/pl





**This tutorial was originally written for a now deprecated development version of FreeCAD. This tutorial requires a complete rewrite to align with the PartDesign changes that will be in the upcoming v0.17 release.**





![Poradnik dotyczący oprawki łożyska - Gotowa oprawka łożyska *(góra)*\|thumb\|right\|400px](images/HolderTop1-1.jpg )

## Cel w skrócie 

Celem tego poradnika jest zapoznanie użytkownika z dwoma różnymi przebiegami pracy dla tworzenia części odlewanej z pochyleniami i zaokrągleniami. W zależności od tego, z jakich innych programów CAD korzystałeś, jeden lub drugi może być ci znany. Jako przykład roboczy będziemy modelować prostą oprawkę łożyska.

To jest pierwsza część poradnika. Wykorzysta on coś, co można nazwać przepływem pracy **pojedynczej zawartości**, używając *(prostszej)* górnej części uchwytu jako przykładu.

Oczywiście, aby przejść przez ten poradnik należy aktywować środowisko pracy Projekt Części.

~~Moją wersję części stworzonej za pomocą tego poradnika można znaleźć [http://ubuntuone.com/5gok0J4dye3Fo4BKWMGWVa tutaj](http://ubuntuone.com/5gok0J4dye3Fo4BKWMGWVa_tutaj.md).~~ *Plik nie jest już dostępny, nowy zostanie udostępniony w późniejszym terminie*.


## Założenia projektowe 

Oprawka powinna być w stanie utrzymać łożysko o średnicy 90 mm i szerokości do 33 mm *(np. DIN 630 typ 2308)*. Łożysko wymaga kołnierza o wysokości co najmniej 4,5 mm w oprawie *(i na wale)*. Górna część oprawy zostanie przykręcona do dolnej za pomocą dwóch śrub 12 mm. Po obu stronach łożyska powinien znajdować się rowek umożliwiający zamocowanie standardowego pierścienia uszczelniającego wał DIN 3760: 38x55x7 lub 40x55x7 z jednej strony i 50x68x8 z drugiej strony.

Uchwyt będzie odlewem piaskowym o minimalnej grubości ścianki 5 mm, kącie zanurzenia 2° i minimalnym promieniu zaokrąglenia 3 mm.

== Setting up the skeleton geometry ==

![Bearing holder with the two most important skeleton planes\|thumb\|right\|text-top\|400px](images/HolderTop1-2.jpg )

The idea of skeleton geometry is to capture the basic design dimensions in a single datum feature (e.g. a plane or an axis). When the design dimension changes, all that needs to be done is to change the skeleton feature. If the model is well built, then all its feature will recompute to reflect the design change. This reduces the danger that in a complex model, where the basic design dimensions are used in multiple places, you forget to change it somewhere.

The alternative to skeleton geometry is to have a table of the basic design dimensions that assign a symbolic name to each dimension, and then use the symbolic name wherever the dimensions is required to build the model. FreeCAD does not allow this approach yet.

![Base planes and all datum planes\|thumb\|right\|text-top\|400px](images/HolderTop1-3.jpg )

For the case of the bearing holder, the two most important design dimensions are the distance between the bolts (which limits the size of the bearing that can be used) and the height of the bolt heads. The dimensions chosen are

-   Distance between bolts: Radius of bearing (45) + wall thickness (5) plus radius of hole for bolt (7) = 57mm, so the vertical plane will be 57mm offset from the YZ-plane. To create this datum plane, select the YZ-plane and then choose to create a new datum plane. Enter the offset in the dialog that opens up
-   Height of bolt heads: This was chosen as an offset of 28mm from the XZ-plane

For convenience, two further datum planes can be created to reflect the amount of material that must be cut away from the sides of the bearing holder. They are offset +22 and -22 from the XY-plane.

It is advisable to give clear names to the skeleton geometry. Most of the time, you will want to turn off visibility for datum planes because they clutter up the screen, and if the planes have self-explanatory names you can just pick them by name instead of from the screen.

## The solid geometry 

<img alt="Sketch of the first pad" src=images/HolderTop1-4.jpg  style="width:400px;"> Now its time to start creating some real geometry. The sketch for the first pad is shown on the right. It is placed on the XY-plane. There are just three dimensions: The inner radius (22.5mm), the machining allowance (3mm) at the base as an offset to the XZ-plane and the distance from the datum plane representing the bolt axis (7mm). This means that if you later move the datum plane, the pad will automatically adjust its outer radius. Remember that before you can use the datum plane for dimensioning, you need to introduce it as external geometry to the sketcher.

You are probably wondering why there is a small straight segment at the bottom of each arc. This segment ensures that there will be a draft angle of 2 degrees on the arcs. This might look like a lot of work for a very small benefit, but many CAD programs (and maybe FreeCAD one day) have tools that highlight a solid model in different colours and immediately show you all faces where the draft angle is not correct. You don\'t want that to happen to your model, especially after putting on a lot of fillets!

When you have done the sketch (which is a bit tricky because of the 2 degree tangential lines), just pad it symmetrically to the sketch plane with a length of 62mm: 34mm for the bearing, 2x 9mm for the sealing rings, 2x 5mm for the wall thickness.
<img alt="Sketch of the cut-away at the side of the pad" src=images/HolderTop1-5.jpg  style="width:400px;"> Next we want to cut away some material where the sealing rings are, because their outer diameter is much less than the bearing\'s. The easiest way to create the sketches is to select the sketch of the pad and then choose \"Duplicate selection\" from the edit menu. You can then remap the sketch to the side of the pad, and modify it as shown in the picture.

The only two important dimensions in the sketch are 3mm of machining allowance at the bottom, and a inner diameter of 78mm: 68mm for the outer diameter of the sealing ring + 2x 5mm wall thickness. Since the sealing ring on the other side will only have a diameter of 55mm, the cut-out can be 65mm here.

After you have created the sketch, pocket it up to the datum plane marking the bearing side plus 5mm wall thickness. If you ever want to modify the holder to be able to hold wider bearings, all you have to do is to change the dimension of these datum planes, and the cut-out depth will follow along.
<img alt="Sketch of the cut-away inside the pad" src=images/HolderTop1-6.jpg  style="width:400px;"> To reduce the amount of machining required, we also want to cut away some material inside the holder. Again, duplicating the sketch of the first pad is convenient. It doesn\'t even have to be remapped. Again, the only important dimensions are the machining allowance (3mm) and the outer diameters: 84mm for the place where the bearing will be (90mm - 2x machining allowance), 49mm for the smaller sealing ring (55mm - 2x 3mm) and 62mm for the larger sealing ring.

After creating the sketches, pocket them: Symetrically 28mm for the bearing cut-out (34mm - 2x machining allowance) and one-sided 23mm for the cut-outs for the sealing rings: 34mm / 2 for half the bearing width + 9mm for the sealing rings - 3mm machining allowance.
<img alt="Main geometry of the holder top" src=images/HolderTop1-7.jpg  style="width:400px;"> Your part should now look like the picture on the right. Note how the different cut-aways combine to create an almost uniform wall thickness, which will make the casting easier and less liable to have pores.
<img alt="Sketch with draft where the bolts will be" src=images/HolderTop1-8.jpg  style="width:400px;"> Now all that remains is to create some material for the bolts to go through. You might be tempted to sketch these as a circle and then pad them, but this will head you for trouble when you try to put the draft onto them later (I assume that is a weakness of OpenCascade). So to circumvent the problems, it is better to create a sketch with the draft angle included and then rotate it through 360 degrees.

Here again the skeleton planes come in useful. You will need the bolt axis plane and the bolt head plane as external geometry. Then, create a straight line for the rotation axis and make sure it is constrained to the bolt axis plane reference. Toggle it to be construction geometry. Then, sketch the rest of the contour. The important dimensions are the machining allowance at the top and bottom and the radius of 12mm: 7mm for the hole radius + 5mm wall thickness.
<img alt="Finished geometry of the holder top (without draft and fillets)" src=images/HolderTop1-9.jpg  style="width:400px;"> Create a revolution feature from the sketch and then mirror it on the YZ-plane. This is all the solid geometry we need to model. The rest is draft and fillets.

## Applying draft to the side faces 

<img alt="The neutral plane for creating drafts" src=images/HolderTop1-10.jpg  style="width:400px;"> The next step is to apply drafts on all faces. Its important to consider the location of the neutral plane, that is, the plane which the face is \"rotated\" around. If we choose as neutral plane the bottom of the holder, then we will have a problem with the wall thickness in the top part of the holder. Therefore, we create a datum plane at an offset of 40mm from the XZ plane as a compromise between the top of the holder becoming to thin and the bottom becoming to wide.
<img alt="Applying draft to the side faces of the holder" src=images/HolderTop1-11.jpg  style="width:400px;"> To put draft on a face, select this face and create the draft feature. You can then select more faces to apply the draft on. If you have a large part, it is advisable to draft only one face at a time. This means that if you change the geometry and a draft fails, only this one feature will fail, whereas if you put all faces in one draft feature, then the whole feature might fail because of one face failing. For a small part like the bearing holder, its sufficient to create two draft features: One for the four outside faces, and one for the inside faces.

The dialog will force you to select a neutral plane before completing. You can leave the pull direction empty, in this case it will be normal to the neutral plane. Don\'t forget to set the draft angle to 2 degrees.

## Filleting the holder 

<img alt="Fillet where the bolts will go" src=images/HolderTop1-13.jpg  style="width:400px;"> We can now fillet the part. The picture shows the first set of fillets. Start with the small circular fillets and make them 4mm radius. Even though 3mm would be enough as per specification of the part, a radius of 4mm means that after machining 1mm of the fillet is left, reducing the sharp edge produced by the machining. The large fillets are 6mm radius to help spread the force from the bolts into the rest of the part. It would be nice to make this radius even larger, but unfortunately OpenCascade can\'t handle overlapping fillets yet.

As with drafts, in a complex part you should fillet only one edge at a time to avoid unnecessary failures if the base geometry changes.
<img alt="Filleting the outside of the holder" src=images/HolderTop1-12.jpg  style="width:400px;"> The rest of the fillets are simply 3mm radius. Looking at the picture on the right, the two highlighted fillets could actually be filleted with 5mm to achieve a more uniform wall thickness for the casting. After machining, the minimum wall thickness of 5mm would still be maintained. But again the fact that OpenCascade can\'t handle overlapping fillets prevents us from doing this for the inner of the two highlighted fillets.
<img alt="Filleting the inside of the holder - problematic edge" src=images/HolderTop1-14.jpg  style="width:400px;"> Filleting the inside of the part presents us with a difficulty that cannot be solved with the current tools in the PartDesign workbench. The highlighted edge cannot be filleted at all, again because the rounds would overlap. This could be worked around by creating a sweep instead of a fillet, except that sweeps are not implemented in PartDesign yet. For the time being, we are forced to leave the edge as it is.
<img alt="The filleted part (except for the impossible edge)" src=images/HolderTop1-15.jpg  style="width:400px;"> The picture on the right shows the finished part in the state it will be before machining (except for the one edge that is impossible to fillet). You will notice that one edge that runs around the whole part has been left unfilleted on purpose. This is the edge where the bottom and the top of the mould meet. Here, no fillet is possible (and none is required anyway).

## Machining

<img alt="Machining the top and bottom of the holder" src=images/HolderTop1-16.jpg  style="width:400px;"> <img alt="Machining the inside of the bearing holder" src=images/HolderTop1-17.jpg  style="width:400px;"> Now we can cut away the material that will be machined off the raw cast part. This is very easy with the skeleton geometry defined. The idea is to create all machining features (Pockets and Grooves) using datum features only. This means they will be totally independent of the solid geometry of the bearing holder, which gives us some big advantages:

-   No matter how you change the solid geometry, the features for the machining can never fail.
-   You can create the machining geometry before finalizing the solid, which gives you useful visual feedback.
-   If you move the skeleton datum planes, then both the solid geometry and the machining will adapt automatically.
-   If you make a mistake in your solid geometry, the machining will still be in the correct position, and very likely the mistake will become glaringly obvious (e.g. a wall thickness becoming 2mm instead of 5mm). Whereas if you reference the machining to the solid geometry, it will adapt to the error in the solid and e.g. maintain the 5mm wall thickness, just in the same wrong location as the solid is.

Before starting on the machining geometry, I like to place a datum point in the tree and name it something like \"Machining_starts_here\". This is useful if you want to switch between the raw and the machined state of the part because you can see at a glance where to move the insert point to get the raw state.

To machine the bottom of the holder, just sketch a large rectangle on the XZ plane and pocket it. For the top, sketch a circle on the datum plane defining the bolt head location, and then mirror the pocket on the YZ plane. In the same way, create a pocket for the hole which the bolt will go through and mirror it. To machine the inside of the holder, create a sketch on the YZ plane and groove it.
<img alt="Finished part" src=images/HolderTop1-1.jpg  style="width:400px;"> Once you have done the machining, you can have a nice visual effect by colouring all the machined faces so that you can see at one glance which parts are raw casting and which are machined after casting.

## Final notes 

We have modelled the bearing holder top with the dimensions it will have after casting. To create the casting mould, you need to apply shrinkage to your part because after casting, when the hot metal cools down, it will shrink by a few percent (depending on the material). Usually it is best to leave the application of shrinkage to the foundry making the part because they have the required special knowledge. They should also tell you if your part has problematic areas, e.g. very thick walls suddenly joining to very thin sections without a properly tapered section between them.

## Part Two 

[PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Bearingholder Tutorial I/pl
