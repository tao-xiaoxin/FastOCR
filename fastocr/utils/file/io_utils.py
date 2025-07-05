import io
from PyPDF2 import PdfReader

def get_pdf_page_count(pdf_content):
    """计算PDF页数"""
    try:
        # 使用BytesIO创建内存文件对象
        pdf_file = io.BytesIO(pdf_content)
        # 使用PyPDF2读取PDF
        pdf_reader = PdfReader(pdf_file)
        # 获取页数
        page_count = len(pdf_reader.pages)
        # logger.info(f"PDF页数: {page_count}")
        return page_count
    except Exception as e:
        # logger.warning(f"计算PDF页数时出错: {e}")
        return 1  # 如果出错，返回默认值1
