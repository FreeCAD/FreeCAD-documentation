# Part and PartDesign/ko
## 요약

<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [부품 작업대와](Part_Workbench/ko.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [부품설계 작업대의](PartDesign_Workbench/ko.md) 사용의 차이점과 그로 인한 결과에 대해 수년 동안 많은 논의가 있었습니다.

사용자가 하나에 익숙해질 때까지 둘 중 하나를 사용하고 다른 하나를 배우는 것이 좋습니다. 또한 일반적으로 새로운 사용자는 두 작업의 서로 다른 결과를 이해할 때까지 혼합하지 않는 것이 좋습니다.

이 차이점과 결과에 대해 이야기해 봅시다.



## 부품 작업대의 개념 

부품 작업대에서는 기본적으로 [CSG 스타일 모델링방법으로](Constructive_solid_geometry/ko.md) 작업 합니다. 연산자는 다양한 기본 입체도형들을 결합하여 원하는 모양을 표현합니다. (실제로는 부품 작업대에서는 기본 입체도형보다 한 단계 더 나아가 작업자가 스케치+돌출 작업(또는 스케치+회전, 로프트, 스윕\...)을 사용하여 임의의 모양을 만들 수도 있습니다.) 각각의 기본 입체도형 또는 형상이 생성되면 생성된 다른 객체(스케치 및 해당 부착 제외)와 관계가 없으며 독립적인 고체가 됩니다.

![centre\|독립적인 고체들](images/Part_CSG_Prims.png )

이 독립적인 상태는 연산자가 일부 연산을 사용하여 두 값을 결합할 때까지(일반적으로 두 값을 더하거나 빼는 부울 연산) 그대로 유지됩니다. 부울 연산 이후에는 새로운 고체가 생성되며 각각의 처음의 고체는 여전히 개별적으로 접근이 가능합니다.

여기서 핵심은 각각은 모두 단일한 독립적 고체라는 점과 그것들을 결합한다는 점입니다.



## 부품설계 작업대의 개념 

부품설계 작업대에서 [몸통(Body)은](PartDesign_Body/ko.md) 단일한 누적 고체로 직접 구성됩니다.

몸통의 첫 번째 단계는 덧셈적 기본입체도형 요소, 스케치의 돌출 또는 가져온 모양(기본 [특징이라고](Feature/ko.md) 함)의 재료 덩어리 이어야 합니다.

이 초기 재료 덩어리는 원하는 최종 형상(고체)이 만들어질 때까지 순차적으로 변경됩니다.

각 작업이 재료를 추가하거나 제거하며 순차적으로 모양을 형성해 나간다는 의미에서 누적된다고 합니다.

기본적으로 몸통의 \"끝단(Tip)\"은 - 특정 특징의 시각화에 자발적인 변경이 없는 한 - 몸통에 가장 마지막에 누적된 형상 변경 작업입니다. 이 끝단은 몸통의 현재 상태이고 가시적며, 새로운 특징의 추가 작업에 의해 다시 변경될 준비가 된 상태입니다.

Any function under the body represents the cumulative shape of the solid from the 1st feature to the feature considered.

따라서 **완전한 고체**를 갖기 위해서는 한편으로는 끝단 특징이 고체 구성의 마지막 단계여야 하고 다른 한편으로는 **선택해야 하는 것은 몸통**이며, 구성 단계가 아닙니다.

이렇게 하면 수정 시 **항상 고체의 마지막 버전을 표시**할 수 있습니다.


<div class="mw-translate-fuzzy">

**참고 및 추가 사항:** At each time of the construction, the last function used is the \"Tip\", which can be defined too as \"active stage in the construction of the object\" or \"stage preceding the next action in the construction of the object\". When the object\'s drawing is complete, Tip is naturally the last stage or feature of the construction. But if desired, in case of forgetting, any feature of the construction can be provisionally declared as Tip: it then becomes the step preceding the next action in the construction of the object, which means that new feature(s) can be inserted anywhere in the construction, **on condition not to create any incompatible with the suite**.


</div>

모든 작업이 완료되면 마지막 특징을 다시 끝단으로 설정해야 합니다.

![centre\|특징들이 누적된 몸통 고체](images/Part_Design_Cumulativ.png )

이 그림은 몸통을 보여줍니다. 패딩된 스케치와 원뿔 도형이라는 특징들이 누적 작업된 고체입니다. 이것은 한 덩어리의 단일한 연속된 고체입니다.

끝단이 **Pad**인 경우 패드는 별도로 존재할 수 있지만, 끝단이 **Cone**인 경우 원뿔은 별도로 존재할 수 없습니다(원뿔은 패드 위에 누적되어야 합니다.Tip on cone = pad + cone).

(자주 언급되는 또 다른 사항은 몸통은 ***반드시***\' 단일한 연속된 고체여야 한다는 것입니다.이는 몸통의 특징에 의해 생성된 모든 geometry가 이전 geometry와 \'닿아야\' 함을 의미합니다.)



## 차이점과 그에 따른 결과 

초보자에게는 권장되지 않지만, 위에서 설명한 두 작업대의 목적과 차이점을 알고 있다면 부품 작업대와 부품설계 작업대의 도구를 결합할 수 있습니다. 예를 들어 :

사람들은 종종 부품 작업대의 불리언 연산을 위해 몸통 자체가 아닌 몸통의 일부 도형특징을 선택하려 할 때 문제가 발생합니다. 이것은 선택된 도형특징이 완전한 고체를 대표하지 않기 때문에 문제가 됩니다.

어떤 면에서는 부품 작업대 관점에서 몸통은 또 다른 기본 입체도형입니다. 따라서 몸통과 부품 작업대 객체를 사용하여 불리언 연산을 수행하는 것은 유효합니다. 하지만 결과 객체는 부품 작업대 객체가 됩니다. 따라서 부품설계 작업대 도구는 더 이상 이를 사용할 수 없습니다.

그리고 상황은 더욱 복잡해질 수 있습니다. 새로운 몸통을 생성하고 이전 단락에서 나온 결과를 그 안으로 끌어오면 BaseObject가 생성됩니다. 그런 다음 부품설계 작업대 도구를 사용할 수 있습니다.



## 주의사항

몸통(Body)에서 단일 고체를 나타내는 끝단(Tip)과 관련하여 주의할 점이 있습니다. *만약* 끝단이 뺄셈적 도형특징(예: 포켓)이고 이를 대칭복사와 같은 변환 작업에서 사용하는 경우, 대칭복사 작업은 특징들이 누적된 몸통 전체가 아니라 끝단의 도형특징에만 적용됩니다. 따라서 누적 고체가 아니라 뺄셈적 특징만 대칭복사 됩니다. 그리고 이 결과는 단일 고체를 만들어야 합니다.(대칭복사된 특징이 기존의 누적된 몸통과 이어져야만 합니다.)

이 예에서, 끝단(즉, 슬롯의 포켓)을 기준 평면 이나 고체의 면을 기준으로 대칭복사하면 전체 모델의 고체를 대칭복사 하지 않습니다. (실제로는, 트리에서 대칭 복사된 도형특징이 추가됩니다.)

![centre\|몸통의 끝단-마지막 도형특징(포켓)](images/PhantomMirror.png )

이 예에서는 끝단(슬롯의 포켓)이 기준 평면을 기준으로 대칭복사 됩니다.

![centre\|대칭복사된 뺄셈적 도형특징](images/MirroredSlot.png )

자세한 내용은 <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [부품설계의 대칭복사](PartDesign_Mirrored/ko.md) 페이지를 참조하세요.



## 비교

아래에서 각각의 작업대를 사용하여 구성된 동일한 예제를 볼 수 있습니다. 물론, 각 작업대마다 여러 가지 가능한 구성 방법이 있습니다. ![부품 작업대와 부품설계 작업대의 구성 방법 비교](images/PartWBvsPartDesignWBexample.jpg )

+++
| <img alt="" src=images/Workbench_PartDesign.svg  style="width:48px;"> 부품설계 작업대                                                                               | <img alt="" src=images/Workbench_Part.svg  style="width:48px;"> 부품 작업대                                                                                                                                                                                              |
+====================================================================================================================================================================+===================================================================================================================================================================================================================================================================+
| 01- <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> 몸통 생성 \> <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> XZ 평면에 스케치 생성 | 01- <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> 스케치 작업대로 전환 \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> XZ 평면에 스케치 생성 \> <img alt="" src=images/Workbench_Part.svg  style="width:24px;">부품 작업대로 전환 |
+++
| ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                   | ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )                                                                                                                                                                                    |
+++
|                                                                                                                                                                    |                                                                                                                                                                                                                                                                   |
+++

+++
| 02- <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> Z축 중심으로 회전 | 02- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Z축 중심으로 회전       |
+++
| ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )       | ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg ) |
+++
|                                                                                              |                                                                                  |
+++

