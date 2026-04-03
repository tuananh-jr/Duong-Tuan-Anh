import tkinter as tk
from tkinter import messagebox

def selection_sort_recursive(arr, n, index=0):
    # Điều kiện dừng: nếu đã duyệt hết mảng
    if index == n:
        return
    
    # Tìm phần tử nhỏ nhất trong đoạn còn lại
    min_idx = index
    for j in range(index + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
            
    # Hoán đổi phần tử nhỏ nhất với phần tử ở vị trí hiện tại
    arr[index], arr[min_idx] = arr[min_idx], arr[index]
    
    # Gọi đệ quy cho vị trí tiếp theo
    selection_sort_recursive(arr, n, index + 1)

def handle_sort():
    try:
        # Lấy dữ liệu từ ô nhập liệu
        input_str = entry.get()
        # Chuyển chuỗi thành danh sách số nguyên
        arr = [int(x) for x in input_str.split()]
        
        if not arr:
            messagebox.showwarning("Lỗi", "Vui lòng nhập mảng số!")
            return

        # Thực hiện sắp xếp đệ quy
        selection_sort_recursive(arr, len(arr))
        
        # Hiển thị kết quả lên giao diện
        result_label.config(text=f"Mảng sau khi sắp xếp: {' '.join(map(str, arr))}", fg="#2ecc71")
    except ValueError:
        messagebox.showerror("Lỗi", "Dữ liệu nhập vào phải là các số nguyên cách nhau bằng dấu cách.")

# --- Thiết lập giao diện đồ họa (GUI) ---
root = tk.Tk()
root.title("Selection Sort Đệ Quy")
root.geometry("450x250")

# Tiêu đề
title = tk.Label(root, text="Sắp Xếp Chọn (Recursive Selection Sort)", font=("Arial", 12, "bold"))
title.pack(pady=10)

# Ô nhập mảng
instructions = tk.Label(root, text="Nhập mảng (ví dụ: 3 5 4 6 7 1 2):")
instructions.pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.insert(0, "3 5 4 6 7 1 2") # Dữ liệu mẫu từ ảnh của bạn

# Nút thực hiện
sort_button = tk.Button(root, text="Sắp Xếp", command=handle_sort, bg="#3498db", fg="white", padx=20)
sort_button.pack(pady=10)

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="Kết quả sẽ hiển thị ở đây", font=("Arial", 10, "italic"))
result_label.pack(pady=10)

root.mainloop()
