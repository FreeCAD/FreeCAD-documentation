# Raytracing templates/ru
## Introduction

The [Raytracing Workbench](Raytracing_Workbench.md) comes with some templates for povray and luxrender, but you can easily create your own. All you need to do is to create a scene file for the given renderer, then edit it manually with a text editor to insert special tags that FreeCAD will recognize and where it will insert its contents (camera and objects data).

Personal templates <small>(v0.18)</small>  can be placed under the path


```python
~/.FreeCAD/data/Mod/Raytracing/Templates
```

## Povray

Povray scene files (with extension .pov) can be created manually with a text editor (povray is made primarily to be used as a scripting language), but also with a wide range of 3D applications, such as [blender](http://www.blender.org). On the [povray website](http://www.povray.org/) you can find further information and a list of applications able to produce .pov files.

When you have a .pov file ready, you need to open it with a text editor, and do two operations:

1.  Strip out the camera information, because FreeCAD will place its own camera data. To do so, locate a text block like this: camera { ... }, which describes the camera parameters, and delete it (or put \"//\" in front of each line to comment them out).
2.  Insert the following line somewhere: //RaytracingContent. This is where FreeCAD will insert its contents (camera and objects data). You can, for example, put this line at the very end of the file.

Note that FreeCAD will also add some declarations, that you can use in your template, after the //RaytracingContent tag. These are:

-   cam_location: the location of the camera
-   cam_look_at: the location of the target point of the camera
-   cam_sky: the up vector of the camera.
-   cam_angle: the angle of the camera

If you want, for example, to place a lamp above the camera, you can use this: 
```python
light_source {
 cam_location + cam_angle * 100
 color rgb <10, 10, 10>
}
```

## Luxrender

Luxrender scene files (with extension.lxs) can either be single files, or a master .lxs file that includes world definition (.lxw), material definition (.lxm) and geometry definition (.lxo) files. You can work with both styles, but it is also easy to transform a group of 4 files in a single .lxs file, by copying the contents of each .lxw, .lxm and .lxo file and pasting it at the point where that file is inserted in the master .lxs file.

Luxrender scene files are hard to produce by hand, but are easy to produce with many 3D applications such as [blender](http://www.blender.org). On the [luxrender website](http://www.luxrender.net), you\'ll find more information and plugins for the main 3D applications out there.

If you will work with separated .lxw, .lxm and .lxo files, beware that the final .lxs exported by FreeCAD might be at a different location than the template file, and therefore these files might not be found by Luxrender at render time. In this case you should or copy these files to the location of your final file, or edit their paths in the exported .lxs file.

If you are exporting a scene file from blender, and wish to merge everything into one single file, you will need to perform one step before exporting: By default, the luxrender exporter in blender exports all mesh geometry as separate .ply files, instead of placing the mesh geometry directly inside the .lxo file. To change that behaviour, you need to select each of your meshes in blender, go to the \"mesh\" tab and set the option \"export as\" to \"luxrender mesh\" for each one of them.

After you have your scene file ready, to turn it into a FreeCAD template, you need to perform the following steps:

1.  Locate the camera position, a single line that begins with LookAt, and delete it (or place a \"#\" at the beginning of the line to comment it out)
2.  At that place, insert the following line: #RaytracingCamera
3.  At a desired point, for example just after the end of the materials definition, before the geometry information, or at the very end, just before the final WorldEnd line, insert the following line: #RaytracingContent. That is where FreeCAD will insert its own objects.

Note that in luxrender, the objects stored in a scene file can define transformation matrixes, that perform location, rotation or scaling operations. These matrixes can stack and affect everything that come after them, so, by placing your #RaytracingContent tag at the end of the file, you might see your FreeCAD objects affected by a transformation matrix placed earlier in the template. To make sure that this doesn\'t happen, place your #RaytracingContent tag before any other geometry object present in the template. FreeCAD itself won\'t define any of those transformation matrixes.


{{Raytracing Tools navi/ru}}


{{Userdocnavi/ru}}



---
⏵ [documentation index](../README.md) > [Raytracing](Category_Raytracing.md) > Raytracing templates/ru
