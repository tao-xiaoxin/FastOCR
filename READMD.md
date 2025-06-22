# FastOCR

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.13+-green.svg)](https://fastapi.tiangolo.com/)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-3.0-orange.svg)](https://github.com/PaddlePaddle/PaddleOCR)
[![License](https://img.shields.io/badge/License-Apache%202.0-red.svg)](LICENSE)

## 📖 项目简介

FastOCR 是一个基于 FastAPI 框架和 PaddleOCR 3.0 引擎构建的高性能光学字符识别（OCR）服务。该项目利用百度飞桨团队开源的 PaddleOCR 3.0 技术，提供快速、准确、易用的 OCR 解决方案，支持多种图片格式的文字识别，并提供 RESTful API 接口。

## ✨ 主要特性

- 🚀 **高性能**: 基于 FastAPI 异步框架和 PaddleOCR 引擎，提供快速响应
- 🎯 **高精度**: 集成 PaddleOCR 先进算法，支持中英文等多语言识别
- 📱 **多格式支持**: 支持 JPG、PNG、PDF 等多种图片格式
- 🌐 **RESTful API**: 提供标准化的 HTTP API 接口
- 🔧 **易于部署**: 支持 Docker 容器化部署
- 📊 **实时监控**: 内置性能监控和日志记录
- 🔒 **安全可靠**: 支持文件类型验证和大小限制
- 🎨 **版面分析**: 支持文本检测、方向分类、文本识别一体化

## 🛠️ 技术栈

- **后端框架**: FastAPI
- **OCR 引擎**: PaddleOCR (核心引擎)
- **异步处理**: asyncio, aiofiles
- **数据验证**: Pydantic
- **文档生成**: Swagger UI / ReDoc
- **容器化**: Docker

## 📋 系统要求

- Python 3.8+
- 内存: 4GB+ (推荐 8GB+)
- 存储: 2GB+ 可用空间
- GPU: 可选，支持 CUDA 加速（推荐）

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/tao-xiaoxin/FastOCR.git
cd FastOCR
```

### 2. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 1. 安装 PaddlePaddle 3.0.0
# CPU 端安装
python -m pip install paddlepaddle==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# GPU 端安装 (Linux 平台，CUDA 11.8 示例)
# python -m pip install paddlepaddle-gpu==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# 2. 安装 PaddleOCR
pip install paddleocr

# 3. 安装项目依赖
pip install -r requirements.txt
```

### 3. 启动服务

```bash
# 开发模式启动
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 生产模式启动
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### 4. 访问服务

- API 文档: http://localhost:8000/docs
- 交互式文档: http://localhost:8000/redoc
- 健康检查: http://localhost:8000/health

## 📚 API 使用示例

### 图片文字识别

```python
import requests

# 上传图片进行 OCR 识别
url = "http://localhost:8000/ocr/recognize"
files = {"file": open("image.jpg", "rb")}
data = {
    "use_angle_cls": True,  # 使用方向分类器
    "lang": "ch",           # 中文识别
    "det_db_thresh": 0.3,   # 检测阈值
    "det_db_box_thresh": 0.5  # 检测框阈值
}
response = requests.post(url, files=files, data=data)

print(response.json())
```

### 批量识别

```python
import requests

# 批量识别多张图片
url = "http://localhost:8000/ocr/batch"
files = [
    ("files", open("image1.jpg", "rb")),
    ("files", open("image2.png", "rb")),
    ("files", open("image3.pdf", "rb"))
]
response = requests.post(url, files=files)

print(response.json())
```

### 获取识别结果详情

```python
import requests

# 获取详细的识别结果，包括文本框位置和置信度
url = "http://localhost:8000/ocr/recognize_detailed"
files = {"file": open("image.jpg", "rb")}
response = requests.post(url, files=files)

result = response.json()
for text_box in result['text_boxes']:
    print(f"文本: {text_box['text']}")
    print(f"置信度: {text_box['confidence']}")
    print(f"位置: {text_box['bbox']}")
```

## 🐳 Docker 部署

### 构建镜像

```bash
docker build -t fastocr .
```

### 运行容器

```bash
# CPU 版本
docker run -d -p 8000:8000 --name fastocr fastocr

# GPU 版本（需要 NVIDIA Docker）
docker run -d -p 8000:8000 --gpus all --name fastocr fastocr:gpu
```

### Docker Compose

```yaml
version: '3.8'
services:
  fastocr:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./uploads:/app/uploads
      - ./models:/app/models  # PaddleOCR 模型缓存
    environment:
      - MAX_FILE_SIZE=10485760
      - ALLOWED_EXTENSIONS=jpg,jpeg,png,pdf
      - USE_GPU=false
      - PADDLE_DEVICE=cpu
```

## 🔧 配置说明

### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `MAX_FILE_SIZE` | `10485760` | 最大文件大小（字节） |
| `ALLOWED_EXTENSIONS` | `jpg,jpeg,png,pdf` | 允许的文件扩展名 |
| `USE_GPU` | `false` | 是否使用 GPU 加速 |
| `PADDLE_DEVICE` | `cpu` | Paddle 设备选择 (cpu/gpu) |
| `LANGUAGE` | `ch` | 识别语言 (ch/en) |
| `USE_ANGLE_CLS` | `true` | 是否使用方向分类器 |

### 配置文件

项目支持通过 `config.yaml` 文件进行详细配置：

```yaml
paddleocr:
  use_angle_cls: true      # 使用方向分类器
  lang: ch                 # 识别语言
  use_gpu: false           # 是否使用 GPU
  gpu_mem: 500             # GPU 显存限制 (MB)
  det_db_thresh: 0.3       # 检测阈值
  det_db_box_thresh: 0.5   # 检测框阈值
  det_db_unclip_ratio: 1.6 # 检测框扩张比例
  rec_char_dict_path: null # 识别字典路径

server:
  host: 0.0.0.0
  port: 8000
  workers: 4

storage:
  upload_dir: ./uploads
  max_file_size: 10485760
  allowed_extensions: [jpg, jpeg, png, pdf]
  model_cache_dir: ./models  # PaddleOCR 模型缓存目录
```

## 📊 性能优化

- **异步处理**: 使用 FastAPI 异步特性提高并发性能
- **模型缓存**: PaddleOCR 模型自动缓存，避免重复下载
- **GPU 加速**: 支持 CUDA 加速，大幅提升识别速度
- **内存优化**: 智能内存管理，支持大图片处理
- **批量处理**: 支持批量图片识别，提高处理效率

## 🔍 监控与日志

- **健康检查**: `/health` 端点提供服务状态监控
- **性能指标**: 集成 Prometheus 指标收集
- **日志记录**: 结构化日志记录，支持 ELK 集成
- **错误追踪**: 详细的错误信息和堆栈跟踪
- **模型状态**: 监控 PaddleOCR 模型加载和使用状态

## 🤝 贡献指南

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 开发环境设置

```bash
# 安装开发依赖
pip install -r requirements-dev.txt

# 安装 PaddlePaddle 3.0.0
python -m pip install paddlepaddle==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# 安装 PaddleOCR
pip install paddleocr

# 运行测试
pytest

# 代码格式化
black .
isort .

# 类型检查
mypy .
```

## 📄 许可证

本项目采用 [Apache License 2.0](LICENSE) 许可证。

## 🙏 致谢

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度飞桨团队开源的优秀 OCR 引擎
- [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速的 Web 框架
- [PaddlePaddle](https://www.paddlepaddle.org.cn/) - 百度深度学习平台
- [OpenCV](https://opencv.org/) - 计算机视觉库
- [Pillow](https://python-pillow.org/) - Python 图像处理库

## 📞 联系我们

- 项目主页: https://github.com/your-username/FastOCR
- 问题反馈: https://github.com/your-username/FastOCR/issues
- 邮箱: your-email@example.com

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！
