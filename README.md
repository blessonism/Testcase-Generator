# Test Case Automation Project

## 项目简介

本项目旨在自动化生成和处理测试用例文档。通过解析用户输入的测试用例文本，并将其填充到指定的 Word 文档模板中。



## 文件说明

- `Test_Script_Utils/` 目录：包含辅助功能模块
  - `input_utils.py`：处理用户输入和验证的功能
  - `doc_utils.py`：处理Word文档表格相关的功能
- `Testcase_Template.docx`：Word文档模板
- `main.py`：项目主文件，包含主要的逻辑流程
- `README.md`：项目说明文件



## 安装依赖

运行项目之前，请确保已安装所需的Python库。你可以使用以下命令安装依赖：

```bash
pip install python-docx
```

## 使用说明

### 运行主程序

> 在项目根目录下运行 main.py 文件：

### 输入测试用例

按照以下格式输入测试用例：

```text
id_value: 1
Module_Name_value: Div module;
Author_value: Edom;
Date_value: 2024.05.21;
Test_Title_value: User enter invalid number and we get an error;
Description_value: User enters invalid numbers for division and expects an error;
pre-conditions_value: User is attempting to divide two invalid numbers;
Test Step1: User enters one invalid number for division;
Test Data1: Abc
Expected Result1: Get error tips;
Actual Result1: We get error tips;
Test Step2: User enters two invalid numbers for division;
Test Data2: xyz
Expected Result2: Get error tips;
Actual Result2: We get error tips;
Test Step3: User enters "/" operator for division;
Test Data3: /
Expected Result3: Get warn tip;
Actual Result3: We get warn tip;
Test Step4: User presses the "=" operator to perform division;
Test Data4: =
Expected Result4: Get warn tip;
Actual Result4: We get warn tip;
Post-conditions_value: If the numbers are invalid, we can't divide them, and our test case is pass.
```

### 输出结果

程序将自动处理输入的测试用例，并将结果填充到 Testcase_Template.docx 模板中，生成的文档将保存在 TestCase 目录下。



## 模块说明

### utils/input_utils.py

包含处理用户输入和验证的功能：

- `get_input_text()`: 读取用户的多行输入
- `extract_value(pattern, text)`: 使用正则表达式提取值
- `validate_input(input_text)`: 验证用户输入的规范性
- `extract_and_map_text(input_text)`: 提取并映射文本

### utils/doc_utils.py

包含处理Word文档表格相关的功能：

- `replace_table_value(doc, old_value, new_value)`: 替换Word文档表格中的文本
- `clear_rows_with_text(table, text_to_clear)`: 清除包含特定文本的行
- `remove_extra_steps(doc, num_steps)`: 根据用户输入的测试步骤数，删除多余的行
- `center_align_table_text(doc)`: 将所有表格中的文本居中对齐
- `format_table_text(table)`: 格式化表格中的文本
- `format_table_content(table)`: 格式化表格内容

### main.py

项目主文件，包含主要的逻辑流程：

- 获取用户输入文本
- 验证用户输入
- 打开Word文档
- 提取并映射文本
- 替换文档中的文本
- 根据输入步骤数删除多余行
- 表格文本居中对齐
- 格式化表格文本和内容
- 保存修改后的文档



## 注意事项

确保 Testcase_Template.docx 模板文件存在且未被其他程序占用。

确保输入的测试用例文本格式正确。