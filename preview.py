#!/usr/bin/env python3
"""
平安健康险技能市场本地预览服务器
运行此脚本后，在浏览器中访问 http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
import sys

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 设置正确的MIME类型
        if self.path.endswith('.css'):
            self.send_header('Content-Type', 'text/css')
        elif self.path.endswith('.js'):
            self.send_header('Content-Type', 'application/javascript')
        elif self.path.endswith('.html'):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 60)
    print("平安健康险技能市场 - 本地预览服务器")
    print("=" * 60)
    print(f"服务器运行在: http://localhost:{PORT}")
    print("")
    print("可用页面:")
    print("  1. 前台首页: http://localhost:8000/index.html")
    print("  2. 后台管理: http://localhost:8000/admin.html")
    print("  3. 技能详情: http://localhost:8000/skill-detail.html")
    print("")
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)
    
    # 自动打开首页
    try:
        webbrowser.open(f'http://localhost:{PORT}/index.html')
    except:
        pass
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"服务器已启动，正在监听端口 {PORT}...")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"错误：端口 {PORT} 已被占用")
            print("请关闭占用该端口的程序，或修改脚本中的PORT变量")
        else:
            raise

if __name__ == "__main__":
    main()