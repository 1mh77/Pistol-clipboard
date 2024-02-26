# main.py
import keyboard
from clipboard import set_clipboard_text, get_clipboard_text
from gui import ClipboardGUI
import threading
from collections import deque
import time

class ClipboardQueueManager:
    def __init__(self, update_gui_callback):
        self.clipboard_queue = deque()
        self.update_gui_callback = update_gui_callback

    def copy_clipboard(self):
        # 模拟Ctrl+C按键以复制选中的文本
        keyboard.send('ctrl+c')
        # 稍等片刻，等待系统处理复制操作
        time.sleep(0.1)  # 延时确保剪贴板内容已更新，需要时可调整
        # 获取剪贴板上的文本并添加到队列中
        text = get_clipboard_text()
        if text:
            self.clipboard_queue.append(text)
            if self.update_gui_callback:
                self.update_gui_callback()

    def paste_clipboard(self):
        if self.clipboard_queue:
            text = self.clipboard_queue.popleft()
            set_clipboard_text(text)
            # 模拟Ctrl+V按键以粘贴文本
            keyboard.send('ctrl+v')
            if self.update_gui_callback:
                self.update_gui_callback()

    def clear(self):
        self.clipboard_queue.clear()
        if self.update_gui_callback:
            self.update_gui_callback()

def setup_hotkeys(queue_manager):
    # 注册全局快捷键Ctrl+C
    keyboard.add_hotkey('ctrl+c', queue_manager.copy_clipboard, suppress=True)
    # 注册粘贴快捷键Ctrl+Shift+V
    keyboard.add_hotkey('ctrl+v', queue_manager.paste_clipboard, suppress=True)

def main():
    queue_manager = ClipboardQueueManager(None)
    # 直接在创建GUI实例时传递queue_manager
    gui = ClipboardGUI(queue_manager)

    # 设置队列管理器的GUI更新回调
    queue_manager.update_gui_callback = gui.refresh_display

    # 在后台线程中设置快捷键
    hotkey_thread = threading.Thread(target=setup_hotkeys, args=(queue_manager,))
    hotkey_thread.daemon = True
    hotkey_thread.start()

    gui.run()

if __name__ == "__main__":
    main()
