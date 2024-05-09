import streamlit as st
import pandas as pd
import base64

# CSVデータの作成（仮のデータ）
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Location': ['Tokyo', 'Osaka', 'Kyoto']}
df = pd.DataFrame(data)

# CSVファイルをストリーミングしてダウンロード
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV</a>'
st.markdown(href, unsafe_allow_html=True)

# 表の表示
st.write(df)
