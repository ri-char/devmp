import sys
code = [0xB8, 0x54, 0x54, 0x00, 0x00, 0x66, 0x31, 0xC0, 0xBB, 0x54,
        0x54, 0x00, 0x00, 0x31, 0xDB, 0xB9, 0x45, 0x45, 0x00, 0x00,
        0x48, 0x31, 0xC9, 0xBA, 0x43, 0x43, 0x00, 0x00, 0x83, 0xE2,
        0x00]

sys.path.append('./build/')

import pydevmp

im = pydevmp.InstManager()
print(im.setAsm(bytes(code), 0x1000))
while im.next():
    pass
print(im)
print(im.getDeletedAddr())
print(im.getUsefulAddr())
print(bytes(im))