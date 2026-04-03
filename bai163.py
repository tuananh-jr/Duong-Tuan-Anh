import tkinter as tk
from tkinter import messagebox
import math

def my_pow(x, n):
    """Thuật toán lũy thừa nhanh với độ phức tạp O(log n)"""
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    
    # Tính x^(n/2) một lần duy nhất để tối ưu
    temp = my_pow(x, n // 2)
    
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

def calculate():
    try:
        # Lấy dữ liệu từ các ô nhập
        x = float(entry_x.get())
        n = int(entry_n.get())
        
        # Tính toán bằng hàm tự viết
        res_mypow = my_pow(x, n)
        
        # Tính toán bằng hàm hệ thống math.pow
        res_pow = math.pow(x, n)
        
        # Hiển thị kết quả lên giao diện
        label_res_mypow.config(text=f"mypow() : {res_mypow:.6f}", fg="#1a73e8")
        label_res_pow.config(text=f"pow()    : {res_pow:.6f}", fg="#d93025")
        
    except ValueError:
        messagebox.showerror("Lỗi dữ liệu", "Vui lòng nhập x là số thực và n là số nguyên!")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi toán học", "Không thể tính lũy thừa âm của 0!")

# --- Khởi tạo cửa sổ giao diện ---
root = tk.Tk()
root.title("Tính Lũy Thừa x^n")
root.geometry("400x300")
root.resizable(False, False)

# Tiêu đề
title = tk.Label(root, text="Chương Trình Tính x^n Tối Ưu", font=("Arial", 14, "bold"))
title.pack(pady=15)

# Frame nhập liệu
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Nhập x:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
entry_x = tk.Entry(input_frame, width=15)
entry_x.grid(row=0, column=1, padx=5, pady=5)
entry_x.insert(0, "8.5") # Giá trị mặc định theo ảnh

tk.Label(input_frame, text="Nhập n:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
entry_n = tk.Entry(input_frame, width=15)
entry_n.grid(row=1, column=1, padx=5, pady=5)
entry_n.insert(0, "-2") # Giá trị mặc định theo ảnh

# Nút tính toán
btn_calc = tk.Button(root, text="Tính toán", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=20)
btn_calc.pack(pady=10)

# Khu vực hiển thị kết quả
result_frame = tk.Frame(root, relief="sunken", borderwidth=1, padx=20, pady=10)
result_frame.pack(pady=10, fill="x", padx=40)

label_res_mypow = tk.Label(result_frame, text="mypow() : --", font=("Courier", 11, "bold"))
label_res_mypow.pack(anchor="w")

label_res_pow = tk.Label(result_frame, text="pow()    : --", font=("Courier", 11, "bold"))
label_res_pow.pack(anchor="w")

root.mainloop()