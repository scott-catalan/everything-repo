'''
# Project Creation Date: 4:50:54 PM, 2/19/2026
'''
import random as r

class PC:
    def __init__(self, gpu, cpu, ram):
        self.gpu = gpu
        self.cpu = cpu
        self.ram = ram

gpus = [
    "NVIDIA GeForce RTX 4090",
    "NVIDIA GeForce RTX 4080",
    "NVIDIA GeForce RTX 4070 Ti",
    "NVIDIA GeForce RTX 4070",
    "NVIDIA GeForce RTX 4060 Ti",
    "AMD Radeon RX 7900 XTX",
    "AMD Radeon RX 7900 XT",
    "AMD Radeon RX 7800 XT",
    "AMD Radeon RX 7700 XT",
    "NVIDIA GeForce GTX 1660 Super",
    "NVIDIA GeForce RTX 3060 Ti",
    "NVIDIA GeForce RTX 3070",
    "NVIDIA GeForce RTX 3080",
    "AMD Radeon RX 6800 XT",
    "AMD Radeon RX 6700 XT"
]
cpus = [
    "Intel Core i9-14900K",
    "Intel Core i7-14700K",
    "Intel Core i5-14600K",
    "Intel Core i5-13600K",
    "Intel Core i3-13100",
    "AMD Ryzen 9 7950X",
    "AMD Ryzen 9 7900X",
    "AMD Ryzen 7 7800X3D",
    "AMD Ryzen 7 7700X",
    "AMD Ryzen 5 7600",
    "AMD Ryzen 5 5600X",
    "Intel Core i7-13700F",
    "Intel Core i5-12400F"
]
ram_amounts = [
    "8GB DDR4",
    "16GB DDR4",
    "32GB DDR4",
    "64GB DDR4",
    "8GB DDR5",
    "16GB DDR5",
    "32GB DDR5",
    "64GB DDR5"
]

gpu_prices = {
    "NVIDIA GeForce RTX 4090": 1699,
    "NVIDIA GeForce RTX 4080": 1199,
    "NVIDIA GeForce RTX 4070 Ti": 799,
    "NVIDIA GeForce RTX 4070": 599,
    "NVIDIA GeForce RTX 4060 Ti": 399,
    "AMD Radeon RX 7900 XTX": 999,
    "AMD Radeon RX 7900 XT": 899,
    "AMD Radeon RX 7800 XT": 499,
    "AMD Radeon RX 7700 XT": 399,
    "NVIDIA GeForce GTX 1660 Super": 229,
    "NVIDIA GeForce RTX 3060 Ti": 399,
    "NVIDIA GeForce RTX 3070": 499,
    "NVIDIA GeForce RTX 3080": 699,
    "AMD Radeon RX 6800 XT": 649,
    "AMD Radeon RX 6700 XT": 479
}
cpu_prices = {
    "Intel Core i9-14900K": 589,
    "Intel Core i7-14700K": 399,
    "Intel Core i5-14600K": 289,
    "Intel Core i5-13600K": 279,
    "Intel Core i3-13100": 129,
    "AMD Ryzen 9 7950X": 599,
    "AMD Ryzen 9 7900X": 449,
    "AMD Ryzen 7 7800X3D": 399,
    "AMD Ryzen 7 7700X": 329,
    "AMD Ryzen 5 7600": 229,
    "AMD Ryzen 5 5600X": 199,
    "Intel Core i7-13700F": 319,
    "Intel Core i5-12400F": 179
}
ram_prices = {
    "8GB DDR4": 30,
    "16GB DDR4": 60,
    "32GB DDR4": 110,
    "64GB DDR4": 200,
    "8GB DDR5": 45,
    "16GB DDR5": 80,
    "32GB DDR5": 150,
    "64GB DDR5": 280
}

while True:
    pcs = []
    amount = input("How many PCs do you want to search for?\n>")
    if not amount.isdecimal():
        continue

    for i in range(int(amount)):
        pcs.append(PC(r.choice(gpus), r.choice(cpus), r.choice(ram_amounts)))

    print(pcs)