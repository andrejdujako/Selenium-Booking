from booking.booking import Booking
import booking.constants as const
import time
#
# inst = Booking()
# inst.land_first_page()

# with Booking(teardown=True) as bot:
try:
    with Booking() as bot:
        bot.land_first_page()
        # print("Exiting With block..")
        # Using context managers as soon as PY reaches the end of the WITH block
        # it automatically calls the def __exit__ method
        # bot.change_currency(currency='USD')
        # bot.change_currency(currency='MKD')
        bot.select_place_to_go(const.DESTINATION)
        bot.select_date(check_in=const.CHECK_IN_DATE, check_out=const.CHECK_OUT_DATE)
        bot.select_adults(const.ADULTS, const.CHILDREN, const.ROOMS)
        bot.click_search()
        bot.apply_filters()
        bot.refresh() # Workaround to get right results
        bot.get_results()
        # print(len(bot.get_results())) # we get 25 results

except Exception as e:
    if 'in PATH' in str(e):
        print("There is a problem with the selenium driver")
        print(' Windows: \n'
              r'set PATH=%PATH%;C:\path-to-folder\ ' 
              '\n Linux: \n'
              'PATH=$PATH:/path/to/folder/ \n')
    else:
        raise
#     we raise the original exception otherwise
