####################################
# 作成者：渡邉 優太                
# 作成日：2022/08/13               
####################################

if [ $PROCESS_COUNT -gt 0  ]; then
  echo "停止済みです"
  exit 1
fi

pkill -KILL -f fileUpload.py

