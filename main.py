"""
@filename: main.py
@author: Edom
@time:2024-5-21
"""

import os
from docx import Document
import re

# 从自定义模块导入功能
from Test_Script_Utils.input_utils import get_input_text, extract_value, validate_input, extract_and_map_text
from Test_Script_Utils.doc_utils import (
    replace_table_value,
    remove_extra_steps,
    center_align_table_text,
    format_table_text,
    format_table_content
)


def main():
    # 获取用户输入文本
    input_text = get_input_text()

    # 验证用户输入
    errors = validate_input(input_text)
    if errors:
        for error in errors:
            print(error)
        return

    # 打开Word文档
    try:
        doc = Document('Testcase_Template.docx')
    except Exception as e:
        print(f"无法打开文档: {e}")
        return

    # 提取id_value和Module_Name_value
    value_id = extract_value(r'id_value:\s*(\d+)', input_text)
    value_name = extract_value(r'Module_Name_value:\s*([^;]+?);', input_text)

    if not value_id or not value_name:
        print("缺少id_value或Module_Name_value")
        return

    outDocName = f"Test-case_{value_id}_{value_name}"

    # 统计用户输入的测试步骤数
    num_steps = len(re.findall(r'Test Step\d+:', input_text))

    print(f'输入数据中包含 Test Step 数为：{num_steps}')
    # 根据输入步骤数删除多余行
    remove_extra_steps(doc, num_steps)

    # 提取并映射文本
    result = extract_and_map_text(input_text)

    # 替换文档中的文本
    for key, value in result.items():
        replace_table_value(doc, key, value)

    # 表格文本居中对齐
    center_align_table_text(doc)

    # 格式化表格文本和内容
    format_table_text(doc.tables)
    format_table_content(doc.tables)

    output_folder = 'TestCase'

    # 确保目录存在
    os.makedirs(output_folder, exist_ok=True)

    # 保存修改后的文档
    output_file = os.path.join(output_folder, f"{outDocName}.docx")
    try:
        doc.save(output_file)
        print(f'输出路径为：{output_file}')
        print("finished")
    except Exception as e:
        print(f"无法保存文档: {e}")
        print("请确保文档未被打开。")


if __name__ == "__main__":
    main()
