from TreeMap import TreeMap
from User import User

treemap = TreeMap()
print('--------------------------------------')
print('### TreeMap empty:')
treemap.display()
print('root:', treemap.root)

print('--------------------------------------')
print('### TreeMap with nodes:')

treemap['marco'] = User('Marco', 'Marco Facci', 'marco_facci@example.com')
treemap['francesco'] = User('Francesco', 'Francesco Cortese', 'francesco_cortese@example.com')
treemap['andrea'] = User('Andrea', 'Andrea Chiesa', 'andrea_chiesa@example.com')
treemap.display()
print('len:', len(treemap))
print('root:', treemap.root)
print('example:', treemap['marco'].name)

print('--------------------------------------')
print('### print all elements:')
for key, value in treemap:
    print(key, value)

print('--------------------------------------')
print('### list all elements:')
print(list(treemap))
