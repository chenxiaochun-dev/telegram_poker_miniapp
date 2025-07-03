@echo off
setlocal enabledelayedexpansion

:: === 项目自动部署脚本：前端 + Flask 后端 + Heroku ===

:: Step 1: 构建前端
echo [1/4] 正在构建 React 前端...
cd frontend
if exist build (
    rmdir /s /q build
)
call npm install
call npm run build
if %errorlevel% neq 0 (
    echo ❌ 前端构建失败！
    pause
    exit /b 1
)
cd ..

:: Step 2: 拷贝构建产物到 backend/frontend
echo [2/4] 拷贝构建产物到 backend/frontend...
if exist backend\frontend (
    rmdir /s /q backend\frontend
)
mkdir backend\frontend
xcopy /E /Y /Q frontend\build\* backend\frontend\

:: Step 3: Git 提交更新
echo [3/4] 提交 Git 变更...
cd backend
git add .
git commit -m "自动部署：构建前端并更新 Heroku"
if %errorlevel% neq 0 (
    echo ⚠️ 没有新的更改可提交。
)

:: Step 4: 推送到 Heroku
echo [4/4] 推送到 Heroku...
git push heroku master
if %errorlevel% neq 0 (
    echo ❌ 推送 Heroku 失败，请检查错误。
    pause
    exit /b 1
)
cd ..

:: === 部署完成，打开浏览器 ===
echo ✅ 部署成功！正在打开浏览器...
start https://telegram-poker-miniapp.herokuapp.com/

pause
