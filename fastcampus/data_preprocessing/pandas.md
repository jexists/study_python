## pandas 사용 (데이터 프레임 생성)

→ `import pandas as pd`

```python
import pandas as pd

df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})

type(df) # pandas.core.frame.DataFrame

df
```


### 1. Dict 사용 데이터 프레임 생성

```python
use_dict = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}

df2 = pd.DataFrame(use_dict)

df2
```


### 2. List 사용 데이터 프레임 생성

→ column 이름 자동 생성 (나중에 변경해야함)

```python
use_list = [[1,4,7],[2,5,8],[3,6,9]]

df3 = pd.DataFrame(use_list)

df3
```


- column 이름 변경

```python
df3.columns=['a','b','c']

df3
```


### 빈값 넣기 (numpy)

→ `import numpy as np`

→ np.NaN

```python
import numpy as np

use_any_type = {'type': ['string','한국어',123], 'number':[700,10,5], 'test': ['hello',np.NaN, 'world']}

df5 = pd.DataFrame(use_any_type)

df5
```
