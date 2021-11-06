import pandas as pd

# 読み込むExcelファイルを格納する。
file_name_list = [
    'sampleA.xlsx',
    'sampleB.xlsx',
]

dict = {}

for file_name in file_name_list:
    # read_excel参考 : https://note.nkmk.me/python-pandas-read-excel/
    df = pd.read_excel(file_name)
    for sample_name in df:
        # 試料名が初めて現れる場合
        # get参考 : https://note.nkmk.me/python-dict-get/
        if dict.get(sample_name) is None:
            # values参考 : https://note.nkmk.me/python-pandas-dataframe-values-columns-index/
            # tolist参考 : https://note.nkmk.me/python-numpy-list/
            dict[sample_name] = df[sample_name].values.tolist()
        # 一度試料名が出てきた場合
        else:
            # values参考 : https://note.nkmk.me/python-pandas-dataframe-values-columns-index/
            # tolist参考 : https://note.nkmk.me/python-numpy-list/
            # +=参考 : https://it-biz.online/python/assignment-operator/
            dict[sample_name] += df[sample_name].values.tolist()

# 参考 : https://qiita.com/ShoheiKojima/items/30ee0925472b7b3e5d5c
d2 = {}
for k, v in dict.items():
    d2[k] = pd.Series(v)
result = pd.DataFrame(d2)

print(result)
# to_csv参考 : https://note.nkmk.me/python-pandas-to-csv/
result.to_csv('output.csv')
