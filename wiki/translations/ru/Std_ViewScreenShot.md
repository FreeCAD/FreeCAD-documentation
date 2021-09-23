---
- GuiCommand:/ru
   Name:Std ViewScreenShot
   Name/ru:Std ViewScreenShot
   MenuLocation:Инструменты → Сохранить изображение...
   Workbenches:Все
   SeeAlso:[Std Print](Std_Print/ru.md), [Std PrintPdf](Std_PrintPdf/ru.md)
---

# Std ViewScreenShot/ru

## Описание

The **Std ViewScreenShot** command opens a dialog box to create an image file, a screenshot, from the active [3D view](3D_view.md).

<img alt="" src=images/Save_picture.png  style="width:800px;"> 
*The Save picture dialog box after pressing the Extended button*

## Применение

1.  Select the **Tools → <img src="images/Std_ViewScreenShot.svg" width=16px> Save picture...** option from the menu.
2.  The Save picture dialog box opens.
3.  Optionally press the **Extended** button to reveal an additional panel in the dialog box. For more information see [Options](#Options.md).
4.  Optionally browse to the correct folder.
5.  Enter a filename and select the file type.
6.  Press the **Save** button to create the image file and close the dialog box.

## Опции

### Image dimensions 

1.  Select a standard size from the **Standard sizes** dropdown list. Or specify the **Width** and **Height** for a custom size.
2.  Optionally press an **Aspect ratio** button to set the width-to-height ratio of the image. If the **Width** input box has the focus the height of the image will change and vice versa.

### Image properties 

1.  Select an option from the **Background** dropdown list:
    -   
        {{Value|Current}}
        
        This option uses the background of the 3D view.

    -   
        {{Value|White}}
        

    -   
        {{Value|Black}}
        

    -   
        {{Value|Transparent}}
        
        Not all image formats support transparency.
2.  Select an option from the **Creation method** dropdown list:
    -   
        {{Value|Offscreen (New)}}
        
        This is the default method. This method supports [anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing). *Technical information: The most important classes for this method are Qt\'s QOffscreenSurface and QOpenGLFramebufferObject.*

    -   
        {{Value|Offscreen (Old)}}
        
        This method does not work on many modern Linux systems as it relies on the graphics driver. This method does not support anti-aliasing. *Technical information: This is a real off-screen rendering method that only uses functions from the Coin3d library.*

    -   
        {{Value|Framebuffer (custom)}}
        
        This method supports anti-aliasing. *Technical information: If anti-aliasing is off, this method reads the image directly from the graphics renderer, else it renders to a framebuffer and gets the image from there. The key part of this method is Qt\'s QOpenGLFramebufferObject class.*

    -   
        {{Value|Framebuffer (as is)}}
        
        This method uses the same techniques as **Framebuffer (custom)**. It also supports anti-aliasing but has some limitations related to custom sizes and always uses the current background of the 3D view.

### Image comment 

1.  Select the {{RadioButton|TRUE|Insert MIBA}} option to add [MIBA](MIBA.md) information to the file. Not all image formats support this.
2.  Or select the {{RadioButton|TRUE|Insert comment}} option and type a comment in the text field to embed a comment in the file. Not all image formats support this.
3.  Check the {{CheckBox|TRUE|Add watermark}} checkbox to add a watermark. The watermark is placed in the lower left corner of the image and consists of the FreeCAD logo and name above the main FreeCAD URL: [www.freecadweb.org](http://www.freecadweb.org).

## Примечания

-   The number of available image file formats may vary depending on your OS.
-   Some OpenGL drivers don\'t allow renderings above a certain maximum size.

## Настройки

-   The 3D view background can be changed in the preferences: **Edit → Preferences... → Display → Colors → Background color**. See [Preferences Editor](Preferences_Editor#Colors.md).
-   To change the 3D view anti-aliasing: **Edit → Preferences... → Display → 3D view → Rendering → Anti-Aliasing**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting

It is possible to create screenshots with python code.


```python
Gui.ActiveDocument.ActiveView.saveImage('C:/temp/test.png',1656,783,'Current')
```

This script saves a series of screenshots of different sizes and from different directions. The camera type, orthographic or perspective, is also changed.


```python
import Part, PartGui
# Loading test part
Part.open('C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp')
OutDir = 'C:/temp/'
 
# Creating images with different Views, Cameras and sizes
for p in ['PerspectiveCamera','OrthographicCamera']:
    Gui.SendMsgToActiveView(p)
    for f in ['ViewAxo','ViewFront','ViewTop']:
        Gui.SendMsgToActiveView(f)
        for x,y in [[500,500],[1000,3000],[3000,1000],[3000,3000],[8000,8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.jpg',x,y,'White')
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.png',x,y,'Transparent')

# Close active document
App.closeDocument(App.ActiveDocument.Name)
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewScreenShot/ru
