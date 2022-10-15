import sys
sys.path.append("..")
import unreal
import os


#移动文件到哪个文件夹中



#实例化 系统库、编辑器库、编辑器资产库
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# 获取选中的资产
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)

# 清除了几个
cleaned = 0

#文件移动的路径
parent_dir = "\\Game"
#移动到当前文件夹目录下
if num_assets > 0:
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(selected_assets[0])
    parent_dir = os.path.dirname(asset_path)


for asset in selected_assets:
    #获取资产的 名称和类别
    #asset_name系统库获取对象名称资产
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    #复制到哪的文件
    #检查异常
    try:
        #新文件夹的名称是类别名
        new_path = os.path.join(parent_dir, class_name, asset_name)
        #执行文件--不执行等于没做
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        cleaned += 1

        unreal.log_error("资产名称 {} 它移动到的文件路径 {}".format(asset_name, new_path))

    except Exception as err:
        unreal.log_error("资产名称 {} 它移动到的文件路径 {}".format(asset_name, new_path))


    unreal.log_error("移动了 {} 个资产,一共选中了 {} 个".format(cleaned, num_assets))