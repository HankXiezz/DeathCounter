import tkinter as tk
import keyboard

# 初始化计数器
death_count = 0
input_buffer = ""


# 更新计数器显示
def update_display():
    global death_count
    label.config(text=f"死亡次数: {death_count}")

# 处理加号键按下事件
def on_key_event():
    global death_count
    death_count += 1
    update_display()

# 处理键盘输入
def on_key_input(event):
    global input_buffer
    key = event.name  # 获取键的名称
    if key.isdigit():  # 只处理数字键
        input_buffer += key
        # 保持缓冲区长度为4
        input_buffer = input_buffer[-3:]

        if input_buffer == "336":
            on_closing()
# 创建主窗口
root = tk.Tk()
root.title("死亡计数器")

# 将窗口置于最顶层
root.attributes("-topmost", True)

# 禁止调整窗口大小
root.resizable(False, False)
root.overrideredirect(True)
root.geometry("300x100")

# 设置窗口透明度
root.wm_attributes('-transparentcolor', root['bg'])

# # 创建标签用于显示计数
# label = tk.Label(root, text=f"死亡次数: {death_count}", font=("Arial", 24), fg='black')
# label.pack(padx=22, pady=22)
# 创建白色文字标签
label = tk.Label(root, text=f"死亡次数: {death_count}", font=("Arial", 24), fg='white')
label.place(x=20, y=20)  # 与阴影标签重叠

# 绑定加号键（小键盘和主键盘）
keyboard.add_hotkey('1', on_key_event)
# 绑定数字输入，用于退出程序
keyboard.on_press(on_key_input)

# 绑定关闭事件，解除按键监听
def on_closing():
    keyboard.unhook_all_hotkeys()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# 运行主窗口
root.mainloop()