print(__name__)
print(__file__)
# پایتون اینا رو معرفی کرده است
print(__package__)


if __name__ == "__main__":
    print("خودت داری همین فایل را اجرا میکنی")
else:
    print("یک فایل دیگر دارد این را اجرا میکند")