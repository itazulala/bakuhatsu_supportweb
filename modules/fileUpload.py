from watchdog.observers.polling import PollingObserver
from watchdog.events import PatternMatchingEventHandler
from subprocess import run
from pathlib import Path
from re import compile
import time

# 監視対象ディレクトリを指定する
target_dir = './uploads'
# 監視対象ファイルのパターンマッチを指定する
target_file = '*.md'
# FAQファイルパターン
pattern = '^FAQ-.+\.md'


class FileChangeHandler(PatternMatchingEventHandler):

    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)

    def on_created(self, event):
        filename = Path(event.src_path).name
        filepath = str(Path(event.src_path))
        if compile(pattern).match(filename):
            command_file = 'importFaqMarkdown'
        else:
            command_file = 'importContentsMarkdown'
        run(["python", "manage.py", command_file, "-a", "created", "-f" + filepath])

    def on_modified(self, event):
        filename = Path(event.src_path).name
        filepath = str(Path(event.src_path))
        print('%s modified' % filepath)
        if compile(pattern).match(filename):
            command_file = 'importFaqMarkdown'
        else:
            command_file = 'importContentsMarkdown'
        run(["python", "manage.py", command_file, "-a", "modified", "-f" + filepath])

    def on_deleted(self, event):
        filename = Path(event.src_path).name
        filepath = str(Path(event.src_path))
        print('%s deleted' % filepath)
        if compile(pattern).match(filename):
            command_file = 'importFaqMarkdown'
        else:
            command_file = 'importContentsMarkdown'
        run(["python", "manage.py", command_file, "-a", "deleted", "-f" + filepath])


# コマンド実行の確認
if __name__ == "__main__":
    # ファイル監視の開始
    observer = PollingObserver()
    observer.schedule(FileChangeHandler([target_file]), target_dir, recursive=True)
    observer.start()

    # 処理が終了しないようスリープを挟んで無限ループ
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
