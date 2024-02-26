# clipboard.py
import win32clipboard as clipboard
import win32con

def set_clipboard_text(text):
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    clipboard.CloseClipboard()

def get_clipboard_text():
    clipboard.OpenClipboard()
    try:
        text = clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    except Exception as e:
        print(e)
        text = ''  # 如果剪贴板为空或不包含文本，则返回空字符串
    finally:
        clipboard.CloseClipboard()
    return text
