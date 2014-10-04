# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QDate(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDate()
    QDate(int, int, int)
    QDate(QDate)
    """
    def addDays(self, p_int): # real signature unknown; restored from __doc__
        """ QDate.addDays(int) -> QDate """
        return QDate

    def addMonths(self, p_int): # real signature unknown; restored from __doc__
        """ QDate.addMonths(int) -> QDate """
        return QDate

    def addYears(self, p_int): # real signature unknown; restored from __doc__
        """ QDate.addYears(int) -> QDate """
        return QDate

    def currentDate(self): # real signature unknown; restored from __doc__
        """ QDate.currentDate() -> QDate """
        return QDate

    def day(self): # real signature unknown; restored from __doc__
        """ QDate.day() -> int """
        return 0

    def dayOfWeek(self): # real signature unknown; restored from __doc__
        """ QDate.dayOfWeek() -> int """
        return 0

    def dayOfYear(self): # real signature unknown; restored from __doc__
        """ QDate.dayOfYear() -> int """
        return 0

    def daysInMonth(self): # real signature unknown; restored from __doc__
        """ QDate.daysInMonth() -> int """
        return 0

    def daysInYear(self): # real signature unknown; restored from __doc__
        """ QDate.daysInYear() -> int """
        return 0

    def daysTo(self, QDate): # real signature unknown; restored from __doc__
        """ QDate.daysTo(QDate) -> int """
        return 0

    def fromJulianDay(self, p_int): # real signature unknown; restored from __doc__
        """ QDate.fromJulianDay(int) -> QDate """
        return QDate

    def fromString(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.fromString(str, Qt.DateFormat format=Qt.TextDate) -> QDate
        QDate.fromString(str, str) -> QDate
        """
        return QDate

    def getDate(self): # real signature unknown; restored from __doc__
        """ QDate.getDate() -> (int, int, int) """
        pass

    def gregorianToJulian(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QDate.gregorianToJulian(int, int, int) -> int """
        return 0

    def isLeapYear(self, p_int): # real signature unknown; restored from __doc__
        """ QDate.isLeapYear(int) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QDate.isNull() -> bool """
        return False

    def isValid(self, p_int=None, p_int_1=None, p_int_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.isValid() -> bool
        QDate.isValid(int, int, int) -> bool
        """
        return False

    def julianToGregorian(self, p_int): # real signature unknown; restored from __doc__
        """ QDate.julianToGregorian(int) -> (int, int, int) """
        pass

    def longDayName(self, p_int, QDate_MonthNameType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.longDayName(int) -> str
        QDate.longDayName(int, QDate.MonthNameType) -> str
        """
        return ""

    def longMonthName(self, p_int, QDate_MonthNameType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.longMonthName(int) -> str
        QDate.longMonthName(int, QDate.MonthNameType) -> str
        """
        return ""

    def month(self): # real signature unknown; restored from __doc__
        """ QDate.month() -> int """
        return 0

    def setDate(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QDate.setDate(int, int, int) -> bool """
        return False

    def setYMD(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QDate.setYMD(int, int, int) -> bool """
        return False

    def shortDayName(self, p_int, QDate_MonthNameType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.shortDayName(int) -> str
        QDate.shortDayName(int, QDate.MonthNameType) -> str
        """
        return ""

    def shortMonthName(self, p_int, QDate_MonthNameType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.shortMonthName(int) -> str
        QDate.shortMonthName(int, QDate.MonthNameType) -> str
        """
        return ""

    def toJulianDay(self): # real signature unknown; restored from __doc__
        """ QDate.toJulianDay() -> int """
        return 0

    def toPyDate(self): # real signature unknown; restored from __doc__
        """ QDate.toPyDate() -> datetime.date """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDate.toString(Qt.DateFormat format=Qt.TextDate) -> str
        QDate.toString(str) -> str
        """
        return ""

    def weekNumber(self): # real signature unknown; restored from __doc__
        """ QDate.weekNumber() -> (int, int) """
        pass

    def year(self): # real signature unknown; restored from __doc__
        """ QDate.year() -> int """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DateFormat = 0
    MonthNameType = None # (!) real value is ''
    StandaloneFormat = 1


