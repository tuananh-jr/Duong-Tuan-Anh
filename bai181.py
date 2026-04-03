import tkinter as tk
from tkinter import filedialog, messagebox
import os

def solve_181():
    search_str = entry_search.get()
    file_path = label_path.cget("text")
    
    if not search_str:
        messagebox.showwarning("Thông báo", "Vui lòng nhập chuỗi cần tìm!")
        return
    
    if not os.path.exists(file_path) or file_path == "Chưa chọn file":
        messagebox.showwarning("Thông báo", "Vui lòng chọn một file văn bản!")
        return

    try:
        results = ""
        # Mở file với encoding utf-8 để đọc tiếng Việt nếu có
        with open(file_path, 'r', encoding='utf-8') as f:
            for idx, line in enumerate(f):
                if search_str in line:
                    positions = []
                    start = 0
                    # Tìm tất cả các vị trí xuất hiện của chuỗi s trong dòng
                    while True:
                        pos = line.find(search_str, start)
                        if pos == -1: break
                        positions.append(str(pos))
                        start = pos + 1
                    
                    if positions:
                        results += f"Dòng {idx}: {' '.join(positions)}\n"
        
        # Hiển thị kết quả lên Textbox
        text_res.config(state='normal') # Cho phép sửa nội dung để chèn kết quả
        text_res.delete("1.0", tk.END)
        if results:
            text_res.insert(tk.END, results)
        else:
            text_res.insert(tk.END, f"Không tìm thấy chuỗi '{search_str}' trong file.")
        text_res.config(state='disabled') # Khóa không cho người dùng sửa kết quả
            
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi đọc file: {e}")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Chọn file văn bản",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        label_path.config(text=file_path, fg="blue")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Bài 181: Tìm vị trí chuỗi trong File (Tkinter)")
root.geometry("550x500")

# Các thành phần giao diện
tk.Label(root, text="CHƯƠNG TRÌNH TÌM VỊ TRÍ CHUỖI S TRONG FILE", font=("Arial", 12, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Chuỗi cần tìm:").grid(row=0, column=0, padx=5)
entry_search = tk.Entry(frame_input, width=30)
entry_search.grid(row=0, column=1, padx=5)

btn_browse = tk.Button(root, text="Chọn File Văn Bản", command=select_file)
btn_browse.pack(pady=5)

label_path = tk.Label(root, text="Chưa chọn file", fg="gray", wraplength=500)
label_path.pack(pady=5)

btn_run = tk.Button(root, text="TÌM KIẾM", command=solve_181, bg="green", fg="white", width=15, font=("Arial", 10, "bold"))
btn_run.pack(pady=15)
tk.Label(root, text="Kết quả (Dòng: Các vị trí):").pack(anchor="w", padx=25)
text_res = tk.Text(root, width=60, height=12, state='disabled', bg="#f0f0f0")
text_res.pack(pady=5, padx=20)

root.mainloop()