import tkinter as tk
from tkinter import messagebox
import math

# Hàm tạo ma trận
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            val = math.sin((i - 2 * j) / math.pi)
            row.append(val)
        matrix.append(row)
    return matrix

# Hàm đếm số phần tử không âm
def count_non_negative(matrix):
    return sum(1 for row in matrix for val in row if val >= 0)

# Xử lý khi nhấn nút
def on_generate():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError
        matrix = create_matrix(n)
        count = count_non_negative(matrix)
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, f"Ma trận A ({n}x{n}):\n")
        for row in matrix:
            text_result.insert(tk.END, " ".join(f"{val:.6f}" for val in row) + "\n")
        text_result.insert(tk.END, f"\nCó {count} phần tử không âm")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập n là số nguyên dương!")

# Tạo giao diện
root = tk.Tk()
root.title("Bài 96: Ma trận và đếm phần tử không âm")
root.geometry("640x480")
root.configure(bg="#f0f8ff")

# Tiêu đề
title = tk.Label(root, text="Tạo ma trận A và đếm phần tử không âm",
                 font=("Segoe UI", 13, "bold"), bg="#f0f8ff", fg="#1a73e8")
title.pack(pady=10)

# Hướng dẫn
guide = tk.Label(root, text="Nhập bậc ma trận n:",
                 font=("Segoe UI", 10), bg="#f0f8ff")
guide.pack()

# Ô nhập
entry_n = tk.Entry(root, font=("Segoe UI", 11), width=10, justify="center")
entry_n.pack(pady=5)

# Nút tạo
btn_generate = tk.Button(root, text="Tạo ma trận", font=("Segoe UI", 11, "bold"),
                         bg="#1a73e8", fg="white", width=15, command=on_generate)
btn_generate.pack(pady=10)

# Khung kết quả
frame_result = tk.Frame(root, bg="#e8f0fe", bd=2, relief="groove")
frame_result.pack(padx=20, pady=10, fill="both", expand=True)

text_result = tk.Text(frame_result, font=("Consolas", 11), bg="#ffffff", fg="#202124", wrap="word")
text_result.pack(padx=10, pady=10, fill="both", expand=True)

# Chạy chương trình
root.mainloop()