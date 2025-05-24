<div class="undefined "><div class="problems_header_content__o_4YA"><div class="problems_header_content__title__L2cB2 g-mb-0"><h3 class="g-m-0">Count the number of possible triangles</h3><div style="padding-top: 2px;"><div class="sprint_sprint_popup_container__zCU0K"><i aria-hidden="true" class="bookmark outline icon"></i></div><div class="sprint_sprint_modal_container_mobile__09_Vr"><i aria-hidden="true" class="bookmark outline icon"></i></div></div></div><i id="bug_1" aria-hidden="true" class="bug icon"></i></div><div class="problems_header_description__t_8PB"><span>Difficulty: <strong>Medium</strong></span><span>Accuracy: <strong>28.53%</strong></span><span>Submissions: <strong>139K+</strong></span><span>Points: <strong>4</strong></span><span class="problems_label__MY7nU">Average Time: <strong>15m</strong></span></div><div class="ui divider"></div><div><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an integer array <strong>arr[]</strong>. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle.&nbsp;</span></p>
<blockquote>
<p><span style="font-size: 18px;">A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.</span></p>
</blockquote>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [4, 6, 3, 7]
<strong>Output</strong>: 3
<strong>Explanation</strong>: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.  <br></span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [10, 21, 22, 100, 101, 200, 300]
<strong>Output</strong>: 6
<strong>Explanation</strong>: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [1, 2, 3]
<strong>Output</strong>: 0
<strong>Explanation</strong>: No triangles are possible.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= arr.size() &lt;= 10<sup>3</sup></span><br><span style="font-size: 18px;">0 &lt;= arr[i] &lt;= 10</span><sup>5</sup></p></div></div>