---
- GuiCommand:
   Name:Draft SetStyle
   MenuLocation:Utilities - Set style
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**S** **S**
   Version:0.19
   SeeAlso:[Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md), [Draft ApplyStyle](Draft_ApplyStyle.md)
---

# Draft SetStyle/pl

## Description

The <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft SetStyle** command sets the default style for new objects.

<img alt="" src=images/Draft_SetStyle_Taskpanel.png  style="width:" height="550px;"> 
*The Style settings task panel*

## Usage

1.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_style.png ) button in the [Draft Tray](Draft_Tray.md). Depending on the current style settings this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style** option from the menu.
    -   Use the keyboard shortcut: **S** then **S**. <small>(v0.20)</small> 
2.  The **Style settings** task panel opens. See [Options](#Options.md) for more information.
3.  Optionally change one or more settings.
4.  Press the **OK** button to save the settings.
5.  The button in the [Draft Tray](Draft_Tray.md) is updated.

## Options

-   From the dropdown list at the top of the task panel an exiting style preset can be selected. <small>(v0.20)</small> 
-   Press the **<img src="images/Document-save.svg" width=16px> Save style** button to save the style settings as a preset. <small>(v0.20)</small> 
-   In the **Lines and faces** section the following settings can be specified:
    -   
        **Line color**
        
        . This is also used for annotations (<small>(v0.21)</small> ) and for the **Point Color** of objects.

    -   
        **Line width**
        
        . This is also used for annotations (<small>(v0.21)</small> ) and for the **Point Size** of objects.

    -   
        **Draw style**
        
        .

    -   
        **Display mode**
        
        .

    -   
        **Shape color**
        
        .

    -   
        **Transparency**
        
        .
-   The settings in the **Annotations** section apply to [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md). The following settings can be specified (see [Draft Text](Draft_Text#View.md) for details):
    -   
        **Text font**
        
        .

    -   
        **Text size**
        
        . This is in fact the default line height, the letters are smaller.

    -   
        **Text color**
        
        .

    -   
        **Line spacing**
        
        . Not used for dimensions. <small>(v0.20)</small> 
-   In the **Dimensions** section the following settings can be specified (see [Draft Dimension](Draft_Dimension#View.md) for details):
    -   
        **Arrow style**
        
        .

    -   
        **Arrow size**
        
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
        
        . <small>(v0.20)</small> 

    -   
        **Show units**
        
        .

    -   
        **Unit override**
        
        .
-   Press the **<img src="images/Draft_SetStyle.svg" width=16px> Selected** button to apply the settings to selected objects or groups. Objects can be selected while the task panel is open. <small>(v0.20)</small> 
-   Press the **<img src="images/Draft_Text.svg" width=16px> Annotations** button to apply the settings to all [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md) in the current document. <small>(v0.21)</small> 
-   Press the **Cancel** button to finish the command without saving the settings.

## Notes

-   The **Line color**, **Line width**, **Shape color** and **Transparency** settings are not only used for Draft objects, but also for objects created with other workbenches.
-   Styles are saved in a file with a fixed name: **StylePresets.json** which is stored in FreeCAD\'s user **Draft** folder:
    -   On Linux it is usually **/home/<username>/.local/share/FreeCAD/Draft/** (<small>(v0.20)</small> ) or **/home/<username>/.FreeCAD/Draft/** ({{VersionMinus|0.19}}).
    -   On Windows it is **%APPDATA%\FreeCAD\Draft\**, which is usually **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\**.
    -   On macOS it is usually **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

The following preferences are involved:

-   Line color: **Edit → Preferences... → Part/Part Design → Shape appearance → Default Shape view properties → Line color** and **Vertex color**.
-   Line width: **Edit → Preferences... → Part/Part Design → Shape appearance → Default Shape view properties → Line width** and **Vertex size**.
-   Draw style: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → DefaultDrawStyle**.
-   Display mode: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → DefaultDisplayMode**.
-   Shape color: **Edit → Preferences... → Part/Part Design → Shape appearance → Default Shape view properties → Shape color**.
-   Transparency: **Edit → Preferences... → Part/Part Design → Shape appearance → Default Shape view properties → Shape transparency**.
-   Text font: **Edit → Preferences... → Draft → Texts and dimensions → Text settings → Font family**.
-   Text size: **Edit → Preferences... → Draft → Texts and dimensions → Text settings → Font size**.
-   Text color: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → DefaultTextColor**.
-   Line spacing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → LineSpacing**.
-   Arrow style: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Arrow style**.
-   Arrow size: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Arrow size**.
-   Dim overshoot: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Dimension line overshoot**.
-   Ext lines: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Extension lines size**.
-   Ext overshoot: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Extension line overshoot**.
-   Text spacing: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Text spacing**.
-   Show units: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Show the unit suffix in dimensions**.
-   Unit override: **Edit → Preferences... → Draft → Texts and dimensions → Dimension settings → Override unit**.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/pl
