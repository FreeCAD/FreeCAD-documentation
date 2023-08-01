---
- TutorialInfo:   Topic:Add FEM Equation
   Level:Advanced
   Time:1 day
   Author:[JohnWang](User_JohnWang.md)
   FCVersion:0.19
---

# Add FEM Equation Tutorial/en





## Introduction

In this tutorial we are going to add the **Flow** equation to FreeCAD and implement support for the elmer solver. Please make sure you have read and understood [Extend FEM Module](Extend_FEM_Module.md) before reading this tutorial.

The task can be split into five parts:

-   **New equation type**. This step must only be done if the equation doesn\'t exist in FreeCAD yet (as opposed to a equation that is already in FreeCAD but not supported by the target solver).
-   **New equation object**. Adding a concrete document object representing the elmer specific equation.
-   **Extend solver object**. Adding support for the new equation to the solver object of elmer.
-   **Extend writer object**. Extending the analysis export of elmer to support the new equation type.
-   **Gui tool to create a equation**. Access the new equation function through workbench Gui.

## New equation type 

In this step we are going to modify the following file:

-    **src/Mod/Fem/femsolver/equationbase.py**
    

The equation type is shared among all equation objects of the different solver. Each type has a string specifier (e.g. \"Heat\") and a dedicated command that adds the equation to the selected solver. This allows for a simpler GUI where we have only one button for the heat equation which is used for all supported solver.

First add the new equation to the {{Incode|equationbase.py}} module. Each equation requires two classes. A document proxy and a view proxy. Those two classes will later be used as base classes for the Elmer specific equation classes. Just copy-paste them from an existing equation type and adjust the icon path inside {{Incode|getIcon(self)}} of the view proxy.


```python
class FlowProxy(BaseProxy):
    pass

class FlowViewProxy(BaseViewProxy):
    def getIcon(self):
        return ":/icons/FEM_EquationFlow.svg"
```

## New Elmer\'s equation object 

In this step we are going to implement the document object. We need to add a new {{Incode|flow.py}} file at:

-    **src/Mod/Fem/femsolver/elmer/equations/flow.py**
    

and modify the following files:

-    **src/Mod/Fem/ObjectsFem.py**
    

-    **src/Mod/Fem/CMakeLists.txt**
    

Let\'s start with adding the new {{Incode|flow.py}} file. This file can be copied from an existing equation.

### Keywords

-   If the new equation only supports keywords for **linear** systems copy the {{Incode|femsolver/elmer/equations/elasticity.py}} module.
-   If the new equation supports keywords for both **linear** and **non-linear** systems, copy {{Incode|femsolver/elmer/equations/heat.py}}.

The flow equation in Elmer is a potentially non-linear equation. This means that we are going to base our work on {{Incode|heat.py}}.

### Editing files 

After copying {{Incode|heat.py}} to {{Incode|flow.py}}, adjust {{Incode|flow.py}} in these locations:

-   the name argument of the {{Incode|create}} module function,
-   the base classes of the {{Incode|Proxy}} class,
-   the {{Incode|Type}} attribute of the {{Incode|Proxy}} class,
-   the {{Incode|ViewProxy}} classes.


```python
def create(doc, name="'''Flow'''"):
    return femutils.createObject(
        doc, name, Proxy, ViewProxy)

class Proxy(nonlinear.Proxy, equationbase.'''Flow'''Proxy):

    Type = "Fem::EquationElmer'''Flow'''"

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.Priority = 10

class ViewProxy(nonlinear.ViewProxy, equationbase.'''Flow'''ViewProxy):
    pass
```

Then you need to change the properties added via the {{Incode|obj.addProperty(..)}} function to those needed by the equation.

At the moment of writing this tutorial Elmer flow equation doesn\'t have any special properties. See Elmer elasticity equation for an example with properties.

Finally one has to register a **makeEquationFlow** definition in {{Incode|src/Mod/Fem/ObjectsFem.py}} by duplicating an available entry.

FreeCAD uses **make** to build the program. So we need to register the new module file ({{Incode|flow.py}}) in {{Incode|src/Mod/Fem/CMakeLists.txt}} the way described in [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). The suitable lists can be easily found by searching for existing equation modules files of Elmer.

## Extend Solver Object 

In this step we are going to modify the following file:

-    **src/Mod/Fem/femsolver/elmer/solver.py**
    

Right now we made FreeCAD aware that there is a new type of equation and even added a command that adds this equation to the selected solver object. We also implemented a concrete equation object for Elmer. Whats left to do now is to make the connection between Elmer and the flow equation. This must be done directly in Elmer solver object.

Register the module in which we just implemented our new equation object ({{Incode|flow.py}}) with the equation specifier from step 1 (\"Flow\") in the {{Incode|_EQUATIONS}} list in {{Incode|elmer/solver.py}}.


```python
from .equations import electrostatic
+from .equations import flow

...

_EQUATIONS = {
    "Heat": heat,
    "Elasticity": elasticity,
+    "Flow": flow,
}
```

## Extend writer object 

In this step we are going to modify the following file:

-    **src/Mod/Fem/femsolver/elmer/writer.py**
    

This file contains the {{Incode|Writer}} class which exports the analysis into Elmer SIF format.

For every supported equation there are two main methods handling the export of the respective equation. Just copy all of them from an existing equation and adjust them to your needs.

-    {{Incode|_getFlowSolver}}
    

-    {{Incode|_handleFlow}}
    

You need to register the {{Incode|_handleFlow}} method inside the {{Incode|Writer}} class:


```python
class Writer(object):
...
    def write(self):
...
        self._handleFlow()

...

```


{{Incode|_handleFlow}}

can control a series of other detailed methods. Our flow equation uses the following detailed methods:

-    {{Incode|_handleFlowConstants}}
    

-    {{Incode|_handleFlowMaterial}}
    

-    {{Incode|_handleFlowInitialVelocity}}
    

-    {{Incode|_handleFlowBndConditions}}
    

-    {{Incode|_handleFlowEquation}}
    

We now finished the function part of the new equation. Next we\'ll connect the new equation through the GUI.

## Gui tool to create an equation 

We have just created a new equation class. To access it from the FEM GUI, we need to create a button and link it to the new equation class. Here is a tutorial: [Add Button to FEM Toolbar Tutorial](Add_Button_to_FEM_Toolbar_Tutorial.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add FEM Equation Tutorial/en
