# to run the code in E2B CLOUD :
# pip install e2b
# Steps how to run this code:
# Starts an E2B remote sandbox session (a Linux virtual environment in the cloud).
# Clones your GitHub repo inside the sandbox.
# Installs Python dependencies required to:
# Installs Chromium, Firefox, and WebKit in the sandbox.
# Lists the contents of your cloned GitHub repo.
# This runs your test file using python directly.
# Prints the output and error logs from running the test file.
# Marks the end of your sandbox session.

import asyncio
from e2b_code_interpreter import Sandbox  # Adjusted import based on your environment
# from e2b import Sandbox
from e2b.sandbox.commands.command_handle import CommandExitException


REPO_URL = "https://github.com/Keerthikasubramaniyam/One_Computer_Use"
REPO_DIR = "One_Computer_Use"
E2B_API_KEY = "your_e2b_api_key_here"  # Replace with your actual key

async def main():
    print("🚀 Starting E2B sandbox...")
    sandbox = Sandbox(api_key=E2B_API_KEY)

    print("🔄 Cloning your repo...")
    sandbox.commands.run(f"git clone {REPO_URL}")
    print("✅ Repo cloned")

    print("📦 Installing pytest, playwright, and pytest-playwright...")
    sandbox.commands.run("pip install pytest playwright pytest-playwright")

    print("🌐 Installing Playwright browsers...")
    sandbox.commands.run("playwright install")

    print("📂 Navigating into repo directory...")
    sandbox.commands.run(f"cd {REPO_DIR}")

    print("📁 Listing all files and folders inside the repo:")
    list_files_result = sandbox.commands.run(f"ls {REPO_DIR}")
    print(list_files_result.stdout)
# 
    print("🧪 Running pytest on test_playwright.py...")
    # result = sandbox.commands.run(f"pytest test_playwright.py -s")
    result = sandbox.commands.run(f"cd {REPO_DIR} && python test_playwright.py")

    print("\n✅ Test Output:\n")
    print(result.stdout)

    print("\n🐞 Any Errors:\n")
    print(result.stderr)

    # await sandbox.shutdown()  # optional: cleanup
    print("🧹 Sandbox session ended.")

asyncio.run(main())

