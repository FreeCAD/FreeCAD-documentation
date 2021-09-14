# Line drawing function/cs




{{TOCright}}

## Introduction

This page shows how advanced functionality can easily be created in Python. In this exercise, we will build a new tool that draws a line. This tool can then be linked to a FreeCAD command, and that command can be called by any element in the interface, like a menu item or a toolbar button.

## The main script 

First we will write a script containing all our functionality. Then we will save this in a file and import it in FreeCAD to make all its classes and functions available. Launch your favorite code editor and type the following lines:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}

## Detailed explanation 


```python
import Part, FreeCADGui
from pivy.coin import *
```

In Python when you want to use functions from another module you need to import it. In our case we will need functions from the [Part](Part_Workbench.md) module, for creating the line, and from the Gui module `FreeCADGui`, for accessing the [3D view](3D_view.md). We also need the complete contents of the Coin library so we can directly use all Coin objects like `SoMouseButtonEvent`, etc.


```python
class line:
```

Here we define our main class. Why do we use a class and not a function? The reason is that we need our tool to stay \"alive\" while we are waiting for the user to click on the screen. A function ends when its task has been done, but an object (a class defines an object) stays alive until it is destroyed.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```

In Python, every class or function can have a documentation string (docstring). This is particularly useful in FreeCAD, because when you call that class in the interpreter, the description string will be displayed as a tooltip.


```python
def __init__(self):
```

Python classes can always contain an `__init__` function, which is executed when the class is called to create an object. Here we will put everything we want to happen when our line tool begins.


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```

In a class you usually want to prepend `self.` to variable names to make the variables easily accessible to all functions inside and outside the class. Here we will use `self.view` to access and manipulate the active 3D view.


```python
self.stack = []
```

Here we create an empty list that will contain the 3D points sent by the `getpoint()` function.


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```

