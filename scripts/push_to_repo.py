import subprocess
import os

# 配置Git
subprocess.run(["git", "config", "--global", "user.name", "github-actions"])
subprocess.run(["git", "config", "--global", "user.email", "github-actions@github.com"])

# 克隆目标仓库
repo_url = os.getenv('TARGET_REPO_URL')
subprocess.run(["git", "clone", repo_url, "target_repo"])

# 复制生成的 Markdown 文件到目标仓库
subprocess.run(["cp", "output.md", "target_repo/"])

# 提交并推送更改
os.chdir("target_repo")
subprocess.run(["git", "add", "output.md"])
subprocess.run(["git", "commit", "-m", "Update output.md with new data"])
subprocess.run(["git", "push"])
