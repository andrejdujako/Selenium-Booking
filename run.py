from booking.booking import Booking
#
# inst = Booking()
# inst.land_first_page()

# with Booking(teardown=True) as bot:
with Booking() as bot:
    bot.land_first_page()
    # print("Exiting With block..")
    # Using context managers as soon as PY reaches the end of the WITH block
    # it automatically calls the def __exit__ method
    # bot.change_currency(currency='USD')
    # bot.change_currency(currency='MKD')
    bot.select_place_to_go("Ohrid")
    bot.select_date(check_in="2022-09-29", check_out="2022-10-10")
    bot.select_adults(4, 0, 3)
    bot.click_search()
    bot.sort_button()

