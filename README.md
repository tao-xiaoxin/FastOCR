# FastOCR

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.13+-green.svg)](https://fastapi.tiangolo.com/)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-3.1-orange.svg)](https://github.com/PaddlePaddle/PaddleOCR)
[![License](https://img.shields.io/badge/License-Apache%202.0-red.svg)](LICENSE)

## 📖 项目简介

FastOCR 是一个基于 FastAPI 框架和 PaddleOCR 3.1 引擎构建的高性能光学字符识别（OCR）服务。该项目利用百度飞桨团队开源的 PaddleOCR 3.1 技术，提供快速、准确、易用的 OCR 解决方案，支持多种图片格式的文字识别，并提供 RESTful API 接口。

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

## 📁 项目结构

```
FastOCR/
├── fastocr/                     # 主包目录
│   ├── __init__.py
│   ├── core/                    # 核心功能模块
│   │   ├── __init__.py
│   │   ├── document.py          # 文档抽象类
│   │   ├── element.py           # 文档元素（文本、图像、表格等）
│   │   └── pipeline.py          # 处理流水线
│   ├── parsers/                 # 解析器模块
│   │   ├── __init__.py
│   │   ├── pdf_parser.py        # PDF解析器
│   │   ├── image_parser.py      # 图像解析器
│   │   └── base_parser.py       # 解析器基类
│   ├── processors/              # 处理器模块
│   │   ├── __init__.py
│   │   ├── layout_detector.py   # 布局检测
│   │   ├── ocr_processor.py     # OCR处理
│   │   ├── table_extractor.py   # 表格提取
│   │   └── image_extractor.py   # 图像提取
│   ├── models/                  # 模型管理
│   │   ├── __init__.py
│   │   ├── model_manager.py     # 模型管理器
│   │   └── model_configs.py     # 模型配置
│   ├── utils/                   # 工具函数包
│   │   ├── __init__.py
│   │   ├── image/               # 图像处理工具（格式转换、增强、裁剪、编码等）
│   │   │   ├── __init__.py
│   │   │   ├── conversion.py    # 图像格式转换
│   │   │   ├── enhancement.py   # 图像增强处理
│   │   │   ├── cropping.py      # 图像裁剪工具
│   │   │   └── encoding.py      # 图像编码解码
│   │   ├── file/                # 文件操作工具（IO操作、路径处理、压缩等）
│   │   │   ├── __init__.py
│   │   │   ├── io_utils.py      # 文件读写操作
│   │   │   ├── path_utils.py    # 路径处理工具
│   │   │   └── compression.py   # 文件压缩解压
│   │   ├── config/              # 配置管理工具（设置加载、验证、环境变量等）
│   │   │   ├── __init__.py
│   │   │   ├── settings.py      # 配置加载管理
│   │   │   ├── validation.py    # 配置验证
│   │   │   └── environment.py   # 环境变量管理
│   │   ├── validation/          # 数据验证工具（文件验证、图像验证、数据格式验证等）
│   │   │   ├── __init__.py
│   │   │   ├── file_validator.py # 文件类型验证
│   │   │   ├── image_validator.py # 图像格式验证
│   │   │   └── data_validator.py # 数据格式验证
│   │   ├── logger/              # 日志处理工具（配置设置、格式化器、处理器等）
│   │   │   ├── __init__.py
│   │   │   ├── setup.py         # 日志配置设置
│   │   │   ├── formatters.py    # 日志格式化器
│   │   │   └── handlers.py      # 自定义日志处理器
│   │   ├── metrics/             # 性能指标工具（性能测量、准确率计算、监控等）
│   │   │   ├── __init__.py
│   │   │   ├── performance.py   # 性能测量工具
│   │   │   ├── accuracy.py      # 准确率计算
│   │   │   └── monitoring.py    # 监控指标收集
│   │   └── common/              # 通用工具函数（装饰器、异常、常量等）
│   │       ├── __init__.py
│   │       ├── decorators.py    # 装饰器工具
│   │       ├── exceptions.py    # 自定义异常
│   │       └── constants.py     # 常量定义
│   ├── api/                     # API接口
│   │   ├── __init__.py
│   │   ├── rest_api.py          # REST API
│   │   └── client.py            # 客户端
│   └── cli/                     # 命令行接口
│       ├── __init__.py
│       └── main.py              # CLI入口
├── tests/                       # 测试目录
│   ├── __init__.py
│   ├── test_parsers/
│   ├── test_processors/
│   └── test_utils/
├── docs/                        # 文档目录
│   ├── api/
│   ├── examples/
│   └── guides/
├── examples/                    # 示例代码
│   ├── basic_usage.py
│   ├── pdf_processing.py
│   └── batch_processing.py
├── configs/                     # 配置文件
│   ├── default.yaml
│   └── models.yaml
├── scripts/                     # 脚本目录
│   ├── setup_models.py
│   └── benchmark.py
├── requirements/                # 依赖管理
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── setup.py                     # 安装配置
├── README.md
├── LICENSE
├── .gitignore
└── .env.example
```

### 目录说明

- **`fastocr/`**: 主要的Python包，包含所有核心功能
  - **`core/`**: 文档处理的核心抽象和流水线
  - **`parsers/`**: 各种文档格式的解析器（PDF、图像等）
  - **`processors/`**: 具体的处理模块（OCR、布局检测、表格提取等）
  - **`models/`**: 模型管理和配置
  - **`utils/`**: 工具函数包
    - **`image/`**: 图像处理工具（格式转换、增强、裁剪、编码等）
    - **`file/`**: 文件操作工具（IO操作、路径处理、压缩等）
    - **`config/`**: 配置管理工具（设置加载、验证、环境变量等）
    - **`validation/`**: 数据验证工具（文件验证、图像验证、数据格式验证等）
    - **`logger/`**: 日志处理工具（配置设置、格式化器、处理器等）
    - **`metrics/`**: 性能指标工具（性能测量、准确率计算、监控等）
    - **`common/`**: 通用工具函数（装饰器、异常、常量等）
  - **`api/`**: REST API 接口和客户端
  - **`cli/`**: 命令行接口

- **`tests/`**: 完整的测试套件，按模块组织
- **`docs/`**: 项目文档，包括API文档、使用指南等
- **`examples/`**: 使用示例和演示代码
- **`configs/`**: 配置文件模板
- **`scripts/`**: 辅助脚本（模型下载、基准测试等）
- **`requirements/`**: 分环境的依赖管理

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

# 1. 安装 PaddlePaddle 3.1.0
# CPU 端安装
python -m pip install paddlepaddle==3.1.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# GPU 端安装 (Linux 平台，CUDA 11.8 示例)
# python -m pip install paddlepaddle-gpu==3.1.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

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

# 安装 PaddlePaddle 3.1.0
python -m pip install paddlepaddle==3.1.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

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

- 项目主页: https://github.com/tao-xiaoxin/FastOCR
- 问题反馈: https://github.com/tao-xiaoxin/FastOCR/issues
- 邮箱: your-email@example.com

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！
