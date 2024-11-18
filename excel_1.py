import pandas as pd

# 엑셀 파일 경로를 지정
file_path = 'C:/Users/khk/바탕화면/일자리 창출 확인서_1.xlsx'  # 경로 수정

# 엑셀 파일 읽기
df = pd.read_excel(file_path)

df = pd.read_excel(file_path, sheet_name='Sheet2')
row_data = df.iloc[3]
filtered_values = row_data[(row_data >= 15) & (row_data <= 34)]

print(filtered_values.xlsx)




