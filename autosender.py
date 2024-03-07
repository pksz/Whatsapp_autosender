
#TO-DO -- send predefined messeges to people over whatsapp
#import needed libs
#create our token
#figure out the input method of the sender numbers
#implement changing names
#implement changing inventory numbers
#find out the deployment device and fix any issues that may arise

#libs
# whatsappkit for small no of messages
import pywhatkit as pwk
import tkinter as tk
from tkinter import ttk,scrolledtext
from PIL import Image,ImageTk
#

#change names and first line before prod
templates=dict()
templates.update({"after_meeeting_message": '''

As a business development, we've below-mentioned projects in which you can open your store:

1) Bhutani Alphathum (Sector-90, Noida)

2) Elan Epic (Sec-70, Gurgaon)

3) Elan Miracle (Sec-84, Gurgaon)

4) Elan Town Center (Sec-67, Gurgaon)

5) M3M Urbana (Sec-67, Gurgaon)

6) M3M 65th Avenue (Sec-65, Gurgaon)

7) Conscient One (Sec-109, Gurgaon)

8) Omaxe Chowk (Chandni Chowk)

9) Vegas (Sec-14, Dwarka, New Delhi)

10) Dwarka City Center II (Sec-12, Dwarka, New Delhi)

11) Pacific (Subhash Nagar, NSP, Dwarka, Jasolla)

12) Unity One (Janakpuri, Rohini, Shahdara, Panipat)

13) Delhi Metro

And many more



Kindly let us know if you need the profile of any of the above projects.


Thanks.
Regards,
Nakul Maini
Eminence Infrastructures
*************************************
''' 
,


#change names and first line before prod
'pitch_message':'''
We would like to inform you that we are a brand leasing consultancy firm and we've various luxury and High Street projects with us in Delhi/NCR.

Kindly refer to the profile and give us a chance to work with you.

Kindly let us know for further information and proposals.

Thanks.
Regards,
Nakul Maini
Eminence Infrastructures

*************************************
'''
,
#change names and first line before prod also seperate into three different ones
'greeting_message':'''

Hello,
This is Nakul Maini from Eminence Infrastructures.
It was nice interacting with you, looking forward to hearing from you very soon.
Thank you.
*************************************
'''
,
#not in prod
'greeting_message2':'''
Hello,
This is Nakul Maini from Eminence Infrastructures.
Please contact us for Brand Leasing/Investment in Luxury and High Street Projects in Delhi/NCR.
It was nice interacting with you and looking forward to hearing from you very soon.
Thank you.
*************************************
Hello,
This is Nakul Maini from Eminence Infrastructures.
I tried calling you but couldn't reach you, kindly contact us for Brand Leasing/Investment in Luxury and High Street Projects in Delhi/NCR.
Thank you.

'''
,
#not in prod

#change first line before prod and add additional info could make it a template system
'inventory_message':'''
Inventory Code: 
Location: 
Area (in sq.ft.): 
Demand:'''
})


#messagelist
message_list=['after_meeeting_message','pitch_message','greeting_message','inventory_message']
#TO-Do make it private if possible
message=''
######

#matches the selected choice to a predefined template key value
def select_template(choice):
    
    for template in templates.keys(): #compares dict keys to dropdown menu options
        if choice==template:
            message=templates.get(template)
            update_message_box(message)
            return
        else :
            print('template not found')
            
        
def update_message_box(messagedraft): 
    text_area.delete(1.0,tk.END)
    text_area.insert(tk.END,messagedraft)
          
# send code 
def send_message():
    reciver_number=recipient_number.get()
    reciver_number="+91"+reciver_number
    msg= text_area.get(1.0,tk.END)

    try:
        # Sending a message to a contact (Indian dial code +91)
        pwk.sendwhatmsg_instantly(reciver_number,msg,wait_time=15) 
        print("Message Sent!")  # Prints success message in the console
    #show exception
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        sending_exception = template.format(type(ex).__name__, ex.args)
        print (sending_exception)

#GUI
main_window=tk.Tk()
main_window.geometry("600x600")
main_window.minsize(100,100)
main_window.maxsize(1200,720)
main_window.title("Automating Whatsapp Messages Prototype")
main_window.configure(bg='#B1A2CA')

label_reciver_number=tk.Label(main_window,text="Reciever's number :" )
recipient_number = tk.Entry(main_window)  #enter field for number
label_message=tk.Label(main_window,text="Message")
text_area=scrolledtext.ScrolledText(main_window,wrap=tk.WORD,width=40,height=8)  #message window
send_button=tk.Button(main_window,text="Send",command=send_message)
status_label= tk.Label(main_window,text="")
#dropdown menu

message_show_default=tk.StringVar(main_window)      #stores selected value
message_show_default.set("Select an option")       #default value
#dropdown box
message_dropdown=tk.OptionMenu(main_window,message_show_default,*message_list,command=select_template)



#logo

icon='images\\leasingemininacelogo.jpg'
load=Image.open(icon)
render=ImageTk.PhotoImage(load)

#set logo
main_window.iconphoto(False,render)

#bgimage CANVAS
bg_img=Image.open('images\\leasingemininacelogo.jpg')
bg_img=bg_img.resize((100,100))
bg_img=ImageTk.PhotoImage(bg_img)

canvas = tk.Canvas(main_window,width=100,height=100,background="white")
canvas.create_image(50, 50, anchor=tk.CENTER, image=bg_img)
#Layout
canvas.pack(side='top',)
label_reciver_number.pack()
recipient_number.pack()
label_message.pack()
text_area.pack()
send_button.pack()
status_label.pack()
message_dropdown.pack()
main_window.mainloop()

