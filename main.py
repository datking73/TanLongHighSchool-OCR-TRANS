from tkinter import *
from PIL import ImageTk, Image
import subprocess
import pytesseract
from googletrans import Translator
import time
class ScreenTranslate:

    def __init__(self, master):
        self.master = master
        master.title("Screen Translate")
        
        self.lang_src = "eng"
        self.lang_dest = "vie"
        self.text = ""

        self.textTrans = ""

        self.capture = Button(master, text="Capture", command=self.capture)
        self.lang_button = Button(master, text="Language", command=self.changeLang)
        #nút chức năng

        # 

        self.capture.grid(row=0, column=0,padx=(50, 10), pady=10)
        self.lang_button.grid(row=0, column=1,padx=(10, 50))
        #Độ rộng khung chức năng

    def capture(self):
        print("Capture")
        #print(self.lang_src)

        #mở file hỗ trợ chụp màn hình
        subprocess.call(['python', 'ScreenCapture.py'], shell=True)


        #tạo cửa sổ mới hiện ngôn ngữ dịch
        imgApp = Toplevel()

        #mở file ảnh đã chụp
        imsize = Image.open('Capture.jpg')
        width, height = imsize.size

        #tạo cửa sổ 
        wh = str(width+80) + 'x' + str(height+80)
        imgApp.geometry(wh)
        imgApp.title("Image")
        imgApp.attributes('-topmost',True)

        menubar = Menu(imgApp)
        menubar.add_command(label="Translate",command=self.Translate)
        menubar.add_command(label="Language",command=self.changeLang)

        imgApp.config(menu=menubar)
        
        #show ảnh đã chụp tỉ lệ khung bằng với ảnh
        canvas = Canvas(imgApp, height=height, width=width)
        canvas.pack(padx=20,pady=20)
        
       

        im = Image.open('Capture.jpg')
        canvas.image = ImageTk.PhotoImage(im)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')
        
        

        imgApp.mainloop()

        

    def changeLang(self):
        print("Change lang")

        SRC = [
        "Vie",
        "English",
        "Chinese"
        ] #etc

        DEST = [
        "Vie",
        "English",
        "Chinese"
        ] #etc

        master = Toplevel()
        master.attributes('-topmost',True)
        
        lbl_lang_src = Label(master, text="Source Language")
        lbl_lang_src.grid(column=0, row=0, padx=10)
        
        src_var = StringVar(master)
        src_var.set(SRC[0]) # default value
        
        w1 = OptionMenu(master, src_var, *SRC)
        w1.grid(column=1,row=0,padx=10)

        dest_var = StringVar(master)
        dest_var.set(DEST[1]) # default value

        lbl_lang_dest = Label(master, text="Target Language")
        lbl_lang_dest.grid(column=0, row=1, padx=10)

        w2 = OptionMenu(master, dest_var, *DEST)
        w2.grid(column=1,row=1,padx=10)

        def ok():
            print ("Source Lang.:" + src_var.get())
            print ("Target Lang.:" + dest_var.get())            



            # Ngôn ngữ cần dịch
            if "Vie" in src_var.get():
                self.lang_src = "vie"
                print(self.lang_src)

            if "Chinese" in src_var.get():
                self.lang_src = "chi_sim"
                print(self.lang_src)

            if "English" in src_var.get():
                self.lang_src = "eng"
                print(self.lang_src)

            
            # Ngôn ngữ dịch
            if "Vie" in dest_var.get():
                self.lang_dest = "vie"
                print(self.lang_dest)

            if "Chinese" in dest_var.get():
                self.lang_dest = "chi_sim"
                print(self.lang_dest)

            if "English" in dest_var.get():
                self.lang_dest = "eng"
                print(self.lang_dest)
                
            master.destroy()
            

        button = Button(master, text="OK", command=ok)
        button.grid(column=0,row=2)

        master.mainloop()

    def Translate(self):
        # thư viện tesseract đọc ảnh từ màn hình
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.text = pytesseract.image_to_string(Image.open('Capture.jpg'), lang=self.lang_src)


        print(self.text)

        #tạo cửa sổ mới show chữ đã đọc được
        OCRbox = Tk()
        OCRbox.geometry("515x620")
        OCRbox.title("Translation")
        OCRbox.attributes('-topmost',True)

        #text box

        lbl = Label(OCRbox, text="OCR Text")
        lbl.grid(column=0, row=0, padx=10)


        T = Text(OCRbox, wrap=WORD, width=70, height= 20)
        T.grid(column=0, row=1, padx=10, pady=10)
        T.tag_configure('tag-center', justify='center')

        
        T.insert(END, self.text)
    

        lbl_translate = Label(OCRbox, text="Translated")
        lbl_translate.grid(column=0, row=2, padx=10)

        translator = Translator()

        
        if self.lang_dest == 'chi_sim' and self.lang_src == "eng":
            tr = translator.translate(self.text, dest='zh-cn',src='en')
            print(tr.text)
            self.textTrans = tr.text
            
        if self.lang_dest == 'chi_sim' and self.lang_src == "vie":
            tr = translator.translate(self.text, dest='zh-cn',src='vi')
            print(tr.text)
            self.textTrans = tr.text

        
        if self.lang_dest == 'eng'and self.lang_src == "chi_sim":
            tr = translator.translate(self.text, dest='en',src='zh-cn')
            print(tr.text)
            self.textTrans = tr.text

        if self.lang_dest == 'eng'and self.lang_src == "vie":
            tr = translator.translate(self.text, dest='en',src='vi')
            print(tr.text)
            self.textTrans = tr.text

        
        if self.lang_dest == 'vie' and self.lang_src == "eng":
            tr = translator.translate(self.text, dest='vi',src='en')
            print(tr.text)
            self.textTrans = tr.text

        if self.lang_dest == 'vie' and self.lang_src == "chi_sim":
            tr = translator.translate(self.text, dest='vi',src='zh-cn')
            print(tr.text)
            self.textTrans = tr.text

               
        TransOut = Text(OCRbox, wrap=WORD, width=70, height= 20)
        TransOut.grid(column=0, row=3, padx=10, pady=10)
        TransOut.insert(END, self.textTrans)
        
        OCRbox.mainloop()

root = Tk()
my_gui = ScreenTranslate(root)
root.mainloop()
