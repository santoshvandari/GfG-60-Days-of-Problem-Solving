<div class="undefined "><div class="problems_header_content__o_4YA"><div class="problems_header_content__title__L2cB2 g-mb-0"><h3 class="g-m-0">Subarrays with sum K</h3><div style="padding-top: 2px;"><div class="sprint_sprint_popup_container__zCU0K"><i aria-hidden="true" class="bookmark outline icon"></i></div><div class="sprint_sprint_modal_container_mobile__09_Vr"><i aria-hidden="true" class="bookmark outline icon"></i></div></div></div><i id="bug_1" aria-hidden="true" class="bug icon"></i></div><div class="problems_header_description__t_8PB"><span>Difficulty: <strong>Medium</strong></span><span>Accuracy: <strong>49.74%</strong></span><span>Submissions: <strong>75K+</strong></span><span>Points: <strong>4</strong></span></div><div class="ui divider"></div><div><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number <strong>k</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong><strong> </strong>arr = [10, 2, -2, -20, 10], k = -10
<strong>Output:</strong> 3
<strong>Explaination:</strong> Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr = [9, 4, 20, 3, 10, 5], k = 33
<strong>Output:</strong> 2
<strong>Explaination:</strong> Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [1, 3, 5], k = 0<br></span><span style="font-size: 14pt;"><strong>Output:</strong> 0
<strong>Explaination: </strong>No subarray with 0 sum.</span></pre>
<p><strong style="font-size: 14pt; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Constraints:</strong></p>
<ul>
<li><span style="font-size: 14pt;">1 ≤ arr.size() ≤ 10<sup>5</sup></span></li>
<li><span style="font-size: 14pt;">-10<sup>3</sup> ≤ arr[i] ≤ 10<sup>3</sup></span></li>
<li><span style="font-size: 14pt;">-10<sup>7</sup>&nbsp;≤ k&nbsp;≤ 10<sup>7</sup></span></li>
</ul></div></div>