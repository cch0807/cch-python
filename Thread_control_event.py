import threading
import time

def before_work():
    evt.set()
    print('* before work, done')

def after_work():
    print('** after work, waiting')
    evt.wait()
    print('** after work, done')

def check_state():
    print('*** check state', evt.is_set())
    evt.wait()
    print('*** check state,', evt.is_set())

if __name__ == '__main__':
    evt = threading.Event()
    after_thr = threading.Thread(target=after_work)
    before_thr = threading.Thread(target=before_work)
    state_thr = threading.Thread(target=check_state)
    after_thr.start()
    time.sleep(1)
    state_thr.start()
    before_thr.start()
