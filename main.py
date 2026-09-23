import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

class ROIWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ROI智能计算器 V1.2.0')
        self.resize(1100, 700)
        self.setStyleSheet('''
        QWidget{background:#06152f;color:#e8f5ff;font-family:Microsoft YaHei;font-size:14px;}
        QFrame{background:#0b2145;border:1px solid #168cff;border-radius:16px;}
        QLineEdit{background:#071a35;border:1px solid #18a8ff;border-radius:8px;padding:8px;color:white;}
        QPushButton{background:#087cff;border-radius:10px;padding:10px;color:white;font-weight:bold;}
        QPushButton:hover{background:#12b8ff;}
        QLabel#title{font-size:28px;color:#2fd7ff;font-weight:bold;}
        QLabel#roi{font-size:48px;color:#00eaff;font-weight:bold;}
        ''')
        self.price=QLineEdit(); self.cost=QLineEdit(); self.ship=QLineEdit(); self.ad=QLineEdit(); self.platform=QLineEdit(); self.refund=QLineEdit()
        self.result=QLabel('ROI 计算结果')
        self.result.setObjectName('roi')
        left=QFrame(); ll=QVBoxLayout(left)
        ll.addWidget(QLabel('经营参数'))
        for n,w in [('商品售价',self.price),('商品成本',self.cost),('商品运费',self.ship),('广告花费',self.ad),('平台扣点%',self.platform),('退款率%',self.refund)]:
            ll.addWidget(QLabel(n)); ll.addWidget(w)
        btn=QPushButton('开始测算'); btn.clicked.connect(self.calc); ll.addWidget(btn)
        right=QFrame(); rl=QVBoxLayout(right)
        rl.addWidget(QLabel('测算结果'))
        rl.addWidget(self.result)
        self.info=QLabel('每单广告费 / 平台扣点 / 毛利率')
        rl.addWidget(self.info)
        layout=QVBoxLayout(self)
        title=QLabel('ROI智能计算器'); title.setObjectName('title')
        layout.addWidget(title)
        row=QHBoxLayout(); row.addWidget(left); row.addWidget(right); layout.addLayout(row)
    def calc(self):
        try:
            price=float(self.price.text() or 0); ad=float(self.ad.text() or 0)
            roi=price/ad if ad else 0
            self.result.setText(f'{roi:.2f}')
            self.info.setText('达到该ROI可覆盖广告投入并评估盈利空间')
        except:
            self.result.setText('请输入数字')

app=QApplication(sys.argv)
w=ROIWindow(); w.show()
sys.exit(app.exec())
