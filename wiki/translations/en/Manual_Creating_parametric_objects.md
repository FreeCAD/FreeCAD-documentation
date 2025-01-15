# Manual:Creating parametric objects/en
{{Manual:TOC}}

In the [previous chapter](Manual_Creating_and_manipulating_geometry.md), we explored how to create **Part** geometry and display it on screen by attaching it to a \"dumb\" (non-parametric) document object. While effective, this approach becomes cumbersome when you need to modify the shape. Each change requires creating a new shape and reassigning it to the object, resulting in repetitive and inefficient workflows.

Throughout this manual, we've seen how parametric objects address this issue by allowing dynamic updates. By modifying a single property, the shape recalculates automatically, eliminating the need for manual updates. This recalculation process enables more efficient modeling and introduces adaptability to designs. Internally, parametric objects operate similarly to what we've already done: they recalculate the contents of their **Shape** property every time one of their properties changes. This iterative process is seamless and ensures that the object remains consistent with its defined parameters.

FreeCAD offers a user-friendly system for creating parametric objects entirely in Python. These objects are defined using a Python class, which:

-   Declares the necessary properties for the object.
-   Defines the behavior when any of these properties are modified.

The structure of such a parametric object is as simple as this:


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```

All Python classes typically have an **\_\_init\_\_** method. This method is executed when a class is instantiated---that is, when a Python object is created from the class. You can think of a class as a \"template\" or blueprint used to create live instances of itself. Each instance of the class becomes an independent object with its own attributes and methods. In our **\_\_init\_\_** method, we perform two crucial tasks:

-   Store the class itself in the **Proxy** attribute of the FreeCAD document object:

By assigning **self** to the **Proxy** attribute of the FreeCAD document object, we link the logic of our Python class to the FreeCAD object. This means the document object will \"carry\" the Python class code inside itself, allowing it to behave according to the logic defined in the class. This connection enables FreeCAD to know how to interact with and recalculate the parametric object.

-   Create all the properties the object needs:

Using the **addProperty** method, we define the custom properties required by the object. Properties act as parameters or variables for the object and can be accessed, modified, and displayed in FreeCAD\'s property editor. In the example, we add a floating-point property named **MyLength**. This property will later influence the shape or behavior of the object.

There are many types of properties available in FreeCAD, ranging from floating-point numbers to strings and even specialized types for geometry and materials. To explore the full list of available property types, you can type the following code in the Python console:


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```

The second key part of our class is the **execute** method. This method is automatically triggered whenever the object is marked for recomputation, which happens when one of its properties is modified. The **execute** method is where all the recalculations for the object take place, ensuring that its shape and behavior are updated to reflect any changes. Within the **execute** method, you perform all the necessary operations to generate the new geometry for your object. Typically, this involves recalculating the shape based on the current values of its properties and then assigning the updated shape to the object\'s **Shape** attribute using a statement like **obj.Shape = myNewShape**. The **execute** method takes a single argument, **obj**, which represents the FreeCAD document object associated with your parametric object. This allows you to directly manipulate the object within the method, such as accessing its properties, updating its geometry, or performing other operations.

In summary:

-   The **execute** method is called whenever the object needs to be updated.
-   It is responsible for recalculating the shape and assigning it to the object\'s **Shape** attribute.
-   The **obj** argument gives access to the FreeCAD document object, enabling you to make changes programmatically.

With this system, FreeCAD handles the rest---ensuring that the object is properly updated in the document and displayed correctly in the graphical interface.

One crucial thing to remember is that when you create parametric objects in a FreeCAD document, the Python code used to define them is not saved within the file. This is an intentional security measure. If FreeCAD files were allowed to store Python code, it could open the door for malicious actors to distribute files containing harmful scripts that might damage someone's computer. As a result, when you share a FreeCAD file containing parametric objects created with custom Python code, the recipient must also have access to the code used to define those objects. Without it, FreeCAD won't know how to recalculate or interact with the objects properly.

