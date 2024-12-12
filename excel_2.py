import pandas as pd

# 엑셀 파일 경로를 지정
xlsx = pd.read_excel('./c:/사용자/khk/ldeaProjects/pandas/io/excel/excel2.xlsx')  # 경로 수정

# 엑셀 파일 읽기
df = pd.read_excel(xlsx)

df = pd.read_excel(xlsx, sheet_name='Sheet2')
inputs = []

for index, row in df.iterrows():
    for col_name, value in row.items():
        inputs.append(value)
        break

ll = str(inputs[0]).strip()

if ll == "서울":
    print('서울')
else :
    print('경기')





