"""
File: my_drawing.py
Name: Marco Yue
----------------------
TODO: draw something
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(width=450, height=900, title='Amazing Profit')


def main():
    """
    A stock trading apps screen.
    Dream come True!
    Hope I won't see this terrible scene on my phone in my lifetime ....
    """
    top_line = GRect(450, 20, x=0, y=0)
    top_line.filled = True
    top_line.color = 'darkblue'
    top_line.fill_color = 'darkblue'
    window.add(top_line)

    time_label = GLabel(' 下午 1:30 ')
    time_label.font = 'Courier-14'
    time_label.color = 'white'
    window.add(time_label, 10, 22)

    power_label = GLabel(' 10% ')
    power_label.font = 'Helvetica-14'
    power_label.color = 'white'
    window.add(power_label, 400, 22)

    power = GRect(10, 15, x=390, y=3)
    power.filled = True
    power.color = 'red'
    power.fill_color = 'red'
    window.add(power)

    tool_bar = GRect(450, 35, x=0, y=21)
    tool_bar.filled = True
    tool_bar.color = 'black'
    tool_bar.fill_color = 'black'
    window.add(tool_bar)

    tool_bar_label = GLabel(' 下單  委託  明細  庫存  帳務 ')
    tool_bar_label.font = 'Courier-18'
    tool_bar_label.color = 'white'
    window.add(tool_bar_label, 30, 55)

    find_mark = GOval(25, 25, x=410, y=25)
    find_mark.filled = False
    find_mark.color = 'white'
    window.add(find_mark)

    find_mark_2 = GLine(435, 45, 445, 55)
    find_mark_2.filled = False
    find_mark_2.color = 'white'
    window.add(find_mark_2)

    tool_bar_tri = GPolygon()
    tool_bar_tri.add_vertex((15, 40))
    tool_bar_tri.add_vertex((30, 50))
    tool_bar_tri.add_vertex((30, 30))
    tool_bar_tri.filled = True
    tool_bar_tri.fill_color = 'white'
    window.add(tool_bar_tri)

    mid_up = GRect(450, 200, x=0, y=56)
    mid_up.filled = True
    mid_up.color = 'black'
    mid_up.fill_color = 'black'
    window.add(mid_up)

    account = GRect(250, 35, x=10, y=56)
    account.filled = False
    account.color = 'white'
    window.add(account)

    account_label = GLabel(' 證878787-66666')
    account_label.font = 'Courier-18'
    account_label.color = 'white'
    window.add(account_label, 10, 90)

    account_tri = GPolygon()
    account_tri.add_vertex((240, 85))
    account_tri.add_vertex((250, 65))
    account_tri.add_vertex((230, 65))
    account_tri.filled = True
    account_tri.fill_color = 'white'
    window.add(account_tri)

    account_r = GRect(150, 35, x=280, y=56)
    account_r.filled = False
    account_r.color = 'white'
    window.add(account_r)

    account_label_r = GLabel(' 現股 ')
    account_label_r.font = 'Courier-18'
    account_label_r.color = 'white'
    window.add(account_label_r, 330, 90)

    account_tri_r = GPolygon()
    account_tri_r.add_vertex((410, 85))
    account_tri_r.add_vertex((420, 65))
    account_tri_r.add_vertex((400, 65))
    account_tri_r.filled = True
    account_tri_r.fill_color = 'white'
    window.add(account_tri_r)

    payback_mark = GOval(120, 120, x=50, y=105)
    payback_mark.filled = True
    payback_mark.fill_color = 'limegreen'
    payback_mark.color = 'limegreen'
    window.add(payback_mark)

    payback_mark2 = GOval(100, 100, x=60, y=115)
    payback_mark2.filled = True
    payback_mark2.fill_color = 'black'
    window.add(payback_mark2)

    payback_label = GLabel('股票報酬')
    payback_label.font = 'Courier-13'
    payback_label.color = 'white'
    window.add(payback_label, 75, 160)

    payback_label2 = GLabel('-100%')
    payback_label2.font = 'Courier-15'
    payback_label2.color = 'limegreen'
    window.add(payback_label2, 80, 190)

    payback_worth = GLabel('股票市值         0')
    payback_worth.font = 'Courier-16'
    payback_worth.color = 'white'
    window.add(payback_worth, 200, 130)

    payback_cost = GLabel('總成本     2,000,000')
    payback_cost.font = 'Courier-16'
    payback_cost.color = 'white'
    window.add(payback_cost, 200, 170)

    coin_style = GLabel('(幣別:新台幣)')
    coin_style.font = 'Courier-12'
    coin_style.color = 'white'
    window.add(coin_style, 330, 200)

    counting = GRect(110, 35, x=200, y=210)
    counting.filled = True
    counting.fill_color = 'darkblue'
    counting.color = 'white'
    window.add(counting)

    searching = GRect(110, 35, x=320, y=210)
    searching.filled = True
    searching.fill_color = 'darkblue'
    searching.color = 'white'
    window.add(searching)

    counting_label = GLabel('當沖試算')
    counting_label.font = 'Courier-16'
    counting_label.color = 'white'
    window.add(counting_label, 213, 240)

    searching_label = GLabel('維持率試算')
    searching_label.font = 'Courier-15'
    searching_label.color = 'white'
    window.add(searching_label, 323, 240)

    real_payback = GLabel('報酬 -2,000,000')
    real_payback.font = 'Courier-12'
    real_payback.color = 'limegreen'
    window.add(real_payback, 40, 250)

    mid_blue_bar = GRect(450, 50, x=0, y=256)
    mid_blue_bar.filled = True
    mid_blue_bar.fill_color = 'midnightblue'
    mid_blue_bar.color = 'blue'
    window.add(mid_blue_bar)

    mid_blue_label = GLabel(' 名稱    市/均     股數/可下單數     損益')
    mid_blue_label.font = 'cCourier-20'
    mid_blue_label.color = 'white'
    window.add(mid_blue_label, 0, 295)

    first = GRect(450, 80, x=0, y=306)
    first.filled = True
    first.fill_color = 'black'
    first.color = 'blue'
    window.add(first)

    first_label_1 = GLabel(' 台G電     0.0000              400 ')
    first_label_1.font = 'cCourier-18'
    first_label_1.color = 'white'
    window.add(first_label_1, 0, 345)

    first_label_r1 = GLabel('-400,000')
    first_label_r1.font = 'cCourier-18'
    first_label_r1.color = 'limegreen'
    window.add(first_label_r1, 360, 345)

    first_label_2 = GLabel('   現股      1000.0              400 ')
    first_label_2.font = 'cCourier-18'
    first_label_2.color = 'white'
    window.add(first_label_2, 0, 375)

    first_label_r2 = GLabel('-100.00%')
    first_label_r2.font = 'cCourier-18'
    first_label_r2.color = 'limegreen'
    window.add(first_label_r2, 360, 375)

    second = GRect(450, 80, x=0, y=386)
    second.filled = True
    second.fill_color = 'black'
    second.color = 'blue'
    window.add(second)

    second_label_1 = GLabel(' 大綠光    0.0000              400 ')
    second_label_1.font = 'cCourier-18'
    second_label_1.color = 'white'
    window.add(second_label_1, 0, 425)

    second_label_r1 = GLabel('-400,000')
    second_label_r1.font = 'cCourier-18'
    second_label_r1.color = 'limegreen'
    window.add(second_label_r1, 360, 425)

    second_label_2 = GLabel('   現股      1000.0              400 ')
    second_label_2.font = 'cCourier-18'
    second_label_2.color = 'white'
    window.add(second_label_2, 0, 455)

    second_label_r2 = GLabel('-100.00%')
    second_label_r2.font = 'cCourier-18'
    second_label_r2.color = 'limegreen'
    window.add(second_label_r2, 360, 455)

    third = GRect(450, 80, x=0, y=466)
    third.filled = True
    third.fill_color = 'black'
    third.color = 'blue'
    window.add(third)

    third_label_1 = GLabel(' 連發哥    0.0000              400 ')
    third_label_1.font = 'cCourier-18'
    third_label_1.color = 'white'
    window.add(third_label_1, 0, 505)

    third_label_r1 = GLabel('-400,000')
    third_label_r1.font = 'cCourier-18'
    third_label_r1.color = 'limegreen'
    window.add(third_label_r1, 360, 505)

    third_label_2 = GLabel('   現股      1000.0              400 ')
    third_label_2.font = 'cCourier-18'
    third_label_2.color = 'white'
    window.add(third_label_2, 0, 535)

    third_label_r2 = GLabel('-100.00%')
    third_label_r2.font = 'cCourier-18'
    third_label_r2.color = 'limegreen'
    window.add(third_label_r2, 360, 535)

    four = GRect(450, 80, x=0, y=546)
    four.filled = True
    four.fill_color = 'black'
    four.color = 'blue'
    window.add(four)

    four_label_1 = GLabel(' 海公公    0.0000              400 ')
    four_label_1.font = 'cCourier-18'
    four_label_1.color = 'white'
    window.add(four_label_1, 0, 585)

    four_label_r1 = GLabel('-400,000')
    four_label_r1.font = 'cCourier-18'
    four_label_r1.color = 'limegreen'
    window.add(four_label_r1, 360, 585)

    four_label_2 = GLabel('   現股      1000.0              400 ')
    four_label_2.font = 'cCourier-18'
    four_label_2.color = 'white'
    window.add(four_label_2, 0, 615)

    four_label_r2 = GLabel('-100.00%')
    four_label_r2.font = 'cCourier-18'
    four_label_r2.color = 'limegreen'
    window.add(four_label_r2, 360, 615)

    fifth = GRect(450, 80, x=0, y=626)
    fifth.filled = True
    fifth.fill_color = 'black'
    fifth.color = 'blue'
    window.add(fifth)

    fifth_label_1 = GLabel(' 種花電    0.0000              400 ')
    fifth_label_1.font = 'cCourier-18'
    fifth_label_1.color = 'white'
    window.add(fifth_label_1, 0, 665)

    fifth_label_r1 = GLabel('-400,000')
    fifth_label_r1.font = 'cCourier-18'
    fifth_label_r1.color = 'limegreen'
    window.add(fifth_label_r1, 360, 665)

    fifth_label_2 = GLabel('   現股      1000.0              400 ')
    fifth_label_2.font = 'cCourier-18'
    fifth_label_2.color = 'white'
    window.add(fifth_label_2, 0, 695)

    fifth_label_r2 = GLabel('-100.00%')
    fifth_label_r2.font = 'cCourier-18'
    fifth_label_r2.color = 'limegreen'
    window.add(fifth_label_r2, 360, 695)

    final = GRect(450, 200, x=0, y=707)
    final.filled = True
    final.fill_color = 'black'
    final.color = 'black'
    window.add(final)

    bot = GRect(450, 50, x=0, y=857)
    bot.filled = True
    bot.fill_color = 'darkgrey'
    bot.color = 'gray'
    window.add(bot)

    bot_tri = GPolygon()
    bot_tri.add_vertex((100, 890))
    bot_tri.add_vertex((80, 880))
    bot_tri.add_vertex((100, 870))
    bot_tri.filled = False
    bot_tri.color = 'white'
    bot_tri.fill_color = 'white'
    window.add(bot_tri)

    bot_oval = GOval(25, 25, x=207, y=868)
    bot_oval.filled = False
    bot_oval.color = 'white'
    bot_oval.fill_color = 'white'
    window.add(bot_oval)

    bot_rect = GRect(20, 20, x=347, y=870)
    bot_rect.filled = False
    bot_rect.color = 'white'
    bot_rect.fill_color = 'white'
    window.add(bot_rect)

    house_tri = GPolygon()
    house_tri.add_vertex((20, 835))
    house_tri.add_vertex((50, 835))
    house_tri.add_vertex((35, 820))
    house_tri.filled = True
    house_tri.fill_color = 'white'
    window.add(house_tri)

    house_rect1 = GRect(8, 13, x=25, y=835)
    house_rect1.filled = True
    house_rect1.fill_color = 'white'
    window.add(house_rect1)

    house_rect2 = GRect(8, 13, x=36, y=835)
    house_rect2.filled = True
    house_rect2.fill_color = 'white'
    window.add(house_rect2)

    house_label = GLabel('  選股    自選     交易    行情     專家')
    house_label.font = 'cCourier-18'
    house_label.color = 'white'
    window.add(house_label, 80, 850)

    warn = GLabel('*注意事項*')
    warn.font = 'cCourier-15'
    warn.color = 'white'
    window.add(warn, 10, 810)

    warn_line = GLabel('*投資一定有風險，基金投資幾乎穩賠，申購前應詳閱公開說明書。*')
    warn_line.font = 'cCourier-8'
    warn_line.color = 'white'
    window.add(warn_line, 120, 805)


if __name__ == '__main__':
    main()
