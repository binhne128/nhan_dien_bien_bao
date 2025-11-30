import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy

from tensorflow.keras.models import load_model

model = load_model('my_model.h5', compile=False)


classes = { 1:'Tốc độ tối đa cho phép (20km/h)',
            2:'Tốc độ tối đa cho phép (30km/h)',      
            3:'Tốc độ tối đa cho phép (50km/h)',       
            4:'Tốc độ tối đa cho phép (60km/h)',      
            5:'Tốc độ tối đa cho phép (70km/h)',    
            6:'Tốc độ tối đa cho phép (80km/h)',      
            7:'Hết hạn chế tốc độ tối đa (80km/h)',     
            8:'Tốc độ tối đa cho phép (100km/h)',    
            9:'Tốc độ tối đa cho phép (120km/h)',     
           10:'Cấm vượt',   
           11:'Cấm ô tô tải vượt',     
           12:'Giao nhau với đường không ưu tiên',     
           13:'Đường ưu tiên',    
           14:'Giao nhau với đường ưu tiên',     
           15:'Dừng lại',       
           16:'Đường cấm',       
           17:'Cấm xe tải',       
           18:'Cấm đi ngược chiều',       
           19:'Nguy hiểm',     
           20:'Chỗ ngoặt nguy hiểm vòng sang trái',      
           21:'Chỗ ngoặt nguy hiểm vòng sang phải',   
           22:'Nhiều chỗ ngoặt nguy hiểm liên tiếp ',      
           23:'Đường không bằng phẳng',     
           24:'Đường trơn',       
           25:'Đường bị hẹp bên phải',  
           26:'Công trường đang thi công',    
           27:'Giao nhau với tín hiệu đèn',      
           28:'Đường người đi bộ cắt ngang',     
           29:'Trẻ em',     
           30:'Đường người đi xe đạp cắt ngang',       
           31:'Đường có tuyết',
           32:'Thú rừng vượt qua đường',      
           33:'Hết tất cả các lệnh cấm',      
           34:'Các xe chỉ được rẽ phải',     
           35:'Các xe chỉ được rẽ trái',       
           36:'Hướng đi thẳng phải theo',      
           37:'Các xe chỉ được đi thẳng và rẽ phải',      
           38:'Các xe chỉ được đi thẳng và rẽ trái',      
           39:'Hướng phải đi vòng sang phải',     
           40:'Hướng phải đi vòng sang trái',      
           41:'Nơi giao nhau chạy theo vòng xuyến',     
           42:'Hết cấm vượt',      
           43:'Hết cấm ô tô tải vượt' }
                 
top=tk.Tk()
top.geometry('800x600')
top.title('Nhận dạng biển báo giao thông ')
top.configure(background='#ffffff')

label=Label(top,background='#ffffff', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred_probabilities = model.predict(image)[0]
    pred = pred_probabilities.argmax(axis=-1)
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Nhận dạng",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#c71b20', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#c71b20', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Nhận dạng biển báo giao thông",pady=10, font=('arial',20,'bold'))
heading.configure(background='#ffffff',foreground='#364156')

heading1 = Label(top, text="Máy học cơ bản và ứng dụng",pady=10, font=('arial',20,'bold'))
heading1.configure(background='#ffffff',foreground='#364156')

heading2 = Label(top, text="Nhóm thực hiện: 06",pady=5, font=('arial',20,'bold'))
heading2.configure(background='#ffffff',foreground='#364156')

heading3 = Label(top, text="GVHD: Nguyễn Thanh Tuấn",pady=5, font=('arial',20,'bold'))
heading3.configure(background='#ffffff',foreground='#364156')

heading.pack()
heading1.pack()
heading2.pack()
heading3.pack()
top.mainloop()
