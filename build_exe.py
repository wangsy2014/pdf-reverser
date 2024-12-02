import PyInstaller.__main__
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 打包参数
params = [
    '124.py',
    '--name=PDF页面顺序反转工具',
    '--windowed',
    '--onefile',
    '--clean',
    '--noconfirm',
    f'--distpath={os.path.join(current_dir, "dist")}',
    f'--workpath={os.path.join(current_dir, "build")}',
    '--add-data=README.md;.'  # 如果有其他资源文件
]

# 执行打包
PyInstaller.__main__.run(params) 