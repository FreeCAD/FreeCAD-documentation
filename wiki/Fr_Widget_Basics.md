# Fr Widget Basics

This chapter teaches you the basics of Fr\_Widget toolkit

## Writing your first Fr\_Widget program 

Basically, you need always to have a Fr\_CoinWindow. This widget is the container of the other widgets you create. It is a subclass of Fr\_Group. The Fr\_CoinWindow used to distribute events and hold a link to each widget you have in your window.

Fr\_CoinWindow doesn\'t draw any thing and it is not restricted to any dimensions. But there must be a such windows for getting your Fr\_Widgets work. If FreeCAD adapt this toolkit someday, the Fr\_CoinWindow should be always available and you shouldn\'t required to create one. But at the moment, you have to create one Fr\_CoinWindow whenever you need to use the toolkit. Notice that you shouldn\'t make several of Fr\_CoinWindow.. Only once.

The widgets interact with the user using the callback system.


```python
import ThreeDWidgets.fr_arrow_widget as wd
import ThreeDWidgets.fr_coinwindow as wnn
import math

mywin = wnn.Fr_CoinWindow()       #Create an instance of the CoinWindow                         
vec=App.Vector(0,0,0)             #Position of the widget 
arrows=(wd.Fr_Arrow_Widget(vec))  #An instance of the arrow widget 
rotation=([0.0,0.0,1.0,45)])      #Internally is radians but the widget system takes degree
arrows.w_color=(10,40,10)         #Color of the widget. Basically it R,G,B in the range of 0 to 1 in float values
arrows.setRotationAngle(rotation) #Rotation of the widget. It consist of the axis in three float values, and an angle
mywin.addWidget(arrows)           #Add the widget to the window 
mywin.show()                      #Show the window 
```

##### Explaining the code 

-   First line imports the fr\_arrow\_widget. Later we use it to create the widget itself.
-   Second line imports the fr\_coinwindow. As mentioned this is the container of the system. Without this widget, you will not be able to show anything
-   Third line is math library from Python. It is required for now but this will change. It is used to convert the rotation angle to radians. But in the future the interface angles will be in degree. Internally is still radians as COIN3D is in radians.

## Creating Fr\_Line\_widget as an example 

Lets start creating a new drawing widget. This widget will draw a line and has a label. We need to get two vertices to draw the line. The widget itself is a subclass of the abstract object called Fr\_Widget. Fr\_Widget is the base class for all widgets. It contains basic variable, objects and functions definitions. Some of these are not implemented and you have to implemented. If you will use any function that aren\'t implemented, an exception will popup.

#### Part1:

The class declaration for our new object:

```python
class Fr_Line_Widget(fr_widget.Fr_Widget):

    def __init__(self, vectors: List[App.Vector] = [], label: str = "", lineWidth=1):
        super().__init__(vectors, label)     
    """
    This class is for drawing a line in coin3D world
    """
       super().__init__(vectors, label)        
        #Must be initialized first as per the following discussion. 
        
        self.w_lineWidth = lineWidth  # Default line width
        self.w_widgetType = constant.FR_WidgetType.FR_EDGE
        
        self.w_callback_=callback           #External function
        self.w_lbl_calback_=lblcallback     #External function
        self.w_KB_callback_=KBcallback      #External function
        self.w_move_callback_=movecallback  #External function
        w_wdgsoSwitch = coin.SoSwitch()        
        w_wdgsoSwitch.whichChild = coin.SO_SWITCH_ALL  # Show all
```

The line (super) must be written in the first line after the definition of the class since we want to initialize the abstract widget(Fr\_Widget) before changing the internal objects and variables. We have as arguments to the widget:(vertices, label and line width). You must give exactly 2 vertices to the class, but line width and label is optional. Default line width is be 1.

There are four callbacks that we should define if we want to take benefit of the events. These are external function user should define them to do other tasks as events occur. For example mouse click or keyboard events ..etc.

The last two lines are related to Coin3d. The first one is a coin.SoSwitch object in coin which can be used to hide or show the drawn object. The other line is the configuration of that switch. We allow by default showing all objects.

#### Part2:

Look at Fr\_Widget. The functions that have no implementation must be implemented here. The most important functions are (draw, handle, redraw, label\_draw,label\_redraw). Drawing the object will be different from widget to widget. But they have many things in common. The uses the drawing functions implemented in fr\_draw.py. Since the actual drawing is implemented in fr\_draw, we will not describe here the COIN3D commands.

