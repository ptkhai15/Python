class Phone()
	Brand = "Apple"
	Model = "iphone X"
	Colour = "Black"
	Camera_Mp = "12 MP"
	Hdd = "128 GB"
	Ram = "3 GB"
	Platform = "iOS 12.3"

myPhone = Phone()

type(MyPhone)

MyPhone.Model

dir(MyPhone)

class Phone()
	def __init__(self):
		print("the function was called.")

Phone_1 = Phone() //the function was called

class Phone()
	def __init__(self,Brand,Model,Colour,Camera_MP,HDD,Ram,Platform):
		self.Brand = Brand
		self.Model = Model
		self.Colour = Colour
		self.Camera_MP = Camera_MP
		self.HDD = HDD
		self.Ram = Ram
		self.Platform = Platform

	def Show_Info():
		print("Phone Information",
			"\nBrand: ",self.Brand,
			"\nModel: ",self.Model,
			"\nColour: ",self.Colour,
			"\nCamera_MP: ",self.Camera_MP,
			"\nHDD: ",self.HDD,
			"\nRam: ",self.Ram,
			"\nPlatform: ",self.Platform)

MyPhone = Phone("Huawei","Mate 20 Pro","Black","40 MP","128 GB","6 GB","Android 9.0")
Myphone.Show_Info()

class Table(Phone):

Table_1 = Table("Huawei","Mate 20 Pro","Black","40 MP","128 GB","6 GB","Android 9.0")
Table_1.Show_Info()

class Table(Phone):
	def Change_Ram(self,new_ram):
		print("Changing ram...")
		self.Ram = new_ram

Table_1.Change_Ram("8 GB")

class Laptop()
        def __init__(self,Brand,Model,Colour,Camera_MP,HDD,Ram,Platform):
		print("Creating car object")
                self.Brand = Brand
                self.Model = Model
                self.Colour = Colour
                self.HDD = HDD
                self.Ram = Ram
                self.Platform = Platform
	def __str__(self):
		return "Brand: {}\nModel: {}\nColour: {}\nCamera_MP: {}\nHDD: {}\nRam: {}\nPlatform: {}".format(self.Brand,self.Model,self.Colour,self.HDD,self.Ram,self.Platform)
	def __del__(self):
		print("Deleting car object...")

Laptop_1 = Laptop("Huawei","Mate 20 Pro","Black","40 MP","128 GB","6 GB","Android 9.0")
print(Laptop_1)
del Laptop_1
