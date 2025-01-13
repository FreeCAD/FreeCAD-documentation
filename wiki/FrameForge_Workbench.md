# <img alt="FrameForge Workbench icon" src=images/FrameForge.svg  style="width:64px;"> FrameForge Workbench

 

## Introduction

FrameForge is dedicated to creating Frames and Beams, and apply operations (miter cuts, trim cuts) to theses profiles.

The tutorial below is also available on [GitHub](https://github.com/lukh/frameforge/blob/main/docs/tutorial.md).

## Tutorial

### Create the skeleton 

Beams are attached to edges (from a sketch for instance) or Parametric Lines. For a start, we are going to create a simple frame.



1.  
    In a new file, switch to the FrameForge workbench.

    
2.  
    Create a sketch, and specify the XY orientation.

    

    <img alt="" src=images/FrameForge_00-create-sketch.png  style="width:500px;">

    <img alt="" src=images/FrameForge_01-select-orientation.png  style="width:200px;">
3.  
    Draw a simple square in the sketch. This will be our skeleton.

    

    <img alt="" src=images/FrameForge_02-create-frame-skeleton.png  style="width:300px;">
4.  
    Close Sketch edit mode.

    



### Create the frame 



1.  
    Launch the Create Profile tool.

    

    <img alt="" src=images/FrameForge_10-profiles.png  style="width:300px;">

    <img alt="" src=images/FrameForge_10-profiles-task.png  style="width:300px;">

    <img alt="" src=images/FrameForge_10-profiles-task-2.png  style="width:300px;">
2.  
    Select a profile from the lists (Material / Family / Size). You can change the size just below the family, the tool has a lot of predefined profiles, you can also change the parameters.

    

    <img alt="" src=images/FrameForge_11-profiles-family.png  style="width:300px;">
3.  
    In the 3D View, select the edges to apply the profile to.

    

    <img alt="" src=images/FrameForge_13-edge-selection.png  style="width:500px;">
4.  
    Press **OK** in the task panel. You now have four profiles and your first frame.

    

    <img alt="" src=images/FrameForge_14-profiles-done.png  style="width:500px;">

    <img alt="" src=images/FrameForge_14-zoom-on-profiles.png  style="width:300px;">



### Going 3D 

We can build more complex shapes, and there are several ways of doing it.

#### More sketches (part 1) 

We can add more sketches to our project:



1.  
    Create a new Sketch.

    
2.  
    Select the same orientation as before (XY).

    
3.  
    Draw a square with the same size and placement as before.

    
4.  
    Change the position of the sketch to put it 400mm above the first one.

    

    <img alt="" src=images/FrameForge_20-sketch-base-placement.png  style="width:300px;">

    <img alt="" src=images/FrameForge_20-sketch-base-placement-2.png  style="width:300px;">
5.  
    You can now use the Create Profile tool again to create another square frame.

    

    <img alt="" src=images/FrameForge_21-stacked-frames.png  style="width:400px;">



#### Parametric Line 

You can create Parametric Lines by joining two vertexes (points). Theses lines can be used for profiles as well.



1.  
    To see the sketches temporarily hide the profile objects with the **Space Bar**.

    

    <img alt="" src=images/FrameForge_22-hide-profiles.png  style="width:300px;">
2.  
    Select two vertexes.

    

    ![](images/FrameForge_23-select-vertexes.png )
3.  
    Create a Parametric Line.

    

    <img alt="" src=images/FrameForge_24-create-parametric-line.png  style="width:300px;">

    <img alt="" src=images/FrameForge_25-parametric-line.png  style="width:300px;">
4.  
    Repeat for the other 3 legs of the frame.

    
5.  
    Use the Create Profile tool again to attach profiles to the 4 lines.

    1.  Launch Create Profile.
    2.  Select the profile you want.
    3.  Select the 4 Parametric Lines.
    4.  Press **OK**.

    

    <img alt="" src=images/FrameForge_26-cube-done.png  style="width:400px;">



#### More sketches (part2) 

There is another ways to add sketches, that allows to do more complicated stuff.

Sometimes you want to add a sketch at a specific location, and link it to another sketch. So that when you modify the first sketch, the second will follow. This is not possible with the Position / Base Placement, that is an absolute position, you have to \"Map\" the second sketch to the first sketch.



1.  
    Create a new Sketch, and set its orientation to YZ.

    Just for reference I have added a circle to the sketch so you can see where it is.

    

    <img alt="" src=images/FrameForge_30-mapmode-sketch.png  style="width:300px;">
2.  
    Click on the Map Mode property:

    

    <img alt="" src=images/FrameForge_31-mapmode.png  style="width:300px;">

    <img alt="" src=images/FrameForge_32-mapmode-dialog.png  style="width:300px;">
3.  
    You can change the Map Mode, selecting faces, vertexes and edges. Here, our circle sketch has been realigned. There are a lot of options.

    

    <img alt="" src=images/FrameForge_33-mapmode.png  style="width:800px;">
4.  
    You can then edit the sketch, and create more lines and frames.

    



### Bevels and corners 

As you can see, the junctions are not good yet. The profiles are centered on the skeleton, and stop at the ends of the edges.

We are going to make corners and bevels. There are two methods for that.

#### Via Bevels property 

This is the preferred option for simple frames.



1.  
    Let\'s hide everything except the first frame we made.

    

    <img alt="" src=images/FrameForge_40-show-first-frame.png  style="width:500px;">
2.  
    Select one of the profiles, and in the Property editor look for Bevel Start/End Cut1/Cut2.

    

    <img alt="" src=images/FrameForge_41-bevels.png  style="width:300px;">
3.  
    There are 4 entries (Start/End Cut1/Cut2). These allow you to create bevels in the two axis, at the start or end of the profile. Negative angles work, and must be used to compensate directions.

    
4.  
    You can change the properties of multiple profiles at the same time.

    

    <img alt="" src=images/FrameForge_42-batchs-bevels.png  style="width:700px;">



#### Via Create Miter Ends tool 



1.  
    Let\'s show the other base frame.

    

    <img alt="" src=images/FrameForge_50-base-config.png  style="width:500px;">
2.  
    First we must add offsets to the existing profiles. Offsets add to the dimensions of the edges. You can change the profiles one at a time, or change them all at once.

    

    <img alt="" src=images/FrameForge_51-add-offset.png  style="width:500px;">
3.  
    Deselect all objects, then select two touching Profiles. You must select faces in the 3D view, not objects in the Tree view.

    

    <img alt="" src=images/FrameForge_52-select-touching-profiles.png  style="width:300px;">
4.  
    Click on the Create Miter Ends tool to create two trimmed profiles.

    

    <img alt="" src=images/FrameForge_53-create-miter-end.png  style="width:300px;">

    <img alt="" src=images/FrameForge_54-miter-end.png  style="width:300px;">
5.  
    Repeat for the other corners of the second frame.

    



#### Via Trim Profile tool 



1.  
    When all profiles are made visible again, you can see that the vertical profiles are not cut as they should be.

    

    <img alt="" src=images/FrameForge_60-startwith.png  style="width:300px;">

    <img alt="" src=images/FrameForge_61-bad-joint.png  style="width:300px;">
2.  
    Launch the Trim Profile tool.

    

    <img alt="" src=images/FrameForge_62-endtrim.png  style="width:300px;">

    <img alt="" src=images/FrameForge_62-endtrim-task.png  style="width:300px;">
3.  
    Select the vertical profile first, add it as the Trimmed Object with the **<img src="images/List-add.svg" width=16px>** button.

    

    <img alt="" src=images/FrameForge_63-select-trimmed-body-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_63-select-trimmed-body-2.png  style="width:400px;">
4.  
    Select the Trimming Boundaries you want to cut with. Here I have rotated the view to select two bottom faces.

    

    <img alt="" src=images/FrameForge_64-select-trimming-boundaries-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_64-select-trimming-boundaries-2.png  style="width:400px;">
5.  
    You can change the cut type: straight or following the other profile.

    

    <img alt="" src=images/FrameForge_64-select-cuttype-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_64-select-cuttype-2.png  style="width:400px;">
6.  
    You also can add faces to trim the other side of the profile.

    



### Organizing Objects 

That\'s the bad part. I find the Tree view messy. Really messy.

#### Part Container 

I often use Part containers to group profiles, sketches, etc.

<img alt="" src=images/FrameForge_70-part-container.png  style="width:300px;">

<img alt="" src=images/FrameForge_71-part-container.png  style="width:300px;">

You should drag only one profile at a time into the container. I don\'t know why, but FreeCAD is not happy about a group drag. Sometime parts and profiles then jump out of the Part container.

#### Fusion

You can fuse profiles together. It allows to group objects.

<img alt="" src=images/FrameForge_72-fusion.png  style="width:300px;">

<img alt="" src=images/FrameForge_72-fusion-done.png  style="width:300px;">

### Using profiles in PartDesign 



1.  
    To use these profiles in PartDesign you need to create a fusion and then a Body.

    

    <img alt="" src=images/FrameForge_80-body.png  style="width:300px;">
2.  
    Drag and drop the fusion onto the Body.

    

    <img alt="" src=images/FrameForge_81-basefeature.png  style="width:300px;">
3.  
    You now have a standard PartDesign Body and you can use PartDesign to do whatever you want. You can for example create holes.

    

    <img alt="" src=images/FrameForge_82-making-holes.png  style="width:400px;">

    <img alt="" src=images/FrameForge_83-holes-made.png  style="width:400px;">



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > FrameForge Workbench
