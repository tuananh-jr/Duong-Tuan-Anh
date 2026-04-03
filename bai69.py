import tkinter as tk
from tkinter import messagebox
import random

# Hàm tạo mảng ngẫu nhiên
def generate_array(n):
    return [random.randint(-100, 100) for _ in range(n)]

# Hàm tìm "run" tăng dài nhất đầu tiên
def longest_increasing_run(arr):
    if not arr:
        return []
    longest = []
    current = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current.append(arr[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [arr[i]]
    if len(current) > len(longest):
        longest = current
    return longest

# Xử lý khi nhấn nút
def on_generate():
    try:
        n = int(entry_n.get())
        if not (1 <= n <= 99):
            raise ValueError
        arr = generate_array(n)
        run = longest_increasing_run(arr)
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, f"Mảng ngẫu nhiên ({n} phần tử):\n{arr}\n\n")
        text_result.insert(tk.END, f'"run" tăng dài nhất đầu tiên:\n{run}')
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập n trong khoảng [1, 99]!")

# Tạo giao diện
root = tk.Tk()
root.title("Bài 69: Tìm 'run' tăng dài nhất")
root.geometry("600x400")
root.configure(bg="#f0f8ff")

# Tiêu đề
title = tk.Label(root, text="Tạo mảng ngẫu nhiên và tìm 'run' tăng dài nhất",
                 font=("Segoe UI", 13, "bold"), bg="#f0f8ff", fg="#1a73e8")
title.pack(pady=10)

# Hướng dẫn
guide = tk.Label(root, text="Nhập số phần tử n (1–99):",
                 font=("Segoe UI", 10), bg="#f0f8ff")
guide.pack()

# Ô nhập
entry_n = tk.Entry(root, font=("Segoe UI", 11), width=10, justify="center")
entry_n.pack(pady=5)

# Nút tạo
btn_generate = tk.Button(root, text="Tạo và tìm 'run'", font=("Segoe UI", 11, "bold"),
                         bg="#1a73e8", fg="white", width=15, command=on_generate)
btn_generate.pack(pady=10)

# Khung kết quả
frame_result = tk.Frame(root, bg="#e8f0fe", bd=2, relief="groove")
frame_result.pack(padx=20, pady=10, fill="both", expand=True)

text_result = tk.Text(frame_result, font=("Consolas", 11), bg="#ffffff", fg="#202124", wrap="word")
text_result.pack(padx=10, pady=10, fill="both", expand=True)

# Chạy chương trình
root.mainloop()