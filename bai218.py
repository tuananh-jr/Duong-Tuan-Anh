import tkinter as tk
from tkinter import messagebox

# Cấu trúc Node cho danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SelectionSortGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bài 218: Selection Sort Linked List (Hoán chuyển Node)")
        self.root.geometry("500x400")
        self.head = None

        # Giao diện
        tk.Label(root, text="Nhập số (cách nhau khoảng trắng):", font=("Arial", 10)).pack(pady=10)
        self.entry_input = tk.Entry(root, width=40)
        self.entry_input.pack(pady=5)
        self.entry_input.insert(0, "1 3 5 7 2 4 6 8") # Dữ liệu mẫu như trong sách 

        self.btn_sort = tk.Button(root, text="Bắt đầu sắp xếp", command=self.process_sort, bg="green", fg="white")
        self.btn_sort.pack(pady=10)

        tk.Label(root, text="Danh sách ban đầu:", font=("Arial", 10, "bold")).pack()
        self.lbl_original = tk.Label(root, text="", fg="blue")
        self.lbl_original.pack(pady=5)

        tk.Label(root, text="Danh sách sau khi sắp xếp:", font=("Arial", 10, "bold")).pack()
        self.lbl_result = tk.Label(root, text="", fg="red")
        self.lbl_result.pack(pady=5)

    def build_list(self, data_str):
        try:
            nums = [int(x) for x in data_str.split()]
            if not nums: return None
            head = Node(nums[0])
            current = head
            for val in nums[1:]:
                current.next = Node(val)
                current = current.next
            return head
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số nguyên!")
            return None

    def list_to_str(self, head):
        res = []
        curr = head
        while curr:
            res.append(f"[{curr.data}]")
            curr = curr.next
        return " -> ".join(res)

    def selection_sort_node_swap(self):
        # Thuật toán hoán chuyển node thực sự 
        if not self.head or not self.head.next:
            return

        # Dùng node giả (ghost node) để xử lý node đầu dễ hơn 
        dummy = Node(0)
        dummy.next = self.head
        
        # p1 là node trước p, p là node đang xét cố định để tìm min
        p1 = dummy
        while p1.next and p1.next.next:
            p = p1.next
            min_node = p
            min_prev = p1
            
            # Duyệt tìm node nhỏ nhất trong phần còn lại
            q1 = p
            while q1.next:
                q = q1.next
                if q.data < min_node.data:
                    min_node = q
                    min_prev = q1
                q1 = q1.next
            
            # Nếu tìm thấy node nhỏ hơn thì hoán chuyển node
            if min_node != p:
                # Nếu p và min_node kế tiếp nhau
                if p.next == min_node:
                    p.next = min_node.next
                    min_node.next = p
                    p1.next = min_node
                else:
                    # Hoán chuyển các liên kết next 
                    p_next = p.next
                    p.next = min_node.next
                    min_prev.next = p
                    min_node.next = p_next
                    p1.next = min_node
                
                # Sau khi swap node, p cũ giờ nằm ở vị trí min_node, 
                # ta cần gán lại p là node vừa được đưa lên đầu đoạn để duyệt tiếp
                p = p1.next 
            
            p1 = p # Chuyển sang vị trí kế tiếp
            
        self.head = dummy.next

    def process_sort(self):
        input_data = self.entry_input.get()
        self.head = self.build_list(input_data)
        if not self.head: return

        self.lbl_original.config(text=self.list_to_str(self.head))
        
        self.selection_sort_node_swap()
        
        self.lbl_result.config(text=self.list_to_str(self.head))

if __name__ == "__main__":
    root = tk.Tk()
    app = SelectionSortGUI(root)
    root.mainloop()