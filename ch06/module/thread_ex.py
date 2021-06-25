import threading


def fuction_a():
    print("5초 마다 실행")
    timer = threading.Timer(5,fuction_a)
    timer.start()

fuction_a()