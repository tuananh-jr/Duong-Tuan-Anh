import tkinter as tk
from tkinter import ttk, messagebox
import math

# ===== Hàm toán =====
def f(x):
    return (math.sin(x)**2) * math.cos(x)

def trapezoidal(a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return s * h

# ===== Xử lý =====
def tinh():
    try:
        eps = float(entry_eps.get())
        a, b = 0, math.pi/2

        n = 1
        I_old = trapezoidal(a, b, n)

        while True:
            n *= 2
            I_new = trapezoidal(a, b, n)
            if abs(I_new - I_old)/3 < eps:
                break
            I_old = I_new

        result.set(f"Kết quả ≈ {I_new:.10f}\nSố đoạn n = {n}")

    except:
        messagebox.showerror("Lỗi", "Nhập sai định dạng!")

# ===== GUI =====
root = tk.Tk()
root.title("Tính tích phân")
root.geometry("420x300")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")

# Frame chính
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Tiêu đề
title = ttk.Label(frame, text="TÍNH TÍCH PHÂN (HÌNH THANG)",
                  font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

# Công thức
formula = ttk.Label(frame,
    text="∫₀^(π/2) sin²(x)·cos(x) dx",
    font=("Segoe UI", 12))
formula.pack(pady=5)

# Input
input_frame = ttk.Frame(frame)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Độ chính xác ε:").grid(row=0, column=0, padx=5)

entry_eps = ttk.Entry(input_frame, width=15)
entry_eps.grid(row=0, column=1)
entry_eps.insert(0, "1e-6")

# Button
btn = ttk.Button(frame, text="Tính toán", command=tinh)
btn.pack(pady=10)

# Kết quả
result = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result,
                         font=("Segoe UI", 11),
                         foreground="blue")
result_label.pack(pady=10)

# Footer nhỏ
footer = ttk.Label(frame, text="PP Hình thang - Numerical Integration",
                   font=("Segoe UI", 8))
footer.pack(side="bottom", pady=5)

root.mainloop()