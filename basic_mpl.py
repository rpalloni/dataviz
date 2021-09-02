
import matplotlib.pyplot as plt
import numpy as npfig,axs = plt.subplots(figsize=(15,7)) 

data1 = np.random.normal(0,1,100)
data2 = np.random.normal(0,1,100)
data3 = np.random.normal(0,1,100)
x_ax = np.arange(0,100,10)
y_ax = np.arange(-3,3,1)
axs.plot(data1,marker="o")
axs.plot(data2,marker="*")
axs.plot(data3,marker="^")
axs.set_xticks(x_ax)
axs.set_xticklabels(labels=x_ax,rotation=45)
axs.set_yticks(y_ax)
axs.set_yticklabels(labels=y_ax,rotation=45)
axs.set_xlabel("X label")
axs.set_ylabel("Y label")
axs.set_title("Title")
axs.grid("on")


t = np.sin(np.linspace(-3,3,50))
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', color="red")
plt.plot(t, t**2, 'bs', color="blue")
plt.plot(t, t**3, 'g^', color="green")
plt.plot(t, t**4, "o", color="orange")
plt.plot(t, t**5, "o-", color="black")
plt.show()


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