+++
| 03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> XY 평면에 새 스케치 | 03- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> 스케치 작업대로 전환 \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> XY 평면에 새 스케치 \> \> <img alt="" src=images/Workbench_Part.svg  style="width:24px;">부품 작업대로 전환 |
+++
| ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )         | ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                                                                                                                                                                                   |
+++
|                                                                                          |                                                                                                                                                                                                                                                                    |
+++

+++
| 04- <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> 포켙      | 04a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> 아래로 돌출          |
+++
| ![](images/04pocket_PartWBvsPartDesignWBn.jpg ) | ![](images/04aExtrude_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                                |
+++

+++
|                                                                              | 04b- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> 잘라내기             |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/04bCut_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                        |
+++

+++
| 05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> XZ 평면에 새 스케치 | 05- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> 스케치 작업대로 전환 \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> XZ 평면에 새 스케치 \> <img alt="" src=images/Workbench_Part.svg  style="width:24px;">부품 작업대로 전환 |
+++
| ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )           | ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )                                                                                                                                                                                |
+++
|                                                                                          |                                                                                                                                                                                                                                                                 |
+++

+++
| 06- <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> XZ평면 기준 대칭 패드 | 06a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> XZ평면 기준 대칭 돌출 |
+++
| ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )     | ![](images/06aExtrude_PartWBvsPartDesignWB.jpg )  |
+++
|                                                                                    |                                                                                 |
+++

