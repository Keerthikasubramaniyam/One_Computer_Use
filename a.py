import asyncio
from e2b_code_interpreter import Sandbox  # or from e2b import Sandbox
from e2b.sandbox.commands.command_handle import CommandExitException

REPO_URL = "https://github.com/Keerthikasubramaniyam/One_Computer_Use"
REPO_DIR = "One_Computer_Use"
E2B_API_KEY = "your_e2b_api_key_here"
# E2B_API_KEY = "e2b_2ee321a4c089ee3c92a6b4b2"

async def main():
    print("🚀 Starting E2B sandbox...")
    sandbox = Sandbox(api_key=E2B_API_KEY)

    print("🔄 Cloning your repo...")
    sandbox.commands.run(f"git clone {REPO_URL}")
    print("✅ Repo cloned")

    print("📦 Installing requirements...")
    sandbox.commands.run("pip install pytest playwright pytest-playwright")

    print("🌐 Installing Playwright browsers...")
    sandbox.commands.run("playwright install")

    print("📁 Listing all files inside the repo folder:")
    list_result = sandbox.commands.run(f"ls {REPO_DIR}")
    print(list_result.stdout)

    print("🧪 Running pytest on test_playwright.py...")
    try:
        result = sandbox.commands.run(f"cd {REPO_DIR} && pytest test_playwright.py -s")
        print("\n✅ Test Output:\n", result.stdout)
        print("\n🐞 Any Errors:\n", result.stderr)
    except CommandExitException as e:
        print("❌ Test run exited with error (non-zero exit code). Here's the output anyway:\n")
        print("🖨️ STDOUT:\n", e.stdout)
        print("🐛 STDERR:\n", e.stderr)

    print("🧹 Sandbox session ended.")

asyncio.run(main())
