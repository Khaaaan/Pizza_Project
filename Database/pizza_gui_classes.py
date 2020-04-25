import tkinter as tk
# import pizza
# import login_password
# import cart
# import admin
from Database import pizza
from Database import login_password
from Database import cart
from Database import admin


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Pizza Order")
        self.geometry("680x680")
        self.configure(bg='red')
        # self.configure(bg ='red')
        self.frame = None
        self.switch_frame(Login)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:  # if it is not StartPage
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()


array = [0]
count = 0


def counter():
    global array
    global count
    count += 1
    array.append(0)


def anti_counter():
    global array
    global count
    # array.pop(count)
    if count > 0:
        del array[count]
        count -= 1
# def update_info():
#     window.frame.inform.delete(0.0, END)
#     window.frame.inform.insert(tk.END, myPizza.get_status())

# class Builder:
#     def __init__(self, pizzatype):
#         self.myPizza = pizza.PizzaBuilder(pizzatype)

#     def add(extension):
#         self.myPizza.add_extension(extension)

#     def remove(extension):
#         self.myPizza.remove_extension(extension)


def login(frame, username, password):
    if username == 'admin' and password == 'admin':
        frame.root.switch_frame(Admin)
        return
    global user
    user = username
    respond = login_password.login(username, password)
    if respond:
        frame.root.switch_frame(StartPage)
    else:
        frame.fail = tk.Label(
            frame, text='Username or password is incorrect')
        frame.fail.grid(row=8)
        # frame.fail.after(1000, lambda: frame.fail.destroyb())


