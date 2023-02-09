score_dict = {"student": ["Tom", "Lisa", "Sarah"], "score": [80, 90, 95]}

# Iterating thru
[print(col) for (col, _) in score_dict.items()]

import pandas as pd

score_df = pd.DataFrame(score_dict)
print(score_df)

for (student, score) in score_df.items():
    print(student)
    print(score)

# loop through rows
for (i, row) in score_df.iterrows():
    print(row.student)
