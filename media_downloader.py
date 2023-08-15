import streamlit as st
import openai




def youtube_audio_downloader(link):
    from pytube import YouTube
    import os
    import re
    if 'youtube.com' not in link:
        print('Invalid YouTube link')
        return False
    yt=YouTube(link)
    audio=yt.streams.filter(only_audio=True).first()
    print("Downloading....")
    output_file=audio.download()
    if os.path.exists(output_file):
        print("Downloaded! ")
    else:
        print("Error in downloading the file")
        return False
    return (f'Title: {yt.title}')



if __name__== '__main__':
    openai.api_key=open('key.txt').read().strip('\n')

    col1,col2=st.columns([0.85,0.15])
    with col1:
        st.title("YouTube Audio Downloader")
    with col2:
        st.image('music.png',width=100)
    with st.form(key='my_form'):
        yt_url=st.text_input(label='YouTube URL')
        submit_button=st.form_submit_button(label='Submit')

        if submit_button:
            result=youtube_audio_downloader(yt_url)
            st.write(result)

            