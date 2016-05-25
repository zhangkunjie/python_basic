# coding=utf-8
f=open("D://train.txt", "w",encoding='utf-8')
#显示指针的位置
print(f.tell())
f.write("AAAAAABBBBBBBBBBBBBBBBB\n打死的大的");
print(f.tell())
f.close()