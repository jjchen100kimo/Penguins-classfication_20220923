# HW01程式碼
# Streamlit documentation: https://docs.streamlit.io/
# https://docs.streamlit.io/library/cheatsheet


import streamlit as st
import numpy as np
import joblib


#load model 模型載入
rg2=joblib.load('penguins.joblib')
scaler=oblib.load('scaler.joblib')

y_dict={1:'Adelie', 2:'Chinstrap', 3:'Gentoo'}
island_dict={'Torgersen':1, 'Biscoe':2, 'Dream':3}
sex_dict={'Female':0, 'Male':1}

#網頁畫面設計
st.markdown('#企鵝品種預測')

#下拉式選單
island=st.selectbox('島嶼:',island_dict.keys() )

#滑動按鈕:'提示'，最小值，最大值，預設值
bill_length=st.select_slider('嘴巴長度', 30,60,40)
bill_depth=st.select_slider('嘴巴寬度', 10,25,15)
flipper_length=st.select_slider('翅膀長度', 170,230,200)
body_mass=st.select_slider('體重', 2500,6500,4000)

#radio
sex=st.radio('性別',sex_dict.keys())

#按下
if st.button('預測'):
    #predict
    #抓數字，二維陣列
    X=np.array([[island_dict[island], bill_length, bill_depth, flipper_length,
        body_mass, sex_dict[sex]]])
        
    #標準化特徵縮放轉換
    X=scaler.transform(X)
    #預測，**粗體字
    st.markdown(f'==>**{y_dict[int(rg2.predict(X))]}**')



'''
#button1 = st.button('Click me')
#checkbox1 = st.checkbox('I agree')
#animal = st.radio('Pick one', ['cats', 'dogs'])

#下拉式選單
#*selectbox1 = st.selectbox('Pick one', ['cats', 'dogs'])
multiselect1 = st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
slider1 = st.slider('Pick a number', 0, 100)
#*st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')

# st.download_button('Download file', data)
st.camera_input("Take a picture")
st.color_picker('Pick a color')

if st.button('查詢'):
    st.write(f'# {animal}')
    
'''