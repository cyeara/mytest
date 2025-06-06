import streamlit as st # 导入Streamlit并用st代表它
import pandas as pd  # 导入Pandas并用pd代替

st.title(' :underage: 学生 小陆-数字文档')

st.header(' :heart_eyes: 基础信息')#标题一

st.write('学生ID:NEO-2023-001')

st.write('注册时间:`2025-6-5 06:06:06`丨精神状态: ✅正常')

st.subheader(' :muscle: 技能矩阵')#标题三

c1, c2, c3 = st.columns(3)#将三行合成一行
c1.metric(label="c语言", value="95%", delta="2")#第一技能
c2.metric(label="Python", value="87%", delta="-1")#第二技能
c3.metric(label="Java", value="68%", delta="-10", delta_color="off")#第三技能


st.header("Streamlit课程进度")#标题行
txet1="Streamlit课程进度" #进度条
my_bar=st.progress(30,text=txet1)

st.header(' :pencil: 任务日志')
# 创建数据字典
data = {
    '日期': ['2023-10-01', '2023-10-05', '2023-10-12'],
    '任务': ['学生数学档案', '课程管理系统', '数据图表表示'],
    '状态': ['✅ 完成', '⏳ 进行中', '❌ 未完成'],
    '难度': ['★★☆☆☆', '★☆☆☆☆', '★★★☆☆']
}
# 定义数据框所用的索引
index = pd.Series(['01', '02', '03'], name='序列')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)
st.dataframe(df)

st.header(' :shit: 最新代码成果')#标题行

python_code = '''def hello():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()
'''
# 创建一个代码块，用于展示python_code的内容
# 并设置语法高亮
st.code(python_code,line_numbers=True)

st.markdown('***')#添加下划线

st.write('`>> SYSTEM MESSAGE:`下一个任务目标已解锁...')#markdown字体改变，文本输入

st.write('`>> TARGET:`课程管理系统')#markdown字体改变，文本输入

st.write('`>> COUNTDOWN:`2025-06-03 15:15:15')#markdown字体改变，文本输入

st.text('系统状态:在线 连接状态:已加密')#文本输入