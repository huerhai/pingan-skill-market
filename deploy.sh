#!/bin/bash

# 平安健康险技能市场部署脚本

echo "=== 平安健康险技能市场部署脚本 ==="
echo ""

# 检查是否在项目根目录
if [ ! -f "index.html" ]; then
    echo "错误：请在项目根目录运行此脚本"
    exit 1
fi

echo "1. 检查Git状态..."
git status

echo ""
echo "2. 创建GitHub Pages部署分支..."
git checkout -b gh-pages 2>/dev/null || git checkout gh-pages

echo ""
echo "3. 添加所有文件..."
git add .

echo ""
echo "4. 提交更改..."
git commit -m "部署到GitHub Pages - $(date '+%Y-%m-%d %H:%M:%S')"

echo ""
echo "5. 推送到GitHub..."
echo "请确保已经设置了GitHub远程仓库："
echo "  git remote add origin https://github.com/你的用户名/pingan-skill-market.git"
echo ""
echo "然后运行："
echo "  git push -u origin gh-pages"
echo ""
echo "6. 在GitHub仓库设置中："
echo "   Settings → Pages → Branch: gh-pages → / (root) → Save"
echo ""
echo "部署完成后，网站将在以下地址访问："
echo "  https://你的用户名.github.io/pingan-skill-market/"
echo ""
echo "=== 部署说明完成 ==="