import random

# part1
def random_generate():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    z = ['+', '-', '*', '/']
    z = random.choice(z)
    if z == '/':
        while y == 0:
            y = random.randint(0, 10)
    question = f"{x} {z} {y}"
    if z == '+':
        answer = x + y
    elif z == '-':
        answer = x - y
    elif z == '*':
        answer = x * y
    elif z == '/':
        answer = round(x / y, 2)
    return question, answer

# part3,4
def main():
    aTrue = 0
    aTotal = 0
    while True:
        question, answer = random_generate()  # 调用函数生成问题和答案
        print(f"问题：{question} = ?")
        while True:
            user_input = input("请输入你的答案（出发保留两位）：")
            try:
                user_answer = float(user_input)
                aTotal += 1
                if user_answer==answer:
                    print("回答正确！")
                    aTrue += 1
                else:
                    print(f"回答错误.")
                break
            except ValueError:
                flag = input('输入错误，是否继续(y/n)：').lower()
                if flag != 'y':
                    print(f"正确率：{aTrue / aTotal:.2f}")

# 运行主程序
    main()
