import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
from PIL import Image
from gdown import download

def read_public_file_from_drive(file_url):
    response=requests.get(file_url)
    if response.status_code == 200:
        content = response.text
        return content
    else:
        raise Exception(f"Error reading file :{response.status_code}")

def add_labeled_parking(x,y,width,height,i,content_set,angle=0):
    if i in content_set:
        color='orange'
    else:
        color= 'green'
    ax.add_patch(plt.Rectangle(xy=(x,y),width=rect_width,height=rect_height,color=color,angle=angle))
    text_x=x+rect_width /2
    text_y=y+rect_height / 2
    ax.text(text_x,text_y,str(i),ha='center',va='top',fontsize=12,fontweight='bold',color='white')

    
st.title('Al-motnby street')


#Read file content
try:
    url='https://drive.google.com/uc?id=1rSpre8qZUYieaOtGLoBShQEud-ldRrcH'
    download(url,output="all_spots_in_use.txt",quiet=False)
    with open("all_spots_in_use.txt",'r') as f:
        content=f.read()
    content_lines=content.splitlines()
    content_set=set(int(line) for line in content_lines)
except Exception as e:
    st.error(f"Error reading file:{str(e)}")

text="""The following visualization provides real-time information on occupied and available parking spaces at the end of Al-Motnby street in Haifa. There are 20 numbered parking spaces in total. The occupied spaces are highlighted in orange, while available spaces are highlighted in green."""
st.markdown(f"#### {text}")

color_width=80
color_height=80
color1="green"
color2="orange"
green_image=Image.new("RGB",(color_width,color_height),color1)
orange_image=Image.new("RGB",(color_width,color_height),color2)
green_image.save("green_square.png")
orange_image.save("orange_square.png")
col1, col2=st.columns(2)
with col1:
    st.image("green_square.png",caption="Available")
with col2:
    st.image("orange_square.png",caption="Occupied")

bg_img=mpimg.imread('pages/parkingLot.JPG')
rect_width=70
rect_height=58
figure,ax=plt.subplots(figsize=(10,6))
ax.imshow(bg_img,extent=None,aspect='auto')

for i in range(1,21):
    if(i==1):
        x_min=695
        y_min=180
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,-7)
    elif(i==2):
        rect_width=50
        rect_height=25
        x_min=800
        y_min=125
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,-7)
    elif(i==3):
        rect_width=50
        rect_height=25
        x_min=850
        y_min=115
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,-7)
    elif(i==4):
        rect_width=20
        rect_height=45
        x_min=880
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==5):
        rect_width=20
        rect_height=45
        x_min=860
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==6):
        rect_width=25
        rect_height=45
        x_min=835
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==7):
        rect_width=25
        rect_height=45
        x_min=810
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==8):
        rect_width=25
        rect_height=45
        x_min=785
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==9):
        rect_width=25
        rect_height=45
        x_min=760
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==10):
        rect_width=25
        rect_height=45
        x_min=735
        y_min=55
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,13)
    elif(i==11):
        rect_width=80
        rect_height=36
        x_min=600
        y_min=93
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)
    elif(i==12):
        rect_width=70
        rect_height=70
        x_min=571
        y_min=187
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,-7)
    elif(i==13):
        rect_width=80
        rect_height=36
        x_min=520
        y_min=93
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)
    elif(i==14):
        rect_width=70
        rect_height=75
        x_min=501
        y_min=187
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,-7)
    elif(i==15):
        rect_width=71
        rect_height=75
        x_min=430
        y_min=187
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set,-7)
    elif(i==16):
        rect_width=125
        rect_height=42
        x_min=400
        y_min=105
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)
    elif(i==17):
        rect_width=90
        rect_height=42
        x_min=310
        y_min=105
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)
    elif(i==18):
        rect_width=125
        rect_height=37
        x_min=185
        y_min=95
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)
    elif(i==19):
        rect_width=125
        rect_height=37
        x_min=60
        y_min=80
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)
    elif(i==20):
        rect_width=60
        rect_height=37
        x_min=0
        y_min=75
        add_labeled_parking(x_min,y_min,rect_width,rect_height,i,content_set)


        
#ax.axis=('off')
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
st.pyplot(figure)

st.markdown(f"#### Live view from the street:")

try:
    image_url='https://drive.google.com/uc?id=1O0Ysdojc757QMUyrmGCkzv5thNrkQufT'
    download(image_url,output="last_img.png",quiet=False)
    st.image('last_img.png')
except Exception as e:
    st.error(f"Error downloading live image:{str(e)}")

st.markdown(":car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car:")
conatc_text="""I strive to provide accurate information about parking space availability, but I acknowledge that errors may occur. Due to various factors, the status of occupied parking spaces displayed here may not always be entirely up to date. Your assistance in maintaining the accuracy of this information is invaluable to me. If you notice any discrepancies or encounter an issuem I encourage you to navigate to the 'Contact' section in the navigation bar and inform me of the error, along with the time and date it occured. Your feedback helps me improve my service and ensure a better experience for all users. Thank you for your understanding and cooperation."""
st.markdown(f"##### {conatc_text}")
st.markdown(":car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car:")
while True:
    current_time=time.localtime()
    if (current_time.tm_min % 2)==0 and current_time.tm_sec==30:
        break

st.rerun()
