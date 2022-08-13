####################################
# 作成者：渡邉 優太 
# 作成日：2022/08/13               
####################################

PROCESS_COUNT=`ps aux | grep fileUpload | grep -v grep | wc -l`

#起動済みの場合は処理を中断する
if [ $PROCESS_COUNT -gt 0  ]; then
  echo "起動済みです"
  exit 1
fi

python modules/fileUpload.py &

