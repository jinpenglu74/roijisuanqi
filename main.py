import tkinter as tk
from tkinter import ttk


def calculate():
    try:
        price=float(price_var.get() or 0)
        cost=float(cost_var.get() or 0)
        shipping=float(ship_var.get() or 0)
        ad=float(ad_var.get() or 0)
        platform=float(platform_var.get() or 0)/100
        refund=float(refund_var.get() or 0)/100

        income=price*(1-platform)*(1-refund)
        profit=income-cost-shipping-ad
        roi=price/ad if ad else 0

        roi_result.config(text=f"ROI {roi:.2f}")
        profit_result.config(text=f"利润 ¥{profit:.2f}")
        state_result.config(text="盈利" if profit>=0 else "亏损")
    except:
        state_result.config(text="请输入数字")

root=tk.Tk()
root.title("ROI智能计算器 V1.0")
root.geometry("700x450")

price_var=tk.StringVar()
cost_var=tk.StringVar()
ship_var=tk.StringVar()
ad_var=tk.StringVar()
platform_var=tk.StringVar()
refund_var=tk.StringVar()

for title,var in [("商品售价",price_var),("商品成本",cost_var),("运费",ship_var),("广告花费",ad_var),("平台扣点%",platform_var),("退款率%",refund_var)]:
    ttk.Label(root,text=title).pack()
    ttk.Entry(root,textvariable=var).pack()

ttk.Button(root,text="计算ROI",command=calculate).pack(pady=15)

roi_result=ttk.Label(root,text="ROI")
roi_result.pack()
profit_result=ttk.Label(root,text="利润")
profit_result.pack()
state_result=ttk.Label(root,text="等待输入")
state_result.pack()

root.mainloop()
