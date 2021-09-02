
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


# categorical
names = ['cats', 'dogs', 'dragons']
values = [5, 25, 125]
plt.figure(figsize=(15, 7))
plt.subplot(131)
plt.bar(names, values, color="red", label="bar chart")
plt.legend()
plt.subplot(132)
plt.scatter(names, values, color="orange", label="scatter plot")
plt.legend()
plt.subplot(133)
plt.plot(names, values, color="green", label="line plot")
plt.legend()
plt.suptitle('Categorical Plots')
plt.show()

# facets
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.2)

plt.figure()

plt.subplot(2,2,1)
plt.plot(t1, f(t1), 'black')

plt.subplot(2,2,2)
plt.plot(t2, np.tan(2*np.pi*t2), 'r--')

plt.subplot(2,2,3)
plt.plot(t2, np.exp(t2), 'g^')

plt.subplot(2,2,4)
plt.plot(t2, np.cos(2*np.pi*t2), 'orange')

# add text layer
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local maximum here', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
