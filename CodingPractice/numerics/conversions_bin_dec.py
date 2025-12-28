'''

@author: Solrac
'''

def convert_dec_bin(num):
    if num == 0:
        return ""
    else:
        return convert_dec_bin(num // 2) + str(num % 2)

def convert_bin_dec(string):
    result = 0
    dec_num = list(string)
    dec_num.reverse()
    for i in range(len(dec_num)):
        result += int(dec_num[i]) * 2 ** i
    return result

if __name__ == '__main__':
    print(convert_dec_bin(5))
    print(convert_bin_dec('101'))
