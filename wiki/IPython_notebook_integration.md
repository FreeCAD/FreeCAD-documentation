# IPython notebook integration
This page is dedicated to the Google Summer of Code project regarding the interoperability between IPython and FreeCAD, mostly regarding visualisation.

## Outline

FreeCAD is quite popular for its extensive Python API providing grounds for many advanced macros and extensions. The API, which exposes everything from the document structure, basic workbench specific types and even the whole GUI, offers large amounts of freedom for the user to create everything he wants. Python in itself has become increasingly popular in the scientific community over the last years, partially surpassing classical interpreted languages like Matlab in certain areas. Due to this increased interest in and usage of the language an ecosystem for scientific computation has evolved around Python, leading to advanced coding environments like IPython and its Jupyter notebook. As this scientific usage of the language fits very well into FreeCADs profile as a python driven CAx application it should be possible to tightly integrate it into the scientific workflow. This means less usage of a custom application GUI but good integration into multi-purpose computation environments like IPython.

FreeCAD\'s API in itself is solid and powerful enough to be used in IPython extensively, however, one main issue with CAx code is the visualisation. It is nearly impossible to develop 3D models without seeing them. It is therefore important to find a way to visualize FreeCAD\'s 3D scene in the IPython display system as supported by the IPython QTConsole and the Jupyter notebook.

## Details

1.  Get familiar with FreeCADs openinventor scenegraph and the basic working of the GUI module. Also learn the openinventor API and the scene graph structure it provides.
2.  Find a JavaScript library which makes it easy to create 3D scene graphs via WebGL and analyse how the nodes can be mapped to the open inventor scene graph nodes. A good candidate is [SceneJS](http://scenejs.org/)
3.  Write a openinventor action writing the JavaScript file which mimics the scene graph from the open inventor representation
    1.  It should export geometry nodes as well as material (color etc.), lightning and camera
    2.  Advanced: Implement a replacement for all openinventor nodes
4.  Create a real JavaScript 3D viewer which mimics FreeCAD viewer
    1.  It should support 3D navigation, standard views (top, bottom,\...)
    2.  Advanced: It should mimic the FreeCAD preselection, e.g. show edges, faces and vertices as they are in FreeCAD
    3.  Advanced: It should show the correct geometry names as in FreeCAD when preselected
    4.  Advanced: Implement multiple navigation modes
5.  Extend FreeCAD with functions returning an IPython compatible version of the created JavaScript 3D viewer
6.  Replace the current WebGL export with the new advanced component

## Expected Outcome 

1.  The possibility to easily show FreeCAD document objects in Jupyter without needing to fire up the FreeCAD GUI
2.  The possibility to comfortably navigate the 3D scene inside of Jupyter
3.  Better WebGL export
4.  Documentation of the FreeCAD IPython interoperability in the Wiki and an example Jupyter notebook.

## Future Possibilities 

If the 3D scene can be navigated other things, which FreeCAD can display, remain, for example the spreadsheet.

## Project Properties 

### Skills

-   Programming language mainly C++ and JavaScript
-   Understand and use APIs from FreeCAD and external libraries like openinventor

### Difficulty

Easy

### Additional Information 

-   Ticket on FreeCAD bug tracker: [\#2869](https://freecadweb.org/tracker/view.php?id=2869)
-   A FreeCAD kernel for Jupyter: [looooo/jupyter\_freecad\_kernel](https://github.com/looooo/jupyter_freecad_kernel)
-   Dedicated discussion: [IPython notebook integration](http://forum.freecadweb.org/viewtopic.php?f=22&t=14740)
-   Thread discussion: [How to use Jupyter Notebook with FreeCad (Guide)](https://forum.freecadweb.org/viewtopic.php?f=22&t=38976)
-   Thread discussion: [Embedding FreeCAD in IPython](https://forum.freecadweb.org/viewtopic.php?t=13620)
-   Thread discussion: [Has Anyone successfully connected to FC thru Jupyter ?](https://forum.freecadweb.org/viewtopic.php?t=38217)
-   Thread discussion: [IPython Qt Console](https://forum.freecadweb.org/viewtopic.php?f=10&t=14166)

## GSoC 2020 

This project was chosen for GSoC 2020. The results can be found here: [Git repo](https://github.com/kryptokommunist/Jupyter_FreeCAD). The corresponding thread in the FreeCAD forum can be found [here](https://forum.freecadweb.org/viewtopic.php?f=8&t=46039). Find a blog post [here](https://kryptokommun.ist/tech/2020/08/31/google-summer-of-code.html). The full project proposal can be found [here](https://docs.google.com/document/d/1VgfsD06Qvb87S-tQazfTsyYTp14Z3EjF4V9puPVNCTQ/edit). The results are a good base to build upon.

_ _ _

---
[documentation index](../README.md) > IPython notebook integration
