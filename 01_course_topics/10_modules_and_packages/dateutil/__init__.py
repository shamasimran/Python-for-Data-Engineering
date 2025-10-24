# It tells Python this folder is a package.
# Without it, older Python versions (<3.3) won’t recognize it as a package.

# if we keep this file empty, Python will still treat the directory as a package.
# but, in that case the import statements will be different in main.py as given below:
# from dateutil.formatter import format_date
# from dateutil.calculator import DateCalculator 

from .formatter import format_date
from .calculator import DateCalculator

#  __all__ helps you control the public interface of your package.
# it is used to explicitly define which names are exported when someone imports your package using: from dateutil import *

__all__ = ["format_date", "DateCalculator"]