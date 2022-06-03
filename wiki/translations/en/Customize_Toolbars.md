# Customize Toolbars/en
{{TutorialInfo|Topic=SampleTopic|Level=Beginner|Time=5 minutes|Author=[Mario52](User_Mario52.md)|FCVersion=All}}

## Synopsis

This tutorial shows you the customization of toolbars. Tools (inclusive Macro-tools) can be used in different workbenches. In an example a Macro becomes a Macro-tool by creation of a **Menu text**, a **Tool tip** and an **Icon**. Afterwards this Macro-tool becomes part of an extra toolbar in a workbench.

## Usage

**1.** Find the Customize Menu

-   Click **Main Menu → Tools → Customize**,

<img alt="Customize" src=images/CustomizeToolBar_01.png  style="width   *640px;"> 

-   or right click on any toolbar.

<img alt="Right mouse click" src=images/CustomizeToolBar_02.png  style="width   *640px;"> 

-   The Customize window appears.

<img alt="The Customize window appears" src=images/CustomizeToolBar_03.png  style="width   *640px;"> 

**2.** Make a Macro to a Macro-Tool

-   Select the \"Macro\" tab.

-   To add an icon for the provided macro click the Pixmap button (labelled **... **).

<img alt="Select a toolbar" src=images/CustomizeToolBar_04.png  style="width   *640px;"> 

-   Search for an appropriate icon from amongst FreeCAD\'s existing icons,


<div class="mw-collapsible mw-collapsed toccolours">

      \[or add your own icon by clicking **Add icons...**\].                  (expand for an example)


<div class="mw-collapsible-content">

<img alt="Add icon" src=images/CustomizeToolBar_05.png  style="width   *640px;"> 

     \[You will get a file selection window, select your custom image file (PNG format, 64x64 pixels)\]

<img alt="Get a file" src=images/CustomizeToolBar_06.png  style="width   *640px;"> 


</div>


</div>

-   Select your icon and click **OK**.

<img alt="Select your icon" src=images/CustomizeToolBar_07.png  style="width   *640px;"> 

-   The icon you selected is now displayed next to the Pixmap button labelled **...**.

<img alt="Your icon is displayed" src=images/CustomizeToolBar_08.png  style="width   *640px;"> 

-   Select the provided macro in line **Macro   *** and specify a **Menu text**   * (which will appear as the text label in the menu); also fill in the *\'Tool Tip\'   ** (which is the text that will appear when a mouse is over the button on the toolbar); further lines are optional.

-   Click the button **Add**.

<img alt="Click the button" src=images/CustomizeToolBar_09.png  style="width   *640px;"> 

-   The button of the macro-tool is now created.

<img alt="Your button is created" src=images/CustomizeToolBar_10.png  style="width   *640px;"> 

**3.** Create a toolbar outside the workbench **Macro** which contains the created **Macro-tool**

-   Select the **Toolbars** tab and choose the workbench (for which the toolbar is provided) in the drop down on the right (**Part** in this example).

     \[Since version 0.15 there is a  **[<img src=images/Freecad.svg style="width   *16px"> Global**  toolbar. If this is selected, the provided toolbar will be in each workbench.\]

<img alt="Toolbars tab" src=images/CustomizeToolBar_11.png  style="width   *640px;"> 

-   In the dropdown on the left select **Macros**.

<img alt="Macros" src=images/CustomizeToolBar_12.png  style="width   *640px;"> 

-   The macro-tool with its icon appears in the list.

<img alt="Your icon is listed" src=images/CustomizeToolBar_13.png  style="width   *640px;"> 

-   Click the button **New...**

<img alt="Click on \"New\"" src=images/CustomizeToolBar_14.png  style="width   *640px;"> 

-   In the window \"New Toolbar\" enter the name of the provided extra toolbar for the **Part** Workbench and click **OK**

<img alt="Enter the name for your toolbar" src=images/CustomizeToolBar_15.png  style="width   *640px;"> 

-   The toolbar is now created.

-   To add the created macro-tool to this toolbar, select it in the left window and then click the **Button** with the arrow pointing right.

<img alt="Select your macro" src=images/CustomizeToolBar_16.png  style="width   *640px;"> 

-   You have created now a toolbar called \"Camera\" (with the Macro-tool **Camera** in it)

-   Click the **Close** button.

<img alt="Close" src=images/CustomizeToolBar_17.png  style="width   *640px;"> 

-   Your new toolbar is now contained in the toolbars\' right-click menu. Its Icons (in our example only the camera) are visible, if the toolbar is activated (blue checkmark).

<img alt="New Toolbar" src=images/CustomizeToolBar_18.png  style="width   *640px;"> 

## Notes

See also [Interface Customization](Interface_Customization.md).



[Category   *Preferences](Category_Preferences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > Customize Toolbars/en
