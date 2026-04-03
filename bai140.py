import tkinter as tk
from tkinter import messagebox

# Hàm kiểm tra ISBN
def check_isbn(isbn):
    # Loại bỏ dấu nối
    isbn_clean = isbn.replace("-", "").upper()
    # Kiểm tra độ dài hợp lệ (10 ký tự cho ISBN-10)
    if len(isbn_clean) != 10:
        return False
    
    total = 0
    # Tính tổng theo quy tắc
    for i, ch in enumerate(reversed(isbn_clean), start=1):
        if ch == "X":
            val = 10
        elif ch.isdigit():
            val = int(ch)
        else:
            return False
        total += val * i
    
    return total % 11 == 0

# Xử lý khi nhấn nút
def on_check():
    isbn = entry_isbn.get().strip()
    if not isbn:
        messagebox.showerror("Lỗi", "Vui lòng nhập số ISBN!")
        return
    valid = check_isbn(isbn)
    text_result.delete("1.0", tk.END)
    if valid:
        text_result.insert(tk.END, f"ISBN {isbn} hợp lệ ✅")
    else:
        text_result.insert(tk.END, f"ISBN {isbn} không hợp lệ ❌")

# Tạo giao diện
root = tk.Tk()
root.title("Bài 140: Kiểm tra ISBN")
root.geometry("500x300")
root.configure(bg="#f0f8ff")

# Tiêu đề
title = tk.Label(root, text="Kiểm tra số ISBN hợp lệ",
                 font=("Segoe UI", 13, "bold"), bg="#f0f8ff", fg="#1a73e8")
title.pack(pady=10)

# Hướng dẫn
guide = tk.Label(root, text="Nhập ISBN (10 ký tự, có thể có dấu -):",
                 font=("Segoe UI", 10), bg="#f0f8ff")
guide.pack()

# Ô nhập
entry_isbn = tk.Entry(root, font=("Segoe UI", 11), width=25, justify="center")
entry_isbn.pack(pady=5)

# Nút kiểm tra
btn_check = tk.Button(root, text="Kiểm tra", font=("Segoe UI", 11, "bold"),
                      bg="#1a73e8", fg="white", width=12, command=on_check)
btn_check.pack(pady=10)

# Khung kết quả
frame_result = tk.Frame(root, bg="#e8f0fe", bd=2, relief="groove")
frame_result.pack(padx=20, pady=10, fill="both", expand=True)

text_result = tk.Text(frame_result, font=("Consolas", 12), bg="#ffffff", fg="#202124", wrap="word", height=5)
text_result.pack(padx=10, pady=10, fill="both", expand=True)

# Chạy chương trình
root.mainloop()