class Login(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.configure(bg='red')
        tk.Label(self, text="Login Page", bg='red', fg='white',
                 font="Times 15 bold").grid(row=1)
        # Username
        tk.Label(self, text="Username", fg="white", bg='red').grid(row=2)
        self.username = tk.Entry(self)
        self.username.grid(row=3)
        # Password
        tk.Label(self, text="Password", fg='white', bg='red').grid(row=4)
        self.password = tk.Entry(self)
        self.password.grid(row=5)
        # login
        tk.Button(self, text="LOGIN", width=30,
                  command=lambda: login(self, self.username.get(), self.password.get())).grid(row=6)
        tk.Button(self, text="REGISTER", width=30,
                  command=lambda: root.switch_frame(Register)).grid(row=7)
        tk.Label(self, text='')


def register(frame, username, password):
    answer = login_password.register(username, password)
    frame.text = tk.Label(frame, text=answer, width=30, bg='red', fg='white')
    frame.text.grid(row=7)
    # frame.text.after(1000, lambda: frame.text.destroy())


class Register(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.configure(bg='red')
        tk.Label(self, text="Register Page", bg='red', fg='white',
                 font="Times 15 bold").grid(row=0)
        # Username
        tk.Label(self, text="Username", fg="white", bg='red').grid(row=1)
        self.username = tk.Entry(self)
        self.username.grid(row=2)
        # Password
        tk.Label(self, text="Password", fg='white', bg='red').grid(row=3)
        self.password = tk.Entry(self)
        self.password.grid(row=4)
        # login
        tk.Button(self, text="REGISTER", width=30,
                  command=lambda: register(self, self.username.get(), self.password.get())).grid(row=5)
        tk.Button(self, text="Go Back", width=30,
                  command=lambda: root.switch_frame(Login)).grid(row=6)


def add_pizza(frame, name, status, price):
    if (name == '' or status == '' or price == ''):
        tk.Label(frame, text="Fill the blanks", width=30,
                 bg='red', fg='white').grid(row=7, column=1)
        return
    respond = admin.add(name, status, price)
    tk.Label(frame, text=respond, width=30, bg='red',
             fg='white').grid(row=7, column=1)


class Admin(tk.Frame):
    def __init__(self, root):
        self.root = root
        tk.Frame.__init__(self, root)
        self.configure(bg='red')
        self.name = tk.Entry(self)
        self.status = tk.Entry(self)
        self.price = tk.Entry(self)
        tk.Label(self, text='Pizza name', bg='red').grid(row=0, column=1)
        self.name.grid(row=1, column=1)
        # tk.Label(self, text='', bg='red').pack()
        tk.Label(self, text='Satus', bg='red').grid(row=2, column=1)
        self.status.grid(row=3, column=1)
        # tk.Label(self, text='', bg='red').pack()
        tk.Label(self, text='price', bg='red').grid(row=4, column=1)
        self.price.grid(row=5, column=1)

        tk.Button(self, text="Create new pizza",
                  command=lambda: add_pizza(self,
                                            self.name.get(), self.status.get(), self.price.get())).grid(row=6, column=1)

        # tk.Button(self, text="User Information",
        #           command=lambda: tk.Tk()).pack()

        # tk.Label(self, text='', bg='red').grid(row=8, column=1)
        tk.Label(self, text='User Information', bg='red').grid(row=9, column=1)
        self.username = tk.Entry(self)
        self.username.grid(row=10, column=1)
        tk.Button(self, text="GET INFO",
                  command=lambda: [self.check(self.username.get()), self.search(self.username.get())]).grid(row=11, column=1)
        # Log out
        tk.Button(self, text='LOG OUT',
                  command=lambda: root.switch_frame(Login)).grid(row=8, column=1)

    def search(self, username):
        if username:
            list = login_password.search(username)
            string = "Username: " + list[0] + "\n" + "Password: " + list[1]
            self.text_widget = tk.Text(self, width=20, height=2)
            self.text_widget.grid(row=12, column=1)
            self.text_widget.insert(tk.END, string)
            tk.Label(self, text='', bg="red").grid(row=13)

    def check(self, username):

        if username:
            string = ''
            my_list = cart.read_all(username)
            for purchase in my_list:
                string += purchase[0] + "\nPrice: " + \
                    str(purchase[1]) + '\nDate/time:' + purchase[2] + '\n\n\n'
                self.text1 = tk.Text(self, width=50, height=25)
                self.text1.grid(row=14, column=1)
                self.text1.insert(tk.END, string)


def create(pizzaType, row=None):
    # global myPizza
    global array
    array[count] = pizza.PizzaBuilder(pizzaType, row)
    # array.append(pizza.PizzaBuilder(pizzaType))


class StartPage(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(bg='red')
        tk.Label(self, text="StartPage", bg='red', fg='white',
                 font="Times 15 bold").pack()

        myfile = open("Database/notifications.txt", "r+")
        news = myfile.read()
        myfile.close()

        tk.Label(self, text=news, bg='red', fg='white',
                 font="Times 15 bold").pack()

        # self.logo1 = tk.PhotoImage(file="photo/margherita1.png")
        # self.logo2 = tk.PhotoImage(file="photo/pepperoni1.png")
        # tk.Label(self, image=logo1).pack(side='bottom')
        # tk.Label(self, image=self.logo1, bg="red").grid(row=1, column=0)
        tk.Button(self, text="Margherita", width=30,
                  command=lambda: [create("Margherita"),
                                   root.switch_frame(PageOne)]).pack()

        # tk.Label(self, image=self.logo2, bg='red').grid(row=1, column=2)
        tk.Button(self, text='Pepperoni', width=30,
                  command=lambda: [create("Pepperoni"),
                                   root.switch_frame(PageOne)]).pack()
        my_list = admin.get_all()

        if my_list is not None:
            for row in my_list:
                tk.Button(self, text=row[0], width=30,
                          command=lambda: [create('ConcretePizza', row),
                                           root.switch_frame(PageOne)]).pack()

        # History
        tk.Button(self, text='PURCHASE INFO',
                  command=lambda: root.switch_frame(Cart)).pack(side=tk.RIGHT)
        # Log out
        tk.Button(self, text='LOG OUT',
                  command=lambda: root.switch_frame(Login)).pack(side=tk.LEFT)

        # w = Frame(root)
        # Label(w,...).pack()


class Cart(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(bg='red')

        tk.Button(self, text="Go Back",
                  command=lambda: root.switch_frame(StartPage)).grid(row=0, column=0, sticky=tk.W)
        tk.Label(self, text="Product", fg='white',
                 bg="red").grid(row=1, column=0)
        tk.Label(self, text="Price", fg='white',
                 bg="red").grid(row=1, column=1)
        tk.Label(self, text="Purchase date/time",
                 fg='white', bg="red").grid(row=1, column=2)
        my_list = cart.read_all(user)
        n = 2
        for purchase in my_list:
            self.text1 = tk.Text(self, width=30, height=5)
            self.text1.grid(row=n, column=0)
            self.text1.insert(tk.END, purchase[0])
            self.text1 = tk.Text(self, width=5, height=5)
            self.text1.grid(row=n, column=1)
            self.text1.insert(tk.END, purchase[1])
            self.text1 = tk.Text(self, width=30, height=5)
            self.text1.grid(row=n, column=2)
            self.text1.insert(tk.END, purchase[2])

            tk.Label(self, text='', bg='red').grid(row=n + 1)
            n += 2


class PageOne(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        tk.Label(self, text='Page One', bg='red', fg='white',
                 font='Times 15 bold').grid(row=0, column=1)
        self.configure(bg='red')
        self.logo1 = tk.PhotoImage(file="photo/beef.png")
        self.logo2 = tk.PhotoImage(file="photo/cheese.png")
        self.logo3 = tk.PhotoImage(file="photo/tomato.png")
        tk.Label(self, image=self.logo1, bg="red").grid(row=1, column=0)
        tk.Label(self, image=self.logo2, bg="red").grid(row=1, column=1)
        tk.Label(self, image=self.logo3, bg="red").grid(row=1, column=2)

        tk.Label(self, text=' ', bg='red').grid(row=5)
        tk.Button(self, text="Go Back",
                  command=lambda: root.switch_frame(StartPage)).grid(row=7, column=0)
        tk.Button(self, text="Order",
                  command=lambda: root.switch_frame(PageTwo)).grid(row=7, column=2)
        # tk.Label(self, text="Add something:").

        # ADD
        tk.Button(self, text="ADD", width=7,
                  command=lambda: [array[count].add_extension("Beef"),
                                   self.update_info()]).grid(row=3, column=0)
        tk.Button(self, text='ADD', width=7,
                  command=lambda: [array[count].add_extension("Cheese"),
                                   self.update_info()]).grid(row=3, column=1)
        tk.Button(self, text='ADD', width=7,
                  command=lambda: [array[count].add_extension("Tomato"),
                                   self.update_info()]).grid(row=3, column=2)

        # tk.Label(self, text="Remove something:").pack()
        # REMOVE
        tk.Button(self, text="REMOVE", width=7,
                  command=lambda: [array[count].remove_extension("Beef"),
                                   self.update_info()]).grid(row=4, column=0)
        tk.Button(self, text='REMOVE', width=7,
                  command=lambda: [array[count].remove_extension("Cheese"),
                                   self.update_info()]).grid(row=4, column=1)
        tk.Button(self, text='REMOVE', width=7,
                  command=lambda: [array[count].remove_extension("Tomato"),
                                   self.update_info()]).grid(row=4, column=2)
        self.inform = tk.Text(self, width=30, height=5)
        self.inform.insert(tk.END, array[count].get_status())
        self.inform.grid(row=6, column=1)

    def update_info(self):
        self.inform.delete(0.0, tk.END)
        self.inform.insert(tk.END, array[count].get_status())


class PageTwo(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(bg="red")
        tk.Label(self, text='Page Two', bg='red',
                 fg="white", font="Times 15 bold").grid(row=0)

        # tk.Label(self, text='', bg='red').grid(row=5)

        tk.Button(self, text="Go Back",
                  command=lambda: root.switch_frame(PageOne)).grid(row=1, sticky=tk.W)
        price = 0.0
        for i in array:
            price += i.get_price()
        tk.Button(self, text="Confirm", command=lambda:
                  [cart.confirm(array, price, user),
                   root.switch_frame(StartPage)]).grid(row=1, sticky=tk.E)
        # ONE MORE PIZZA
        tk.Button(self, text="One More Pizza", width=30,
                  command=lambda: [counter(), root.switch_frame(StartPage)]).grid(row=2, sticky=tk.W)
        # REMOVE LAST PIZZA
        tk.Button(self, text="Remove last PIZZA", width=30,
                  command=lambda: [anti_counter(), self.update_info(), ]).grid(row=3, sticky=tk.W)

        tk.Label(self, text="Price:", bg='red', fg="white",
                 font="Times 12 italic bold").grid(row=4, sticky=tk.W)

        self.output = tk.Text(self, width=30, height=2)

        self.output.insert(tk.END, "$ " + str(price))
        self.output.grid(row=5)
        tk.Label(self, text="Status:", bg='red', fg="white",
                 font="Times 12 italic bold").grid(row=6, sticky=tk.W)
        self.status = tk.Text(self, width=30, height=20, wrap=tk.WORD)
        for i in array:

            # status.insert(tk.END, array[count].get_status())
            self.status.insert(tk.END, '\n\n\n' + i.get_status())
            self.status.grid(row=7)

    def update_info(self):
        self.output.delete(1.0, tk.END)
        self.status.delete(1.0, tk.END)

        price = 0
        for i in array:
            price += i.get_price()
        self.output.insert(tk.END, "$ " + str(price))
        self.output.grid(row=5)
        tk.Label(self, text="Status:", bg='red', fg="white",
                 font="Times 12 italic bold").grid(row=6, sticky=tk.W)
        flag = 7
        for i in array:
            self.status = tk.Text(self, width=30, height=4, wrap=tk.WORD)
            # status.insert(tk.END, array[count].get_status())
            self.status.insert(tk.END, i.get_status())
            self.status.grid(row=flag)
            flag += 1
