from typing import Tuple


def run():
    height = input('身高(cm):')
    weight = input('体重(kg):')
    height = int(height)
    weight = int(weight)
    bmi_and_text = get_text(height, weight)
    print_text = "bmi为%.1f,%s" % bmi_and_text
    print(print_text)


def get_text(height: float, weight: int)-> Tuple[float, str]:
    # 低于18.5：过轻
    # 18.5-25：正常
    # 25-28：过重
    # 28-32：肥胖
    # 高于32：严重肥胖
    height = height / 100
    bmi = weight/(height*height)
    text = ''
    if(bmi < 18.5):
        text = '过轻'
    elif(bmi >= 18.5 and bmi < 25):
        text = '正常'
    elif(bmi >= 25 and bmi < 28):
        text = '过重'
    elif(bmi >= 28 and bmi < 32):
        text = '肥胖'
    else:
        text = '严重肥胖'
    return (bmi, text)


if __name__ == "__main__":
    run()
