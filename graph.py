import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys
import socket
import asyncio
import time


class plotWindow:
    def __init__(self):
        # # UIを設定
        # self.win = pg.GraphicsWindow()
        # self.win.setWindowTitle('Random plot')
        # self.plt = self.win.addPlot()
        # self.plt.setYRange(0, 1)
        # self.curve = self.plt.plot(pen=(0, 0, 255))

        # self.data = np.zeros(100)

        # # データを更新する関数を呼び出す時間を設定
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.update)
        # self.timer.start(100)
        print('Init')
    
    async def showGraph(self):
        print('showGraph==start')
        # UIを設定
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('Random plot')
        self.plt = self.win.addPlot()
        self.plt.setYRange(0, 1)
        self.curve = self.plt.plot(pen=(0, 0, 255))

        self.data = np.zeros(100)

        # データを更新する関数を呼び出す時間を設定
        async with True:
            print('showGraph==ing')
            time.sleep(1)
            self.update()
            # self.timer = QtCore.QTimer()
            # self.timer.timeout.connect(self.update)
            # self.timer.start(100)
        
        print('showGraph==fin')

        if (sys.flags.interactive!=1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def update(self):
        self.data = np.delete(self.data, 0)
        self.data = np.append(self.data, np.random.rand())
        self.curve.setData(self.data)

    async def udpServer(self):
        print('udpServer==start')
        async with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('192.168.10.200', 6666))
            while True:
                data, addr = s.recvfrom(1024)
                data = str(data).replace("b'acc,", "").replace("'", "")
                if "feat-acc," in data:
                    continue

                data = str(data).split(',')
                data = [float(i) for i in data]
                plotwin.update(data)
                print("data: {}, addr: {}".format(data, addr))
        print('udpServer==fin')


if __name__=="__main__":
    plotwin=plotWindow()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(plotwin.showGraph())

    plotwin.showGraph()
    plotwin.udpServer()


