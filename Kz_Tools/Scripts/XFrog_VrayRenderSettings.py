# python
# -*- coding: utf-8 -*-

# http://modo.sdk.thefoundry.co.uk//td-sdk/examples.html

# ----------------------------------------------------------------
# Xfrog Plants for MODO を V-RayのGPUレンダリングに対応させる
#
# 基本的な処理の流れ
# 1. Materialの種類をV-Ray Materialに変更
# 2. Stencilの画像マップをvmtl Opacity Grayscaleに変更
# 3. Stencilの画像マップのInvert設定を解除
# 4. Diffuse Colorの画像マップをvmtl Diffuse colorに変更（おまけ）
# ----------------------------------------------------------------

import lx
import modo

scene = modo.Scene()

# 選択されたitemの処理
selected = scene.selected
for selItem in selected:
    print(selItem)

    # 配下のMaterialに対する処理
    print("Materials")
    for item in selItem.children(recursive=True, itemType=modo.constants.ADVANCEDMATERIAL_TYPE):
        item.select(replace=True)
        print (item, item.name)

        # BumpMapの設定を取得（取得できない場合は5mm）
        bumpAmp = 0.005  # Default bump = 5mm
        bumpCh = item.channel('bumpAmp')
        if bumpCh is not None:
            bumpAmp = bumpCh.get()
        print(bumpAmp)

        # Materialの種類をvray_materialに変換してBump設定を引き継ぐ
        lx.eval('vray.material.changeType material.vray.material')
        lx.eval('item.channel material.vray.material$bumpAmp %s' % bumpAmp)

    # 配下のImageに対する処理
    print("Images")
    for item in selItem.children(recursive=True, itemType=modo.constants.IMAGEMAP_TYPE):
        item.select(replace=True)
        effect = lx.eval('shader.setEffect ?')

        if effect == 'stencil':
            # Effectがstencilの場合はvmtl_opacityに変更してInvertを解除
            print (item, item.name, effect)
            lx.eval('shader.setEffect vmtl_opacity')
            lx.eval('item.channel textureLayer$invert false')

        elif effect == 'diffColor':
            # EffectがdiffColorの場合はvmtl_diffuseに変更
            print (item, item.name, effect)
            lx.eval('shader.setEffect vmtl_diffuse')

# 最初に選択されていた状態に戻す
replace = True
for selItem in selected:
    selItem.select(replace=replace)
    if replace:
        replace = False  # 2つ目以降は追加
