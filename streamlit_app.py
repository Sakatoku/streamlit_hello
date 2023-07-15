import streamlit as st

st.write('Hello world!')

# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('st.write')

# # Example 1

st.write('Hello, *World!* :sunglasses:')

# # Example 2

# st.write(1234)

# # Example 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4

# st.write('Below is a DataFrame:', df)

# # Example 5

# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# # ランダムなデータを挿入したデータフレームを生成する(3次元の点×200点)
# df_random = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
# # AltairでChartを生成する
# c = alt.Chart(df_random).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# # 生成したChartを表示
# st.write('Chart:', c)

# df1 = pd.read_csv('japan.csv')
# df2 = pd.read_csv('thailand.csv')
# df3 = pd.read_csv('vietnam.csv')
# # 3つのDataframeについてそれぞれM列とF列を足す
# df1['Country'] = 'Japan'
# df1['Population'] = df1['M'] + df1['F']
# df1 = df1.drop(['M', 'F'], axis='columns')
# df2['Country'] = 'Thailand'
# df2['Population'] = df2['M'] + df2['F']
# df2 = df2.drop(['M', 'F'], axis='columns')
# df3['Country'] = 'Vietnam'
# df3['Population'] = df3['M'] + df3['F']
# df3 = df3.drop(['M', 'F'], axis='columns')
# df_union = pd.concat([df1, df2, df3])
# df_union
# st.write(alt.Chart(df_union).mark_line().encode(x=alt.X('Age', sort=None), y='Population:Q', color='Country:N'))

