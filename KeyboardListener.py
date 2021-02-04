from PyQt5.QtCore import QObject, QRunnable, pyqtSlot, QThreadPool, pyqtSignal
from pynput import keyboard


class WorkerSignals(QObject):
    main = pyqtSignal()
    add = pyqtSignal()
    options = pyqtSignal()
    escape = pyqtSignal()

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def show_add(self):
        print("Hotkey add")
        self.signals.add.emit()

    def show_main(self):
        print("Hotkey main")
        self.signals.main.emit()

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
            '<cmd>+<shift>+<space>': self.show_add,
            '<ctrl>+<shift>+<space>': self.show_main,
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