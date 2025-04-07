import asyncio
from e2b.sandbox.base import BaseSandbox  # ✅ NEW import

REPO_URL = "https://github.com/KeerthiSubramaniyam/One_Computer_Use"
REPO_DIR = "One_Computer_Use"
E2B_API_KEY = "e2b_2ee321a4c089ee3c92f42f886b2ce47d9ea6b4b2"  # 🔐 Replace with your actual key

async def main():
    print("🚀 Starting E2B sandbox...")
    sandbox = await BaseSandbox.create(api_key=E2B_API_KEY)

    print("🔄 Cloning your repo...")
    await sandbox.run(f"git clone {REPO_URL}")

    print("📦 Installing pytest and playwright...")
    await sandbox.run("pip install pytest playwright")

    print("🌐 Installing Playwright browsers...")
    await sandbox.run("playwright install")

    print("🧪 Running your test.py...")
    result = await sandbox.run(f"cd {REPO_DIR} && pytest test.py")

    print("\n✅ Test Output:\n")
    print(result.output)

    await sandbox.close()
    print("🧹 Sandbox closed.")

asyncio.run(main())
