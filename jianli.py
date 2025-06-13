import streamlit as st
from PIL import Image, ImageEnhance
st.set_page_config(page_title='个人简历生成器',layout='wide')



if 'xueli' not in st.session_state:
    st.session_state.xueli = None

if 'yuyan_nengli' not in st.session_state:
    st.session_state.yuyan_nengli = []

if 'jineng' not in st.session_state:
    st.session_state.jineng = []
    
if 'gongzuo_jingyan' not in st.session_state:
    st.session_state.gongzuo_jingyan = None

if 'qiwang_gongzi' not in st.session_state:
    st.session_state.qiwang_gongzi= 0

if 'geren_jianjie' not in st.session_state:
    st.session_state.geren_jianjie= None

if 'geren_time' not in st.session_state:
    st.session_state.geren_time= None

if 'image' not in st.session_state:
    st.session_state.image= None



c1,c2=st.columns([1,2])

with c1:
    st.header('🎨个人简历生成器')
    st.caption('使用Seamlit创建您的个性化简历')
    st.subheader('个人信息表单')
    st.markdown('***')
    st.session_state['name'] = st.text_input('姓名：', '')


    st.session_state['occupy']=st.text_input('职位:','')



    st.session_state['tele']=st.text_input('电话:','')



    st.session_state['email']=st.text_input('邮箱:','')



    st.session_state['birthday']=st.date_input("出生日期", value=None)


    st.write('性别')
    st.session_state['sex']= st.radio(
        '你的性别是什么',
        ['男', '女', '其他'],
        horizontal=True,
        label_visibility='hidden'
    )

    
    st.session_state['xueli']= st.selectbox('学历：', ['大专', '本科', '研究生'])
    st.session_state['yuyan_nengli']= st.multiselect(
        '语言能力',
        ['英语','日语','中文','俄语']
        )

    st.session_state['jineng']= st.multiselect(
        '技能（可多选）',
        ['Python','C语言','机器学习','Java','C++','数据库']
        )

    my_range_gongzuojy = range(0,31)
    st.session_state.gongzuo_jingyan = st.select_slider('工作经验', options=my_range_gongzuojy, value=0)

    my_range_qiwanggongzi = range(0, 100000)
    st.session_state.qiwang_gongzi= st.select_slider('期望工资', options=my_range_qiwanggongzi, value=(0,10000))

    st.session_state.geren_jianjie=st.text_area(label='个人简介：', placeholder='请输入您的个人简介')
   
    st.session_state.geren_time=st.time_input("每日最佳联系时间段")

    st.session_state.image = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"])



with c2:
    st.caption('')
    st.caption('')
    st.caption('')
    st.caption('')
    st.caption('')
    st.caption('')
    st.caption('') 
    st.subheader('简历实时预览')
    
    st.markdown('***')
    st.write('', st.session_state['name'])
    
    
    c1,c2=st.columns(2)
    with c1:
        if st.session_state.image is not None:
            st.session_state.image = Image.open(st.session_state.image)
            st.image(st.session_state.image, caption="上传的图片", use_column_width=True, width=400)
        
        st.write('职位：', st.session_state['occupy'])
        st.write('电话：', st.session_state['tele'])
        st.write('邮箱：', st.session_state['email'])
        st.write('出生日期：', st.session_state['birthday'])
    with c2:

        st.write('性别：', st.session_state['sex'])
        st.write('学历：', st.session_state['xueli'])
        st.write('工作经验：', st.session_state['gongzuo_jingyan'],'年')
        st.write('期望薪资：', st.session_state['qiwang_gongzi'])
        st.write('最佳联系时间：', st.session_state['geren_time'])
        st.write('语言能力：', st.session_state['yuyan_nengli'])
        
    st.markdown("---")      
    st.subheader('个人简介')
    st.write(st.session_state['geren_jianjie'])
    st.subheader('专业技能')
    st.write(st.session_state['jineng'])
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('_在顶级的算法世界里，你是最优解_')
    

