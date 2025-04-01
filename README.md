# 钟泉江 324080203115 24机械1班 github：https://github.com/Charlie-ZQJ/work
## 1、work.py：3个计算功能的代码
```python
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
```


## 2、系统信息收集
```bash
#!/bin/bash
{
    echo "当前用户: $(whoami)"
    echo -e "\n系统时间:" 
    date
    echo -e "\nCPU负载:" 
    uptime
    echo -e "\n磁盘使用:" 
    df -h
    echo -e "\n内存使用:" 
    free -m
} > system_report.txt
```

### 功能描述
编写了一个名为sys_info.sh的Bash脚本，用于收集并保存系统信息。脚本执行后会显示并保存以下信息到system_report.txt文件中。
### 使用方法
1、保存脚本sys_info.sh文件

2、赋予执行权限，在终端中运行以下命令为脚本文件添加执行权限：
```bash
chmod +x sys_info.sh
```

3、执行脚本：
```bash
./sys_info.sh
```
执行完成后，脚本会在当前目录下生成一个system_report.txt文件，其中包含了当前用户、时间、CPU 负载、磁盘使用情况、内存使用情况等信息。

4、查看输出：
```bash
cat system_report.txt
```


## 3、批量创建用户
```bash
#!/bin/bash
while IFS= read -r username
do
    if id "$username" &>/dev/null; then
        echo "用户 $username 已存在，跳过创建。"
    else
        useradd "$username"
        if [ $? -eq 0 ]; then
            echo "用户 $username 创建成功！"
        else
            echo "创建用户 $username 失败！"
        fi
    fi
done < user_list.txt
```

### 功能描述
该脚本用于批量创建用户。
它会从user_list.txt文件中逐行读取用户名，并检查用户是否存在：
如果用户已存在，则跳过该用户，并输出提示信息。
如果用户不存在，则使用useradd命令创建该用户，并输出创建成功或失败的提示。
### 使用方法
1、保存脚本create_users.sh文件

2、创建一个名为 user_list.txt`的文件，按行列出需要创建的用户名

3、为脚本添加执行权限：
```bash
chmod +x create_users.sh
```

4、执行脚本:
```bash
./create_users.sh
```

