# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:41:09 2019

@author: adnan
"""

import pandas as pd
"""
        MERGE
"""

student = ['rahim','korim','jobbar','lyla','sony']
score = ['43','76','87','45','79']
subject = ['math','english']
df1 = pd.DataFrame({'student':student, 'subject':subject[0], 'score':score})
df1

student = ['rahim','mokles','kuddus','lyla']
total_score = ['54','86','57','83']
subject = ['english']
df2 = pd.DataFrame({'student':student, 'subject':subject[0], 'score':total_score})
df2

#inner merge
inner_merge = df1.merge(df2, on='student', how='inner')

#left merge
left_merge = df1.merge(df2, on='student', how='left')

#right merge
right_merge = df1.merge(df2, on='student', how='right')

#outer merge
outer_merge = df1.merge(df2, on='student', how='outer')


"""
        JOIN
"""

player = ['player1','player2','player3']
point = [8,9,6]
game = ['game1','game2','game3']
df3 = pd.DataFrame({'player':player,'points':point,'game':game}, index=['l1','l2','l3'])
df3

player = ['player1','player5','player6']
power = ['kick','elbow','stamina']
game = ['game1','game4','game5']
df4 = pd.DataFrame({'players':player,'power':power,'games':game}, index=['l1','l4','l5'])
df4

#inner join
inner_join = df3.join(df4, how='inner')

#left join
left_join = df3.join(df4, how='left')

#right join
right_join = df3.join(df4, how='right')

#outer join
outer_join = df3.join(df4, how='outer')

"""
        CONCATENATE
"""

concate = pd.concat([df3,df4], sort=False)       