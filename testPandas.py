import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# data https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data


# 表示桁数を2桁に設定
pd.set_option('precision', 2)

# usecolsで読み込む列番号を指定する
df = pd.read_csv('abalone.data', names=('性別', '殻長', '殻幅',  '高さ',  '重さ',  '年輪'), usecols = [0, 1, 2, 3, 4, 8])

# データのスキーマ情報を表示する
print(df.dtypes)

# 年齢（年輪＋1.5）列を追加
df['年齢'] = df['年輪'] + 1.5
print(df.head())

# 列名を指定して抽出
df2 = df.loc[:, ['殻長', '殻幅',  '高さ']]
print(df2.head())

# 統計情報を表示
print(df2.describe())

################## 前処理 ##################

# 性別の情報を0 or 1のフラグで表される列に変更する。
df_sex = pd.get_dummies(df['性別'], prefix='性別')
print(df_sex.head())

# def_sexとdfをjoin
temp_data = df_sex.join(df)
print(temp_data.head())

# 不要列の削除   ※axis=1は行でなく列の削除であることを示す
train_data = temp_data.drop(['性別', '年輪'], axis=1)
print(train_data.head())


X_train = train_data.iloc[:, :7]
y_train = train_data.iloc[:, 7]
print(X_train.head())
print(y_train.head())

################## 回帰モデルの学習と推定 ##################

# 回帰モデルの定義
model = RandomForestRegressor()

# 訓練データを使って回帰モデルを構築
model.fit(X_train, y_train)

# 訓練データに対する推定
prediction = model.predict(X_train)

# MSE（平均2乗誤差）の計算
print(mean_squared_error(y_train, prediction))