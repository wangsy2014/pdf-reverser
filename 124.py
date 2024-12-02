import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class PDFReverser:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PDF页面顺序反转工具")
        self.window.geometry("400x200")
        
        # 创建按钮和标签
        self.select_button = tk.Button(self.window, text="选择PDF文件", command=self.select_file)
        self.select_button.pack(pady=20)
        
        self.file_label = tk.Label(self.window, text="未选择文件")
        self.file_label.pack(pady=10)
        
        self.reverse_button = tk.Button(self.window, text="反转页面顺序", command=self.reverse_pdf)
        self.reverse_button.pack(pady=20)
        
        self.input_file_path = None
        
    def select_file(self):
        # 打开文件选择对话框
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            self.input_file_path = file_path
            self.file_label.config(text=f"已选择: {file_path}")
    
    def reverse_pdf(self):
        if not self.input_file_path:
            messagebox.showerror("错误", "请先选择PDF文件")
            return
            
        try:
            # 获取输出文件路径
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")]
            )
            
            if output_path:
                # 打开输入的PDF文件
                with open(self.input_file_path, 'rb') as input_file:
                    reader = PyPDF2.PdfReader(input_file)
                    writer = PyPDF2.PdfWriter()

                    # 获取总页数
                    num_pages = len(reader.pages)

                    # 反向添加页面到新的PDF
                    for page_num in range(num_pages - 1, -1, -1):
                        page = reader.pages[page_num]
                        writer.add_page(page)

                    # 写入到输出的PDF文件
                    with open(output_path, 'wb') as output_file:
                        writer.write(output_file)
                
                messagebox.showinfo("成功", "PDF页面顺序反转完成！")
        
        except Exception as e:
            messagebox.showerror("错误", f"处理PDF时出错：{str(e)}")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PDFReverser()
    app.run() 