
![qwenvl](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/db84bdde-e2be-48fa-8ce5-cdd5ee2dd057)

<h1 align="center">QWen-VL in ComfyUI</h1>

![Dingtalk_20240130191521](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/5d10adba-90a6-48e0-94de-33d10b5d32f9)


## 项目介绍 | Info

- 将阿里 [QWen-VL](https://github.com/QwenLM/Qwen-VL) 双模型（Plus & Max）通过 API 调用引入到 ComfyUI 中，初测下来 QWen-VL 是目前开源世界最好的视觉模型

- 目前 QWen-VL API 免费开放（🆕刚收到阿里的通知：3.18开始正式收费！收费标准见下图），你可以在这里申请一个自己的 API Key：[QWen-VL API 申请](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key)

  ![image](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/8e28aa5a-637b-43b6-b43b-a98da7d01779)


- 版本：V1.0 支持单/多轮对话双模式、支持读取本地图像


## 视频演示



https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/430d4ea1-6484-46e2-85bf-ad7cf95dda95



## 详细说明 | Features

- QWen-VL 目前提供 2 种模型：

<!---
   - QWen-VL-Plus: 通义千问大规模视觉语言模型增强版。大幅提升细节识别能力和文字识别能力，支持超百万像素分辨率和任意长宽比规格的图像。在广泛的视觉任务上提供卓越的性能。

   - QWen-VL-Max: 通义千问超大规模视觉语言模型。相比增强版，再次提升视觉推理能力和指令遵循能力，提供更高的视觉感知和认知水平。在更多复杂任务上提供最佳的性能。
--->

   | 模型         | 说明                      |
   |--------------|---------------------------|
   | QWen-VL-Plus | 通义千问大规模视觉语言模型增强版。大幅提升细节识别能力和文字识别能力，支持超百万像素分辨率和任意长宽比规格的图像。在广泛的视觉任务上提供卓越的性能。|
   | QWen-VL-Max  | 通义千问超大规模视觉语言模型。相比增强版，再次提升视觉推理能力和指令遵循能力，提供更高的视觉感知和认知水平。在更多复杂任务上提供最佳的性能。        |


- 节点（均采用隐式 API KEY）:

   - ㊙️QWenVL_Zho：同时支持两种模型，接受本地图像作为输入（图像仅临时储存用完会自动清除）     

   - ㊙️QWenVL_Chat_Zho：同时支持两种模型，支持上下文窗口，接受本地图像作为输入（图像储存在 /custom nodes/ComfyUI-Qwen-VL-API/qw 文件夹中，可手动清理）
  

- 节点示例 & 与 Gemini-Pro-Vision 对比（描述更准更详细，且支持上下文多轮对话，Gemini-Pro-Vision 仅支持单轮对话）：


  ![Dingtalk_20240130191546](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/0806782a-341b-4d53-b482-04f515db2bc3)


  ![Dingtalk_20240130133911](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/1c62f1ae-2832-4b07-9f04-0b835f8c7a8f)


- 上下文多轮对话：

  ![Dingtalk_20240130174301](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/e63c1ea1-c96a-4550-8c40-7af54a2f4262)


## 参数说明 | Parameters

- image：接入本地图像
- prompt：提示词
- model_name：模型选择，QWen-VL-Plus 或 QWen-VL-Max
- seed：随机种子


## 使用方法 | How to use

- 首先需要申请一个自己的 QWen-VL_API_Key：[QWen-VL API 申请](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key)

- 将你的 QWen-VL_API_Key 添加到 `config.json` 文件中，运行时会自动加载

- 输出节点可配合像[ComfyUI-Gemini](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini)中 ✨DisplayText_Zho 一样的任何接受文本的节点

## 安装 | Install

- 推荐使用管理器 ComfyUI Manager 安装（ON THE WAY）

- 手动安装：
    1. `cd custom_nodes`
    2. `https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API.git`
    3. `cd custom_nodes/ComfyUI-Qwen-VL-API`
    4. `pip install -r requirements.txt`
    5. 重启 ComfyUI


## 工作流 | Workflow

### V1.0 工作流

  [Qwen-VL V1.0【Zho】](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/blob/main/QWEN-VL%20WORKFLOWS/Qwen-VL%20V1.0%E3%80%90Zho%E3%80%91.json)

  ![Dingtalk_20240130200115](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API/assets/140084057/bae0447b-a4bf-45a3-ad27-c496a02bd6d2)


## 更新日志 | Changelog

20240130

- V1.0版：支持单/多轮对话双模式、支持读取本地图像

- 创建项目


## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API&type=Timeline)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-Qwen-VL-API&Timeline)


## Credits

[QWen-VL](https://github.com/QwenLM/Qwen-VL)
