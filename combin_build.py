import subprocess
import sys
import os

def build_executable():
    """
    使用PyInstaller构建可执行文件
    命令: pyinstaller -F -w -n mytools.exe main.py
    """
    # 构建命令参数
    cmd = [
        'pyinstaller',
        '-F',           # 打包成单个可执行文件
        '-w',           # Windows GUI应用程序，无控制台窗口
        '-n', 'mytools.exe',  # 可执行文件名称
        'combin.py'       # 主程序文件
    ]
    
    print("开始构建可执行文件...")
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        # 执行构建命令
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("构建成功完成!")
        print("可执行文件位置: dist/mytools.exe")
        
        # 输出标准输出和标准错误
        if result.stdout:
            print("输出信息:")
            print(result.stdout)
            
        if result.stderr:
            print("警告信息:")
            print(result.stderr)
            
    except subprocess.CalledProcessError as e:
        print("构建过程中出现错误:")
        print(f"返回码: {e.returncode}")
        print(f"错误输出: {e.stderr}")
        print(f"标准输出: {e.stdout}")
        sys.exit(1)
        
    except FileNotFoundError:
        print("错误: 找不到pyinstaller命令，请确保已安装PyInstaller")
        print("可以通过以下命令安装: pip install pyinstaller")
        sys.exit(1)

if __name__ == "__main__":
    build_executable()