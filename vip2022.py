
import array as arr


def in_range(n):
    if n >= 0 and n <= 255:
        return True
    return False


def has_leading_zero(n):
    if len(n) > 1:
        if n[0] == "0":
            return True
    return False


def isValid(s):

    s = s.split(".")
    if len(s) != 4:
        return 0
    for n in s:

        if has_leading_zero(n):
            return 0
        if len(n) == 0:
            return 0
        try:
            n = int(n)

            if not in_range(n):
                return 0
        except:
            return 0
    return 1


if __name__ == "__main__":
    print("please emter a valid ipv4 address 1 if it is valid and 0 for invalid")
    j=0
    list = []
    while(j<10):
        ip = input()
        if (isValid(ip)):
            list.append(ip)
            res = ''.join(format(ord(i), '08b') for i in ip)
            list.append(res)
            print("The ip after binary conversion : " + str(res))
            octalIP='.'.join(["%04o" % int(x) for x in ip.split('.')])
            list.append(octalIP)
            print("The ip after octal conversion : " + octalIP)
            ip = ip.split('.')
            hexa = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, ip))
            list.append(hexa)
            print("the ip after hexadecimal conversion : "+hexa)
            j=j+1
        with open('listfile.txt', 'w') as filehandle:
            for listitem in list:
                filehandle.write('%s\n' % listitem)