
acl_num = int(input("¿Cuál es el número de ACL IPv4? "))

if acl_num >= 1 and acl_num <= 99:
    print("Esta es una ACL IPv4 estándar.")
elif acl_num >=100 and acl_num <= 199:
    print("Esta es una ACL IPv4 extendida.")
else:
    print("Esto no es una ACL IPv4 estándar o extendida.")
