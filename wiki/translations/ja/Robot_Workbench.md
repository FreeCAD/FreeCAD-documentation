# Robot Workbench/ja
**The Robot Workbench is unmaintained. If you have experience with the topic and are interested in maintaining it, please state your intention in the developer's section of the [https://forum.freecadweb.org/index.php FreeCAD forum].

The reason this workbench is still in the master source code is because this workbench is programmed in C++. If this workbench could be programmed in Python, then it could be made an [external workbench](external_workbenches.md) and it could be moved to a separate repository.
**

## Introduction

<img alt="Robot workbench icon" src=images/Workbench_Robot.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

ロボットワークベンチは_。 以下の作業を行うことができます：

-   ロボット、加工物とシミュレーション環境のセットアップ
-   軌道の作成と書き込み
-   CAD部品形状を軌道に分解
-   ロボットの動作と到達可能範囲のシミュレート
-   ロボットプログラムファイルへの軌道のエクスポート


</div>

You can do the following tasks:

-   Set up a simulation environment with a robot and work pieces.
-   Create and fill up movement trajectories.
-   Decompose features of a CAD part to a trajectory.
-   Simulate the robot movement and reaching distance.
-   Export the trajectory to a robot program file.


<div class="mw-translate-fuzzy">

以下で例を見ることができます： _


</div>


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## ツール

ロボット設定を作成するのに使う主要なコマンドです。

### ロボット

6軸ロボットを作成、管理するためのツール


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Robot_CreateRobot.png  style="width:30px;"> [ロボットを作成](Robot_CreateRobot/jp.md): シーンに新しいロボットを挿入します
-   <img alt="" src=images/Robot_Simulate.png  style="width:30px;"> [軌道をシミュレート](Robot_Simulate/jp.md): シミュレーションダイアログを開き、シミュレートを行います
-   <img alt="" src=images/Robot_Export.png  style="width:30px;"> [軌道をエクスポート](Robot_Export/jp.md): ロボットプログラムファイルをエクスポートします
-   <img alt="" src=images/Robot_SetHomePos.png  style="width:30px;"> [定位置を設定](Robot_SetHomePos/jp.md): ロボットの定位置を設定します
-   <img alt="" src=images/Robot_RestoreHomePos.png  style="width:30px;"> [定位置に戻す](Robot_RestoreHomePos/jp.md): ロボットを定位置に動かします


</div>

### 軌道

軌道を作成し、操作するためのツールです。パラメトリックなものと非パラメトリックなものの二種類があります。


<div class="mw-translate-fuzzy">

#### 非パラメトリック

-   <img alt="" src=images/Robot_CreateTrajectory.png  style="width:30px;"> [軌道を作成](Robot_CreateTrajectory/jp.md): シーンに新しいロボットを挿入します
-   <img alt="" src=images/Robot_SetDefaultOrientation.png  style="width:30px;"> [デフォルトの方向を設定](Robot_SetDefaultOrientation/jp.md): デフォルトで作成される方位通過点を設定します
-   <img alt="" src=images/Robot_SetDefaultValues.png  style="width:30px;"> [デフォルトの速度パラメーターを設定](Robot_SetDefaultValues/jp.md): 通過点作成時に使用されるデフォルト値を設定します
-   <img alt="" src=images/Robot_InsertWaypoint.png  style="width:30px;"> [通過点を挿入](Robot_InsertWaypoint/jp.md): 現在のロボット位置から軌道に通過点を挿入します
-   <img alt="" src=images/Robot_InsertWaypointPre.png  style="width:30px;"> [通過点を挿入](Robot_InsertWaypointPre/jp.md): 現在のマウス位置から軌道に通過点を挿入します


</div>


<div class="mw-translate-fuzzy">

#### パラメトリック

-   <img alt="" src=images/Robot_Edge2Trac.png  style="width:30px;"> [エッジから軌道を作成](Robot_Edge2Trac/jp.md): エッジを軌道に分解した新しいオブジェクトを挿入します
-   <img alt="" src=images/Robot_TrajectoryDressUp.png  style="width:30px;"> [軌道をドレスアップ](Robot_TrajectoryDressUp/jp.md): 軌道の一つ以上のプロパティを上書きします
-   <img alt="" src=images/Robot_TrajectoryCompound.png  style="width:30px;"> [軌道を合成](Robot_TrajectoryCompound/jp.md): 複数の単一軌道を合成したものを作成します


</div>


<div class="mw-translate-fuzzy">

## スクリプト処理

このセクションは以下のスクリプトから生成されています： <http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Robot/RobotExample.py?view=markup> 必要であればこのファイルを直接使用することもできます。


</div>

See the [Robot API example](Robot_API_example.md) for a description of the functions used to model the robot displacements.

## チュートリアル

-   [Robot 6-Axis](Robot_6-Axis.md)
-   [VRMLのロボットシミュレーション準備](VRML_Preparation_for_Robot_Simulation.md)


<div class="mw-translate-fuzzy">


{{docnav|FEM Workbench|Standard Menu}}


{{docnav/jp|Drawing Workbench/jp|Raytracing Workbench/jp}}


</div>


{{Robot Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Robot Workbench/ja