Each function in the fr\_draw returns the same object which is a coin.SoSeparator. This object is a container (group) of several coin commands. Details of those commands could be found in the documentation of COIN3D. But we will be describing the most common used commands when we explain the fr\_draw.py.

#### Part3:

We start to explain the code. This part is not difficult to understand .. It sets the width 
```python

    def lineWidth(self, width):
        """ Set the line width"""
        self.w_lineWidth = width
``` This is the most important function in this toolkit. It handles the events occur in the coin window and try to distinguish between different events. Coin3d doesn\'t implement by default double-click, but this function is implementing that also.

For Keyboard events, at the moment the toolkit doesn\'t mask the events. They are still the coin3d definition. This might change in the future. Whenever a widget uses the event, it must return 1 as an indication that the event(s) is/are processed. I think the code is self explanatory. Events, colors, and other constants could be found in the file constant.py. 
```python
    def handle(self, event):
        """
        This function is responsible of taking events and processing 
        it. Required action will be executed here. If the object is not targeted, 
        the function will skip the events. But if the widget was
        targeted, it returns 1. Returning 1 means that the widget
        processed the event and no other widgets needs to get the 
        event. Window object is responsible for distributing the events.
        """
        if type(event)==int:
            if event==FR_EVENTS.FR_NO_EVENT:
                return 1    # we treat this event. Nothing to do 
        
            clickwdgdNode = fr_coin3d.objectMouseClick_Coin3d(self.w_parent.link_to_root_handle.w_lastEventXYZ.pos,
                                                            self.w_pick_radius, self.w_widgetSoNodes)
            clickwdglblNode = fr_coin3d.objectMouseClick_Coin3d(self.w_parent.link_to_root_handle.w_lastEventXYZ.pos,
                                                            self.w_pick_radius, self.w_widgetlblSoNodes) 

            if clickwdgdNode == None and clickwdglblNode == None:
                #SoSwitch not found 
                self.remove_focus()
                return 0 
            
            if self.w_parent.link_to_root_handle.w_lastEvent == FR_EVENTS.FR_MOUSE_LEFT_DOUBLECLICK:
                # Double click event.
                if clickwdglblNode != None:
                    print("Double click detected")
                    #if not self.has_focus():
                    #    self.take_focus()
                    self.do_lblcallback()
                    return 1

            elif self.w_parent.link_to_root_handle.w_lastEvent == FR_EVENTS.FR_MOUSE_LEFT_RELEASE:
                if clickwdgdNode != None or clickwdglblNode != None:
                    if not self.has_focus():
                        self.take_focus()
                    self.do_callback()
                    return 1            

            #Don't care events, return the event to other widgets    
        return 0  # We couldn't use the event .. so return 0 

```

#### Part4:

This part is about the function \'draw\'. This function is responsible for drawing the whole widget. It takes care of drawing the widget when it is active, inactive, selected, has focus, lost focus, ..etc.

It has a direct connection to the fr\_draw library that provides the primitive drawings for ex. (Line, Square, Box, Arrow, 2D Arrow, Cube, Cylinder ..etc). For our widget we uses the line drawing. Lets look at the code

```python
    def draw(self):
        """
        Main draw function. It is responsible for creating the SoSeparator node,
        and draw the line on the screen - in the COIN3D world. 
        """
        try:
            
            if len(self.w_vector) < 2:
                raise ValueError('Must be 2 Vectors')
            p1 = self.w_vector[0]
            p2 = self.w_vector[1]

            if self.is_active() and self.has_focus():
                usedColor = self.w_selColor
            elif self.is_active() and (self.has_focus() != 1):
                usedColor = self.w_color
            elif self.is_active() != 1:
                usedColor = self.w_inactiveColor
            if self.is_visible():
                self.saveSoNodesToWidget(fr_draw.draw_line(p1, p2, usedColor, self.w_lineWidth))
                self.saveSoNodeslblToWidget(self.draw_label(usedColor))
                #add both to the same switch. and add them to the senegraph automatically
                allSwitch=[]
                allSwitch.append(self.w_widgetSoNodes)
                allSwitch.append(self.w_widgetlblSoNodes)
                self.addSoNodeToSoSwitch(allSwitch)
            else:
                return  # We draw nothing .. This is here just for clarifying the code

        except Exception as err:
            App.Console.PrintError("'Fr_Line_Widget' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

```

