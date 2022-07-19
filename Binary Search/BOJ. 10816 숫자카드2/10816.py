# ¼ýÀÚÄ«µå 2
# »ó±ÙÀÌ´Â n°³ÀÇ ¼ýÀÚÄ«µå¸¦ °¡Áö°í ÀÖ´Ù.
# Á¤¼ö m°³°¡ ÁÖ¾îÁ³À» ¶§, ÀÌ ¼ö°¡ ÀûÇôÀÖ´Â ¼ýÀÚÄ«µå¸¦ »ó±ÙÀÌ´Â ¸î°³¸¦ °¡Áö°íÀÖÀ»±î
# ÀÌÀü Ç®ÀÌ >> ÃÖ¾ÇÀÇ °æ¿ì
import sys

iput = sys.stdin.readline

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
things = list(map(int, input().split()))

# targetÀÇ °¡Àå ¿À¸¥ÂÊÀ» Ã£±â À§ÇÑ ÀÌÁø Å½»ö ÇÔ¼ö
'''
±âÁ¸ÀÇ ÀÌÁø Å½»öÀÇ º¯Çü
±âÁ¸ÀÇ ÀÌÁø Å½»ö¿¡¼­ arr[mid] == targetÀÌ¸é °á°ú¸¦ return ÇÏ´Âµ¥ ¹Ý¿¡
º¯ÇüÇÑ ºÎºÐÀº arr[mid] == targetÀÌ¶óµµ start°ªÀ» Á¶Á¤ÇØÁÖ¾î °¡Àå ¿À¸¥ÂÊ targetÀÇ ÀÎµ¦½º °ªÀ» Ã£À½
Á¾·á Á¶°ÇÀº start == end ÀÏ °æ¿ì, Áï Å½»ö ¹üÀ§°¡ ÇÏ³ªÀÏ °æ¿ì·Î Á¶Á¤.
'''
def upper_target(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] > target:
        return upper_target(start, mid, arr, target)
    else:
        return upper_target(mid + 1, end, arr, target)

# targetÀÇ °¡Àå ¿ÞÂÊÀ» Ã£±â À§ÇÑ ÀÌÁø Å½»ö ÇÔ¼ö
def lower_target(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] >= target:
        return lower_target(start, mid, arr, target)
    else:
        return lower_target(mid + 1, end, arr, target)


def main_func():
    for num in things:
        print(upper_target(0, n, array, num) - lower_target(0, n, array, num), end=" ")


main_func()
