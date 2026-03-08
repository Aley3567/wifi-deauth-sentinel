# Progress Checklist

> 每次开发前看一眼，接着上次的继续。完成的打 `[x]`。

## Step 0: 项目脚手架 + GitHub 仓库
- [x] 创建目录骨架（firmware / backend / frontend / docs / scripts）
- [x] .gitignore / LICENSE / .env.example
- [x] README.md（项目介绍、架构图、技术栈）
- [x] docker-compose.yml 骨架
- [x] 后端 FastAPI 骨架（main.py / routes / models / services）
- [x] 固件 PlatformIO 骨架
- [x] 前端 package.json + Dockerfile
- [x] CI workflow（.github/workflows/ci.yml）
- [ ] GitHub 仓库创建 + 初始提交推送
- [ ] GitHub Issues 创建（Step 1-8）

## Step 1: ESP32 WiFi 嗅探验证
- [ ] ESP32 固件：开启 WiFi promiscuous mode
- [ ] 捕获 802.11 Deauth 管理帧
- [ ] 串口输出：源 MAC、目标 MAC、RSSI、帧计数
- [ ] 验证：发送 1000 个 Deauth 帧，捕获率 ≥95%

## Step 2: 规则引擎 + MQTT 通信链路
- [ ] ESP32 端滑动窗口规则引擎（5s 窗口，阈值可配）
- [ ] MQTT over TLS：Mosquitto broker 配置
- [ ] ESP32-A → UART → ESP32-B → MQTT 上报链路
- [ ] 后端 FastAPI 接收 MQTT 事件，存入 SQLite
- [ ] 验证：20 次实验，p95 延迟 <2s，TLS 校验成功

## Step 3: LLM 二次研判集成
- [ ] 后端 LLM 集成模块（DeepSeek API）
- [ ] Prompt 工程：安全分析 prompt 设计
- [ ] 灰色地带事件二次研判
- [ ] 自然语言安全报告生成
- [ ] 离线降级：LLM 不可用时降级为模板报告
- [ ] 验证：3 类场景数据集，输出结构化 JSON

## Step 4: Web Dashboard + 实时可视化
- [ ] Vue3 项目初始化（Vite + ECharts）
- [ ] 实时攻击时间线图表
- [ ] 设备状态面板
- [ ] 告警列表 + 详情页
- [ ] WebSocket 实时推送
- [ ] 验证：攻击 → 3s 内弹出告警，LLM 归因 10s 内补全

## Step 5: 对比实验 + 指标采集
- [ ] 自动化攻击脚本（高频/低频/间歇/正常漫游）
- [ ] 隔离测试环境搭建（自建 AP）
- [ ] 数据采集：检测延迟、误报率、漏报率、LLM 归因准确率
- [ ] 对比实验：纯规则引擎 vs 规则引擎+LLM
- [ ] 输出混淆矩阵 + 对比图表
- [ ] 验证：≥100 个带标签样本

## Step 6: 自然语言对话界面
- [ ] 前端对话组件
- [ ] 查询类交互（"今天有攻击吗？"）
- [ ] 配置类交互（白名单映射 + 用户确认）
- [ ] 解读类交互（LLM 上下文分析）
- [ ] Function calling 机制
- [ ] 验证：10 条测试指令，意图识别 ≥90%

## Step 7: Docker 部署 + 告警推送
- [ ] docker-compose 一键启动
- [ ] Telegram Bot / 邮件告警
- [ ] 部署文档
- [ ] 验证：新机器 docker-compose up → 健康检查通过

## Step 8: 论文撰写 + 答辩准备
- [ ] 毕设论文
- [ ] 答辩 PPT
- [ ] 现场演示脚本
- [ ] 验证：10 分钟演示彩排 3 次无阻塞
