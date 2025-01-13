# FrameForge Workbench/pl
<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="FrameForge Workbench icon" src=images/FrameForge.svg  style="width:128px;">


</div>





<div lang="en" dir="ltr" class="mw-content-ltr">

## Introduction


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

FrameForge is dedicated to creating Frames and Beams, and apply operations (miter cuts, trim cuts) to theses profiles.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The tutorial below is also available on [GitHub](https://github.com/lukh/frameforge/blob/main/docs/tutorial.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Tutorial


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Create the skeleton 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Beams are attached to edges (from a sketch for instance) or Parametric Lines. For a start, we are going to create a simple frame.


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">In a new file, switch to the FrameForge workbench.
</div>
    

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Create a sketch, and specify the XY orientation.
</div><img alt="" src=images/FrameForge_00-create-sketch.png  style="width:500px;">

    <img alt="" src=images/FrameForge_01-select-orientation.png  style="width:200px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Draw a simple square in the sketch. This will be our skeleton.
</div><img alt="" src=images/FrameForge_02-create-frame-skeleton.png  style="width:300px;">

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Close Sketch edit mode.
</div>
    


<div lang="en" dir="ltr" class="mw-content-ltr">

### Create the frame 


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Launch the Create Profile tool.
</div><img alt="" src=images/FrameForge_10-profiles.png  style="width:300px;">

    <img alt="" src=images/FrameForge_10-profiles-task.png  style="width:300px;">

    <img alt="" src=images/FrameForge_10-profiles-task-2.png  style="width:300px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Select a profile from the lists (Material / Family / Size). You can change the size just below the family, the tool has a lot of predefined profiles, you can also change the parameters.
</div><img alt="" src=images/FrameForge_11-profiles-family.png  style="width:300px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">In the 3D View, select the edges to apply the profile to.
</div><img alt="" src=images/FrameForge_13-edge-selection.png  style="width:500px;">

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Press **OK** in the task panel. You now have four profiles and your first frame.
</div><img alt="" src=images/FrameForge_14-profiles-done.png  style="width:500px;">

    <img alt="" src=images/FrameForge_14-zoom-on-profiles.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

### Going 3D 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

We can build more complex shapes, and there are several ways of doing it.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### More sketches (part 1) 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

We can add more sketches to our project:


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Create a new Sketch.
</div>
    

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Select the same orientation as before (XY).
</div>
    

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Draw a square with the same size and placement as before.
</div>
    

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Change the position of the sketch to put it 400mm above the first one.
</div><img alt="" src=images/FrameForge_20-sketch-base-placement.png  style="width:300px;">

    <img alt="" src=images/FrameForge_20-sketch-base-placement-2.png  style="width:300px;">

5.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You can now use the Create Profile tool again to create another square frame.
</div><img alt="" src=images/FrameForge_21-stacked-frames.png  style="width:400px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Parametric Line 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

You can create Parametric Lines by joining two vertexes (points). Theses lines can be used for profiles as well.


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">To see the sketches temporarily hide the profile objects with the **Space Bar**.
</div><img alt="" src=images/FrameForge_22-hide-profiles.png  style="width:300px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Select two vertexes.
</div>![](images/FrameForge_23-select-vertexes.png )

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Create a Parametric Line.
</div><img alt="" src=images/FrameForge_24-create-parametric-line.png  style="width:300px;">

    <img alt="" src=images/FrameForge_25-parametric-line.png  style="width:300px;">

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Repeat for the other 3 legs of the frame.
</div>
    

5.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Use the Create Profile tool again to attach profiles to the 4 lines.

    1.  Launch Create Profile.
    2.  Select the profile you want.
    3.  Select the 4 Parametric Lines.
    4.  Press **OK**.
</div><img alt="" src=images/FrameForge_26-cube-done.png  style="width:400px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

#### More sketches (part2) 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

There is another ways to add sketches, that allows to do more complicated stuff.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Sometimes you want to add a sketch at a specific location, and link it to another sketch. So that when you modify the first sketch, the second will follow. This is not possible with the Position / Base Placement, that is an absolute position, you have to \"Map\" the second sketch to the first sketch.


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Create a new Sketch, and set its orientation to YZ.
</div>
    <div lang="en" dir="ltr" class="mw-content-ltr">Just for reference I have added a circle to the sketch so you can see where it is.
</div><img alt="" src=images/FrameForge_30-mapmode-sketch.png  style="width:300px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Click on the Map Mode property:
</div><img alt="" src=images/FrameForge_31-mapmode.png  style="width:300px;">

    <img alt="" src=images/FrameForge_32-mapmode-dialog.png  style="width:300px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You can change the Map Mode, selecting faces, vertexes and edges. Here, our circle sketch has been realigned. There are a lot of options.
</div><img alt="" src=images/FrameForge_33-mapmode.png  style="width:800px;">

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You can then edit the sketch, and create more lines and frames.
</div>
    


<div lang="en" dir="ltr" class="mw-content-ltr">

### Bevels and corners 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

As you can see, the junctions are not good yet. The profiles are centered on the skeleton, and stop at the ends of the edges.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

We are going to make corners and bevels. There are two methods for that.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Via Bevels property 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This is the preferred option for simple frames.


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Let\'s hide everything except the first frame we made.
</div><img alt="" src=images/FrameForge_40-show-first-frame.png  style="width:500px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Select one of the profiles, and in the Property editor look for Bevel Start/End Cut1/Cut2.
</div><img alt="" src=images/FrameForge_41-bevels.png  style="width:300px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">There are 4 entries (Start/End Cut1/Cut2). These allow you to create bevels in the two axis, at the start or end of the profile. Negative angles work, and must be used to compensate directions.
</div>
    

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You can change the properties of multiple profiles at the same time.
</div><img alt="" src=images/FrameForge_42-batchs-bevels.png  style="width:700px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Via Create Miter Ends tool 


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Let\'s show the other base frame.
</div><img alt="" src=images/FrameForge_50-base-config.png  style="width:500px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">First we must add offsets to the existing profiles. Offsets add to the dimensions of the edges. You can change the profiles one at a time, or change them all at once.
</div><img alt="" src=images/FrameForge_51-add-offset.png  style="width:500px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Deselect all objects, then select two touching Profiles. You must select faces in the 3D view, not objects in the Tree view.
</div><img alt="" src=images/FrameForge_52-select-touching-profiles.png  style="width:300px;">

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Click on the Create Miter Ends tool to create two trimmed profiles.
</div><img alt="" src=images/FrameForge_53-create-miter-end.png  style="width:300px;">

    <img alt="" src=images/FrameForge_54-miter-end.png  style="width:300px;">

5.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Repeat for the other corners of the second frame.
</div>
    


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Via Trim Profile tool 


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">When all profiles are made visible again, you can see that the vertical profiles are not cut as they should be.
</div><img alt="" src=images/FrameForge_60-startwith.png  style="width:300px;">

    <img alt="" src=images/FrameForge_61-bad-joint.png  style="width:300px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Launch the Trim Profile tool.
</div><img alt="" src=images/FrameForge_62-endtrim.png  style="width:300px;">

    <img alt="" src=images/FrameForge_62-endtrim-task.png  style="width:300px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Select the vertical profile first, add it as the Trimmed Object with the **<img src="images/List-add.svg" width=16px>** button.
</div><img alt="" src=images/FrameForge_63-select-trimmed-body-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_63-select-trimmed-body-2.png  style="width:400px;">

4.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Select the Trimming Boundaries you want to cut with. Here I have rotated the view to select two bottom faces.
</div><img alt="" src=images/FrameForge_64-select-trimming-boundaries-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_64-select-trimming-boundaries-2.png  style="width:400px;">

5.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You can change the cut type: straight or following the other profile.
</div><img alt="" src=images/FrameForge_64-select-cuttype-1.png  style="width:400px;">

    <img alt="" src=images/FrameForge_64-select-cuttype-2.png  style="width:400px;">

6.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You also can add faces to trim the other side of the profile.
</div>
    


<div lang="en" dir="ltr" class="mw-content-ltr">

### Organizing Objects 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

That\'s the bad part. I find the Tree view messy. Really messy.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Part Container 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

I often use Part containers to group profiles, sketches, etc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/FrameForge_70-part-container.png  style="width:300px;">


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/FrameForge_71-part-container.png  style="width:300px;">


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

You should drag only one profile at a time into the container. I don\'t know why, but FreeCAD is not happy about a group drag. Sometime parts and profiles then jump out of the Part container.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Fusion


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

You can fuse profiles together. It allows to group objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/FrameForge_72-fusion.png  style="width:300px;">


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/FrameForge_72-fusion-done.png  style="width:300px;">


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Using profiles in PartDesign 


</div>

1.  
    <div lang="en" dir="ltr" class="mw-content-ltr">To use these profiles in PartDesign you need to create a fusion and then a Body.
</div><img alt="" src=images/FrameForge_80-body.png  style="width:300px;">

2.  
    <div lang="en" dir="ltr" class="mw-content-ltr">Drag and drop the fusion onto the Body.
</div><img alt="" src=images/FrameForge_81-basefeature.png  style="width:300px;">

3.  
    <div lang="en" dir="ltr" class="mw-content-ltr">You now have a standard PartDesign Body and you can use PartDesign to do whatever you want. You can for example create holes.
</div><img alt="" src=images/FrameForge_82-making-holes.png  style="width:400px;">

    <img alt="" src=images/FrameForge_83-holes-made.png  style="width:400px;">



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > FrameForge Workbench/pl