The simplest way to ensure this is to save the Python code in a macro file. When distributing your FreeCAD file, you can include the macro alongside it. Alternatively, you can share the macro on the [FreeCAD macros repository](Macros_recipes.md), allowing others to easily download and use it. This approach ensures that your custom parametric objects remain functional on other systems while maintaining security best practices.

Below, we will do a small exercise, building a parametric object that is a simple parametric rectangular face. More complex examples are available on the [parametric object example](Scripted_objects.md) and in the [FreeCAD source code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) itself.

We will give our object two properties: Length and Width, which we will use to construct a rectangle. Then, since our object will already have a pre-built Placement property (all geometric objects have one by default, no need to add it ourselves), we will displace our rectangle to the location/rotation set in the Placement, so the user will be able to move the rectangle anywhere by editing the Placement property.


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```

Instead of pasting the above code in the Python console, we\'d better save it somewhere, so we can reuse and modify it later. For example in a new macro (menu **Macro -\> Macros -\> Create**). Name it, for example, \"ParamRectangle\". However, FreeCAD macros are saved with a .FCMacro extension, which Python doesn\'t recognize when using import. So, before using the above code, we will need to rename the ParamRectangle.FCMacro file to ParamRectangle.py. This can be done simply from your file explorer, by navigating to the Macros folder indicated in menu Tools -\> Macros.

Once that is done, we can now do this in the Python Console:


```python
import ParamRectangle
```

By exploring the contents of ParamRectangle, we can verify that it contains our ParametricRectangle class.

To create a new parametric object using our ParametricRectangle class, we will use the following code. Observe that we use **Part::FeaturePython** instead of **Part::Feature** that we have been using in the previous chapters (The Python version allows to define our own parametric behaviour):


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

Here is a quick breakdown of the previous commands:

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")**: Creates a new **Part::FeaturePython** object named **Rectangle** in the active FreeCAD document. This object is specifically designed for custom parametric behavior, allowing Python-defined logic to manage its properties and behavior.

-   **ParamRectangle.ParametricRectangle(myObj)**: Initializes the object by associating it with the **ParametricRectangle** class from the **ParamRectangle** module or script. This links the custom Python-defined logic to the object, enabling it to act as a parametric object.

-   **myObj.ViewObject.Proxy = 0**: Resets the **ViewObject.Proxy** attribute to 0, ensuring that the object uses FreeCAD's default view handling. This step is required unless you define a custom ViewProvider to manage the visual representation of the object.

-   **FreeCAD.ActiveDocument.recompute()**: Recomputes the document to update the geometry and reflect changes in the FreeCAD graphical interface, making the new object fully visible and functional

Nothing will appear on screen just yet, because the **Length** and **Width** properties are 0, which will trigger our \"do-nothing\" condition inside execute. We just need to change the values of Length and Width, and our object will magically appear and be recalculated on the fly.

Of course, it would be tedious to have to type these 4 lines of Python code each time we want to create a new parametric rectangle. A very simple way to solve this is placing the 4 lines above inside our **ParamRectangle.py** file, at the end, after the end of the **ParametricRectange** class (We can do this from the Macro editor).

Now, when we type import ParamRectangle, a new parametric rectangle will automatically be created. Even better, we can add a toolbar button that will do just that:

-   Open menu **Tools -\> Customize**
-   Under the \"Macros\" tab, select our ParamRectangle.py macro, fill in the details as you wish, and press \"Add\":

![](images/FreeCAD_python_macroRec.png )

-   Under the Toolbars tab, create a new custom toolbar in the workbench of your choice (or globally), select your macro and add it to the toolbar:

![](images/FreeCAD_python_toolbarCus.png )

-   That\'s it, we now have a new toolbar button which, when clicked, will create a parametric rectangle.

Remember, if you want to distribute files created with this new tool to other people, they must have the **ParamRectangle.py** macro installed on their computers too.

**Read more**

-   [The FreeCAD macros repository](Macros_recipes.md)
-   [Parametric object example](Scripted_objects.md)
-   [More examples in the FreeCAD code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating parametric objects/en
