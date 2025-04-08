# import asyncio
# from e2b.sandbox.base import BaseSandbox

# REPO_URL = "https://github.com/KeerthiSubramaniyam/One_Computer_Use"
# REPO_DIR = "One_Computer_Use"
# E2B_API_KEY = "e2b_2ee321a4c089ee3c92f42f886b2ce47d9ea6b4b2"  # 🔐 Replace with your actual key

# async def main():
#     print("🚀 Starting E2B sandbox...")
#     sandbox = await BaseSandbox.create(api_key=E2B_API_KEY)

#     print("🔄 Cloning your repo...")
#     await sandbox.run(f"git clone {REPO_URL}")

#     print("📦 Installing pytest and playwright...")
#     await sandbox.run("pip install pytest playwright")

#     print("🌐 Installing Playwright browsers...")
#     await sandbox.run("playwright install")

#     print("🧪 Running your test.py...")
#     result = await sandbox.run(f"cd {REPO_DIR} && pytest test.py")

#     print("\n✅ Test Output:\n")
#     print(result.output)

#     await sandbox.close()
#     print("🧹 Sandbox closed.")

# asyncio.run(main())


import asyncio
from e2b import Sandbox

REPO_URL = "https://github.com/Keerthikasubramaniyam/One_Computer_Use"
REPO_DIR = "One_Computer_Use"
E2B_API_KEY = "e2b_2ee321a4c089ee3c92f42f886b2ce47d9ea6b4b2"  # Replace with your actual key

async def main():
    print("🚀 Starting E2B sandbox...")
    sandbox = Sandbox(api_key=E2B_API_KEY)

    print("🔄 Cloning your repo...")
    sandbox.commands.run(f"git clone {REPO_URL}")
    print("🔄 cloned your repo...")

    print("📦 Installing pytest and playwright...")
    sandbox.commands.run("pip install pytest playwright")
    version_result= sandbox.commands.run("pytest --version")
    print(version_result.stdout)


    print("🌐 Installing Playwright browsers...")
    sandbox.commands.run("playwright install")

    print("🧪 Running your test.py...")
    result = sandbox.commands.run(f"cd {REPO_DIR} && pytest playwright.py -s")
    print("🧪 Completed your test.py...")

    print("\n✅ Test Output:\n")
    print(result.stdout)

    print("\n🐞 Any Errors:\n")
    print(result.stderr)

    # await sandbox.shutdown()  
    print("🧹 Sandbox closed.")

asyncio.run(main())
