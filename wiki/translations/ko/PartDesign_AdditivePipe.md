---
 GuiCommand:
   Name: PartDesign AdditivePipe
   MenuLocation: 부품 설계 , 덧셈 도형특징 생성 , 파이프 추가
   Workbenches: PartDesign_Workbench/ko
   Version: 0.17
   SeeAlso: PartDesign_AdditiveLoft/ko, PartDesign_SubtractivePipe/ko
---

# PartDesign AdditivePipe/ko



## 설명

**파이프 추가**는 활성화된 몸통에서 열려 있거나 닫힌 경로를 따라 하나 이상의 스케치(단면이라고도 함)를 쓸어서 파이프 형태의 고체를 만듭니다. 몸통에 이미 도형특징이 있는 경우 파이프는 병합됩니다.

![](images/PartDesign_AdditivePipe_example.svg ) 
*왼쪽: 경로 (C)를 따라 쓸기할 단면 (A) 및 (B); 오른쪽: 생성된 파이프*



## 용법

위의 예시 이미지는 두 가지 다른 단면 모양을 보여줍니다. 아래 글에서는 단일 모양에 대해서만 절차를 설명하는데 이렇게 하면 전체 경로를 따라 동일한 단면을 갖는 부품이 생성됩니다.

1.  두 개의 별도 스케치를 만듭니다.
    -   하나는 경로용입니다. 예를 들어 위 이미지와 같이 곡선으로 연결된 두 개의 선이 경로가 됩니다.
    -   하나는 단면 모양을 위한 것입니다. 위 이미지의 첫 번째 모양은 원입니다. 스케치 대신 3D 개체의 면을 사용할 수도 있습니다. (<small>(v0.20)</small> )

2.  3D보기 에서 두 도형을 올바르게 **정렬**합니다. 단면의 원점을 경로 선에 배치하는 것이 좋습니다. 두 스케치는 대부분의 경우 **직교**해야 합니다. 이는 \'Map Mode\' 기능으로 수행할 수 있습니다.(**Space**를 사용하여 두 스케치를 모두 표시합니다. 단면 스케치를 선택합니다. Properties/DataTab/MapMode를 선택합니다. 오른쪽에 나타나는 **...** 버튼을 클릭합니다. 부착 대화 상자에서 경로 스케치의 꼭지점을 선택하고 올바른 모드를 선택하여 두 스케치가 올바르게 정렬되도록 합니다.)

3.  도구를 호출하는 방법에는 여러 가지가 있습니다.
    -   
        **<img src="images/PartDesign_AdditivePipe.svg" width=16px> 파이프 추가
**
        
        버튼을 누릅니다.

    -   메뉴에서 **부품설계 → 덧셈 도형특징 생성 → <img src="images/PartDesign_AdditivePipe.svg" width=16px> 파이프 추가** 를 선택합니다.

4.  도형특징 선택 대화상자에서 단면으로 사용할 스케치를 선택하고 **OK**버튼을 누릅니다.
    -   또는 도구를 시작하기 전에 3D 개체의 스케치 또는 면을 선택할 수 있습니다.(<small>(v0.20)</small> ) 이 경우에는 이 대화 상자가 표시되지 않습니다.

5.  쓸기할 경로 아래의 파이프 매개변수에서 **Object**버튼을 누릅니다.

6.  3D 보기에서 경로로 사용할 스케치를 선택합니다. 이 경우 전체 스케치가 경로로 사용됩니다.
    -   또는 **모서리 추가**를 누르고 3D 보기에서 모서리를 선택하여 스케치에 하나의 모서리를 선택할 수 있습니다. 각 가장자리에 대해 **모서리 추가**를 다시 눌러야 한다는 점에 유의하세요. 분기가 없는 연속되는 을 선택해야 합니다.

7.  대부분의 경우 다른 설정은 기본 설정과 함께 작동합니다.

8.  
    **확인**버튼을 누릅니다.

둘 이상의 단면을 사용하려면 위에서 설명한 대로 첫 번째 단면 스케치부터 시작합니다. 그런 다음 단면 변환에서 변환 모드를 다중 단으로 설정합니다; **단면 추가**를 누른 다음 [3D 보기에서](3D_view/ko.md) 스케치를 선택하세요. 각각의 추가 단면에 대해 반복합니다.



## 선택 사항 

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard

    :   This keeps the cross-section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by the first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvelinear equivalence** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of its length.
-   Binormal
    -   Specify binormal vector in X, Y and Z

**Corner Transition**

-   Transformed
-   Right
-   Rounded

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign AdditivePipe object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Add Sub Shape|PartShape|Hidden**:

-    **Base Feature|Link|Hidden**:

-    **_Body|LinkHidden|Hidden**:


{{TitleProperty|Part Design}}

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**: reference to sketch.

-    **Midplane|Bool**: extrude symmetrically to sketch face.

-    **Reversed|Bool**: reverses extrusion direction.

-    **Up To Face|LinkSub**: face where feature will end.

-    **Allow Multi Face|Bool**: allow multiple faces in profile.


{{TitleProperty|Sweep}}

-    **Sections|LinkSubList**: lists the sections used.

-    **Spine|LinkSub**: spine (path) to sweep along.

-    **Spine Tangent|Bool**: true or false (default). True extends the spine to include tangent edges.

-    **Auxiliary Spine|LinkSub|Hidden**: secondary spine (path) to orient the Sweep.

-    **Auxiliary Spine Tangent|Bool**: true or false (default). True extends the auxiliary spine to include tangent edges.

-    **Auxiliary Curvelinear|Bool**: true or false (default). True calculates the normal between equidistant points on both spines.

-    **Mode|Enumeration**: profile mode. Options are *Fixed*, *Frenet*, *Auxiliary* or *Binormal*. See [Options](#Options.md).

-    **Binormal|Vector**: binormal vector for corresponding orientation mode.

-    **Transition|Enumeration**: transition mode. Options are *Transformed*, *Right Corner* or *Round Corner*.

-    **Transformation|Enumeration**: *Constant* uses a single cross-section. *Multisection* uses two or more cross-sections. *Linear*, *S-shape* and *Interpolation* are currently not functional.

## Notes

-   To better control the shape of the pipe, it is recommended that all cross-sections have the same number of segments. For example, for a pipe between a rectangle and a circle, the circle should be broken down into 4 connected arcs.
-   You can pipe from or toward a single [vertex](Glossary#V.md) from a sketch or the body. <small>(v0.20)</small> 
-   When you select a [vertex](Glossary#V.md) as section, it must be the last section of the pipe. Otherwise the pipe body would consist of two solids connected at a single point. This would violates the CAD kernel\'s definition of a 3D object. You can change the order of the sections by dragging them in the list.
-   The path can only be from a single sketch, feature or ShapeBinder. In case you want to sweep along several edges from different sketches, use a [SubShapeBinder](PartDesign_SubShapeBinder.md).
-   The path must not contain branches or T-junctions etc. Loops are allowed.
-   It can lead to issues if the cross-section is not perpendicular to the path in 3D.
-   A cross-section cannot lie on the same plane as the one immediately preceding it.
-   The cross-sections must not contain disjoint or crossing loops.
-   If the sketch has inner geometry, then the order in which the sketch geometry is created should be the same for all sections. Either start all sections with the inner geometry, or start them all with the outer. Otherwise an invalid pipe will be created where inner and outer walls cross.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/ko
