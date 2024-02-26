import tkinter as tk

class ClipboardGUI:
    def __init__(self, queue_manager=None):
        self.root = tk.Tk()
        self.root.title("My Clipboard Manager")
        self.root.iconbitmap('C:\\Users\Miles\自制队列剪贴板\pythonProject1\\icon.ico')  # 确保图标文件在正确路径

        # 创建文本框（Listbox）来显示队列内容
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 创建一个框架来放置按钮，使其能够居中放置在窗口的底部
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # 加载按钮图标，确保图标文件存在
        self.topmost_icon = tk.PhotoImage(file='C:\\Users\Miles\自制队列剪贴板\pythonProject1\\topmost_icon.png')  # 按钮图标文件
        self.clear_icon = tk.PhotoImage(file='C:\\Users\Miles\自制队列剪贴板\pythonProject1\\clear_icon.png')  # 另一个按钮图标文件

        # 在button_frame中创建另一个框架container_frame来包含按钮
        self.container_frame = tk.Frame(self.button_frame)
        self.container_frame.pack(expand=True)

        # 创建置顶按钮并添加到container_frame中
        self.toggle_topmost_button = tk.Button(self.container_frame, image=self.topmost_icon, command=self.toggle_topmost)
        self.toggle_topmost_button.pack(side=tk.LEFT, padx=2, pady=5)

        # 创建清空队列按钮并添加到container_frame中
        self.clear_button = tk.Button(self.container_frame, image=self.clear_icon, command=self.clear_queue)
        self.clear_button.pack(side=tk.LEFT, padx=2, pady=5)

        self.queue_manager = queue_manager
        # 初始化一个变量来追踪窗口的置顶状态
        self.is_topmost = False
        if self.queue_manager:
            self.refresh_display()

    def toggle_topmost(self):
        """切换窗口的置顶状态"""
        self.is_topmost = not self.is_topmost
        self.root.attributes('-topmost', self.is_topmost)

    def clear_queue(self):
        """清空队列并更新显示"""
        if self.queue_manager:
            self.queue_manager.clear()
            self.refresh_display()

    def refresh_display(self):
        """从队列管理器获取队列内容并在列表框中显示"""
        self.listbox.delete(0, tk.END)
        for item in self.queue_manager.clipboard_queue:
            self.listbox.insert(tk.END, item)

    def run(self):
        """启动GUI的主循环"""
        self.root.mainloop()

# 注意：确保替换图标和图片文件的路径为你实际使用的路径。
