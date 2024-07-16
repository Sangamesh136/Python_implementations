# def divide(a):
#     try :
#         return a/0
#     except ZeroDivisionError:
#         print("cant divide by 0")
#         return
# divide(5)

x=0
y="ghj"
try:
    z=x+y
except TypeError:
    print("te")
except ZeroDivisionError:
    print("zde")
except SyntaxError:
    print("se")
except SystemError:
    print("sye")
except ValueError:
    print("ve")
except IndentationError:
    print("Inderr")
except IndexError:
    print("ir")
except ImportError:
    print("Import err")
except InterruptedError:
    print("iperr")
