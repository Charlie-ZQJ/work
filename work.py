def factorial(n):
#计算非负整数的阶乘
    if n < 0:
        print("错误：阶乘只定义在非负整数,请输入非负整数")
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
#判断一个数是否为素数
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
#生成斐波那契数列
    if n <= 0:
        return []
    fib = [0, 1][:n]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]


def main_menu():
#用户交互菜单系统
    while True:
        print("\n======== 功能菜单 ========")
        print("1. 计算阶乘")
        print("2. 判断素数")
        print("3. 生成斐波那契数列")
        print("4. 退出程序")

        choice = input("请输入选项(1-4): ")

        if choice == '4':
            print("感谢使用，程序已退出！")
            break

        try:
            if choice == '1':
                num = int(input("请输入非负整数："))
                print(f"{num}! = {factorial(num)}")

            elif choice == '2':
                num = int(input("请输入正整数："))
                print(f"{num}是素数" if is_prime(num) else f"{num}不是素数")

            elif choice == '3':
                length = int(input("请输入数列长度："))
                print(f"斐波那契数列：{fibonacci(length)}")

            else:
                print("无效选项，请重新输入")
        except ValueError:  # 处理非数字输入[15](@ref)
            print("输入错误：请输入有效整数")


if __name__ == "__main__":
    main_menu()