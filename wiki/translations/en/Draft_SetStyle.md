---
 GuiCommand:
   Name: Draft SetStyle
   MenuLocation: Utilities , Set style
   Workbenches: Draft_Workbench, BIM_Workbench
   Shortcut: Draft: **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor, Draft_ApplyStyle
---

# Draft SetStyle/en

## Description

The <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft SetStyle** command sets the default style for new objects.

<img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Shape.png  style="width:" height="500px;"> <img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Annotation.png  style="width:" height="500px;"> 
*The two tabs (<small>(v1.0*) of the Style settings task panel)</small> 

## Usage

1.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_style.png ) button in the [Draft Tray](Draft_Tray.md). Depending on the current style settings this button can look different.
    -   [Draft](Draft_Workbench.md): Select the **Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style** option from the menu, or from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
    -   Draft: Use the keyboard shortcut: **S** then **S**.
2.  The **Style settings** task panel opens. See [Options](#Options.md) for more information.
3.  Optionally change one or more settings.
4.  Press the **OK** button to save the settings.
5.  The button in the [Draft Tray](Draft_Tray.md) is updated.

## Options

-   From the dropdown list at the top of the task panel an exiting style preset can be selected.
-   Press the **<img src="images/Document-save.svg" width=16px>** button to save the current style settings as a preset.
-   On the **Shape** tab the following settings can be specified:
    -   
        **Shape appearance**
        
        -   
            **Shape color**
            
            .

        -   
            **Ambient shape color**
            
            . <small>(v1.0)</small> 

        -   
            **Emissive shape color**
            
            . <small>(v1.0)</small> 

        -   
            **Specular shape color**
            
            . <small>(v1.0)</small> 

        -   
            **Shape transparency**
            
            .

        -   
            **Shape shininess**
            
            . <small>(v1.0)</small> 

    -   
        **Other**
        
        -   
            **Line color**
            
            .

        -   
            **Line width**
            
            .

        -   
            **Point color**
            
            . <small>(v1.0)</small> 

        -   
            **Point size**
            
            . <small>(v1.0)</small> 

        -   
            **Draw style**
            
            .

        -   
            **Display mode**
            
            .
-   The settings on the **Annotation** tab apply to [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md). The following settings can be specified (see [Draft Text](Draft_Text#View.md) and [Draft Dimension](Draft_Dimension#View.md) for details):
    -   
        **Texts**
        
        -   
            **Font name**
            
            .

        -   
            **Font size**
            
            . This is in fact the default line height, the letters are smaller.

        -   
            **Line spacing factor**
            
            . Not used for dimensions.

        -   
            **Scale multiplier**
            
            . This is the inverse of the scale set in the [Draft annotation scale widget](Draft_annotation_scale_widget.md). If the scale is {{value|1:100}} the multiplier is {{Value|100}}. <small>(v1.0)</small> 

        -   
            **Text color**
            
            .

    -   
        **Lines and arrows**
        
        -   
            **Line width**
            
            . <small>(v1.0)</small> 

        -   
            **Arrow type**
            
            .

        -   
            **Arrow size**
            
            .

        -   
            **Line and arrow color**
            
            . <small>(v1.0)</small> 

    -   
        **Dimensions**
        
        -   
            **Show unit**
            
            .

        -   
            **Unit override**
            
            .

        -   
            **Dim line overshoot**
            
            . <small>(v0.21)</small> 

        -   
            **Ext line length**
            
            . <small>(v0.21)</small> 

        -   
            **Ext line overshoot**
            
            . <small>(v0.21)</small> 

        -   
            **Text spacing**
            
            .
-   Press the **<img src="images/Draft_SetStyle.svg" width=16px> Selected** button to apply the settings to selected objects or groups. Objects can be selected while the task panel is open.
-   Press the **<img src="images/Draft_Text.svg" width=16px> Annotations** button to apply the settings to all [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md) in the current document. <small>(v0.21)</small> 
-   Press the **Cancel** button to finish the command without saving the settings.

## Notes

-   The settings on the **Shape** tab, except **Draw style** and **Display mode**, are not only used for Draft objects, but also for objects created with other workbenches.
-   All settings, except **Draw style** and **Display mode**, can also be changed in the preferences. See [PartDesign Preferences](PartDesign_Preferences#Shape_appearance.md) and [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).
-   Styles are saved in a file with a fixed name: **StylePresets.json** which is stored in FreeCAD\'s user **Draft** folder:
    -   On Linux it is usually **/home/<username>/.local/share/FreeCAD/Draft/**.
    -   On Windows it is **%APPDATA%\FreeCAD\Draft\**, which is usually **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\**.
    -   On macOS it is usually **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/en
