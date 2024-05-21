"""
@filename: main.py
@author: Edom
@time:2024-5-21
"""

import re


def get_input_text():
    """读取用户的多行输入"""
    input_text = ""
    try:
        while True:
            line = input()
            if not line:
                break
            input_text += line + "\n"
    except EOFError:
        pass
    return input_text


def extract_value(pattern, text):
    """使用正则表达式提取值"""
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return ""


def validate_input(input_text):
    """验证用户输入的规范性"""
    errors = []

    patterns = {
        "id_value": r'id_value:\s*\d+',
        "Module_Name_value": r'Module_Name_value:\s*[^;]+;',
        "Author_value": r'Author_value:\s*[^;]+;',
        "Date_value": r'Date_value:\s*\d{4}\.\d{2}\.\d{2};',
        "Test_Title_value": r'Test_Title_value:\s*[^;]+;',
        "Description_value": r'Description_value:\s*[^;]+;',
        "pre-conditions_value": r'pre-conditions_value:\s*[^;]+;',
        "Test_Step": r'Test Step\d+:\s*[^;]+;',
        "Test_Data": r'Test Data\d+:\s*[^;]+',
        "Expected_Result": r'Expected Result\d+:\s*[^;]+;',
        "Actual_Result": r'Actual Result\d+:\s*[^;]+;',
        "Post_conditions_value": r'Post-conditions_value:\s*[^;.]+[;.]'
    }

    for key, pattern in patterns.items():
        if key.startswith("Test_Step") or key.startswith("Test_Data") or key.startswith("Expected_Result") or key.startswith("Actual_Result"):
            matches = re.findall(pattern, input_text)
            if not matches:
                errors.append(f"缺少或不符合规范的 {key} 条目。")
        else:
            if not re.search(pattern, input_text):
                errors.append(f"缺少或不符合规范的 {key} 条目。")

    return errors


def extract_and_map_text(input_text):
    """提取并映射文本"""
    text_map = {}
    lines = input_text.strip().split('\n')

    for line in lines:
        key, value = line.split(': ', 1)
        text_map[key] = value

    return text_map
