# CISCO-router-telnet-Batch-opening-for-win-by-pyqt
To open multiple telnet links through port number increasing。可以批量打开思科路由模拟器的telnet链接，并且可以代替输入回车和no 方便批量打开多个思科路由模拟器
环境由eric6+python3.6+pyqt5+win32api+pyinstaller组成。
文件包含编译的工程文件，打包时产生的临时文件，打包后的可执行文件。其中核心代码文件为Ui_xshell.py和xshell.py。
Xshell文件名只不过是当时基于Xshell起的文件名，与主题无关。
执行原理：
将端口号自增，生成telnet链接，请求系统打开。所以只适用于连号端口的模拟器，且本机已经可以打开telnet：//的链接。


power by 天域至尊
CSDN：https://blog.csdn.net/qq_39091354
