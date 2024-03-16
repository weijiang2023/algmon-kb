import plotly.graph_objects as go

categories = ['1.时尚度', '2.搭配与协调性', '3.剪裁与设计',
              '4.舒适度', '5.姿态与表现力', '6.适应场合', '7.时装秀主题呈现', '8.价格']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
    r=[9, 9, 9, 6, 8, 6, 8, 9],
    theta=categories,
    fill='toself',
    name='Look 1'
))

fig.add_trace(go.Scatterpolar(
    r=[4, 3, 2, 1, 2, 8, 7, 7],
    theta=categories,
    fill='toself',
    name='Look 2'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )),
    showlegend=False
)

fig.show()
