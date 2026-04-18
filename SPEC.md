# 小工具站 - 项目规范

## 1. Concept & Vision

一个干净、专业的在线小工具集合站。所有工具均为纯浏览器端运行，无需安装，打开即用。定位：帮助开发者/运营/办公人员提升效率的工具箱。长期运营，持续更新，零成本启动。

## 2. Design Language

- **Aesthetic**: 现代极简工具站，类似 iCase/即时工具风格
- **Colors**:
  - Primary: `#2563eb` (蓝)
  - Secondary: `#1e40af`
  - Accent: `#10b981` (绿)
  - Background: `#f8fafc`
  - Card: `#ffffff`
  - Text: `#1e293b`
  - Muted: `#64748b`
- **Typography**: "PingFang SC", "Microsoft YaHei", system-ui, sans-serif
- **Spacing**: 8px 基准网格
- **Motion**: 卡片 hover 上浮 + 轻微阴影加深，过渡 200ms

## 3. Layout

```
[ Header: Logo + 导航 + 打赏按钮 ]
[ Hero: 一句话价值主张 ]
[ 工具卡片网格: 3列/2列/1列响应式 ]
[ Footer: 版权 + 友链 + 协议 ]
```

## 4. 工具清单 (Phase 1)

| ID | 名称 | 分类 | 功能描述 | 优先级 |
|----|------|------|---------|--------|
| T01 | JSON 美化器 | 开发 | JSON 格式化/压缩/校验 | P0 |
| T02 | 二维码生成器 | 通用 | 支持 Logo 和颜色定制 | P0 |
| T03 | 文件哈希校验 | 开发 | MD5/SHA1/SHA256 | P0 |
| T04 | 颜色转换器 | 设计 | HEX/RGB/HSL 互转 | P1 |
| T05 | URL 编码解码 | 开发 | URL 安全编码 | P1 |
| T06 | Base64 编解码 | 开发 | 文本/文件 Base64 | P1 |

## 5. 变现路径

- Phase 1: 积累流量 + 打赏 (Buy Me a Coffee)
- Phase 2: 会员解锁高级功能 (如大文件处理)
- Phase 3: 广告接入 (Google AdSense)

## 6. 合规

- MIT 开源协议
- 隐私政策（仅统计访问量，无用户数据收集）
- 服务条款
- 无需 ICP 备案（GitHub Pages 海外托管）

## 7. 技术

- 纯 HTML5 + CSS3 + Vanilla JS
- CDN: Tailwind CSS (via CDN), 无需构建
- 图标: Lucide Icons (CDN)
- 部署: GitHub Pages
