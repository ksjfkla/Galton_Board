from random import choice
import datetime
import matplotlib.pyplot as plt
import numpy as np

starttime = datetime.datetime.now()


#核心
def chuandao(haoma123):
    global haoma
    global jiedian
    global boo
    global floor
    global haomaoriginal
    global jishuqi
    global jianyancishu
    
    haoma = haoma123 
    jianyancishu += 1        
    if jiedian[haoma] == "左":
        floor += 1
        jiedian[haoma + floor] = choice(boo)
        jishuqi += 1
        print(f"第{floor}层的节点{haoma}的状态是：左")
        print("-" * 20)
        haomaoriginal = haoma
        
        #chuandao(haoma + floor)
        haoma += floor
    
    elif jiedian[haoma] == "右":
        floor += 1
        jiedian[haoma + floor + 1] = choice(boo)
        jishuqi += 1
        print(f"第{floor}层的节点{haoma}的状态是：右")
        print("-" * 20)
        haomaoriginal = haoma
        #chuandao(haoma + floor + 1)
        haoma += (floor + 1)
    else:
        print("false"*10)
      

# 画图
def zhexiantu(z):
    global xzhou
    global yzhou
    plt.figure(figsize=(7,7),dpi=100)
    plt.plot(xzhou, yzhou, linewidth = 1)
    plt.title(f"Normal Distribution", fontsize=24) 
    plt.xlabel(f"last floor", fontsize=14)
    plt.ylabel(f"{ballsamount} balls", fontsize=14) 
    #plt.ylim((min(dict1[l]), max(dict1[l])))
    
    my_x_ticks = np.arange(min(xzhou), max(xzhou)+1, 1)
    my_y_ticks = np.arange(min(yzhou), max(yzhou)+1, 10)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    
    
    plt.tick_params(axis='both', labelsize=10)
    plt.savefig(f"F:\\pythonxiong\\normal_b\\sdyxpng\\normals_{z}.png")




#前置属性
boo = ["左", "右"]


#按钮
ballsamount = 100000
floorsamount = 100
rounds = 1

# 生成一个mclist
mcn = 0   
for m in list(range(1, floorsamount)):
    mcn += m
mclist = list(range(mcn, mcn + floorsamount))
# 检验mclist
print(mclist)

# 生成一个result字典，key为mclist，value为存放左右的list
result = {}
for mc in mclist:
    result[mc] = []


# 计数器的设置
jishuqi = 0
jianyancishu = 0
     
for ball in list(range(ballsamount)):        
    
    jiedian = {}
    jiedian[0] = choice(boo)
    jishuqi += 1
    floor = 0 
    haoma = 0
    while floor < floorsamount:
        chuandao(haoma)
        
        print("*" * 10)
        
        
    #if jiedian[haoma] == "左":
    #    haoma -= floor
        #floor -= 1
    #elif jiedian[haoma] == "右":
    #    haoma -= (floor + 1)
        #floor -= 1
    
    #print(floor, haomaoriginal)
    print(f"结束时，第{floor}层的节点{haomaoriginal}的状态是：{jiedian[haomaoriginal]}")
    result[haomaoriginal].append(jiedian[haomaoriginal])
    
    
  
xzhou = mclist
yzhou = [] 
    
   
for r in mclist:
    print(f"末层号码{r}装有：{result[r]}")
    yzhou.append(len(result[r]))


for last in list(range(rounds)):
    zhexiantu(last + 1)

print("%"*30)
print(xzhou)
print(yzhou)
print("%"*30)


endtime = datetime.datetime.now()
print(f"程序的运行时间为：{endtime-starttime}") 
#print(f"总运算次数为：{jishuqi}")
print(f"总共需要检验节点信号{jianyancishu}次")