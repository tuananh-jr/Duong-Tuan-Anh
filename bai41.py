import tkinter as tk
from tkinter import messagebox
import itertools

# Tính giá trị biểu thức với các phép toán
def evaluate_expression(ops):
    expr = f"((((1 {ops[0]} 2) {ops[1]} 3) {ops[2]} 4) {ops[3]} 5) {ops[4]} 6"
    try:
        value = eval(expr)
        return value, expr
    except ZeroDivisionError:
        return None, expr

# Tìm các tổ hợp phép toán cho ra kết quả 36
def find_solutions():
    operators = ['+', '-', '*', '/']
    solutions = []
    for ops in itertools.product(operators, repeat=5):
        val, expr = evaluate_expression(ops)
        if val is not None and abs(val - 36) < 1e-9:
            solutions.append(expr)
    return solutions

# Xử lý khi nhấn nút "Tìm"
def on_find():
    results = find_solutions()
    if results:
        text_result.delete("1.0", tk.END)
        for expr in results:
            text_result.insert(tk.END, f"{expr} = 36\n")
    else:
        messagebox.showinfo("Kết quả", "Không tìm thấy biểu thức nào bằng 36.")

# Tạo giao diện
root = tk.Tk()
root.title("Bài 41: Thay dấu hỏi để được 36")
root.geometry("520x400")
root.configure(bg="#f0f8ff")

# Tiêu đề
title = tk.Label(root, text="((((1 ? 2) ? 3) ? 4) ? 5) ? 6 = 36",
                 font=("Segoe UI", 13, "bold"), bg="#f0f8ff", fg="#1a73e8")
title.pack(pady=10)

# Hướng dẫn
guide = tk.Label(root, text="Tìm cách thay ? bằng +, -, *, / sao cho biểu thức = 36",
                 font=("Segoe UI", 10), bg="#f0f8ff")
guide.pack()

# Nút tìm
btn_find = tk.Button(root, text="Tìm kết quả", font=("Segoe UI", 11, "bold"),
                     bg="#1a73e8", fg="white", width=12, command=on_find)
btn_find.pack(pady=10)

# Khung kết quả
frame_result = tk.Frame(root, bg="#e8f0fe", bd=2, relief="groove")
frame_result.pack(padx=20, pady=10, fill="both", expand=True)

text_result = tk.Text(frame_result, font=("Consolas", 11), bg="#ffffff", fg="#202124", wrap="word")
text_result.pack(padx=10, pady=10, fill="both", expand=True)

# Chạy chương trình
root.mainloop()