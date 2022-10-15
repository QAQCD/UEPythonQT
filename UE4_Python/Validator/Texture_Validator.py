import math
import sys
sys.path.append("..")
import unreal

#检查选中的纹理是否为2的幂数

#实例化编辑器
editor_util = unreal.EditorUtilityLibrary()

#获取当前选定资产的集合
#获取不到文件夹资产
selected_assets = editor_util.get_selected_assets()
num_asssets = len(selected_assets)

not_pow = 0

for asset in selected_assets:
    #获取名称和路径
    asset_name = asset.get_fname()
    asset_path = asset.get_path_name()

    #这里检查的是纹理，非纹理检查会有异常
    # 用try except来进行捕获异常
    try:
        #图片xy尺寸
        x_size = asset.blueprint_get_size_x()
        y_size = asset.blueprint_get_size_y()
        #检查xy
        is_x_valid = math.log(x_size, 2).is_integer()
        is_y_valid = math.log(y_size, 2).is_integer()

        if not is_x_valid or not is_y_valid:
            unreal.log("{}不是二的幂({},{})".format(asset_name, x_size, y_size))
            unreal.log("路径是 {}".format(asset_path))
            not_pow += 1

    except Exception as err:
        unreal.log("{}不是纹理--{}".format(asset_name, err))


unreal.log("{}选中,{}纹理有问题".format(num_asssets, not_pow))