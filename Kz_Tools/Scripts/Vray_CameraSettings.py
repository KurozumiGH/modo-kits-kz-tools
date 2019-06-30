# python
# -*- coding: utf-8 -*-

# http://modo.sdk.thefoundry.co.uk//td-sdk/examples.html

import modo


# V-Ray Exposure の反転
def toggleVrayExposure():
    # レンダリングに利用するカメラを取得
    scene = modo.Scene()
    camera = scene.renderCamera

    # vray_exposureのchannelが有効な場合のみ設定を反転
    ch_vray_exposure = camera.channel('vray_exposure')
    if ch_vray_exposure is not None:
        param = not ch_vray_exposure.get()  # 反転
        print(camera, "Set vray_exposure", param)
        ch_vray_exposure.set(param)
    else:
        print("vray_exposure channel not found.")


toggleVrayExposure()
