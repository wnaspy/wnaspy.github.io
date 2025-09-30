import marshal
import pickle
import pickletools

data = {"username":"konchan","age":21}
pickle_bytes = b'\x80\x04\x95"\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08username\x94\x8c\x07konchan\x94\x8c\x03age\x94K\x15u.'

print(pickletools.dis(pickle_bytes))