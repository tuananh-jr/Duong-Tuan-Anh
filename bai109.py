import tkinter as tk

# Hàm tạo ma trận theo quy luật
def create_matrix(n=5):
    nums = list(range(1, n*n + 1))
    matrix = [[0]*n for _ in range(n)]
    diagonals = [[] for _ in range(2*n - 1)]

    # Gom các phần tử theo đường chéo phụ (i+j = const)
    idx = 0
    for s in range(2*n - 1):
        for i in range(n):
            j = s - i
            if 0 <= j < n:
                diagonals[s].append((i, j))

    # Ghi số vào các đường chéo, đổi chiều xen kẽ
    for k, diag in enumerate(diagonals):
        if k % 2 == 0:
            for (i, j) in diag:
                matrix[i][j] = nums[idx]
                idx += 1
        else:
            for (i, j) in reversed(diag):
                matrix[i][j] = nums[idx]
                idx += 1
    return matrix

# Xử lý khi nhấn nút
def on_generate():
    matrix = create_matrix(5)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "Ma trận 5x5:\n\n")
    for row in matrix:
        text_result.insert(tk.END, " ".join(f"{val:3d}" for val in row) + "\n")

# Tạo giao diện
root = tk.Tk()
root.title("Bài 109: Ma trận 5x5 theo đường chéo")
root.geometry("500x400")
root.configure(bg="#f0f8ff")

# Tiêu đề
title = tk.Label(root, text="Tạo ma trận 5x5 với số từ 1 đến 25",
                 font=("Segoe UI", 13, "bold"), bg="#f0f8ff", fg="#1a73e8")
title.pack(pady=10)

# Nút tạo
btn_generate = tk.Button(root, text="Tạo ma trận", font=("Segoe UI", 11, "bold"),
                         bg="#1a73e8", fg="white", width=15, command=on_generate)
btn_generate.pack(pady=10)

# Khung kết quả
frame_result = tk.Frame(root, bg="#e8f0fe", bd=2, relief="groove")
frame_result.pack(padx=20, pady=10, fill="both", expand=True)

text_result = tk.Text(frame_result, font=("Consolas", 12), bg="#ffffff", fg="#202124", wrap="word")
text_result.pack(padx=10, pady=10, fill="both", expand=True)

# Chạy chương trình
root.mainloop()