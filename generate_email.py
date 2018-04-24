def trunlde(nangluong,mau):
    if nangluong >=100:
        print("ban co the xai duoc  chieu cuoi(chieu r)")
    elif nangluong >=70 and nangluong < 100:
        print("ban co  the xai duoc chieu q,w,e")
    elif nangluong <70 and nangluong > 50:
        print("ban co the xai duoc chieu q,w")
    elif nangluong <=30 and nangluong<50:
        print("ban co the xai duoc chieu q")
    else:
        print("ban da khong du nang luong de xai bat cu chieu nao")

    if(mau>0):
        print("ban con song")
    else:
        print("ban die")


trunlde(50,9)
trunlde(20,8)
trunlde(150,0)
