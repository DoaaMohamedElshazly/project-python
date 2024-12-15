from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
import os
# دالة لتحويل النص داخل الـ Entry إلى صوت
def play_text():
    text = entry.get()  # جلب النص من الـ Entry
    if text != "":
        # تحويل النص إلى صوت باستخدام gTTS
        tts = gTTS(text, lang='en')  # يمكن تحديد اللغة هنا (مثل "en" للانجليزيه)
        tts.save("output.mp3")  # حفظ الصوت في ملف MP3
        os.system("start output.mp3")  # لتشغيل الصوت على نظام ويندوز
    else:
        messagebox.showwarning("warning", "please enter your text")

# دالة لإغلاق البرنامج
def exit_program():
    root.quit()  # غلق واجهة الـ GUI
# دالة لمسح النص داخل الـ Entry
def clear_text():
    entry.delete(0, tk.END)  # مسح النص داخل الـ Entry

# إنشاء نافذة الـ GUI
root =Tk()
root.title("Text to Speech")

# إعداد حجم النافذة
root.geometry("450x350")

# إنشاء الـ Entry لإدخال النص
entry = ttk.Entry(root,width="40")
entry.pack(padx=20,pady=20,ipadx=30)

# إنشاء الأزرار
play_button = ttk.Button(root, text="Play", command=play_text)
play_button.pack(pady=5)

exit_button = ttk.Button(root, text="Exit", command=exit_program, style="Exit.TButton")
exit_button.pack(pady=5)

set_button = ttk.Button(root, text="Set", command=clear_text)
set_button.pack(pady=5)

# تخصيص تصميم الزر "Exit" ليكون لونه أحمر
style = ttk.Style()
style.configure("Exit.TButton", fg="red", bg="red")

# تشغيل واجهة الـ GUI
root.mainloop()