The function checks if we have got two vectors since the line needs two vectors. And after that it chooses the desired color based on the widgets status. Every widget needs to save the node to the widget and to the switch the widget has. The SoSwitch is to hide the widget when that is required. When the widget needs to redraw the whole drawing, first it removes the SoSeparator from the COIN3D scene graph and it should remove it from the widget also. And then it will recreate the whole thing again. that function is called redraw. The label is also drawn here. But we will talk about the labels later. But you need to call the draw\_label here. COIN3D drawings will be discussed in a separate page. Something to remember, draw your coin3d objects in the same way you draw in FreeCAD. Always make the default position (0,0,1). .i.e. the object should be drawn towards +Z axis. This is useful since when you apply rotation of other FreeCAD object your COIN object will take that direction without any problem. This is why my arrows (2d or 3D) are all located on the Z axis by default if you don\'t change them

#### Part5:

Widgets Label: Labels are necessary for the widget toolkit. For example the label for line widget can be used to show the length of the side the line is drawn for. It has also the call back mechanism so you can interact with the text shown on the screen. For our widget (Fr\_Line\_Widget) the label is drawn near to the beginning of the line ..i.e. near to the first Vertex. At the moment there is no alignment mechanism but that is in the todo list. This part will be updated later when that is implemented. Label drawings are collect in the file fr\_label\_draw.py. The text drawn is only 2D. There might be the need of making 3D text .. but this will/must come to the todo list. 
```python
    def draw_label(self,usedColor):
        LabelData = fr_widget.propertyValues()
        LabelData.linewidth = self.w_lineWidth
        LabelData.labelfont = self.w_font
        LabelData.fontsize = self.w_fontsize
        LabelData.labelcolor = usedColor
        LabelData.vectors = self.w_vector
        LabelData.alignment = FR_ALIGN.FR_ALIGN_LEFT_BOTTOM
        lbl = fr_label_draw.draw_label(self.w_label, LabelData)
        self.w_widgetlblSoNodes = lbl
        return lbl
``` PropertyValues is an object that is used to send the parameter to the drawing function. It simplifies the API interface for the label drawing. Many parameter must be defined for the label. For example (font name, font size, used color , position or the vector , alignment (which is not implemented yet), ..etc. All these are used to determine how the draw\_label will draw the actual text. The returned value from the draw\_label is an SoSeparator which should be added to the scene graph.

#### Part6:

This part is also relate to draw function. We need a mechanism to redraw the drawings. Normally you must remove the drawings and redraw the objects to get the coin3d objects changed. Fr\_Wdiget do the same. looking to the following code: 
```python
    def redraw(self):
        """
        After the widgets damages, this function should be called.        
        """
        if self.is_visible():
            # Remove the SoSwitch from fr_coinwindo
            self.w_parent.removeSoSwitchFromSeneGraph(self.w_wdgsoSwitch)

            # Remove the node from the switch as a child
            self.removeSoNodeFromSoSwitch()
           
            # Remove the seneNodes from the widget
            self.removeSoNodes()
            #Redraw label
            
            self.lblRedraw()
            self.draw()def lblRedraw(self):
        if(self.w_widgetlblSoNodes!=None):
            self.w_widgetlblSoNodes.removeAllChildren()
        
    
``` First function (redraw) will remove the drawings from the scene graph and remove the holder of the objects inside the widget. SoSepartor will be deleted since it will be recreated when draw function activates. But the SoSwitch object inside the widget doesn\'t need to be delete. It will not have any child/children. The same should happen to the label. That is why we have another function for redrawing the label (lblRedraw).

#### Part7:

We need also functions that will put the size of the object, resize it and move it. Bellow are the functions: 
```python

    def move(self, newVecPos):
        """
        Move the object to the new location referenced by the 
        left-top corner of the object. Or the start of the line
        if it is a line.
        """
        self.resize([newVecPos[0], newVecPos[1]])
    def resize(self, vectors: List[App.Vector]):  # Width, height, thickness
        """Resize the widget by using the new vectors"""
        self.w_vector = vectors
        self.redraw()

    def size(self, vectors: List[App.Vector]):
        """Resize the widget by using the new vectors"""
        self.resize(vectors)

    def label_move(self, newPos):
        pass
```}

Label move is not implemented yet. But drawing move,size and resize in deed is the same function. There many ways to do this job but to make it simple, Fr\_Widget delete the original vector and simply redraw the whole object. Not so much to clarify .. It is clear how the function works.

==== Part8: ====

to be continued\...
