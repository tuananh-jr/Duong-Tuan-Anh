import tkinter as tk
from tkinter import messagebox
import math

def calculate_position():
    try:
        # Lấy dữ liệu từ các ô nhập
        xc = float(entry_xc.get())
        yc = float(entry_yc.get())
        r  = float(entry_r.get())
        xm = float(entry_xm.get())
        ym = float(entry_ym.get())

        if r < 0:
            messagebox.showerror("Lỗi", "Bán kính R không được âm!")
            return

        # Tính khoảng cách d từ tâm C đến điểm M
        # Công thức: d = sqrt((xM - xC)^2 + (yM - yC)^2)
        distance = math.sqrt((xm - xc)**2 + (ym - yc)**2)

        # Xác định vị trí
        if math.isclose(distance, r, rel_tol=1e-9):
            result_text = "M nằm TRÊN đường tròn C()"
            color = "#2980b9" # Xanh dương
        elif distance < r:
            result_text = "M nằm TRONG đường tròn C()"
            color = "#27ae60" # Xanh lá
        else:
            result_text = "M nằm NGOÀI đường tròn C()"
            color = "#e67e22" # Cam

        # Hiển thị kết quả lên giao diện
        label_res.config(text=result_text, fg=color)
        label_dist.config(text=f"Khoảng cách d = {distance:.2f} (R = {r})")

    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng chỉ nhập các chữ số!")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Circle Geometry Tool")
root.geometry("400x450")
root.configure(bg="#f5f6fa")

# Tiêu đề
tk.Label(root, text="VỊ TRÍ ĐIỂM M & ĐƯỜNG TRÒN", font=("Arial", 14, "bold"), 
         bg="#f5f6fa", fg="#2f3640").pack(pady=20)

# Khung nhập liệu (Container)
frame = tk.Frame(root, bg="#f5f6fa")
frame.pack(padx=20)

def create_input(label_text, default_val):
    row = tk.Frame(frame, bg="#f5f6fa")
    row.pack(fill="x", pady=5)
    tk.Label(row, text=label_text, width=15, anchor="w", bg="#f5f6fa", font=("Arial", 10)).pack(side="left")
    entry = tk.Entry(row, font=("Arial", 10), bd=1, relief="solid")
    entry.insert(0, default_val)
    entry.pack(side="right", expand=True, fill="x")
    return entry

entry_xc = create_input("Tâm xC:", "0.5")
entry_yc = create_input("Tâm yC:", "4.3")
entry_r  = create_input("Bán kính R:", "7.4")
entry_xm = create_input("Điểm xM:", "3.2")
entry_ym = create_input("Điểm yM:", "6.5")

# Nút tính toán
btn_calc = tk.Button(root, text="KIỂM TRA VỊ TRÍ", command=calculate_position,
                     bg="#8e44ad", fg="white", font=("Arial", 11, "bold"),
                     padx=20, pady=10, bd=0, cursor="hand2")
btn_calc.pack(pady=25)

# Vùng hiển thị kết quả
label_res = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f5f6fa")
label_res.pack()

label_dist = tk.Label(root, text="", font=("Arial", 9), bg="#f5f6fa", fg="#7f8c8d")
label_dist.pack(pady=5)

root.mainloop()

root.mainloop()
