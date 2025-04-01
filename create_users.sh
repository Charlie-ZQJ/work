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

