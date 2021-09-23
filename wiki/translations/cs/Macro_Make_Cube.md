# Macro Make Cube/cs



{{Macro/cs
|Name=Make Cube
|Translate=Make Cube
|Icon=Macro_makeCube.png
|Description=Toto makro vytváří kostku podle 4 vyžádaných bodů
|Author=Yorik
|Version=2.0
|Date=2011-08-01
|FCVersion=<=0.11
|Download=[https://www.freecadweb.org/wiki/File:Macro_makeCube.png ToolBar Icon]
}}

## Popis

Toto makro vytvoří kostku tím, že požádá o 4 body

## Skript

ToolBar Icon ![](images/Macro_makeCube.png )

**Macro\_Make\_Cube.FCMacro**


```python
# first we import the needed Draft modules
import draftTools, WorkingPlane
from draftlibs import fcvec

class myCommand(draftTools.Creator):
    "A class to define our custom command"
    # this command is based on the generic draftTools Creator template
    # it will ask for 4 points, defining our cube

    def __init__(self):
        # general setup, we define everything we'll need at startup
        print "Starting command..."
        # The Activated function of the Creator defines several variables such as self.view
        draftTools.Creator.Activated(self,"Cube")
        # we use the point UI of the draft Toolbar, which has X,Y and Z input fields
        self.ui.pointUi()
        self.points = [] # here we will store our points
        self.linetracker = draftTools.lineTracker()
        # we build a special cube tracker which is a list of 4 rectangle trackers
        self.cubetracker = []
        for i in range(4): 
            self.cubetracker.append(draftTools.rectangleTracker())
        self.constraintracker = draftTools.lineTracker(dotted=True)
        self.call = self.view.addEventCallback("SoEvent",self.action)

    def action(self,arg):
        # 3D scene handler. This function will be called by the 3D view on
        # special events such as keypress or mouse movements. We must take
        # care of treating what we want. All the hard work will be here!
        point,ctrlPoint = draftTools.getPoint(self,arg)
        if arg["Type"] == "SoKeyboardEvent": 
            if arg["Key"] == "ESCAPE":
                # important! if ESC is pressed, we cancel everything
                self.finish()
        elif arg["Type"] == "SoLocation2Event":
            # this will be executed in case of mouse movement
            if len(self.points) == 1:
                # this will be executed after we got our first point
                self.linetracker.p2(point)
                self.length = self.linetracker.getLength()
                self.ui.setRadiusValue(self.length)
            elif len(self.points) == 2:
                # now we already have our base line, we update the 1st rectangle
                self.cubetracker[0].p3(point)
                self.width = self.cubetracker[0].getSize()[1]
                self.ui.setRadiusValue(self.width)
            elif len(self.points) == 3:
                # we must first find our height point by projecting on the normal
                w = fcvec.project(point,self.normal)
                # then we update all rectangles
                self.cubetracker[1].p3((self.cubetracker[0].p2()).add(w))
                self.cubetracker[2].p3((self.cubetracker[0].p4()).add(w))
                self.cubetracker[3].p1((self.cubetracker[0].p1()).add(w))
                self.cubetracker[3].p3((self.cubetracker[0].p3()).add(w))
                self.height = w.Length
                self.ui.setRadiusValue(self.height)

        elif arg["Type"] == "SoMouseButtonEvent":
            if (arg["State"] == "DOWN") and (arg["Button"] == "BUTTON1"):
                # this will be executed in case of mouse button 1 pressed
                print "Got point: ",point
                if len(self.points) == 0:
                    # this is our first clicked point   
                    self.linetracker.p1(point)
                    self.linetracker.on()
                    # we set the radius UI, which has only a length input field
                    # but we change the "radius" name
                    self.ui.radiusUi()
                    self.ui.labelRadius.setText("Width")
                elif len(self.points) == 1:
                    # this is our second point
                    # first we turn off our line tracker
                    self.linetracker.off()
                    # then we turn on only one of the rectangles
                    baseline = point.sub(self.points[0])
                    self.cubetracker[0].setPlane(baseline)
                    self.cubetracker[0].p1(self.linetracker.p1())
                    self.cubetracker[0].on()
                    self.ui.labelRadius.setText("Length")
                elif len(self.points) == 2:
                    # this is our third point
                    # we can get the cubes Z axis from our first rectangle
                    self.normal = self.cubetracker[0].getNormal()
                    # we can therefore define the (u,v) planes of all rectangles
                    u = self.cubetracker[0].u
                    v = self.cubetracker[0].v
                    self.cubetracker[1].setPlane(u,self.normal)
                    self.cubetracker[2].setPlane(u,self.normal)
                    self.cubetracker[3].setPlane(u,v)
                    # and the origin points of the vertical rectangles
                    self.cubetracker[1].p1(self.cubetracker[0].p1())
                    self.cubetracker[2].p1(self.cubetracker[0].p3())
                    # finally we turn all rectangles on
                    for r in self.cubetracker:
                        r.on()
                    self.ui.labelRadius.setText("Heigth")
                elif len(self.points) == 3:
                    # finally we have all our points! Let's create the actual cube.
                    cube = self.doc.addObject("Part::Box","Cube")
                    cube.Length = self.length
                    cube.Width = self.width
                    cube.Height = self.height
                    # we get 3 points that define our cube orientation
                    p1 = self.cubetracker[0].p1()
                    p2 = self.cubetracker[0].p2()
                    p3 = self.cubetracker[0].p4()
                    cube.Placement = WorkingPlane.getPlacementFromPoints([p1,p2,p3])
                    self.finish()
                self.points.append(point)

    def finish(self):
        # this will be executed when finishing the command
        # first thing, we remove our callback function
        self.view.removeEventCallback("SoEvent",self.call)
        # then we turn off the draft toolbar
        self.ui.offUi()
        # important! we must remove all coin stuff
        self.linetracker.finalize()
        for r in self.cubetracker:
            r.finalize()
        # then we call the generic finish function of our creator object
        draftTools.Creator.finish(self)
        print "Finished!"

#  finally, we execute our code!
myCommand()
```

