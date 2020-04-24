#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   exam-04.py
@Contact :   howq@outlook.com
@License :   MIT

@Modify Time      @Author    @Version    @Desc
------------      -------    --------    -----------
2020/4/23 16:33   howq       1.0         None
"""

import numpy as np

np_type = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['S1', 'i', 'i', 'i']
})

# .encode('utf-8')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
peoples = np.array(
    [
        ("张飞".encode('utf-8'), 66, 65, 30),
        ("关羽".encode('utf-8'), 95, 85, 98),
        ("赵云".encode('utf-8'), 93, 92, 96),
        ("黄忠".encode('utf-8'), 90, 88, 77),
        ("典韦".encode('utf-8'), 80, 90, 90)
    ]
    , dtype=np_type
)


chinese = peoples[:]['chinese']
english = peoples[:]['english']
math = peoples[:]['math']

print(np.mean(chinese))
print(np.mean(math))
print(np.mean(english))
