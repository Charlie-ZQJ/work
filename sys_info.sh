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
