# 小工具箱

免费在线工具集合，浏览器端运行，无需安装，完全免费。

## 工具列表

| 工具 | 功能 | 分类 |
|------|------|------|
| JSON 美化器 | 格式化、压缩、校验 JSON | 开发 |
| 二维码生成器 | 生成美化二维码，支持 Logo | 通用 |
| 文件哈希校验 | MD5 / SHA1 / SHA256 | 开发 |
| 颜色转换器 | HEX / RGB / HSL 互转 | 设计 |
| URL 编码解码 | URL 安全编码与解码 | 开发 |
| Base64 编解码 | 文本 Base64 互转 | 开发 |

## 快速开始

### 本地预览

直接双击 `index.html` 用浏览器打开即可运行，无需任何服务器。

或用 VS Code：
```
code .
```
在 VS Code 里安装 "Live Server" 插件，右键 `index.html` → "Open with Live Server"。

### 部署到 GitHub Pages（免费）

1. **创建 GitHub 仓库**
   - 访问 [github.com/new](https://github.com/new)
   - 仓库名：`tools-site`（或你喜欢的名字）
   - 选择 **Public**
   - 不初始化 README

2. **上传文件**
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/你的用户名/tools-site.git
   git push -u origin main
   ```

3. **开启 GitHub Pages**
   - 进入仓库 → Settings → Pages
   - Source 选择 `main` 分支，`/ (root)`
   - 点击 Save

4. **访问你的网站**
   - 等待 2 分钟，访问：`https://你的用户名.github.io/tools-site/`

## 自定义

### 改名
编辑 `index.html`，替换以下内容：
- 标题：`小工具箱` → 你的名字
- 描述文字和链接

### 添加新工具
在 `index.html` 的 `toolMap` 对象和对应的 HTML/JS 代码中按格式添加即可。

### 替换打赏链接
1. 注册 [Buy Me a Coffee](https://www.buymeacoffee.com/)
2. 创建你的收款页面
3. 把 `index.html` 中所有的 `https://www.buymeacoffee.com/` 替换为你的链接

### 添加自定义域名

1. 购买域名（阿里云/腾讯云，.com 年费约 ¥60）
2. GitHub Pages 设置 → Custom domain → 输入你的域名
3. 在你的域名服务商处添加 DNS 记录：
   - 类型 `CNAME`，主机记录 `@`，值 `你的用户名.github.io`
   - 类型 `CNAME`，主机记录 `www`，值 `你的用户名.github.io`

## 合规

- MIT 开源协议
- 隐私政策：`privacy.html`
- 服务条款：`terms.html`
- 无需 ICP 备案（GitHub Pages 海外托管）
