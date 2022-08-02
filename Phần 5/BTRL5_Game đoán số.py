"""
- Máy random 1 số trong đoạn [1...100]
- Người chơi đoán số, chỉ được đoán sai 7 lần. Mỗi lần đoán sai sẽ thông báo số người chơi đoán nhỏ hơn hay lớn hơn số
của máy và hiển thị số lần đoán.
- Game kết thúc khi: đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
- Sau khi game kết thúc hỏi người chơi có tiếp tục hay không ?
"""
import random
win = False
while True:
    n = random.randint(1, 100)
    for i in range(1, 8):
        print("-> Bạn đoán lần {0}".format(i))
        x = int(input("Mời bạn nhập 1 số: "))
        if x == n:
            print("Chúc mừng nhé. Bạn đoán đúng rồi! -> Số máy là: {0}".format(n))
            win = True
            break
        else:
            if n < x:
                print("<Nhỏ hơn số bạn nhập>")
            else:
                print("<Lớn hơn số bạn nhập>")
    if not win:
        print("GAME OVER")
        print("Số của máy là: {0}".format(n))
    print("Bạn có muốn tiếp tục hay không ?(c/k)")
    a = input()
    if a == "k":
        break
print("Cám ơn bạn đã tham gia trò chơi. Hẹn gặp lại!")
