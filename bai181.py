import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def search_in_file():
    file_path = entry_file.get()
    search_str = entry_search.get()
    
    if not file_path or not search_str:
        messagebox.showwarning("Chú ý", "Vui lòng chọn file và nhập chuỗi cần tìm!")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        result_area.config(state=tk.NORMAL) # Cho phép ghi vào vùng kết quả
        result_area.delete('1.0', tk.END)    # Xóa kết quả cũ
        
        found = False
        for line_idx, line in enumerate(lines):
            if search_str in line:
                found = True
                # Tìm tất cả vị trí xuất hiện của chuỗi trong dòng
                positions = []
                start_pos = 0
                while True:
                    idx = line.find(search_str, start_pos)
                    if idx == -1: break
                    positions.append(str(idx))
                    start_pos = idx + 1
                
                # Hiển thị kết quả dạng: Dong X: vị trí 1, vị trí 2...
                result_area.insert(tk.END, f"Dong {line_idx}: {' '.join(positions)}\n")
        
        if not found:
            result_area.insert(tk.END, "Không tìm thấy chuỗi yêu cầu trong tập tin.")
        
        result_area.config(state=tk.DISABLED) # Khóa vùng kết quả (chỉ đọc)
        
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy tập tin!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)

# --- Thiết lập Giao diện ---
root = tk.Tk()
root.title("Trình Tìm Kiếm Nội Dung File")
root.geometry("500x550")
root.configure(bg="#f0f2f5")

# Tiêu đề
tk.Label(root, text="TÌM VỊ TRÍ CHUỖI TRONG FILE", font=("Helvetica", 14, "bold"), 
         bg="#f0f2f5", fg="#1a73e8").pack(pady=20)

# Khung nhập liệu
input_frame = tk.Frame(root, bg="#f0f2f5")
input_frame.pack(padx=20, fill="x")

# Chọn File
tk.Label(input_frame, text="Đường dẫn file:", bg="#f0f2f5").pack(anchor="w")
file_sub_frame = tk.Frame(input_frame, bg="#f0f2f5")
file_sub_frame.pack(fill="x", pady=(0, 10))

entry_file = tk.Entry(file_sub_frame, font=("Arial", 10))
entry_file.pack(side="left", expand=True, fill="x", padx=(0, 5))
btn_browse = tk.Button(file_sub_frame, text="Chọn File...", command=browse_file, bg="#e1e4e8")
btn_browse.pack(side="right")

# Nhập chuỗi tìm kiếm
tk.Label(input_frame, text="Chuỗi cần tìm (s):", bg="#f0f2f5").pack(anchor="w")
entry_search = tk.Entry(input_frame, font=("Arial", 12), bd=1, relief="solid")
entry_search.pack(fill="x", pady=(0, 20))

# Nút thực hiện
btn_search = tk.Button(root, text="BẮT ĐẦU TÌM KIẾM", command=search_in_file,
                       bg="#1a73e8", fg="white", font=("Arial", 11, "bold"),
                       pady=10, cursor="hand2", bd=0)
btn_search.pack(pady=10)

# Vùng hiển thị kết quả (ScrolledText)
tk.Label(root, text="Kết quả chi tiết:", bg="#f0f2f5", font=("Arial", 9, "italic")).pack(anchor="w", padx=20)
result_area = scrolledtext.ScrolledText(root, height=12, font=("Consolas", 11), 
                                        bg="white", state=tk.DISABLED)
result_area.pack(padx=20, pady=5, fill="both", expand=True)

root.mainloop()
