---
 TutorialInfo:
   Topic: Example Combined Footing
   Level: Intermediate
   Time: 
   Author: Shiv Charan
   FCVersion: 0.20
   Files: 
---

# Example Combined Footing/de







## Beschreibung

The [Footing Reinforcement](Arch_Rebar_Footing_Reinforcement.md) tool allows the user to create reinforcing bars inside a Footing [Arch Structure](Arch_Structure.md) object.

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

In this example we will create Combined Footing Reinforcement as shown in below figure.

![](images/Combined_Footing_reinforcement.png ) 
*A Example of Combined Footing reinforcement in Footing [Arch Structure](Arch_Structure.md)*

![](images/Side_view_of_combined_footing_of_footing_reinforcement.png ) 
*Right view of given Footing Reinforcement example*

![](images/Combined_footing_front_view_.png ) 
*Front view of given Footing Reinforcement example*



## Anwendung

1\. Select vertical face of a previously created Footing **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object. as shown in below image.

![](images/FootingSelectedFace.png ) 
*Selected face for Footing Arch Structure*

2\. Then select **[Footing Reinforcement](Arch_Rebar_Footing_Reinforcement.md)** from the rebar tools.

3\. A footing reinforcement dialog box will pop-out on screen as shown below.

![](images/Footing_Reinforcement_GUI_.png ) 
*Dialog Box for the Footing Reinforcement*

4\. Select the desired rebar type and other input data for rebars in parallel direction of selected face in footing reinforcement mesh as show in below image.

5\. Now click on Next button or select Cross Rebars in list view and desired data for input data for rebars in cross direction of selected face in footing reinforcement mesh as show in below image.

6\. click next or click on Columns in list view and fill desired input for columns in footing reinforcement. Here you can select to add secondary rebars in columns or not.

7\. click next or click on Ties in list view and fill desired input for Ties in columns of footing reinforcement.

8\. click next or click on Main rebars in list view and fill desired input for main rebars in columns of footing reinforcement.

Only if secondary rebars check is enable then:

9\. click next or click on XDir Secondary rebar in list view and fill desired input for secondary rebars in X direction in a column in footing reinforcement.

10\. click next or click on YDir Secondary rebar in list view and fill desired input for secondary rebars in Y direction in a column in footing reinforcement.

11\. Click **OK** or **Apply** or **Finish** to generate Footing reinforcement.

12\. Click **Cancel** to exit the dialog box.



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Category_Arch.md) > Example Combined Footing/de