+++
|                                                                              | 06b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> 설계제도 작업대로 전환 \> <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> 원호형 복사 \> <img alt="" src=images/Workbench_Part.svg  style="width:24px;">부품 작업대로 전환 |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )                                                                                                                                               |
+++
|                                                                              |                                                                                                                                                                                                                                                  |
+++

Translations:Part and PartDesign/49/ko

+++
|                                                                              | 06c- <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> 결합(합집합)             |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/06cFusion_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                              |
+++

+++
| 07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> 기본 면 위에 새 스케치      | 07- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> 스케치 작업대로 전환 \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> XZ평면에 새 스케치 \> <img alt="" src=images/Workbench_Part.svg  style="width:24px;">부품 작업대로 전환 |
+++
| ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg ) | ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )                                                                                                                                                                               |
+++
|                                                                                                  |                                                                                                                                                                                                                                                                |
+++

+++
| 08- <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> 구명 - 카운터보어               | 08a- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> 회전                 |
+++
| ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg ) | ![](images/08aRevolve_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                                |                                                                                |
+++

+++
|                                                                              | 08b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> 설계제도 작업대로 전환 \> <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> 원호형 복사 \> <img alt="" src=images/Workbench_Part.svg  style="width:24px;">부품 작업대로 전환 |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )                                                                                                                                               |
+++
|                                                                              |                                                                                                                                                                                                                                                  |
+++

+++
| 09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> 구멍과 패드를 원형복사      | 09- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> 잘라내기(차집합)    |
+++
| ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg ) | ![](images/09Cut_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                                            |                                                                      |
+++

두 작업대의 구성 트리와 해당 구성 및 읽기 타임라인을 비교하세요.

+++
| 10- 부품설계 작업대의 구성 트리                                                    | 10- 부품 작업대의 구성 트리                                            |
+++
| ![](images/PartvsPartDesign_TreePartDesignWB.jpg ) | ![](images/PartvsPartDesign_TreePartWB.jpg ) |
+++
|                                                                                    |                                                                        |
+++



## 결론

부품 작업대와 부품설계 작업대는 약간의 주의를 기울여 함께 사용하면 매우 복잡한 모형을 만들 수 있습니다.

[맨 위로](#Top.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Part](Part_Workbench.md) > Part and PartDesign/ko
