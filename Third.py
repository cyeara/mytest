import streamlit as st

st.set_page_config(page_title='音乐播放器',page_icon='🎵')

if 'a' not in st.session_state:
    st.session_state['a']=0

audio_arr=[{
    'url':'https://music.163.com/song/media/outer/url?id=2633225875.mp3',
    'image':'https://p1.music.126.net/TBjkf6t3Yj9XNmWp1TqxPg==/109951170012510702.jpg',
    'name':'Hero','singer':'歌手:Mili','album':'所属专辑:Hero'
    },{'url':'https://music.163.com/song/media/outer/url?id=2707332868.mp3',
    'image':'https://p1.music.126.net/3SREPNrEu561h_K2jLB8ww==/109951171011324261.jpg',
    'name':'Tian Tian','singer':'歌手:Mili','album':'所属专辑:Tian Tian'
    },{'url':'https://music.163.com/song/media/outer/url?id=2676626158.mp3',
    'image':'https://p1.music.126.net/PLzyS6NhTcIS6KiWbetsjA==/109951170498058292.jpg',
    'name':'スゴすぎ前橋ウィッチーズ！','singer':'歌手:前橋ウィッチーズ','album':'所属专辑:スゴすぎ前橋ウィッチーズ！'
    }]

a1, a2 ,a3= st.columns(3)
with a1:
    st.image(audio_arr[st.session_state['a']]['image'], caption='封面')

with a2:
    st.subheader(audio_arr[st.session_state['a']]['name'])
    st.text(audio_arr[st.session_state['a']]['singer'])
    st.text(audio_arr[st.session_state['a']]['album'])
 
#st.image(audio_arr[st.session_state['a']]['image'])
#st.header(audio_arr[st.session_state['a']]['name'])
#st.subheader(audio_arr[st.session_state['a']]['singer'])
#st.subheader(audio_arr[st.session_state['a']]['album'])
st.audio(audio_arr[st.session_state['a']]['url'])

def back():
    global a
    st.session_state['a']=(st.session_state['a']-1)%len(audio_arr)

def next():
    global a
    st.session_state['a']=(st.session_state['a']+1)%len(audio_arr)

c1,c2=st.columns(2)

with c1:
    st.button('上一首',on_click=back,use_container_width=True)
with c2:
    st.button('下一首',on_click=next,use_container_width=True)
