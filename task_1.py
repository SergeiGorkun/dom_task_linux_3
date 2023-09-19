
import subprocess
import pytest
import time

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

@pytest.fixture(autouse=True)
def record_statistics():

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("/путь/к/файлу/stat.txt", "a") as f:
        f.write(f"{current_time}, количество файлов, размер файла, статистика загрузки процессора\n")


def test_step1():
    # Тест1
    assert checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"

def test_step2():
    # Тест2
    assert checkout("cd /home/zerg/out; 7z e arx2.7z -o/home/zerg/folder1 -y", "Everything is Ok"), "test2 FAIL"

def test_step3():
    # Тест3
    assert checkout("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"

def test_list_files():
    # Тест на список файлов в архиве
    assert checkout("cd /home/zerg/out; 7z l arx2.7z", "Everything is Ok"), "List files test FAIL"

def test_extract_with_paths():
    # Тест на извлечение с сохранением путей
    assert checkout("cd /home/zerg/out; 7z x arx2.7z -o/home/zerg/folder2", "Everything is Ok"), "Extract with paths test FAIL"

if __name__ == "__main__":
    pytest.main()