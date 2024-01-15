---
 GuiCommand:
   Name: Draft SetStyle
   MenuLocation: Utilities , Set style
   Workbenches: Draft_Workbench, Arch_Workbench
   Shortcut: **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor, Draft_ApplyStyle
---

# Draft SetStyle/en

## Description

The <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft SetStyle** command sets the default style for new objects.

<img alt="" src=images/Draft_SetStyle_Taskpanel.png  style="width:" height="550px;"> 
*The Style settings task panel*

## Usage

1.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_style.png ) button in the [Draft Tray](Draft_Tray.md). Depending on the current style settings this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style** option from the menu.
    -   Use the keyboard shortcut: **S** then **S**.
2.  The **Style settings** task panel opens. See [Options](#Options.md) for more information.
3.  Optionally change one or more settings.
4.  Press the **OK** button to save the settings.
5.  The button in the [Draft Tray](Draft_Tray.md) is updated.

## Options

-   From the dropdown list at the top of the task panel an exiting style preset can be selected.
-   Press the **<img src="images/Document-save.svg" width=16px>** button to save the current style settings as a preset.
-   In the **Shapes** section the following settings can be specified:
    -   
        **Shape color**
        
        .

    -   
        **Transparency**
        
        .

    -   
        **Line color**
        
        .

    -   
        **Line width**
        
        .

    -   
        **Point color**
        
        . <small>(v0.22)</small> 

    -   
        **Point size**
        
        . <small>(v0.22)</small> 

    -   
        **Draw style**
        
        .

    -   
        **Display mode**
        
        .
-   The settings in the **Annotations** section apply to [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md). The following settings can be specified (see [Draft Text](Draft_Text#View.md) for details):
    -   
        **Text color**
        
        .

    -   
        **Font name**
        
        .

    -   
        **Font size**
        
        . This is in fact the default line height, the letters are smaller.

    -   
        **Line spacing**
        
        . Not used for dimensions.

    -   
        **Scale multiplier**
        
        . This is the inverse of the scale set in the [Draft annotation scale widget](Draft_annotation_scale_widget.md). If the scale is {{value|1:100}} the multiplier is {{Value|100}}. <small>(v0.22)</small> 
-   In the **Dimensions** section the following settings can be specified (see [Draft Dimension](Draft_Dimension#View.md) for details):
    -   
        **Line and arrow color**
        
        . <small>(v0.22)</small> 

    -   
        **Line width**
        
        . <small>(v0.22)</small> 

    -   
        **Arrow type**
        
        .

    -   
        **Arrow size**
        
        .

    -   
        **Show unit**
        
        .

    -   
        **Unit override**
        
        .

    -   
        **Dim overshoot**
        
        . <small>(v0.21)</small> 

    -   
        **Ext lines**
        
        . <small>(v0.21)</small> 

    -   
        **Ext overshoot**
        
        . <small>(v0.21)</small> 

    -   
        **Text spacing**
        
        .
-   Press the **<img src="images/Draft_SetStyle.svg" width=16px> Selected** button to apply the settings to selected objects or groups. Objects can be selected while the task panel is open.
-   Press the **<img src="images/Draft_Text.svg" width=16px> Annotations** button to apply the settings to all [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md) in the current document. <small>(v0.21)</small> 
-   Press the **Cancel** button to finish the command without saving the settings.

## Notes

-   The settings in the **Shapes** section, except **Draw style** and **Display mode**, are not only used for Draft objects, but also for objects created with other workbenches.
-   All settings, except **Draw style** and **Display mode**, can also be changed in the preferences. See [PartDesign Preferences](PartDesign_Preferences#Shape_appearance.md) and [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).
-   Styles are saved in a file with a fixed name: **StylePresets.json** which is stored in FreeCAD\'s user **Draft** folder:
    -   On Linux it is usually **/home/<username>/.local/share/FreeCAD/Draft/**.
    -   On Windows it is **%APPDATA%\FreeCAD\Draft\**, which is usually **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\**.
    -   On macOS it is usually **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/en
