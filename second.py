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