import sys
from PIL import Image
import numpy as np

# --- 1. 添加单位转换常量 ---
# INCH_TO_CM 保持不变
INCH_TO_CM = 2.54
# 质量单位从 LB 转换为 GRAMS (1 lb = 453.592 g)
LB_TO_GRAMS = 453.592

# import image_util (已注释，保留原状)
from model_wrapper import ComplexModel

shape_aware_model = ComplexModel()

def predict_mass(filename, dims):
    global shape_aware_model
    im = Image.open(filename)
    #im = image_util.resize_and_pad_image(im,(299,299))
    im = np.array(im)

    # dims 现在已经是转换后的 (L_in, W_in, H_in)
    output = shape_aware_model.predict((im,dims)) 
    return output

def main():
    try:
        # 捕获参数
        filename, l_cm_str, w_cm_str, h_cm_str = sys.argv[1:]
    except ValueError:
        print("Usage: $ python predict_mass.py filename length width height")
        print("Length, width, and height must be floating point numbers in CENTIMETERS (cm).")
        sys.exit(1)

    # --- 2. 参数转换 (CM -> INCH) ---
    L_cm = float(l_cm_str)
    W_cm = float(w_cm_str)
    H_cm = float(h_cm_str)

    # 将 CM 转换为 INCHES (模型要求)
    L_in = L_cm / INCH_TO_CM
    W_in = W_cm / INCH_TO_CM
    H_in = H_cm / INCH_TO_CM

    # 打印输入 (使用 CM)
    print("Got: filename=", filename, 'dimensions= (', 
          "{:.2f} cm by {:.2f} cm by {:.2f} cm.)".format(L_cm, W_cm, H_cm))
    
    # 使用 INCHES 值进行预测
    dims_in_inches = (L_in, W_in, H_in)
    output_lb = predict_mass(filename, dims_in_inches) # output is in pounds

    # --- 3. 输出转换 (LB -> GRAMS) 和安全提取 ---
    # 将磅 (lb) 转换为克 (g)
    output_grams = output_lb * LB_TO_GRAMS

    # 核心修复: 安全提取标量值
    try:
        # 如果是 NumPy 数组，则提取第一个元素
        final_grams = output_grams.flatten()[0]
    except AttributeError:
        # 如果已经是标量，则直接使用
        final_grams = output_grams

    # 打印最终结果 (使用 GRAMS)
    print(filename, 'probably weighs about', "{:.2f}".format(final_grams), 'grams.')

if __name__ == "__main__":
    main()