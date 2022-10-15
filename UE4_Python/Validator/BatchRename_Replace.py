import sys
sys.path.append("..")
import unreal

#批量重命名(替换名称)

def rename_assets(search_pattern, replace_pattern, use_case):
    #实例化 系统库、编辑器库、字符串库
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    #获取选中的资产
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    #替换了几处
    replaced = 0

    #unreal.log("选中了 {} 资产".format(num_assets))

    #循环 选中的资产并替换
    for asset in selected_assets:
        #获取选中资产的名称
        # asset_name系统库获取对象名称资产
        asset_name = system_lib.get_object_name(asset)
        #unreal.log(asset_name)

        #如果包含 选中资产的名称，要替换的名称，忽略大小写吗
        if string_lib.contains(asset_name, search_pattern, use_case = use_case):
            #如果不忽略大小写
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            #替换的名称
            replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case = search_case)
            #执行替换--不执行等于没做
            editor_util.rename_asset(asset, replaced_name)
            # unreal.log(replaced_name)

            replaced +=1
            unreal.log("替换 {} 为 {}".format(asset_name, replaced_name))
        
        else:
            unreal.log("{} 中不含 {} 字符,无法替换已跳过".format(asset_name, search_pattern))

    unreal.log("替换 {} 处名称，一共选中了 {} 资产".format(replaced, num_assets))


#将名称中含有 New 字符串的，替换为 AA ,不忽略大小写
rename_assets("New", "AA", False)