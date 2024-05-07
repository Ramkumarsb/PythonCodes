'''
import turtle as t
x=t.Turtle()
def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle+10)

for i in range(1):
    square(45)


phone_book = {
    'Jhon':['857297000','john@xyzmail.com'],
    'Bob':['799488000', 'bob@xyzmail.com'],
    'Tom':['9749552647','tom@xyzmail.com']
}
#print(phone_book)
for g,h in phone_book.items():
    print(g,":",h)

'''
