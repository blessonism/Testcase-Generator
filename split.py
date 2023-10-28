"""
@filename:split.py
@author:JunLeon
@time:2023-10-23
"""

def extract_and_map_text(input_text):
    text_map = {}
    lines = input_text.strip().split('\n')

    for line in lines:
        key, value = line.split(': ', 1)
        text_map[key] = value

    return text_map


# # 示例用法
# input_text = """
# Module_Name_value: Add module
# Test_Title_value: User enter valid numbers and perform addition
# Description_value: User enters valid numbers and performs addition operation.
# pre-conditions_value: 1. Calculator is open and ready for input.
# Test Step1: User enters the first valid number.
# Test Data1: 5
# Expected Result1: The first number is entered.
# Test Step2: User enters the "+" operator.
# Test Data2: +
# Expected Result2: The addition operator is entered.
# Test Step3: User enters the second valid number.
# Test Data3: 7
# Expected Result3: The second number is entered.
# Test Step4: User presses the "=" operator to perform the addition.
# Test Data4: =
# Expected Result4: The addition operation is executed, and the result is displayed.
# Actual Result1: The first number is entered.
# Actual Result2: The addition operator is entered.
# Actual Result3: The second number is entered.
# Actual Result4: The addition operation is executed, and the result is displayed.
# """
#
# result = extract_and_map_text(input_text)
#
# for key, value in result.items():
#     print(f"map[{key}] = \"{value}\"")

