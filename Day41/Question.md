<div class="undefined "><div class="problems_header_content__o_4YA"><div class="problems_header_content__title__L2cB2 g-mb-0"><h3 class="g-m-0">Set Matrix Zeroes</h3><div style="padding-top: 2px;"><div class="sprint_sprint_popup_container__zCU0K"><i aria-hidden="true" class="bookmark outline icon"></i></div><div class="sprint_sprint_modal_container_mobile__09_Vr"><i aria-hidden="true" class="bookmark outline icon"></i></div></div></div><i id="bug_1" aria-hidden="true" class="bug icon"></i></div><div class="problems_header_description__t_8PB"><span>Difficulty: <strong>Medium</strong></span><span>Accuracy: <strong>52.54%</strong></span><span>Submissions: <strong>37K+</strong></span><span>Points: <strong>4</strong></span></div><div class="ui divider"></div><div><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given a 2D matrix <strong>mat</strong>[][] of size </span><span style="font-size: 18px;"><strong>n×m</strong>.&nbsp;</span><span style="font-size: 18px;">The task is to modify the matrix such that if <strong>mat[i][j]</strong> is 0, all the elements in the&nbsp;</span><span style="font-size: 18px;"><strong>i</strong>-th row and </span><span style="font-size: 18px;"><strong>j</strong>-th column are set to 0 </span><span style="font-size: 18px;">and do it in <strong>constant space complexity</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">mat[][] = [[1, -1, 1],
                [-1, 0, 1],
                [1, -1, 1]]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [[1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]]
</span><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;"> </span></span><span style="font-size: 18px;">mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.</span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">mat[][] = [[0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [[0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]]
</span><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;"> </span></span><span style="font-size: 18px;">mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n, </span><span style="font-size: 18px;">m</span><span style="font-size: 18px;"> ≤ 500</span><sup><br></sup><span style="font-size: 18px;">- 2<sup>31</sup> ≤ mat[i][j] ≤ 2<sup>31</sup> - 1</span></p></div></div>