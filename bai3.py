import math
import tkinter as tk
from tkinter import messagebox

# Hàm kiểm tra
def kiem_tra():
    try:
        xC = float(entry_xC.get())
        yC = float(entry_yC.get())
        R = float(entry_R.get())
        xM = float(entry_xM.get())
        yM = float(entry_yM.get())

        CM = math.sqrt((xM - xC)**2 + (yM - yC)**2)

        if CM == R:
            kq = "M nằm trên đường tròn"
        elif CM < R:
            kq = "M nằm trong đường tròn"
        else:
            kq = "M nằm ngoài đường tròn"

        ket_qua.set(kq)

        # Vẽ hình
        canvas.delete("all")

        scale = 20  # tỷ lệ phóng to
        offset = 200  # dịch tâm ra giữa canvas

        # Tọa độ trên canvas
        xC_draw = xC * scale + offset
        yC_draw = -yC * scale + offset
        xM_draw = xM * scale + offset
        yM_draw = -yM * scale + offset

        # Vẽ đường tròn
        canvas.create_oval(
            xC_draw - R*scale, yC_draw - R*scale,
            xC_draw + R*scale, yC_draw + R*scale,
            outline="blue"
        )

        # Vẽ tâm C
        canvas.create_oval(
            xC_draw-3, yC_draw-3, xC_draw+3, yC_draw+3,
            fill="black"
        )
        canvas.create_text(xC_draw, yC_draw-10, text="C")

        # Vẽ điểm M
        canvas.create_oval(
            xM_draw-3, yM_draw-3, xM_draw+3, yM_draw+3,
            fill="red"
        )
        canvas.create_text(xM_draw, yM_draw-10, text="M")

    except:
        messagebox.showerror("Lỗi", "Nhập sai dữ liệu!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Bài 3 - Điểm và đường tròn")

# Nhập dữ liệu
tk.Label(root, text="C(xC, yC):").grid(row=0, column=0)
entry_xC = tk.Entry(root, width=5)
entry_xC.grid(row=0, column=1)
entry_yC = tk.Entry(root, width=5)
entry_yC.grid(row=0, column=2)

tk.Label(root, text="R:").grid(row=1, column=0)
entry_R = tk.Entry(root, width=5)
entry_R.grid(row=1, column=1)

tk.Label(root, text="M(xM, yM):").grid(row=2, column=0)
entry_xM = tk.Entry(root, width=5)
entry_xM.grid(row=2, column=1)
entry_yM = tk.Entry(root, width=5)
entry_yM.grid(row=2, column=2)

# Nút bấm
tk.Button(root, text="Kiểm tra", command=kiem_tra).grid(row=3, column=1)

# Kết quả
ket_qua = tk.StringVar()
tk.Label(root, textvariable=ket_qua, fg="blue").grid(row=4, column=1)

# Canvas vẽ
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.grid(row=5, column=0, columnspan=3)

root.mainloop()