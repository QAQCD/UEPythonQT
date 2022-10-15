import sys
sys.path.append("..")
import unreal, json


#批量重命名(添加前缀)

#实例化 系统库、编辑器库
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

#前缀映射--前缀库
prefix_mapping = {}
with open('E:\\Unreal Projects\\UEPython\\UE4_Python\\prefix_mapping.json', 'r') as json_file:
    prefix_mapping = json.loads(json_file.read())

# 获取选中的资产
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)

# 更改了几处前缀
prefixed = 0


#循环 选中的资产并添加
for asset in selected_assets:
    #获取资产的 名称和类别
    # asset_name系统库获取对象名称资产
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    #获取前缀
    class_prefix = prefix_mapping.get(class_name, None)

    if class_prefix is None:
        # 如果前缀库中没有对应的前缀
        unreal.log_warning("资产名称 {} 在前缀库中没有添加 {} 资产类别".format(asset_name, class_name))
        continue

    if not asset_name.startswith(class_prefix):
        # 如果资产有前缀(和前缀库对应)
        new_name = class_prefix + asset_name
        # 执行替换--不执行等于没做
        editor_util.rename_asset(asset, new_name)
        prefixed += 1
        unreal.log("资产名称 {} 资产类别 {} 前缀名 {}".format(asset_name, class_name, class_prefix))

    else:
        unreal.log("资产名称 {} 资产类别 {} 前缀名是 {}".format(asset_name, class_name, class_prefix))

    unreal.log("添加了 {} 处前缀,一共选择了 {} 资产".format(prefixed, num_assets))
