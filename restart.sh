#!/bin/bash

root_dir='/root/ania-pro'
app_name='main.py'
log_dir='/root/ania-pro/log'
log_name='ania'

# 定义进度条函数
function progress_bar() {
    local duration=${1}

    already_done() { for ((done=0; done<$elapsed; done++)); do printf "▇▇▇▇▇▇▇▇▇▇▇▇▇▇"; done }
    remaining() { for ((remain=$elapsed; remain<$duration; remain++)); do printf " "; done }
    percentage() { printf "| %s%%" $(( (($elapsed)*100)/($duration)*100/100 )); }

    for (( elapsed=1; elapsed<=$duration; elapsed++)); do
        already_done; remaining; percentage
        printf "\r"
        sleep 1
    done
    printf "\n"
}

# 停止当前运行的进程
pid=`ps -ef|grep ${app_name}|grep -v grep|grep -v restart|grep -v tail|awk '{print $2}'`
if [ -n "${pid}" ] ;then
        kill -9 ${pid}
        echo "killed ${pid}"
fi

# 启动项目并显示进度条
nohup python main.py >> nohup.out 2>&1 &
progress_bar 3

echo "Ania 重启成功！"

# 显示日志文件的最后20行
sleep 1
tail -20f ${log_dir}/${log_name}.log
