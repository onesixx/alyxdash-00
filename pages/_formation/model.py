import numpy as np
import pandas as pd
import os

import plotly.graph_objs as go
import plotly.express as px

from alyxdash.utils import make_pdata_undup

df = px.data.stocks()
df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: round(x, 2))
sum(df.duplicated(subset=['GOOG']))

pdata = make_pdata_undup(df, 'GOOG')
pdata
trace1 = go.Scatter(
    x=pdata.index, y=pdata['GOOG'],
    mode='markers', marker=dict(size=3))
layout = go.Layout()
fig = go.Figure([trace1], layout)
fig.show()


iris = px.data.iris()
iris = pd.concat([iris.loc[[9]],  iris.iloc[31:38],
                 iris.loc[[101]], iris.iloc[142:143, :]])
ddata = iris
AirPassengers = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv",
                            header=0, index_col=0, parse_dates=True)
ddata = px.data.stocks()
ddata =
sum(ddata.duplicated(subset=['date', 'AMZN']))


trace1 = go.Scatter(
    x=ddata['date'],
    y=ddata['GOOG'],
    mode='markers',
    marker=dict(color="red")
)
data = [trace1]
layout = go.Layout()
fig = go.Figure(data, layout)
fig.show()

# 중복행 찾기
iris.duplicated()   # F F T F ...
iris.duplicated(keep='first')
iris.duplicated(keep='last')
iris.duplicated(keep='last', subset=None)

iris[iris.duplicated()]            # 중복행 중 첫행만 지우고, 나머지 중복행 남김
iris[iris.duplicated(keep=False)]  # 중복되지않은 행만 남김. (중복행 중 첫행 포함)

# 중복확인
iris.duplicated(keep='first', subset=None)
iris.duplicated(keep='last', subset=None)


iris.duplicated(keep=False)  # 중복값 모두
iris.duplicated(keep='last', subset=['petal_length', 'species'])

# 중복처리
iris.drop_duplicates()


# rleid(df['grp'])

# dfdup = df[~(pd.Series(rleid(df['grp'])).duplicated(keep='first')) |
#            ~(pd.Series(rleid(df['grp'])).duplicated(keep='last'))]

os.chdir('/home/oschung_skcc/my/git/dash_01')
myData_root = os.path.join(os.getcwd(), 'data', 'issue_0227')

FILENM = 'proc_01_T1_11_FCH_Equip113_P218_T55091_T51677_20221207_062322.csv'
FILE_NM = os.path.join(myData_root, FILENM)

ddf = pd.read_csv(FILE_NM,  encoding='euc-kr')

# '시간',
# 'ch1 전압', 'ch1 전류', 'ch1 용량', 'ch1 PV', ...
# 'ch28 전압', 'ch28 전류', 'ch28 용량', 'ch28 PV', ...
# 'ch56_vol', 'ch56_curr', 'ch56_q', 'ch56_pv',
# 'temp_1', 'temp_2', ... 'temp_12'
# power voltage

channel_var = [f'ch{i:02}_{j}' for i in range(1, 57)
               for j in ['vol', 'curr', 'capa', 'pv']]
temperature = [f'temp_{x:02}' for x in range(1, 13)]
cols = ['time'] + channel_var + temperature
# len(cols)
ddf.columns = cols

# ========
for x in ddf.columns:
    print(ddf[x].dtype, end=' ')

# ======= trans...
ddf['duration'] = pd.to_timedelta(ddf['time'])
ddf['second'] = pd.to_timedelta(ddf['duration']).dt.total_seconds().astype(int)

# ddf[ddf.columns[ddf.columns.str.startswith('ch01')] ]

# voldf= ddf.loc[:, ddf.columns[ddf.columns.str.contains('\d+_vol')]]
# df_vol = pd.concat([ddf.time, ddf.second, voldf], axis=1)


plt_data = pd.melt(ddf,
                   id_vars=['second'],
                   value_vars=ddf.columns[2:],
                   var_name='id',
                   value_name='val')
var = '_vol'

fig = px.scatter(
    plt_data[plt_data['id'].str.contains(var)],
    x='second', y='val',
    color='id',
)

fig = px.line(
    plt_data[plt_data['id'].str.contains(var)],
    x='second', y='val',
    color='id',
)

# Set the plot title and axis labels
# fig.update_layout(
#     title='Line and Scatter Plot',
#     xaxis_title='X Axis',
#     yaxis_title='Y Axis')
fig.show()

fig = px.scatter(
    ddf.loc[:, ['time', 'second', 'ch01_vol']],
    x='second', y='ch01_vol',
)
fig.update_traces(
    marker=dict(size=3, color='red',
                line=dict(width=1, color='MediumPurple')),
    selector=dict(mode='markers')
)
# =======


fig = go.Figure()

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_vol.second, y=df_vol.ch01_vol,
        marker=dict(
            color='red',
            size=3,
            line=dict(
                color='MediumPurple',
                width=1
            )
        ),
        showlegend=False
    )
)
fig.update_layout(
    title='Scatter Plot',
    xaxis_title='Second',
    yaxis_title='voltage')
fig.show()


df = px.data.gapminder()
df.columns[df.columns.str.contains('\d+_vol')]
fig = go.Figure()
for x in df.loc[df.continent.isin(["Europe"])].country.unique()[:5]:
    fil = df.loc[(df.country.str.contains(x))]
    fil = df.loc[df.country == 'Albania']
    fig.add_trace(
        go.Scatter(
            x=fil["year"],
            y=fil["pop"],
            mode="lines+markers",
            # marker=dict(
            #     symbol="arrow",
            #     size=15,
            #     angleref="previous",
            # ),
            # name=x,
        )
    )
fig.show()

# ---
# df.head()
# df.columns
# cols = df.columns.tolist()
# type(cols)
# len(cols)   # 237
# # pd.options.display.max_columns = 237
# # pd.options.display.max_rows = 237
# print(cols)


prefix = 'ch1'
suffixes = ['voltage', 'current', 'capacity', 'PV']
variables = [prefix + ' ' + s for s in suffixes]

# print the list of variable names
print(variables)


fch_data = []


# files = []
# for f in files:
#     print(f, os.path.splitext(f))
#     if os.path.splitext(f)[1] != '.csv':
#         print('not csv')
#         continue

#     if f.split('_')[4] == 'FCH':
#         formation_data = pd.read_csv(f, encoding='ISO-8859-1')
#         formation_data.columns = df_colnms
#         fch_data.append([f[:7], formation_data])


def make_data(N):
    data = np.random.randn(N)
    return data


data = make_data(N=50)


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    ))

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=50,
        r=100,
        b=150,
        t=100,
        pad=40
    ),
    paper_bgcolor="LightSteelBlue",
)

fig.show()
