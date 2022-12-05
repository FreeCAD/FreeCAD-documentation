# Integrate Cycles renderer
**Cycles Renderer was added by Yorik in 2019! Please check out the [https://github.com/FreeCAD/FreeCAD-render FreeCAD-Render WB]**

## Outline

[Cycles](https://www.blender.org/manual/render/cycles/) is [Blender](http://www.blender.org)\'s new realistic renderer. Cycles has also been made [standalone](https://wiki.blender.org/index.php/Dev:Source/Render/Cycles/Standalone), and several other 3D modelers such as Rhino and Cinema4D are beginning to use it too.

As the [Raytracing Workbench](Raytracing_Workbench.md) of FreeCAD is already made to support several render engines, it is fairly easy to add a new one.

## Details

1.  Get familiar with the Cycles render engine as used in Blender. You might need to learn to use Blender, as it is the primary tool to use Cycles.
2.  Learn how to build Cycles on the different platforms. As the standalone version of Cycles is not yet as popular as Blender itself, precompiled packages are not available
3.  Learn the XML API of Cycles, how data can be passed to the renderer
4.  Create basic functionality in FreeCAD to create such XML files
5.  Create a new render object by adapting the luxrender object

## Expected outcome 

1.  A new available renderer added to the [Raytracing Workbench](Raytracing_Workbench.md)

## Future Possibilities 

Since direct modeling is a huge area in constant evolution, the work done in this GSoC will only cover a small part of it. But if the bases are done right, extending them will be easy and could develop very far.

## Project Properties 

### Skills

   Programming language C++
   Good understanding and use of APIs from FreeCAD and Cycles
   Knowledge of 3D modeling, topology and computational geometry is a plus

### Difficulty

Medium

## Additional Information



---
![](images/Right_arrow.png) [documentation index](../README.md) > Integrate Cycles renderer
