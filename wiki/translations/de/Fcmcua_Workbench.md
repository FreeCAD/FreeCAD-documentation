# Fcmcua Workbench/de
<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="Fcmcua Workbench icon" src=images/Fcmcua_wb.svg  style="width:128" height="128px;">


</div>


{{TOCright}}



## Einleitung


<div lang="en" dir="ltr" class="mw-content-ltr">

Fcmcua is an [external workbench](External_workbenches.md) that is used to control an assembly created in [Assembly4 Workbench](Assembly4_Workbench.md) from an [OPC UA](wikipedia_OPC_Unified_Architecture.md) server. This provides functionality for simulating machines controlled by digital controllers such as [PLCs](wikipedia_Programmable_logic_controller.md), so long as the controller supports OPC UA. The workbench uses the values provided by the OPC UA server to manipulate the Attachment Offset of each part\'s Local Coordinate System (LCS).


</div>

## Installation

Fcmcua kann mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert werden.



## Anwendung


<div lang="en" dir="ltr" class="mw-content-ltr">

Fcmcua provides two types of mechanisms for simulating movement in a model: **Axis** and **Actuator**.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

An **axis** is controlled by [floating point](wikipedia:Floating-point_arithmetic.md) values that represent either the axis position or the speed of the motor that drives the axis.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

An **actuator** is any motion triggered by a binary signal. In that case Fcmcua itself simulates the motion by calculating the positional values needed for the simulation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

For further usage instructions see the [Fcmcua repository](https://github.com/heissgetraenk/fcmcua).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Connection


</div>

<img alt="" src=images/Fcmcua_wb.svg  style="width:64px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

A URL to the OPC UA server must be specified in the form of {{Incode|opc.tcp://127.0.0.1:4840}}.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Setting a polling rate may be used to limit the time between updates to the FreeCAD assembly.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The connection state is displayed on the connection panel.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Axis Settings 


</div>

<img alt="" src=images/Fcmcua_axes.svg  style="width:64px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

An axis node on the OPC UA server represents a one-dimensional change in the Attachment Offset of a part in the assembly. To configure this assignment the following information must be specified:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   **Node Id:** The address of the server node.
-   **Document Name:** The name of the part\'s document.
-   **LCS:** The label of the part\'s Local Coordinate System.
-   **Offset:** The vector component of the Attachment Offset that the node value will update.
-   **Type:** Speed axis or positional axis.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The value from the server can also be inverted or scaled by supplying a mathematical sign and/or factor.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Actuator Settings 


</div>

<img alt="" src=images/Fcmcua_actuator.svg  style="width:64px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

An actuator node on the OPC UA server acts as a trigger to *open* or *close* the actuator. To configure the actuator the following information must be specified:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   **Type:** Describes how many signals are used to open or close the actuator.
-   **Conditional Block:** An actuator may have a stop in its travel, activated by another binary signal. This feature is optional.
-   **Node Ids:** Depending on the configuration: the addresses of the nodes that trigger the opening/closing or the block of the actuator.
-   **Positions:** Depending on the configuration: the Attachment Offset values in the model that represent the open, close or block position of the actuator.
-   **Durations:** The timing with which the actuator opens or closes.


</div>



## Verweise


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [Fcmcua repository](https://github.com/heissgetraenk/fcmcua)
-   [External workbenches](External_workbenches.md)


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Fcmcua Workbench/de
