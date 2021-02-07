from PyQt5.QtCore import QObject, QRunnable, pyqtSlot, QThreadPool, pyqtSignal
from pynput import keyboard
from threading import Timer


class WorkerSignals(QObject):
    main = pyqtSignal()
    add = pyqtSignal()
    options = pyqtSignal()
    escape = pyqtSignal()

class Worker(QRunnable):
    cmd_count = 0
    ctrl_count = 0
    timeout = .25

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def reset_cmd(self):
        self.cmd_count = 0

    def reset_ctrl(self):
        self.ctrl_count = 0

    def show_add(self):
        print("Hotkey add")
        self.cmd_count += 1

        if self.cmd_count > 1:
            self.signals.add.emit()
            self.reset_cmd()

        timer = Timer(self.timeout, self.reset_cmd)
        timer.start()

    def show_main(self):
        print("Hotkey main")
        self.ctrl_count += 1
        if self.ctrl_count > 1:
            self.signals.main.emit()
            self.reset_ctrl()

        timer = Timer(self.timeout, self.reset_ctrl)
        timer.start()

    def show_options(self):
        print("Hotkey options")
        self.signals.options.emit()

    def escape(self):
        print("Escape")
        self.signals.escape.emit()

    def for_canonical(self, f):
        return lambda k: f(self.l.canonical(k))

    @pyqtSlot()
    def run(self):
        print("Worker running")

        with keyboard.GlobalHotKeys({
            '<shift>': self.show_add,
            '<ctrl>': self.show_main,
            '<cmd>+<shift>+g': self.show_options,
            '<esc>': self.escape
        }) as h:
            h.join()


class KeyboardListener(QObject):
    main = pyqtSignal()
    add = pyqtSignal()
    options = pyqtSignal()
    escape = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.listen()

    def listen(self):
        worker = Worker()
        worker.signals.add.connect(self.add.emit)
        worker.signals.main.connect(self.main.emit)
        worker.signals.options.connect(self.options.emit)
        worker.signals.escape.connect(self.escape.emit)

        self.threadpool.start(worker)