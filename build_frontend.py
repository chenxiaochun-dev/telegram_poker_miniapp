import os
import shutil
import subprocess

def build_and_copy_frontend():
    frontend_dir = "frontend"
    backend_frontend_build = os.path.join("backend", "frontend", "build")
    local_build_dir = os.path.join(frontend_dir, "build")

    print("开始构建前端项目...")

    # 指定 npm.cmd 绝对路径
    npm_path = r"C:\Program Files\nodejs\npm.cmd"

    subprocess.run([npm_path, "run", "build"], cwd=frontend_dir, check=True)

    if os.path.exists(backend_frontend_build):
        print("删除旧的后端 frontend build 文件夹...")
        shutil.rmtree(backend_frontend_build)

    print(f"复制 {local_build_dir} 到 {backend_frontend_build} ...")
    shutil.copytree(local_build_dir, backend_frontend_build)

    print("前端构建并复制完成。")

if __name__ == "__main__":
    try:
        build_and_copy_frontend()
    except subprocess.CalledProcessError:
        print("前端构建失败，请检查 npm 错误信息。")
