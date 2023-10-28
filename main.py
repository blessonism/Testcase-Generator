"""
@filename:main.py
@author:JunLeon
@time:2023-10-23
"""

multiline_text = ""
try:
    while True:
        line = input()
        if not line:
            break
        multiline_text += line + "\n"
except EOFError:
    pass

print("You entered the following text:")
print(multiline_text)
