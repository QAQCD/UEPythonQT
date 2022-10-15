import sys
sys.path.append("..")
import unreal, os, time


#复制文件并显示进度条



#开始时间---用于进度条
start_time = time.time()

#实例化 编辑器库、编辑器资产库
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# 获取选中的资产
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)

# 复制几个
num_copies = 5

#进度条
#获取 复制的总数量、提示、是否运行
total_num_copies = num_assets * num_copies
text_label = "复制选中的资产"
running = True

with unreal.ScopedSlowTask(total_num_copies, text_label) as slow_task:
    #进度条
    slow_task.make_dialog(True)

    #复制资产
    for asset in selected_assets:
        # 获取资产的 名称和路径
        asset_name = asset.get_fname()
        asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
        #获取文件夹路径
        source_path = os.path.dirname(asset_path)
        #区别unreal.log_error("{}---{}".format(asset_path, source_path))
        #LogPython: Error: /Game/Mannequin/Character/Textures/T_UE4Logo_N.T_UE4Logo_N---/Game/Mannequin/Character/Textures

        #复制几次
        for i in range(num_copies):

            #如果用户按下取消按钮，则停止
            if slow_task.should_cancel():
                running = False
                break

            #复制的名称和路径
            new_name = "{}_{}".format(asset_name, i)
            dest_path = os.path.join(source_path, new_name)
            duplicate = editor_asset_lib.duplicate_asset(asset_path, dest_path)

            slow_task.enter_progress_frame(1)

            if duplicate is None:
                unreal.log_warning("{}------{}".format(source_path, dest_path))

        if not running:
            break

        #结束时间---用于进度条
        end_time = time.time()
        unreal.log_error("一共选中 {} 个，复制 {} 次 时间 {}".format(num_assets, num_copies, end_time - start_time))


