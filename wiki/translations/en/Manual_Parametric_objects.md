# Manual:Parametric objects/en
{{Manual:TOC}}

FreeCAD employs a parametric modeling approach, where the geometry of objects is governed by underlying rules and parameters rather than being freely sculpted. This means each component\'s dimensions and characteristics are defined by parameters, which instruct the program on how to generate the geometry. For instance, to create a cylinder, parameters like radius and height are specified. With these values, FreeCAD generates the precise geometrical shape.

In FreeCAD, parametric objects are essentially small, programmable scripts that execute when any parameter is altered. These parameters can vary widely, including integers and floating-point numbers, real-world dimensional values such as millimeters, meters, or feet, coordinates (expressed as x, y, z), text strings, or even references to other objects. Such versatility in parameters allows the creation of complex models through a series of chained operations where each new object derives its characteristics from a previous one, while also introducing additional attributes.

For example, consider creating a solid cubic object through parametric modeling. You start with a basic 2D rectangular shape labeled as \'plate.\' of length l and width w. This sketch defines the base of your cubic object. Next, you define an \'Extrude\' operation, or \'Pad,\' specifying the distance to push or pull the sketch into a 3D object. This results in a solid cubic form based on the Sketch\'s shape and the extrusion distance specified.

![](images/FreeCAD_022_PArametricDesignPlate.png )

On the top face of the plate you sketch a circle of a given diameter d. You then use this circle to create a pocket (remove material) from the original plate.

![](images/FreeCAD_022_ParametricDesignPocket.png )

If you decide to change either of the dimensions of the plate, or of the circle, the final object would be also modified. Thanks to the use of a parametric design approach, there is no need to redo the object from the beginning.

1.  Recomputation is not always automatic. Heavy operations, that might modify a big portion of your document, and therefore take some time, are not performed automatically. Instead, the object (and all the objects that depend on it) will be marked for recomputation (a small blue icon appears on them in the tree view). You must then press the recompute button (or **Edit->Refresh**) to have all the marked objects recomputed.
2.  The dependency tree must always flow in the same direction. Loops are forbidden. (See [DAG](Glossary#Directed_Acyclic_Graph.md), and [DAG view](DAG_view.md)) You can have object A which depends on object B which depends on object C. But you cannot have object A which depends on object B which depends on object A. That would be a circular dependency. However, you can have many objects that depend on the same object, for example, objects B and C both depend on A. Menu **Tools -> Dependency graph** shows you a dependency diagram like on the image above. It can be useful to detect problems.

In FreeCAD\'s parametric modeling process, examining the dependency tree of an object provides a clear insight into the sequential build and relationships within a model. At the foundation of the structure in the above example is the \'Plate Sketch,\' which serves as the base for the initial form of the model. A \'Pad\' operation is then applied, which adds material to this foundational sketch, effectively creating a three-dimensional structure from the two-dimensional base.

Following this, a \'Circle Sketch\' is drafted on the newly formed surface. This circle forms the basis for the subsequent \'Pocket\' operation. The pocket operation strategically removes material from the structure, essentially carving out a portion based on the circle sketch. This process of adding and then subtracting material allows for complex geometries and features to be integrated into the basic model seamlessly.

Through this sequence of operations---starting from the base sketch, adding volume with a pad, and creating detailed features with additional sketches and pockets---the final object takes shape. Each step in this chain depends on its predecessor, illustrating the interconnected nature of parametric design in FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )

Not all objects are parametric in FreeCAD. Often, the geometry that you import from other files won\'t contain any parameters and will be simple, non-parametric objects. However, these can often be used as a base, or starting point for newly created parametric objects, depending, of course, on what the parametric object requires and the quality of the imported geometry.

All objects, however, parametric or not, will have a couple of basic parameters, such as a Name, which is unique in the document and cannot be edited, a Label, which is a user-defined name that can be edited, and a [placement](placement.md), which holds its position in the 3D space.

Finally, it is worth noting that custom parametric objects are [easy to program in Python](Scripted_objects.md).

**Read more**

-   [The properties editor](Property_editor.md)
-   [How to program parametric objects](Scripted_objects.md)
-   [Positioning objects in FreeCAD](Placement.md)
-   [Enabling the dependency graph](Std_DependencyGraph.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/en