This is the important part. Since we are dealing with a [Coin3D](https://github.com/coin3d/coin/wiki) scene, we use a Coin callback mechanism that allows a function to be called every time a certain scene event happens. In our case we are creating a callback for [SoMouseButtonEvent](https://coin3d.github.io/Coin/html/classSoMouseButtonEvent.html) events, and we bind it to the `getpoint()` function. Now every time a mouse button is pressed or released the `getpoint()` function will be executed.

Note that there is also an alternative to `addEventCallbackPivy()` called `addEventCallback()` which does not rely on pivy. But since pivy is a very efficient and natural way to access any part of a Coin scene, it is the better choice. {{Top}} 
```python
def getpoint(self, event_cb):
```

Now we define the `getpoint()` function that will be executed when a mouse button is pressed in a 3D view. This function will receive an argument that we will call `event_cb`. From this event callback we can access the event object, which contains several pieces of information (more info [here](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md)).


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```

The `getpoint()` function will be called when a mouse button is pressed or released. But we only want to pick a 3D point when a button is pressed, otherwise we would end up with two 3D points very close together. So we must check for that here.


```python
pos = event.getPosition()
```

Here we get the screen coordinates of the mouse cursor.


```python
point = self.view.getPoint(pos[0], pos[1])
```

This function gives us a FreeCAD vector (x,y,z) containing the 3D point that lies on the focal plane, just under our mouse cursor. If you are in camera view, imagine a ray coming from the camera, passing through the mouse cursor, and hitting the focal plane. That is the location of our 3D point. If we are in orthogonal view, the ray is parallel to the view direction.


```python
self.stack.append(point)
```

We add our new point to the stack.


```python
if len(self.stack) == 2:
```

Do we have enough points already? if yes, then let\'s draw the line!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```

Here we use the `LineSegment()` function from the Part module that creates a line from two FreeCAD vectors. The line is not bound to any object in our active document, so nothing appears on the screen.


```python
shape = l.toShape()
```

The FreeCAD document can only accept shapes from the Part module. Shapes are the most generic type of the Part module. So we must convert our line to a shape before adding it to the document.


```python
Part.show(shape)
```

The Part module has a very handy `show()` function that creates a new object in the document and binds a shape to it. We could also have created a new object in the document first and then bound the shape to it manually.


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```

Since we are done with our line we remove the callback mechanism here. {{Top}}

## Testing the script 

Now let\'s save our script in a folder where the FreeCAD Python interpreter can find it. When importing modules, the interpreter will look in the following places: the Python installation paths, the FreeCAD {{FileName|bin}} folder, and all FreeCAD {{FileName|Mod}} (module) folders. So the best solution is to create a new folder in one of the {{FileName|Mod}} folders. Let\'s create a {{FileName|MyScripts}} folder there and save our script in it as {{FileName|exercise.py}}.

Now everything is ready. Let\'s start FreeCAD, create a new document, and in the Python interpreter issue:


```python
import exercise
```

If no error message appears our exercise script has been loaded successfully. We can now check its contents with:


```python
dir(exercise)
```

The command `dir()` is a built-in Python command that lists the contents of a module. We can check that our `line()` class is there with:


```python
'line' in dir(exercise)
```

Now let\'s test it:


```python
exercise.line()
```

Click two times in the 3D view and bingo: here is our line! To repeat it just type `exercise.line()` again. {{Top}}

## Registering the script 

For our new line tool to be really useful, and to avoid having to type all that stuff, it should have a button in the interface. One way to do this is to transform our new {{FileName|MyScripts}} folder into a full FreeCAD workbench. This is easy, all that is needed is to put a file called {{FileName|InitGui.py}} inside the {{FileName|MyScripts}} folder. {{FileName|InitGui.py}} will contain the instructions to create a new workbench, and add our new tool to it. Besides that we will also need to change our exercise code a bit, so the `line()` tool is recognized as an official FreeCAD command. Let\'s start by creating an {{FileName|InitGui.py}} file, and writing the following code in it:


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```

By now you probably understand the above script. We create a new class that we call `MyWorkbench`, we give it a title `MenuText`, and we define an `Initialize()` function that will be executed when the workbench is loaded into FreeCAD. In that function, we load the contents of our exercise file, and append the FreeCAD commands found inside to a command list. Then, we make a toolbar called \"My Scripts\" and we assign our command list to it. Currently, of course, we only have one tool, so our command list contains only one element. Then, once our workbench is ready, we add it to the main interface.

But this still won\'t work because a FreeCAD command must be formatted in a certain manner to work, we will need to change our `line()` tool. Our new {{FileName|exercise.py}} script should look like this:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```

What we did here is transform our `__init__()` function into an `Activated()` function. When FreeCAD commands are run, they automatically execute the `Activated()` function. We also added a `GetResources()` function, that informs FreeCAD where it can find the icon for the tool, and what will be the name and tooltip of our tool. Any {{FileName|jpg}}, {{FileName|png}} or {{FileName|svg}} image will work as an icon, it can be any size, but it is best to use a size that is close to the final aspect, like 16x16, 24x24 or 32x32. Then we add the `line()` class as an official FreeCAD command with the `addCommand()` method.

That\'s it, now we just need to restart FreeCAD and we\'ll have a nice new workbench with our brand new line tool! {{Top}}

## So you want more? 

If you liked this exercise, why not try to improve this little tool? There are many things that can be done, for example:

-   Add user feedback: until now we did a very bare tool, the user might be a bit lost when using it. So we could add some feedback, telling the user what to do next. You could issue messages to the FreeCAD console. Have a look in the `FreeCAD.Console` module.
-   Add a possibility to type the 3D points coordinates manually. Look at the Python `input()` function for example.
-   Add the possibility to add more than 2 points.
-   Add events for other things: Now we just check for Mouse button events, what if we would also do something when the mouse is moved, like displaying current coordinates?
-   Give a name to the created object.

Don\'t hesitate to ask questions or share ideas on the [forum](https://forum.freecadweb.org/)! {{Top}} {{Powerdocnavi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
