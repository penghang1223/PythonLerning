class Clock:
    id = None
    price = None
    def ring(self):
            import winsound
            winsound.Beep(2000,3000)
clock1 = Clock()
# 定义一个对象

clock1.id = "iojioasj"
clock1.price = 111
print (clock1.id,clock1.price)
clock1.ring()
