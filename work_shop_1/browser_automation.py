import asyncio
from playwright.async_api import async_playwright

async def main():
    # Launch the Playwright browser in headful (visible) mode
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch Chromium in headful mode

        # Create a new browser context
        context = await browser.new_context()

        # Create a new page within the context
        page = await context.new_page()

        try:
            # Navigate to Google
            await page.goto('https://www.google.com')

            # Type "Winston Zeng" into the search input and press Enter
            await page.type('textarea[name="q"]', 'Winston ZENG')
            await page.press('textarea[name="q"]', 'Enter')

            # Wait for search results to load
            await page.wait_for_load_state('networkidle')

            # Click the first search result link
            link = await page.query_selector('a > h3:has-text("Winston ZENG")')
            
            if link:
                await link.click()

            # Wait for the new page to load
            await page.wait_for_load_state('networkidle')

            # Take a screenshot of the page
            # await page.screenshot(path='capsenlu_profile.png')
            # await page.screenshot()

            # Keep the browser open for visual inspection
            input("Press Enter to close the browser...")

        finally:
            # Close the browser
            await browser.close()

# Run the main function asynchronously
asyncio.run(main())