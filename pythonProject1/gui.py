# gui.py
import tkinter as tk

class ClipboardGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pistol Clipboard")
        self.root.iconbitmap(r'C:\Users\Miles\自制队列剪贴板\pythonProject1\icon.ico')

        self.toggle_topmost_button = tk.Button(self.root, text="Toggle Topmost", command=self.toggle_topmost)
        self.toggle_topmost_button.pack(side=tk.BOTTOM)

        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear Queue", command=self.clear_queue)
        self.clear_button.pack(pady=5)

        self.queue_manager = None

    def set_queue_manager(self, queue_manager):
        self.queue_manager = queue_manager

    def refresh_display(self):
        if self.queue_manager is not None:
            self.listbox.delete(0, tk.END)
            for item in self.queue_manager.clipboard_queue:
                self.listbox.insert(tk.END, item)

    def clear_queue(self):
        if self.queue_manager:
            self.queue_manager.clear()
            self.refresh_display()

    def run(self):
        self.root.mainloop()

    def toggle_topmost(self):
        # 检查当前是否已经是 topmost 状态
        is_topmost = self.root.wm_attributes('-topmost')
        # 切换状态
        self.root.wm_attributes('-topmost', not is_topmost)
        # 更新按钮文本来反映当前状态
        self.toggle_topmost_button.config(text="Disable Topmost" if is_topmost else "Enable Topmost")