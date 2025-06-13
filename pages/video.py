import streamlit as st

def app():
    
    st.title("🎵Streamlit音乐播放器")
    st.text("点击下方视频封面选择要播放的视频")


    # 判断内存中（session_state中）有没有a
    if 'a' not in st.session_state:
        st.session_state['a'] = 0


    video_arr = [{
            'url': 'http://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '大兔子',
            'image': 'https://tse2-mm.cn.bing.net/th/id/OIP-C.tOgmPlv7EVzy24q5s0G-0wHaD2?w=306&h=180&c=7&r=0&o=7&pid=1.7&rm=3',
            'describe': '大兔子~',
            'time':'0:10',
            'classify': '大兔子',
        },{
           'url': 'https://www.w3schools.com/html/movie.mp4',
            'title': '大灰熊',
            'image': 'https://tse3-mm.cn.bing.net/th/id/OIP-C.5LI1CTjBmEw-lG0tKlfxGAAAAA?w=272&h=181&c=7&r=0&o=7&pid=1.7&rm=3',
            'describe': '大灰熊',
            'time':'0:12',
            'classify': '大灰熊',
        },{
            'url': 'https://stream7.iqilu.com/10339/upload_transcode/202002/09/20200209105011F0zPoYzHry.mp4',
            'title': '新闻',
            'image': 'https://tse1-mm.cn.bing.net/th/id/OIP-C.c9Flw6mbOMJxUo-rLx9EmgHaEO?w=298&h=180&c=7&r=0&o=7&pid=1.7&rm=3',
            'describe': '新闻',
            'time':'1:05',
            'classify': '新闻',
        }]





    st.video(video_arr[st.session_state['a']]['url'])
    st.title(video_arr[st.session_state['a']]['title'])
    st.text(video_arr[st.session_state['a']]['describe'])
    col1, col2 = st.columns(2)
    with col1:
        st.write('时长:',video_arr[st.session_state['a']]['time'])
    with col2:
        st.write('分类:',video_arr[st.session_state['a']]['classify'])


    import streamlit as st

    # 创建一个标题
    st.title("多视频空框示例")


    # 图片URL列表
    image_urls = [
      'https://mindfulspirituallife.com/wp-content/uploads/2023/12/cat.jpg',  # 第一个视频的缩略图
        'https://www.allaboutbirds.org/news/wp-content/uploads/2020/07/STanager-Shapiro-ML.jpg',  # 第二个视频的缩略图
        'https://a-z-animals.com/media/2023/02/shutterstock_2152176495.jpg'   # 第三个视频的缩略图
    ]
    # 视频URL列表
    video_urls = [
        "https://www.w3school.com.cn/example/html5/mov_bbb.mp4",
        "https://www.w3schools.com/html/movie.mp4",
        "https://media.w3.org/2010/05/sintel/trailer.mp4"
    ]



    # 为每个视频创建一个单元（按钮+图片+视频占位符）
    for i in range(3):
        # 创建空白按钮
        show_video = st.button("", key=f"btn{i+1}")
        
        # 显示图片
        st.image(image_urls[i], caption=f"", use_container_width=True)
        
        # 创建视频占位符
        video_placeholder = st.empty()
        
        # 根据按钮状态显示相应视频
        if show_video:
            video_placeholder.video(video_urls[i])
        else:
            video_placeholder.markdown(f"")
        
