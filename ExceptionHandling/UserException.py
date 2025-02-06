class PinError(Exception):
    pass
pin = int(input('Enter 4-digit pin'))
correctPin = 1212
try:
    if pin == correctPin:
        print('Account Unblocked')
    else:
        raise PinError('Entered pin is',pin)
except PinError as e:
    print('Incorrect pin', e)