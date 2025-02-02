import re
from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsValidIMEI(BaseFilter):
    async def __call__(self, message: Message):
        try:
            if not re.match(r'^\d{15}$', str(message.text)):
                return False
        
            imei_digits = [int(digit) for digit in str(message.text)]
            checksum = 0
            
            for i in range(14):
                digit = imei_digits[i]
                if i % 2 == 0:
                    checksum += digit
                else:
                    double = digit * 2
                    checksum += double if double < 10 else double - 9
            
            return (checksum + imei_digits[14]) % 10 == 0
        except Exception as e:
            print(e)
            return False