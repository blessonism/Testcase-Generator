"""
@filename:doc_utils.py
@author:JunLeon
@time:2024-05-21
"""


def replace_table_value(doc, old_value, new_value):
    """替换Word文档表格中的文本"""
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if old_value in paragraph.text:
                        paragraph.text = paragraph.text.replace(old_value, new_value)


def clear_rows_with_text(table, text_to_clear):
    """清除包含特定文本的行"""
    rows_to_clear = []
    for row in table.rows:
        cell_texts = [cell.text.strip() for cell in row.cells]
        if any(keyword in cell_texts for keyword in text_to_clear):
            rows_to_clear.append(row)

    for row in rows_to_clear:
        table._element.remove(row._element)


def remove_extra_steps(doc, num_steps):
    """根据用户输入的测试步骤数，删除多余的行"""
    step_keywords = [f"Test Step{i}" for i in range(num_steps + 1, 9)]
    for table in doc.tables:
        clear_rows_with_text(table, step_keywords)


def center_align_table_text(doc):
    """将所有表格中的文本居中对齐"""
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.alignment = 1  # 1表示居中对齐
